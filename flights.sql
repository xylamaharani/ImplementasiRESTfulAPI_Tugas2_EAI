-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3308
-- Generation Time: Apr 04, 2024 at 05:42 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vacay`
--

-- --------------------------------------------------------

--
-- Table structure for table `flights`
--

CREATE TABLE `flights` (
  `flight_id` int(11) NOT NULL,
  `flight_code` varchar(50) NOT NULL,
  `maskapai` varchar(50) NOT NULL,
  `departure` varchar(50) NOT NULL,
  `destinasi` varchar(50) NOT NULL,
  `keberangkatan` datetime NOT NULL,
  `transit` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flights`
--

INSERT INTO `flights` (`flight_id`, `flight_code`, `maskapai`, `departure`, `destinasi`, `keberangkatan`, `transit`) VALUES
(2, 'GI2', 'Garuda Indonesia', 'Surabaya', 'Bandung', '2024-04-20 19:45:00', 0),
(3, 'SA3', 'Singapore Airlines', 'Singapore', 'Sydney', '2024-04-11 10:30:00', 1),
(4, 'E4', 'Emirates', 'Dubai', 'London', '2024-04-12 14:45:00', 0),
(5, 'BA5', 'British Airways', 'London', 'New York', '2024-04-13 17:15:00', 1),
(6, 'QA6', 'Qatar Airways', 'Doha', 'Paris', '2024-04-14 19:30:00', 0),
(7, 'AF7', 'Air France', 'Paris', 'Tokyo', '2024-04-15 22:00:00', 1),
(8, 'DA8', 'Delta Air Lines', 'New York', 'Los Angeles', '2024-04-16 11:00:00', 0),
(9, 'AN9', 'ANA', 'Tokyo', 'Beijing', '2024-04-17 08:30:00', 1),
(10, 'CP10', 'Cathay Pacific', 'Hong Kong', 'Sydney', '2024-04-18 20:45:00', 0),
(11, 'KL11', 'KLM', 'Amsterdam', 'Toronto', '2024-04-19 16:20:00', 1),
(15, 'AA12', 'Lion Air', 'Bandung', 'Bali', '2024-04-18 18:00:00', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `flights`
--
ALTER TABLE `flights`
  ADD PRIMARY KEY (`flight_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `flights`
--
ALTER TABLE `flights`
  MODIFY `flight_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
