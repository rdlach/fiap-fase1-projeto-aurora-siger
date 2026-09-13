# Projeto Aurora Siger - Relatório Operacional de Pré-Decolagem

Este projeto faz parte da atividade integradora da Fase 1 do curso de Ciência da Computação.

O objetivo é simular uma verificação operacional de pré-decolagem da nave Aurora Siger, analisando dados de telemetria e decidindo se a nave está pronta para decolar ou se a decolagem deve ser abortada.

Repositório do projeto:

https://github.com/rdlach/fiap-fase1-projeto-aurora-siger

## O que o projeto analisa

- Temperatura interna e externa
- Integridade estrutural
- Nível de energia
- Pressão dos tanques
- Status dos módulos críticos

## Dados simulados

| Item | Valor usado | Interpretação |
| --- | ---: | --- |
| Temperatura interna | 24 °C | Dentro da faixa segura |
| Temperatura externa | -18 °C | Dentro da faixa segura |
| Integridade estrutural | 1 | Estrutura íntegra |
| Nível de energia | 87% | Energia suficiente |
| Pressão dos tanques | 95% | Pressão operacional |
| Módulos críticos | OK | Módulos funcionando |

## Lógica da decisão

O sistema verifica se todos os dados estão dentro de faixas seguras e, depois disso, realiza a análise energética.

| Verificação | Faixa ou condição segura |
| --- | --- |
| Temperatura interna | Entre 18 °C e 30 °C |
| Temperatura externa | Entre -50 °C e 60 °C |
| Integridade estrutural | Igual a 1 |
| Nível de energia | Maior ou igual a 80% |
| Pressão dos tanques | Entre 80% e 110% |
| Módulos críticos | Igual a OK |

Depois das verificações básicas, o sistema calcula:

- energia disponível;
- perdas energéticas;
- energia restante após a decolagem;
- autonomia inicial estimada.

Se todas as condições forem atendidas e ainda houver energia suficiente após a decolagem, o resultado será:

```text
PRONTO PARA DECOLAR
```

Caso contrário, incluindo falha energética, o resultado será:

```text
DECOLAGEM ABORTADA
```

## Arquivos do projeto

- `nave-cod-siger.ipynb`: notebook principal com a simulação, verificações e análise energética.
- `aurora_siger.py`: versão em script Python para execução direta no PyCharm ou terminal.
- `main_interativo.py`: versão interativa em terminal, usando `input()` para preencher os dados da nave.
- `prints/`: pasta reservada para prints da execução.
- `relatorio/relatorio_pre_decolagem.md`: texto-base do relatório final.
- `relatorio/`: pasta reservada para o PDF final da atividade.
- `AJUSTES_PENDENTES.md`: checklist do que ainda precisa ser revisado pelo grupo.

## Formas de demonstrar o projeto

O projeto pode ser mostrado de duas maneiras.

### 1. Tela interativa no terminal

Essa é a forma mais simples de apresentar a lógica funcionando ao vivo. O programa pergunta se o usuário quer usar um cenário pronto ou gerar dados randômicos.

Depois disso, ele mostra:

- a telemetria carregada;
- as verificações básicas;
- a análise energética;
- a decisão final.

Essa versão é boa para demonstrar o raciocínio do algoritmo passo a passo.

### 2. Tabela no notebook

O notebook também mostra cenários em formato de tabela, parecido com o exemplo usado em aula.

Nesse formato, cada linha representa uma situação da nave. A última coluna mostra a decisão:

- `PRONTO PARA DECOLAR`
- `DECOLAGEM ABORTADA`

Essa versão é boa para documentar o projeto e colocar no relatório.

Na prática, as duas formas se complementam:

- a tela interativa ajuda a apresentar o projeto funcionando;
- a tabela ajuda a deixar a análise organizada no notebook e no relatório.

Ou seja, não precisa escolher apenas uma. A tela mostra a simulação acontecendo e a tabela registra os cenários de forma clara.

## Como executar

### Opção 1: Notebook

1. Abrir o arquivo `nave-cod-siger.ipynb` na sua IDE de preferência.
2. Selecionar um interpretador Python 3.
3. Executar as células na ordem em que aparecem.
4. Conferir o resultado final e a tabela de cenários simulados.

### Opção 2: Script Python

1. Abrir o arquivo `aurora_siger.py` no PyCharm.
2. Selecionar um interpretador Python 3.
3. Clicar com o botão direito no arquivo e escolher `Run 'aurora_siger'`.

Também é possível executar pelo terminal:

```bash
python3 aurora_siger.py
```

### Opção 3: Tela interativa no terminal

Esta versão usa os conceitos básicos vistos na fase: entrada de dados com `input()`, variáveis, conversão de tipos, operadores relacionais, `if/else` e impressão do resultado.

Ao iniciar, o programa permite escolher entre:

- `1 - Usar preset seguro`: carrega dados fixos que resultam em uma decolagem aprovada.
- `2 - Gerar dados randômicos`: gera uma telemetria aleatória, que pode resultar em aprovação ou aborto da decolagem.

No PyCharm:

1. Abrir o arquivo `main_interativo.py`.
2. Clicar com o botão direito no arquivo.
3. Escolher `Run 'main_interativo'`.
4. Digitar os valores pedidos ou pressionar ENTER para usar os valores padrão.

Pelo terminal:

```bash
python3 main_interativo.py
```

## Prints da execução

Adicionar aqui os prints após executar o notebook:

- Print da telemetria inicial
- Print das verificações
- Print da decisão final
- Print da análise energética

Exemplo de inserção no README:

```markdown
![Execução do notebook](prints/nome-do-print.png)
```

## Resultado esperado

Com os dados simulados atualmente, o sistema deve retornar:

```text
PRONTO PARA DECOLAR
```

A energia disponível calculada é de 1044,00 kWh e a autonomia inicial estimada após decolagem é de aproximadamente 8,49 horas.

## Integrantes

- Ronei Davi Lach
- Gabriel Hampel Meireles
- Roberto Kenji Iuvata
- José Roberto Zendron
- David Silva
