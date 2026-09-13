"""Simulação de pré-decolagem da nave Aurora Siger."""


def mostrar_titulo(titulo):
    print("\n" + titulo)
    print("-" * 45)


# Dados simulados da telemetria da nave Aurora Siger
telemetria = {
    "temperatura_interna_c": 24,
    "temperatura_externa_c": -18,
    "integridade_estrutural": 1,
    "nivel_energia_percentual": 87,
    "pressao_tanques_percentual": 95,
    "modulos_criticos": "OK",
}

mostrar_titulo("Telemetria inicial da nave Aurora Siger")

for dado, valor in telemetria.items():
    print(f"{dado}: {valor}")


# Faixas seguras definidas para a simulação
faixas_seguras = {
    "temperatura_interna_min": 18,
    "temperatura_interna_max": 30,
    "temperatura_externa_min": -50,
    "temperatura_externa_max": 60,
    "nivel_energia_min": 80,
    "pressao_tanques_min": 80,
    "pressao_tanques_max": 110,
}

mostrar_titulo("Faixas seguras da missão")

for regra, valor in faixas_seguras.items():
    print(f"{regra}: {valor}")


# Verificações da missão
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

verificacoes = {
    "Temperatura interna": temperatura_interna_ok,
    "Temperatura externa": temperatura_externa_ok,
    "Integridade estrutural": integridade_ok,
    "Nível de energia": energia_ok,
    "Pressão dos tanques": pressao_ok,
    "Módulos críticos": modulos_ok,
}

mostrar_titulo("Resultado das verificações básicas")

for item, aprovado in verificacoes.items():
    status = "OK" if aprovado else "FALHA"
    print(f"{item}: {status}")

# Análise energética
capacidade_total_kwh = 1200
carga_atual_percentual = telemetria["nivel_energia_percentual"]
consumo_decolagem_kwh = 260
perdas_percentual = 6
consumo_operacional_kw = 85

energia_disponivel_kwh = capacidade_total_kwh * (carga_atual_percentual / 100)
perdas_kwh = energia_disponivel_kwh * (perdas_percentual / 100)
energia_restante_kwh = energia_disponivel_kwh - consumo_decolagem_kwh - perdas_kwh
autonomia_horas = energia_restante_kwh / consumo_operacional_kw
energia_pos_decolagem_ok = energia_restante_kwh > 0 and autonomia_horas > 0

mostrar_titulo("Análise energética")
print(f"Capacidade total: {capacidade_total_kwh} kWh")
print(f"Carga atual: {carga_atual_percentual}%")
print(f"Energia disponível: {energia_disponivel_kwh:.2f} kWh")
print(f"Consumo estimado na decolagem: {consumo_decolagem_kwh:.2f} kWh")
print(f"Perdas energéticas: {perdas_kwh:.2f} kWh")
print(f"Energia restante após decolagem: {energia_restante_kwh:.2f} kWh")

if energia_pos_decolagem_ok:
    print(f"Autonomia inicial estimada: {autonomia_horas:.2f} horas")
else:
    print("Autonomia inicial estimada: 0.00 horas")
    print("Energia insuficiente para sustentar a decolagem.")

verificacoes["Energia após decolagem"] = energia_pos_decolagem_ok

mostrar_titulo("Resultado final das verificações")
for item, aprovado in verificacoes.items():
    status = "OK" if aprovado else "FALHA"
    print(f"{item}: {status}")

if all(verificacoes.values()):
    decisao_final = "PRONTO PARA DECOLAR"
else:
    decisao_final = "DECOLAGEM ABORTADA"

print("-" * 45)
print(f"Decisão final: {decisao_final}")


# Análise assistida por IA, simulada a partir das regras do projeto
classificacao_dados = {
    "temperatura_interna_c": "dado numérico real",
    "temperatura_externa_c": "dado numérico real",
    "integridade_estrutural": "dado lógico/binário",
    "nivel_energia_percentual": "dado numérico real",
    "pressao_tanques_percentual": "dado numérico real",
    "modulos_criticos": "dado textual/categórico",
}

anomalias = [item for item, aprovado in verificacoes.items() if not aprovado]

mostrar_titulo("Classificação dos dados")
for dado, classificacao in classificacao_dados.items():
    print(f"{dado}: {classificacao}")

mostrar_titulo("Possíveis anomalias")
if anomalias:
    for anomalia in anomalias:
        print(f"Atenção: {anomalia} fora do padrão seguro")
else:
    print("Nenhuma anomalia crítica encontrada nos dados simulados.")

mostrar_titulo("Sugestões de risco")
if decisao_final == "PRONTO PARA DECOLAR":
    print("Manter monitoramento contínuo durante a contagem regressiva.")
    print("Revalidar energia, pressão e módulos críticos antes da ignição.")
else:
    print("Abortar a decolagem e investigar os itens com falha.")
    print("Executar diagnóstico técnico antes de uma nova tentativa.")
