from peewee import *
import datetime


db = SqliteDatabase('estacionamento.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    user_name = CharField(unique=True)
    password = CharField()
    is_admin = BooleanField(default=False)
    is_active = BooleanField(default=True)
    created_on = DateTimeField(default=datetime.datetime.now)
    
    


class Car(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    manufacturer = CharField()
    created_on = DateTimeField(default=datetime.datetime.now)
    price_per_hour = FloatField()


class Color(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    hex = CharField()
    created_on = DateTimeField(default=datetime.datetime.now)


class Parking(BaseModel):
    id = IntegerField(primary_key=True)
    plate = CharField()
    car = ForeignKeyField(Car, backref='parkings')
    color = ForeignKeyField(Color, backref='parkings')
    is_it_parked = BooleanField(default=True)
    entry_date = DateTimeField(default=datetime.datetime.now)
    departure_date = DateTimeField(null=True)
    entry_user = ForeignKeyField(User, backref='entries')
    departure_user = ForeignKeyField(User, backref='departures', null=True)
    final_price = FloatField(null=True)


def create_tables():
    with db:
        db.create_tables([User, Car, Color, Parking])


##if __name__ == '__main__':
    ##create_tables()
    ##print("Tabelas criadas com sucesso.")
