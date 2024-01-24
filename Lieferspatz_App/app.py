import sqlite3
import random
from flask import Flask, session, render_template, request, g, redirect, url_for
from datetime import datetime, time

app = Flask(__name__)
app.secret_key = "123456"

#connecting the sqlite3 database to the application
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('lieferspatz2.db')
    return db
                              

#terminating our database connection once we're done using it
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

        
#filtering the restaurants for zipCode and openingTimes 
def restaurant_list():
    user_zip_code = session["user"][4]
    current_time = datetime.now().time()

    cursor = get_db().cursor()
    cursor.execute("select id, name, details, deliveryRadius, openingTime, closingTime from restaurants")
    all_data = cursor.fetchall()

    filtered_restaurants = []

    for restaurant in all_data: 
        delivery_radius_zip_codes = list(map(int, restaurant[3].split(', ')))
        opening_time_str = restaurant[4]
        closing_time_str = restaurant[5]
        opening_time = datetime.strptime(opening_time_str, "%H:%M").time()
        closing_time = datetime.strptime(closing_time_str, "%H:%M").time()
        if int(user_zip_code) in delivery_radius_zip_codes and opening_time <= current_time <= closing_time:
            filtered_restaurants.append((restaurant[0], restaurant[1], restaurant[2]))
    return filtered_restaurants

def get_menu_items(restaurant_id):
    cursor = get_db().cursor()
    cursor.execute("select * from menu_items where restaurant_id=?", (restaurant_id,))
    menu_items = cursor.fetchall()
    return menu_items

def get_restaurant_name(restaurant_id):
    cursor = get_db().cursor()
    cursor.execute("select name from restaurants where id=?", (restaurant_id,))
    restaurant = cursor.fetchone()
    restaurant_name = restaurant[0]
    return restaurant_name if restaurant else None

@app.route("/start")
def index(): 
	return render_template("homepage.html")

@app.route("/homepage", methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		if request.form.get('registerClientBtn') == "Als Kunde registrieren":
			return redirect(url_for("create_client_account"))
		elif request.form.get('loginClientBtn') == "Als Kunde anmelden":
			return redirect(url_for("login_client"))
		elif request.form.get('registerRestaurantBtn') == "Als Restaurant registrieren":
			return redirect(url_for("create_restaurant_account"))
		elif request.form.get('loginRestaurantBtn') == "Als Restaurant anmelden":
			return redirect(url_for("login_restaurant"))
	else: 
		return redirect(url_for("home"))
		

@app.route("/registerClient", methods=["POST", "GET"])
def create_client_account():
	if request.method == "POST":
		connection = sqlite3.connect('lieferspatz2.db')
		cursor = connection.cursor()

		cursor.execute("create table if not exists client_accounts (id integer primary key autoincrement, forname text, lastname text, address text, zipCode text, username text, password text)")
		first_name = request.form['firstName']
		last_name = request.form['lastName']
		address = request.form['address']
		zip_Code = request.form['zipCode']
		username = request.form['username']
		password = request.form['password']

		cursor.execute("insert into client_accounts (forname, lastname, address, zipCode, username, password) values (?,?,?,?,?,?)", (first_name, last_name, address, zip_Code, username, password))

		connection.commit()
		connection.close()

		return redirect(url_for("login_client"))
	else:
		return render_template("registerClient.html")
	
@app.route("/loginClient", methods=["POST", "GET"])
def login_client():
	if request.method == "POST":
		session.permanent = True
		connection = sqlite3.connect('lieferspatz2.db')
		cursor = connection.cursor()

		username = request.form['username']
		password = request.form['password']

		cursor.execute("select * from client_accounts where username == ? and password == ?", (username,  password))
		result = cursor.fetchone()
		connection.commit()
		connection.close()

		if result:
			session["user"] = result
			return redirect(url_for("restaurants"))
		else:
			return render_template("loginClient.html")	
		
	else:
		return render_template("loginClient.html")	


@app.route("/registerRestaurant", methods=["POST", "GET"])
def create_restaurant_account():
	if request.method == 'POST':
		connection = sqlite3.connect('lieferspatz2.db')
		cursor = connection.cursor()

		cursor.execute("create table if not exists restaurants (id integer primary key autoincrement, name text, address text, zipCode text, details text, deliveryRadius text, openingTime text, closingTime text, userName text, password text)")
		restaurant_name = request.form['restaurantName']
		address = request.form['address']
		zip_Code = request.form['zipCode']
		deliveryRadius = request.form['servedArea']
		openingTime = request.form['openFrom']
		closingTime = request.form['openUntil']  
		details = request.form['description']
		username = request.form['username']
		password = request.form['password']

		cursor.execute("insert into restaurants (name, address, zipCode, details, deliveryRadius, openingTime, closingTime, userName, password) values (?,?,?,?,?,?,?,?,?)", (restaurant_name, address, zip_Code, details, deliveryRadius, openingTime, closingTime, username, password))

		connection.commit()
		connection.close()

		return redirect(url_for("login_restaurant"))
	else:
		return render_template("registerRestaurant.html")

@app.route("/loginRestaurant", methods=["POST", "GET"])
def login_restaurant():
	if request.method == 'POST':
		session.permanent = True
		connection = sqlite3.connect('lieferspatz2.db')
		cursor = connection.cursor()

		username = request.form['username']
		password = request.form['password']

		cursor.execute("select * from restaurants where userName == ? and password == ?", (username, password))
		result = cursor.fetchone() 
		connection.commit()
		connection.close()

		if result:
			session["user"] = result
			return redirect(url_for("login_restaurant"))  #Link zur Restaurant-Übersicht einfügen
		else:
			return render_template("loginRestaurant.html")
	else:
		return render_template("loginRestaurant.html")

@app.route("/restaurants")
def restaurants():
    filtered_restaurants = restaurant_list()
    return render_template("restaurants.html", restaurant_data = filtered_restaurants)

@app.route("/menu/<int:restaurant_id>")
def menu(restaurant_id):
    menu_items = get_menu_items(restaurant_id)
    restaurant_name = get_restaurant_name(restaurant_id)
    return render_template("menu.html", menu_items=menu_items, restaurant_name=restaurant_name)

#die nachfolgende Methode funktioniert noch nicht, also bitte komplett ignorieren!!! Ich musste sie einbauen, weil sonst eine Fehlermeldung im Front-End entsteht
@app.route("/add_to_cart", methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        restaurant_id = request.form.get('restaurant_id')
        menu_items = get_menu_items(restaurant_id)
        client_id = 1          #client id aus der Session einsetzen!!!

        cursor = get_db().cursor()
        current_datetime = datetime.now()
        order_date_str = current_datetime.strftime("%d.%m.%Y")
        order_time_str = current_datetime.strftime("%H:%M")
        cursor.execute("insert into orders (client_id, orderDate, orderTime) values (?, ?, ?)", (client_id, order_date_str, order_time_str))
        order_id = cursor.lastrowid

        '''for item in menu_items:
            item_id = request.form.get('item_id{{ item[0] }}')
            quantity_key = 'quantity{{ item[0] }}' + str(item[0])
            quantity = int(request.form.get(quantity_key, 0))

            if quantity > 0:
                cursor.execute("insert into order_content (order_id, item_id, quantity) values (?,?,?)", (order_id, item_id, quantity))'''
        get_db().commit 
        cursor.close()
        return redirect('/')
	
if __name__ == '__main__':
	app.run(debug=True)

