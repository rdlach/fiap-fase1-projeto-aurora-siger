WITH nova_decolagem AS (
    INSERT INTO decolagem (
        data_inicio,
        data_fim,
        cenario,
        status,
        motivo_aborto
    )
    VALUES (
        '2026-09-13 14:30:47',
        '2026-09-13 14:31:47',
        'SUCESSO_DIRETO',
        'PRONTO PARA DECOLAR',
        NULL
    )
    RETURNING id
)
INSERT INTO telemetria (
    data_hora,
    tempo_decolagem,
    temperatura_interna,
    temperatura_externa,
    integridade_estrutural_ok,
    vibracao_estrutural_g,
    nivel_energia,
    pressao_lh2_psi,
    pressao_lox_psi,
    motor_ok,
    navegacao_ok,
    comunicacao_ok,
    sistema_eletrico_ok,
    resfriamento_ativo,
    pressurizacao_ativa,
    decolagem_id
)
SELECT
    '2026-09-13 14:31:47',
    60,
    23.60,
    17.70,
    TRUE,
    1.500,
    94.00,
    126.00,
    127.80,
    TRUE,
    TRUE,
    TRUE,
    TRUE,
    TRUE,
    FALSE,
    id
FROM nova_decolagem;

WITH nova_decolagem AS (
    INSERT INTO decolagem (
        data_inicio,
        data_fim,
        cenario,
        status,
        motivo_aborto
    )
    VALUES (
        '2026-09-13 14:32:47',
        '2026-09-13 14:33:47',
        'FALHA_CRITICA',
        'DECOLAGEM ABORTADA',
        'Falha crítica persistente no sistema elétrico'
    )
    RETURNING id
)
INSERT INTO telemetria (
    data_hora,
    tempo_decolagem,
    temperatura_interna,
    temperatura_externa,
    integridade_estrutural_ok,
    vibracao_estrutural_g,
    nivel_energia,
    pressao_lh2_psi,
    pressao_lox_psi,
    motor_ok,
    navegacao_ok,
    comunicacao_ok,
    sistema_eletrico_ok,
    resfriamento_ativo,
    pressurizacao_ativa,
    decolagem_id
)
SELECT
    '2026-09-13 14:33:47',
    60,
    23.98,
    17.76,
    TRUE,
    1.500,
    91.50,
    125.90,
    127.80,
    TRUE,
    TRUE,
    TRUE,
    FALSE,
    TRUE,
    FALSE,
    id
FROM nova_decolagem;
