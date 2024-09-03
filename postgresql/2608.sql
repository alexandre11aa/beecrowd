<<<<<<< HEAD
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
        (1, 'Two-door wardrobe', 100  , 800),
        (2, 'Dining table'     , 1000 , 560),
        (3, 'Towel holder'     , 10000, 25.50),
        (4, 'Computer desk'    , 350  , 320.50),
        (5, 'Chair'            , 3000 , 210.64),
        (6, 'Single bed'       , 750  , 460)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2608)

SELECT 
    MAX(price),
    MIN(price)
FROM 
=======
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
        (1, 'Two-door wardrobe', 100  , 800),
        (2, 'Dining table'     , 1000 , 560),
        (3, 'Towel holder'     , 10000, 25.50),
        (4, 'Computer desk'    , 350  , 320.50),
        (5, 'Chair'            , 3000 , 210.64),
        (6, 'Single bed'       , 750  , 460)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2608)

SELECT 
    MAX(price),
    MIN(price)
FROM 
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
    products;