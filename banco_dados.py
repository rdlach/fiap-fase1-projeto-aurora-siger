"""Funções para salvar as execuções da missão em um banco PostgreSQL."""

import os
from datetime import datetime


def obter_configuracao_postgres():
    return {
        "host": os.getenv("POSTGRES_HOST", "localhost"),
        "port": os.getenv("POSTGRES_PORT", "5432"),
        "dbname": os.getenv("POSTGRES_DB", "aurora_siger"),
        "user": os.getenv("POSTGRES_USER", "postgres"),
        "password": os.getenv("POSTGRES_PASSWORD", "postgres"),
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
                CREATE TABLE IF NOT EXISTS execucoes_pre_decolagem (
                    id SERIAL PRIMARY KEY,
                    data_hora TIMESTAMP NOT NULL,
                    origem_dados VARCHAR(80) NOT NULL,
                    temperatura_interna_c NUMERIC(8, 2) NOT NULL,
                    temperatura_externa_c NUMERIC(8, 2) NOT NULL,
                    integridade_estrutural INTEGER NOT NULL,
                    nivel_energia_percentual NUMERIC(8, 2) NOT NULL,
                    pressao_tanques_percentual NUMERIC(8, 2) NOT NULL,
                    modulos_criticos VARCHAR(20) NOT NULL,
                    energia_disponivel_kwh NUMERIC(10, 2) NOT NULL,
                    perdas_kwh NUMERIC(10, 2) NOT NULL,
                    energia_restante_kwh NUMERIC(10, 2) NOT NULL,
                    autonomia_horas NUMERIC(10, 2) NOT NULL,
                    decisao_final VARCHAR(40) NOT NULL
                )
                """
            )


def salvar_execucao(telemetria, resultado_energia, decisao_final, origem_dados):
    criar_tabela_execucoes()

    with conectar_postgres() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO execucoes_pre_decolagem (
                    data_hora,
                    origem_dados,
                    temperatura_interna_c,
                    temperatura_externa_c,
                    integridade_estrutural,
                    nivel_energia_percentual,
                    pressao_tanques_percentual,
                    modulos_criticos,
                    energia_disponivel_kwh,
                    perdas_kwh,
                    energia_restante_kwh,
                    autonomia_horas,
                    decisao_final
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    datetime.now(),
                    origem_dados,
                    telemetria["temperatura_interna_c"],
                    telemetria["temperatura_externa_c"],
                    telemetria["integridade_estrutural"],
                    telemetria["nivel_energia_percentual"],
                    telemetria["pressao_tanques_percentual"],
                    telemetria["modulos_criticos"],
                    resultado_energia["energia_disponivel_kwh"],
                    resultado_energia["perdas_kwh"],
                    resultado_energia["energia_restante_kwh"],
                    resultado_energia["autonomia_horas"],
                    decisao_final,
                ),
            )

            id_execucao = cursor.fetchone()[0]

    return id_execucao
