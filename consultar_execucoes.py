"""Consulta as últimas execuções salvas no banco PostgreSQL."""

from banco_dados import conectar_postgres, criar_tabela_execucoes


try:
    criar_tabela_execucoes()

    with conectar_postgres() as conexao:
        with conexao.cursor() as cursor:
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

    if not execucoes:
        print("Nenhuma execução foi salva ainda.")
    else:
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
except Exception as erro:
    print("Não foi possível consultar o banco PostgreSQL.")
    print(f"Motivo: {erro}")
