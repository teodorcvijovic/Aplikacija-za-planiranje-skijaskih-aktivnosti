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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jahorina_myuser`
--

LOCK TABLES `jahorina_myuser` WRITE;
/*!40000 ALTER TABLE `jahorina_myuser` DISABLE KEYS */;
INSERT INTO `jahorina_myuser` VALUES (8,'pbkdf2_sha256$320000$dzewPePIJkbabFVqWcxwPx$co9EB2XARShYNs3j5e+VlNX0H2OPpVScig61q5/wn4Y=','2022-06-10 21:48:21.919880',1,'teo','','','',1,1,'2022-06-10 19:13:50.028564',0),(9,'pbkdf2_sha256$320000$KhLR6Nydyu43FXShnjRNaP$ghwF8O2idRVTVB+IEaIP+bTWFW6H1XhrKv60r55d/w0=','2022-06-10 21:37:03.972460',0,'filip','Filip','Stojsavljevic','filip@gmail.com',0,1,'2022-06-10 19:30:00.000000',0),(10,'pbkdf2_sha256$320000$KhLR6Nydyu43FXShnjRNaP$ghwF8O2idRVTVB+IEaIP+bTWFW6H1XhrKv60r55d/w0=','2022-06-10 19:31:01.000000',0,'teodor','Teodor','Cvijovic','cvijovicteodor@outlook.com',0,1,'2022-06-10 19:30:57.000000',0),(11,'lara','2022-06-10 19:31:37.000000',0,'lara','Lara','Petrovic','lara@gmail.com',0,1,'2022-06-10 19:31:30.000000',0),(12,'pbkdf2_sha256$320000$KhLR6Nydyu43FXShnjRNaP$ghwF8O2idRVTVB+IEaIP+bTWFW6H1XhrKv60r55d/w0=','2022-06-10 19:32:39.000000',0,'zika','Zika','Zikic','zika@gmail.com',0,1,'2022-06-10 19:32:33.000000',0),(13,'pbkdf2_sha256$320000$KhLR6Nydyu43FXShnjRNaP$ghwF8O2idRVTVB+IEaIP+bTWFW6H1XhrKv60r55d/w0=','2022-06-10 19:33:13.000000',0,'pera','Pera','Peric','pera@gmail.com',0,1,'2022-06-10 19:33:08.000000',0),(14,'pbkdf2_sha256$320000$cEf7M7fPhIq6LhIlEfmJhJ$1YKfXwAvzLdgJ9Vdl4yMtOZKue5oJ1HkEpC/V19kRxM=','2022-06-10 21:14:36.247547',0,'nikola','Nikola','Jovanovic','dzoni1@gmail.com',0,1,'2022-06-10 21:14:35.947906',0),(15,'pbkdf2_sha256$320000$MlYlwXZfxCKzXH8Hep5sT5$8mUKzAKnRcVosH026wrmn4voEboZG0DknGlBquNOX2s=','2022-06-10 21:15:06.996012',0,'nikola10','Nikola','Jovanovic','dzoni1@gmail.com',0,1,'2022-06-10 21:15:06.578372',0),(16,'pbkdf2_sha256$320000$7GPeztV8DI3DRoABqFKMT5$pvLzpOOvkHaOO4j8OR06W1/O7/tdSC4WYawVL94//rc=','2022-06-10 21:32:44.103053',0,'nikola101','Nikola','Jovanovic','dzoni1@gmail.com',0,1,'2022-06-10 21:32:43.659616',0);
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

-- Dump completed on 2022-06-11  0:19:25
