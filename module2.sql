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

