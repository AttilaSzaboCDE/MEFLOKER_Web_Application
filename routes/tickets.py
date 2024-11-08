from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.datamodels import db, Ticket, Car
from datetime import datetime

tickets_bp = Blueprint('tickets', __name__)

regios = [
    "Bács-Kiskun vármegye",
    "Baranya vármegye",
    "Békés vármegye",
    "Borsod-Abaúj-Zemplén vármegye",
    "Csongrád vármegye",
    "Fejér vármegye",
    "Győr-Moson-Sopron vármegye",
    "Hajdú-Bihar vármegye",
    "Heves vármegye",
    "Jász-Nagykun-Szolnok vármegye",
    "Komárom-Esztergom vármegye",
    "Pest vármegye",
    "Somogy vármegye",
    "Szabolcs-Szatmár-Bereg vármegye",
    "Tolna vármegye",
    "Vas vármegye",
    "Veszprém vármegye",
    "Zala vármegye",
    "Országos"
]

@tickets_bp.route('/add', methods=['GET', 'POST'])
def add_ticket():
    if request.method == 'POST':
        car_id = request.form['car_id']
        regio = request.form['regio']
        end_date = request.form['end_date']

        # Autó ellenőrzése
        car = Car.query.filter_by(id=car_id).first()
        if not car:
            flash("Az autó nem található!", "danger")
            return render_template('add_ticket.html')

        # Dátum ellenőrzése
        if datetime.strptime(end_date, '%Y-%m-%d') <= datetime.utcnow():
            flash("A lejárati dátum nem lehet múltbeli!", "warning")
            return render_template('add_ticket.html')

        # Jegy hozzáadása
        new_ticket = Ticket(car_id=car_id, regio=regio, time_stamp=datetime.utcnow(), end_date=end_date)
        db.session.add(new_ticket)
        db.session.commit()

        flash("Jegy sikeresen hozzáadva!", "success")
        return redirect(url_for('tickets.display_tickets'))
    
    return render_template('add_ticket.html')

@tickets_bp.route('/')
def display_tickets():
    tickets = Ticket.query.all()
    return render_template('display_tickets.html', tickets=tickets)

@tickets_bp.route('/delete/<int:ticket_id>', methods=['POST'])
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    flash("Jegy sikeresen törölve!", "success")
    return redirect(url_for('tickets.display_tickets'))
