from routes.calendar import calendar_bp
from routes.cars import cars_bp
from routes.index import index_bp
from routes.issuereportings import issuereportings_bp
from routes.login import login_bp
from routes.logout import logout_bp
from routes.tickets import tickets_bp
from routes.waybills import waybills_bp

def init_routes(app):
    app.register_blueprint(calendar_bp, url_prefix='/calendar')
    app.register_blueprint(cars_bp, url_prefix='/cars')
    app.register_blueprint(index_bp, url_prefix="/")
    app.register_blueprint(issuereportings_bp, url_prefix="/issuereportings")
    app.register_blueprint(login_bp, url_prefix="/login")
    app.register_blueprint(logout_bp, url_prefix="/logout")
    app.register_blueprint(tickets_bp, url_prefix='/tickets')
    app.register_blueprint(waybills_bp, url_prefix="/waybill")