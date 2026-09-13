"""Testes das regras temporais da pré-decolagem."""

import random
import unittest
from datetime import timedelta
from unittest.mock import MagicMock, patch

import banco_dados
from simulacao_decolagem import (
    PARAMETROS_SEGURANCA,
    _falhas_persistentes,
    analisar_cenario,
    gerar_telemetria_cenario,
)


class SimulacaoTemporalTest(unittest.TestCase):
    def test_cenarios_fixos(self):
        for nome, tamanho, status in (
            ("SUCESSO_DIRETO", 61, "PRONTO PARA DECOLAR"),
            ("ERRO_CORRIGIDO", 61, "PRONTO PARA DECOLAR"),
            ("FALHA_CRITICA", 41, "DECOLAGEM ABORTADA"),
        ):
            with self.subTest(nome=nome):
                leituras = gerar_telemetria_cenario(nome)
                self.assertEqual(len(leituras), tamanho)
                self.assertEqual(analisar_cenario(nome, leituras)["status"], status)

        corrigido = gerar_telemetria_cenario("ERRO_CORRIGIDO")
        self.assertEqual([leitura["pressurizacao_ativa"] for leitura in corrigido[20:24]], [False, True, True, False])
        critico = gerar_telemetria_cenario("FALHA_CRITICA")
        self.assertEqual(critico[-1]["tempo_decolagem"], 40)
        self.assertEqual(_falhas_persistentes(critico), ["Sistema elétrico"])

    def test_cinco_falhas_nao_abortam_e_recuperacao_zera_contagem(self):
        leituras = gerar_telemetria_cenario("SUCESSO_DIRETO")[:12]
        for tempo in (*range(5), *range(6, 11)):
            leituras[tempo]["motor_ok"] = False
        self.assertEqual(_falhas_persistentes(leituras), [])
        leituras[11]["motor_ok"] = False
        self.assertEqual(_falhas_persistentes(leituras), ["Motor"])

    def test_customizado_mantem_variaveis_e_para_na_primeira_falha_persistente(self):
        finais = set()
        for semente in range(200):
            random.seed(semente)
            leituras = gerar_telemetria_cenario("CUSTOMIZADO")
            analise = analisar_cenario("CUSTOMIZADO", leituras)
            finais.add(len(leituras) < 61)
            self.assertEqual([leitura["tempo_decolagem"] for leitura in leituras], list(range(len(leituras))))
            self.assertTrue(all(not _falhas_persistentes(leituras[:indice]) for indice in range(1, len(leituras))))
            self.assertEqual(analise["falhas_persistentes"], _falhas_persistentes(leituras))
            if len(leituras) < 61:
                self.assertTrue(analise["falhas_persistentes"])

            for anterior, atual in zip(leituras, leituras[1:]):
                self.assertLessEqual(atual["nivel_energia"], anterior["nivel_energia"])
                for indicador, campos in (
                    ("resfriamento_ativo", ("temperatura_interna", "temperatura_externa")),
                    ("pressurizacao_ativa", ("pressao_lh2_psi", "pressao_lox_psi")),
                ):
                    esperado = any(
                        not PARAMETROS_SEGURANCA[campo][0] <= anterior[campo] <= PARAMETROS_SEGURANCA[campo][1]
                        for campo in campos
                    )
                    self.assertEqual(atual[indicador], esperado)
                    if atual[indicador]:
                        for campo in campos:
                            minimo, maximo = PARAMETROS_SEGURANCA[campo]
                            if anterior[campo] < minimo:
                                self.assertGreater(atual[campo], anterior[campo])
                            elif anterior[campo] > maximo:
                                self.assertLess(atual[campo], anterior[campo])

        self.assertEqual(finais, {True, False})

    def test_banco_recebe_apenas_leituras_ate_a_parada_com_horarios_simulados(self):
        leituras = gerar_telemetria_cenario("FALHA_CRITICA")
        conexao = MagicMock()
        cursor = conexao.cursor.return_value.__enter__.return_value
        cursor.fetchone.return_value = (42,)
        with patch.object(banco_dados, "criar_tabela_execucoes"), patch.object(
            banco_dados, "conectar_postgres"
        ) as conectar:
            conectar.return_value.__enter__.return_value = conexao
            self.assertEqual(
                banco_dados.salvar_cenario_decolagem("FALHA_CRITICA", leituras, "DECOLAGEM ABORTADA", "Sistema elétrico"),
                42,
            )

        inicio, fim = cursor.execute.call_args.args[1][:2]
        self.assertEqual(fim - inicio, timedelta(seconds=40))
        linhas = cursor.executemany.call_args.args[1]
        self.assertEqual(len(linhas), 41)
        self.assertEqual(linhas[0][0], inicio)
        self.assertEqual(linhas[-1][0], fim)
        self.assertTrue(all(linha[0] == inicio + timedelta(seconds=linha[1]) for linha in linhas))


if __name__ == "__main__":
    unittest.main()
