from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session
from models.datamodels import db, Car
from datetime import datetime
from werkzeug.utils import secure_filename
import os
from form_validators import is_valid_date_format, validate_mileage_is_a_number, validate_licence_plate_is_right_form, is_valid_time_format


cars_bp = Blueprint('cars', __name__, url_prefix='/cars')

types = [
    "ferdehátú",
    "szedán",
    "kombi",
    "dobozos furgon",
    "platós furgon",
    "kisbusz",
    "busz",
    "SUV",
    "pick-up",
    "terepjáró",
    "kisteherautó",
    "nyerges vontató",
    "kisbusz"
]

fuels = [
    "benzin",
    "elektromos",
    "gáz",
    "gázolaj",
    "hidrogén"
]

statuses = [
    "aktív", "inaktív", "foglalható", "törölt"
]

# Engedélyezett fájlkiterjesztések (opcionális)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def validate_image(image):
    if not image:
        return "Kérjük, válasszon ki egy képet.", None
    # Ellenőrizzük, hogy a fájl neve tartalmaz-e kiterjesztést
    if '.' not in image.filename:
        return "A fájl neve nem tartalmaz kiterjesztést.", None
    # Ellenőrizzük, hogy a fájl kiterjesztése engedélyezett-e
    extension = image.filename.rsplit('.', 1)[1].lower()
    if extension not in ALLOWED_EXTENSIONS:
        return "Csak PNG, JPG, JPEG vagy GIF formátumú képeket tölthet fel.", None

    # Kép fájlnevének generálása
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{secure_filename(image.filename)}"
    upload_folder = current_app.config['UPLOAD_FOLDER']  # Az UPLOAD_FOLDER dinamikus elérése
    filepath = os.path.join(upload_folder, filename)
    
    # Kép mentése
    try:
        image.save(filepath)
        return None, filename
    except Exception as e:
        return f"Hiba történt a kép mentése közben: {e}", None


def check_licence_plate_exists(licence_plate):
    return db.session.query(Car).filter_by(licence_plate=licence_plate).first() is not None

def validate_brand(brand):
    if not brand:
        return "A márka megadása kötelező."
    elif len(brand) > 20:
        return "A márka neve túl hosszú. Legfeljebb 20 karakter lehet."
    return None

def validate_model(model):
    if not model:
        return "Az autó típusának megadása kötelező."
    elif len(model) > 30:
        return "Az autó típusa túl hosszú. Legfeljebb 30 karakter lehet."
    return None

def validate_type(type_):
    if not type_:
        return "Az autó kivitelének megadása kötelező."
    elif type_ not in types:
        return "Érvénytelen kivitel. Kérjük, válasszon a megadott opciók közül."
    return None

def validate_fuel(fuel):
    if not fuel:
        return "Az üzemanyag megadása kötelező."
    elif fuel not in fuels:
        return "Érvénytelen üzemanyag típus. Kérjük, válasszon a megadott opciók közül."
    return None


def validate_status(status):
    if not status:
        return "Az állapot megadása kötelező."
    elif status not in statuses:
        return "Érvénytelen állapot. Kérjük, válasszon a megadott opciók közül."
    return None

def validate_technical_inspection_end_date(date_str):
    if date_str is None:
        return "A műszaki lejárati dátum nem lehet üres."
    try:
        inspection_date = datetime.strptime(date_str, '%Y-%m-%d')
        if inspection_date <= datetime.now():
            return "A műszaki lejárati dátum a jövőben kell legyen."
    except ValueError:
        return "A műszaki lejárati dátum nem érvényes formátum (pl.: 2024-05-01)."
    return None


@cars_bp.route('/add', methods=['GET', 'POST'])
#@role_required('Admin', 'Manager')
#@permission_required('add_car')
def add_car():
    print("elindult")
    if request.method == 'POST':
        print("megvolt a post")
        # Form adatok lekérése
        licence_plate = request.form.get('licence_plate')
        brand = request.form.get('brand')
        model = request.form.get('model')
        type_ = request.form.get('type')
        fuel = request.form.get('fuel')
        mileage = request.form.get('mileage')
        technical_inspection_end_date = request.form.get('technical_inspection_end_date')
        status = request.form.get('status')
        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #request.form.get('time_stamp')
        image_file = request.files.get('image')  # Képfájl kivétele
        
        # Form validáció
        errors = []
        for validator, field_value in [
            (validate_licence_plate_is_right_form, licence_plate),
            (check_licence_plate_exists, licence_plate),
            (validate_brand, brand),
            (validate_model, model),
            (validate_type, type_),
            (validate_fuel, fuel),
            (validate_mileage_is_a_number, mileage),
            (validate_technical_inspection_end_date, technical_inspection_end_date),
            (validate_status, status),
            (is_valid_time_format, time_stamp)
        ]:
            error = validator(field_value)
            if error:
                errors.append(error)
        
        print("request.files tartalma:", request.files)
        # Kép validálása
        image_error, image_path = validate_image(image_file)
        if image_error:
            errors.append(image_error)
        print("validálás lefutott")

        # Hibák kiírása képernyőre
        if errors:
            flash(errors, "warning")
            print("error kiment")
            return render_template('add_car.html', 
                                   types=types, 
                                   fuels=fuels, 
                                   statuses=statuses, 
                                   datetime=datetime,
                                   licence_plate=licence_plate,
                                   brand=brand,
                                   model=model,
                                   type_=type_,
                                   fuel=fuel,
                                   mileage=mileage,
                                   technical_inspection_end_date=technical_inspection_end_date,
                                   status=status
                                  )

        # Új autó objektum létrehozása
        new_car = Car(
            licence_plate=licence_plate,
            brand=brand,
            model=model,
            type=type_,
            fuel=fuel,
            mileage=mileage,
            technical_inspection_end_date=datetime.strptime(technical_inspection_end_date, '%Y-%m-%d'),
            status=status,
            #time_stamp=time_stamp,
            image=image_path
        )

        # Adatbázisba tétel
        try:
            db.session.add(new_car)
            db.session.commit()
            flash("Autó sikeresen hozzáadva a rendszerhez!","success")
            print("Sikeres betétel az adatbázisba")
            return redirect(url_for('cars.add_car'))
        except Exception as e:
            db.session.rollback()
            print(f"Hiba: {e}")  # Nyomtatja a hibát a konzolra
            print("Hiba adatbázisba tételnél")
            flash("Hiba adatbázisba tételnél", "danger")
            #flash({"type": "danger", "message": "Hiba történt az autó mentése közben. Próbálja újra!"}, "danger")
            return render_template('add_car.html', types=types, fuels=fuels, statuses=statuses, datetime=datetime)

    # GET kérés esetén az űrlap renderelése
    return render_template('add_car.html', types=types, fuels=fuels, statuses=statuses, datetime=datetime)

@cars_bp.route('/')
def display_cars():
    cars = Car.query.all()
    image_folder_path = os.path.join(current_app.config['UPLOAD_FOLDER'])
    return render_template('display_cars.html', cars=cars, image_folder_path=image_folder_path)

@cars_bp.route('/edit/<int:car_id>', methods=['GET', 'POST'])
def edit_car(car_id): #nincs kész. nincs tesztelve
    car = Car.query.get_or_404(car_id)
    
    if request.method == 'POST':
        # Form adatok frissítése
        car.brand = request.form['brand']
        car.model = request.form['model']
        car.type = request.form['type']
        car.fuel = request.form['fuel']
        car.mileage = request.form['mileage']
        car.status = request.form['status']
        car.technical_inspection_end_date = request.form['technical_inspection_end_date']
        
        db.session.commit()
        flash("Autó sikeresen frissítve!", "success")
        return redirect(url_for('cars.display_cars'))
    
    return render_template('edit_car.html', car=car)

@cars_bp.route('/remove/<int:car_id>', methods=['POST'])
def remove_car(car_id): #nincs kész. nincs tesztelve
    car = Car.query.get_or_404(car_id)
    car.status = 'removed'
    db.session.commit()
    #flash("Autó eltávolítva!", "danger")
    return redirect(url_for('cars.display_cars'))

@cars_bp.route('/car/<car_licence_plate>')
def display_car(car_licence_plate):
    car = Car.query.filter_by(licence_plate=car_licence_plate).first_or_404()
    return render_template('display_car.html', car=car)