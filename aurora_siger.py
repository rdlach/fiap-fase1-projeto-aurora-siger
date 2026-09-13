"""Simulação automática de pré-decolagem da nave Aurora Siger."""

from banco_dados import salvar_cenario_decolagem
from main_interativo import (
    calcular_energia,
    decidir_status,
    mostrar_analise_energetica,
    mostrar_decisao_final,
    mostrar_linha,
    mostrar_resumo_temporal,
    mostrar_resultado_verificacoes,
    mostrar_telemetria_final,
    mostrar_titulo,
)
from simulacao_decolagem import (
    analisar_cenario,
    converter_para_telemetria_resumida,
    gerar_telemetria_cenario,
)


cenario = "SUCESSO_DIRETO"
mostrar_titulo("AURORA SIGER - SIMULAÇÃO AUTOMÁTICA")
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
