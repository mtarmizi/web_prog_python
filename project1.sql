-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               5.7.24 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping data for table project1.admin: ~2 rows (approximately)
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` (`username`, `password`) VALUES
	('admin1234', 'admin1234'),
	('mizi1234', 'mizi1234');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;

-- Dumping data for table project1.artist: ~8 rows (approximately)
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
INSERT INTO `artist` (`artist_id`, `artist_name`, `artist_style`, `birthplace`, `dob`, `age`) VALUES
	('artist001', 'Eddie Putera', 'Craftor', 'Kedah', '1968-06-05', 53),
	('artist002', 'Nor Tijan Firdaus', 'Craftor', 'Selangor', '1986-02-11', 35),
	('artist003', 'Anniketyni Madian', 'Sculptor', 'Sarawak', '1986-12-08', 34),
	('artist004', 'Yusuf Ghani', 'Painter', 'Johor', '1950-05-10', 71),
	('artist005', 'Khalil Ibrahim', 'Painter', 'Kelantan', '1934-04-18', 87),
	('artist006', 'Shaq Koyok', 'Painter', 'Selangor', '1985-03-05', 36),
	('artist007', 'Raja Shahriman', 'Sculptor', 'Perak', '1967-11-17', 53),
	('artist008', 'Kok Yew Puah', 'Painter', 'Selangor', '1947-05-06', 74),
	('artist009', 'Ibrahim Hussein', 'Painter', 'Kedah', '1936-03-13', 85),
	('artist123', 'Muhamad Tarmizi', 'Painter', 'Kuala Lumpur', '1992-07-16', 28);
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;

-- Dumping data for table project1.artwork: ~6 rows (approximately)
/*!40000 ALTER TABLE `artwork` DISABLE KEYS */;
INSERT INTO `artwork` (`artwork_id`, `title`, `artwork_type`, `year`, `artist_id`, `gallery_id`, `picture_name`) VALUES
	('artwork001', 'Miniature Diorama', 'Miniature', 2017, 'artist001', 'gallery02', 'artwork001.jpg'),
	('artwork003', 'Garuda', 'Acrylic on Canvas', 1970, 'artist009', 'gallery01', 'artwork003.jpg'),
	('artwork005', 'Gerak Tempur 11', 'Metal', 1999, 'artist007', 'gallery04', 'artwork005.jpg'),
	('artwork007', 'My Father & The Astronaut', 'Acrylic on Canvas', 1970, 'artist009', 'gallery05', 'artwork007.jpg'),
	('artwork009', 'Temple Figures', 'Acrylic & charcoal on paper', 1997, 'artist008', 'gallery03', 'artwork009.jpg'),
	('artwork010', 'Bandau Nulang', 'Mixed of Hardwood', 2017, 'artist003', 'gallery01', 'artwork010.jpg'),
	('artwork123', 'Tarmizi', 'Oil on Canvas', 2000, 'artist123', 'gallery04', 'artwork123.jpg');
/*!40000 ALTER TABLE `artwork` ENABLE KEYS */;

-- Dumping data for table project1.gallery: ~5 rows (approximately)
/*!40000 ALTER TABLE `gallery` DISABLE KEYS */;
INSERT INTO `gallery` (`gallery_id`, `gallery_name`, `address`, `contact`) VALUES
	('gallery01', 'National Art Gallery', 'Jalan Temerloh, Kuala Lumpur', '03-4025 7000'),
	('gallery02', 'TMS Art Gallery', 'Jalan Tiara Kemensah 3, Ampang Jaya, Selangor ', '0134567897'),
	('gallery03', 'Johor Art Gallery', 'Jalan Petrie, Kampung Baru, Johor', '07-226 3266'),
	('gallery04', 'UITM Museum & Art Gallery', 'UITM Shah Alam, Selangor', '03-5516 4502'),
	('gallery05', 'Islamic Art Museum', 'Jalan Lembah, Tasik Perdana, Kuala Lumpur', '03-2092 7070');
/*!40000 ALTER TABLE `gallery` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
