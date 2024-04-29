-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 29-Abr-2024 às 22:09
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.2.12

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
-- Estrutura da tabela `avaliacao`
--

CREATE TABLE `avaliacao` (
  `id` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `data_hora` varchar(50) NOT NULL,
  `pergunta_1` int(1) NOT NULL,
  `pergunta_2` int(1) NOT NULL,
  `pergunta_3` int(1) NOT NULL,
  `pergunta_4` int(1) NOT NULL,
  `observacao` varchar(560) NOT NULL,
  `resposta` varchar(560) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `avaliacao`
--

INSERT INTO `avaliacao` (`id`, `id_cliente`, `data_hora`, `pergunta_1`, `pergunta_2`, `pergunta_3`, `pergunta_4`, `observacao`, `resposta`) VALUES
(1, 0, '', 1, 0, 0, 2, 'har har har har', ''),
(4, 2, '', 1, 0, 3, 2, 'Te pego na rua fpd', ''),
(5, 3, '', 0, 1, 3, 2, 'Iago fpd e a bik heinn', ''),
(6, 4, '', 1, 1, 3, 2, 'Iago minhas costa fpd', ''),
(7, 5, '', 0, 1, 3, 2, 'Iago fpd e a bik heinn', ''),
(8, 6, '2024-04-29 22:08:37', 0, 0, 0, 0, 'Adorei', '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `cliente`
--

CREATE TABLE `cliente` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telefone` varchar(255) NOT NULL,
  `cpf` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `cliente`
--

INSERT INTO `cliente` (`id`, `nome`, `email`, `telefone`, `cpf`) VALUES
(1, 'PEdro', 'padeiro@hotmail.com', '0', '0'),
(5, 'Iago', 'qqqqqq@gmail.com', '(44) 44444-4444', '330.059.999-54'),
(6, 'Kelvin', '43@mail', '(33) 33333-3333', '231.231.431-21');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `avaliacao`
--
ALTER TABLE `avaliacao`
  ADD PRIMARY KEY (`id`,`id_cliente`);

--
-- Índices para tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `avaliacao`
--
ALTER TABLE `avaliacao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
