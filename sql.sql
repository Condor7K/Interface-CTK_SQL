-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS comercio;

-- Seleciona o banco de dados
USE comercio;

-- Tabela de Usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único para cada usuário
    usuario VARCHAR(255) NOT NULL,      -- Nome de usuário
    senha VARCHAR(255) NOT NULL,        -- Senha do usuário
    tipo_user ENUM('admin', 'user') NOT NULL,  -- Tipo de usuário, podendo ser 'admin' ou 'user'
    CONSTRAINT uc_usuario UNIQUE (usuario)  -- Garantir que o nome de usuário seja único
);

-- Tabela de Estoque
CREATE TABLE IF NOT EXISTS estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único para cada item de estoque
    produto VARCHAR(255) NOT NULL,      -- Nome do produto
    setor ENUM('Mercearia', 'Laticinios', 'Limpeza', 'Higiene', 'Bebidas', 'Papelaria', 'Confeitaria') NOT NULL,  -- Setor do produto
    quantidade INT NOT NULL,            -- Quantidade em estoque
    preco DECIMAL(10, 2) NOT NULL,      -- Preço de venda do produto
    data_entrada DATE NOT NULL          -- Data de entrada no estoque
);

-- Tabela de Logs (caso seja necessário armazenar registros de atividades do sistema)
CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único para cada log
    usuario_id INT NOT NULL,            -- ID do usuário que realizou a ação
    acao VARCHAR(255) NOT NULL,         -- Descrição da ação realizada
    data_acao DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Data e hora da ação
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)  -- Relacionamento com a tabela de usuários
);

-- Tabela de Vendas (caso seja necessário registrar as vendas realizadas)
CREATE TABLE IF NOT EXISTS vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único para cada venda
    usuario_id INT NOT NULL,            -- ID do usuário que realizou a venda
    total DECIMAL(10, 2) NOT NULL,      -- Valor total da venda
    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Data e hora da venda
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)  -- Relacionamento com a tabela de usuários
);

SELECT * FROM usuarios;

SELECT * FROM estoque;

