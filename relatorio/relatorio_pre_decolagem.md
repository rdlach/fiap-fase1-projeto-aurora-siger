# Relatório Operacional de Pré-Decolagem - Nave Aurora Siger

## 1. Introdução

Este relatório apresenta uma simulação de verificação operacional de pré-decolagem da nave Aurora Siger. O objetivo é organizar dados de telemetria, aplicar um algoritmo de decisão, executar a lógica em Python, calcular a condição energética inicial e refletir sobre os impactos éticos, sociais e sustentáveis do uso de tecnologia em uma missão espacial.

A simulação decide entre dois resultados possíveis:

- PRONTO PARA DECOLAR
- DECOLAGEM ABORTADA

## 1.1 Organização e descrição da telemetria

Foram simulados dados essenciais para uma avaliação inicial da nave antes da decolagem.

| Dado | Valor simulado | Descrição |
| --- | ---: | --- |
| Temperatura interna | 24 °C | Condição térmica interna da nave |
| Temperatura externa | -18 °C | Condição térmica externa antes da decolagem |
| Integridade estrutural | 1 | Indica estrutura íntegra quando igual a 1 |
| Nível de energia | 87% | Percentual de carga disponível |
| Pressão dos tanques | 95% | Condição operacional dos tanques |
| Módulos críticos | OK | Estado dos módulos essenciais da nave |

Esses dados foram escolhidos por representarem fatores importantes para uma decisão de pré-decolagem. Caso algum deles esteja fora da faixa segura, a decolagem deve ser abortada para evitar riscos técnicos e operacionais.

## 1.2 Algoritmo de verificação

O algoritmo compara os dados de telemetria com faixas seguras previamente definidas. A decisão final depende de todas as verificações serem aprovadas.

| Item verificado | Critério seguro |
| --- | --- |
| Temperatura interna | Entre 18 °C e 30 °C |
| Temperatura externa | Entre -50 °C e 60 °C |
| Integridade estrutural | Igual a 1 |
| Nível de energia | Maior ou igual a 80% |
| Pressão dos tanques | Entre 80% e 110% |
| Módulos críticos | Igual a OK |

### Pseudocódigo

```text
INÍCIO
    Ler dados de telemetria da nave
    Verificar temperatura interna
    Verificar temperatura externa
    Verificar integridade estrutural
    Verificar nível de energia
    Verificar pressão dos tanques
    Verificar módulos críticos

    SE todas as verificações forem verdadeiras ENTÃO
        Exibir "PRONTO PARA DECOLAR"
    SENÃO
        Exibir "DECOLAGEM ABORTADA"
    FIM SE
FIM
```

## 1.3 Script em Python

A lógica foi implementada no notebook `nave-cod-siger.ipynb`. O script cria um conjunto de dados simulados, executa as verificações e imprime a decisão final.

Trecho principal da decisão:

```python
if all(verificacoes.values()):
    decisao_final = "PRONTO PARA DECOLAR"
else:
    decisao_final = "DECOLAGEM ABORTADA"
```

O comando `all()` verifica se todas as condições da lista de verificações são verdadeiras. Se uma única condição falhar, a decisão final passa a ser "DECOLAGEM ABORTADA".

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
| Carga atual | 87% |
| Consumo estimado na decolagem | 260 kWh |
| Perdas energéticas | 6% |
| Consumo operacional estimado | 85 kW |

Cálculos:

```text
Energia disponível = 1200 x 0,87 = 1044 kWh
Perdas energéticas = 1044 x 0,06 = 62,64 kWh
Energia restante = 1044 - 260 - 62,64 = 721,36 kWh
Autonomia inicial = 721,36 / 85 = 8,49 horas
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
| Pressão dos tanques | Numérico real |
| Módulos críticos | Textual/categórico |

Com os dados simulados, nenhuma anomalia crítica foi identificada. Mesmo assim, a recomendação é manter monitoramento contínuo durante a contagem regressiva e revalidar energia, pressão e módulos críticos antes da ignição.

## 1.6 Reflexão crítica

O uso de tecnologia em missões espaciais exige ética e responsabilidade. Sistemas automatizados podem apoiar decisões importantes, mas precisam ser claros, auditáveis e acompanhados por pessoas capacitadas. Uma decisão incorreta em um sistema crítico pode gerar riscos humanos, financeiros e ambientais.

A exploração espacial também possui impacto social. Ela pode estimular ciência, educação, inovação e desenvolvimento de novas tecnologias. Ao mesmo tempo, é necessário garantir que esse avanço não amplie desigualdades nem desvie recursos de problemas sociais importantes.

Do ponto de vista da sustentabilidade tecnológica, missões espaciais e sistemas computacionais devem considerar eficiência energética, redução de desperdício, descarte correto de componentes eletrônicos e uso consciente de recursos. A tecnologia deve servir ao progresso humano sem ignorar seus impactos sobre o planeta.

## 2. Entregáveis

O projeto contém:

- Notebook Python: `nave-cod-siger.ipynb`
- README.md com explicação do projeto e instruções de execução
- Pasta `prints/` para imagens da execução
- Texto-base do relatório final

Antes da entrega, o grupo deve gerar o PDF final e inserir os prints da execução no README.

## 3. Conclusão

A simulação mostrou que os dados da nave Aurora Siger estão dentro das faixas seguras estabelecidas. A análise energética também indica carga suficiente para a etapa inicial da missão. Portanto, considerando os parâmetros definidos nesta simulação, a decisão operacional é:

```text
PRONTO PARA DECOLAR
```
