-- psql -h localhost -p 5432 -U postgres -d estrela -f 0000.sql

-- psql: Cliente de linha de comando do PostgreSQL para executar comandos e scripts SQL.
-- -h localhost: Especifica o host do servidor PostgreSQL. localhost indica que o servidor está na mesma máquina.
-- -p 5432: Define a porta onde o servidor PostgreSQL está ouvindo. 5432 é a porta padrão.
-- -U postgres: Nome do usuário para se conectar ao banco de dados. postgres é o superusuário padrão do PostgreSQL.
-- -d 0000: Nome do banco de dados ao qual você está se conectando. estrela é o banco de dados onde o script será executado.
-- -f restart.sql: Especifica o arquivo de script SQL que você deseja executar. restart.sql é o arquivo contendo os comandos SQL.

-- psql -h localhost -p 5432 -U alexandre11aa -d estrela -f 2602.sql

-- psql: É o cliente de linha de comando do PostgreSQL para interagir com o banco de dados.
-- -h localhost: Especifica o host onde o servidor PostgreSQL está rodando. localhost indica que o servidor está rodando na mesma máquina onde o comando está sendo executado.
-- -p 5432: Define a porta onde o servidor PostgreSQL está ouvindo. 5432 é a porta padrão do PostgreSQL.
-- -U alexandre11aa: Define o nome de usuário para se conectar ao banco de dados. Neste caso, o usuário é alexandre11aa.
-- -d estrela: Especifica o banco de dados ao qual você deseja se conectar. Neste caso, o banco de dados é estrela.
-- -f delete_tables.sql: Indica o arquivo SQL a ser executado. O psql lerá e executará os comandos no arquivo delete_tables.sql.

-- Desabilitar as checagens de restrições de chave estrangeira temporariamente
SET session_replication_role = replica;

-- Gerar e executar comandos para apagar todas as tabelas
DO $$ 
DECLARE 
    r RECORD;
BEGIN 
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') 
    LOOP 
        EXECUTE 'DROP TABLE IF EXISTS public.' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP; 
END $$;

-- Habilitar novamente as checagens de restrições de chave estrangeira
SET session_replication_role = DEFAULT;
