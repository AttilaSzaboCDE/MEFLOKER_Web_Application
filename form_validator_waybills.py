def validate_mileage_is_a_number(mileage):
    if not mileage:
        return "A kilométer óra állás megadása kötelező."
    elif not mileage.isdigit() or len(mileage) > 7:
        return "A kilométer óra állás csak szám lehet, és legfeljebb 7 karakter hosszú."
    return None  # Ha nincs hiba, None-t ad vissza
"""
def check_mileage_is_greater(opening_mileage, licence_plate):
    if licence_plate = 
   return None
"""
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