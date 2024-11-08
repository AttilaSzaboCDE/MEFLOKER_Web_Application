from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime

issuereportings_bp = Blueprint('issuereportings', __name__)

# Variables:
saved_time = None

@issuereportings_bp.route('/', methods=['GET', 'POST'])
def issuereporting():
    if request.method == 'POST':
        global saved_time
        saved_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Itt kaphatod meg az űrlap adatait
        name = request.form['name']
        license_plate = request.form['license_plate']
        id_code = request.form['id_code']
        message = request.form['message']

        print("Név:", name)
        print("Rendszám:", license_plate)
        print("Személyazonosító kód:", id_code)
        print("Üzenet:", message)
        print("Az űrlap időpontja:", saved_time) 
        
    return render_template('issuereporting.html', saved_time=saved_time)