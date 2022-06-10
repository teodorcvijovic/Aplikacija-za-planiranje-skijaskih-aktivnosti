-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: jahorina_test
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
-- Table structure for table `jahorina_skitrack`
--

DROP TABLE IF EXISTS `jahorina_skitrack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jahorina_skitrack` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `color` int NOT NULL,
  `length` int NOT NULL,
  `is_foggy` tinyint(1) NOT NULL,
  `is_opened` tinyint(1) NOT NULL,
  `is_busy` tinyint(1) NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  `comment` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jahorina_skitrack`
--

LOCK TABLES `jahorina_skitrack` WRITE;
/*!40000 ALTER TABLE `jahorina_skitrack` DISABLE KEYS */;
INSERT INTO `jahorina_skitrack` VALUES (8,'Poljice',0,10,0,1,0,'2022-06-10 23:36:47.930482','#$&!'),(9,'Ogorjelica',1,13,0,1,0,'2022-06-10 21:47:59.000000','Trenutno nema novih obavestenja.'),(10,'Skocine',1,10,0,1,0,'2022-06-10 21:47:59.000000','Trenutno nema novih obavestenja.'),(11,'Olimpijski spust',2,9,0,1,0,'2022-06-10 21:47:59.000000','Trenutno nema novih obavestenja.'),(12,'Rajska Vrata',1,10,0,1,0,'2022-06-10 21:47:59.000000','Trenutno nema novih obavestenja.'),(13,'Olimpijski Veleslalom',2,6,0,1,0,'2022-06-10 21:47:59.000000','Trenutno nema novih obavestenja.');
/*!40000 ALTER TABLE `jahorina_skitrack` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-11  0:19:26
