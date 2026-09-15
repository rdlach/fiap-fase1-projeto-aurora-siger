"""Funções para salvar e consultar cenários da missão em PostgreSQL."""

import os
from getpass import getuser
from datetime import datetime, timedelta

from simulacao_decolagem import PARAMETROS_SEGURANCA


UNIDADES_PARAMETROS = {
    "temperatura_interna": "C",
    "temperatura_externa": "C",
    "vibracao_estrutural_g": "g RMS",
    "nivel_energia": "%",
    "pressao_lh2_psi": "psi",
    "pressao_lox_psi": "psi",
}

PARAMETROS_PADRAO = [
    (
        parametro,
        UNIDADES_PARAMETROS[parametro],
        valores[0],
        valores[1],
    )
    for parametro, valores in PARAMETROS_SEGURANCA.items()
]


def obter_configuracao_postgres():
    return {
        "host": os.getenv("POSTGRES_HOST", "localhost"),
        "port": os.getenv("POSTGRES_PORT", "5432"),
        "dbname": os.getenv("POSTGRES_DB", "aurora_siger"),
        "user": os.getenv("POSTGRES_USER", getuser()),
        "password": os.getenv("POSTGRES_PASSWORD", ""),
    }


def conectar_postgres():
    try:
        import psycopg
    except ImportError as erro:
        raise RuntimeError(
            "Driver do PostgreSQL não encontrado. "
            "Instale com: pip install -r requirements.txt"
        ) from erro

    return psycopg.connect(**obter_configuracao_postgres())


def criar_tabela_execucoes():
    with conectar_postgres() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS decolagem (
                    id SERIAL PRIMARY KEY,
                    data_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    data_fim TIMESTAMP,
                    cenario VARCHAR(30),
                    status VARCHAR(30),
                    motivo_aborto VARCHAR(200)
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS parametros_seguranca (
                    id SERIAL PRIMARY KEY,
                    parametro VARCHAR(50) NOT NULL UNIQUE,
                    unidade VARCHAR(20),
                    valor_minimo NUMERIC(8, 3),
                    valor_maximo NUMERIC(8, 3)
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS telemetria (
                    id SERIAL PRIMARY KEY,
                    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    tempo_decolagem INTEGER,
                    temperatura_interna NUMERIC(6, 2),
                    temperatura_externa NUMERIC(6, 2),
                    integridade_estrutural_ok BOOLEAN,
                    vibracao_estrutural_g NUMERIC(6, 3),
                    nivel_energia NUMERIC(6, 2),
                    pressao_lh2_psi NUMERIC(6, 2),
                    pressao_lox_psi NUMERIC(6, 2),
                    motor_ok BOOLEAN,
                    navegacao_ok BOOLEAN,
                    comunicacao_ok BOOLEAN,
                    sistema_eletrico_ok BOOLEAN,
                    resfriamento_ativo BOOLEAN,
                    pressurizacao_ativa BOOLEAN,
                    decolagem_id INTEGER REFERENCES decolagem(id)
                )
                """
            )
            cursor.executemany(
                """
                INSERT INTO parametros_seguranca (
                    parametro,
                    unidade,
                    valor_minimo,
                    valor_maximo
                )
                SELECT %s, %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1
                    FROM parametros_seguranca
                    WHERE parametro = %s
                )
                """,
                [
                    (parametro, unidade, minimo, maximo, parametro)
                    for parametro, unidade, minimo, maximo in PARAMETROS_PADRAO
                ],
            )


def _limitar_texto(texto, limite):
    return str(texto)[:limite]


def _modulos_criticos_ok(telemetria):
    return telemetria.get("modulos_criticos", "OK") == "OK"


def _motivo_aborto(decisao_final):
    if decisao_final == "PRONTO PARA DECOLAR":
        return None

    return "Falha identificada nas verificações da missão"


def salvar_cenario_decolagem(cenario, leituras, status, motivo_aborto=None):
    criar_tabela_execucoes()
    data_execucao = datetime.now()
    data_fim = data_execucao + timedelta(seconds=leituras[-1]["tempo_decolagem"])

    with conectar_postgres() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO decolagem (
                    data_inicio,
                    data_fim,
                    cenario,
                    status,
                    motivo_aborto
                )
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    data_execucao,
                    data_fim,
                    _limitar_texto(cenario, 30),
                    status,
                    motivo_aborto,
                ),
            )
            id_decolagem = cursor.fetchone()[0]

            cursor.executemany(
                """
                INSERT INTO telemetria (
                    data_hora,
                    tempo_decolagem,
                    temperatura_interna,
                    temperatura_externa,
                    integridade_estrutural_ok,
                    vibracao_estrutural_g,
                    nivel_energia,
                    pressao_lh2_psi,
                    pressao_lox_psi,
                    motor_ok,
                    navegacao_ok,
                    comunicacao_ok,
                    sistema_eletrico_ok,
                    resfriamento_ativo,
                    pressurizacao_ativa,
                    decolagem_id
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                [
                    (
                        data_execucao + timedelta(seconds=leitura["tempo_decolagem"]),
                        leitura["tempo_decolagem"],
                        leitura["temperatura_interna"],
                        leitura["temperatura_externa"],
                        leitura["integridade_estrutural_ok"],
                        leitura["vibracao_estrutural_g"],
                        leitura["nivel_energia"],
                        leitura["pressao_lh2_psi"],
                        leitura["pressao_lox_psi"],
                        leitura["motor_ok"],
                        leitura["navegacao_ok"],
                        leitura["comunicacao_ok"],
                        leitura["sistema_eletrico_ok"],
                        leitura["resfriamento_ativo"],
                        leitura["pressurizacao_ativa"],
                        id_decolagem,
                    )
                    for leitura in leituras
                ],
            )

    return id_decolagem


def salvar_execucao(telemetria, resultado_energia, decisao_final, origem_dados):
    criar_tabela_execucoes()
    data_execucao = datetime.now()
    modulos_ok = _modulos_criticos_ok(telemetria)
    pressao_media_tanques = telemetria.get("pressao_media_tanques_psi")
    if pressao_media_tanques is None:
        pressao_media_tanques = (
            telemetria["pressao_lh2_psi"] + telemetria["pressao_lox_psi"]
        ) / 2

    with conectar_postgres() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO decolagem (
                    data_inicio,
                    data_fim,
                    cenario,
                    status,
                    motivo_aborto
                )
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    data_execucao,
                    data_execucao,
                    _limitar_texto(origem_dados, 30),
                    decisao_final,
                    _motivo_aborto(decisao_final),
                ),
            )
            id_execucao = cursor.fetchone()[0]

            cursor.execute(
                """
                INSERT INTO telemetria (
                    data_hora,
                    tempo_decolagem,
                    temperatura_interna,
                    temperatura_externa,
                    integridade_estrutural_ok,
                    vibracao_estrutural_g,
                    nivel_energia,
                    pressao_lh2_psi,
                    pressao_lox_psi,
                    motor_ok,
                    navegacao_ok,
                    comunicacao_ok,
                    sistema_eletrico_ok,
                    resfriamento_ativo,
                    pressurizacao_ativa,
                    decolagem_id
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    data_execucao,
                    0,
                    telemetria["temperatura_interna_c"],
                    telemetria["temperatura_externa_c"],
                    telemetria["integridade_estrutural"] == 1,
                    telemetria.get("vibracao_estrutural_g", 0),
                    telemetria["nivel_energia_percentual"],
                    telemetria.get("pressao_lh2_psi", pressao_media_tanques),
                    telemetria.get("pressao_lox_psi", pressao_media_tanques),
                    telemetria.get("motor_ok", modulos_ok),
                    telemetria.get("navegacao_ok", modulos_ok),
                    telemetria.get("comunicacao_ok", modulos_ok),
                    telemetria.get("sistema_eletrico_ok", modulos_ok),
                    telemetria.get("resfriamento_ativo", False),
                    telemetria.get("pressurizacao_ativa", False),
                    id_execucao,
                ),
            )

    return id_execucao


def listar_execucoes(limite=10):
    criar_tabela_execucoes()

    with conectar_postgres() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    d.id,
                    d.data_inicio,
                    d.cenario,
                    d.status,
                    d.motivo_aborto,
                    COUNT(t.id) AS leituras,
                    MIN(t.nivel_energia) AS energia_minima,
                    MAX(t.nivel_energia) AS energia_maxima
                FROM decolagem d
                LEFT JOIN telemetria t ON t.decolagem_id = d.id
                GROUP BY d.id
                ORDER BY d.id DESC
                LIMIT %s
                """,
                (limite,),
            )

            return cursor.fetchall()
