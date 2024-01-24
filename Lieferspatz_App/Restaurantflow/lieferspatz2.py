import sqlite3 

connection = sqlite3.connect("lieferspatz2.db")
cursor = connection.cursor()
print("Database connected")

# (id, forname, lastname, address, zipCode, username, password)
client_accounts = [
(1, "Lisa", "Seibert", "Regenstraße 6", 40477, "lisaseibert", "123456"),
(2, "Max", "Mustermann", "Sonnenstraße 10", 40479, "maxmustermann", "123456"),
(3, "Anna", "Maier", "Regenbogenstraße 5", 40476, "annamaier", "123456"),
(4, "Tobias", "Jause", "Jacobistraße 22", 40478, "tobiasjause", "123456"),
(5, "Stefan", "Rahn", "Oststraße 3", 40475, "stefanrahn", "123456")
]

# (id, name, address, zipCode, details, deliveryRadius, openingTime, closingTime, userName, password)
restaurant_list = [
    (1, "Das Schnitzelhaus", "Sonnenstraße 10", 40477, "Deutsche Küche", "40477, 40476, 40478, 40475", "10:00", "22:00", "schnitzelhaus", "123456"),
    (2, "Das Apfelhaus", "Apfelstraße 5", 40478, "Cafe mit süßen Desserts nur aus Äpfeln", "40477, 40476, 40478, 40479", "9:00", "17:00", "apfelhaus", "123456"),
    (3, "Lupo", "Pizzastraße 8", 40476, "Italienische Pizzeria", "40477, 40476", "12:00", "23:00", "lupo", "123456"),
    (4, "Takumi", "Japanstraße 3", 40475, "Japanische Nudelsuppen", "40475", "12:00", "22:00", "takumi", "123456"),
    (5, "Eat Tokyo", "Sushistraße 11", 40477, "Sushi", "40477, 40478", "12:00", "22:00", "eattokyo", "123456"),
    (6, "Scaramangas", "Regenstraße 2", 40473, "Vietnamesische Küche", "40473, 40472, 40474", "13:00", "23:00", "scaramangas", "123456"),
    (7, "Wilma Wunder", "Wunderstraße 1", 40477, "Restaurant, Brunch und Cafe mit deutschen Spezialitäten", "40477, 40478, 40479", "10:00", "22:00", "wilma", "123456"),
    (8, "Frittenwerk", "Pommesstraße 12", 40478, "Pommes und Poutines", "40478, 40477", "11:00", "23:00", "frittenwerk", "123456"),
    (9, "Tandori Chicken", "Hagelstraße 14", 40479, "Indische Küche", "40479, 40478, 40477", "12:00", "22:00", "tandorichicken", "123456"),
    (10, "Falafel Fabrik", "Falafelstraße 15", 40480, "Libanesische Küche", "40480, 40479, 40478", "11:00", "23:00", "falafelfabrik", "123456"),
]

item_list = [
	(1, 1, "Wiener Schnitzel", 12.99, "Kalb", "Hauptspeise"),
	(2, 1, "Kräuterbaguette", 6.99, "Vegetarisch", "Vorspeise"),
	(3, 1, "Brownie", 7.99, "Vegetarisch", "Nachspeise"),
	(4, 1, "Krustenbraten", 15.99, "Schwein", "Hauptspeise"),
	(5, 1, "Gemischter Salat", 5.99, "Vegetarisch", "Vorspeise"),
    (6, 1, "Mozarella Sticks", 5.99, "Vegetarisch", "Vorspeise"),
    (7, 1, "Cola", 2.99, "Alkoholfrei", "Getränk"),
    (8, 1, "Fanta", 2.99, "Alkoholfrei", "Getränk"),
    (9, 1, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (10, 1, "Bier", 2.99, "Alkohol", "Getränk"),
    (11, 2, "Schokoapfelkuchen", 3.99, "Kuchen", "Nachspeise"),
	(12, 2, "Mandelapfelkuchen", 3.99, "Kuchen", "Nachspeise"),
	(13, 2, "Apple Crumble", 3.99, "Kuchen", "Nachspeise"),
	(14, 2, "Apfeltarte", 4.99, "Kuchen", "Nachspeise"),
	(15, 2, "Apfeltorte", 4.99, "Kuchen", "Nachspeise"),
    (16, 2, "Gedeckter Apfelkuchen", 4.99, "Kuchen", "Nachspeise"),
    (17, 2, "Kaffee", 2.99, "Alkoholfrei", "Getränk"),
    (18, 2, "Tee", 2.99, "Alkoholfrei", "Getränk"),
    (19, 2, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (20, 2, "Limonade", 2.99, "Alkoholfrei", "Getränk"),
    (21, 3, "Pizza Margerita", 7.99, "Vegetarisch", "Hauptspeise"),
	(22, 3, "Pizza Salami", 8.99, "Schwein", "Hauptspeise"),
	(23, 3, "Pizza Schinken", 8.99, "Schwein", "Hauptspeise"),
	(24, 3, "Pizza Tonno", 8.99, "Fisch", "Hauptspeise"),
	(25, 3, "Pizza Hawai", 9.99, "Schwein", "Hauptspeise"),
    (26, 3, "Pizzabrötchen mit Aioli", 3.99, "Vegetarisch", "Vorspeise"),
    (27, 3, "Cola", 2.99, "Alkoholfrei", "Getränk"),
    (28, 3, "Fanta", 2.99, "Alkoholfrei", "Getränk"),
    (29, 3, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (30, 3, "Bier", 2.99, "Alkohol", "Getränk"),
    (31, 4, "Shoyu Ramen", 11.99, "Schwein", "Hauptspeise"),
	(32, 4, "Tonkotsu Ramen", 11.99, "Schwein", "Hauptspeise"),
	(33, 4, "Shio Ramen", 11.99, "Schwein", "Hauptspeise"),
	(34, 4, "Miso Ramen", 11.99, "Schwein", "Hauptspeise"),
	(35, 4, "Takoyaki", 5.99, "Fisch", "Vorspeise"),
    (36, 4, "Veggie Miso Ramen", 10.99, "Vegetarisch", "Hauptspeise"),
    (37, 4, "Cola", 2.99, "Alkoholfrei", "Getränk"),
    (38, 4, "Fanta", 2.99, "Alkoholfrei", "Getränk"),
    (39, 4, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (40, 4, "Bier", 2.99, "Alkohol", "Getränk"),
    (41, 5, "Gurken Maki", 3.99, "Vegetarisch", "Hauptspeise"),
	(42, 5, "Avocado Maki", 3.99, "Vegetarisch", "Hauptspeise"),
	(43, 5, "Lachs Maki", 4.99, "Fisch", "Hauptspeise"),
	(44, 5, "Thunfisch Maki", 4.99, "Fisch", "Hauptspeise"),
	(45, 5, "Miso Suppe", 2.99, "Schwein", "Vorspeise"),
    (46, 5, "California Roll", 4.99, "Fisch", "Hauptspeise"),
    (47, 5, "Cola", 2.99, "Alkoholfrei", "Getränk"),
    (48, 5, "Fanta", 2.99, "Alkoholfrei", "Getränk"),
    (49, 5, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (50, 5, "Bier", 2.99, "Alkohol", "Getränk"),
    (51, 6, "Frühlingsrollen", 4.99, "Vegetarisch", "Vorspeise"),
	(52, 6, "Sommerollen", 4.99, "Vegetarisch", "Vorspeise"),
	(53, 6, "Pho Suppe", 11.99, "Fisch", "Hauptspeise"),
	(54, 6, "Erdnuss Curry", 10.99, "Vegetarisch", "Hauptspeise"),
	(55, 6, "Reisnudelsalat", 11.99, "Schwein", "Hauptspeise"),
    (56, 6, "Papayasalat", 5.99, "Fisch", "Vorspeise"),
    (57, 6, "Cola", 2.99, "Alkoholfrei", "Getränk"),
    (58, 6, "Fanta", 2.99, "Alkoholfrei", "Getränk"),
    (59, 6, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (60, 6, "Bier", 2.99, "Alkohol", "Getränk"),
    (61, 7, "Bruschetta", 5.99, "Vegetarisch", "Vorspeise"),
	(62, 7, "Tomatensuppe", 5.99, "Vegetarisch", "Vorspeise"),
	(63, 7, "Caesar Salad", 10.99, "Schwein", "Hauptspeise"),
	(64, 7, "Schnitzel mit Pommes", 12.99, "Schwein", "Hauptspeise"),
	(65, 7, "Flammkuchen mit Speck und Zwiebel", 12.99, "Schwein", "Hauptspeise"),
    (66, 7, "Käsespätzle", 11.99, "Vegetarisch", "Hauptspeise"),
    (67, 7, "Cola", 2.99, "Alkoholfrei", "Getränk"),
    (68, 7, "Fanta", 2.99, "Alkoholfrei", "Getränk"),
    (69, 7, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (70, 7, "Bier", 2.99, "Alkohol", "Getränk"),
    (71, 8, "Hausfritten", 3.99, "Vegetarisch", "Vorspeise"),
	(72, 8, "Avocado Fritten", 5.99, "Vegetarisch", "Hauptspeise"),
	(73, 8, "Knoblauch Fritten", 5.99, "Vegetarisch", "Hauptspeise"),
	(74, 8, "Currywurst mit Fritten", 9.99, "Schwein", "Hauptspeise"),
	(75, 8, "Käse Fritten", 7.99, "Vegetarisch", "Hauptspeise"),
    (76, 8, "Tex Mex Fritten", 7.99, "Schwein", "Hauptspeise"),
    (77, 8, "Cola", 2.99, "Alkoholfrei", "Getränk"),
    (78, 8, "Fanta", 2.99, "Alkoholfrei", "Getränk"),
    (79, 8, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (80, 8, "Bier", 2.99, "Alkohol", "Getränk"),
    (81, 9, "Samosa", 3.99, "Vegetarisch", "Vorspeise"),
	(82, 9, "Nan mit Knoblauch", 2.99, "Vegetarisch", "Vorspeise"),
	(83, 9, "Chicken Tikka", 12.99, "Hähnchen", "Hauptspeise"),
	(84, 9, "Chicken Mango", 12.99, "Hähnchen", "Hauptspeise"),
	(85, 9, "Gemüse Reis mit Yoghurt", 9.99, "Vegetarisch", "Hauptspeise"),
    (86, 9, "Butter Chicken", 11.99, "Hähnchen", "Hauptspeise"),
    (87, 9, "Cola", 2.99, "Alkoholfrei", "Getränk"),
    (88, 9, "Fanta", 2.99, "Alkoholfrei", "Getränk"),
    (89, 9, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (90, 9, "Bier", 2.99, "Alkohol", "Getränk"),
    (91, 10, "Spinat Taschen", 4.99, "Vegetarisch", "Vorspeise"),
	(92, 10, "Tabouleh", 4.99, "Vegetarisch", "Vorspeise"),
	(93, 10, "Falafel Teller mit Pommes", 12.99, "Vegetarisch", "Hauptspeise"),
	(94, 10, "Hähnchen Teller mit Pommes", 12.99, "Hähnchen", "Hauptspeise"),
	(95, 10, "Moussaka", 9.99, "Rind", "Hauptspeise"),
    (96, 10, "Gemischter Teller mit Pommes", 11.99, "Hähnchen und Rind", "Hauptspeise"),
    (97, 10, "Cola", 2.99, "Alkoholfrei", "Getränk"),
    (98, 10, "Fanta", 2.99, "Alkoholfrei", "Getränk"),
    (99, 10, "Wasser", 1.99, "Alkoholfrei", "Getränk"),
    (100, 10, "Bier", 2.99, "Alkohol", "Getränk"),
]

#(id, client_id, restaurant_id, orderDate, orderTime, status, comment(optional))
orders = [
    (1, 1, 1, "15.01.2024", "18:29", "abgeschlossen", "Schnitzel mit Pommes bitte"),
    (2, 1, 2, "02.01.2024", "20:12", "abgeschlossen", "Keine Sahne"),
    (3, 2, 3, "03.01.2024", "16:32", "abgeschlossen", "Pizza mit Oregano und Knoblauch"),
    (4, 2, 4, "10.01.2024", "17:45", "abgeschlossen", "Keine Pilze"),
    (5, 3, 5, "11.01.2024", "13:24", "abgeschlossen", ""),
    (6, 3, 6, "13.01.2024", "15:36", "abgeschlossen", ""),
    (7, 4, 3, "16.01.2024", "19:23", "abgeschlossen", ""),
    (8, 4, 7, "15.01.2024", "20:02", "abgeschlossen", ""),
    (9, 5, 8, "17.01.2024", "14:05", "abgeschlossen", ""),
    (10, 5, 10, "19.01.2024", "18:29", "abgeschlossen", ""),
]

#(id, order_id, item_id, quantity)
order_content = [
    (1, 1, 1, 1),
    (2, 1, 2, 1),
    (3, 1, 7, 1),
    (4, 2, 11, 2),
    (5, 2, 17, 2),
    (6, 3, 21, 1),
    (7, 3, 25, 1),
    (8, 3, 27, 2),
    (9, 4, 31, 1),
    (10, 5, 41, 1),
    (11, 5, 42, 2),
    (12, 5, 43, 2),
    (13, 5, 45, 1),
    (14, 6, 52, 1),
    (15, 6, 54, 1),
    (16, 7, 21, 3),
    (17, 8, 61, 1),
    (18, 8, 65, 1),
    (19, 8, 68, 1),
    (20, 9, 71, 1),
    (21, 9, 72, 1),
    (22, 9, 77, 2),
    (23, 10, 93, 1),
    (24, 10, 100, 1)
]

cursor.execute("create table if not exists client_accounts (id integer primary key autoincrement, forname text, lastname text, address text, zipCode integer, username text, password text)")
cursor.executemany("insert into client_accounts values (?, ?, ?, ?, ?, ?, ?)", client_accounts)
connection.commit()
print("The client data was successfully inserted")

cursor.execute("create table if not exists restaurants (id integer primary key autoincrement, name text, address text, zipCode integer, details text, deliveryRadius text, openingTime time, closingTime time, userName text, password text)")
cursor.executemany("insert into restaurants values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", restaurant_list)
connection.commit()
print("The restaurant data was successfully inserted")

cursor.execute("create table if not exists menu_items (id integer primary key autoincrement, restaurant_id integer, name text, price real, description text, category text, foreign key (restaurant_id) references restaurants (id))")
cursor.executemany("insert into menu_items values (?, ?, ?, ?, ?, ?)", item_list)
connection.commit()
print("The menu items were successfully inserted")

cursor.execute("create table if not exists orders (id integer primary key autoincrement, client_id integer, restaurant_id integer, orderDate text, orderTime text, status text, comment text, foreign key (client_id) references client_accounts (id), foreign key (restaurant_id) references restaurants(id))")
cursor.executemany("insert into orders values (?, ?, ?, ?, ?, ?, ?)", orders)
connection.commit()
print("The orders were successfully inserted")

cursor.execute("create table if not exists order_content (id integer primary key autoincrement, order_id integer, item_id integer, quantity integer, foreign key (order_id) references orders (id), foreign key(item_id) references menu_items(id))")
cursor.executemany("insert into order_content values (?, ?, ?, ?)", order_content)
connection.commit()
print("The order contents were successfully inserted")

connection.close()