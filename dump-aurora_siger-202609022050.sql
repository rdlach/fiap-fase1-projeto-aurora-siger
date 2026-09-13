--
-- PostgreSQL database dump
--

\restrict dEbjGZ4VdvgEFaFoUAfhANcnXad67ofEtBF3XFv33kvaPZBeQll6iXqITVP0LUk

-- Dumped from database version 17.10
-- Dumped by pg_dump version 17.10

-- Started on 2026-09-02 20:50:35

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 16932)
-- Name: decolagem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.decolagem (
    id integer NOT NULL,
    data_inicio timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    data_fim timestamp without time zone,
    cenario character varying(30),
    status character varying(30),
    motivo_aborto character varying(200)
);


ALTER TABLE public.decolagem OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16931)
-- Name: decolagem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.decolagem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.decolagem_id_seq OWNER TO postgres;

--
-- TOC entry 4920 (class 0 OID 0)
-- Dependencies: 219
-- Name: decolagem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.decolagem_id_seq OWNED BY public.decolagem.id;


--
-- TOC entry 222 (class 1259 OID 16940)
-- Name: parametros_seguranca; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parametros_seguranca (
    id integer NOT NULL,
    parametro character varying(50) NOT NULL,
    unidade character varying(20),
    valor_minimo numeric(8,3),
    valor_maximo numeric(8,3)
);


ALTER TABLE public.parametros_seguranca OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16939)
-- Name: parametros_seguranca_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parametros_seguranca_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.parametros_seguranca_id_seq OWNER TO postgres;

--
-- TOC entry 4921 (class 0 OID 0)
-- Dependencies: 221
-- Name: parametros_seguranca_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parametros_seguranca_id_seq OWNED BY public.parametros_seguranca.id;


--
-- TOC entry 218 (class 1259 OID 16924)
-- Name: telemetria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.telemetria (
    id integer NOT NULL,
    data_hora timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    tempo_decolagem integer,
    temperatura_interna numeric(6,2),
    temperatura_externa numeric(6,2),
    integridade_estrutural_ok boolean,
    vibracao_estrutural_g numeric(6,3),
    nivel_energia numeric(6,2),
    pressao_lh2_psi numeric(6,2),
    pressao_lox_psi numeric(6,2),
    motor_ok boolean,
    navegacao_ok boolean,
    comunicacao_ok boolean,
    sistema_eletrico_ok boolean,
    resfriamento_ativo boolean,
    pressurizacao_ativa boolean,
    decolagem_id integer
);


ALTER TABLE public.telemetria OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16923)
-- Name: telemetria_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.telemetria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.telemetria_id_seq OWNER TO postgres;

--
-- TOC entry 4922 (class 0 OID 0)
-- Dependencies: 217
-- Name: telemetria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.telemetria_id_seq OWNED BY public.telemetria.id;


--
-- TOC entry 4754 (class 2604 OID 16935)
-- Name: decolagem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.decolagem ALTER COLUMN id SET DEFAULT nextval('public.decolagem_id_seq'::regclass);


--
-- TOC entry 4756 (class 2604 OID 16943)
-- Name: parametros_seguranca id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parametros_seguranca ALTER COLUMN id SET DEFAULT nextval('public.parametros_seguranca_id_seq'::regclass);


--
-- TOC entry 4752 (class 2604 OID 16927)
-- Name: telemetria id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.telemetria ALTER COLUMN id SET DEFAULT nextval('public.telemetria_id_seq'::regclass);


--
-- TOC entry 4912 (class 0 OID 16932)
-- Dependencies: 220
-- Data for Name: decolagem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.decolagem (id, data_inicio, data_fim, cenario, status, motivo_aborto) FROM stdin;
1	2026-09-02 20:46:56.87714	2026-09-02 20:47:56.87714	SUCESSO_DIRETO	PRONTO PARA DECOLAR	\N
2	2026-09-02 20:48:56.87714	2026-09-02 20:49:56.87714	ERRO_CORRIGIDO	PRONTO PARA DECOLAR	\N
3	2026-09-02 20:50:56.87714	2026-09-02 20:51:56.87714	FALHA_CRITICA	DECOLAGEM ABORTADA	Falha crítica persistente no sistema elétrico
\.


--
-- TOC entry 4914 (class 0 OID 16940)
-- Dependencies: 222
-- Data for Name: parametros_seguranca; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.parametros_seguranca (id, parametro, unidade, valor_minimo, valor_maximo) FROM stdin;
1	temperatura_interna	C	18.000	27.000
2	temperatura_externa	C	10.000	34.000
3	vibracao_estrutural_g	g RMS	0.000	0.050
4	nivel_energia	%	80.000	100.000
5	pressao_lh2_psi	psi	31.000	34.000
6	pressao_lox_psi	psi	38.000	41.000
\.


--
-- TOC entry 4910 (class 0 OID 16924)
-- Dependencies: 218
-- Data for Name: telemetria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.telemetria (id, data_hora, tempo_decolagem, temperatura_interna, temperatura_externa, integridade_estrutural_ok, vibracao_estrutural_g, nivel_energia, pressao_lh2_psi, pressao_lox_psi, motor_ok, navegacao_ok, comunicacao_ok, sistema_eletrico_ok, resfriamento_ativo, pressurizacao_ativa, decolagem_id) FROM stdin;
1	2026-09-02 20:46:56.87714	0	23.00	18.00	t	0.600	100.00	123.00	126.00	t	t	t	t	t	f	1
2	2026-09-02 20:46:57.87714	1	23.01	18.00	t	0.615	99.90	123.05	126.03	t	t	t	t	t	f	1
3	2026-09-02 20:46:58.87714	2	23.02	17.99	t	0.630	99.80	123.10	126.06	t	t	t	t	t	f	1
4	2026-09-02 20:46:59.87714	3	23.03	17.99	t	0.645	99.70	123.15	126.09	t	t	t	t	t	f	1
5	2026-09-02 20:47:00.87714	4	23.04	17.98	t	0.660	99.60	123.20	126.12	t	t	t	t	t	f	1
6	2026-09-02 20:47:01.87714	5	23.05	17.98	t	0.675	99.50	123.25	126.15	t	t	t	t	t	f	1
7	2026-09-02 20:47:02.87714	6	23.06	17.97	t	0.690	99.40	123.30	126.18	t	t	t	t	t	f	1
8	2026-09-02 20:47:03.87714	7	23.07	17.97	t	0.705	99.30	123.35	126.21	t	t	t	t	t	f	1
9	2026-09-02 20:47:04.87714	8	23.08	17.96	t	0.720	99.20	123.40	126.24	t	t	t	t	t	f	1
10	2026-09-02 20:47:05.87714	9	23.09	17.96	t	0.735	99.10	123.45	126.27	t	t	t	t	t	f	1
11	2026-09-02 20:47:06.87714	10	23.10	17.95	t	0.750	99.00	123.50	126.30	t	t	t	t	t	f	1
12	2026-09-02 20:47:07.87714	11	23.11	17.95	t	0.765	98.90	123.55	126.33	t	t	t	t	t	f	1
13	2026-09-02 20:47:08.87714	12	23.12	17.94	t	0.780	98.80	123.60	126.36	t	t	t	t	t	f	1
14	2026-09-02 20:47:09.87714	13	23.13	17.94	t	0.795	98.70	123.65	126.39	t	t	t	t	t	f	1
15	2026-09-02 20:47:10.87714	14	23.14	17.93	t	0.810	98.60	123.70	126.42	t	t	t	t	t	f	1
16	2026-09-02 20:47:11.87714	15	23.15	17.93	t	0.825	98.50	123.75	126.45	t	t	t	t	t	f	1
17	2026-09-02 20:47:12.87714	16	23.16	17.92	t	0.840	98.40	123.80	126.48	t	t	t	t	t	f	1
18	2026-09-02 20:47:13.87714	17	23.17	17.92	t	0.855	98.30	123.85	126.51	t	t	t	t	t	f	1
19	2026-09-02 20:47:14.87714	18	23.18	17.91	t	0.870	98.20	123.90	126.54	t	t	t	t	t	f	1
20	2026-09-02 20:47:15.87714	19	23.19	17.91	t	0.885	98.10	123.95	126.57	t	t	t	t	t	f	1
21	2026-09-02 20:47:16.87714	20	23.20	17.90	t	0.900	98.00	124.00	126.60	t	t	t	t	t	f	1
22	2026-09-02 20:47:17.87714	21	23.21	17.90	t	0.915	97.90	124.05	126.63	t	t	t	t	t	f	1
23	2026-09-02 20:47:18.87714	22	23.22	17.89	t	0.930	97.80	124.10	126.66	t	t	t	t	t	f	1
24	2026-09-02 20:47:19.87714	23	23.23	17.89	t	0.945	97.70	124.15	126.69	t	t	t	t	t	f	1
25	2026-09-02 20:47:20.87714	24	23.24	17.88	t	0.960	97.60	124.20	126.72	t	t	t	t	t	f	1
26	2026-09-02 20:47:21.87714	25	23.25	17.88	t	0.975	97.50	124.25	126.75	t	t	t	t	t	f	1
27	2026-09-02 20:47:22.87714	26	23.26	17.87	t	0.990	97.40	124.30	126.78	t	t	t	t	t	f	1
28	2026-09-02 20:47:23.87714	27	23.27	17.87	t	1.005	97.30	124.35	126.81	t	t	t	t	t	f	1
29	2026-09-02 20:47:24.87714	28	23.28	17.86	t	1.020	97.20	124.40	126.84	t	t	t	t	t	f	1
30	2026-09-02 20:47:25.87714	29	23.29	17.86	t	1.035	97.10	124.45	126.87	t	t	t	t	t	f	1
31	2026-09-02 20:47:26.87714	30	23.30	17.85	t	1.050	97.00	124.50	126.90	t	t	t	t	t	f	1
32	2026-09-02 20:47:27.87714	31	23.31	17.85	t	1.065	96.90	124.55	126.93	t	t	t	t	t	f	1
33	2026-09-02 20:47:28.87714	32	23.32	17.84	t	1.080	96.80	124.60	126.96	t	t	t	t	t	f	1
34	2026-09-02 20:47:29.87714	33	23.33	17.84	t	1.095	96.70	124.65	126.99	t	t	t	t	t	f	1
35	2026-09-02 20:47:30.87714	34	23.34	17.83	t	1.110	96.60	124.70	127.02	t	t	t	t	t	f	1
36	2026-09-02 20:47:31.87714	35	23.35	17.83	t	1.125	96.50	124.75	127.05	t	t	t	t	t	f	1
37	2026-09-02 20:47:32.87714	36	23.36	17.82	t	1.140	96.40	124.80	127.08	t	t	t	t	t	f	1
38	2026-09-02 20:47:33.87714	37	23.37	17.82	t	1.155	96.30	124.85	127.11	t	t	t	t	t	f	1
39	2026-09-02 20:47:34.87714	38	23.38	17.81	t	1.170	96.20	124.90	127.14	t	t	t	t	t	f	1
40	2026-09-02 20:47:35.87714	39	23.39	17.81	t	1.185	96.10	124.95	127.17	t	t	t	t	t	f	1
41	2026-09-02 20:47:36.87714	40	23.40	17.80	t	1.200	96.00	125.00	127.20	t	t	t	t	t	f	1
42	2026-09-02 20:47:37.87714	41	23.41	17.80	t	1.215	95.90	125.05	127.23	t	t	t	t	t	f	1
43	2026-09-02 20:47:38.87714	42	23.42	17.79	t	1.230	95.80	125.10	127.26	t	t	t	t	t	f	1
44	2026-09-02 20:47:39.87714	43	23.43	17.79	t	1.245	95.70	125.15	127.29	t	t	t	t	t	f	1
45	2026-09-02 20:47:40.87714	44	23.44	17.78	t	1.260	95.60	125.20	127.32	t	t	t	t	t	f	1
46	2026-09-02 20:47:41.87714	45	23.45	17.78	t	1.275	95.50	125.25	127.35	t	t	t	t	t	f	1
47	2026-09-02 20:47:42.87714	46	23.46	17.77	t	1.290	95.40	125.30	127.38	t	t	t	t	t	f	1
48	2026-09-02 20:47:43.87714	47	23.47	17.77	t	1.305	95.30	125.35	127.41	t	t	t	t	t	f	1
49	2026-09-02 20:47:44.87714	48	23.48	17.76	t	1.320	95.20	125.40	127.44	t	t	t	t	t	f	1
50	2026-09-02 20:47:45.87714	49	23.49	17.76	t	1.335	95.10	125.45	127.47	t	t	t	t	t	f	1
51	2026-09-02 20:47:46.87714	50	23.50	17.75	t	1.350	95.00	125.50	127.50	t	t	t	t	t	f	1
52	2026-09-02 20:47:47.87714	51	23.51	17.75	t	1.365	94.90	125.55	127.53	t	t	t	t	t	f	1
53	2026-09-02 20:47:48.87714	52	23.52	17.74	t	1.380	94.80	125.60	127.56	t	t	t	t	t	f	1
54	2026-09-02 20:47:49.87714	53	23.53	17.74	t	1.395	94.70	125.65	127.59	t	t	t	t	t	f	1
55	2026-09-02 20:47:50.87714	54	23.54	17.73	t	1.410	94.60	125.70	127.62	t	t	t	t	t	f	1
56	2026-09-02 20:47:51.87714	55	23.55	17.73	t	1.425	94.50	125.75	127.65	t	t	t	t	t	f	1
57	2026-09-02 20:47:52.87714	56	23.56	17.72	t	1.440	94.40	125.80	127.68	t	t	t	t	t	f	1
58	2026-09-02 20:47:53.87714	57	23.57	17.72	t	1.455	94.30	125.85	127.71	t	t	t	t	t	f	1
59	2026-09-02 20:47:54.87714	58	23.58	17.71	t	1.470	94.20	125.90	127.74	t	t	t	t	t	f	1
60	2026-09-02 20:47:55.87714	59	23.59	17.71	t	1.485	94.10	125.95	127.77	t	t	t	t	t	f	1
61	2026-09-02 20:47:56.87714	60	23.60	17.70	t	1.500	94.00	126.00	127.80	t	t	t	t	t	f	1
62	2026-09-02 20:48:56.87714	0	23.10	18.20	t	0.650	100.00	124.00	126.00	t	t	t	t	t	f	2
63	2026-09-02 20:48:57.87714	1	23.11	18.20	t	0.664	99.89	124.04	126.03	t	t	t	t	t	f	2
64	2026-09-02 20:48:58.87714	2	23.12	18.19	t	0.678	99.78	124.07	126.06	t	t	t	t	t	f	2
65	2026-09-02 20:48:59.87714	3	23.12	18.19	t	0.692	99.67	124.11	126.09	t	t	t	t	t	f	2
66	2026-09-02 20:49:00.87714	4	23.13	18.18	t	0.706	99.56	124.14	126.12	t	t	t	t	t	f	2
67	2026-09-02 20:49:01.87714	5	23.14	18.18	t	0.720	99.45	124.18	126.15	t	t	t	t	t	f	2
68	2026-09-02 20:49:02.87714	6	23.15	18.17	t	0.734	99.34	124.21	126.18	t	t	t	t	t	f	2
69	2026-09-02 20:49:03.87714	7	23.16	18.17	t	0.748	99.23	124.25	126.21	t	t	t	t	t	f	2
70	2026-09-02 20:49:04.87714	8	23.16	18.16	t	0.762	99.12	124.28	126.24	t	t	t	t	t	f	2
71	2026-09-02 20:49:05.87714	9	23.17	18.16	t	0.776	99.01	124.32	126.27	t	t	t	t	t	f	2
72	2026-09-02 20:49:06.87714	10	23.18	18.15	t	0.790	98.90	124.35	126.30	t	t	t	t	t	f	2
73	2026-09-02 20:49:07.87714	11	23.19	18.15	t	0.804	98.79	124.39	126.33	t	t	t	t	t	f	2
74	2026-09-02 20:49:08.87714	12	23.20	18.14	t	0.818	98.68	124.42	126.36	t	t	t	t	t	f	2
75	2026-09-02 20:49:09.87714	13	23.20	18.14	t	0.832	98.57	124.46	126.39	t	t	t	t	t	f	2
76	2026-09-02 20:49:10.87714	14	23.21	18.13	t	0.846	98.46	124.49	126.42	t	t	t	t	t	f	2
77	2026-09-02 20:49:11.87714	15	23.22	18.13	t	0.860	98.35	124.53	126.45	t	t	t	t	t	f	2
78	2026-09-02 20:49:12.87714	16	23.23	18.12	t	0.874	98.24	124.56	126.48	t	t	t	t	t	f	2
79	2026-09-02 20:49:13.87714	17	23.24	18.12	t	0.888	98.13	124.60	126.51	t	t	t	t	t	f	2
80	2026-09-02 20:49:14.87714	18	23.24	18.11	t	0.902	98.02	124.63	126.54	t	t	t	t	t	f	2
81	2026-09-02 20:49:15.87714	19	23.25	18.11	t	0.916	97.91	124.67	126.57	t	t	t	t	t	f	2
82	2026-09-02 20:49:16.87714	20	23.26	18.10	t	0.930	97.80	124.70	98.00	t	t	t	t	t	t	2
83	2026-09-02 20:49:17.87714	21	23.27	18.10	t	0.944	97.69	124.74	97.00	t	t	t	t	t	t	2
84	2026-09-02 20:49:18.87714	22	23.28	18.09	t	0.958	97.58	124.77	96.00	t	t	t	t	t	t	2
85	2026-09-02 20:49:19.87714	23	23.28	18.09	t	0.972	97.47	124.81	95.00	t	t	t	t	t	t	2
86	2026-09-02 20:49:20.87714	24	23.29	18.08	t	0.986	97.36	124.84	94.00	t	t	t	t	t	t	2
87	2026-09-02 20:49:21.87714	25	23.30	18.08	t	1.000	97.25	124.88	94.00	t	t	t	t	t	t	2
88	2026-09-02 20:49:22.87714	26	23.31	18.07	t	1.014	97.14	124.91	94.50	t	t	t	t	t	t	2
89	2026-09-02 20:49:23.87714	27	23.32	18.07	t	1.028	97.03	124.95	95.00	t	t	t	t	t	t	2
90	2026-09-02 20:49:24.87714	28	23.32	18.06	t	1.042	96.92	124.98	95.50	t	t	t	t	t	t	2
91	2026-09-02 20:49:25.87714	29	23.33	18.06	t	1.056	96.81	125.02	96.00	t	t	t	t	t	t	2
92	2026-09-02 20:49:26.87714	30	23.34	18.05	t	1.070	96.70	125.05	97.00	t	t	t	t	t	t	2
93	2026-09-02 20:49:27.87714	31	23.35	18.05	t	1.084	96.59	125.09	98.00	t	t	t	t	t	t	2
94	2026-09-02 20:49:28.87714	32	23.36	18.04	t	1.098	96.48	125.12	99.00	t	t	t	t	t	t	2
95	2026-09-02 20:49:29.87714	33	23.36	18.04	t	1.112	96.37	125.16	100.00	t	t	t	t	t	t	2
96	2026-09-02 20:49:30.87714	34	23.37	18.03	t	1.126	96.26	125.19	101.00	t	t	t	t	t	t	2
97	2026-09-02 20:49:31.87714	35	23.38	18.03	t	1.140	96.15	125.23	102.00	t	t	t	t	t	t	2
98	2026-09-02 20:49:32.87714	36	23.39	18.02	t	1.154	96.04	125.26	103.00	t	t	t	t	t	t	2
99	2026-09-02 20:49:33.87714	37	23.40	18.02	t	1.168	95.93	125.30	104.00	t	t	t	t	t	t	2
100	2026-09-02 20:49:34.87714	38	23.40	18.01	t	1.182	95.82	125.33	105.00	t	t	t	t	t	t	2
101	2026-09-02 20:49:35.87714	39	23.41	18.01	t	1.196	95.71	125.37	106.00	t	t	t	t	t	t	2
102	2026-09-02 20:49:36.87714	40	23.42	18.00	t	1.210	95.60	125.40	124.00	t	t	t	t	t	f	2
103	2026-09-02 20:49:37.87714	41	23.43	18.00	t	1.224	95.49	125.44	124.10	t	t	t	t	t	f	2
104	2026-09-02 20:49:38.87714	42	23.44	17.99	t	1.238	95.38	125.47	124.20	t	t	t	t	t	f	2
105	2026-09-02 20:49:39.87714	43	23.44	17.99	t	1.252	95.27	125.51	124.30	t	t	t	t	t	f	2
106	2026-09-02 20:49:40.87714	44	23.45	17.98	t	1.266	95.16	125.54	124.40	t	t	t	t	t	f	2
107	2026-09-02 20:49:41.87714	45	23.46	17.98	t	1.280	95.05	125.58	124.50	t	t	t	t	t	f	2
108	2026-09-02 20:49:42.87714	46	23.47	17.97	t	1.294	94.94	125.61	124.60	t	t	t	t	t	f	2
109	2026-09-02 20:49:43.87714	47	23.48	17.97	t	1.308	94.83	125.65	124.70	t	t	t	t	t	f	2
110	2026-09-02 20:49:44.87714	48	23.48	17.96	t	1.322	94.72	125.68	124.80	t	t	t	t	t	f	2
111	2026-09-02 20:49:45.87714	49	23.49	17.96	t	1.336	94.61	125.72	124.90	t	t	t	t	t	f	2
112	2026-09-02 20:49:46.87714	50	23.50	17.95	t	1.350	94.50	125.75	125.00	t	t	t	t	t	f	2
113	2026-09-02 20:49:47.87714	51	23.51	17.95	t	1.364	94.39	125.79	125.10	t	t	t	t	t	f	2
114	2026-09-02 20:49:48.87714	52	23.52	17.94	t	1.378	94.28	125.82	125.20	t	t	t	t	t	f	2
115	2026-09-02 20:49:49.87714	53	23.52	17.94	t	1.392	94.17	125.86	125.30	t	t	t	t	t	f	2
116	2026-09-02 20:49:50.87714	54	23.53	17.93	t	1.406	94.06	125.89	125.40	t	t	t	t	t	f	2
117	2026-09-02 20:49:51.87714	55	23.54	17.93	t	1.420	93.95	125.93	125.50	t	t	t	t	t	f	2
118	2026-09-02 20:49:52.87714	56	23.55	17.92	t	1.434	93.84	125.96	125.60	t	t	t	t	t	f	2
119	2026-09-02 20:49:53.87714	57	23.56	17.92	t	1.448	93.73	126.00	125.70	t	t	t	t	t	f	2
120	2026-09-02 20:49:54.87714	58	23.56	17.91	t	1.462	93.62	126.03	125.80	t	t	t	t	t	f	2
121	2026-09-02 20:49:55.87714	59	23.57	17.91	t	1.476	93.51	126.07	125.90	t	t	t	t	t	f	2
122	2026-09-02 20:49:56.87714	60	23.58	17.90	t	1.490	93.40	126.10	126.00	t	t	t	t	t	f	2
123	2026-09-02 20:50:56.87714	0	23.00	18.00	t	0.600	100.00	123.50	126.00	t	t	t	t	t	f	3
124	2026-09-02 20:50:57.87714	1	23.01	18.00	t	0.615	99.90	123.54	126.03	t	t	t	t	t	f	3
125	2026-09-02 20:50:58.87714	2	23.02	17.99	t	0.630	99.80	123.58	126.06	t	t	t	t	t	f	3
126	2026-09-02 20:50:59.87714	3	23.03	17.99	t	0.645	99.70	123.62	126.09	t	t	t	t	t	f	3
127	2026-09-02 20:51:00.87714	4	23.04	17.98	t	0.660	99.60	123.66	126.12	t	t	t	t	t	f	3
128	2026-09-02 20:51:01.87714	5	23.05	17.98	t	0.675	99.50	123.70	126.15	t	t	t	t	t	f	3
129	2026-09-02 20:51:02.87714	6	23.06	17.98	t	0.690	99.40	123.74	126.18	t	t	t	t	t	f	3
130	2026-09-02 20:51:03.87714	7	23.07	17.97	t	0.705	99.30	123.78	126.21	t	t	t	t	t	f	3
131	2026-09-02 20:51:04.87714	8	23.08	17.97	t	0.720	99.20	123.82	126.24	t	t	t	t	t	f	3
132	2026-09-02 20:51:05.87714	9	23.09	17.96	t	0.735	99.10	123.86	126.27	t	t	t	t	t	f	3
133	2026-09-02 20:51:06.87714	10	23.10	17.96	t	0.750	99.00	123.90	126.30	t	t	t	t	t	f	3
134	2026-09-02 20:51:07.87714	11	23.11	17.96	t	0.765	98.90	123.94	126.33	t	t	t	t	t	f	3
135	2026-09-02 20:51:08.87714	12	23.12	17.95	t	0.780	98.80	123.98	126.36	t	t	t	t	t	f	3
136	2026-09-02 20:51:09.87714	13	23.13	17.95	t	0.795	98.70	124.02	126.39	t	t	t	t	t	f	3
137	2026-09-02 20:51:10.87714	14	23.14	17.94	t	0.810	98.60	124.06	126.42	t	t	t	t	t	f	3
138	2026-09-02 20:51:11.87714	15	23.15	17.94	t	0.825	98.50	124.10	126.45	t	t	t	t	t	f	3
139	2026-09-02 20:51:12.87714	16	23.16	17.94	t	0.840	98.40	124.14	126.48	t	t	t	t	t	f	3
140	2026-09-02 20:51:13.87714	17	23.17	17.93	t	0.855	98.30	124.18	126.51	t	t	t	t	t	f	3
141	2026-09-02 20:51:14.87714	18	23.18	17.93	t	0.870	98.20	124.22	126.54	t	t	t	t	t	f	3
142	2026-09-02 20:51:15.87714	19	23.19	17.92	t	0.885	98.10	124.26	126.57	t	t	t	t	t	f	3
143	2026-09-02 20:51:16.87714	20	23.20	17.92	t	0.900	98.00	124.30	126.60	t	t	t	t	t	f	3
144	2026-09-02 20:51:17.87714	21	23.21	17.92	t	0.915	97.90	124.34	126.63	t	t	t	t	t	f	3
145	2026-09-02 20:51:18.87714	22	23.22	17.91	t	0.930	97.80	124.38	126.66	t	t	t	t	t	f	3
146	2026-09-02 20:51:19.87714	23	23.23	17.91	t	0.945	97.70	124.42	126.69	t	t	t	t	t	f	3
147	2026-09-02 20:51:20.87714	24	23.24	17.90	t	0.960	97.60	124.46	126.72	t	t	t	t	t	f	3
148	2026-09-02 20:51:21.87714	25	23.25	17.90	t	0.975	97.50	124.50	126.75	t	t	t	t	t	f	3
149	2026-09-02 20:51:22.87714	26	23.26	17.90	t	0.990	97.40	124.54	126.78	t	t	t	t	t	f	3
150	2026-09-02 20:51:23.87714	27	23.27	17.89	t	1.005	97.30	124.58	126.81	t	t	t	t	t	f	3
151	2026-09-02 20:51:24.87714	28	23.28	17.89	t	1.020	97.20	124.62	126.84	t	t	t	t	t	f	3
152	2026-09-02 20:51:25.87714	29	23.29	17.88	t	1.035	97.10	124.66	126.87	t	t	t	t	t	f	3
153	2026-09-02 20:51:26.87714	30	23.30	17.88	t	1.050	97.00	124.70	126.90	t	t	t	t	t	f	3
154	2026-09-02 20:51:27.87714	31	23.31	17.88	t	1.065	96.90	124.74	126.93	t	t	t	t	t	f	3
155	2026-09-02 20:51:28.87714	32	23.32	17.87	t	1.080	96.80	124.78	126.96	t	t	t	t	t	f	3
156	2026-09-02 20:51:29.87714	33	23.33	17.87	t	1.095	96.70	124.82	126.99	t	t	t	t	t	f	3
157	2026-09-02 20:51:30.87714	34	23.34	17.86	t	1.110	96.60	124.86	127.02	t	t	t	t	t	f	3
158	2026-09-02 20:51:31.87714	35	23.35	17.86	t	1.125	96.50	124.90	127.05	t	t	t	f	t	f	3
159	2026-09-02 20:51:32.87714	36	23.38	17.86	t	1.140	96.30	124.94	127.08	t	t	t	f	t	f	3
160	2026-09-02 20:51:33.87714	37	23.40	17.85	t	1.155	96.10	124.98	127.11	t	t	t	f	t	f	3
161	2026-09-02 20:51:34.87714	38	23.43	17.85	t	1.170	95.90	125.02	127.14	t	t	t	f	t	f	3
162	2026-09-02 20:51:35.87714	39	23.45	17.84	t	1.185	95.70	125.06	127.17	t	t	t	f	t	f	3
163	2026-09-02 20:51:36.87714	40	23.48	17.84	t	1.200	95.50	125.10	127.20	t	t	t	f	t	f	3
164	2026-09-02 20:51:37.87714	41	23.50	17.84	t	1.215	95.30	125.14	127.23	t	t	t	f	t	f	3
165	2026-09-02 20:51:38.87714	42	23.53	17.83	t	1.230	95.10	125.18	127.26	t	t	t	f	t	f	3
166	2026-09-02 20:51:39.87714	43	23.55	17.83	t	1.245	94.90	125.22	127.29	t	t	t	f	t	f	3
167	2026-09-02 20:51:40.87714	44	23.58	17.82	t	1.260	94.70	125.26	127.32	t	t	t	f	t	f	3
168	2026-09-02 20:51:41.87714	45	23.60	17.82	t	1.275	94.50	125.30	127.35	t	t	t	f	t	f	3
169	2026-09-02 20:51:42.87714	46	23.63	17.82	t	1.290	94.30	125.34	127.38	t	t	t	f	t	f	3
170	2026-09-02 20:51:43.87714	47	23.65	17.81	t	1.305	94.10	125.38	127.41	t	t	t	f	t	f	3
171	2026-09-02 20:51:44.87714	48	23.68	17.81	t	1.320	93.90	125.42	127.44	t	t	t	f	t	f	3
172	2026-09-02 20:51:45.87714	49	23.70	17.80	t	1.335	93.70	125.46	127.47	t	t	t	f	t	f	3
173	2026-09-02 20:51:46.87714	50	23.73	17.80	t	1.350	93.50	125.50	127.50	t	t	t	f	t	f	3
174	2026-09-02 20:51:47.87714	51	23.75	17.80	t	1.365	93.30	125.54	127.53	t	t	t	f	t	f	3
175	2026-09-02 20:51:48.87714	52	23.78	17.79	t	1.380	93.10	125.58	127.56	t	t	t	f	t	f	3
176	2026-09-02 20:51:49.87714	53	23.80	17.79	t	1.395	92.90	125.62	127.59	t	t	t	f	t	f	3
177	2026-09-02 20:51:50.87714	54	23.83	17.78	t	1.410	92.70	125.66	127.62	t	t	t	f	t	f	3
178	2026-09-02 20:51:51.87714	55	23.85	17.78	t	1.425	92.50	125.70	127.65	t	t	t	f	t	f	3
179	2026-09-02 20:51:52.87714	56	23.88	17.78	t	1.440	92.30	125.74	127.68	t	t	t	f	t	f	3
180	2026-09-02 20:51:53.87714	57	23.90	17.77	t	1.455	92.10	125.78	127.71	t	t	t	f	t	f	3
181	2026-09-02 20:51:54.87714	58	23.93	17.77	t	1.470	91.90	125.82	127.74	t	t	t	f	t	f	3
182	2026-09-02 20:51:55.87714	59	23.95	17.76	t	1.485	91.70	125.86	127.77	t	t	t	f	t	f	3
183	2026-09-02 20:51:56.87714	60	23.98	17.76	t	1.500	91.50	125.90	127.80	t	t	t	f	t	f	3
\.


--
-- TOC entry 4923 (class 0 OID 0)
-- Dependencies: 219
-- Name: decolagem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.decolagem_id_seq', 3, true);


--
-- TOC entry 4924 (class 0 OID 0)
-- Dependencies: 221
-- Name: parametros_seguranca_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.parametros_seguranca_id_seq', 6, true);


--
-- TOC entry 4925 (class 0 OID 0)
-- Dependencies: 217
-- Name: telemetria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.telemetria_id_seq', 183, true);


--
-- TOC entry 4760 (class 2606 OID 16938)
-- Name: decolagem decolagem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.decolagem
    ADD CONSTRAINT decolagem_pkey PRIMARY KEY (id);


--
-- TOC entry 4762 (class 2606 OID 16945)
-- Name: parametros_seguranca parametros_seguranca_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parametros_seguranca
    ADD CONSTRAINT parametros_seguranca_pkey PRIMARY KEY (id);


--
-- TOC entry 4758 (class 2606 OID 16930)
-- Name: telemetria telemetria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.telemetria
    ADD CONSTRAINT telemetria_pkey PRIMARY KEY (id);


--
-- TOC entry 4763 (class 2606 OID 16946)
-- Name: telemetria fk_telemetria_decolagem; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.telemetria
    ADD CONSTRAINT fk_telemetria_decolagem FOREIGN KEY (decolagem_id) REFERENCES public.decolagem(id);


-- Completed on 2026-09-02 20:50:35

--
-- PostgreSQL database dump complete
--

\unrestrict dEbjGZ4VdvgEFaFoUAfhANcnXad67ofEtBF3XFv33kvaPZBeQll6iXqITVP0LUk

