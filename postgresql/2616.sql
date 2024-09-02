-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS customers (
    id numeric PRIMARY KEY,
    name varchar,
    street varchar,
    city varchar
);

CREATE TABLE IF NOT EXISTS rentals (
    id numeric PRIMARY KEY,
    rentals_date DATE,
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
    INTO rentals (id, rentals_date, id_customers) VALUES
        (1, '2016-09-10', 3),
        (2, '2016-02-09', 1),
        (3, '2016-02-08', 4),
        (4, '2016-02-09', 2),
        (5, '2016-02-03', 6),
        (6, '2016-04-04', 4)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2616)

SELECT 
    c.name,
    r.rentals_date
FROM 
    customers c
JOIN 
    rentals r ON r.id_customers = c.id
WHERE
    EXTRACT(YEAR FROM r.rentals_date) = 2016 AND 
    EXTRACT(MONTH FROM r.rentals_date) = 9;
