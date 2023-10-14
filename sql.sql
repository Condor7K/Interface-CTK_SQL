# mercearia frios_laticinios higiene_limpeza doces_achocolatados bebidas cmb

CREATE TABLE estoque (
    id_codigo INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(255) NOT NULL,
    setor VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    data_insercao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO estoque (produto, setor, quantidade, preco) VALUES ('Café Pilão 1kg', 'Mercearia', '250', '35.90');

INSERT INTO estoque (produto, setor, quantidade, preco) VALUES ('Leite Integral Piracanjuba 1L', 'laticinios', '358', '5.36');

INSERT INTO estoque (produto, setor, quantidade, preco) VALUES ('Limpador Perfumado para pisos Casa & Perfume', 'limpeza', '286', '38.96');

INSERT INTO estoque (produto, setor, quantidade, preco) VALUES ('Pasta de dentes colgate 90g', 'higiene', '568', '5.99');

INSERT INTO estoque (produto, setor, quantidade, preco) VALUES ('Vodka balalaika 1l', 'bebidas', '379', '19.99');

INSERT INTO estoque (produto, setor, quantidade, preco) VALUES ('Caderno Universitário Barbie 96fls Capa Love To Me', 'papelaria', '250', '19.90');

INSERT INTO estoque (produto, setor, quantidade, preco) VALUES ('Chocolate Kit Kat ao Leite Nestlé', 'confeitaria', '657', '3.99');

DROP TABLE estoque;
