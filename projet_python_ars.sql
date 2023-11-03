-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 03 nov. 2023 à 10:42
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

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
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Type` enum('Regular','Senior','Child','Guest') NOT NULL,
  `MembershipNumber` int DEFAULT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
(10, 'Rome', 'Paris', '2023-11-14 15:10:00', '2023-11-14 17:30:00', '170.00', 60);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
