import pandas
import psycopg2
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt
import numpy

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "m.rezakova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "1?4O!U=Nfx8ajQeH"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

inspector = inspect(engine)
print(inspector.get_table_names())
print(inspector.get_columns("uzivatele-m.rezakova"))


#Pomocí SQL dotazu do databáze si připrav dvě pandas tabulky:
#tabulka smrk bude obsahovat řádky, které mají v sloupci dd_txt hodnotu "Smrk, jedle, douglaska"

smrk = pandas.read_sql("SELECT * from dreviny WHERE dd_txt = 'Smrk, jedle, douglaska'", con=engine)
#print(smrk)
#print(smrk.dtypes)

smrk = smrk.set_index("rok")
#print(smrk.head())
smrk = smrk.sort_index()
#print(smrk.head())

ax = smrk.plot(kind="bar", y="hodnota")
plt.show()

#tabulka nahodila_tezba bude obsahovat řádky, které mají v sloupci druhtez_txt hodnotu "Nahodilá těžba dřeva"
#Vytvoř graf, který ukáže vývoj objemu těžby pro tabulku smrk. Pozor, řádky nemusí být seřazené podle roku.

nahodila_tezba = pandas.read_sql("SELECT * from dreviny WHERE druhtez_txt = 'Nahodilá těžba dřeva'", con=engine)
print(nahodila_tezba.head(10))

nahodila_tezba_pivot = pandas.pivot_table(nahodila_tezba, values="hodnota", index="rok", columns="prictez_txt", aggfunc=numpy.sum)
nahodila_tezba_pivot.plot(kind="bar", title="Vývoj nahodilé těžby")
plt.show()

#dobrovolný doplněk:

print("Nárůst těžby dřeva z roku 2007 byl způsoben orkánem Kyrill.")
