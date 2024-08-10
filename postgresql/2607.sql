-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS providers (
    id numeric PRIMARY KEY,
    name varchar,
    street varchar,
    city varchar,
    state char(2)
);

-- Inserção dos dados na tabela

INSERT 
    INTO providers (id, name, street, city, state) VALUES
        (1, 'Henrique'        , 'Av Brasil'     , 'Rio de Janeiro', 'RJ'),
        (2, 'Marcelo Augusto' , 'Rua Imigrantes', 'Belo Horizonte', 'MG'),
        (3, 'Caroline Silva'  , 'Av São Paulo'  , 'Salvador'      , 'BA'),
        (4, 'Guilerme Staff'  , 'Rua Central'   , 'Porto Alegre'  , 'RS'),
        (5, 'Isabela Moraes'  , 'Av Juiz Grande', 'Curitiba'      , 'PR'),
        (6, 'Francisco Accerr', 'Av Paulista'   , 'São Paulo'     , 'SP')
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2607)

SELECT 
    city
FROM 
    providers
ORDER BY 
    city ASC;