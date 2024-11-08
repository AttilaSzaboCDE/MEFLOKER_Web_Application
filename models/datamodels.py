from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Ticket(db.Model):
    __tablename__ = 'tickets'
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), primary_key=True)
    regio = db.Column(db.String(31), nullable=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.Date)

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    licence_plate = db.Column(db.String(7), unique=True, nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String, nullable=True)  # Tárolhatsz képeket fájlként
    fuel = db.Column(db.String(20), nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    technical_inspection_end_date = db.Column(db.DateTime)

class Waybill(db.Model):
    __tablename__ = 'waybills'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), nullable=True)
    opening_time = db.Column(db.DateTime, nullable=False)
    opening_location = db.Column(db.String(50), nullable=False)
    opening_mileage = db.Column(db.Integer, nullable=False)
    closeing_time = db.Column(db.DateTime, nullable=True)
    closeing_location = db.Column(db.String(50), nullable=True)
    closeing_mileage = db.Column(db.Integer, nullable=True)
    wb_time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False)
    status_time_stamp = db.Column(db.DateTime)

class IssueReport(db.Model):
    __tablename__ = 'issuereports'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    description = db.Column(db.Text, nullable=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)

class DriverLicense(db.Model):
    __tablename__ = 'drivers_licenses'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    number = db.Column(db.String(10), unique=True, nullable=False)
    end_of_validity = db.Column(db.Date, nullable=False)
    category_list = db.Column(db.String(50), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)