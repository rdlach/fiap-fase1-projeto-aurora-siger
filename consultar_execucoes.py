"""Consulta as últimas execuções salvas no banco PostgreSQL."""

from banco_dados import listar_execucoes


try:
    execucoes = listar_execucoes()

    if not execucoes:
        print("Nenhuma execução foi salva ainda.")
    else:
        print("Últimos cenários de decolagem salvos")
        print("-" * 80)

        for execucao in execucoes:
            (
                id_execucao,
                data_inicio,
                cenario,
                status,
                motivo_aborto,
                leituras,
                energia_minima,
                energia_maxima,
            ) = execucao

            print(f"ID: {id_execucao}")
            print(f"Início: {data_inicio}")
            print(f"Cenário: {cenario}")
            print(f"Status: {status}")
            print(f"Leituras de telemetria: {leituras}")
            if energia_minima is not None and energia_maxima is not None:
                print(f"Energia registrada: {energia_minima:.2f}% a {energia_maxima:.2f}%")
            if motivo_aborto:
                print(f"Motivo do aborto: {motivo_aborto}")
            print("-" * 80)
except Exception as erro:
    print("Não foi possível consultar o banco PostgreSQL.")
    print(f"Motivo: {erro}")
