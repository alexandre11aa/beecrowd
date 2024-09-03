<<<<<<< HEAD
-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS customers (
    id numeric PRIMARY KEY,
    name varchar,
    street varchar,
    city varchar
);

-- Inserção dos dados na tabela

INSERT 
    INTO customers (id, name, street, city) VALUES
        (1, 'Giovanna Goncalves Oliveira', 'Rua Mato Grosso'               , 'Canoas'),
        (2, 'Kauã Azevedo Ribeiro'       , 'Travessa Ibiá'                 , 'Uberlândia'),
        (3, 'Rebeca Barbosa Santos'      , 'Rua Observatório Meteorológico', 'Salvador'),
        (4, 'Sarah Carvalho Correia'     , 'Rua Antônio Carlos da Silva'   , 'Uberlândia'),
        (5, 'João Almeida Lima'          , 'Rua Rio Taiuva'                , 'Ponta Grossa'),
        (6, 'Diogo Melo Dias'            , 'Rua Duzentos e Cinqüenta'      , 'Várzea Grande')
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2615)

SELECT 
    DISTINCT c.city
FROM 
    customers c
=======
-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS customers (
    id numeric PRIMARY KEY,
    name varchar,
    street varchar,
    city varchar
);

-- Inserção dos dados na tabela

INSERT 
    INTO customers (id, name, street, city) VALUES
        (1, 'Giovanna Goncalves Oliveira', 'Rua Mato Grosso'               , 'Canoas'),
        (2, 'Kauã Azevedo Ribeiro'       , 'Travessa Ibiá'                 , 'Uberlândia'),
        (3, 'Rebeca Barbosa Santos'      , 'Rua Observatório Meteorológico', 'Salvador'),
        (4, 'Sarah Carvalho Correia'     , 'Rua Antônio Carlos da Silva'   , 'Uberlândia'),
        (5, 'João Almeida Lima'          , 'Rua Rio Taiuva'                , 'Ponta Grossa'),
        (6, 'Diogo Melo Dias'            , 'Rua Duzentos e Cinqüenta'      , 'Várzea Grande')
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2615)

SELECT 
    DISTINCT c.city
FROM 
    customers c
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
