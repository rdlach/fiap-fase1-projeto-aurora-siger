CREATE TABLE IF NOT EXISTS execucoes_pre_decolagem (
    id SERIAL PRIMARY KEY,
    data_hora TIMESTAMP NOT NULL,
    origem_dados VARCHAR(80) NOT NULL,
    temperatura_interna_c NUMERIC(8, 2) NOT NULL,
    temperatura_externa_c NUMERIC(8, 2) NOT NULL,
    integridade_estrutural INTEGER NOT NULL,
    nivel_energia_percentual NUMERIC(8, 2) NOT NULL,
    pressao_tanques_percentual NUMERIC(8, 2) NOT NULL,
    modulos_criticos VARCHAR(20) NOT NULL,
    energia_disponivel_kwh NUMERIC(10, 2) NOT NULL,
    perdas_kwh NUMERIC(10, 2) NOT NULL,
    energia_restante_kwh NUMERIC(10, 2) NOT NULL,
    autonomia_horas NUMERIC(10, 2) NOT NULL,
    decisao_final VARCHAR(40) NOT NULL
);
