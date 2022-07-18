-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 18, 2022 at 09:51 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user`
--

-- --------------------------------------------------------

--
-- Table structure for table `users_table`
--

DROP TABLE IF EXISTS `users_table`;
CREATE TABLE IF NOT EXISTS `users_table` (
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users_table`
--

INSERT INTO `users_table` (`username`, `email`, `password`) VALUES
('sexaa', 'gargaradhya505@gmail.com', '123'),
('Arnav jain', 'jainarnav12345@gmail.com', '123'),
('Vaibhav', 'vaibhavtushar19@gmail.com', 'vaibhav19'),
('Vaibhav', 'vaibhavtushar19@gmail.com', 'vaibhav19'),
('Vaibhav', 'vaibhavtushar19@gmail.com', 'vaibhav19'),
('Rythem', 'rythemsharma21@gmail.com', 'Rythem@123'),
('Rythem', 'rythemsharma21@gmail.com', 'Rythem@123'),
('Rythem', 'rythemsharma21@gmail.com', 'Rythem@123'),
('Rythem', 'rythemsharma21@gmail.com', 'Rythem@123'),
('Rythem', 'rythemsharma21@gmail.com', 'rythem@123'),
('Rythem', 'rythemsharma21@gmail.com', 'Rythem@123'),
('Shubhank', 'shubhank.singhal98@gmail.com', '12345678'),
('Shrey', 'shreychoudhary034@gmail.com', '1234');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
