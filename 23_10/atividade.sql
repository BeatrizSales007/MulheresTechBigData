CREATE DATABASE aula02;

CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    duracao INT NOT NULL, -- duração em meses
    nivel VARCHAR(50), -- nível do curso
    preco DECIMAL(10, 2) NOT NULL, -- preço do curso
    certificacao BOOLEAN -- se oferece certificação
);

CREATE TABLE filiais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado CHAR(2) NOT NULL,
    capacidade INT NOT NULL, -- capacidade de alunos
    telefone VARCHAR(15) -- contato da filial
);

INSERT INTO cursos (nome, duracao, nivel, preco, certificacao) VALUES
('Introdução ao Marketing', 6, 'Básico', 500.00, TRUE),
('Desenvolvimento Web', 12, 'Intermediário', 1200.00, TRUE),
('Design Gráfico', 8, 'Avançado', 1500.00, TRUE),
('Banco de Dados', 10, 'Intermediário', 1000.00, TRUE),
('Análise de Dados', 6, 'Avançado', 2000.00, TRUE),
('Segurança da Informação', 8, 'Avançado', 1800.00, TRUE),
('Inglês para Negócios', 4, 'Básico', 600.00, FALSE),
('Administração', 10, 'Intermediário', 800.00, TRUE),
('Marketing Digital', 6, 'Básico', 700.00, TRUE),
('Programação Python', 12, 'Intermediário', 1200.00, TRUE);

INSERT INTO filiais (nome, cidade, estado, capacidade, telefone) VALUES
('Filial Rio de Janeiro', 'Rio de Janeiro', 'RJ', 200, '21-2222-3333'),
('Filial São Paulo', 'São Paulo', 'SP', 300, '11-3333-4444'),
('Filial Belo Horizonte', 'Belo Horizonte', 'MG', 150, '31-4444-5555'),
('Filial Porto Alegre', 'Porto Alegre', 'RS', 180, '51-5555-6666'),
('Filial Salvador', 'Salvador', 'BA', 250, '71-6666-7777'),
('Filial Recife', 'Recife', 'PE', 120, '81-7777-8888'),
('Filial Curitiba', 'Curitiba', 'PR', 170, '41-8888-9999'),
('Filial Manaus', 'Manaus', 'AM', 100, '92-9999-1111'),
('Filial Brasília', 'Brasília', 'DF', 200, '61-1111-2222'),
('Filial Fortaleza', 'Fortaleza', 'CE', 130, '85-2222-3333');

SELECT * FROM cursos WHERE certificacao = TRUE AND nivel = 'Avançado';

SELECT * FROM filiais WHERE capacidade > 150;