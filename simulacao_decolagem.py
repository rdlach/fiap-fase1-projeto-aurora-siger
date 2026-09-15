"""Lógica de simulação por cenários da pré-decolagem Aurora Siger."""

import random


CENARIOS_DISPONIVEIS = {
    "1": "SUCESSO_DIRETO",
    "2": "ERRO_CORRIGIDO",
    "3": "FALHA_CRITICA",
    "4": "CUSTOMIZADO",
}

LIMITE_FALHA_CONSECUTIVA = 5

PARAMETROS_SEGURANCA = {
    "temperatura_interna": (18, 27),
    "temperatura_externa": (10, 34),
    "vibracao_estrutural_g": (0, 1.5),
    "nivel_energia": (80, 100),
    "pressao_lh2_psi": (120, 130),
    "pressao_lox_psi": (120, 130),
}

NOMES_VERIFICACOES = {
    "temperatura_interna": "Temperatura interna",
    "temperatura_externa": "Temperatura externa",
    "vibracao_estrutural_g": "Vibração estrutural",
    "nivel_energia": "Nível de energia",
    "pressao_lh2_psi": "Pressão LH2",
    "pressao_lox_psi": "Pressão LOX",
    "integridade_estrutural_ok": "Integridade estrutural",
    "motor_ok": "Motor",
    "navegacao_ok": "Navegação",
    "comunicacao_ok": "Comunicação",
    "sistema_eletrico_ok": "Sistema elétrico",
}


def _temperatura_interna(cenario, tempo):
    if cenario == "ERRO_CORRIGIDO":
        return 23.10 + (0.008 * tempo)

    if cenario == "FALHA_CRITICA" and tempo > 35:
        return 23.35 + (0.025 * (tempo - 35))

    return 23.00 + (0.01 * tempo)


def _temperatura_externa(cenario, tempo):
    if cenario == "FALHA_CRITICA":
        return 18.00 - (0.004 * tempo)

    inicio = 18.20 if cenario == "ERRO_CORRIGIDO" else 18.00
    return inicio - (0.005 * tempo)


def _vibracao(cenario, tempo):
    inicio = 0.650 if cenario == "ERRO_CORRIGIDO" else 0.600
    incremento = 0.014 if cenario == "ERRO_CORRIGIDO" else 0.015
    return inicio + (incremento * tempo)


def _nivel_energia(cenario, tempo):
    if cenario == "ERRO_CORRIGIDO":
        return 100 - (0.11 * tempo)

    if cenario == "FALHA_CRITICA" and tempo > 35:
        return 96.50 - (0.20 * (tempo - 35))

    return 100 - (0.10 * tempo)


def _pressao_lh2(cenario, tempo):
    if cenario == "ERRO_CORRIGIDO":
        return 124.00 + (0.035 * tempo)

    if cenario == "FALHA_CRITICA":
        return 123.50 + (0.040 * tempo)

    return 123.00 + (0.050 * tempo)


def _pressao_lox(cenario, tempo):
    if cenario != "ERRO_CORRIGIDO":
        return 126.00 + (0.030 * tempo)

    if tempo < 20:
        return 126.00 + (0.030 * tempo)

    if tempo <= 22:
        return 117.00 + (2.00 * (tempo - 20))

    return 123.00 + (0.05 * (tempo - 23))


def _fora_da_faixa(leitura, parametro):
    minimo, maximo = PARAMETROS_SEGURANCA[parametro]
    return not minimo <= leitura[parametro] <= maximo


def _valor_em_correcao(valor_anterior, parametro):
    minimo, maximo = PARAMETROS_SEGURANCA[parametro]

    if valor_anterior < minimo:
        return round(min(valor_anterior + random.uniform(1.2, 2.0), minimo + 0.3), 2)
    if valor_anterior > maximo:
        return round(max(valor_anterior - random.uniform(1.2, 2.0), maximo - 0.3), 2)

    return round(min(max(valor_anterior + random.uniform(-0.3, 0.3), minimo), maximo), 2)


def _falhas_persistentes(leituras):
    if len(leituras) <= LIMITE_FALHA_CONSECUTIVA:
        return []

    ultimas_verificacoes = [
        verificar_leitura(leitura)
        for leitura in leituras[-(LIMITE_FALHA_CONSECUTIVA + 1):]
    ]
    return [
        item
        for item in ultimas_verificacoes[0]
        if all(not verificacoes[item] for verificacoes in ultimas_verificacoes)
    ]


def _gerar_telemetria_customizada():
    leituras = []
    temperaturas = ("temperatura_interna", "temperatura_externa")
    pressoes = ("pressao_lh2_psi", "pressao_lox_psi")
    faixas_iniciais = {
        "temperatura_interna": (22, 25),
        "temperatura_externa": (17, 25),
        "pressao_lh2_psi": (124, 127),
        "pressao_lox_psi": (124, 127),
    }
    variacoes = {
        "temperatura_interna": (0.2, 3, 5),
        "temperatura_externa": (0.45, 5, 9),
        "pressao_lh2_psi": (0.4, 5, 8),
        "pressao_lox_psi": (0.4, 5, 8),
    }

    for tempo in range(61):
        anterior = leituras[-1] if leituras else None
        resfriamento_ativo = bool(anterior and any(_fora_da_faixa(anterior, campo) for campo in temperaturas))
        pressurizacao_ativa = bool(anterior and any(_fora_da_faixa(anterior, campo) for campo in pressoes))
        sensores = {}

        for campo in temperaturas + pressoes:
            em_correcao = resfriamento_ativo if campo in temperaturas else pressurizacao_ativa
            if em_correcao:
                sensores[campo] = _valor_em_correcao(anterior[campo], campo)
            elif anterior is None:
                sensores[campo] = round(random.uniform(*faixas_iniciais[campo]), 2)
            else:
                variacao, choque_minimo, choque_maximo = variacoes[campo]
                novo_valor = anterior[campo] + random.uniform(-variacao, variacao)
                if random.random() < 0.04:
                    novo_valor += random.choice((-1, 1)) * random.uniform(choque_minimo, choque_maximo)
                sensores[campo] = round(novo_valor, 2)

        if anterior is None:
            energia = round(random.uniform(96, 100), 2)
            vibracao = round(random.uniform(0.4, 0.7), 3)
        else:
            energia = round(max(0, anterior["nivel_energia"] - random.uniform(0.08, 0.18)), 2)
            vibracao = round(max(0, anterior["vibracao_estrutural_g"] + random.uniform(-0.12, 0.12)), 3)
            if random.random() < 0.02:
                vibracao = round(vibracao + random.uniform(0.5, 0.8), 3)

        sistemas = {}
        for campo in ("integridade_estrutural_ok", "motor_ok", "navegacao_ok", "comunicacao_ok", "sistema_eletrico_ok"):
            if anterior is None:
                sistemas[campo] = True
            elif anterior[campo]:
                sistemas[campo] = random.random() >= 0.01
            else:
                sistemas[campo] = random.random() < 0.3

        leituras.append(
            {
                "tempo_decolagem": tempo,
                "temperatura_interna": sensores["temperatura_interna"],
                "temperatura_externa": sensores["temperatura_externa"],
                "integridade_estrutural_ok": sistemas["integridade_estrutural_ok"],
                "vibracao_estrutural_g": vibracao,
                "nivel_energia": energia,
                "pressao_lh2_psi": sensores["pressao_lh2_psi"],
                "pressao_lox_psi": sensores["pressao_lox_psi"],
                "motor_ok": sistemas["motor_ok"],
                "navegacao_ok": sistemas["navegacao_ok"],
                "comunicacao_ok": sistemas["comunicacao_ok"],
                "sistema_eletrico_ok": sistemas["sistema_eletrico_ok"],
                "resfriamento_ativo": resfriamento_ativo,
                "pressurizacao_ativa": pressurizacao_ativa,
            }
        )

        if _falhas_persistentes(leituras):
            break

    return leituras


def gerar_telemetria_cenario(cenario):
    if cenario == "CUSTOMIZADO":
        return _gerar_telemetria_customizada()

    leituras = []

    for tempo in range(61):
        sistema_eletrico_ok = not (cenario == "FALHA_CRITICA" and tempo >= 35)
        anterior = leituras[-1] if leituras else None
        pressurizacao_ativa = bool(anterior and any(_fora_da_faixa(anterior, campo) for campo in ("pressao_lh2_psi", "pressao_lox_psi")))

        leituras.append(
            {
                "tempo_decolagem": tempo,
                "temperatura_interna": round(_temperatura_interna(cenario, tempo), 2),
                "temperatura_externa": round(_temperatura_externa(cenario, tempo), 2),
                "integridade_estrutural_ok": True,
                "vibracao_estrutural_g": round(_vibracao(cenario, tempo), 3),
                "nivel_energia": round(_nivel_energia(cenario, tempo), 2),
                "pressao_lh2_psi": round(_pressao_lh2(cenario, tempo), 2),
                "pressao_lox_psi": round(_pressao_lox(cenario, tempo), 2),
                "motor_ok": True,
                "navegacao_ok": True,
                "comunicacao_ok": True,
                "sistema_eletrico_ok": sistema_eletrico_ok,
                "resfriamento_ativo": False,
                "pressurizacao_ativa": pressurizacao_ativa,
            }
        )

        if _falhas_persistentes(leituras):
            break

    return leituras


def verificar_leitura(leitura):
    verificacoes = {}

    for parametro, (minimo, maximo) in PARAMETROS_SEGURANCA.items():
        verificacoes[NOMES_VERIFICACOES[parametro]] = minimo <= leitura[parametro] <= maximo

    for campo in [
        "integridade_estrutural_ok",
        "motor_ok",
        "navegacao_ok",
        "comunicacao_ok",
        "sistema_eletrico_ok",
    ]:
        verificacoes[NOMES_VERIFICACOES[campo]] = leitura[campo]

    return verificacoes


def analisar_cenario(cenario, leituras):
    telemetria_final = leituras[-1]
    verificacoes_finais = verificar_leitura(telemetria_final)
    alertas_corrigidos = []

    for leitura in leituras[:-1]:
        verificacoes = verificar_leitura(leitura)
        for item, aprovado in verificacoes.items():
            if not aprovado and verificacoes_finais.get(item, False):
                alerta = (leitura["tempo_decolagem"], item)
                if alerta not in alertas_corrigidos:
                    alertas_corrigidos.append(alerta)

    falhas_finais = [
        item for item, aprovado in verificacoes_finais.items() if not aprovado
    ]

    if falhas_finais:
        status = "DECOLAGEM ABORTADA"
        motivo_aborto = ", ".join(falhas_finais)
    else:
        status = "PRONTO PARA DECOLAR"
        motivo_aborto = None

    return {
        "cenario": cenario,
        "leituras": leituras,
        "telemetria_final": telemetria_final,
        "verificacoes_finais": verificacoes_finais,
        "alertas_corrigidos": alertas_corrigidos,
        "falhas_persistentes": _falhas_persistentes(leituras),
        "status": status,
        "motivo_aborto": motivo_aborto,
    }


def converter_para_telemetria_resumida(leitura):
    pressao_media = (leitura["pressao_lh2_psi"] + leitura["pressao_lox_psi"]) / 2
    modulos_ok = all(
        [
            leitura["motor_ok"],
            leitura["navegacao_ok"],
            leitura["comunicacao_ok"],
            leitura["sistema_eletrico_ok"],
        ]
    )

    return {
        "temperatura_interna_c": leitura["temperatura_interna"],
        "temperatura_externa_c": leitura["temperatura_externa"],
        "integridade_estrutural": 1 if leitura["integridade_estrutural_ok"] else 0,
        "nivel_energia_percentual": leitura["nivel_energia"],
        "pressao_media_tanques_psi": round(pressao_media, 2),
        "modulos_criticos": "OK" if modulos_ok else "FALHA",
    }
