from datetime import datetime


def is_valid_date_format(date):
    '''Ellenőrzi, hogy a dátum jó formátumban van e.'''
    if date is None:
        return "Dátum mező nem lehet üres."
    try:
        inspection_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return "A dátum nem érvényes formátum (pl.: 2024-05-01)."
    return None

def is_valid_time_format(time):
    '''Ellenőrzi, hogy az időpont/időbályegző jó formátumban van-e.'''
    if time is None:
        return "Időbélyegző mező nem lehet üres."
    try:
        # Az időpont formátuma: 'YYYY-MM-DD HH:MM:SS'
        inspection_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return "Az időpont nem érvényes formátum (pl.: 2024-05-01 14:30:00)."
    return None

def validate_mileage_is_a_number(mileage):
    if not mileage:
        return "A kilométer óra állás megadása kötelező."
    elif not mileage.isdigit() or len(mileage) > 7:
        return "A kilométer óra állás csak szám lehet, és legfeljebb 7 karakter hosszú."
    return None  # Ha nincs hiba, None-t ad vissza

def check_mileage_is_greater(mileage,licence_plate):
    '''Ellenőrzi, hogy a megadott mileage nagyobb e, mint az adatbázisban tárolt.'''
    return "dfdf"

def validate_licence_plate_is_right_form(licence_plate):
    '''Ellenőrzi, hogy a magyar rendszámoknak megfelelő e a formátum.'''
    if not licence_plate:
        return "A rendszám megadása kötelező."
    elif len(licence_plate) != 6 and len(licence_plate) != 7:
        return "A rendszám formátuma helytelen (példa: ABCD123, vagy ABC123)."
    elif len(licence_plate) == 7:
        if not licence_plate[:4].isalpha() or not licence_plate[4:].isdigit():
            return "A rendszám formátuma helytelen (példa: ABCD123, vagy ABC123)."
    elif len(licence_plate) == 6:
        if not licence_plate[:3].isalpha() or not licence_plate[3:].isdigit():
            return "A rendszám formátuma helytelen (példa: ABCD123, vagy ABC123)."
    #elif check_licence_plate_exists(licence_plate):
    #    return "A rendszám már létezik a rendszerben."
    return None