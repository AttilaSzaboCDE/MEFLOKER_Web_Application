from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from models.datamodels import db, Waybill
from form_validator_waybills import validate_mileage_is_a_number, validate_licence_plate_is_right_form

waybills_bp = Blueprint('waybills', __name__)

def check_licence_plate_exists(licence_plate):
    return db.session.query(Waybill).filter_by(licence_plate=licence_plate).first() is not None
"""
def check_mileage_is_greater(opening_mileage, licence_plate):
   licence_plate = db.session.get(licence_plate)
   opening_mileage = db.session.
   return licence_plate, opening_mileage
"""
@waybills_bp.route('/', methods=['GET','POST'])
def waybill():
   licence_plate = request.form.get('licence_plate')
   opening_mileage = request.form.get('opening_mileage')
   opening_place = request.form.get('opening_place')
   closeing_mileage = request.form.get('closeing_mileage')
   closeing_location = request.form.get('closeing_location')
   
   if request.method == 'POST':
      errors = []
      for validator, field_value in [
         (validate_licence_plate_is_right_form),
         (validate_mileage_is_a_number),
      ]:
         error = validator(field_value)
         if error:
            errors.append(error)
                
      # Hibák kiírása képernyőre
      if errors:
         flash(errors, "warning")
         print("error kiment")
         return render_template('add_car.html',
                                 licence_plate=licence_plate,
                                 opening_mileage=opening_mileage,
                                 opening_place=opening_place,
                                 closeing_mileage=closeing_mileage,
                                 closeing_location=closeing_location
                                 )

      # Új menetlevél objektum létrehozása
      new_waybill = Waybill(
         licence_plate=licence_plate,
         opening_mileage=opening_mileage,
         opening_place=opening_place,
         closeing_mileage=closeing_mileage,
         closeing_location=closeing_location
      ) 
      # Adatbázisba tétel
      try:
         db.session.add(new_waybill)
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
   return render_template('waybill.html')
 

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')