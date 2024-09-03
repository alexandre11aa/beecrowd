<<<<<<< HEAD
-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS categories (
    id numeric PRIMARY KEY,
    name varchar
);

CREATE TABLE IF NOT EXISTS providers (
    id numeric PRIMARY KEY,
    name varchar,
    street varchar,
    city varchar,
    state char(2)
);

CREATE TABLE IF NOT EXISTS products (
    id numeric PRIMARY KEY,
    name varchar,
    amount numeric,
    price numeric,
    id_providers numeric REFERENCES providers(id),
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
    INTO providers (id, name, street, city, state) VALUES
        (1, 'Henrique'        , 'Av Brasil'     , 'Rio de Janeiro', 'RJ'),
        (2, 'Marcelo Augusto' , 'Rua Imigrantes', 'Belo Horizonte', 'MG'),
        (3, 'Caroline Silva'  , 'Av São Paulo'  , 'Salvador'      , 'BA'),
        (4, 'Guilerme Staff'  , 'Rua Central'   , 'Porto Alegre'  , 'RS'),
        (5, 'Isabela Moraes'  , 'Av Juiz Grande', 'Curitiba'      , 'PR'),
        (6, 'Francisco Accerr', 'Av Paulista'   , 'São Paulo'     , 'SP')
    ON CONFLICT (id) DO NOTHING;

INSERT 
    INTO products (id, name, amount, price, id_providers, id_categories) VALUES
        (1, 'Two-door wardrobe', 100  , 800   , 6, 8),
        (2, 'Dining table'     , 1000 , 560   , 1, 9),
        (3, 'Towel holder'     , 10000, 25.50 , 5, 1),
        (4, 'Computer desk'    , 350  , 320.50, 4, 6),
        (5, 'Chair'            , 3000 , 210.64, 3, 6),
        (6, 'Single bed'       , 750  , 460   , 1, 2)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2605)

SELECT 
    p.name,
    pr.name
FROM 
    products p
JOIN
    providers pr ON p.id_providers = pr.id
JOIN
    categories c ON p.id_categories = c.id
WHERE 
=======
-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS categories (
    id numeric PRIMARY KEY,
    name varchar
);

CREATE TABLE IF NOT EXISTS providers (
    id numeric PRIMARY KEY,
    name varchar,
    street varchar,
    city varchar,
    state char(2)
);

CREATE TABLE IF NOT EXISTS products (
    id numeric PRIMARY KEY,
    name varchar,
    amount numeric,
    price numeric,
    id_providers numeric REFERENCES providers(id),
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
    INTO providers (id, name, street, city, state) VALUES
        (1, 'Henrique'        , 'Av Brasil'     , 'Rio de Janeiro', 'RJ'),
        (2, 'Marcelo Augusto' , 'Rua Imigrantes', 'Belo Horizonte', 'MG'),
        (3, 'Caroline Silva'  , 'Av São Paulo'  , 'Salvador'      , 'BA'),
        (4, 'Guilerme Staff'  , 'Rua Central'   , 'Porto Alegre'  , 'RS'),
        (5, 'Isabela Moraes'  , 'Av Juiz Grande', 'Curitiba'      , 'PR'),
        (6, 'Francisco Accerr', 'Av Paulista'   , 'São Paulo'     , 'SP')
    ON CONFLICT (id) DO NOTHING;

INSERT 
    INTO products (id, name, amount, price, id_providers, id_categories) VALUES
        (1, 'Two-door wardrobe', 100  , 800   , 6, 8),
        (2, 'Dining table'     , 1000 , 560   , 1, 9),
        (3, 'Towel holder'     , 10000, 25.50 , 5, 1),
        (4, 'Computer desk'    , 350  , 320.50, 4, 6),
        (5, 'Chair'            , 3000 , 210.64, 3, 6),
        (6, 'Single bed'       , 750  , 460   , 1, 2)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2605)

SELECT 
    p.name,
    pr.name
FROM 
    products p
JOIN
    providers pr ON p.id_providers = pr.id
JOIN
    categories c ON p.id_categories = c.id
WHERE 
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
    c.id = 6;