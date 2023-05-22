-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: FELICITY
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `COORDINATORS`
--

DROP TABLE IF EXISTS `COORDINATORS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `COORDINATORS` (
  `COORD_Roll_Number` int NOT NULL,
  PRIMARY KEY (`COORD_Roll_Number`),
  CONSTRAINT `COORDINATORS_ibfk_1` FOREIGN KEY (`COORD_Roll_Number`) REFERENCES `STUDENTS` (`Roll_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COORDINATORS`
--

LOCK TABLES `COORDINATORS` WRITE;
/*!40000 ALTER TABLE `COORDINATORS` DISABLE KEYS */;
INSERT INTO `COORDINATORS` VALUES (2017103791),(2018102991),(2020113251),(2021101063),(2021111007);
/*!40000 ALTER TABLE `COORDINATORS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EVENTS`
--

DROP TABLE IF EXISTS `EVENTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EVENTS` (
  `Event_Name` varchar(50) DEFAULT NULL,
  `EVENT_TYPE` varchar(15) DEFAULT NULL,
  `VENUE` varchar(30) DEFAULT NULL,
  `ORGANISED_BY` varchar(30) DEFAULT NULL,
  `COORD_Roll_Number` int DEFAULT NULL,
  `APPROVED` tinyint(1) DEFAULT NULL,
  `Event_Number` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Event_Number`),
  KEY `COORD_Roll_Number` (`COORD_Roll_Number`),
  CONSTRAINT `EVENTS_ibfk_1` FOREIGN KEY (`COORD_Roll_Number`) REFERENCES `COORDINATORS` (`COORD_Roll_Number`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EVENTS`
--

LOCK TABLES `EVENTS` WRITE;
/*!40000 ALTER TABLE `EVENTS` DISABLE KEYS */;
INSERT INTO `EVENTS` VALUES ('trasion','cultural','Bakul Warehouse','fashion club',2017103791,1,1),('pentastic','cultural','Amphi','artsoc',2021111007,1,2),('vismriti','cultural','Vindhya','music club',2020113251,0,3),('story teller','cultural','Felicity Ground','literature club',2021111007,0,4),('robotic seminar','technical','Bakul Warehouse','robotics club',2020113251,1,5),('Music hair','misc','Amphi','debsoc',2021111007,1,7);
/*!40000 ALTER TABLE `EVENTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EXPENDITURE`
--

DROP TABLE IF EXISTS `EXPENDITURE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EXPENDITURE` (
  `Event_Number` int NOT NULL,
  `FUND_PROPOSED` int DEFAULT NULL,
  `FUND_RELEASED` int DEFAULT NULL,
  PRIMARY KEY (`Event_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EXPENDITURE`
--

LOCK TABLES `EXPENDITURE` WRITE;
/*!40000 ALTER TABLE `EXPENDITURE` DISABLE KEYS */;
INSERT INTO `EXPENDITURE` VALUES (1,20000,16999),(2,40000,5000),(5,0,0),(7,7979,7878);
/*!40000 ALTER TABLE `EXPENDITURE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FOOD_OPTIONS`
--

DROP TABLE IF EXISTS `FOOD_OPTIONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FOOD_OPTIONS` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `STALL_NAME` varchar(50) DEFAULT NULL,
  `ITEM` varchar(50) DEFAULT NULL,
  `PRICE` int DEFAULT NULL,
  PRIMARY KEY (`SNo`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FOOD_OPTIONS`
--

LOCK TABLES `FOOD_OPTIONS` WRITE;
/*!40000 ALTER TABLE `FOOD_OPTIONS` DISABLE KEYS */;
INSERT INTO `FOOD_OPTIONS` VALUES (1,'BEVERAGE STALL','TEA',10),(2,'BERVERAGE STALL','COFFEE',15),(3,'BERVERAGE STALL','GREEN TEA',30),(4,'FOODIEE STALL','NOODLES',70),(5,'FOODIEE STALL','MOMO',180),(6,'FOODIEE STALL','BURGER',269),(7,'THE CHEESE STALL','PIZZA',300),(8,'THE CHEESE STALL','PASTA',100);
/*!40000 ALTER TABLE `FOOD_OPTIONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FOOD_STALLS`
--

DROP TABLE IF EXISTS `FOOD_STALLS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FOOD_STALLS` (
  `STALL_NAME` varchar(50) NOT NULL,
  `TENDER_PRICE` int DEFAULT NULL,
  PRIMARY KEY (`STALL_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FOOD_STALLS`
--

LOCK TABLES `FOOD_STALLS` WRITE;
/*!40000 ALTER TABLE `FOOD_STALLS` DISABLE KEYS */;
INSERT INTO `FOOD_STALLS` VALUES ('BERVERAGE STALL',20000),('Drinks Corner',15000),('FOODIEE STALL',30000),('haldiram spec',1201),('THE CHEESE STALL',50000);
/*!40000 ALTER TABLE `FOOD_STALLS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `INCOME`
--

DROP TABLE IF EXISTS `INCOME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `INCOME` (
  `SOURCE_NAME` varchar(50) NOT NULL,
  `AMOUNT` int DEFAULT NULL,
  PRIMARY KEY (`SOURCE_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `INCOME`
--

LOCK TABLES `INCOME` WRITE;
/*!40000 ALTER TABLE `INCOME` DISABLE KEYS */;
INSERT INTO `INCOME` VALUES ('APPLE',100000),('BERVERAGE STALL',20000),('Drinks Corner',15000),('FOODIEE STALL',30000),('haldiram spec',1201),('JIO',300000),('SAMSUNG',50000),('TATA',40000),('THE CHEESE STALL',50000);
/*!40000 ALTER TABLE `INCOME` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PARTICIPANT_LIST`
--

DROP TABLE IF EXISTS `PARTICIPANT_LIST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PARTICIPANT_LIST` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `Event_Number` int DEFAULT NULL,
  `Roll_Number` int DEFAULT NULL,
  PRIMARY KEY (`SNo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PARTICIPANT_LIST`
--

LOCK TABLES `PARTICIPANT_LIST` WRITE;
/*!40000 ALTER TABLE `PARTICIPANT_LIST` DISABLE KEYS */;
INSERT INTO `PARTICIPANT_LIST` VALUES (1,1,2022202991),(2,6,2022202991),(3,3,2021111007);
/*!40000 ALTER TABLE `PARTICIPANT_LIST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SCHEDULE`
--

DROP TABLE IF EXISTS `SCHEDULE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SCHEDULE` (
  `Event_Name` varchar(50) NOT NULL,
  `TIME` time DEFAULT NULL,
  `ORGANISED_BY` varchar(30) NOT NULL,
  PRIMARY KEY (`Event_Name`,`ORGANISED_BY`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SCHEDULE`
--

LOCK TABLES `SCHEDULE` WRITE;
/*!40000 ALTER TABLE `SCHEDULE` DISABLE KEYS */;
INSERT INTO `SCHEDULE` VALUES ('Music hair','17:30:00','debsoc'),('pentastic','10:30:00','artsoc'),('robotic seminar','15:00:00','robotics club'),('story teller','10:30:00','literature club'),('trasion','10:30:00','fashion club'),('vismriti','10:30:00','music club');
/*!40000 ALTER TABLE `SCHEDULE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SPONSORED_EVENTS`
--

DROP TABLE IF EXISTS `SPONSORED_EVENTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SPONSORED_EVENTS` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `Event_Number` int DEFAULT NULL,
  `SPONSOR_NAME` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`SNo`),
  KEY `SPONSOR_NAME` (`SPONSOR_NAME`),
  KEY `Event_Number` (`Event_Number`),
  CONSTRAINT `SPONSORED_EVENTS_ibfk_1` FOREIGN KEY (`SPONSOR_NAME`) REFERENCES `SPONSORS` (`SPONSOR_NAME`),
  CONSTRAINT `SPONSORED_EVENTS_ibfk_2` FOREIGN KEY (`Event_Number`) REFERENCES `EVENTS` (`Event_Number`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SPONSORED_EVENTS`
--

LOCK TABLES `SPONSORED_EVENTS` WRITE;
/*!40000 ALTER TABLE `SPONSORED_EVENTS` DISABLE KEYS */;
INSERT INTO `SPONSORED_EVENTS` VALUES (1,1,'SAMSUNG'),(2,1,'APPLE'),(3,1,'TATA'),(5,5,'TATA');
/*!40000 ALTER TABLE `SPONSORED_EVENTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SPONSORS`
--

DROP TABLE IF EXISTS `SPONSORS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SPONSORS` (
  `SPONSOR_NAME` varchar(50) NOT NULL,
  `AMOUNT` int DEFAULT NULL,
  PRIMARY KEY (`SPONSOR_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SPONSORS`
--

LOCK TABLES `SPONSORS` WRITE;
/*!40000 ALTER TABLE `SPONSORS` DISABLE KEYS */;
INSERT INTO `SPONSORS` VALUES ('APPLE',100000),('JIO',300000),('SAMSUNG',50000),('TATA',40000);
/*!40000 ALTER TABLE `SPONSORS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STUDENTS`
--

DROP TABLE IF EXISTS `STUDENTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `STUDENTS` (
  `First_Name` varchar(30) DEFAULT NULL,
  `Middle_Name` varchar(30) DEFAULT NULL,
  `Last_Name` varchar(30) DEFAULT NULL,
  `Roll_Number` int NOT NULL,
  `DOB` date DEFAULT NULL,
  PRIMARY KEY (`Roll_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STUDENTS`
--

LOCK TABLES `STUDENTS` WRITE;
/*!40000 ALTER TABLE `STUDENTS` DISABLE KEYS */;
INSERT INTO `STUDENTS` VALUES ('Chandana','Shinde','Penukonda',2017103791,'1998-11-02'),('Varenya',NULL,NULL,2017110111,'2001-06-11'),('Sriya',NULL,NULL,2018102891,'2003-09-27'),('Vishna',NULL,'Panyala',2018102991,'2003-09-27'),('Vaishnavi','Shah','Ovhal',2019103251,'2000-01-02'),('Mihi',NULL,'Kats',2019103491,'2002-05-20'),('Pooja',NULL,'Shinde',2019103791,'2001-12-20'),('Pucker','Kunal','Naij',2019213451,'1999-07-30'),('Boomi',NULL,'Papireddy',2019223451,'1998-08-30'),('Shakira','Shrikara','Kara',2020113251,'2002-06-12'),('Siddart','Pinchinakodaka','Naij',2020113450,'2003-01-30'),('Pranjali',NULL,'Bishnoi',2020203251,'1998-03-12'),('wgvyrt','Ming','Fesx',2020213150,'1998-02-28'),('Rutuja',NULL,NULL,2020213251,'2000-06-12'),('Gauri','Singh','Fooo',2020213450,'1997-03-31'),('Rushil',NULL,'Satvik',2021101060,'2003-05-30'),('Rushil',NULL,'Kaul',2021101063,'2003-05-20'),('Sunkari','Sai','Satvik',2021101117,'2004-01-01'),('Harshitha','Sri','Mareddy',2021102111,'2004-05-11'),('Roja','Papireddy','Sahoo',2021105821,'2004-02-21'),('Mihika',NULL,'Sanghi',2021106801,'2004-01-21'),('Sreenivas','Bhumireddy','Papireddy',2021111007,'2003-05-11'),('Meghana',NULL,'Tedla',2021113450,'2005-01-30'),('Siddhi',NULL,'Agarwal',2021202111,'2000-05-11'),('Janhavi',NULL,'Moze',2022102991,'2006-08-17'),('Vanshika','Dhengra','Shastri',2022202991,'2001-09-17');
/*!40000 ALTER TABLE `STUDENTS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27 21:01:20
