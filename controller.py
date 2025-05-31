from model import db,User, Car, Color, Parking
from datetime import datetime
from peewee import DoesNotExist
from utils import *
from peewee import *
import requests

import json

class Controller:
    # ----------------------------
    # USER CONTROLLER
    # ----------------------------
    def create_user(name, user_name, password, is_admin=False, is_active=True):
        return User.create(
            name=name,
            user_name=user_name,
            password=password,
            is_admin=is_admin,
            is_active=is_active,
        )

    def get_all_users():
        return list(User.select().dicts())

    def update_user(user_id, **kwargs):
        query = User.update(**kwargs).where(User.id == user_id)
        return query.execute()

    def delete_user(user_id):
        return User.delete().where(User.id == user_id).execute()

    def login_user(user_name, password):   

        active = User.select().where(User.is_active == True)
        try:
            user = active.where(
                (User.user_name == user_name) &
                (User.password == password)
            ).first()
        except User.DoesNotExist:
            user = None

        return user

        

    # ----------------------------
    # CAR CONTROLLER
    # ----------------------------

    def create_car(name, manufacturer, price_per_hour):
        return Car.create(
            name=name,
            manufacturer=manufacturer,
            price_per_hour=price_per_hour
        )

    def get_all_cars():
        return list(Car.select().dicts())

    def update_car(car_id, **kwargs):
        return Car.update(**kwargs).where(Car.id == car_id).execute()

    def delete_car(car_id):
        return Car.delete().where(Car.id == car_id).execute()

    # ----------------------------
    # COLOR CONTROLLER
    # ----------------------------

    def create_color(name, hex_code):
        return Color.create(name=name, hex=hex_code)

    def get_all_colors():
        return list(Color.select().dicts())

    def update_color(color_id, **kwargs):
        return Color.update(**kwargs).where(Color.id == color_id).execute()

    def delete_color(color_id):
        return Color.delete().where(Color.id == color_id).execute()

    # ----------------------------
    # PARKING CONTROLLER
    # ----------------------------

    def register_parking(plate, car_id, color_id, entry_user_id):
        return Parking.create(
            plate=plate,
            car=car_id,
            color=color_id,
            entry_user=entry_user_id
        )

    def get_all_parkings():
        return list(Parking.select().dicts())

    def finish_parking(parking_id, departure_user_id, final_price):
        try:
            parking = Parking.get_by_id(parking_id)
            parking.departure_date = datetime.datetime.now()
            parking.departure_user = departure_user_id
            parking.final_price = final_price
            parking.is_it_parked = False
            parking.save()
            return True
        except DoesNotExist:
            return False

    def delete_parking(parking_id):
        return Parking.delete().where(Parking.id == parking_id).execute()
    
    

    def export_to_json(filename="backup_estacionamento.json"):
        data = {
            "users": [dict(u) for u in User.select().dicts()],
            "cars": [dict(c) for c in Car.select().dicts()],
            "colors": [dict(c) for c in Color.select().dicts()],
            "parkings": [dict(p) for p in Parking.select().dicts()],
        }

        
        for table in data.values():
            for row in table:
                for key, value in row.items():
                    if isinstance(value, datetime):
                        row[key] = value.isoformat()

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"Exportação concluída para {filename}")

    


    def import_from_json(filename="backup_estacionamento.json"):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for user in data["users"]:
            user["created_on"] = parse_datetime(user.get("created_on"))

        for car in data["cars"]:
            car["created_on"] = parse_datetime(car.get("created_on"))

        for color in data["colors"]:
            color["created_on"] = parse_datetime(color.get("created_on"))

        for park in data["parkings"]:
            park["entry_date"] = parse_datetime(park.get("entry_date"))
            park["departure_date"] = parse_datetime(park.get("departure_date"))
        
        
        
        with db.atomic():
            User.insert_many(data["users"]).on_conflict_replace().execute()
            Car.insert_many(data["cars"]).on_conflict_replace().execute()
            Color.insert_many(data["colors"]).on_conflict_replace().execute()
            Parking.insert_many(data["parkings"]).on_conflict_replace().execute()

        print("Importação do JSON concluída com sucesso.")

    def import_from_url(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()

            for user in data["users"]:
                user["created_on"] = parse_datetime(user.get("created_on"))

            for car in data["cars"]:
                car["created_on"] = parse_datetime(car.get("created_on"))

            for color in data["colors"]:
                color["created_on"] = parse_datetime(color.get("created_on"))
                
            for park in data["parkings"]:
                park["entry_date"] = parse_datetime(park.get("entry_date"))
                park["departure_date"] = parse_datetime(park.get("departure_date"))
        
            with db.atomic():
                User.insert_many(data["users"]).on_conflict_replace().execute()
                Car.insert_many(data["cars"]).on_conflict_replace().execute()
                Color.insert_many(data["colors"]).on_conflict_replace().execute()
                Parking.insert_many(data["parkings"]).on_conflict_replace().execute()

            print("Importação via URL concluída com sucesso.")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar o arquivo JSON: {e}")
        except KeyError as e:
            print(f"Erro na estrutura do JSON: chave ausente {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
