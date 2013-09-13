CREATE TABLE `lecture` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `title` varchar(128) NOT NULL,
	  `starttime` int(10) NOT NULL,
	  `location` varchar(128) DEFAULT NULL,
	  `speaker` varchar(128) DEFAULT NULL,
	  `publishtime` int(10) NOT NULL,
	  `link` varchar(512) NOT NULL,
	  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 
