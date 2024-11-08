from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime

login_bp = Blueprint('login', __name__)

@login_bp.route('/')
def do_login():
    return render_template('login.html')
    