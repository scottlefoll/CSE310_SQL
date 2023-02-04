INSERT INTO customers (custFirstname, custLastname, custEmail, custPassword, custLevel, comments) 
    Values ('Tom', 'Stinson', 'tomstinson@gmail.com', 'Iamtired@n', 1, 'He buys a lot of Legos'),
    ('Jill', 'Hilliard', 'jilliard@aol.com', 'awert234', 3, 'Loves Hot Wheels'),
    ('Ryan', 'Phillips', 'ryanphill@outlook.com', '23434523', 3, 'Fisher Price for his kids'),
    ('Gary', 'Mitchell', 'g.mitchell@cloudnet.com', 'q2345;oiuhjag90', 3, 'Wants to special order some things.'),
    ('Mel', 'Gibson', 'melthegreat@gibson.com', 'd;opijs9', 1, 'He is hot on Nerf guns for his battles'),
    ('Fisher', 'Omara', 'romara@cbc.net', 'q2345;oiuhjag90', 3, 'Bought once - nasty customer.');

UPDATE customers SET custLevel = 1 WHERE custEmail = 'g.mitchell@cloudnet.com';

UPDATE toyStock SET stockDesc = REPLACE(stockDesc, "little ones", "children") WHERE stockBrand = 'Fisher Price';

SELECT toyStock.stockBrand, toyStock.stockModel, toyStock.stockDesc, toyType.typeName from toyStock  
  INNER JOIN toyType ON toyStock.typeID = toyType.typeID 
  WHERE toyType.typeName = "Disney"

DELETE FROM toyStock WHERE INSTR(stockModel, 'Starship') > 0 AND stockBrand = 'Lego';

UPDATE toyStock SET stockImage = CONCAT("/assets", stockImage), 
stockThumb = CONCAT("/assets", stockThumb);


**********************

DROP DATABASE IF EXISTS sql_module2;
SET SQL_MODE = NO_AUTO_VALUE_ON_ZERO;
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = '+00:00';
DROP DATABASE IF EXISTS sql_module2;
CREATE DATABASE sql_module2;
USE sql_module2;
--
-- Database: sql_module2
--
--
-- Table structure for table toyStock
--
DROP TABLE IF EXISTS toyStock;
CREATE TABLE toyStock (
  stockId int UNSIGNED NOT NULL,
  stockBrand varchar(30) NOT NULL,
  stockModel varchar(30) NOT NULL,
  stockDesc text NOT NULL,
  stockImage varchar(50) NOT NULL,
  stockThumb varchar(50) NOT NULL,
  stockCost decimal(10, 0) NOT NULL,
  stockQuantity smallint NOT NULL,
  stockHue varchar(20) NOT NULL,
  typeId int NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = latin1;

--
-- Dumping data for table toyStock
--
INSERT INTO toyStock (
    stockId,
    stockBrand,
    stockModel,
    stockDesc,
    stockImage,
    stockThumb,
    stockCost,
    stockQuantity,
    stockHue,
    typeId
  )
VALUES (
    1001,
    'Fisher Price' ,
    'Farm',
    'This is a great toy for the little ones. It comes with a tractor, a trailer, and a cow. The cow is a little loose but it is still a great toy.',
    '/images/farm.png',
    '/images/farm-small.png',
    29.95,
    41,
    'red',
    1
  ),
  (
    1002,
    'Fisher Price',
    'Playhouse',
    'The Fisher Price playhouse will engage your little ones for hours as they recreate life at home.',
    '/images/house.png',
    '/images/house-small.png',
    31.99,
    27,
    'white',
    1
  ),
  (
    1003,
    'Lego',
    'Starship 1',
    'Children become heroes in their own epic stories with this cool LEGO brick version of Luke Skywalkers X-wing Fighter (75301) from the classic Star Wars trilogy.',
    '/images/star.png',
    '/images/star-small.png',
    79.99,
    15,
    'white',
    3
  ),
  (
    1004,
    'Disney',
    'Jasmine',
    'Dreaming of a life beyond the walls of the palace in Agrabah, Jasmine finds herself in the adventure of a lifetime thanks to Aladdin and the Genie.
     With this Royal Shimmer Disney Princess doll, kids can imagine Jasmine flying in on a magical carpet.',
    '/images/jasmine.png',
    '/images/jasmine-small.png',
    19.99,
    30,
    'purple',
    2
  ),
  (
    1005,
    'Disney',
    'Ariel',
    'Disney Princess Royal Shimmer Ariel Doll, Fashion Doll with Skirt and Accessories, Toy for Kids Ages 3 and Up. 
     Free-spirited Ariel explores the world above the waves on her journey to fulfill her dreams in Disneys The Little Mermaid.',
    '/images/ariel.png',
    '/images/ariel-small.png',
    19.99,
    100,
    'green',
    2
  ),
  (
    1006,
    'Lego',
    'Starship 2',
    'Kids can role-play as the villains from the classic Star Wars trilogy with this cool LEGO brick version of the Imperial TIE Fighter (75300).',
    '/images/star2.png',
    '/images/star2-small.png',
    59.99,
    25,
    'black',
    3
  ),
  (
    1007,
    'Lego',
    'Yoda',
    'The great Jedi master from the Star Wars movies.',
    '/images/yoda.png',
    '/images/yoda-small.png',
    69.99,
    27,
    'tan',
    3
  ),
  (
    1008,
    'Lego',
    'Speed',
    'This buildable LEGO Speed Champions Nissan Skyline GT-R (R34) replica model (76917) has been inspired by the iconic car from the 2 Fast 2 Furious movie.',
    '/images/speed.png',
    '/images/speed-small.png',
    49.99,
    19,
    'silver',
    3
  ),
  (
    1009,
    'Ford Toys',
    'F150',
    'Rugged and fun adventure is calling! We’ve got the perfect ride-on for your truck-loving kid who has a need for speed! The blue Ford F-150 12-volt battery ride-on is the perfect toy to provide your kid with loads of fun during playtime. ',
    '/images/ford.jpg',
    '/images/ford-small.jpg',
    398.99,
    9,
    'blue',
    5
  ),
  (
    1010,
    'Hot Wheels',
    'Hot Wheels9',
    '9-Car Gift Pack (Styles May Vary) - Pack of 2.',
    '/images/hotwheels9.png',
    '/images/hotwheels9-small.png',
    9.99,
    31,
    'misc',
    4
  ),
  (
    1011,
    'Hot Wheels',
    'Hot Wheels Loop Track',
    'Its extreme action on a raised gradient track with angled turns, an outrageous loop, and a motorized boost that make this set a classic, over-the-top Hot Wheels experience!',
    '/images/hotwheels.png',
    '/images/hotwheels-small.png',
    75.95,
    21,
    'green',
    4
  ),
  (
    1012,
    'Lego',
    'Dinosaur',
    'This buildable LEGO Speed Champions Nissan Skyline GT-R (R34) replica model (76917) has been inspired by the iconic car from the 2 Fast 2 Furious movie.',
    '/images/dino.png',
    '/images/dino-small.png',
    19.99,
    19,
    'green',
     3
  ),
  (
    1013,
    'Marvel International',
    'Batmobile',
    'The Batmobile is a fictional car appearing in American comic books published by DC Comics, commonly as the main vehicle of the superhero Batman.',
    '/images/batmobile.png',
    '/images/batmobile-small.png',
    25.99,
    15,
    'black',
    6
  ),
  (
    1014,
    'Marvel International',
    'Batman',
    'Batman is a fictional superhero appearing in American comic books published by DC Comics, commonly known as the superhero Batman.',
    '/images/batman.png',
    '/images/batman-small.png',
    23.99,
    15,
    'black',
    6
  ),
  (
    1015,
    'Sweet Toys',
    'Baby Love',
    'Let your little one buckles up their baby doll and transport her all around the house My Sweet Love 13” Baby Doll with Carrier and Handle Play Set',
    '/images/baby-png',
    '/images/baby-small.png',
    19.99,
    21,
    'beige',
    7
  ),
    (
    1016,
    'Fisher Price',
    'Airport',
    'The Fisher Price airport will amaze all of the little ones in your home with imaginary play in the sky!',
    '/images/air.png',
    '/images/air-small.png',
    41.99,
    23,
    'green',
    1
  ),
    (
    1017,
    'Lego',
    'Starship 3',
    'Inspire youngsters and adults with this 75257 LEGO Star Wars Millennium Falcon model.',
    '/images/star3.png',
    '/images/star3-small.png',
    79.99,
    15,
    'white',
    3
  ),
    (
    1018,
    'Lego',
    'Starship 4',
    'Star Wars: The Empire Strikes Back fans can play out Imperial missions to defeat the Rebel Alliance with this LEGO brick-built TIE Bomber (75347) starfighter toy.',
    '/images/star4.png',
    '/images/star4-small.png',
    79.99,
    15,
    'white',
    3
  );
--
-- Indexes for table toyStock
--
ALTER TABLE toyStock
ADD PRIMARY KEY (stockId),
  ADD KEY typeId (typeId);
--
-- AUTO_INCREMENT for table 
--
ALTER TABLE toyStock
MODIFY stockId int NOT NULL AUTO_INCREMENT,
  AUTO_INCREMENT = 16;
--
-- Table structure for table toyType
--
DROP TABLE IF EXISTS toyType;
CREATE TABLE toyType (
  typeId int NOT NULL,
  typeName varchar(30) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
-- Dumping data for table toyType
--
INSERT INTO toyType (typeId, typeName)
VALUES (1, 'Playsets'),
  (2, 'Disney'),
  (3, 'Lego'),
  (4, 'Hot Wheels'),
  (5, 'Powered Rides'),
  (6, 'Superheroes'),
  (7, 'Dolls');
  
--
-- Indexes for table toyType
--
ALTER TABLE toyType
ADD PRIMARY KEY (typeId);
--
-- AUTO_INCREMENT for table toyType
--
ALTER TABLE toyType
MODIFY typeId int NOT NULL AUTO_INCREMENT,
  AUTO_INCREMENT = 7;
--
-- Constraints for table toyStock
--
ALTER TABLE toyStock
ADD CONSTRAINT toyStock_ibfk_1 FOREIGN KEY (typeId) REFERENCES toyType (typeId);
COMMIT;
--
-- Table structure for table clients
--
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
  custId int UNSIGNED NOT NULL,
  custFirstname varchar(15) NOT NULL,
  custLastname varchar(25) NOT NULL,
  custEmail varchar(40) NOT NULL,
  custPassword varchar(255) NOT NULL,
  custLevel enum('1','2','3') NOT NULL DEFAULT '1',
  comments text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Indexes for table customers
--
ALTER TABLE customers
  ADD PRIMARY KEY (custID);

-- AUTO_INCREMENT for table customers

ALTER TABLE customers
  MODIFY custID int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

