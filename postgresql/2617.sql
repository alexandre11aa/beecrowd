-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS providers (
    id numeric PRIMARY KEY,
    name VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    state varchar
);

CREATE TABLE IF NOT EXISTS products (
    id numeric PRIMARY KEY,
    name VARCHAR(255),
    amount numeric,
    price numeric,
    id_providers numeric
);

-- Inserção dos dados na tabela

INSERT 
    INTO providers (id, name, street, city, state) VALUES
        (1, 'Ajax SA'     , 'Presidente Castelo Branco', 'Porto Alegre'  , 'RS'),
        (2, 'Sansul SA'   , 'Av Brasil'                , 'Rio de Janeiro', 'RJ'),
        (3, 'South Chairs', 'Av Moinho'                , 'Santa Maria'   , 'RS'),
        (4, 'Elon Electro', 'Apolo'                    , 'São Paulo'     , 'SP'),
        (5, 'Mike Electro', 'Pedro da Cunha'           , 'Curitiba'      , 'PR')
    ON CONFLICT (id) DO NOTHING;

INSERT 
    INTO products (id, name, amount, price, id_providers) VALUES
        (1, 'Blue Chair'     , 30 , 300.00 , 5),
        (2, 'Red Chair'      , 50 , 2150.00, 1),
        (3, 'Disney Wardrobe', 400, 829.50 , 4),
        (4, 'Blue Toaster'   , 20 , 9.90   , 3),
        (5, 'Solar Panel'    , 30 , 3000.25, 4)
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2617)

SELECT 
    pt.name,
    pr.name
FROM 
    providers pr
JOIN 
    products pt ON pt.id_providers = pr.id
WHERE
    pr.name =  'Ajax SA';