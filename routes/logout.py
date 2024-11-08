from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/', methods=['POST'])
def do_logout():
    
    return "logout"