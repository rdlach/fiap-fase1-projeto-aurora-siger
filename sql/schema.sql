CREATE TABLE IF NOT EXISTS decolagem (
    id SERIAL PRIMARY KEY,
    data_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_fim TIMESTAMP,
    cenario VARCHAR(30),
    status VARCHAR(30),
    motivo_aborto VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS parametros_seguranca (
    id SERIAL PRIMARY KEY,
    parametro VARCHAR(50) NOT NULL UNIQUE,
    unidade VARCHAR(20),
    valor_minimo NUMERIC(8, 3),
    valor_maximo NUMERIC(8, 3)
);

CREATE TABLE IF NOT EXISTS telemetria (
    id SERIAL PRIMARY KEY,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tempo_decolagem INTEGER,
    temperatura_interna NUMERIC(6, 2),
    temperatura_externa NUMERIC(6, 2),
    integridade_estrutural_ok BOOLEAN,
    vibracao_estrutural_g NUMERIC(6, 3),
    nivel_energia NUMERIC(6, 2),
    pressao_lh2_psi NUMERIC(6, 2),
    pressao_lox_psi NUMERIC(6, 2),
    motor_ok BOOLEAN,
    navegacao_ok BOOLEAN,
    comunicacao_ok BOOLEAN,
    sistema_eletrico_ok BOOLEAN,
    resfriamento_ativo BOOLEAN,
    pressurizacao_ativa BOOLEAN,
    decolagem_id INTEGER REFERENCES decolagem(id)
);

INSERT INTO parametros_seguranca (
    parametro,
    unidade,
    valor_minimo,
    valor_maximo
)
VALUES
    ('temperatura_interna', 'C', 18.000, 27.000),
    ('temperatura_externa', 'C', 10.000, 34.000),
    ('vibracao_estrutural_g', 'g RMS', 0.000, 1.500),
    ('nivel_energia', '%', 80.000, 100.000),
    ('pressao_lh2_psi', 'psi', 120.000, 130.000),
    ('pressao_lox_psi', 'psi', 120.000, 130.000)
ON CONFLICT (parametro) DO NOTHING;
