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
-- Table structure for table `jahorina_activity`
--

DROP TABLE IF EXISTS `jahorina_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jahorina_activity` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `obj_name` varchar(100) DEFAULT NULL,
  `obj_contact` varchar(17) DEFAULT NULL,
  `x` decimal(21,20) NOT NULL,
  `y` decimal(21,20) NOT NULL,
  `skitrack_id` bigint NOT NULL,
  `type_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jahorina_activity_skitrack_id_ec2644f9_fk_jahorina_skitrack_id` (`skitrack_id`),
  KEY `jahorina_activity_type_id_d6f04942_fk_jahorina_category_id` (`type_id`),
  CONSTRAINT `jahorina_activity_skitrack_id_ec2644f9_fk_jahorina_skitrack_id` FOREIGN KEY (`skitrack_id`) REFERENCES `jahorina_skitrack` (`id`),
  CONSTRAINT `jahorina_activity_type_id_d6f04942_fk_jahorina_category_id` FOREIGN KEY (`type_id`) REFERENCES `jahorina_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jahorina_activity`
--

LOCK TABLES `jahorina_activity` WRITE;
/*!40000 ALTER TABLE `jahorina_activity` DISABLE KEYS */;
INSERT INTO `jahorina_activity` VALUES (42,'Hotel Termag','+311 313 3331',0.47533092659446446000,0.64879029955393690000,7,24),(43,'Olimp Bar','+311 313 3331',0.56644318377170360000,0.18400898471456400000,7,25),(44,'Rajska Vrata','+311 313 3331',0.34210073921265255000,0.45209104003147190000,6,22),(45,'Peggy','+311 313 3331',0.53292074952724770000,0.45526360873344710000,9,21),(46,'Cafe Vrh','+311 313 3331',0.36616812790097986000,0.28553118317777170000,9,26),(47,'Buregdžinica','+311 313 3331',0.88189788550799380000,0.65830800565986260000,8,27),(49,'Klub','+3132424 242',0.18378164917450143000,0.35878310860336665000,7,25),(50,'Peggy Cafe','+342424',0.39794043044396177000,0.57881806192652510000,7,26);
/*!40000 ALTER TABLE `jahorina_activity` ENABLE KEYS */;
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
