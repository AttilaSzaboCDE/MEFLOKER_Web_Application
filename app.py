from flask import Flask, flash, jsonify, render_template, request, redirect, url_for
from datetime import datetime
#import models.datamodels as datamodels

from models.datamodels import db
from routes import init_routes
import os

app = Flask(__name__, static_folder='static/Assets')
app.secret_key = 'valami_titkos_kulcs'  # Titkos kulcs beállítása

# Ideiglene SQLite kapcsolat
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'titok'

db.init_app(app) # SQLAlchemy összekapcsolása a Flask alkalmazással

init_routes(app) # Routes inicializálása

# Feltöltött képek mentési mappája
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static/Assets/uploads')


#@app.route('/')
#def login():
#    return render_template('login.html')
#

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Az adatbázis létrehozása, ha még nincs
    app.run(debug=True)
