import streamlit as st
st.markdown('# PROJEKT BIKES IN EDINBURGH - DATOVÁ AKADEMIE  ENGETO 2022')
st.markdown('#### Pro řešení projektu používáme programovací jazyk Python a jeho knihovny Pandas, Math, Numpy a pro zobrazování grafů knihovnu Plotly.')

st.markdown("## OBSAH")
st.markdown("### [1. ZADÁNÍ](#section1)")
st.markdown("### [2. ÚPRAVA DAT PRO DATOVOU ANALÝZU](#section2)") 
st.markdown("####  [2.1. SOUBOR EDINBURGH_BIKES.CSV](#section2.1)")
st.markdown("#####  [2.1.2. Základní informace o získaných datech](#section2.1.2)")
st.markdown("#####  [2.1.3. Úprava datových typů](#section2.1.3)")
st.markdown("#####  [2.1.4. Analýza chybějících údajů](#section2.1.4)")  
st.markdown("####  [2.2. SOUBOR EDINBURG_WEATHER.CSV](#section2.2)")
st.markdown("#####  [2.2.1. Načtení souboru s převedením sloupce date na datový typ datetime](#section2.2.1)")
st.markdown("#####  [2.2.2. Základní informace o získaných datech](#section2.2.2)")
st.markdown("#####  [2.2.3. Úprava datových typů](#section2.2.3)")
st.markdown("#####  [2.2.4. Analýza chybějících údajů](#section2.2.4)")
st.markdown("#####  [2.2.5. Vytvoření průměrných hodnot na jednotlivé dny](#section2.2.5)")
st.markdown("#####  [2.2.6. Spojení upravených tabulek do jedné](#section2.2.6)")   
st.markdown("### [3. DATOVÁ ANALÝZA - VÝPŮJČKY KOL V EDINBURGHU](#section3)")
st.markdown("####  [3.1. VYTVOŘENÍ JEDINEČNÝCH STANIC POUŽÍVANÝCH PRO VÝPŮJČKU NEBO VRÁCENÍ](#section3.1)")
st.markdown("####  [3.2. VÝPOČET VZDÁLENOSTÍ MEZI JEDNOTLIVÝMI STANICEMI VZDUŠNOU ČAROU](#section3.2)")
st.markdown("####  [3.3. STANICE PRO VÝPŮJČKU KOL](#section3.3)")
st.markdown("#####  [3.3.1. Vytvoření tabulky s jedinečnými stanicemi pro výpůjčku kol](#section3.3.1)")
st.markdown("#####  [3.3.2. Deskriptivní statistika](#section3.3.2)")
st.markdown("#####  [3.3.3. Histogram pro stanice výpůjček kol](#section3.3.3)")
st.markdown("#####  [3.3.4. Neaktivní stanice pro výpůjčku kol](#section3.3.4)")
st.markdown("#####  [3.3.5. Aktivní stanice pro výpůjčku kol](#section3.3.5)")
st.markdown("#####  [3.3.6. Nejčastěji používané stanice - TOP 10](#section3.3.6)")
st.markdown("####  [3.4. STANICE PRO VRÁCENÍ KOL](#section3.4)")
st.markdown("#####  [3.4.1. Vytvoření tabulky s jedinečnými stanicemi pro vrácení kol](#section3.4.1)")
st.markdown("#####  [3.4.2. Deskriptivní statistika](#section3.4.2)")
st.markdown("#####  [3.4.3. Histogram pro stanice, kam se kola vracejí](#section3.4.3)")
st.markdown("#####  [3.4.4. Neaktivní stanice pro vrácení kol](#section3.4.4)")
st.markdown("#####  [3.4.5. Aktivní stanice pro vrácení kol](#section3.4.5)")
st.markdown("#####  [3.4.6. Nejčastěji používané stanice - TOP 10](#section3.4.6)")
st.markdown("####  [3.5. STANICE, NA KTERÝCH SE KOLA HROMADÍ, NEBO CHYBÍ](#section3.5)")
st.markdown("#####  [3.5.1. Vytvoření tabulky, která srovnává počet výskytů pro půjčku a vrácení u jednotlivých stanic](#section3.5.1)")
st.markdown("#####  [3.5.2. Výsledné tabulky](#section3.5.2)")
st.markdown("####  [3.6. ANALÝZA DOBY VÝPŮJČKY](#section3.6)")
st.markdown("#####  [3.6.1. Deskriptivní statistika](#section3.6.1)")
st.markdown("#####  [3.6.2. Histogram doby výpůjček](#section3.6.2)")
st.markdown("####  [3.7. VÝVOJ POPTÁVKY PRO PŮJČOVÁNÍ KOL V ČASE](#section3.7)")
st.markdown("#####  [3.7.1. Vytvoření tabulky pro zkoumání vývoje poptávky](#section3.7.1)")
st.markdown("#####  [3.7.2. Analýza vývoje poptávky](#section3.7.2)")
st.markdown("#####  [3.7.3. Vliv počasí na výpůjčku kol](#section3.7.3)")
st.markdown("######    [3.7.3.1. Analýza jarního období](#section3.7.3.1)")
st.markdown("######    [3.7.3.2. Analýza letního období](#section3.7.3.2)")
st.markdown("######    [3.7.3.3. Analýza podzimního období](#section3.7.3.3)")
st.markdown("######    [3.7.3.4. Analýza zimního období](#section3.7.3.4)")
st.markdown("#####    [3.7.4. Srovnání počtu výpůjček kol o víkendu a během pracovního týdne](#section3.7.4)")
st.markdown("#####    [3.7.5. Vývoj výpůjček a vrácení kol v jednotlivých stanicích](#section3.7.5)")

st.markdown("<a id='section1'></a>", unsafe_allow_html = True)
st.markdown('## 1. ZADÁNÍ')
st.markdown('V Edinburghu, stejně jako v dalších městech, funguje systém "bike sharing" - ve městě jsou stanice s koly, člověk si může nějaké půjčit a potom ho vrátit v nějaké další stanici. Problém je, že v některých stanicích se kola pravidelně hromadí a jinde naopak chybí. Provozovatel kol, firma Just Eat Cycles, zadala projekt, jehož cílem je systém zefektivnit.') 
st.markdown('Vaším úkolem je zpracovat relevantní data a zjistit z nich informace užitečné pro zbytek týmu. Máte k dispozici data o všech výpůjčkách a data o počasí. Proveďte standardní deskriptivní statistiku dat. Také zjistěte minimálně následující informace:')
st.markdown('• identifikujte aktivní a neaktivní stanice')
st.markdown('•	identifikujte nejfrekventovanější stanice')
st.markdown('•	identifikujte stanice, na kterých se kola hromadí a stanice, kde potenciálně chybí')
st.markdown('•	spočítejte vzdálenosti mezi jednotlivými stanicemi')
st.markdown('•	jak dlouho trvá jedna výpůjčka? Najděte odlehlé hodnoty, zobrazte histogram')
st.markdown('Analýza poptávky:')
st.markdown('•	zobrazte vývoj poptávky po půjčování kol v čase')
st.markdown('•	identifikujte příčiny výkyvů poptávky')
st.markdown('•	zjistěte vliv počasí na poptávku po kolech')
st.markdown('•	půjčují si lidé kola více o víkendu než během pracovního týdne?')
st.markdown("<a id='section2'></a>", unsafe_allow_html = True)
st.markdown('## 2. ÚPRAVA DAT PRO DATOVOU ANALÝZU')
st.markdown("<a id='section2.1'></a>", unsafe_allow_html = True)
st.markdown('### 2.1. SOUBOR EDINBURGH_BIKES.CSV')

import pandas as pd
import math
import cmath
import numpy as np
pd.options.mode.chained_assignment = None  # Deaktivace falešného varování default='warn'
from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning) # Deaktivace upozornění Performance warning
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.markdown("<a id='section2.1.1'></a>", unsafe_allow_html = True)
st.markdown('#### 2.1.1. Základní informace o získaných datech')
st.markdown('Soubor obsahuje **438 259 záznamů od 15.9. 2018 – 30.6 2021.**')
st.markdown('Záznam jedné výpůjčky obsahuje **13 různých informací.**')

# Načtení souboru edinburgh_bikes.csv - převod některých sloupců na časové razítko a na číselné hodnoty.
df = pd.read_csv("edinburgh_bikes.csv", delimiter=',', decimal=',')
st.write(df.head())

st.markdown("<a id='section2.1.2'></a>", unsafe_allow_html = True)
st.markdown('#### 2.1.2. Úprava datových typů')
st.markdown('Původní data jsme upravili, co do datových typů kvůli dalším výpočtům.')
st.markdown('Datový typ object u sloupců **STARTED_AT a ENDED_AT** jsme převedli na **DATETIME64**, a u sloupců **START_STATION_LATIDUDE, END_STATION_LATITUDE, START_STATION_LONGITUDE a END_STATION_LONGITUDE** jsme převedli na číselný formát.')

# Převod STARTED_AT a ENDED_AT na časové razítko a START_STATION_LATIDUDE, END_STATION_LATITUDE, START_STATION_LONGITUDE a END_STATION_LONGITUDE na číselné hodnoty.
st.write("DATOVÉ TYPY PŮVODNÍ TABULKY: ")
d_types = df.dtypes
old_types = d_types.astype(str)
st.write(old_types)
st.write("")

# Úprava sloupce started_at a ended_at - rozdělení na datum a čas
started_list = df["started_at"].str.split(" ")
start = started_list.values
s_date = []
s_time = []
for i in range(len(start)):
    s_date.append(start[i][0])
    s_time.append(start[i][1])

ended_list = df["ended_at"].str.split(" ")
end = ended_list.values
e_date = []
e_time = []
for i in range(len(end)):
    e_date.append(end[i][0])
    e_time.append(end[i][1])
    
# Vložení nových sloupců a odstranění původních a sloupce index
df = df.assign(started_date = s_date,
               started_time = s_time, 
               ended_date = e_date,
               ended_time = e_time
              )
df = df.drop(columns=["index", "started_at", "ended_at"])

# Převod sloupců na formát datumu čísla
selected_columns = ["started_date","ended_date"]
for i in selected_columns:
    df[i] = pd.to_datetime(df[i], format='%Y/%m/%d')
        
selected_columns = ["start_station_latitude","start_station_longitude","end_station_latitude","end_station_longitude"]
for i in selected_columns:
    df[i] = pd.to_numeric(df[i], errors='coerce')
    
st.write("DATOVÉ TYPY TABULKY PO ÚPRAVĚ: ")
d_types = df.dtypes
new_types = d_types.astype(str)
st.write(new_types)
st.write("")

st.markdown("<a id='section2.1.3'></a>", unsafe_allow_html = True)
st.markdown('#### 2.1.3. Analýza chybějících údajů')
st.markdown('Při zkoumání dat jsme zjistili, že v některých záznamech chybí některé informace. Jedná se o sloupce **START_STATION_DESCRIPTION (4 141 záznamů)** a **END_STATION_DESCRIPTION (4 689 záznamů)**.')
st.markdown('Z našeho pohledu se jedná o druhotné informace v záznamu a z toho důvodu nebudeme tyto záznamy odstraňovat, ale hodnotu NaN nahrazujeme číslem 0.')
# Zjištění chybějících informací, jejich nahrazení nulou a ověření, že rozměry tabulky jsou stále stejné
df_bikes = df
st.write("CHYBĚJÍCÍ ÚDAJE: ")
st.write(df_bikes.isna().sum())
df_bikes = df_bikes.fillna(0)
st.write("")
st.write("KONTROLA PO OPRAVĚ: ")
st.write(df_bikes.isna().sum())



st.markdown("<a id='section2.2.'></a>", unsafe_allow_html = True)
st.markdown("### 2.2. SOUBOR EDINBURG_WEATHER.CSV")
st.markdown("<a id='section2.2.1'></a>", unsafe_allow_html = True)
st.markdown("#### 2.2.1 Načtení souboru s převedením sloupce date na datový typ datetime ")
df2 = pd.read_csv("edinburgh_weather.csv", delimiter=',', decimal=',', parse_dates=["date"])


st.markdown("<a id='section2.2.2'></a>", unsafe_allow_html = True)
st.markdown("#### 2.2.2. Základní informace o získaných datech")
st.markdown("Soubor obsahuje **6 336 záznamů od 01.09.2018 – 31.10.2020**.")
st.markdown("Jeden záznam obsahuje **11 různých informací vztahující se k počasí**.")
print("ROZMĚRY TABULKY: ")
print(df2.shape)
print("")
st.write("STRUKTURA TABULKY")
st.write(df2.head())


st.markdown("<a id='section2.2.3'></a>", unsafe_allow_html = True)
st.markdown("#### 2.2.3 Úprava datových typů")
st.markdown("Původní data jsme upravili, co do datových typů kvůli dalším výpočtům.")
st.markdown("Sloupec **DATE** jsme převedli na **DATETIME64**, a sloupce **TEMP, FEELS, WIND, GUST, RAIN, HUMIDITY, CLOUD, PRESSURE** jsme převedli na číselný formát.")
st.markdown("Sloupec **WIND** jsme rozdělili do dvou sloupců na **WIND_KM_H** a **WIND_DIRECTION**.")
st.markdown("Tedy tabulka má po úpravě  **12 sloupců**.")
# Úprava sloupce wind - vytáhnutí hodnot síly a směru větru
wind_list = df2["wind"].str.split(" ")
wind = wind_list.values
w_km_h = []
w_direction = []
for i in range(len(wind)):
    w_km_h.append(wind[i][0])
    w_direction.append(wind[i][3])

# Příprava k převodu na číselný formát - vložení upravených sloupců a odtranění původních
df2 = df2.assign(time_h = df2["time"],
                 temp_degree = df2["temp"].str.strip("°c"),
                 feells_degree = df2["feels"].str.strip("°c"),
                 wind_km_h = w_km_h,
                 wind_direction = w_direction,
                 gust_km_h = df2["gust"].str.strip("km/h"),
                 rain_mm = df2["rain"].str.strip("mm"),
                 humitidy_percent = df2["humidity"].str.strip("%"),
                 cloud_percent = df2["cloud"].str.strip("%"),
                 pressure_mb = df2["pressure"].str.strip("mb"),
                 visibility = df2["vis"]
                )
df2 = df2.drop(columns=["time", "temp", "feels", "wind", "gust", "rain", "humidity", "cloud", "pressure", "vis"])

# Převod sloupců na číselný formát
selected_columns = ["temp_degree","feells_degree","wind_km_h","gust_km_h", "rain_mm", "humitidy_percent", "cloud_percent", "pressure_mb"]
for i in selected_columns:
    df2[i] = pd.to_numeric(df2[i], errors='coerce')    

# Zjištění rozměrů upravené tabulky a datových typů
print("ROZMĚRY TABULKY PO ÚPRAVĚ: ")
print(df2.shape)
print("")
st.write("DATOVÉ TYPY TABULKY PO ÚPRAVĚ: ")
d_types = df2.dtypes
new_types = d_types.astype(str)
st.write(new_types)
st.write("")
st.write("TABULKA PO ÚPRAVĚ")
st.write(df2.head())


st.markdown("<a id='section2.2.4'></a>", unsafe_allow_html = True)
st.markdown("#### 2.2.4. Analýza chybějících údajů")
st.markdown("Při zkoumání dat jsme v upravené tabulce nenašli žádné chybějící údaje.")
st.write("CHYBĚJÍCÍ ÚDAJE: ")
st.write(df2.isna().sum())
st.write("")


st.markdown("<a id='section2.2.5'></a>", unsafe_allow_html = True)
st.markdown("#### 2.2.5. Vytvoření průměrných hodnot na jednotlivé dny")
st.markdown("Tabulka obsahuje 8 měření za jeden den.  Z těchto dat jsme vytvořili tabulku s průměrnými hodnotami.")
st.markdown("Nešlo zprůměrovat sloupce **VISIBILITY** A **WIND_DIRECTION**, protože se jedná o textové sloupce. Z toho důvodu jsou vynechány  i při spojení do výsledné tabulky pro datovou analýzu.")
# Vytvoření průměrných hodnot a seskupení podle data
print("TABULKA PRŮMĚRNÝCH HODNOT")
df_weather = df2.groupby("date", as_index = False).mean().round(2)
st.write(df_weather.head())


st.markdown("<a id='section2.2.6'></a>", unsafe_allow_html = True)
st.markdown("#### 2.2.6. Spojení upravených tabulek do jedné ")
st.markdown("Při spojování jsme odhalili překlep ve stanici **Picardy Place**. Z toho důvodu jsme stanici Picady Place, přejmenovali na Picardy place, aby tento údaj nezkresloval naše zkoumání.")
st.markdown("Zároveň jsme znovu  ověřili datové typy a provedli analýzu chybějících údajů, pří které jsme odhalili, že data o počasí chybí u **85 288 záznamů**. Je to dáno tím, že data o počasí jsou pouze **do 31.10.2020**, zatímco záznamy o výpůjčkách kol jsou až **do 30.6. 2021**. Z toho důvodu hodnotu **Nan** neopravujeme a necháváme v záznamech, protože nám nebude dělat potíže v našem hledání odpovědí na zadané otázky a zároveň budeme moci využít data o výpůjčkách.")
st.markdown("Finální tabulka pro datovou analýzu má tedy **438 259 záznamů**. Každý záznam obsahuje **23 různých informací**.")
# Spojení tabulek df_bikes a df_weather
df_final = df_bikes.merge(df_weather, how = "left", left_on = "started_date", right_on = "date"  )
print("ROZMĚRY TABULKY: ")
print(df_final.shape)
st.write("DATOVÉ TYPY TABULKY: ")
d_types = df_final.dtypes
new_types = d_types.astype(str)
st.write(new_types)
st.write("")

# Zjištění. zda v záznamech existují chybějící informace - data o počasí končí 31.10.2020, data o výpůjčkách 30.6.2021, rozdíl je tedy 85288 záznamů
st.write("CHYBĚJÍCÍ ÚDAJE: ")
st.write(df_final.isna().sum())
st.write("")

# Změna jména Picady place na Picardy place, jedná se překlep.
df_final = df_final.replace({"Picady Place": "Picardy Place"})
st.write("FINÁLNÍ TABULKA PRO DATOVOU ANALÝZU")
st.write(df_final.head())



st.markdown("<a id='section3'></a>", unsafe_allow_html = True)
st.markdown("## 3. DATOVÁ ANALÝZA - VÝPŮJČKY KOL V EDINBURGHU")
st.markdown("<a id='section3.1.'></a>", unsafe_allow_html = True)
st.markdown("### 3.1. VYTVOŘENÍ JEDINEČNÝCH STANIC POUŽÍVANÝCH PRO VÝPŮJČKU NEBO VRÁCENÍ")
st.markdown("Z finální tabulky jsme odstranili duplicity ve sloupcích **START_STATION_NAME** a **END_STATION_NAME**. Následně jsme prověřili množinu jmen stanic pro výpůjčku a pro vrácení, protože se tam objevily rozdíly. Do výsledné tabulky jedinečných stanic jsem nakonec vložili jedinečné stanice z **END_STATION_NAME**, protože sloupec má o dvě stanice více. Výsledná tabulka obsahuje **169 stanic** se zeměpisnou hodnoty šířky a délky, kterou budeme používat pro výpočet vzdáleností stanic od sebe. Tabulku jsme uložili do souboru **STATIONS_EDINBURH.CSV.**")
# Odstranění duplicit stanic pro výpůjčku a vrácení, porovnání a zjištění odlišných stanic, a následně vytvoření výsledné tabulky.
df_no_duplicate_start = df_final.drop_duplicates(subset=["start_station_name"])
df_no_duplicate_start = df_no_duplicate_start.drop(columns=["start_station_id","duration", "started_date", "started_time", "end_station_id", "end_station_name", "end_station_description", "end_station_latitude", 
                                                "end_station_longitude", "ended_date","ended_time", "temp_degree", "feells_degree", "wind_km_h", "gust_km_h", "rain_mm", "humitidy_percent", "cloud_percent", "pressure_mb"])

df_no_duplicate_end = df_final.drop_duplicates(subset=["end_station_name"])
df_no_duplicate_end = df_no_duplicate_end.drop(columns=["start_station_id","duration", "started_date", "started_time", "end_station_id", "start_station_name", "start_station_description", "start_station_latitude", 
                                              "start_station_longitude", "end_station_id", "ended_date","ended_time", "temp_degree", "feells_degree", "wind_km_h", "gust_km_h", "rain_mm", "humitidy_percent", "cloud_percent", "pressure_mb"])

# Porovnání stanic start a end a zjištění rozdílu
end_name = set(df_no_duplicate_end["end_station_name"])
start_name = set(df_no_duplicate_start["start_station_name"])
difference = end_name - start_name

st.write("ROZDÍLNÉ HODNOTY VE STANICÍCH VÝPŮJČEK")
start_difference = df_no_duplicate_start.loc[df_no_duplicate_start["start_station_name"].isin(difference)]
st.write(start_difference)
st.write("")
st.write("ROZDÍLNÉ HODNOTY VE STANICÍCH VRÁCENÍ")
end_difference = df_no_duplicate_end.loc[df_no_duplicate_end["end_station_name"].isin(difference)]
st.write(end_difference)
st.write("")

# Úprava výsledné tabulky
df_stations_edinburgh = df_no_duplicate_end
df_stations_edinburgh = df_stations_edinburgh.drop(columns=["end_station_description"])
df_stations_edinburgh = df_stations_edinburgh.rename(columns={"end_station_name": "station_name", "end_station_latitude": "station_latitude", 
                                                             "end_station_longitude": "station_longitude"})
# Využijeme při tvorbě tabulky vzdáleností
station_name = list(df_stations_edinburgh["station_name"]) 

df_stations_edinburgh.set_index("station_name", inplace=True)
st.write("VÝSLEDNÁ TABULKA VŠECH STANIC V EDINBURGHU PRO VÝPŮJČKY A VRÁCENÍ KOL")
st.write(df_stations_edinburgh)
st.write("")

df_stations_edinburgh.to_csv("stations_edinburgh.csv")


st.markdown("<a id='section3.2'></a>", unsafe_allow_html = True)
st.markdown("### 3.2. VÝPOČET VZDÁLENOSTÍ MEZI JEDNOTLIVÝMI STANICEMI VZDUŠNOU ČAROU")
st.markdown("Vzdálenost počítáme podle Haversinova vzorce, který bere v potaz kulatost země. Výsledná tabulka je uložena v souboru **DISTANCE_STATIONS.CSV**.")
# Vytvoření tabulky vzdálenosti pro jednotlivé stanice. 
df_distance_stations = df_stations_edinburgh
df_distance_stations = df_distance_stations.drop(columns=["station_latitude", "station_longitude", "date"])

for name in station_name:
    df_distance_stations[name] = 0
    
# Výpočet vzdáleností mezi jednotlivými místy. Vzdálenost počítáme podle Haversinova vzorce ,který bere v potaz kulatost země.
# ACOS(SIN(RADIANS(lat1))*SIN(RADIANS(lat2))+COS(RADIANS(lat1))*COS(RADIANS(lat2))*COS(RADIANS(long2-long1)))*6371
# Pro výpočet používáme i knihovnu cmath, protože při použití klasické knihovny math docházelo k chybě ValueError: math domain error.
# Na různých fórech jsem se dozvěděl, že se jedná o chybu, když používáme uvnitř funkce záporné číslo, nebo nulové číslo, což je při našem výpočtu pravda, protože longitude je záporná,
# ale je zajímavé, když jsem funkci testoval, že výpočet beží do 20 hodnoty, pak do 55 hodnoty, pak do 122 hodnoty, pak do 144 hodnoty, a pak až do konce, přestože jsou všude záporné hodnoty.
    
dist = []
k = 0
for j in range(len(df_stations_edinburgh["station_latitude"])):
    for i in range(len(df_stations_edinburgh["station_latitude"])):
        calculation = cmath.acos(cmath.sin(math.radians(df_stations_edinburgh["station_latitude"][j])) * cmath.sin(math.radians(df_stations_edinburgh["station_latitude"][i])) 
        + cmath.cos(math.radians(df_stations_edinburgh["station_latitude"][j])) * cmath.cos(math.radians(df_stations_edinburgh["station_latitude"][i]))
        * cmath.cos(math.radians(df_stations_edinburgh["station_longitude"][i]) - math.radians(df_stations_edinburgh["station_longitude"][j]))) * 6371
        dist.append (round(calculation.real,2))
    df_distance_stations[station_name[k]] = dist
    dist.clear()
    k+=1
    
st.write("VÝSLEDNÁ TABULKA VZDÁLENOSTÍ V KM")
st.write(df_distance_stations)


st.markdown("<a id='section3.3'></a>", unsafe_allow_html = True)
st.markdown("### 3.3. STANICE PRO VÝPŮJČKU KOL")
st.markdown("<a id='section3.3.1'></a>", unsafe_allow_html = True)
st.markdown("#### 3.3.1. Vytvoření tabulky s jedinečnými stanicemi pro výpůjčku kol ")
st.markdown("K vytvoření této tabulky používáme již vytvořenou tabulku pro jedinečné hodnoty **START_STATION** a přidáváme sloupec **FREQUENCY_START_STATION**, který vyjadřuje četnost užívání jednotlivých stanic během sledovaného období. Tabulka tedy obsahuje **168 stanic**, které uvádíme na mapě.")
df_start_stations_frequency = df_final["start_station_name"].value_counts().rename_axis('unique_values').reset_index(name='counts')
df_start_stations_frequency = df_no_duplicate_start.merge(df_start_stations_frequency, how = "left", left_on = "start_station_name", right_on = "unique_values" )
df_start_stations_frequency = df_start_stations_frequency.drop(columns=["unique_values", "date"])
df_start_stations_frequency = df_start_stations_frequency.rename(columns={"counts": "frequency_start_station"})
st.write("VÝSLEDNÁ TABULKA STANIC V EDINBURGHU PRO VÝPŮJČKY KOL")
d_types = df_start_stations_frequency
new_types = d_types.astype(str)
st.write(new_types)
st.write ("")

fig = px.scatter_mapbox(df_start_stations_frequency,lat="start_station_latitude", lon="start_station_longitude", hover_name = "start_station_name", hover_data = ["frequency_start_station"] ,zoom=10, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)   #  =  fig.show()


st.markdown("<a id='section3.3.2'></a>", unsafe_allow_html = True)
st.markdown("#### 3.3.2 Deskriptivní statistika")
st.markdown("**Pro stanice, odkud si lidé kola půjčují můžeme říci, že za sledovanou dobu je:**")
st.markdown("a) průměrné využití každé stanice:			2609x")
st.markdown("b) 25% percentil: 							221x ")
st.markdown("c) 50 % percentil (medián): 				1427x")
st.markdown("d) 75 % percentil:							4053x")
st.markdown("e) směrodatná odchylka: 					3145x")
st.markdown("f) minimální hodnota:						1x")
st.markdown("g) maximální hodnota:						17390x")
st.markdown("**To v přepočtu při daném časovém rozpětí datové sady (1019 dnů) zaokrouhleně znamená, že:**")
st.markdown("a) průměrné využití stanice pro výpůjčku je: 	2,5x  denně")
st.markdown("b) 25% percentil: 								1x  za 5 dní")
st.markdown("c) 50 % percentil (medián): 					1,5x denně")
st.markdown("d) 75 % percentil:								4x denně")
st.markdown("e) variační koeficient							121%")
st.markdown("f) minimální hodnota							1x za 1019 dní")
st.markdown("g) maximální hodnota							17x denně")
# Zjištění základních hodnot deskriptivní statistiky.
print(df_start_stations_frequency["frequency_start_station"].describe().round(2))


st.markdown("<a id='section3.3.3'></a>", unsafe_allow_html = True)
st.markdown("#### 3.3.3. Histogram pro stanice výpůjček kol ")
st.markdown("Z níže uvedeného histogramu je vidět, že soubor dat ohledně stanic, ze kterých se kola půjčují se **nepodobá normálnímu rozdělení pravděpodobnosti** a v datech se vyskytují odlehlé hodnoty. ")
st.markdown("Hranici slabé a silné odlehlé hodnoty jsme určili na základě 1., a 3. kvartilu spolu s interkvartilovým rozsahem. Na základě takového výpočtu nyní víme, že: ")
st.markdown("**Hranice pro slabou odlehlou hodnotu** je každá stanice, ze které se kolo půjčí více než **9801x**. Takovýchto stanic je celkem **5**, což odpovídá zhruba **3%** z celkového počtu stanic.")
st.markdown("**Hranice pro silnou odlehlou hodnotu** je každá stanice, ze které se kolo půjčí více než **15490x**. Takovouto stanici máme pouze **jednu**, což odpovídá zhruba **0,5%** z celkového počtu stanic.")
st.markdown("Tedy odlehlé hodnoty z celkové sady tvoří **3,5%**.")
fig = px.histogram(df_start_stations_frequency, x="frequency_start_station")
st.plotly_chart(fig, use_container_width=True)
first_quartil = 221
third_quartil = 4053
IQR = third_quartil - first_quartil                                 # Interquartilový rozsah
outlier = round(1.5 * IQR + third_quartil)
strong_outlier = round(3 * IQR + third_quartil)
print("Hranice slabé odlehlé hodnoty je: ", outlier, "x")
print("Hranice silné odlehlé hodnoty je: ", strong_outlier, "x")
print("")

df_outlier = df_start_stations_frequency.query("frequency_start_station > 9801 and frequency_start_station <= 15549").count()
print("POČET SLABÝCH ODLEHLÝCH HODNOT: ", df_outlier["frequency_start_station"])
df_strong_outlier = df_start_stations_frequency.query("frequency_start_station > 15549").count()
print("POČET SILNÝCH ODLEHLÝCH HODNOT: ", df_strong_outlier["frequency_start_station"])


st.markdown("<a id='section3.3.4'></a>", unsafe_allow_html = True)
st.markdown("#### 3.3.4. Neaktivní stanice pro výpůjčku kol")
st.markdown("Z výše uvedených údajů jsme se rozhodli definovat, že **neaktivní stanicí je ta, která je využita méně než jednou denně**. Tomuto kritériu vyhovuje **71 stanic**. Seznam všech neaktivních stanic je uložen v souboru **START_INACTIVE_STATION.CSV**.")
df_inactive_station = df_start_stations_frequency.query("frequency_start_station <= 1019")
df_inactive_station ["start_station_name"].nunique()
fig = px.scatter_mapbox(df_inactive_station,lat="start_station_latitude", lon="start_station_longitude", hover_name = "start_station_name", hover_data = ["frequency_start_station"] ,zoom=11, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Uložení neaktivních stanic do souboru 
df_inactive_station.to_csv("start_inactive_station.csv")


st.markdown("<a id='section3.3.5'></a>", unsafe_allow_html = True)
st.markdown("#### 3.3.5. Aktivní stanice pro výpůjčku kol")
st.markdown("Po zjištění počtu neaktivních stanic můžeme říci, že **aktivních stanic zůstává 97**. Seznam všech aktivních stanic je uložen v souboru **START_ACTIVE_STATION.CSV.**")
df_active_station = df_start_stations_frequency.query("frequency_start_station > 1019")
fig = px.scatter_mapbox(df_active_station,lat="start_station_latitude", lon="start_station_longitude", hover_name = "start_station_name", hover_data = ["frequency_start_station"] ,zoom=11, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Uložení aktivních stanic do souboru 
df_active_station.to_csv("start_active_station.csv")


st.markdown("<a id='section3.3.6'></a>", unsafe_allow_html = True)
st.markdown("#### 3.3.6 Nejčastěji používané stanice - TOP 10")
st.markdown("Výpůjčka se v těchto staních pohybuje mezi **9 - 17 denně**.")
df_top = df_active_station.sort_values(by=["frequency_start_station"], ascending=False)
st.write (df_top[["start_station_name", "frequency_start_station"]].head(10))
st.write("")

fig = px.scatter_mapbox(df_top.head(10),lat="start_station_latitude", lon="start_station_longitude", hover_name = "start_station_name", hover_data = ["frequency_start_station"] ,zoom=10, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.4'></a>", unsafe_allow_html = True)
st.markdown("### 3.4. STANICE PRO VRÁCENÍ KOL")
st.markdown("<a id='section3.4.1'></a>", unsafe_allow_html = True)
st.markdown("#### 3.4.1. Vytvoření tabulky s jedinečnými stanicemi pro vrácení kol")
st.markdown("K vytvoření této tabulky používáme již vytvořenou tabulku pro jedinečné hodnoty **END_STATION**  a přidáváme sloupec **FREQUENCY_START_STATION**, který vyjadřuje četnost užívání jednotlivých stanic. Tabulka tedy obsahuje **169 stanic**, které uvádíme na mapě.")
df_end_stations_frequency = df_final["end_station_name"].value_counts().rename_axis('unique_values').reset_index(name='counts')
df_end_stations_frequency = df_no_duplicate_end.merge(df_end_stations_frequency, how = "left", left_on = "end_station_name", right_on = "unique_values" )
df_end_stations_frequency = df_end_stations_frequency.drop(columns=["unique_values", "date"])
df_end_stations_frequency = df_end_stations_frequency.rename(columns={"counts": "frequency_end_station"})
st.write("VÝSLEDNÁ TABULKA STANIC V EDINBURGHU PRO VRÁCENÍ KOL")
d_types = df_end_stations_frequency
new_types = d_types.astype(str)
st.write(new_types)
st.write("")

fig = px.scatter_mapbox(df_end_stations_frequency,lat="end_station_latitude", lon="end_station_longitude", hover_name = "end_station_name", hover_data = ["frequency_end_station"] ,zoom=11, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.4.2'></a>", unsafe_allow_html = True)
st.markdown("#### 3.4.2 Deskriptivní statistika")
st.markdown("**Pro stanice, kam lidé kola vracejí můžeme říci, že za sledovanou dobu je:**")
st.markdown("a) průměrné využití každé stanice:			2593x")
st.markdown("b) 25% percentil: 							224x ")
st.markdown("c) 50 % percentil (medián): 				1473x")
st.markdown("d) 75 % percentil:							3872x")
st.markdown("e) směrodatná odchylka: 					3188x")
st.markdown("f) minimální hodnota:						2x")
st.markdown("g) maximální hodnota:						16656x")
st.markdown("**To v přepočtu při daném časovém rozpětí datové sady (1019 dnů) zaokrouhleně znamená, že:**")
st.markdown("a) průměrné využití stanice pro výpůjčku je: 	2,5x  denně")
st.markdown("b) 25% percentil: 								1x  za 5 dní")
st.markdown("c) 50 % percentil (medián): 					1,5x denně")
st.markdown("d) 75 % percentil:								4x denně")
st.markdown("e) variační koeficient							123%")
st.markdown("f) minimální hodnota							1x za 510 dní")
st.markdown("g) maximální hodnota							16x denně")
# Zjištění základních hodnot deskriptivní statistiky.
print(df_end_stations_frequency["frequency_end_station"].describe().round(2))


st.markdown("<a id='section3.4.3'></a>", unsafe_allow_html = True)
st.markdown("#### 3.4.3. Histogram pro stanice, kam se kola vracejí")
st.markdown("Z níže uvedeného histogramu je vidět, že soubor dat ohledně stanic, ze kterých se kola půjčují se **nepodobá normálnímu rozdělení pravděpodobnosti** a v datech se vyskytují odlehlé hodnoty. ")
st.markdown("Hranici slabé a silné odlehlé hodnoty jsme určili jako při výpočtu stanic, odkud si kola lidé půjčují.")
st.markdown("**Hranice pro slabou odlehlou hodnotu** je každá stanice, ze které se kolo půjčí více než **9344x**. Takovýchto stanic je celkem **4**, což odpovídá zhruba **2%** z celkového počtu stanic.")
st.markdown("**Hranice pro silnou odlehlou hodnotu** je každá stanice, ze které se kolo půjčí více než **14816x**. Takovýchto stanic je celkem **3**, což odpovídá zhruba **2%** z celkového počtu stanic.")
st.markdown("Tedy odlehlé hodnoty z celkové sady tvoří **4%**.")
fig = px.histogram(df_end_stations_frequency, x="frequency_end_station")
st.plotly_chart(fig, use_container_width=True)
first_quartil = 224
third_quartil = 3872
IQR = third_quartil - first_quartil                                 # Interquartilový rozsah
outlier = round(1.5 * IQR + third_quartil)
strong_outlier = round(3 * IQR + third_quartil)
print("Hranice slabé odlehlé hodnoty je: ", outlier, "x")
print("Hranice silné odlehlé hodnoty je: ", strong_outlier, "x")
print("")

df_outlier = df_end_stations_frequency.query("frequency_end_station > 9344 and frequency_end_station <= 14816").count()
print("POČET SLABÝCH ODLEHLÝCH HODNOT: ", df_outlier["frequency_end_station"])
df_strong_outlier = df_end_stations_frequency.query("frequency_end_station > 14816").count()
print("POČET SILNÝCH ODLEHLÝCH HODNOT: ", df_strong_outlier["frequency_end_station"])


st.markdown("<a id='section3.4.4'></a>", unsafe_allow_html = True)
st.markdown("#### 3.4.4. NEAKTIVNÍ STANICE PRO VRÁCENÍ KOL")
st.markdown("Z výše uvedených údajů jsme se rozhodli definovat, že **neaktivní stanicí je ta, která je využita méně než jednou denně**. Tomuto kritériu vyhovuje **70 stanic**. Seznam všech neaktivních stanic je uložen v souboru **END_INACTIVE_STATION.CSV.**")
df_inactive_station = df_end_stations_frequency.query("frequency_end_station <= 1019")
df_inactive_station ["end_station_name"].nunique()
print("VÝSLEDNÁ TABULKA NEAKTIVNÍCH STANIC V EDINBURGHU PRO VRÁCENÍ KOL")
d_types = df_inactive_station
new_types = d_types.astype(str)
st.write(new_types)
st.write("")

fig = px.scatter_mapbox(df_inactive_station,lat="end_station_latitude", lon="end_station_longitude", hover_name = "end_station_name", hover_data = ["frequency_end_station"] ,zoom=10, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Uložení neaktivních stanic do souboru 
df_inactive_station.to_csv("end_inactive_station.csv")


st.markdown("<a id='section3.4.5'></a>", unsafe_allow_html = True)
st.markdown("#### 3.4.5. AKTIVNÍ STANICE PRO VRÁCENÍ KOL")
st.markdown("Po zjištění počtu neaktivních stanic můžeme říci, že **aktivních stanic zůstává 99**. Seznam všech aktivních stanic je uložen v souboru **END_ACTIVE_STATION.CSV.** ")
df_active_station = df_end_stations_frequency.query("frequency_end_station > 1019")
print("VÝSLEDNÁ TABULKA AKTIVNÍCH STANIC V EDINBURGHU PRO VRÁCENÍ KOL")
d_types = df_active_station
new_types = d_types.astype(str)
st.write(new_types)
st.write("")

fig = px.scatter_mapbox(df_active_station,lat="end_station_latitude", lon="end_station_longitude", hover_name = "end_station_name", hover_data = ["frequency_end_station"] ,zoom=11, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Uložení aktivních stanic do souboru 
df_active_station.to_csv("end_active_station.csv")


st.markdown("<a id='section3.4.6'></a>", unsafe_allow_html = True)
st.markdown("#### 3.4.6 NEJČASTĚJI POUŽÍVANÉ STANICE PRO VRÁCENÍ - TOP 10")
st.markdown("Vrácení kol se v těchto stanicích pohybuje mezi **8 - 16 denně.**")
df_top = df_active_station.sort_values(by=["frequency_end_station"], ascending=False)
st.write (df_top[["end_station_name", "frequency_end_station"]].head(10))
st.write("")

fig = px.scatter_mapbox(df_top.head(10),lat="end_station_latitude", lon="end_station_longitude", hover_name = "end_station_name", hover_data = ["frequency_end_station"] ,zoom=10, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.5'></a>", unsafe_allow_html = True)
st.markdown("### 3.5. STANICE, NA KTERÝCH SE KOLA HROMADÍ, NEBO CHYBÍ")
st.markdown("<a id='section3.5.1'></a>", unsafe_allow_html = True)
st.markdown("#### 3.5.1. Vytvoření tabulky, která srovnává počet výskytů pro půjčku a vrácení u jednotlivých stanic")
# Spojení tabulek s četností pro start a end station
df_start_end_stations_frequency = df_end_stations_frequency.merge(df_start_stations_frequency, how = "left", left_on = "end_station_name", right_on = "start_station_name")

df_start_end_stations_frequency = df_start_end_stations_frequency.drop(columns=["start_station_name", "start_station_description", "start_station_latitude", "start_station_longitude"])
df_start_end_stations_frequency = df_start_end_stations_frequency.rename(columns={"end_station_name": "station_name", "end_station_description": "station_description", 
                                                                                  "end_station_latitude": "station_latitude", "end_station_longitude": "station_longitude"})
# Nahrazení NaN hodnot
df_start_end_stations_frequency = df_start_end_stations_frequency.fillna(0)

st.write("VÝSLEDNÁ TABULKA ČETNOSTI POUŽÍTÍ STANICE PRO VÝPŮJČKU, NEBO VRÁCENÍ KOL")
d_types = df_start_end_stations_frequency
new_types = d_types.astype(str)
st.write(new_types)
st.write("")


st.markdown("<a id='section3.5.2'></a>", unsafe_allow_html = True)
st.markdown("#### 3.5.2. Výsledné tabulky ")
st.markdown("Z výsledku je vidět, že **průměrný denní přebytek se pohybuje od 1 - 5 kol**. Celkem takovýchto stanic je **29** . Tam, kde kola chybí je to podobné, **průměrný denní nedostatek se pohybuje od 1 - 5 kol**. Takových stanic je **33**. Na mapě zobrazujeme stanice, kde je počet přebytku, nedostatku větší než 1 kolo denně.")
st.markdown("Stálo by za to nyní zjistit, ze kterých stanic s přebytkem by se mohlo převážet na stanice s nedostatkem. K tomu se dá využít tabulka vzdáleností jednotlivých stanic a vše optimalizovat.")
# Vytvoření seznamu stanic, ve kterých kola přebývají, chybí, nebo jsou si rovny
list_stations_surplus = []
list_stations_lack = []
list_equal = []

for i in range(len(df_start_end_stations_frequency)):
    if df_start_end_stations_frequency["frequency_end_station"][i] > df_start_end_stations_frequency["frequency_start_station"][i]:
        list_stations_surplus.append(df_start_end_stations_frequency["station_name"][i])
    elif df_start_end_stations_frequency["frequency_end_station"][i] < df_start_end_stations_frequency["frequency_start_station"][i]:
        list_stations_lack.append(df_start_end_stations_frequency["station_name"][i])
    else:
        list_equal.append(df_start_end_stations_frequency["station_name"][i])
        
# Vytvoření jednotlivých tabulek pro přebytek, nedostatek, nebo rovnost kol ve stanici
df_stations_surplus = df_start_end_stations_frequency.loc[df_start_end_stations_frequency["station_name"].isin(list_stations_surplus)]
df_stations_lack = df_start_end_stations_frequency.loc[df_start_end_stations_frequency["station_name"].isin(list_stations_lack)]
df_stations_equal = df_start_end_stations_frequency.loc[df_start_end_stations_frequency["station_name"].isin(list_equal)]

# Přepočítání přebytku, nedostatku kol na zakrouhlený denní průměr ve stanici a vytvoření rozdílu těchto hodnot
# Přebytek
fes = df_stations_surplus["frequency_end_station"]
avg_day_end_station = fes/1019
avg_day_end_station = avg_day_end_station.round(0)

fss = df_stations_surplus["frequency_start_station"]
avg_day_start_station = fss/1019
avg_day_start_station = avg_day_start_station.round(0)

df_stations_surplus["avg_day_end_station"] = avg_day_end_station
df_stations_surplus["avg_day_start_station"] = avg_day_start_station

df_stations_surplus["avg_day_different"] = df_stations_surplus["avg_day_end_station"] - df_stations_surplus["avg_day_start_station"]


# Nedostatek
fes = df_stations_lack["frequency_end_station"]
avg_day_end_station = fes/1019
avg_day_end_station = avg_day_end_station.round(0)

fss = df_stations_lack["frequency_start_station"]
avg_day_start_station = fss/1019
avg_day_start_station = avg_day_start_station.round(0)

df_stations_lack["avg_day_end_station"] = avg_day_end_station
df_stations_lack["avg_day_start_station"] = avg_day_start_station

df_stations_lack["avg_day_different"] = df_stations_lack["avg_day_start_station"] - df_stations_lack["avg_day_end_station"]

# Nové vytvoření seznamu stanic, ve kterých kola přebývají, chybí

# Přebytky
list_stations_surplus = []
list_stations_lack = []

for number in df_stations_surplus["avg_day_different"]:
    if number > 0:
        list_stations_surplus.append(number)

df_stations_surplus = df_stations_surplus.loc[df_stations_surplus["avg_day_different"].isin(list_stations_surplus)]
df_stations_surplus = df_stations_surplus.sort_values(by=["avg_day_different"], ascending=False)

# Nedostatky
for number in df_stations_lack["avg_day_different"]:
    if number > 0:
        list_stations_lack.append(number)

df_stations_lack = df_stations_lack.loc[df_stations_lack["avg_day_different"].isin(list_stations_lack)]
df_stations_lack = df_stations_lack.sort_values(by=["avg_day_different"], ascending=False)

# Zobrazení výsledných tabulek
st.write("TABULKA PRŮMĚRNÝCH DENNÍCH PŘEBYTKŮ KOL VE STANICI")
st.write("Počet stanic: ", len(df_stations_surplus))
st.write(df_stations_surplus[["station_name", "avg_day_different"]])
fig = px.scatter_mapbox(df_stations_surplus.head(8),lat="station_latitude", lon="station_longitude", hover_name = "station_name", hover_data = ["avg_day_different"] ,zoom=10, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)
st.write("")

st.write("TABULKA PRŮMĚRNÝCH DENNÍCH NEDOSTATKŮ KOL VE STANICI")
st.write("Počet stanic: ", len(df_stations_lack))
st.write(df_stations_lack[["station_name", "avg_day_different"]])
fig = px.scatter_mapbox(df_stations_lack.head(10),lat="station_latitude", lon="station_longitude", hover_name = "station_name", hover_data = ["avg_day_different"] ,zoom=10, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Uložení seznamu stanic, ve kterých kola přebývají,chybí, nebo jsou si rovny
df_stations_surplus.to_csv("stations_surplus.csv")  
df_stations_lack.to_csv("stations_lack.csv")  


st.markdown("<a id='section3.6'></a>", unsafe_allow_html = True)
st.markdown("### 3.6. ANALÝZA DOBY VÝPŮJČKY")
st.markdown("<a id='section3.6.1'></a>", unsafe_allow_html = True)
st.markdown("#### 3.6.1. Deskriptivní statistika")
st.markdown("Na základě dostupných dat můžeme po zaokrouhlední říci, že: ")
st.markdown("a) průměrná doba výpůjčky je:			 	1949 s = 32,5 min.")
st.markdown("b) 25% percentil: 							624 s =  10,5 min.")
st.markdown("c) 50 % percentil (medián): 				1163 s = 19,5 min.")
st.markdown("d) 75 % percentil:							2529 s = 42,15 min.")
st.markdown("e) variační koeficient: 					290%")
st.markdown("f) minimální doba výpůjčky:					61 s = 1 min.")
st.markdown("g) maximální doba výpůjčky:					2363348 s = 27,5 dne")
print(df_final["duration"].describe().round(2))


st.markdown("<a id='section3.6.2'></a>", unsafe_allow_html = True)
st.markdown("#### 3.6.2. Histogram doby výpůjček")
st.markdown("Z níže uvedeného histogramu je vidět, že soubor dat ohledně doby výpůjčky se **nepodobá normálnímu rozdělení pravděpodobnosti** a v datech se vyskytují odlehlé hodnoty. Zobrazený histogram je již zvětšený, tak, aby bylo možno vidět nějaký průběh spolu s hranicemi odlehlých hodnot. Pokud někdo chce graf vrátit do původního měřítka, stačí v grafu kliknout na ikonu Autoscale. ")
st.markdown("Hranici slabé a silné odlehlé hodnoty jsme určili na základě 1., a 3. kvartilu spolu s interkvartilovým rozsahem. Na základě takového výpočtu nyní víme, že: ")
st.markdown("**Hranice pro slabou odlehlou hodnotu** je 5386s, což je zhruba **90 min. doby výpůjčky**. Takovýchto výpůjček máme celkem **12878**, což odpovídá zhruba **3%** z celkového počtu záznamů.")
st.markdown("**Hranice pro silnou odlehlou hodnotu** je 8244s, což je zhruba **137 min. doby výpůjčky** . Takovýchto výpůjček máme celkem **9278**, což odpovídá zhruba **2%** z celkového počtu záznamů.")
st.markdown("Tedy odlehlé hodnoty z celkové sady tvoří **5%**.")

first_quartil = 624
third_quartil = 2529
IQR = third_quartil - first_quartil                                 # Interquartilový rozsah
outlier = round(1.5 * IQR + third_quartil)
strong_outlier = round(3 * IQR + third_quartil)
print("Hranice odlehlé hodnoty je: ", outlier, "s")
print("Hranice silné odlehlé hodnoty je: ", strong_outlier, "s")
df_outlier = df_final.query("duration > 5386 and duration <= 8244").count()
print("POČET SLABÝCH ODLEHLÝCH HODNOT: ", df_outlier["duration"])
df_strong_outlier = df_final.query("duration > 8244").count()
print("")
print("POČET SILNÝCH ODLEHLÝCH HODNOT: ", df_strong_outlier["duration"])

fig = px.histogram(df_final, x="duration", title="HISTOGRAM DOBY VÝPŮJČEK")
fig.update_layout(
    height=700
)
st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.7'></a>", unsafe_allow_html = True)
st.markdown("### 3.7. VÝVOJ POPTÁVKY PRO PŮJČOVÁNÍ KOL V ČASE")
st.markdown("<a id='section3.7.1'></a>", unsafe_allow_html = True)
st.markdown("#### 3.7.1 Vytvoření tabulky pro zkoumání vývoje poptávky")
# Počet výpůjček pro jednotlivé dny
df_date_counts = df_final.groupby("started_date", as_index = False ).count()
df_date_counts = df_date_counts.drop(columns=["start_station_id","duration", "start_station_description", "start_station_latitude", "start_station_longitude", "started_time", "date", "end_station_id", "end_station_name", "end_station_description", "end_station_latitude", 
                                        "end_station_longitude", "ended_date","ended_time", "temp_degree", "feells_degree", "wind_km_h", "gust_km_h", "rain_mm", "humitidy_percent", "cloud_percent", "pressure_mb"])
df_date_counts = df_date_counts.rename(columns={"start_station_name": "count_of_rental"})

# Průměrné hodnoty faktorů počasí pro jednotlivé dny
df_weather_avg = df_final.groupby("started_date", as_index = False ).mean()
df_weather_avg = df_weather_avg.drop(columns=["start_station_id","duration", "start_station_latitude", "start_station_longitude", "end_station_id", "end_station_latitude", 
                                             "end_station_longitude"])

# Finální tabulka vývoje poptávky půjčování kol a její zobrazení
df_development = df_weather_avg.merge(df_date_counts, how = "left", left_on = "started_date", right_on = "started_date" )
df_development["day_of_week"] = df_development["started_date"].dt.dayofweek

st.write("TABULKA PRO ZKOUMÁNÍ VÝVOJE POPTÁVKY")
st.write(df_development)


st.markdown("<a id='section3.7.2'></a>", unsafe_allow_html = True)
st.markdown("#### 3.7.2. Analýza vývoje poptávky")
st.markdown("**Nejdříve si vykreslíme celkový graf vývoje poptávky půjčování kol. Potom si data, kde nám to dovolí, setřídíme podle ročních období a prozkoumáme je. Nakonec se pokusíme udělat nějaké závěry.**")
st.markdown("* Jaro sledujeme v období 2019, 2020, 2021. Rok 2018 data z tohoto období nemá. ")
st.markdown("* Léto sledujeme pouze v letech 2019 a 2020, protože v roce 2021 máme data pouze pro 11 dnů tohoto období, a proto jsme se rozhodli je nezařadit. Data z roku 2018 vůbec nemáme. ")
st.markdown("* Podzim a zimu sledujeme v období 2018, 2019 a 2020. Rok 2021 již tato data neobsahuje.")
st.markdown("**Během jarního období můžeme říci, že:**")
st.markdown("* v roce **2019** se medián pohyboval kolem **306 výpůjček denně** a celkový počet výpůjček byl **32 419**.")
st.markdown("* v roce **2020** se medián pohyboval kolem **620 výpůjček denně** a celkový počet výpůjček byl **66 801**. Tedy jedná se o **106%** nárůst vůči **2019**.")
st.markdown("* v roce **2021** se medián pohyboval kolem **442 výpůjček denně** a celkový počet výpůjček byl **41 604**. Tedy jedná se o **28%** nárůst vůči **2019** a o **38%** pokles vůči roku **2020**.")
st.markdown("**Během letního období můžeme říci, že:**")
st.markdown("* v roce **2019** se medián pohyboval kolem **460 výpůjček denně** a celkový počet výpůjček byl **44 806**.")
st.markdown("* v roce **2020** se medián pohyboval kolem **963 výpůjček denně** a celkový počet výpůjček byl **91 467**. Tedy jedná se o **104%** nárůst vůči **2019**. ")
st.markdown("**Během podzimního období můžeme říci, že:**")
st.markdown("* v roce **2018** se medián pohyboval kolem **132 výpůjček denně** a celkový počet výpůjček byl **11 939**.")
st.markdown("* v roce **2019** se medián pohyboval kolem **364 výpůjček denně** a celkový počet výpůjček byl **32 592**. Tedy jedná se o **173%** nárůst vůči **2018**.")
st.markdown("* v roce **2020** se medián pohyboval kolem **496 výpůjček denně** a celkový počet výpůjček byl **46 452**. Tedy jedná se o **289%** nárůst vůči **2018** a o **42%** nárůst vůči roku **2019**.")
st.markdown("**Během zimního období můžeme říci, že:**")
st.markdown("* v roce **2018** se medián pohyboval kolem **154 výpůjček denně** a celkový počet výpůjček byl **13 933**.")
st.markdown("* v roce **2019** se medián pohyboval kolem **338 výpůjček denně** a celkový počet výpůjček byl **30 861**. Tedy jedná se o **121%** nárůst vůči **2019**.")
st.markdown("* v roce **2020** se medián pohyboval kolem **186 výpůjček denně** a celkový počet výpůjček byl **20 451**. Tedy jedná se o **47%** nárůst vůči **2018** a o **34%** pokles vůči roku **2019**.")
st.markdown("**Závěry:**")
st.markdown("* Zdá se, že podzim, zima 2018 a jaro, léto 2019 je první sezóna firmy Just Eat Cycles v podnikání s výpůjčkou kol. Z toho důvodu toto období budeme brát jako počáteční hodnoty pro srovnání, zda podnikání přináší úspěch, či nikoliv.")
st.markdown("* Když tedy srovnáme data s těmito hodnotami, pak můžeme říci, že podnikání v této oblasti přináší firmě úspěch, protože vždy každý rok došlo k nárůstu výpůjček. ")
st.markdown("* Po zobrazení grafů a jejich prozkoumání můžeme říci, že výjimečné období je podzim 2019 - podzim 2020, kdy došlo k abnormálnímu nárůstu. V podzimním období 2019 o 173%, v zimním období 2019 - 2020 o 121%, v jarním období 2020 o 106%, v letním období 2020 o 104%, v podzimním období 2020 dokonce o 289% vůči počátečním hodnotám. Z toho důvodu bude dobré zjistit, co za takovýmto nárůstem stálo. Je to dáno počasím, nebo úplně jiným faktorem? To se pokusíme zjistit v dalším zkoumání.")
fig = px.line(df_development, x="started_date", y="count_of_rental", title="Celkový vývoj poptávky půjčování kol v Edinburghu")
fig.update_layout(
    height=700
)
st.plotly_chart(fig, use_container_width=True)


df_spring_2019 = df_development.query("started_date >= 20190320 and started_date <= 20190619")
df_spring_2020 = df_development.query("started_date >= 20200320 and started_date <= 20200619")
df_spring_2021 = df_development.query("started_date >= 20210320 and started_date <= 20210619")
print("CELKOVÝ POČET VÝPŮJČEK - JARO 2019:", df_spring_2019["count_of_rental"].sum())
print("CELKOVÝ POČET VÝPŮJČEK - JARO 2020:", df_spring_2020["count_of_rental"].sum())
print("CELKOVÝ POČET VÝPŮJČEK - JARO 2021:", df_spring_2021["count_of_rental"].sum())
print("")
print("VÝPŮJČKY - JARO 2019:")
print(df_spring_2019["count_of_rental"].describe().round(0))
print("")
print("VÝPŮJČKY - JARO 2020:")
print(df_spring_2020["count_of_rental"].describe().round(0))
print("")
print("VÝPŮJČKY - JARO 2021:")
print(df_spring_2021["count_of_rental"].describe().round(0))

date_rng = pd.date_range('2019-03-20', '2021-06-19', freq='1d')
fig = go.Figure()
start = ['2019-03-20','2020-03-20','2021-03-20']
end = ['2019-06-19','2020-06-19','2021-06-19']
years = ['2019','2020','2021']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["count_of_rental"],
                             name=str(years[idx]),
                             mode='lines',
                            ))
fig.add_hline(y=306, line_color="blue", line_dash="dot", annotation_text="medián 2019 = 306x", annotation_position="top left")
fig.add_hline(y=620, line_color="red", line_dash="dot", annotation_text="medián 2020 = 620x", annotation_position="top left")
fig.add_hline(y=442, line_color="green", line_dash="dot", annotation_text="medián 2021 = 442x", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj poptávky půjčování kol v Edinburghu v jarním období", yaxis_title="count_of_rental")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

df_summer_2019 = df_development.query("started_date >= 20190620 and started_date <= 20190921")
df_summer_2020 = df_development.query("started_date >= 20200620 and started_date <= 20200921")
print("CELKOVÝ POČET VÝPŮJČEK - LÉTO 2019:", df_summer_2019["count_of_rental"].sum())
print("CELKOVÝ POČET VÝPŮJČEK - LÉTO 2020:", df_summer_2020["count_of_rental"].sum())
print("")
print("VÝPŮJČKY - LÉTO 2019:")
print(df_summer_2019["count_of_rental"].describe().round(0))
print("")
print("VÝPŮJČKY - LÉTO 2020:")
print(df_summer_2020["count_of_rental"].describe().round(0))

date_rng = pd.date_range('2019-06-20', '2020-09-21', freq='1d')
fig = go.Figure()
start = ['2019-06-20','2020-06-20']
end = ['2019-09-21','2020-09-21']
years = ['2019','2020','2021']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=round(tmp["count_of_rental"]),
                             name=str(years[idx]),
                             mode='lines',
                            ))
fig.add_hline(y=460, line_color="blue", line_dash="dot", annotation_text="medián 2019 = 460x", annotation_position="top left")
fig.add_hline(y=963, line_color="red", line_dash="dot", annotation_text="medián 2020 = 963x", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj poptávky půjčování kol v Edinburghu v letním období", yaxis_title="count_of_rental")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

df_autumn_2018 = df_development.query("started_date >= 20180922 and started_date <= 20181220")
df_autumn_2019 = df_development.query("started_date >= 20190922 and started_date <= 20191220")
df_autumn_2020 = df_development.query("started_date >= 20200922 and started_date <= 20201220")
print("CELKOVÝ POČET VÝPŮJČEK - PODZIM 2018:", df_autumn_2018["count_of_rental"].sum())
print("CELKOVÝ POČET VÝPŮJČEK - PODZIM 2019:", df_autumn_2019["count_of_rental"].sum())
print("CELKOVÝ POČET VÝPŮJČEK - PODZIM 2020:", df_autumn_2020["count_of_rental"].sum())
print("")
print("VÝPŮJČKY - PODZIM 2018:")
print(df_autumn_2018["count_of_rental"].describe().round(0))
print("")
print("VÝPŮJČKY - PODZIM 2019:")
print(df_autumn_2019["count_of_rental"].describe().round(0))
print("")
print("VÝPŮJČKY - PODZIM 2020:")
print(df_autumn_2020["count_of_rental"].describe().round(0))

date_rng = pd.date_range('2018-09-22', '2020-12-20', freq='1d')
fig = go.Figure()
start = ['2018-09-22','2019-09-22','2020-09-22']
end = ['2018-12-20','2019-12-20','2020-12-20']
years = ['2018','2019','2020']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=round(tmp["count_of_rental"]),
                             name=str(years[idx]),
                             mode='lines',
                            ))
fig.add_hline(y=132, line_color="blue", line_dash="dot", annotation_text="medián 2018 = 132x", annotation_position="bottom right")
fig.add_hline(y=364, line_color="red", line_dash="dot", annotation_text="medián 2019 = 364x", annotation_position="top right")
fig.add_hline(y=496, line_color="green", line_dash="dot", annotation_text="medián 2020 = 496x", annotation_position="top right")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj poptávky půjčování kol v Edinburghu v podzimním období", yaxis_title="count_of_rental")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

df_winter_2018 = df_development.query("started_date >= 20181221 and started_date <= 20190319")
df_winter_2019 = df_development.query("started_date >= 20191221 and started_date <= 20200319")
df_winter_2020 = df_development.query("started_date >= 20201221 and started_date <= 20210319")
print("CELKOVÝ POČET VÝPŮJČEK - ZIMA 2018:", df_winter_2018["count_of_rental"].sum())
print("CELKOVÝ POČET VÝPŮJČEK - ZIMA 2019:", df_winter_2019["count_of_rental"].sum())
print("CELKOVÝ POČET VÝPŮJČEK - ZIMA 2020:", df_winter_2020["count_of_rental"].sum())
print("")
print("VÝPŮJČKY - ZIMA 2018:")
print(df_winter_2018["count_of_rental"].describe().round(0))
print("")
print("VÝPŮJČKY - ZIMA 2019:")
print(df_winter_2019["count_of_rental"].describe().round(0))
print("")
print("VÝPŮJČKY - ZIMA 2020:")
print(df_winter_2020["count_of_rental"].describe().round(0))

date_rng = pd.date_range('2018-12-21', '2021-03-21', freq='1d')
fig = go.Figure()
start = ['2018-12-21','2019-12-21','2020-12-21']
end = ['2019-03-19','2020-03-19','2021-03-19']
years = ['2018','2019','2020']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=round(tmp["count_of_rental"]),
                             name=str(years[idx]),
                             mode='lines',
                            ))
fig.add_hline(y=154, line_color="blue", line_dash="dot", annotation_text="medián 2018 = 154x", annotation_position="bottom left")
fig.add_hline(y=338, line_color="red", line_dash="dot", annotation_text="medián 2019 = 338x", annotation_position="top left")
fig.add_hline(y=186, line_color="green", line_dash="dot", annotation_text="medián 2020 = 186x", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj poptávky půjčování kol v Edinburghu v zimním období", yaxis_title="count_of_rental")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.7.3'></a>", unsafe_allow_html = True)
st.markdown("#### 3.7.3. Vliv počasí na výpůjčku kol")
st.markdown("Z finální tabulky df_development jsme se rozhodli z informací o počasí použít pouze tři, podle kterých budeme zjišťovat, zda počasí může mít vliv na počet výpůjček, či nikoliv. Jedná se o pocitovou teplotu, dešťové srážky a oblačnost.")
st.markdown("Nejdříve si pro zajímavost vykreslíme graf, ve kterém budou výpůjčky kol, pocitová teplota, déšť a oblačnost pro sledované období na jednom místě. Jedná se o interaktivní graf, ve kterém se dají zobrazit po kliknutí v legendě pouze hodnoty, které nás zajímají.")
st.markdown("Potom budeme analyzovat jednotlivá roční období a porovnávat průměrné hodnoty v jednotlivých letech, zda mohou mít na počet výpůjček vliv, či nikoliv.")
st.markdown("**Pro jarní období z dostupných dat můžeme říci, že:**")
st.markdown("* rok 2019 byl o 0,39 °C studenější nežli rok 2020.")
st.markdown("* rok 2019 byl deštivější o 0,18mm nežli rok 2020. ")
st.markdown("* rok 2019 měl o 0,2% více oblačnosti nežli rok 2020.")
st.markdown("**Pro letní období z dostupných dat můžeme říci, že:**")
st.markdown("* rok 2019 byl o 0,97 °C teplejší nežli rok 2020.")
st.markdown("* rok 2019 měl o 0,03mm méně srážek nežli rok 2020. ")
st.markdown("* rok 2019 měl o 4,01% méně oblačnosti nežli rok 2020.")
st.markdown("**Pro podzimní období z dostupných dat můžeme říci, že:**")
st.markdown("* rok 2018 byl o 0,83 °C teplejší nežli rok 2019.")
st.markdown("* rok 2018 měl o 0,37mm méně srážek nežli rok 2019. ")
st.markdown("* rok 2018 měl o 12,28% méně oblačnosti nežli rok 2019.")
st.markdown("**Pro zimní období z dostupných dat můžeme říci, že:**")
st.markdown("* rok 2018 byl o 0,98 °C teplejší nežli rok 2019.")
st.markdown("* rok 2018 měl o 0,28mm méně srážek nežli rok 2019. ")
st.markdown("* rok 2018 měl o 6,3% méně oblačnosti nežli rok 2019.")
st.markdown("**Závěr:**")
st.markdown("Pokud budeme nyní srovnávat medián výpůjček s jednotlivými ročními obdobími, můžeme říci, že počasí nemá vliv na počet výpůjček ve sledovaném období. Sice pro jarní období je rok 2020 příznivější nežli rok 2019, ale rozdíly jsou z našeho pohledu zanedbatelné a nemohou mít vliv na takové navýšení poptávky. V letním období je rok 2019 trochu příznivější nežli rok 2020, a přesto nemá více poptávky nežli rok 2020. Podobně to platí pro podzimní a zimní období, kdy rok 2018 je, co do počasí na tom lepší, nežli rok 2019, ale také to nemá vliv na poptávku.")
st.markdown("Co tedy stojí za takovým navýšením v roce 2020? Stejně jako nás, tak i Skotsko zasáhla vlna COVID19 a práve v roce 2020 proběhlo i v Edinburghu několik [lockdownů](https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_Scotland_(2020)). A z našeho pohledu je toto oním faktorem, který stojí za tak velkým nárůstem výpůjček v roce 2020, kdy lidé hledali možnosti, jak nebýt stále doma a zároveň být alespoň trochu aktivní. ")

fig = go.Figure()
# Add traces
fig.add_trace(go.Scatter(x= df_development["started_date"], y=df_development["count_of_rental"], name="půjčeno"))
fig.add_trace(go.Scatter(x=df_development['started_date'], y=df_development["feells_degree"], name="°C",
    yaxis="y2"))
fig.add_trace(go.Scatter(x=df_development['started_date'], y=df_development["rain_mm"], name="mm",
    yaxis="y3"
))
fig.add_trace(go.Scatter(x=df_development['started_date'], y=df_development["cloud_percent"], name="%",
    yaxis="y4"
))


# Create axis objects
fig.update_layout(
    xaxis=dict(
        title="Datum"
    ),
    yaxis=dict(
        title="<b>počet výpůjček</b>",
        titlefont=dict(
            color="#1f77b4"
        ),
        tickfont=dict(
            color="#1f77b4"
        )
    ),
    yaxis2=dict(
        title="<b>pocitová teplota °C</b>",
        titlefont=dict(
            color="orange"
        ),
        tickfont=dict(
            color="orange"
        ),
        anchor="free",
        overlaying="y",
        side="left",
        position=0.0
    ),
    yaxis3=dict(
        title="<b>srážky mm</b>",
        titlefont=dict(
            color="green"
        ),
        tickfont=dict(
            color="green"
        ),
        anchor="x",
        overlaying="y",
        side="right"
        
    ),
    yaxis4=dict(
        title="<b>oblačnost %</b>",
        titlefont=dict(
            color="#9467bd"
        ),
        tickfont=dict(
            color="#9467bd"
        ),
        anchor="free",
        overlaying="y",
        side="right",
        position=0.93
    )
)

# Update layout properties
fig.update_layout(
    title_text="Vývoj poptávky půjčování kol v Edinburghu v závislosti na počasí",
    height = 800,
    hovermode='x unified'
)

st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.7.3.1'></a>", unsafe_allow_html = True)
st.markdown("#### 3.7.3.1 Analýza jarního období")
print("POCITOVÁ TEPLOTA - JARO 2019:")
print(df_spring_2019["feells_degree"].describe().round(2))
print("")
print("POCITOVÁ TEPLOTA - JARO 2020:")
print(df_spring_2020["feells_degree"].describe().round(2))
print("")
print("SRÁŽKY - JARO 2019:")
print(df_spring_2019["rain_mm"].describe().round(2))
print("")
print("SRÁŽKY - JARO 2020:")
print(df_spring_2020["rain_mm"].describe().round(2))
print("")
print("OBLAČNOST - JARO 2019:")
print(df_spring_2019["cloud_percent"].describe().round(2))
print("")
print("OBLAČNOST - JARO 2020:")
print(df_spring_2020["cloud_percent"].describe().round(2))
print("")

date_rng = pd.date_range('2019-03-20', '2020-06-19', freq='1d')
fig = go.Figure()
start = ['2019-03-20','2020-03-20']
end = ['2019-06-19','2020-06-19']
years = ['2019','2020']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["feells_degree"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=7.59, line_color="blue", line_dash="dot", annotation_text="průměr teploty 2019 = 7.59 °C", annotation_position="bottom left")
fig.add_hline(y=7.98, line_color="red", line_dash="dot", annotation_text="průměr teploty 2020 = 7.98 °C", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj pocitové teploty v Edinburghu v jarním období", yaxis_title="Teplota [°C]")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

date_rng = pd.date_range('2019-03-20', '2020-06-19', freq='1d')
fig = go.Figure()
start = ['2019-03-20','2020-03-20']
end = ['2019-06-19','2020-06-19']
years = ['2019','2020']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["rain_mm"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=0.36, line_color="blue", line_dash="dot", annotation_text="průměr srážek 2019 = 0.36 mm/h", annotation_position="top left")
fig.add_hline(y=0.18, line_color="red", line_dash="dot", annotation_text="průměr srážek 2020 = 0.18 mm/h", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj dešťových srážek v Edinburghu v jarním období", yaxis_title="Déšť [mm]")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

date_rng = pd.date_range('2019-03-20', '2020-06-19', freq='1d')
fig = go.Figure()
start = ['2019-03-20','2020-03-20']
end = ['2019-06-19','2020-06-19']
years = ['2019','2020']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["cloud_percent"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=56.05, line_color="blue", line_dash="dot", annotation_text="průměr oblačnosti 2019 = 56.05%", annotation_position="top left")
fig.add_hline(y=55.85, line_color="red", line_dash="dot", annotation_text="průměr oblačnosti 2020 = 55.85%", annotation_position="bottom left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj oblačnosti v Edinburghu v jarním období", yaxis_title="Oblačnost [%]")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.7.3.2'></a>", unsafe_allow_html = True)
st.markdown("#### 3.7.3.2 Analýza letního období")
print("POCITOVÁ TEPLOTA - LÉTO 2019:")
print(df_summer_2019["feells_degree"].describe().round(2))
print("")
print("POCITOVÁ TEPLOTA - LÉTO 2020:")
print(df_summer_2020["feells_degree"].describe().round(2))
print("")
print("SRÁŽKY - LÉTO 2019:")
print(df_summer_2019["rain_mm"].describe().round(2))
print("")
print("SRÁŽKY - LÉTO 2020:")
print(df_summer_2020["rain_mm"].describe().round(2))
print("")
print("OBLAČNOST - LÉTO 2019:")
print(df_summer_2019["cloud_percent"].describe().round(2))
print("")
print("OBLAČNOST - LÉTO 2020:")
print(df_summer_2020["cloud_percent"].describe().round(2))
print("")

date_rng = pd.date_range('2019-06-20', '2020-09-21', freq='1d')
fig = go.Figure()
start = ['2019-06-20','2020-06-20']
end = ['2019-09-21','2020-09-21']
years = ['2019','2020']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["feells_degree"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=13.98, line_color="blue", line_dash="dot", annotation_text="průměr teploty 2019 = 13.98 °C", annotation_position="top left")
fig.add_hline(y=13.01, line_color="red", line_dash="dot", annotation_text="průměr teploty 2020 = 13.01 °C", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj pocitové teploty v Edinburghu v letním období", yaxis_title="Teplota [°C]")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

date_rng = pd.date_range('2019-06-20', '2020-09-21', freq='1d')
fig = go.Figure()
start = ['2019-06-20','2020-06-20']
end = ['2019-09-21','2020-09-21']
years = ['2019','2020']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["rain_mm"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=0.57, line_color="blue", line_dash="dot", annotation_text="průměr srážek 2019 = 0.57 mm/h", annotation_position="bottom left")
fig.add_hline(y=0.60, line_color="red", line_dash="dot", annotation_text="průměr srážek 2020 = 0.60 mm/h", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj dešťových srážek v Edinburghu v letním období", yaxis_title="Déšť [mm]")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

date_rng = pd.date_range('2019-06-20', '2020-09-21', freq='1d')
fig = go.Figure()
start = ['2019-06-20','2020-06-20']
end = ['2019-09-21','2020-09-21']
years = ['2019','2020']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["cloud_percent"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=62.63, line_color="blue", line_dash="dot", annotation_text="průměr oblačnosti 2019 = 62.63%", annotation_position="bottom left")
fig.add_hline(y=66.64, line_color="red", line_dash="dot", annotation_text="průměr oblačnosti 2020 = 66.64%", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj oblačnosti v Edinburghu v letním období", yaxis_title="Oblačnost [%]")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.7.3.3'></a>", unsafe_allow_html = True)
st.markdown("#### 3.7.3.3 Analýza podzimního období")
print("POCITOVÁ TEPLOTA - PODZIM 2018:")
print(df_autumn_2018["feells_degree"].describe().round(2))
print("")
print("POCITOVÁ TEPLOTA - PODZIM 2019:")
print(df_autumn_2019["feells_degree"].describe().round(2))
print("")
print("SRÁŽKY - PODZIM 2018:")
print(df_autumn_2018["rain_mm"].describe().round(2))
print("")
print("SRÁŽKY - PODZIM 2019:")
print(df_autumn_2019["rain_mm"].describe().round(2))
print("")
print("OBLAČNOST - PODZIM 2018:")
print(df_autumn_2018["cloud_percent"].describe().round(2))
print("")
print("OBLAČNOST - PODZIM 2019:")
print(df_autumn_2019["cloud_percent"].describe().round(2))
print("")

date_rng = pd.date_range('2018-09-22', '2019-12-20', freq='1d')
fig = go.Figure()
start = ['2018-09-22','2019-09-22']
end = ['2018-12-20','2019-12-20']
years = ['2018','2019']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["feells_degree"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=5.39, line_color="blue", line_dash="dot", annotation_text="průměr teploty 2018 = 5.39 °C", annotation_position="top left")
fig.add_hline(y=4.56, line_color="red", line_dash="dot", annotation_text="průměr teploty 2019 = 4.56 °C", annotation_position="bottom left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj pocitové teploty v Edinburghu v podzimním období", yaxis_title="Teplota [°C]")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

date_rng = pd.date_range('2018-09-22', '2019-12-20', freq='1d')
fig = go.Figure()
start = ['2018-09-22','2019-09-22']
end = ['2018-12-20','2019-12-20']
years = ['2018','2019']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["rain_mm"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=0.09, line_color="blue", line_dash="dot", annotation_text="průměr srážek 2018 = 0.09 mm/h", annotation_position="bottom left")
fig.add_hline(y=0.46, line_color="red", line_dash="dot", annotation_text="průměr srážek 2019 = 0.46 mm/h", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj dešťových srážek v Edinburghu v podzimním období", yaxis_title="Déšť [mm]")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

date_rng = pd.date_range('2018-09-22', '2019-12-20', freq='1d')
fig = go.Figure()
start = ['2018-09-22','2019-09-22']
end = ['2018-12-20','2019-12-20']
years = ['2018','2019']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["cloud_percent"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=53.84, line_color="blue", line_dash="dot", annotation_text="průměr oblačnosti 2018 = 53.84%", annotation_position="bottom left")
fig.add_hline(y=66.12, line_color="red", line_dash="dot", annotation_text="průměr oblačnosti 2019 = 66.12%", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj oblačnosti v Edinburghu v podzimním období", yaxis_title="Oblačnost [%]")
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.7.3.4'></a>", unsafe_allow_html = True)
st.markdown("#### 3.7.3.4 Analýza zimního období")
print("POCITOVÁ TEPLOTA - ZIMA 2018:")
print(df_winter_2018["feells_degree"].describe().round(2))
print("")
print("POCITOVÁ TEPLOTA - ZIMA 2019:")
print(df_winter_2019["feells_degree"].describe().round(2))
print("")
print("SRÁŽKY - ZIMA 2018:")
print(df_winter_2018["rain_mm"].describe().round(2))
print("")
print("SRÁŽKY - ZIMA 2019:")
print(df_winter_2019["rain_mm"].describe().round(2))
print("")
print("OBLAČNOST - ZIMA 2018:")
print(df_winter_2018["cloud_percent"].describe().round(2))
print("")
print("OBLAČNOST - ZIMA 2019:")
print(df_winter_2019["cloud_percent"].describe().round(2))
print("")

date_rng = pd.date_range('2018-12-21', '2020-03-21', freq='1d')
fig = go.Figure()
start = ['2018-12-21','2019-12-21']
end = ['2019-03-21','2020-03-21']
years = ['2018','2019']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["feells_degree"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=2.58, line_color="blue", line_dash="dot", annotation_text="průměr teploty 2018 = 2.58 °C", annotation_position="top left")
fig.add_hline(y=1.60, line_color="red", line_dash="dot", annotation_text="průměr teploty 2019 = 1.60 °C", annotation_position="bottom left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj pocitové teploty v Edinburghu v zimním období", yaxis_title="Teplota [°C]",)
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

date_rng = pd.date_range('2018-12-21', '2020-03-21', freq='1d')
fig = go.Figure()
start = ['2018-12-21','2019-12-21']
end = ['2019-03-21','2020-03-21']
years = ['2018','2019']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["rain_mm"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=0.29, line_color="blue", line_dash="dot", annotation_text="průměr srážek 2018 = 0.29 mm/h", annotation_position="bottom left")
fig.add_hline(y=0.57, line_color="red", line_dash="dot", annotation_text="průměr srážek 2019 = 0.57 mm/h", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj dešťových srážek v Edinburghu v zimním období", yaxis_title="Déšť [mm]",)
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)

date_rng = pd.date_range('2018-12-21', '2020-03-21', freq='1d')
fig = go.Figure()
start = ['2018-12-21','2019-12-21']
end = ['2019-03-21','2020-03-21']
years = ['2018','2019']
for idx, (s,e) in enumerate(zip(start, end)):
    tmp = df_development[(df_development["started_date"] >= start[idx]) & (df_development["started_date"] <= end[idx])]
    fig.add_trace(go.Scatter(x=date_rng,
                             y=tmp["cloud_percent"],
                             name=str(years[idx]),
                             mode='lines',
                             opacity=0.65,
                             
                            ))
fig.add_hline(y=57.79, line_color="blue", line_dash="dot", annotation_text="průměr oblačnosti 2018 = 57.79%", annotation_position="bottom left")
fig.add_hline(y=64.09, line_color="red", line_dash="dot", annotation_text="průměr oblačnosti 2019 = 64.09%", annotation_position="top left")
fig.update_layout(height=700, xaxis_tickformat='%d-%b', hovermode='x unified', title_text="Vývoj oblačnosti v Edinburghu v zimním období", yaxis_title="Oblačnost [%]",)
fig.update_xaxes(type='date')
st.plotly_chart(fig, use_container_width=True)


st.markdown("<a id='section3.7.4'></a>", unsafe_allow_html = True)
st.markdown("#### 3.7.4. Srovnání počtu výpůjček kol o víkendu a během pracovního týdne")
st.markdown("Ještě jsme chtěli zjistit, zda si lidé půjčují více kol o víkendu, nebo během pracovního týdne. K tomu jsme si vytvořili dvě tabulky **DF_WEEKEND** a **DF_WEEK**, které vycházejí z tabulky **DF_DEVELOPMENT**. Následně jsme si vypočítali průměrný počet výpůjček v obou obdobích.")
st.markdown("**Závěr**")
st.markdown("Během každého víkendového dne proběhlo průměrně **472 výpůjček**. Během pracovního týdne proběhlo každý pracovní den **413 výpůjček**. Na základě tohoto výsledku můžeme říci, že o víkendech si lidé půjčují více kol, než během pracovního týdne. ")
df_weekend = df_development.query("day_of_week > 4")
df_week = df_development.query("day_of_week <= 4")

df_counts_weekend = df_weekend["count_of_rental"].describe().round(0)
df_counts_week = df_week["count_of_rental"].describe().round(0)

st.write("VÝPŮJČKY BĚHEM VÍKENDU")
st.write(df_counts_weekend)
st.write("")
st.write("VÝPŮJČKY BĚHEM PRACOVNÍHO TÝDNE")
st.write(df_counts_week)


st.markdown("<a id='section3.7.5'></a>", unsafe_allow_html = True)
st.markdown("#### 3.7.5. Vývoj výpůjček a vrácení kol v jednotlivých stanicích")
st.markdown("Na závěr projektu ještě nabízíme možnost sledovat vývoj výpůjček, nebo vrácení kol v jednotlivých stanicích pomocí grafu.")
# Příprava tabulky pro zobrazení
station_name = sorted(station_name) # Použití seznamu jedinečných stanic z 3.3.1.
df_start_station_counts = df_bikes.groupby(["start_station_name","started_date"], as_index = False).count()
df_start_station_counts = df_start_station_counts.rename(columns={"duration": "counts"})
df_start_station_counts = df_start_station_counts[["start_station_name","started_date","counts"]]

fig=go.Figure()

station_plot_names = []
buttons=[]

default_state = "Abbeyhill"

for station in station_name:
    df_station_name = df_start_station_counts[(df_start_station_counts["start_station_name"]==station)]
    fig.add_trace(go.Scatter(x=df_station_name["started_date"], y=df_station_name["counts"], visible=(station==default_state )))
    station_plot_names.extend([station])
    
for station in station_name:
    buttons.append(dict(method='update',
                        label=station,
                        args = [{'visible': [station==r for r in station_plot_names]}]))

# Add dropdown menus to the figure
fig.update_layout(height=800, title_text="Vývoj výpůjček kol v jednotlivých stanicích", yaxis_title="Počet výpůjček", 
                  showlegend=False, updatemenus=[{"buttons": buttons, "direction": "down", "active": station_name.index(default_state), 
                  "showactive": True, "x": 0.8, "y": 1.15}])
st.plotly_chart(fig, use_container_width=True)

# Příprava tabulky pro zobrazení
station_name = sorted(station_name)
df_end_station_counts = df_bikes.groupby(["end_station_name","ended_date"], as_index = False).count()
df_end_station_counts = df_end_station_counts.rename(columns={"duration": "counts"})
df_end_station_counts = df_end_station_counts[["end_station_name","ended_date","counts"]]

fig=go.Figure()

station_plot_names = []
buttons=[]

default_state = "Abbeyhill"

for station in station_name:
    df_station_name = df_end_station_counts[(df_end_station_counts["end_station_name"]==station)]
    fig.add_trace(go.Scatter(x=df_station_name["ended_date"], y=df_station_name["counts"], visible=(station==default_state)))
    station_plot_names.extend([station])
    
for station in station_name:
    buttons.append(dict(method='update',
                        label=station,
                        args = [{'visible': [station==r for r in station_plot_names]}]))

# Add dropdown menus to the figure
fig.update_layout(height=800, title_text="Vývoj počtu vrácení v jednotlivých stanicích", yaxis_title="Počet výpůjček", 
                  showlegend=False, updatemenus=[{"buttons": buttons, "direction": "down", "active": station_name.index(default_state), 
                  "showactive": True, "x": 0.8, "y": 1.15}])
st.plotly_chart(fig, use_container_width=True)
