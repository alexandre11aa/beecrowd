<<<<<<< HEAD
-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS categories (
    id numeric PRIMARY KEY,
    name varchar
);

CREATE TABLE IF NOT EXISTS products (
    id numeric PRIMARY KEY,
    name varchar,
    amount numeric,
    price numeric,
    id_categories numeric REFERENCES categories(id)
);

-- Inserção dos dados na tabela

INSERT 
    INTO categories (id, name) VALUES
        (1, 'old stock'),
        (2, 'new stock'),
        (3, 'modern'),
        (4, 'commercial'),
        (5, 'recyclable'),
        (6, 'executive'),
        (7, 'superior'),
        (8, 'wood'),
        (9, 'super luxury'),
        (10, 'vintage')
    ON CONFLICT (id) DO NOTHING;

INSERT 
    INTO products (id, name, amount, price, id_categories) VALUES
        (1, 'Lampshade'         , 100  , 800   , 4),
        (2, 'Table for painting', 1000 , 560   , 9),
        (3, 'Notebook desk'     , 10000, 25.50 , 9),
        (4, 'Computer desk'     , 350  , 320.50, 6),
        (5, 'Chair'             , 3000 , 210.64, 9),
        (6, 'Home alarm'        , 750  , 460   , 4)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2606)

SELECT 
    p.id,
    p.name
FROM 
    products p
JOIN
    categories c ON p.id_categories = c.id
WHERE 
=======
-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS categories (
    id numeric PRIMARY KEY,
    name varchar
);

CREATE TABLE IF NOT EXISTS products (
    id numeric PRIMARY KEY,
    name varchar,
    amount numeric,
    price numeric,
    id_categories numeric REFERENCES categories(id)
);

-- Inserção dos dados na tabela

INSERT 
    INTO categories (id, name) VALUES
        (1, 'old stock'),
        (2, 'new stock'),
        (3, 'modern'),
        (4, 'commercial'),
        (5, 'recyclable'),
        (6, 'executive'),
        (7, 'superior'),
        (8, 'wood'),
        (9, 'super luxury'),
        (10, 'vintage')
    ON CONFLICT (id) DO NOTHING;

INSERT 
    INTO products (id, name, amount, price, id_categories) VALUES
        (1, 'Lampshade'         , 100  , 800   , 4),
        (2, 'Table for painting', 1000 , 560   , 9),
        (3, 'Notebook desk'     , 10000, 25.50 , 9),
        (4, 'Computer desk'     , 350  , 320.50, 6),
        (5, 'Chair'             , 3000 , 210.64, 9),
        (6, 'Home alarm'        , 750  , 460   , 4)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2606)

SELECT 
    p.id,
    p.name
FROM 
    products p
JOIN
    categories c ON p.id_categories = c.id
WHERE 
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
    c.name LIKE 'super%';