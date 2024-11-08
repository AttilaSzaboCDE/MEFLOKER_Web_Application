from flask import Blueprint, render_template, request, redirect, url_for, flash
import calendar as cal
from datetime import datetime
from models.datamodels import Car

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/')
def calendar():

    hungarian_days = ['Hétfő', 'Kedd', 'Szerda', 'Csütörtök', 'Péntek', 'Szombat', 'Vasárnap']
   
    # Alapértelmezett év és hónap az aktuális dátum
    year = request.args.get('year', datetime.now().year, type=int)
    month = request.args.get('month', datetime.now().month, type=int)

    # Naptár adatok lekérdezése az adott évre és hónapra
    month_days = cal.monthrange(year, month)[1]  # Az adott hónap napjainak száma
    days = [(day, hungarian_days[cal.weekday(year, month, day)]) for day in range(1, month_days + 1)]

    cars = Car.query.all()
    
    return render_template('calendar.html', cars=cars, year=year, month=month, days=days, month_names=cal.month_name)
