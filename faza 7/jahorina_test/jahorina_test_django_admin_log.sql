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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_jahorina_myuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_jahorina_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `jahorina_myuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-06-10 19:24:37.117192','7','nikola10',3,'',6,8),(2,'2022-06-10 19:24:42.251043','6','nikola',3,'',6,8),(3,'2022-06-10 19:24:49.498854','5','mod',3,'',6,8),(4,'2022-06-10 19:24:57.878105','4','pera',3,'',6,8),(5,'2022-06-10 19:25:02.938134','3','zika',3,'',6,8),(6,'2022-06-10 19:25:14.512441','2','mika',3,'',6,8),(7,'2022-06-10 19:27:46.753649','1','default',1,'[{\"added\": {}}]',3,8),(8,'2022-06-10 19:29:06.546981','1','filip',3,'',6,8),(9,'2022-06-10 19:30:57.097087','9','filip',1,'[{\"added\": {}}]',9,8),(10,'2022-06-10 19:31:30.472553','10','teodor',1,'[{\"added\": {}}]',9,8),(11,'2022-06-10 19:32:33.426558','11','lara',1,'[{\"added\": {}}]',9,8),(12,'2022-06-10 19:33:07.984376','12','zika',1,'[{\"added\": {}}]',9,8),(13,'2022-06-10 19:33:40.150536','13','pera',1,'[{\"added\": {}}]',9,8),(14,'2022-06-10 19:46:21.657566','1','Kafa',1,'[{\"added\": {}}]',7,8),(15,'2022-06-10 19:46:36.708018','2','Dorucak',1,'[{\"added\": {}}]',7,8),(16,'2022-06-10 19:46:45.511984','3','Izlazak',1,'[{\"added\": {}}]',7,8),(17,'2022-06-10 19:46:53.232524','4','Rucak',1,'[{\"added\": {}}]',7,8),(18,'2022-06-10 19:47:01.217955','5','Vecera',1,'[{\"added\": {}}]',7,8),(19,'2022-06-10 19:48:25.753541','8','Poljice',1,'[{\"added\": {}}]',8,8),(20,'2022-06-10 19:48:37.507219','9','Ogorjelica',1,'[{\"added\": {}}]',8,8),(21,'2022-06-10 19:48:50.299260','10','Skocine',1,'[{\"added\": {}}]',8,8),(22,'2022-06-10 19:49:05.507022','11','Olimpijski spust',1,'[{\"added\": {}}]',8,8),(23,'2022-06-10 19:50:38.998436','1','Peggy +3132424 242',1,'[{\"added\": {}}]',10,8),(24,'2022-06-10 19:51:28.688576','2','Olimp +3132424 242',1,'[{\"added\": {}}]',10,8),(25,'2022-06-10 19:52:25.511960','4','Ski bar Freeze +3132424 242',1,'[{\"added\": {}}]',10,8),(26,'2022-06-10 19:53:01.702600','5','Konoba Raj +3132424 242',1,'[{\"added\": {}}]',10,8),(27,'2022-06-10 19:53:33.586637','6','Rajska Vrata +3132424 242',1,'[{\"added\": {}}]',10,8),(28,'2022-06-10 19:54:19.101096','7','Olimpijski +3132424 242',1,'[{\"added\": {}}]',10,8),(29,'2022-06-10 20:29:56.439643','12','Rajska Vrata',1,'[{\"added\": {}}]',8,8),(30,'2022-06-10 20:33:37.499159','9','Rajska Vrata +3132424 242',3,'',10,8),(31,'2022-06-10 20:52:41.297576','13','Olimpijski Veleslalom',1,'[{\"added\": {}}]',8,8),(32,'2022-06-10 21:39:11.685428','17','nikola58',3,'',9,8),(33,'2022-06-10 21:51:44.356084','10','Rajska Vrata +3132424 242',3,'',10,8),(34,'2022-06-10 21:53:47.662520','11','Rajska Vrata +3132424 242',3,'',10,8),(35,'2022-06-10 21:58:40.221763','8','Dorucak',1,'[{\"added\": {}}]',7,8),(36,'2022-06-10 21:59:15.272156','12','Olimp +3132424 242',1,'[{\"added\": {}}]',10,8),(37,'2022-06-10 22:01:31.988896','12','Olimp +3132424 242',2,'[{\"changed\": {\"fields\": [\"X\", \"Y\"]}}]',10,8);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
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
