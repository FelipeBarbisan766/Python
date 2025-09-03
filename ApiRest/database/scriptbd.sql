
CREATE DATABASE agendai ;

USE agendai;

--CREATE TABLE (
--    atri tipo tam null def auto_increment,
--    CONSTRAINT pk_TABELA_CAMPO PRIMARY KEY (id),
--    CONSTRAINT fk_TABELA_TABELA_FK_ID FOREING KEY (id) REFERENCES [nome_tabela_fk] (id_tabela_fk)
--);

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    login VARCHAR(60) NOT NULL UNIQUE,
    password VARCHAR(250) NOT NULL,
    active BIT DEFAULT(1),
    CONSTRAINT pk_users_id PRIMARY KEY (id)
);

CREATE TABLE contacts (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL,
    apelido VARCHAR(30) NOT NULL,
    email VARCHAR(250) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    active BIT DEFAULT(1),
    CONSTRAINT pk_contacts_id PRIMARY KEY (id)
);

