-- Criação da tabela caso ela não exista

CREATE TABLE IF NOT EXISTS movies (
    id numeric PRIMARY KEY,
    name varchar,
    id_genres numeric
);

CREATE TABLE IF NOT EXISTS genres (
    id numeric PRIMARY KEY,
    description varchar
);

-- Inserção dos dados na tabela

INSERT 
    INTO movies (id, name, id_genres) VALUES
        (1, 'Batman'                      , 3),
        (2, 'The Battle of the Dark River', 3),
        (3, 'White Duck'                  , 1),
        (4, 'Breaking Barriers'           , 4),
        (5, 'The Two Hours'               , 2)
    ON CONFLICT (id) DO NOTHING;

INSERT 
    INTO genres (id, description) VALUES
        (1, 'Animation'),
        (2, 'Horror'),
        (3, 'Action'),
        (4, 'Drama'),
        (5, 'Comedy')
    ON CONFLICT (id) DO NOTHING;

-- Consulta (BEE 2611)

SELECT 
    m.id,
    m.name
FROM 
    genres g
JOIN 
    movies m ON m.id_genres = g.id
WHERE
    g.description = 'Action';