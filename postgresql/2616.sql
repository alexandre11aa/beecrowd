-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS customers (
    id numeric PRIMARY KEY,
    name varchar,
    street varchar,
    city varchar
);

CREATE TABLE IF NOT EXISTS locations (
    id numeric PRIMARY KEY,
    locations_date DATE,
    id_customers numeric
);

-- Inserção dos dados na tabela

INSERT 
    INTO customers (id, name, street, city) VALUES
        (1, 'Giovanna Goncalves Oliveira', 'Rua Mato Grosso'               , 'Canoas'),
        (2, 'Kauã Azevedo Ribeiro'       , 'Travessa Ibiá'                 , 'Uberlândia'),
        (3, 'Rebeca Barbosa Santos'      , 'Rua Observatório Meteorológico', 'Salvador'),
        (4, 'Sarah Carvalho Correia'     , 'Rua Antônio Carlos da Silva'   , 'Apucarana'),
        (5, 'João Almeida Lima'          , 'Rua Rio Taiuva'                , 'Ponta Grossa'),
        (6, 'Diogo Melo Dias'            , 'Rua Duzentos e Cinqüenta'      , 'Várzea Grande')
    ON CONFLICT (id) DO NOTHING;

INSERT 
    INTO locations (id, locations_date, id_customers) VALUES
        (1, '2016-10-09', 3),
        (2, '2016-09-02', 1),
        (3, '2016-08-02', 4),
        (4, '2016-09-02', 2),
        (5, '2016-03-02', 6),
        (6, '2016-04-04', 4)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2616)

SELECT 
    c.id,
    c.name
FROM 
    customers c
LEFT JOIN 
    locations l ON l.id_customers = c.id
WHERE
    l.id_customers IS NULL
ORDER BY
    c.id;
