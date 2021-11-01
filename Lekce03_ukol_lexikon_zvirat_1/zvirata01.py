import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

zvirata01 = pandas.read_csv("lexikon-zvirat.csv", sep=";")
print(zvirata01)

zvirata01 = zvirata01.dropna(how="all", axis="columns")
zvirata01 = zvirata01.dropna(how="all", axis="rows")
zvirata01 = zvirata01.set_index("id")
print(zvirata01.tail(30))


def check_url(radek):
    if isinstance(radek.image_src, str):
        if ((radek.image_src.startswith("https://zoopraha.cz/images/")) and (radek.image_src.endswith("jpg")) or (radek.image_src.endswith("JPG"))):
            return radek.image_src



nespravny_odkaz = pandas.DataFrame(columns=["nazev", "image_src"])

zvirata01 = zvirata01.reset_index()

for idx, radek in zvirata01.iterrows():
    nazev = radek.title
    if check_url(radek):
        image_src = radek.image_src
    else:
        image_src = radek.title
    nespravny_odkaz = nespravny_odkaz.append({"nazev": nazev, "image_src": image_src}, ignore_index=True)

print(nespravny_odkaz.tail(30))
#print(nespravny_odkaz.loc[77:82])

