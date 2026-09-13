"""Consulta as últimas execuções salvas no banco SQLite."""

import sqlite3
from pathlib import Path


CAMINHO_BANCO = Path("aurora_siger_execucoes.db")


if not CAMINHO_BANCO.exists():
    print("Nenhuma execução foi salva ainda.")
else:
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT
            id,
            data_hora,
            origem_dados,
            nivel_energia_percentual,
            energia_restante_kwh,
            autonomia_horas,
            decisao_final
        FROM execucoes_pre_decolagem
        ORDER BY id DESC
        LIMIT 10
        """
    )

    execucoes = cursor.fetchall()
    conexao.close()

    print("Últimas execuções salvas")
    print("-" * 80)

    for execucao in execucoes:
        (
            id_execucao,
            data_hora,
            origem_dados,
            nivel_energia,
            energia_restante,
            autonomia,
            decisao_final,
        ) = execucao

        print(f"ID: {id_execucao}")
        print(f"Data/hora: {data_hora}")
        print(f"Origem dos dados: {origem_dados}")
        print(f"Nível de energia: {nivel_energia}%")
        print(f"Energia restante: {energia_restante:.2f} kWh")
        print(f"Autonomia: {autonomia:.2f} horas")
        print(f"Decisão final: {decisao_final}")
        print("-" * 80)
