-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: pythonlogin
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `movies_users`
--

DROP TABLE IF EXISTS `movies_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usersid` int(11) NOT NULL,
  `moviesid` int(11) NOT NULL,
  `prefer` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid_idx` (`usersid`),
  KEY `movieid_idx` (`moviesid`),
  CONSTRAINT `movieid` FOREIGN KEY (`moviesid`) REFERENCES `movies` (`id`),
  CONSTRAINT `userid` FOREIGN KEY (`usersid`) REFERENCES `accounts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=191 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies_users`
--

LOCK TABLES `movies_users` WRITE;
/*!40000 ALTER TABLE `movies_users` DISABLE KEYS */;
INSERT INTO `movies_users` VALUES (152,1,8,2),(153,1,101,2),(154,1,102,1),(155,1,173,1),(156,1,179,1),(157,1,250,1),(158,1,9,1),(159,1,111,1),(160,1,112,1),(161,1,191,1),(162,1,195,1),(163,1,198,1),(164,1,201,1),(165,1,278,1),(166,1,264,1),(167,1,332,1),(168,1,333,1),(169,1,231,1),(170,1,232,1),(171,1,235,1),(172,1,1502,1),(173,1,2004,1),(174,1,2953,1),(175,1,26,2),(176,1,50,2),(177,1,95,2),(178,1,175,2),(179,1,252,2),(180,1,289,2),(181,1,301,2),(182,1,443,2),(183,1,890,2),(184,1,17,2),(185,1,27,2),(186,1,84,2),(187,1,168,2),(188,1,1142,1),(189,1,3923,1),(190,1,4324,1);
/*!40000 ALTER TABLE `movies_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-14 22:44:32
