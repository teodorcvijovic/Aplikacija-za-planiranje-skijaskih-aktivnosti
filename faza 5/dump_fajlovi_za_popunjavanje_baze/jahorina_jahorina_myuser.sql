-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: jahorina
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `jahorina_myuser`
--

DROP TABLE IF EXISTS `jahorina_myuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jahorina_myuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_moderator` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jahorina_myuser`
--

LOCK TABLES `jahorina_myuser` WRITE;
/*!40000 ALTER TABLE `jahorina_myuser` DISABLE KEYS */;
INSERT INTO `jahorina_myuser` VALUES (1,'pbkdf2_sha256$320000$8ADuDOddqKhhMfeR5aADAc$BnMiUO5FT2uqTrsjxHNPWEhNCkr8y/CNmBSDZuMrob0=','2022-05-29 11:09:00.681919',1,'admin','','','',1,1,'2022-05-19 23:04:20.016060',0),(7,'pbkdf2_sha256$320000$gYYArYqH4hiu1b3dvE7Rk9$w4GKg45wfqIzodtwNkJJ4HkKstL+uf+6jZNn/cnUqQI=','2022-05-24 01:28:10.403472',0,'teodor','Teodor','Cvijovic','cvijovicteodor@outlook.com',0,1,'2022-05-24 01:16:40.837636',0),(8,'pbkdf2_sha256$320000$7BjxPD0PFczBi2gzxJ4OJe$/9RkmjNjzyfO1r5mwoVuAcOE2MigEDu65oFwTnkYtVY=','2022-05-24 01:18:46.166143',0,'tasha','Tamara','Sekularac','tasha@gmail.com',0,1,'2022-05-24 01:18:46.047043',0);
/*!40000 ALTER TABLE `jahorina_myuser` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-31  1:29:44
