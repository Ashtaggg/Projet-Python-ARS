-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 16 nov. 2023 à 13:19
-- Version du serveur : 8.0.27
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `projet_python_ars`
--

-- --------------------------------------------------------

--
-- Structure de la table `airport`
--

DROP TABLE IF EXISTS `airport`;
CREATE TABLE IF NOT EXISTS `airport` (
  `AirportID` int NOT NULL AUTO_INCREMENT,
  `AirportName` varchar(255) NOT NULL,
  `Location` varchar(255) NOT NULL,
  PRIMARY KEY (`AirportID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `booking`
--

DROP TABLE IF EXISTS `booking`;
CREATE TABLE IF NOT EXISTS `booking` (
  `BookingID` int NOT NULL AUTO_INCREMENT,
  `CustomerID` int DEFAULT NULL,
  `FlightID` int DEFAULT NULL,
  `NumberOfTickets` int NOT NULL,
  `TotalAmount` decimal(10,2) NOT NULL,
  `Timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`BookingID`),
  KEY `CustomerID` (`CustomerID`),
  KEY `FlightID` (`FlightID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `booking`
--

INSERT INTO `booking` (`BookingID`, `CustomerID`, `FlightID`, `NumberOfTickets`, `TotalAmount`, `Timestamp`) VALUES
(1, 3, 64, 1, '110.00', '2023-11-09 13:21:45'),
(3, 3, 65, 2, '90.00', '2023-11-09 13:55:31');

-- --------------------------------------------------------

--
-- Structure de la table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `CustomerID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(255) NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `BirthDate` date NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Type` int NOT NULL COMMENT '0 -> Member\r\n1 -> Admin',
  `PhotoProfil` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci COMMENT 'chemin vers la photo de profil',
  PRIMARY KEY (`CustomerID`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `customer`
--

INSERT INTO `customer` (`CustomerID`, `FirstName`, `LastName`, `Email`, `BirthDate`, `Password`, `Type`, `PhotoProfil`) VALUES
(3, 'Alexis', 'RAYNAL', 'alexis.raynal@edu.ece.fr', '2003-10-01', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 1, '0'),
(4, 'Quentin', 'RICHARD', 'quentin.richard@edu.ece.fr', '0000-00-00', 'cbfad02f9ed2a8d1e08d8f74f5303e9eb93637d47f82ab6f1c15871cf8dd0481', 1, '0'),
(5, 'Anthony', 'SABBAGH', 'anthony.sabbagh@edu.ece.fr', '0000-00-00', '53ed5a8fd89da4f9e6a3c18138c9f6af39d4ea33c8f4650f0f9d849d0651ce64', 1, '0');

-- --------------------------------------------------------

--
-- Structure de la table `discount`
--

DROP TABLE IF EXISTS `discount`;
CREATE TABLE IF NOT EXISTS `discount` (
  `DiscountID` int NOT NULL AUTO_INCREMENT,
  `DiscountType` varchar(255) NOT NULL,
  `Amount` decimal(10,2) NOT NULL,
  PRIMARY KEY (`DiscountID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `EmployeeID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(255) NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `flight`
--

DROP TABLE IF EXISTS `flight`;
CREATE TABLE IF NOT EXISTS `flight` (
  `FlightID` int NOT NULL AUTO_INCREMENT,
  `DepartureCity` varchar(255) NOT NULL,
  `ArrivalCity` varchar(255) NOT NULL,
  `DepartureTime` datetime NOT NULL,
  `ArrivalTime` datetime NOT NULL,
  `TicketPrice` decimal(10,2) NOT NULL,
  `SeatsAvailable` int NOT NULL,
  PRIMARY KEY (`FlightID`)
) ENGINE=MyISAM AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `flight`
--

INSERT INTO `flight` (`FlightID`, `DepartureCity`, `ArrivalCity`, `DepartureTime`, `ArrivalTime`, `TicketPrice`, `SeatsAvailable`) VALUES
(1, 'Paris', 'Berlin', '2023-11-05 08:00:00', '2023-11-05 10:30:00', '150.00', 120),
(2, 'Madrid', 'Lisbon', '2023-11-06 10:30:00', '2023-11-06 12:00:00', '120.00', 100),
(3, 'Rome', 'Amsterdam', '2023-11-07 09:15:00', '2023-11-07 11:45:00', '180.00', 90),
(4, 'London', 'Barcelona', '2023-11-08 11:45:00', '2023-11-08 14:15:00', '200.00', 80),
(5, 'Berlin', 'Paris', '2023-11-09 07:30:00', '2023-11-09 09:00:00', '140.00', 110),
(6, 'Lisbon', 'Madrid', '2023-11-10 13:00:00', '2023-11-10 15:30:00', '130.00', 95),
(7, 'Amsterdam', 'Rome', '2023-11-11 12:45:00', '2023-11-11 15:15:00', '170.00', 75),
(8, 'Barcelona', 'London', '2023-11-12 14:20:00', '2023-11-12 16:50:00', '190.00', 85),
(9, 'Paris', 'Amsterdam', '2023-11-13 16:30:00', '2023-11-13 18:45:00', '160.00', 70),
(10, 'Rome', 'Paris', '2023-11-14 15:10:00', '2023-11-14 17:30:00', '170.00', 60),
(11, 'Paris', 'Berlin', '2023-11-15 08:00:00', '2023-11-15 10:30:00', '150.00', 120),
(12, 'Madrid', 'Lisbon', '2023-11-16 10:30:00', '2023-11-16 12:00:00', '120.00', 100),
(13, 'Rome', 'Amsterdam', '2023-11-17 09:15:00', '2023-11-17 11:45:00', '180.00', 90),
(14, 'London', 'Barcelona', '2023-11-18 11:45:00', '2023-11-18 14:15:00', '200.00', 80),
(15, 'Berlin', 'Paris', '2023-11-19 07:30:00', '2023-11-19 09:00:00', '140.00', 110),
(16, 'Lisbon', 'Madrid', '2023-11-20 13:00:00', '2023-11-20 15:30:00', '130.00', 95),
(17, 'Amsterdam', 'Rome', '2023-11-21 12:45:00', '2023-11-21 15:15:00', '170.00', 75),
(18, 'Barcelona', 'London', '2023-11-22 14:20:00', '2023-11-22 16:50:00', '190.00', 85),
(19, 'Paris', 'Amsterdam', '2023-11-23 16:30:00', '2023-11-23 18:45:00', '160.00', 70),
(20, 'Rome', 'Paris', '2023-11-24 15:10:00', '2023-11-24 17:30:00', '170.00', 60),
(21, 'Berlin', 'Madrid', '2023-11-25 08:30:00', '2023-11-25 10:45:00', '140.00', 100),
(22, 'Amsterdam', 'Lisbon', '2023-11-26 11:15:00', '2023-11-26 13:45:00', '130.00', 90),
(23, 'Paris', 'London', '2023-11-27 12:30:00', '2023-11-27 14:45:00', '160.00', 80),
(24, 'Barcelona', 'Rome', '2023-11-28 09:45:00', '2023-11-28 11:15:00', '180.00', 110),
(25, 'Madrid', 'Berlin', '2023-11-29 14:00:00', '2023-11-29 16:30:00', '150.00', 75),
(26, 'Lisbon', 'Amsterdam', '2023-11-30 15:20:00', '2023-11-30 17:40:00', '170.00', 65),
(27, 'Rome', 'London', '2023-12-01 16:45:00', '2023-12-01 18:00:00', '140.00', 85),
(28, 'London', 'Paris', '2023-12-02 10:00:00', '2023-12-02 12:15:00', '130.00', 95),
(29, 'Amsterdam', 'Barcelona', '2023-12-03 11:45:00', '2023-12-03 13:30:00', '160.00', 75),
(30, 'Berlin', 'Rome', '2023-12-04 09:30:00', '2023-12-04 11:00:00', '180.00', 100),
(31, 'Paris', 'Madrid', '2023-12-05 12:15:00', '2023-12-05 14:45:00', '150.00', 80),
(32, 'Madrid', 'Barcelona', '2023-12-06 14:30:00', '2023-12-06 16:45:00', '160.00', 70),
(33, 'Rome', 'Lisbon', '2023-12-07 15:00:00', '2023-12-07 17:30:00', '140.00', 110),
(34, 'London', 'Amsterdam', '2023-12-08 16:20:00', '2023-12-08 18:40:00', '170.00', 90),
(35, 'Berlin', 'Paris', '2023-12-09 17:45:00', '2023-12-09 19:15:00', '130.00', 75),
(36, 'Amsterdam', 'Madrid', '2023-12-10 11:30:00', '2023-12-10 13:45:00', '150.00', 65),
(37, 'Barcelona', 'Rome', '2023-12-11 10:00:00', '2023-12-11 12:30:00', '160.00', 85),
(38, 'Lisbon', 'London', '2023-12-12 12:45:00', '2023-12-12 15:00:00', '180.00', 70),
(39, 'Paris', 'Berlin', '2023-12-13 08:30:00', '2023-12-13 10:45:00', '140.00', 100),
(40, 'Madrid', 'Lisbon', '2023-12-14 11:15:00', '2023-12-14 13:45:00', '130.00', 90),
(41, 'Rome', 'Amsterdam', '2023-12-15 12:30:00', '2023-12-15 14:45:00', '160.00', 80),
(42, 'London', 'Barcelona', '2023-12-16 09:45:00', '2023-12-16 11:15:00', '180.00', 110),
(43, 'Berlin', 'Paris', '2023-12-17 14:00:00', '2023-12-17 16:30:00', '150.00', 75),
(44, 'Amsterdam', 'Rome', '2023-12-18 15:20:00', '2023-12-18 17:40:00', '170.00', 65),
(45, 'Paris', 'London', '2023-12-19 16:45:00', '2023-12-19 18:00:00', '140.00', 85),
(46, 'Barcelona', 'Madrid', '2023-12-20 10:00:00', '2023-12-20 12:15:00', '130.00', 95),
(47, 'Madrid', 'Berlin', '2023-12-21 11:45:00', '2023-12-21 13:30:00', '160.00', 75),
(48, 'Lisbon', 'Amsterdam', '2023-12-22 09:30:00', '2023-12-22 11:00:00', '180.00', 100),
(49, 'Amsterdam', 'London', '2023-12-23 12:15:00', '2023-12-23 14:45:00', '150.00', 80),
(50, 'Rome', 'Paris', '2023-12-24 14:30:00', '2023-12-24 16:45:00', '160.00', 70),
(51, 'New York', 'Los Angeles', '2023-12-25 08:00:00', '2023-12-25 10:30:00', '250.00', 150),
(52, 'Chicago', 'Miami', '2023-12-26 10:30:00', '2023-12-26 12:00:00', '220.00', 130),
(53, 'San Francisco', 'Las Vegas', '2023-12-27 09:15:00', '2023-12-27 11:45:00', '280.00', 110),
(54, 'Houston', 'Denver', '2023-12-28 11:45:00', '2023-12-28 14:15:00', '300.00', 90),
(55, 'Miami', 'New York', '2023-12-29 07:30:00', '2023-12-29 09:00:00', '260.00', 120),
(56, 'Los Angeles', 'Chicago', '2023-12-30 13:00:00', '2023-12-30 15:30:00', '230.00', 140),
(57, 'Las Vegas', 'San Francisco', '2023-12-31 12:45:00', '2023-12-31 15:15:00', '270.00', 100),
(58, 'Denver', 'Houston', '2024-01-01 14:20:00', '2024-01-01 16:50:00', '290.00', 80),
(59, 'New York', 'San Francisco', '2024-01-02 16:30:00', '2024-01-02 18:45:00', '270.00', 110),
(60, 'Chicago', 'Houston', '2024-01-03 15:10:00', '2024-01-03 17:30:00', '280.00', 100),
(61, 'Las Vegas', 'Miami', '2024-01-04 08:30:00', '2024-01-04 10:45:00', '260.00', 120),
(62, 'San Francisco', 'Los Angeles', '2024-01-05 11:15:00', '2024-01-05 13:45:00', '250.00', 140),
(63, 'New York', 'Chicago', '2024-01-06 12:30:00', '2024-01-06 14:45:00', '280.00', 130),
(64, 'Houston', 'Las Vegas', '2024-01-07 09:45:00', '2024-01-07 11:15:00', '300.00', 110),
(65, 'Miami', 'San Francisco', '2024-01-08 14:00:00', '2024-01-08 16:30:00', '270.00', 90),
(66, 'Chicago', 'New York', '2024-01-09 15:20:00', '2024-01-09 17:40:00', '260.00', 120),
(67, 'Houston', 'Miami', '2024-01-10 16:45:00', '2024-01-10 18:00:00', '240.00', 110),
(68, 'Los Angeles', 'Las Vegas', '2024-01-11 10:00:00', '2024-01-11 12:15:00', '230.00', 100),
(69, 'San Francisco', 'Houston', '2024-01-12 11:45:00', '2024-01-12 13:30:00', '250.00', 80),
(70, 'Miami', 'Chicago', '2024-01-13 10:00:00', '2024-01-13 12:30:00', '270.00', 140),
(71, 'New York', 'Denver', '2024-01-14 12:45:00', '2024-01-14 15:00:00', '290.00', 130),
(72, 'Los Angeles', 'San Francisco', '2024-01-15 09:30:00', '2024-01-15 11:45:00', '280.00', 110),
(73, 'Chicago', 'Las Vegas', '2024-01-16 14:00:00', '2024-01-16 16:30:00', '260.00', 90),
(74, 'Miami', 'New York', '2024-01-17 15:30:00', '2024-01-17 17:45:00', '270.00', 80),
(75, 'San Francisco', 'Denver', '2024-01-18 13:00:00', '2024-01-18 15:30:00', '290.00', 120),
(76, 'Houston', 'Los Angeles', '2024-01-19 08:45:00', '2024-01-19 10:45:00', '240.00', 130),
(77, 'Las Vegas', 'Chicago', '2024-01-20 12:15:00', '2024-01-20 14:30:00', '220.00', 110),
(78, 'New York', 'Miami', '2024-01-21 11:30:00', '2024-01-21 13:45:00', '260.00', 100),
(79, 'Chicago', 'San Francisco', '2024-01-22 10:45:00', '2024-01-22 12:15:00', '270.00', 90),
(80, 'Houston', 'Denver', '2024-01-23 16:00:00', '2024-01-23 18:30:00', '300.00', 140),
(81, 'Los Angeles', 'Las Vegas', '2024-01-24 08:30:00', '2024-01-24 10:45:00', '280.00', 130),
(82, 'Miami', 'Chicago', '2024-01-25 14:00:00', '2024-01-25 16:30:00', '250.00', 120),
(83, 'San Francisco', 'New York', '2024-01-26 15:20:00', '2024-01-26 17:40:00', '280.00', 100),
(84, 'Las Vegas', 'Houston', '2024-01-27 16:45:00', '2024-01-27 18:00:00', '260.00', 90),
(85, 'Denver', 'Los Angeles', '2024-01-28 10:00:00', '2024-01-28 12:15:00', '240.00', 80),
(86, 'New York', 'Chicago', '2024-01-29 11:45:00', '2024-01-29 13:30:00', '260.00', 70),
(87, 'Miami', 'San Francisco', '2024-01-30 14:00:00', '2024-01-30 16:30:00', '240.00', 60),
(88, 'San Francisco', 'Las Vegas', '2024-01-31 13:30:00', '2024-01-31 15:45:00', '280.00', 50),
(89, 'Houston', 'Chicago', '2024-02-01 15:15:00', '2024-02-01 17:45:00', '270.00', 80),
(90, 'Los Angeles', 'New York', '2024-02-02 16:30:00', '2024-02-02 18:45:00', '260.00', 70),
(91, 'Chicago', 'Denver', '2024-02-03 10:45:00', '2024-02-03 12:30:00', '250.00', 90),
(92, 'Miami', 'Las Vegas', '2024-02-04 12:30:00', '2024-02-04 14:45:00', '270.00', 60),
(93, 'New York', 'Houston', '2024-02-05 11:15:00', '2024-02-05 13:45:00', '240.00', 70),
(94, 'San Francisco', 'Los Angeles', '2024-02-06 09:30:00', '2024-02-06 11:45:00', '260.00', 80),
(95, 'Las Vegas', 'Miami', '2024-02-07 14:00:00', '2024-02-07 16:30:00', '280.00', 90),
(96, 'Chicago', 'San Francisco', '2024-02-08 15:45:00', '2024-02-08 17:00:00', '250.00', 100),
(97, 'Denver', 'New York', '2024-02-09 16:15:00', '2024-02-09 18:30:00', '260.00', 110),
(98, 'Houston', 'Los Angeles', '2024-02-10 08:30:00', '2024-02-10 10:45:00', '270.00', 120),
(99, 'Las Vegas', 'Chicago', '2024-02-11 10:00:00', '2024-02-11 12:15:00', '280.00', 130),
(100, 'Miami', 'San Francisco', '2024-02-12 12:45:00', '2024-02-12 14:30:00', '240.00', 140),
(101, 'New York', 'Amsterdam', '2024-02-29 08:00:00', '2024-02-29 10:30:00', '350.00', 150),
(102, 'Los Angeles', 'Paris', '2024-03-01 10:30:00', '2024-03-01 12:00:00', '320.00', 130),
(103, 'Miami', 'Rome', '2024-03-02 09:15:00', '2024-03-02 11:45:00', '380.00', 110),
(104, 'Houston', 'London', '2024-03-03 11:45:00', '2024-03-03 14:15:00', '400.00', 90),
(105, 'Las Vegas', 'Berlin', '2024-03-04 07:30:00', '2024-03-04 09:00:00', '360.00', 120),
(106, 'Chicago', 'Lisbon', '2024-03-05 13:00:00', '2024-03-05 15:30:00', '330.00', 140),
(107, 'San Francisco', 'Barcelona', '2024-03-06 12:45:00', '2024-03-06 15:15:00', '370.00', 100),
(108, 'Denver', 'Madrid', '2024-03-07 14:20:00', '2024-03-07 16:50:00', '390.00', 80),
(109, 'New York', 'Barcelona', '2024-03-08 16:30:00', '2024-03-08 18:45:00', '370.00', 110),
(110, 'Los Angeles', 'Rome', '2024-03-09 15:10:00', '2024-03-09 17:30:00', '380.00', 100),
(111, 'Miami', 'Amsterdam', '2024-03-10 08:30:00', '2024-03-10 10:45:00', '360.00', 130),
(112, 'Houston', 'Lisbon', '2024-03-11 11:15:00', '2024-03-11 13:45:00', '350.00', 120),
(113, 'Las Vegas', 'Berlin', '2024-03-12 12:30:00', '2024-03-12 14:45:00', '380.00', 110),
(114, 'Chicago', 'London', '2024-03-13 09:45:00', '2024-03-13 11:15:00', '400.00', 100),
(115, 'San Francisco', 'Madrid', '2024-03-14 14:00:00', '2024-03-14 16:30:00', '370.00', 90),
(116, 'Denver', 'Paris', '2024-03-15 15:20:00', '2024-03-15 17:40:00', '350.00', 120);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
