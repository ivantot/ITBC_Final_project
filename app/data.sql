-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: expense_tracker
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `budgets`
--

DROP TABLE IF EXISTS `budgets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `budgets` (
  `budget_id` varchar(50) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `balance` float DEFAULT NULL,
  `limit` float DEFAULT NULL,
  `currency` varchar(10) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `user_id` varchar(50) NOT NULL,
  `category_id` varchar(50) NOT NULL,
  PRIMARY KEY (`budget_id`),
  UNIQUE KEY `user_category_is_active_uc` (`user_id`,`category_id`,`is_active`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `budgets_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `budgets_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`),
  CONSTRAINT `budget_currencies_cc` CHECK ((`currency` in (_utf8mb4'DIN',_utf8mb4'EUR'))),
  CONSTRAINT `start_end_cc` CHECK ((`start_date` < `end_date`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `budgets`
--

LOCK TABLES `budgets` WRITE;
/*!40000 ALTER TABLE `budgets` DISABLE KEYS */;
INSERT INTO `budgets` VALUES ('083cac6a-633f-4c28-9412-2da2b6867dd4','beauty spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'2e352223-7400-4a9b-bb4f-6548916d18da','71605e19-c7e6-4dad-89b3-400793cabec8'),('0b29b05a-1260-48f4-a8c6-c5a08b87b976','books spring budget',137.29,150,'EUR','2023-01-01','2023-04-30',1,'c81913ba-8744-4f0d-af63-3e451411069b','e75e0c17-2b7c-44df-b5d9-f93662c6593f'),('15f1a69d-c620-4767-a097-39c56c17dfaa','entertainment spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'49d05b82-8e81-4508-9b61-9a8039b4db56','54f39350-9b89-4a48-aad6-e41db60bbefa'),('17523ff0-0714-4479-9509-d82c3a54fd72','entertainment spring budget',26.24,200,'EUR','2023-01-01','2023-04-30',1,'c81913ba-8744-4f0d-af63-3e451411069b','54f39350-9b89-4a48-aad6-e41db60bbefa'),('2c4c1669-3b24-4505-8223-ea81d3562ec0','clothes spring budget',0,100,'EUR','2023-01-01','2023-04-30',1,'49d05b82-8e81-4508-9b61-9a8039b4db56','111b8ed3-a45e-4a0c-a02f-f14d64318311'),('41bf5761-a45f-4e81-a18f-66bb5464c367','beauty spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'c81913ba-8744-4f0d-af63-3e451411069b','71605e19-c7e6-4dad-89b3-400793cabec8'),('485f5252-a6b2-4a9a-ac21-66ed08d7043f','doctor spring budget',245.47,50,'EUR','2023-01-01','2023-04-30',1,'c81913ba-8744-4f0d-af63-3e451411069b','94156b13-6e17-489f-ac0d-12217c03ccf5'),('4b00d7d8-5439-44fc-83fa-3d418b5e75b6','sports spring budget',100,50,'EUR','2023-01-01','2023-04-30',1,'a6a2e662-ffc6-44fd-807c-8a308688dc1d','bf968dd9-be47-440d-bcc1-322a3575a25d'),('50eb3e11-1b63-402e-a548-c2e11c6bf7b2','entertainment spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'1de62eb1-1b71-4862-9059-ff56cca0b491','54f39350-9b89-4a48-aad6-e41db60bbefa'),('5a1ef6c7-83a2-45f4-8c97-c1a70b3de859','clothes spring budget',0,500,'EUR','2023-01-01','2023-04-30',1,'2e352223-7400-4a9b-bb4f-6548916d18da','111b8ed3-a45e-4a0c-a02f-f14d64318311'),('6da6e592-6f28-42dc-a1d7-22bb62a24538','beauty spring budget',2.97,100,'EUR','2023-01-01','2023-04-30',1,'c81913ba-8744-4f0d-af63-3e451411069b','9275f7fd-06d2-49de-a408-ed91964bddae'),('6ff1a548-d5a2-42db-aecc-00b7dca52e30','sports spring budget',68,50,'EUR','2023-01-01','2023-04-30',1,'c81913ba-8744-4f0d-af63-3e451411069b','bf968dd9-be47-440d-bcc1-322a3575a25d'),('71f32b60-a86c-4eb5-b8f6-517cb6ddc062','doctor spring budget',42.05,50,'EUR','2023-01-01','2023-04-30',1,'a6a2e662-ffc6-44fd-807c-8a308688dc1d','94156b13-6e17-489f-ac0d-12217c03ccf5'),('72bec648-2f59-4d62-9b80-98ddfc9eb6d0','entertainment spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'2e352223-7400-4a9b-bb4f-6548916d18da','54f39350-9b89-4a48-aad6-e41db60bbefa'),('9032523e-5c31-4ed1-a2a2-e8becffca4ce','sports spring budget',0,50,'EUR','2023-01-01','2023-04-30',1,'d1e717d0-e817-4a73-8f88-32a810dcc21c','bf968dd9-be47-440d-bcc1-322a3575a25d'),('90985601-d6fc-4da0-9f94-99e8541f96e6','beauty spring budget',48.97,200,'EUR','2023-01-01','2023-04-30',1,'a6a2e662-ffc6-44fd-807c-8a308688dc1d','71605e19-c7e6-4dad-89b3-400793cabec8'),('93e976ff-320c-42b5-aaf6-f28ff1d2d3b9','entertainment spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'3c50eb81-9aa5-462f-8cde-8460e1e331c9','54f39350-9b89-4a48-aad6-e41db60bbefa'),('9c15f93c-6a74-444b-a5fb-fda3578e4787','clothes spring budget',0,500,'EUR','2023-01-01','2023-04-30',1,'1de62eb1-1b71-4862-9059-ff56cca0b491','111b8ed3-a45e-4a0c-a02f-f14d64318311'),('a1126c83-2cf6-46d1-9f07-fd2f07a862f5','books spring budget',10.17,150,'EUR','2023-01-01','2023-04-30',1,'d1e717d0-e817-4a73-8f88-32a810dcc21c','e75e0c17-2b7c-44df-b5d9-f93662c6593f'),('aa0cd8f3-9146-406f-9d16-45c7dac1ff0f','entertainment spring budget',42.37,200,'EUR','2023-01-01','2023-04-30',1,'d1e717d0-e817-4a73-8f88-32a810dcc21c','54f39350-9b89-4a48-aad6-e41db60bbefa'),('abc989aa-1d64-4508-8a16-a5e75eab6b01','beauty spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'1de62eb1-1b71-4862-9059-ff56cca0b491','71605e19-c7e6-4dad-89b3-400793cabec8'),('ba6f8527-143e-4129-9762-cc9c523f6101','clothes spring budget',0,100,'EUR','2023-01-01','2023-04-30',1,'3c50eb81-9aa5-462f-8cde-8460e1e331c9','111b8ed3-a45e-4a0c-a02f-f14d64318311'),('bccf43a4-28b6-439d-b21f-467d26a1a251','books spring budget',41.77,150,'EUR','2023-01-01','2023-04-30',1,'a6a2e662-ffc6-44fd-807c-8a308688dc1d','e75e0c17-2b7c-44df-b5d9-f93662c6593f'),('c60471a1-949f-43d7-9759-cf51054ad856','doctor spring budget',44,50,'EUR','2023-01-01','2023-04-30',1,'d1e717d0-e817-4a73-8f88-32a810dcc21c','94156b13-6e17-489f-ac0d-12217c03ccf5'),('ca40f6a6-f19b-46f8-8eb3-99af24516a41','entertainment spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'a6a2e662-ffc6-44fd-807c-8a308688dc1d','54f39350-9b89-4a48-aad6-e41db60bbefa'),('d1b01544-1f6f-4c79-8413-f80bd05096bd','beauty spring budget',10.17,100,'EUR','2023-01-01','2023-04-30',1,'d1e717d0-e817-4a73-8f88-32a810dcc21c','9275f7fd-06d2-49de-a408-ed91964bddae'),('d3288b22-4ff8-4c91-a1fa-19143eb909e3','beauty spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'d1e717d0-e817-4a73-8f88-32a810dcc21c','71605e19-c7e6-4dad-89b3-400793cabec8'),('dc9e85f3-4451-4f43-86aa-9eedd0d9231e','clothes spring budget',101.7,100,'EUR','2023-01-01','2023-04-30',1,'c81913ba-8744-4f0d-af63-3e451411069b','111b8ed3-a45e-4a0c-a02f-f14d64318311'),('e44a3be2-a358-475c-a9f5-b8066f02e24f','clothes spring budget',83.1,100,'EUR','2023-01-01','2023-04-30',1,'a6a2e662-ffc6-44fd-807c-8a308688dc1d','111b8ed3-a45e-4a0c-a02f-f14d64318311'),('eaeed9c2-5573-47cf-a6c4-d670c90abf1c','clothes spring budget',0,100,'EUR','2023-01-01','2023-04-30',1,'d1e717d0-e817-4a73-8f88-32a810dcc21c','111b8ed3-a45e-4a0c-a02f-f14d64318311'),('f0f43b14-6179-49d3-94d3-8d875b008d81','beauty spring budget',0,200,'EUR','2023-01-01','2023-04-30',1,'3c50eb81-9aa5-462f-8cde-8460e1e331c9','71605e19-c7e6-4dad-89b3-400793cabec8'),('fe1885af-3a4e-4fe6-8a55-6e359a57b833','beauty spring budget',33.9,100,'EUR','2023-01-01','2023-04-30',1,'a6a2e662-ffc6-44fd-807c-8a308688dc1d','9275f7fd-06d2-49de-a408-ed91964bddae');
/*!40000 ALTER TABLE `budgets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `category_id` varchar(50) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`category_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES ('111b8ed3-a45e-4a0c-a02f-f14d64318311','clothes','Stuff you put on your back',1),('54f39350-9b89-4a48-aad6-e41db60bbefa','entertainment','Fun stuff',1),('71605e19-c7e6-4dad-89b3-400793cabec8','beauty','Face-ironing, nail-polyshing and hair-styling stuff',1),('9275f7fd-06d2-49de-a408-ed91964bddae','food','Stuff you eat',1),('94156b13-6e17-489f-ac0d-12217c03ccf5','doctor','Medicine against death stuff',1),('bf968dd9-be47-440d-bcc1-322a3575a25d','sports','Health and vanity stuff',1),('e75e0c17-2b7c-44df-b5d9-f93662c6593f','books','Stuff you read',1);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `money_accounts`
--

DROP TABLE IF EXISTS `money_accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `money_accounts` (
  `money_account_id` varchar(50) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `user_id` varchar(50) NOT NULL,
  `currency` varchar(10) DEFAULT NULL,
  `balance` float DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`money_account_id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `money_accounts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `money_account_currencies_cc` CHECK ((`currency` in (_utf8mb4'DIN',_utf8mb4'EUR')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `money_accounts`
--

LOCK TABLES `money_accounts` WRITE;
/*!40000 ALTER TABLE `money_accounts` DISABLE KEYS */;
INSERT INTO `money_accounts` VALUES ('00158b50-f645-416d-ba6c-a81bec378625','dara\'s account','c81913ba-8744-4f0d-af63-3e451411069b','DIN',31704.5,1),('3bd1f741-c238-4409-9149-0df0538371cb','zora\'s account','a6a2e662-ffc6-44fd-807c-8a308688dc1d','DIN',58906.5,1),('72721aae-f1e0-4f04-b07c-b1ce0c766bd7','maja\'s account','49d05b82-8e81-4508-9b61-9a8039b4db56','DIN',100000,1),('bcd867d6-57af-40f9-b939-6476d31760a7','zika\'s account','3c50eb81-9aa5-462f-8cde-8460e1e331c9','EUR',1000,1),('c8390ef8-f19c-4a83-996c-2249c31b1338','pera\'s account','1de62eb1-1b71-4862-9059-ff56cca0b491','EUR',1000,1),('ea29a8bf-0cd9-401a-8c3e-8171e2dcd07d','mika\'s account','2e352223-7400-4a9b-bb4f-6548916d18da','EUR',1000,1),('f0a432a1-c78a-47d4-b6ae-fa53103b5162','bora\'s account','d1e717d0-e817-4a73-8f88-32a810dcc21c','EUR',393.29,1);
/*!40000 ALTER TABLE `money_accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `role_id` varchar(50) NOT NULL,
  `role_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE KEY `role_type` (`role_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES ('039cbb0d-5339-416e-8f21-0ec5887a53c6','ADMIN'),('4a700cd5-c483-4309-8b63-45ff051c061b','USER');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `transaction_id` varchar(50) NOT NULL,
  `outbound` tinyint(1) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `currency` varchar(10) DEFAULT NULL,
  `transaction_time` datetime DEFAULT NULL,
  `user_id` varchar(50) NOT NULL,
  `vendor_id` varchar(50) NOT NULL,
  `is_valid` tinyint(1) DEFAULT NULL,
  `cash_payment` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `user_id` (`user_id`),
  KEY `vendor_id` (`vendor_id`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`vendor_id`) REFERENCES `vendors` (`vendor_id`),
  CONSTRAINT `transaction_currencies_cc` CHECK ((`currency` in (_utf8mb4'DIN',_utf8mb4'EUR')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES ('078030af-b7ff-4d6d-a2fd-1ef7c829ebfa',1,350,'DIN','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','7b828b15-b513-4159-a968-c362874a7176',1,0),('08fbf404-e9d8-4c43-8df9-13919ff8e6b7',1,7800,'DIN','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','4b70026c-fb13-45f7-a296-f28c9dd96d93',1,0),('0fc1cf8e-2b51-44ff-864d-1ebc17f6cdae',1,2100,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','586a49c1-73d8-4732-90e1-93745def541c',1,0),('1f3e7901-eee6-4d42-ae45-d4e2c95cff4b',1,7500,'DIN','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','627b28f4-cbf5-4159-b330-aa432e128a92',1,0),('23477b21-c9b8-4982-8768-825afe6e6478',1,16,'EUR','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','09244ce9-09e8-450a-9c7e-894e21c4607b',1,0),('23bcb1a5-ff41-40f3-a756-b45febd6cc54',1,1200,'DIN','2023-02-22 17:29:13','d1e717d0-e817-4a73-8f88-32a810dcc21c','e4fe5d06-5ef3-4e2c-b193-985dce6f1d61',1,0),('25a894e9-c32f-461d-9ea4-ba8ca19d1aa2',1,34,'EUR','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','7232e6a9-e9fe-4a2a-9577-64cd98aa1fb1',1,0),('31ff0c93-ce2d-4157-a0bb-83fed34532ff',1,21,'EUR','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','0979edfa-06e9-40a1-b705-36776f30c8fa',1,0),('3a1b0a3c-ddc2-440a-a19f-40f8b70667a7',1,4000,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','3d8943b3-d770-460e-9f07-d0ad3322b59e',1,0),('4888f7bd-4ffc-44af-9555-551d0545ce50',1,2100,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','586a49c1-73d8-4732-90e1-93745def541c',1,0),('4babbc36-0fd2-4cf0-bf26-211260491bd8',1,10000,'DIN','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','5f1088c4-c364-4e8e-b73a-91eec56755bf',1,0),('4dba8f0d-83cb-44b4-ac6b-a2032e11599b',1,1200,'DIN','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','5f1088c4-c364-4e8e-b73a-91eec56755bf',1,0),('531ed3e9-0012-4496-93c7-9c58970098b1',1,46,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','09244ce9-09e8-450a-9c7e-894e21c4607b',1,0),('56de4a37-076c-41f2-8d68-43b5c4491ad1',1,4330,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','5f1088c4-c364-4e8e-b73a-91eec56755bf',1,0),('6e67ccdd-28c0-42cf-952f-0a32be39d788',1,22,'EUR','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','66f44fd6-49dc-42b8-9116-36eae4bff1ab',1,0),('73af873c-94e3-49e4-bda9-6a6c059ca456',1,600,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','5f1088c4-c364-4e8e-b73a-91eec56755bf',1,0),('8458b8d3-0e98-4b6c-8a3d-f2a2a6d99423',1,3300,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','5784acd7-0a84-4ba4-9515-a97293e8cf1d',1,0),('8ab077b9-fa0a-4b96-9e81-842a4dd6e598',1,5000,'DIN','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','c8376076-e8b0-4bcc-a744-7b25d97c7335',1,0),('98a93edb-7a3d-4307-ba52-7798258530d3',1,121,'EUR','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','4b70026c-fb13-45f7-a296-f28c9dd96d93',1,0),('a2727ef5-a2a4-4134-a846-e7fabc058c8b',1,5005,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','586a49c1-73d8-4732-90e1-93745def541c',1,0),('a7fda00c-fb6a-4c96-949b-48e77c9ebad2',1,600,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','586a49c1-73d8-4732-90e1-93745def541c',1,0),('a85ad596-b405-4aae-b42f-7bca557f1641',1,1200,'DIN','2023-02-22 17:29:13','d1e717d0-e817-4a73-8f88-32a810dcc21c','db2a45ee-f42d-4157-8614-97d223848158',1,0),('aeeaa9e8-b2ab-497d-b1c6-f75ec7fda6d0',1,500,'DIN','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','66f44fd6-49dc-42b8-9116-36eae4bff1ab',1,0),('bf27ae80-4795-42e9-8f65-59fbc67b2c54',1,44,'EUR','2023-02-22 17:29:13','d1e717d0-e817-4a73-8f88-32a810dcc21c','09244ce9-09e8-450a-9c7e-894e21c4607b',1,0),('c8a9f9f3-741c-4132-bb55-993ff2faca3f',1,4916,'DIN','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','09244ce9-09e8-450a-9c7e-894e21c4607b',1,0),('d88ea206-0a06-449f-b42a-19691669094b',1,100,'EUR','2023-02-22 17:29:13','a6a2e662-ffc6-44fd-807c-8a308688dc1d','1d0ba3d7-0234-4295-9251-ba44759e8e99',1,0),('e479a6a0-49a3-4b19-aed1-067a822f2be7',1,34,'EUR','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','7232e6a9-e9fe-4a2a-9577-64cd98aa1fb1',1,0),('f217b44b-0381-46ae-9edf-7b0ec915efa8',1,5000,'DIN','2023-02-22 17:29:13','d1e717d0-e817-4a73-8f88-32a810dcc21c','d6f47c6b-e396-4dd1-bb85-a95605080dfe',1,0),('f927dde2-900d-4c48-a53a-0f64c9e3a2e1',1,4500,'DIN','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','627b28f4-cbf5-4159-b330-aa432e128a92',1,0),('f9d759dc-7d0c-4ff7-b3b2-0362cc861e72',1,5000,'DIN','2023-02-22 17:29:13','c81913ba-8744-4f0d-af63-3e451411069b','5f1088c4-c364-4e8e-b73a-91eec56755bf',1,0);
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_has_roles`
--

DROP TABLE IF EXISTS `user_has_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_has_roles` (
  `user_has_role_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `role_id` varchar(50) NOT NULL,
  PRIMARY KEY (`user_has_role_id`),
  KEY `user_id` (`user_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_has_roles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `user_has_roles_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_has_roles`
--

LOCK TABLES `user_has_roles` WRITE;
/*!40000 ALTER TABLE `user_has_roles` DISABLE KEYS */;
INSERT INTO `user_has_roles` VALUES ('110d7e15-013b-48c3-abd6-ac8a58b7bf5c','1de62eb1-1b71-4862-9059-ff56cca0b491','4a700cd5-c483-4309-8b63-45ff051c061b'),('17d3527b-3f07-48c3-a971-ffecd4adf015','3c50eb81-9aa5-462f-8cde-8460e1e331c9','4a700cd5-c483-4309-8b63-45ff051c061b'),('3e2fcff9-bc16-4c74-859c-85b6b28b9a06','c81913ba-8744-4f0d-af63-3e451411069b','4a700cd5-c483-4309-8b63-45ff051c061b'),('5d1c2670-392d-4079-b43a-e2c2b77e0900','49d05b82-8e81-4508-9b61-9a8039b4db56','039cbb0d-5339-416e-8f21-0ec5887a53c6'),('8472980e-075a-4f0c-8bc1-9d4301dddb2b','2e352223-7400-4a9b-bb4f-6548916d18da','039cbb0d-5339-416e-8f21-0ec5887a53c6'),('85732d89-f8f0-48d1-bab7-61c7e201be26','d1e717d0-e817-4a73-8f88-32a810dcc21c','4a700cd5-c483-4309-8b63-45ff051c061b'),('99059a82-8f0c-4441-b719-5d64c1d86e6c','a6a2e662-ffc6-44fd-807c-8a308688dc1d','4a700cd5-c483-4309-8b63-45ff051c061b');
/*!40000 ALTER TABLE `user_has_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('1de62eb1-1b71-4862-9059-ff56cca0b491','py001@itbc.rs','11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1',1),('2e352223-7400-4a9b-bb4f-6548916d18da','py111@itbc.com','11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1',1),('3c50eb81-9aa5-462f-8cde-8460e1e331c9','py005@itbc.rs','11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1',1),('49d05b82-8e81-4508-9b61-9a8039b4db56','admin@itbc.rs','3eb3fe66b31e3b4d10fa70b5cad49c7112294af6ae4e476a1c405155d45aa121',1),('a6a2e662-ffc6-44fd-807c-8a308688dc1d','py004@itbc.rs','11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1',1),('c81913ba-8744-4f0d-af63-3e451411069b','py003@itbc.rs','11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1',1),('d1e717d0-e817-4a73-8f88-32a810dcc21c','py002@itbc.rs','11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendors`
--

DROP TABLE IF EXISTS `vendors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendors` (
  `vendor_id` varchar(50) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `cash_only` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `category_id` varchar(50) NOT NULL,
  PRIMARY KEY (`vendor_id`),
  UNIQUE KEY `name` (`name`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `vendors_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendors`
--

LOCK TABLES `vendors` WRITE;
/*!40000 ALTER TABLE `vendors` DISABLE KEYS */;
INSERT INTO `vendors` VALUES ('09244ce9-09e8-450a-9c7e-894e21c4607b','ST Medicina','Bulevar Oslobodjenja 29',0,1,'94156b13-6e17-489f-ac0d-12217c03ccf5'),('0979edfa-06e9-40a1-b705-36776f30c8fa','Lucky hair','Sumadijska 52',0,1,'71605e19-c7e6-4dad-89b3-400793cabec8'),('1d0ba3d7-0234-4295-9251-ba44759e8e99','Jump Around','Gajeva 11',0,1,'bf968dd9-be47-440d-bcc1-322a3575a25d'),('3d8943b3-d770-460e-9f07-d0ad3322b59e','Zak','Bulevar Mihajla Pupina 22',0,1,'9275f7fd-06d2-49de-a408-ed91964bddae'),('40731f4f-3879-4d11-a724-9d2210244a81','Aluna','Strazilovska 60',0,1,'71605e19-c7e6-4dad-89b3-400793cabec8'),('4b70026c-fb13-45f7-a296-f28c9dd96d93','Dom Zdravlja Cvjetkovic','Balzakova 44',0,1,'94156b13-6e17-489f-ac0d-12217c03ccf5'),('5227b6ab-7587-4531-884b-a16674599939','24h Gym','Bulevar Oslobodjenja 71a',0,1,'bf968dd9-be47-440d-bcc1-322a3575a25d'),('5784acd7-0a84-4ba4-9515-a97293e8cf1d','Hamam','Pasiceva 7',0,1,'71605e19-c7e6-4dad-89b3-400793cabec8'),('586a49c1-73d8-4732-90e1-93745def541c','F&F','Big',0,1,'111b8ed3-a45e-4a0c-a02f-f14d64318311'),('5f1088c4-c364-4e8e-b73a-91eec56755bf','Vulkan','Promenada',0,1,'e75e0c17-2b7c-44df-b5d9-f93662c6593f'),('627b28f4-cbf5-4159-b330-aa432e128a92','Springfield','Modene 5',0,1,'111b8ed3-a45e-4a0c-a02f-f14d64318311'),('66f44fd6-49dc-42b8-9116-36eae4bff1ab','Maruko','Novosdskog Sajma 10',0,1,'54f39350-9b89-4a48-aad6-e41db60bbefa'),('6765aa02-42d5-4961-89ad-12d8ee5a0d5c','Fliperana','Promenada',0,1,'54f39350-9b89-4a48-aad6-e41db60bbefa'),('7232e6a9-e9fe-4a2a-9577-64cd98aa1fb1','World Class Fitness','Sekspirova 22',0,1,'bf968dd9-be47-440d-bcc1-322a3575a25d'),('7b828b15-b513-4159-a968-c362874a7176','Gyromania','Laze Teleckog 89',0,1,'9275f7fd-06d2-49de-a408-ed91964bddae'),('90afca95-c4c0-4c4d-a4a3-7cf3f972c933','Laguna','Zmaj Jovina 50',0,1,'e75e0c17-2b7c-44df-b5d9-f93662c6593f'),('9102d155-dab4-4454-b768-9e435a562a79','Beba Kids','Merkator',0,1,'111b8ed3-a45e-4a0c-a02f-f14d64318311'),('c8376076-e8b0-4bcc-a744-7b25d97c7335','Medigroup','Narodnog Fronta 29',0,1,'94156b13-6e17-489f-ac0d-12217c03ccf5'),('d6f47c6b-e396-4dd1-bb85-a95605080dfe','Cineplex','Promenada',0,1,'54f39350-9b89-4a48-aad6-e41db60bbefa'),('db2a45ee-f42d-4157-8614-97d223848158','Index Maja','Hadzi Ruvimova 67',0,1,'9275f7fd-06d2-49de-a408-ed91964bddae'),('e4fe5d06-5ef3-4e2c-b193-985dce6f1d61','Bulevar Books','Bulevar Mihajla Pupina 100',0,1,'e75e0c17-2b7c-44df-b5d9-f93662c6593f');
/*!40000 ALTER TABLE `vendors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 19:35:08
