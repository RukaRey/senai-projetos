-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 2024-04-30 14:03:54
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
-- Banco de dados: `sistema_avaliacao`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `adm`
--

CREATE TABLE `adm` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `cpf` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `adm`
--

INSERT INTO `adm` (`id`, `nome`, `senha`, `cpf`) VALUES
(1, 'Jão', '1234', '123.123.123-00');

-- --------------------------------------------------------

--
-- Estrutura para tabela `avaliacao`
--

CREATE TABLE `avaliacao` (
  `id` int(11) NOT NULL,
  `id_cliente` int(10) NOT NULL,
  `id_cliente_falso` int(11) NOT NULL,
  `data_hora` varchar(50) NOT NULL,
  `pergunta_1` int(1) NOT NULL,
  `pergunta_2` int(1) NOT NULL,
  `pergunta_3` int(1) NOT NULL,
  `pergunta_4` int(1) NOT NULL,
  `observacao` varchar(560) NOT NULL,
  `resposta` varchar(560) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `avaliacao`
--

INSERT INTO `avaliacao` (`id`, `id_cliente`, `id_cliente_falso`, `data_hora`, `pergunta_1`, `pergunta_2`, `pergunta_3`, `pergunta_4`, `observacao`, `resposta`) VALUES
(13, 11, 0, '2024-04-30 00:50:37', 0, 1, 1, 2, 'wwwwwwwww', 'Hm.'),
(15, 6, 0, '2024-04-30 00:54:42', 0, 0, 0, 0, '', ''),
(16, 11, 0, '2024-04-30 00:55:22', 0, 0, 0, 0, '', '<strong>Resposta enviada em 2024-04-30 08:56:06   </strong><br>Me faz um pix de 20 reais Raquel'),
(17, 12, 0, '2024-04-29 20:59:31', 1, 0, 0, 0, 'Maicon Kuster', '<strong>Resposta enviada em 2024-04-30 09:00:53   </strong><br>Só 20 reaizinhos Raquel');

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telefone` varchar(255) NOT NULL,
  `cpf` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`id`, `nome`, `email`, `telefone`, `cpf`) VALUES
(1, 'PEdro', 'padeiro@hotmail.com', '0', '0'),
(5, 'Iago', 'qqqqqq@gmail.com', '(44) 44444-4444', '330.059.999-54'),
(6, 'Kelvin', '43@mail', '(33) 33333-3333', '231.231.431-21'),
(7, 'Jonas Completo', 'luciano17701@gmail.com', '(32) 98503-9064', '111.222.333-44'),
(11, 'Maria A', 'a@gmail.com', '(00) 00000-0000', '333.333.333-33'),
(12, 'Mãe', 'snassmash@gmail.com', '(88) 88888-8888', '888.888.888-88');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `adm`
--
ALTER TABLE `adm`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `avaliacao`
--
ALTER TABLE `avaliacao`
  ADD PRIMARY KEY (`id`,`id_cliente_falso`);

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `adm`
--
ALTER TABLE `adm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `avaliacao`
--
ALTER TABLE `avaliacao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
