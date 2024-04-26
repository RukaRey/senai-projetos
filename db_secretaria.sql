-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 2024-04-26 03:44:04
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `db_secretaria`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `alunos`
--

CREATE TABLE `alunos` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `cpf` int(11) NOT NULL,
  `telefone` varchar(30) NOT NULL,
  `email` varchar(255) NOT NULL,
  `mod_matricula` varchar(255) NOT NULL,
  `matricula` varchar(255) NOT NULL,
  `ativo` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `alunos`
--

INSERT INTO `alunos` (`id`, `nome`, `cpf`, `telefone`, `email`, `mod_matricula`, `matricula`, `ativo`) VALUES
(1, 'NAIAN JONAS ARIANO ALEMÃO', 222222222, '2222-3333', 'banaina@gmail.com', '', '', 0),
(2, 'NATAN RODRIGUES NASCIMENTO ROMÃO', 1231123444, '1111-0000', 'pegador3000@gmail.com', '', '', 0),
(14, 'a', 1, '111', 'd@gmail.com', '', '', 0),
(23, 'D', 12, '1112', '22@gmail.com', '', '', 1),
(26, '1', 5, '4', '32@gmail.com', '', '', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedidos_docs`
--

CREATE TABLE `pedidos_docs` (
  `id_docs` int(11) NOT NULL,
  `id_aluno` int(11) NOT NULL,
  `tipo_doc` varchar(255) NOT NULL,
  `preco_emissao` float NOT NULL,
  `status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tipos_doc`
--

CREATE TABLE `tipos_doc` (
  `id_tipos_docs` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `preco` float NOT NULL,
  `gratuito` int(1) NOT NULL,
  `limite_por_disciplina` float NOT NULL,
  `limite_maximo` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tipos_doc`
--

INSERT INTO `tipos_doc` (`id_tipos_docs`, `nome`, `preco`, `gratuito`, `limite_por_disciplina`, `limite_maximo`) VALUES
(1, 'Declaração de Transferência', 15, 0, 0, 0),
(2, 'Histórico Parcial', 15, 0, 0, 0),
(3, 'Carta de apresentação para estágio optativo', 0, 1, 0, 0),
(4, 'Declaração de matrícula', 0, 1, 0, 0),
(5, '2ª via de carteirinha estudantil', 10, 0, 0, 0),
(6, 'Ementa Escolar', 0, 0, 20, 100),
(7, '2ª via de Certificado', 25, 0, 0, 0),
(8, '2ª via de Diploma', 35, 0, 0, 0),
(9, '2ª via de Diploma Curso Superior', 120, 0, 0, 0),
(10, '2ª via Historico Escolar', 20, 0, 0, 0),
(11, 'Declaração de Conclusão', 15, 0, 0, 0),
(12, 'Declaração para Fins de Aposentadoria', 20, 0, 0, 0),
(13, 'Histórico Parcial', 15, 0, 0, 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `pedidos_docs`
--
ALTER TABLE `pedidos_docs`
  ADD PRIMARY KEY (`id_docs`);

--
-- Índices de tabela `tipos_doc`
--
ALTER TABLE `tipos_doc`
  ADD PRIMARY KEY (`id_tipos_docs`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `alunos`
--
ALTER TABLE `alunos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de tabela `pedidos_docs`
--
ALTER TABLE `pedidos_docs`
  MODIFY `id_docs` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tipos_doc`
--
ALTER TABLE `tipos_doc`
  MODIFY `id_tipos_docs` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
