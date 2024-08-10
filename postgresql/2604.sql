-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS products (
    id numeric PRIMARY KEY,
    name varchar,
    amount numeric,
    price numeric
);

-- Inserção dos dados na tabela

INSERT 
    INTO products (id, name, amount, price) VALUES
        (1, 'Two-door wardrobe', 100  , 80),
        (2,	'Dining table'     , 1000 , 560),
        (3,	'Towel holder'     , 10000, 5.50),
        (4,	'Computer desk'    , 350  , 100),
        (5,	'Chair'            , 3000 , 210.64),
        (6,	'Single bed'       , 750  , 99)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2604)

SELECT 
    id,
    name
FROM 
    products
WHERE 
    (price < 10 OR price > 100);