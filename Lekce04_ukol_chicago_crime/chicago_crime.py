import pandas
import psycopg2
from sqlalchemy import create_engine, inspect

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "m.rezakova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "1?4O!U=Nfx8ajQeH"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

inspector = inspect(engine)
print(inspector.get_table_names())
print(inspector.get_columns("crime"))


#Pomocí SQL dotazu si připrav tabulku o krádeži motorových vozidel (sloupec PRIMARY_DESCRIPTION by měl mít hodnotu "MOTOR VEHICLE THEFT").

motor_vehicle_theft = pandas.read_sql("SELECT * FROM crime WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT'", con=engine)
#print(motor_vehicle_theft)

automobile_theft = motor_vehicle_theft[motor_vehicle_theft["SECONDARY_DESCRIPTION"] == "AUTOMOBILE"]
#print(automobile_theft.head())
#print(automobile_theft.dtypes)

automobile_theft = automobile_theft[["DATE_OF_OCCURRENCE", "CASE#"]]
#print(automobile_theft.head())

automobile_theft["DATE_OF_OCCURRENCE_AKTUAL"] = pandas.to_datetime(automobile_theft["DATE_OF_OCCURRENCE"])
#print(automobile_theft.dtypes)
#print(automobile_theft.head())

automobile_theft["MONTH"] = automobile_theft["DATE_OF_OCCURRENCE_AKTUAL"].dt.month
#print(automobile_theft.head())
automobile_theft_top_month = automobile_theft.groupby("MONTH").count().sort_values("CASE#", ascending=False)
print(automobile_theft_top_month.head())
print("K nejvíce krádežím auta dochází v měsíci září.")

