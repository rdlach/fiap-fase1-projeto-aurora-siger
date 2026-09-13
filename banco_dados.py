"""Funções para salvar as execuções da missão em um banco SQLite."""

import sqlite3
from datetime import datetime
from pathlib import Path


CAMINHO_BANCO = Path("aurora_siger_execucoes.db")


def criar_tabela_execucoes():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS execucoes_pre_decolagem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL,
            origem_dados TEXT NOT NULL,
            temperatura_interna_c REAL NOT NULL,
            temperatura_externa_c REAL NOT NULL,
            integridade_estrutural INTEGER NOT NULL,
            nivel_energia_percentual REAL NOT NULL,
            pressao_tanques_percentual REAL NOT NULL,
            modulos_criticos TEXT NOT NULL,
            energia_disponivel_kwh REAL NOT NULL,
            perdas_kwh REAL NOT NULL,
            energia_restante_kwh REAL NOT NULL,
            autonomia_horas REAL NOT NULL,
            decisao_final TEXT NOT NULL
        )
        """
    )

    conexao.commit()
    conexao.close()


def salvar_execucao(telemetria, resultado_energia, decisao_final, origem_dados):
    criar_tabela_execucoes()

    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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

    id_execucao = cursor.lastrowid
    conexao.commit()
    conexao.close()

    return id_execucao
