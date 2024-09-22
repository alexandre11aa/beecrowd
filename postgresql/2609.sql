-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS products (
    id numeric PRIMARY KEY,
    name varchar,
    amount numeric,
    price numeric,
    id_categories numeric
);

CREATE TABLE IF NOT EXISTS categories (
    id numeric PRIMARY KEY,
    name varchar
);

-- Inserção dos dados na tabela

INSERT 
    INTO products (id, name, amount, price, id_categories) VALUES
        (1, 'Two-door wardrobe', 100  , 800   , 1),
        (2, 'Dining table'     , 1000 , 560   , 3),
        (3, 'Towel holder'     , 10000, 25.50 , 4),
        (4, 'Computer desk'    , 350  , 320.50, 2),
        (5, 'Chair'            , 3000 , 210.64, 4),
        (6, 'Single bed'       , 750  , 460   , 1)
    ON CONFLICT (id) DO NOTHING;

INSERT 
    INTO categories (id, name) VALUES
        (1, 'wood'),
        (2, 'luxury'),
        (3, 'vintage'),
        (4, 'modern'),
        (5, 'super luxury')
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2609)

SELECT 
    c.name,
    SUM(p.amount)
FROM 
    categories c
JOIN
    products p ON p.id_categories = c.id
GROUP BY
    c.name;