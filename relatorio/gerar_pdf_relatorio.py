from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT_PDF = "relatorio_pre_decolagem.pdf"


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.drawString(2 * cm, 1.3 * cm, "Projeto Aurora Siger - Relatório Operacional de Pré-Decolagem")
    canvas.drawRightString(19 * cm, 1.3 * cm, f"Página {doc.page}")
    canvas.restoreState()


def add_heading(story, text, style):
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(text, style))
    story.append(Spacer(1, 0.15 * cm))


def add_paragraph(story, text, style):
    story.append(Paragraph(text, style))
    story.append(Spacer(1, 0.18 * cm))


def add_table(story, data):
    table = Table(data, colWidths=[5 * cm, 4 * cm, 7 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#232323")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#999999")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F5F5")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 0.35 * cm))


def add_code(story, text, style):
    story.append(Paragraph(text.replace("\n", "<br/>"), style))
    story.append(Spacer(1, 0.25 * cm))


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="Relatório Operacional de Pré-Decolagem - Aurora Siger",
    )

    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#202020"),
        spaceAfter=18,
    )
    h1 = ParagraphStyle(
        "Heading1Custom",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=17,
        textColor=colors.HexColor("#D20A5C"),
        spaceBefore=8,
        spaceAfter=8,
    )
    h2 = ParagraphStyle(
        "Heading2Custom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#333333"),
        spaceBefore=6,
        spaceAfter=6,
    )
    body = ParagraphStyle(
        "BodyCustom",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        alignment=4,
        spaceAfter=6,
    )
    code = ParagraphStyle(
        "CodeCustom",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=8.5,
        leading=11,
        backColor=colors.HexColor("#F0F0F0"),
        borderColor=colors.HexColor("#CCCCCC"),
        borderWidth=0.5,
        borderPadding=6,
        leftIndent=0,
    )

    story = []
    story.append(Paragraph("Relatório Operacional de Pré-Decolagem", title))
    story.append(Paragraph("Nave Aurora Siger", h2))
    add_paragraph(
        story,
        "Este relatório apresenta uma simulação de verificação operacional de pré-decolagem da nave Aurora Siger. O objetivo é organizar dados de telemetria, aplicar um algoritmo de decisão, executar a lógica em Python, calcular a condição energética inicial e refletir sobre impactos éticos, sociais e sustentáveis do uso de tecnologia em uma missão espacial.",
        body,
    )
    add_paragraph(
        story,
        "A simulação decide entre dois resultados possíveis: PRONTO PARA DECOLAR ou DECOLAGEM ABORTADA.",
        body,
    )

    add_heading(story, "1.1 Organização e descrição da telemetria", h1)
    add_paragraph(
        story,
        "Foram simulados dados essenciais para uma avaliação inicial da nave antes da decolagem. Esses dados representam informações que poderiam ser recebidas por sensores e sistemas de monitoramento.",
        body,
    )
    add_table(
        story,
        [
            ["Dado", "Valor simulado", "Descrição"],
            ["Temperatura interna", "24 °C", "Condição térmica interna da nave"],
            ["Temperatura externa", "-18 °C", "Condição térmica externa antes da decolagem"],
            ["Integridade estrutural", "1", "Estrutura íntegra quando igual a 1"],
            ["Nível de energia", "87%", "Percentual de carga disponível"],
            ["Pressão dos tanques", "95%", "Condição operacional dos tanques"],
            ["Módulos críticos", "OK", "Estado dos módulos essenciais da nave"],
        ],
    )

    add_heading(story, "1.2 Algoritmo de verificação", h1)
    add_paragraph(
        story,
        "O algoritmo compara os dados de telemetria com faixas seguras previamente definidas. A decisão final depende de todas as verificações serem aprovadas.",
        body,
    )
    add_table(
        story,
        [
            ["Item verificado", "Critério seguro", "Observação"],
            ["Temperatura interna", "18 °C a 30 °C", "Ambiente interno estável"],
            ["Temperatura externa", "-50 °C a 60 °C", "Condição externa aceita"],
            ["Integridade estrutural", "Igual a 1", "Sem falha estrutural"],
            ["Nível de energia", "Maior ou igual a 80%", "Energia mínima para partida"],
            ["Pressão dos tanques", "80% a 110%", "Faixa operacional"],
            ["Módulos críticos", "Igual a OK", "Sistemas principais funcionando"],
        ],
    )
    story.append(PageBreak())
    add_heading(story, "Pseudocódigo do algoritmo", h2)
    add_code(
        story,
        "INÍCIO\n"
        "    Ler dados de telemetria da nave\n"
        "    Verificar temperatura, estrutura, energia, pressão e módulos\n"
        "    SE todas as verificações forem verdadeiras ENTÃO\n"
        "        Exibir \"PRONTO PARA DECOLAR\"\n"
        "    SENÃO\n"
        "        Exibir \"DECOLAGEM ABORTADA\"\n"
        "    FIM SE\n"
        "FIM",
        code,
    )

    add_heading(story, "1.3 Script em Python", h1)
    add_paragraph(
        story,
        "A lógica foi implementada no notebook nave-cod-siger.ipynb. O script cria os dados simulados, executa as verificações e imprime a decisão final.",
        body,
    )
    add_code(
        story,
        "if all(verificacoes.values()):\n"
        "    decisao_final = \"PRONTO PARA DECOLAR\"\n"
        "else:\n"
        "    decisao_final = \"DECOLAGEM ABORTADA\"",
        code,
    )
    add_paragraph(
        story,
        "O comando all() verifica se todas as condições são verdadeiras. Se uma única condição falhar, a decisão final passa a ser DECOLAGEM ABORTADA.",
        body,
    )

    story.append(PageBreak())
    add_heading(story, "1.4 Análise energética", h1)
    add_paragraph(
        story,
        "A análise energética calcula a energia disponível a partir da capacidade total da nave e da carga atual. Depois disso, desconta o consumo estimado na decolagem e as perdas energéticas.",
        body,
    )
    add_table(
        story,
        [
            ["Item", "Valor", "Descrição"],
            ["Capacidade total", "1200 kWh", "Capacidade máxima simulada"],
            ["Carga atual", "87%", "Carga informada pela telemetria"],
            ["Consumo na decolagem", "260 kWh", "Energia estimada para a partida"],
            ["Perdas energéticas", "6%", "Perdas do processo"],
            ["Consumo operacional", "85 kW", "Consumo médio após decolagem"],
        ],
    )
    add_code(
        story,
        "Energia disponível = 1200 x 0,87 = 1044 kWh\n"
        "Perdas energéticas = 1044 x 0,06 = 62,64 kWh\n"
        "Energia restante = 1044 - 260 - 62,64 = 721,36 kWh\n"
        "Autonomia inicial = 721,36 / 85 = 8,49 horas",
        code,
    )
    add_paragraph(
        story,
        "Com isso, a nave apresenta energia suficiente para a etapa inicial da missão simulada.",
        body,
    )

    add_heading(story, "1.5 Análise assistida por IA", h1)
    add_paragraph(
        story,
        "A IA pode apoiar a missão classificando os dados, identificando possíveis anomalias e sugerindo riscos.",
        body,
    )
    add_table(
        story,
        [
            ["Dado", "Classificação", "Uso na decisão"],
            ["Temperatura interna", "Numérico real", "Verificação de faixa segura"],
            ["Temperatura externa", "Numérico real", "Verificação de faixa segura"],
            ["Integridade estrutural", "Lógico/binário", "Aprovado ou falha"],
            ["Nível de energia", "Numérico real", "Energia mínima"],
            ["Pressão dos tanques", "Numérico real", "Faixa operacional"],
            ["Módulos críticos", "Textual/categórico", "Status OK ou falha"],
        ],
    )
    add_paragraph(
        story,
        "Com os dados simulados, nenhuma anomalia crítica foi identificada. Mesmo assim, recomenda-se manter monitoramento contínuo durante a contagem regressiva e revalidar energia, pressão e módulos críticos antes da ignição.",
        body,
    )

    add_heading(story, "1.6 Reflexão crítica", h1)
    add_heading(story, "Introdução", h2)
    add_paragraph(
        story,
        "O projeto de verificação de condições para uma decolagem permite refletir sobre a responsabilidade no uso da tecnologia. A análise da telemetria, a avaliação energética e o apoio da inteligência artificial devem estar associados à segurança, à transparência e ao uso consciente dos recursos. Essa perspectiva se relaciona ao tripé da sustentabilidade, que considera as dimensões econômica, social e ambiental, e aos princípios de governança presentes no ESG.",
        body,
    )
    add_heading(story, "Ética e responsabilidade", h2)
    add_paragraph(
        story,
        "No aspecto ético, a segurança deve orientar os critérios de autorização ou cancelamento da decolagem. Informações sobre temperatura, integridade estrutural, energia e pressão precisam ser verificadas, pois dados incorretos ou incompletos podem comprometer a decisão. Também é necessário apresentar os motivos do resultado, permitindo compreender quais condições foram consideradas inadequadas. A inteligência artificial pode auxiliar na identificação de anomalias, mas suas sugestões devem ser avaliadas, mantendo a responsabilidade humana. Em uma aplicação real, a simulação precisaria passar por validações técnicas rigorosas antes de integrar uma operação.",
        body,
    )
    add_heading(story, "Impacto social da exploração espacial", h2)
    add_paragraph(
        story,
        "Quanto ao impacto social, a exploração espacial pode contribuir para pesquisas científicas, comunicação e monitoramento ambiental. Entretanto, esses benefícios precisam ser avaliados junto aos custos, aos riscos e à sua distribuição na sociedade. Uma atuação socialmente responsável deve considerar tanto as pessoas envolvidas nas operações quanto as comunidades afetadas, buscando ampliar o acesso aos conhecimentos e às tecnologias desenvolvidas. Dessa forma, o avanço tecnológico deve estar acompanhado de benefícios coletivos e respeito aos interesses das partes envolvidas.",
        body,
    )
    add_heading(story, "Sustentabilidade tecnológica", h2)
    add_paragraph(
        story,
        "Na dimensão ambiental, a análise da capacidade energética, da carga disponível, do consumo previsto e das perdas contribui para o planejamento do uso de energia. Essa abordagem se alinha à TI Verde ao permitir identificar oportunidades de eficiência, sem comprometer as margens de segurança. Entretanto, a sustentabilidade também exige considerar o ciclo de vida dos equipamentos, desde a extração de materiais e a fabricação até a manutenção e o descarte. Práticas de reparo, reutilização segura e reciclagem, associadas à economia circular, podem reduzir desperdícios e a geração de resíduos.",
        body,
    )
    add_heading(story, "Conclusão", h2)
    add_paragraph(
        story,
        "Por fim, é necessário reconhecer os limites do projeto: calcular o consumo e as perdas energéticas não comprova que toda a missão seja sustentável. Afirmações sobre redução de impactos exigem indicadores e comparações, evitando o greenwashing. Assim, o projeto demonstra que uma decisão tecnicamente viável deve ser acompanhada de critérios éticos, responsabilidade social e atenção ambiental. O sucesso de uma missão envolve não apenas alcançar seu objetivo, mas também justificar suas decisões, proteger as pessoas e utilizar os recursos de maneira responsável.",
        body,
    )

    add_heading(story, "2. Entregáveis", h1)
    add_paragraph(
        story,
        "O projeto contém notebook Python, README.md com explicação e instruções, pasta para prints da execução e este relatório em PDF. Antes da entrega final, o grupo deve inserir os prints no README e conferir o link público do GitHub.",
        body,
    )

    add_heading(story, "3. Conclusão", h1)
    add_paragraph(
        story,
        "A simulação mostrou que os dados da nave Aurora Siger estão dentro das faixas seguras estabelecidas. A análise energética também indica carga suficiente para a etapa inicial da missão. Portanto, considerando os parâmetros definidos nesta simulação, a decisão operacional é: PRONTO PARA DECOLAR.",
        body,
    )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build_pdf()
