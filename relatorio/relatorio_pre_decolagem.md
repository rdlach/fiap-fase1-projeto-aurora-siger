# Relatório Operacional de Pré-Decolagem - Nave Aurora Siger

## 1. Introdução

Este relatório apresenta uma simulação de verificação operacional de pré-decolagem da nave Aurora Siger. O objetivo é organizar dados de telemetria, aplicar um algoritmo de decisão, executar a lógica em Python, calcular a condição energética inicial e refletir sobre os impactos éticos, sociais e sustentáveis do uso de tecnologia em uma missão espacial.

A simulação decide entre dois resultados possíveis:

- PRONTO PARA DECOLAR
- DECOLAGEM ABORTADA

## 1.1 Organização e descrição da telemetria

Foram simulados dados essenciais para uma avaliação inicial da nave antes da decolagem. A tabela abaixo usa a leitura final do cenário `SUCESSO_DIRETO`, em `T+60s`.

| Dado | Valor simulado | Descrição |
| --- | ---: | --- |
| Temperatura interna | 23,60 °C | Condição térmica interna da nave |
| Temperatura externa | 17,70 °C | Condição térmica externa antes da decolagem |
| Integridade estrutural | 1 | Indica estrutura íntegra quando igual a 1 |
| Vibração estrutural | 1,500 g RMS | Vibração medida na estrutura |
| Nível de energia | 94% | Percentual de carga disponível |
| Pressão LH2 | 126,00 psi | Condição operacional do tanque de hidrogênio líquido |
| Pressão LOX | 127,80 psi | Condição operacional do tanque de oxigênio líquido |
| Módulos críticos | OK | Estado dos módulos essenciais da nave |

Esses dados foram escolhidos por representarem fatores importantes para uma decisão de pré-decolagem. Caso algum deles esteja fora da faixa segura, a decolagem deve ser abortada para evitar riscos técnicos e operacionais.

## 1.2 Algoritmo de verificação

O algoritmo compara os dados de telemetria com faixas seguras previamente definidas. A decisão final depende de todas as verificações serem aprovadas.

| Item verificado | Critério seguro |
| --- | --- |
| Temperatura interna | Entre 18 °C e 27 °C |
| Temperatura externa | Entre 10 °C e 34 °C |
| Vibração estrutural | Entre 0 e 1,5 g RMS |
| Integridade estrutural | Igual a 1 |
| Nível de energia | Maior ou igual a 80% |
| Pressão LH2 | Entre 120 e 130 psi |
| Pressão LOX | Entre 120 e 130 psi |
| Módulos críticos | Motor, navegação, comunicação e sistema elétrico iguais a OK |

### Pseudocódigo

```text
INÍCIO
    Ler dados de telemetria da nave
    Verificar temperatura interna
    Verificar temperatura externa
    Verificar vibração estrutural
    Verificar integridade estrutural
    Verificar nível de energia
    Verificar pressão LH2
    Verificar pressão LOX
    Verificar módulos críticos

    SE alguma falha persistir por seis leituras consecutivas ENTÃO
        Exibir "DECOLAGEM ABORTADA"
    SENÃO
        Usar a última leitura para a decisão final
        SE todas as verificações forem verdadeiras ENTÃO
            Exibir "PRONTO PARA DECOLAR"
        SENÃO
            Exibir "DECOLAGEM ABORTADA"
        FIM SE
    FIM SE
FIM
```

## 1.3 Script em Python

A lógica temporal foi implementada em `simulacao_decolagem.py` e utilizada pelo notebook `nave-cod-siger.ipynb`. O script gera leituras sequenciais, executa as verificações e imprime a decisão final.

Trecho principal da decisão:

```python
if falhas or analise["falhas_persistentes"]:
    decisao_final = "DECOLAGEM ABORTADA"
else:
    decisao_final = "PRONTO PARA DECOLAR"
```

Além da verificação final, o programa considera falhas persistentes durante a contagem. Se uma condição grave permanecer fora do padrão por seis leituras consecutivas, a contagem é interrompida.

Com os dados atuais, todas as verificações são aprovadas e o resultado é:

```text
PRONTO PARA DECOLAR
```

## 1.4 Análise energética

A análise energética calcula a energia disponível a partir da capacidade total da nave e da carga atual. Depois disso, desconta o consumo estimado na decolagem e as perdas energéticas.

Dados usados:

| Item | Valor |
| --- | ---: |
| Capacidade total | 1200 kWh |
| Carga atual | 94% |
| Consumo estimado na decolagem | 260 kWh |
| Perdas energéticas | 6% |
| Consumo operacional estimado | 85 kW |

Cálculos:

```text
Energia disponível = 1200 x 0,94 = 1128 kWh
Perdas energéticas = 1128 x 0,06 = 67,68 kWh
Energia restante = 1128 - 260 - 67,68 = 800,32 kWh
Autonomia inicial = 800,32 / 85 = 9,42 horas
```

Com isso, a nave apresenta energia suficiente para a etapa inicial da missão simulada.

## 1.5 Análise assistida por IA

A IA pode apoiar a missão classificando os dados, identificando possíveis anomalias e sugerindo riscos.

Classificação dos dados:

| Dado | Classificação |
| --- | --- |
| Temperatura interna | Numérico real |
| Temperatura externa | Numérico real |
| Integridade estrutural | Lógico/binário |
| Nível de energia | Numérico real |
| Vibração estrutural | Numérico real |
| Pressão LH2 | Numérico real |
| Pressão LOX | Numérico real |
| Módulos críticos | Lógico/binário e categórico |

A decisão automática do programa utiliza regras e faixas de segurança predefinidas. A inteligência artificial foi utilizada como apoio para classificar os dados, interpretar possíveis anomalias e elaborar sugestões de risco. A decisão final continua sujeita às regras de segurança e à supervisão humana. Não se afirma que o programa possui uma IA própria ou um modelo treinado com dados de missões reais.

## 1.6 Reflexão crítica

### Introdução

O projeto de verificação de condições para uma decolagem permite refletir sobre a responsabilidade no uso da tecnologia. A análise da telemetria, a avaliação energética e o apoio da inteligência artificial devem estar associados à segurança, à transparência e ao uso consciente dos recursos. Essa perspectiva se relaciona ao tripé da sustentabilidade, que considera as dimensões econômica, social e ambiental, e aos princípios de governança presentes no ESG.

### Ética e responsabilidade

No aspecto ético, a segurança deve orientar os critérios de autorização ou cancelamento da decolagem. Informações sobre temperatura, integridade estrutural, energia e pressão precisam ser verificadas, pois dados incorretos ou incompletos podem comprometer a decisão. Também é necessário apresentar os motivos do resultado, permitindo compreender quais condições foram consideradas inadequadas. A inteligência artificial pode auxiliar na identificação de anomalias, mas suas sugestões devem ser avaliadas, mantendo a responsabilidade humana. Em uma aplicação real, a simulação precisaria passar por validações técnicas rigorosas antes de integrar uma operação.

### Impacto social da exploração espacial

Quanto ao impacto social, a exploração espacial pode contribuir para pesquisas científicas, comunicação e monitoramento ambiental. Entretanto, esses benefícios precisam ser avaliados junto aos custos, aos riscos e à sua distribuição na sociedade. Uma atuação socialmente responsável deve considerar tanto as pessoas envolvidas nas operações quanto as comunidades afetadas, buscando ampliar o acesso aos conhecimentos e às tecnologias desenvolvidas. Dessa forma, o avanço tecnológico deve estar acompanhado de benefícios coletivos e respeito aos interesses das partes envolvidas.

### Sustentabilidade tecnológica

Na dimensão ambiental, a análise da capacidade energética, da carga disponível, do consumo previsto e das perdas contribui para o planejamento do uso de energia. Essa abordagem se alinha à TI Verde ao permitir identificar oportunidades de eficiência, sem comprometer as margens de segurança. Entretanto, a sustentabilidade também exige considerar o ciclo de vida dos equipamentos, desde a extração de materiais e a fabricação até a manutenção e o descarte. Práticas de reparo, reutilização segura e reciclagem, associadas à economia circular, podem reduzir desperdícios e a geração de resíduos.

### Conclusão

Por fim, é necessário reconhecer os limites do projeto: calcular o consumo e as perdas energéticas não comprova que toda a missão seja sustentável. Afirmações sobre redução de impactos exigem indicadores e comparações, evitando o greenwashing. Assim, o projeto demonstra que uma decisão tecnicamente viável deve ser acompanhada de critérios éticos, responsabilidade social e atenção ambiental. O sucesso de uma missão envolve não apenas alcançar seu objetivo, mas também justificar suas decisões, proteger as pessoas e utilizar os recursos de maneira responsável.

## 2. Entregáveis

O projeto contém:

- Notebook Python: `nave-cod-siger.ipynb`
- README.md com explicação do projeto e instruções de execução
- Pasta `prints/evidencias/` com imagens da implementação
- Texto-base do relatório final
- PDF final gerado em `relatorio/relatorio_pre_decolagem.pdf`

## 3. Conclusão

A simulação do cenário `SUCESSO_DIRETO` mostrou que os dados finais da nave Aurora Siger estão dentro das faixas seguras estabelecidas. A análise energética também indica carga suficiente para a etapa inicial da missão. Portanto, considerando os parâmetros definidos nesta simulação, a decisão operacional é:

```text
PRONTO PARA DECOLAR
```
