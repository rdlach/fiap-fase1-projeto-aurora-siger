"""Versão interativa da simulação de pré-decolagem da Aurora Siger."""

from banco_dados import salvar_cenario_decolagem
from simulacao_decolagem import (
    CENARIOS_DISPONIVEIS,
    analisar_cenario,
    converter_para_telemetria_resumida,
    gerar_telemetria_cenario,
)


def mostrar_titulo(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def mostrar_linha():
    print("-" * 60)


def ler_opcao():
    while True:
        print("\nEscolha um cenário de pré-decolagem:")
        for opcao, cenario in CENARIOS_DISPONIVEIS.items():
            print(f"{opcao} - {cenario}")

        opcao = input("Opção escolhida: ").strip()

        if opcao in CENARIOS_DISPONIVEIS:
            return CENARIOS_DISPONIVEIS[opcao]

        print("Opção inválida. Digite um dos números listados.")


def calcular_energia(telemetria):
    capacidade_total_kwh = 1200
    consumo_decolagem_kwh = 260
    perdas_percentual = 6
    consumo_operacional_kw = 85

    carga_atual_percentual = telemetria["nivel_energia_percentual"]
    energia_disponivel_kwh = capacidade_total_kwh * (carga_atual_percentual / 100)
    perdas_kwh = energia_disponivel_kwh * (perdas_percentual / 100)
    energia_restante_kwh = energia_disponivel_kwh - consumo_decolagem_kwh - perdas_kwh
    autonomia_horas = energia_restante_kwh / consumo_operacional_kw
    energia_suficiente = energia_restante_kwh > 0 and autonomia_horas > 0

    return {
        "Energia após decolagem": energia_suficiente,
        "energia_disponivel_kwh": energia_disponivel_kwh,
        "perdas_kwh": perdas_kwh,
        "energia_restante_kwh": energia_restante_kwh,
        "autonomia_horas": max(0, autonomia_horas),
    }


def mostrar_telemetria_final(telemetria):
    mostrar_titulo("TELEMETRIA FINAL DA SIMULAÇÃO")
    for dado, valor in telemetria.items():
        print(f"{dado}: {valor}")


def mostrar_resumo_temporal(analise):
    leituras = analise["leituras"]
    primeira = leituras[0]
    ultima = leituras[-1]

    mostrar_titulo("RESUMO TEMPORAL")
    print(f"Cenário: {analise['cenario']}")
    print(f"Leituras geradas: {len(leituras)}")
    print(f"Tempo inicial: T+{primeira['tempo_decolagem']}s")
    print(f"Tempo final: T+{ultima['tempo_decolagem']}s")
    if analise["falhas_persistentes"]:
        print("Contagem interrompida: falha por 6 leituras consecutivas.")
        print(f"Falha persistente: {', '.join(analise['falhas_persistentes'])}")
    print(f"Energia inicial: {primeira['nivel_energia']:.2f}%")
    print(f"Energia final: {ultima['nivel_energia']:.2f}%")
    print(f"Pressão LOX final: {ultima['pressao_lox_psi']:.2f} psi")
    print(f"Sistema elétrico final: {'OK' if ultima['sistema_eletrico_ok'] else 'FALHA'}")

    if analise["alertas_corrigidos"]:
        print("\nAlertas normalizados durante a contagem:")
        for tempo, item in analise["alertas_corrigidos"][:5]:
            print(f"- T+{tempo}s: {item}")
        if len(analise["alertas_corrigidos"]) > 5:
            print(f"- mais {len(analise['alertas_corrigidos']) - 5} alerta(s) normalizado(s)")
    else:
        print("\nNenhum alerta intermediário foi normalizado.")


def mostrar_resultado_verificacoes(verificacoes, titulo):
    mostrar_titulo(titulo)
    for item, aprovado in verificacoes.items():
        status = "OK" if aprovado else "FALHA"
        print(f"{item}: {status}")


def mostrar_analise_energetica(resultado_energia):
    mostrar_titulo("ANÁLISE ENERGÉTICA")
    print(f"Energia disponível: {resultado_energia['energia_disponivel_kwh']:.2f} kWh")
    print(f"Perdas energéticas: {resultado_energia['perdas_kwh']:.2f} kWh")
    print(f"Energia restante após decolagem: {resultado_energia['energia_restante_kwh']:.2f} kWh")
    print(f"Autonomia inicial estimada: {resultado_energia['autonomia_horas']:.2f} horas")


def decidir_status(analise, resultado_energia):
    verificacoes = analise["verificacoes_finais"].copy()
    verificacoes["Energia após decolagem"] = resultado_energia["Energia após decolagem"]
    falhas = [item for item, aprovado in verificacoes.items() if not aprovado]

    if falhas or analise["falhas_persistentes"]:
        return "DECOLAGEM ABORTADA", ", ".join(falhas), verificacoes

    return "PRONTO PARA DECOLAR", None, verificacoes


def mostrar_decisao_final(status, motivo_aborto):
    mostrar_titulo("DECISÃO FINAL")
    print(status)

    if motivo_aborto:
        print("\nMotivos identificados:")
        for motivo in motivo_aborto.split(", "):
            print(f"- {motivo}")


def executar_simulacao(cenario):
    leituras = gerar_telemetria_cenario(cenario)
    analise = analisar_cenario(cenario, leituras)
    telemetria_final = converter_para_telemetria_resumida(analise["telemetria_final"])
    resultado_energia = calcular_energia(telemetria_final)
    status, motivo_aborto, verificacoes = decidir_status(analise, resultado_energia)

    mostrar_resumo_temporal(analise)
    mostrar_telemetria_final(telemetria_final)
    mostrar_resultado_verificacoes(verificacoes, "VERIFICAÇÕES FINAIS DA PRÉ-DECOLAGEM")
    mostrar_analise_energetica(resultado_energia)
    mostrar_linha()
    mostrar_decisao_final(status, motivo_aborto)

    try:
        id_execucao = salvar_cenario_decolagem(cenario, leituras, status, motivo_aborto)
        print(f"\nCenário salvo no banco PostgreSQL com o ID {id_execucao}.")
    except Exception as erro:
        print("\nNão foi possível salvar o cenário no PostgreSQL.")
        print(f"Motivo: {erro}")


def main():
    mostrar_titulo("AURORA SIGER - SISTEMA DE PRÉ-DECOLAGEM")
    cenario = ler_opcao()
    executar_simulacao(cenario)


if __name__ == "__main__":
    main()
