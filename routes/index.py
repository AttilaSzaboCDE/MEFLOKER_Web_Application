import os
from flask import Blueprint, current_app, render_template, request, redirect, url_for, flash
from datetime import datetime
from models.datamodels import Car

index_bp = Blueprint('main', __name__)

@index_bp.route('/')
def index():
    cars = Car.query.all()
    image_folder_path = os.path.join(current_app.config['UPLOAD_FOLDER'])
    return render_template('index.html', cars=cars, image_folder_path=image_folder_path)