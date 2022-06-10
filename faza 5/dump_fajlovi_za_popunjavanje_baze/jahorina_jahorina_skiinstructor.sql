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
-- Table structure for table `jahorina_skiinstructor`
--

DROP TABLE IF EXISTS `jahorina_skiinstructor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jahorina_skiinstructor` (
  `myuser_ptr_id` bigint NOT NULL,
  `phone` varchar(17) NOT NULL,
  `instagram` varchar(290) DEFAULT NULL,
  `facebook` varchar(290) DEFAULT NULL,
  `snapchat` varchar(290) DEFAULT NULL,
  `experience` int NOT NULL,
  `birthdate` date NOT NULL,
  PRIMARY KEY (`myuser_ptr_id`),
  CONSTRAINT `jahorina_skiinstruct_myuser_ptr_id_befe6e16_fk_jahorina_` FOREIGN KEY (`myuser_ptr_id`) REFERENCES `jahorina_myuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jahorina_skiinstructor`
--

LOCK TABLES `jahorina_skiinstructor` WRITE;
/*!40000 ALTER TABLE `jahorina_skiinstructor` DISABLE KEYS */;
INSERT INTO `jahorina_skiinstructor` VALUES (7,'+381 60 313 3131','https://www.instagram.com/teodorcv/','t','t',2,'2022-05-03'),(8,'+382 31 313 3131','','s','',4,'2022-05-05');
/*!40000 ALTER TABLE `jahorina_skiinstructor` ENABLE KEYS */;
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
