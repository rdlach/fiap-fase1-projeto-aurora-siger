"""Versão interativa da simulação de pré-decolagem da Aurora Siger."""

import random


def ler_float(mensagem, valor_padrao):
    entrada = input(f"{mensagem} [{valor_padrao}]: ").strip()

    if entrada == "":
        return float(valor_padrao)

    return float(entrada.replace(",", "."))


def ler_opcao():
    while True:
        print("\nEscolha como deseja carregar a telemetria:")
        print("1 - Usar preset seguro")
        print("2 - Gerar dados randômicos")

        opcao = input("Opção escolhida: ").strip()

        if opcao in ("1", "2"):
            return opcao

        print("Opção inválida. Digite 1 ou 2.")


def mostrar_titulo(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def mostrar_linha():
    print("-" * 60)


def gerar_preset():
    return {
        "temperatura_interna_c": 24,
        "temperatura_externa_c": -18,
        "integridade_estrutural": 1,
        "nivel_energia_percentual": 87,
        "pressao_tanques_percentual": 95,
        "modulos_criticos": "OK",
    }


def gerar_dados_randomicos():
    status_modulos = ["OK", "OK", "OK", "FALHA"]

    return {
        "temperatura_interna_c": round(random.uniform(10, 45), 1),
        "temperatura_externa_c": round(random.uniform(-70, 75), 1),
        "integridade_estrutural": random.choice([1, 1, 1, 0]),
        "nivel_energia_percentual": round(random.uniform(40, 100), 1),
        "pressao_tanques_percentual": round(random.uniform(60, 130), 1),
        "modulos_criticos": random.choice(status_modulos),
    }


def verificar_telemetria(telemetria, faixas_seguras):
    temperatura_interna_ok = (
        faixas_seguras["temperatura_interna_min"]
        <= telemetria["temperatura_interna_c"]
        <= faixas_seguras["temperatura_interna_max"]
    )
    temperatura_externa_ok = (
        faixas_seguras["temperatura_externa_min"]
        <= telemetria["temperatura_externa_c"]
        <= faixas_seguras["temperatura_externa_max"]
    )
    integridade_ok = telemetria["integridade_estrutural"] == 1
    energia_ok = telemetria["nivel_energia_percentual"] >= faixas_seguras["nivel_energia_min"]
    pressao_ok = (
        faixas_seguras["pressao_tanques_min"]
        <= telemetria["pressao_tanques_percentual"]
        <= faixas_seguras["pressao_tanques_max"]
    )
    modulos_ok = telemetria["modulos_criticos"] == "OK"

    return {
        "Temperatura interna": temperatura_interna_ok,
        "Temperatura externa": temperatura_externa_ok,
        "Integridade estrutural": integridade_ok,
        "Nível de energia": energia_ok,
        "Pressão dos tanques": pressao_ok,
        "Módulos críticos": modulos_ok,
    }


def calcular_energia(telemetria):
    capacidade_total_kwh = ler_float("\nCapacidade total da nave em kWh", 1200)
    consumo_decolagem_kwh = ler_float("Consumo estimado na decolagem em kWh", 260)
    perdas_percentual = ler_float("Perdas energéticas em percentual", 6)
    consumo_operacional_kw = ler_float("Consumo operacional em kW", 85)

    carga_atual_percentual = telemetria["nivel_energia_percentual"]
    energia_disponivel_kwh = capacidade_total_kwh * (carga_atual_percentual / 100)
    perdas_kwh = energia_disponivel_kwh * (perdas_percentual / 100)
    energia_restante_kwh = energia_disponivel_kwh - consumo_decolagem_kwh - perdas_kwh
    autonomia_horas = energia_restante_kwh / consumo_operacional_kw
    energia_suficiente = energia_restante_kwh > 0 and autonomia_horas > 0

    mostrar_titulo("ANÁLISE ENERGÉTICA")
    print(f"Energia disponível: {energia_disponivel_kwh:.2f} kWh")
    print(f"Perdas energéticas: {perdas_kwh:.2f} kWh")
    print(f"Energia restante após decolagem: {energia_restante_kwh:.2f} kWh")
    if energia_suficiente:
        print(f"Autonomia inicial estimada: {autonomia_horas:.2f} horas")
    else:
        print("Autonomia inicial estimada: 0.00 horas")
        print("Energia insuficiente para sustentar a decolagem.")

    return {
        "Energia pos-decolagem": energia_suficiente,
        "energia_disponivel_kwh": energia_disponivel_kwh,
        "perdas_kwh": perdas_kwh,
        "energia_restante_kwh": energia_restante_kwh,
        "autonomia_horas": max(0, autonomia_horas),
    }


def mostrar_resultado_verificacoes(verificacoes, titulo):
    mostrar_titulo(titulo)
    for item, aprovado in verificacoes.items():
        status = "OK" if aprovado else "FALHA"
        print(f"{item}: {status}")


def mostrar_decisao_final(verificacoes):
    if all(verificacoes.values()):
        decisao_final = "PRONTO PARA DECOLAR"
    else:
        decisao_final = "DECOLAGEM ABORTADA"

    mostrar_titulo("DECISÃO FINAL")
    print(decisao_final)

    if decisao_final == "DECOLAGEM ABORTADA":
        print("\nMotivos identificados:")
        for item, aprovado in verificacoes.items():
            if not aprovado:
                print(f"- {item}")


faixas_seguras = {
    "temperatura_interna_min": 18,
    "temperatura_interna_max": 30,
    "temperatura_externa_min": -50,
    "temperatura_externa_max": 60,
    "nivel_energia_min": 80,
    "pressao_tanques_min": 80,
    "pressao_tanques_max": 110,
}

mostrar_titulo("AURORA SIGER - SISTEMA DE PRÉ-DECOLAGEM")
opcao = ler_opcao()

if opcao == "1":
    telemetria = gerar_preset()
    origem_dados = "Preset seguro"
else:
    telemetria = gerar_dados_randomicos()
    origem_dados = "Dados randômicos"

verificacoes = verificar_telemetria(telemetria, faixas_seguras)

mostrar_titulo(f"TELEMETRIA INFORMADA - {origem_dados.upper()}")
for dado, valor in telemetria.items():
    print(f"{dado}: {valor}")

mostrar_resultado_verificacoes(verificacoes, "VERIFICAÇÕES BÁSICAS DA TELEMETRIA")

resultado_energia = calcular_energia(telemetria)
verificacoes["Energia após decolagem"] = resultado_energia["Energia pos-decolagem"]

mostrar_resultado_verificacoes(verificacoes, "VERIFICAÇÕES FINAIS DA PRÉ-DECOLAGEM")
mostrar_linha()
mostrar_decisao_final(verificacoes)
