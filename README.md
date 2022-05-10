# PROJECT-BIKES-IN-EDINBURGH-WITH-PYTHON
Nejprve jsem projekt psal v Jupyter notebooku, který jsem spouštěl pod Anaconda Navigator. Výsledkem je soubor **ProjectPython_Bikes.ipynb**.
Samotný soubor již obsahuje výsledky řešení i bez spouštění kódu. Na základě testování jsem měl někdy potíže při zobrazení mapových podkladů, když jsem scroloval nahoru a zase dolů v notebooku. Ale zdá se, že zde funguje to, když se na mapu najede a kolečkem myši se udělá zoom, pak se mapa znovu vykreslí. Pokud ani to nezafunguje, pak je nejlepší pustit celý kód znovu.

Vytvořený Jupyter notebook se v GitHubu nezobrazí, protože je již příliš veliký a složitý na vykreslování. Notebook doporučuji stáhnout do svého PC. 

Pokud byste ho chtěli znovu spustit i s kódem budete potřebovat dva zdrojové soubory dat. Zdrojový soubor dat edinburgh_bikes.csv má velikost 101,5MB. Pro uložení tak velikých souborů na GitHub je trochu problém, protože se normálně podporují soubory do 25MB. Pak existuje možnost použít Git Large File Storage (LFS), kterou jsem zkusil, ale bohužel při načtení a spuštění kódu vše nefungovalo správně. Z toho důvodu nabízím stažení zdrojových souborů dat z mého GoogleDisku: https://drive.google.com/drive/folders/1llNX4zMyeBPNW9_uBPvPGbhy_8fVPJig?usp=sharing

Později jsem si chtěl ještě vyzkoušet prezentovat projekt pomocí webového rozhraní přes knihovnu Streamlit. Musím říci, že mě uchvátila, protože člověk nemusí stahovat žádný notebook, ale rovnou se podívat na výsledek na webu. 

# OBSAH PROJEKTU
## 1. ZADÁNÍ PROJEKTU
## 2. ÚPRAVA DAT PRO DATOVOU ANALÝZU
### 2.1. SOUBOR EDINBURGH_BIKES.CSV
#### 2.1.1. Základní informace o získaných datech
#### 2.1.2. Úprava datových typů
#### 2.1.3. Analýza chybějících údajů
### 2.2. SOUBOR EDINBURG_WEATHER.CSV
#### 2.2.1. Načtení souboru s převedením sloupce date na datový typ datetime
#### 2.2.2. Základní informace o získaných datech
#### 2.2.3. Úprava datových typů
#### 2.2.4. Analýza chybějících údajů
#### 2.2.5. Vytvoření průměrných hodnot na jednotlivé dny
#### 2.2.6. Spojení upravených tabulek do jedné
## 3. DATOVÁ ANALÝZA - VÝPŮJČKY KOL V EDINBURGHU
### 3.1. VYTVOŘENÍ JEDINEČNÝCH STANIC POUŽÍVANÝCH PRO VÝPŮJČKU NEBO VRÁCENÍ
### 3.2. VÝPOČET VZDÁLENOSTÍ MEZI JEDNOTLIVÝMI STANICEMI VZDUŠNOU ČAROU
### 3.3. STANICE PRO VÝPŮJČKU KOL
#### 3.3.1. Vytvoření tabulky s jedinečnými stanicemi pro výpůjčku kol
#### 3.3.2. Deskriptivní statistika
#### 3.3.3. Histogram pro stanice výpůjček kol
#### 3.3.4. Neaktivní stanice pro výpůjčku kol
#### 3.3.5. Aktivní stanice pro výpůjčku kol
#### 3.3.6. Nejčastěji používané stanice - TOP 10
### 3.4. STANICE PRO VRÁCENÍ KOL
#### 3.4.1. Vytvoření tabulky s jedinečnými stanicemi pro vrácení kol
#### 3.4.2. Deskriptivní statistika
#### 3.4.3. Histogram pro stanice, kam se kola vracejí
#### 3.4.4. Neaktivní stanice pro vrácení kol
#### 3.4.5. Aktivní stanice pro vrácení kol
#### 3.4.6. Nejčastěji používané stanice - TOP 10
### 3.5. STANICE, NA KTERÝCH SE KOLA HROMADÍ, NEBO CHYBÍ
#### 3.5.1. Vytvoření tabulky, která srovnává počet výskytů pro půjčku a vrácení u jednotlivých stanic
#### 3.5.2. Výsledné tabulky
### 3.6. ANALÝZA DOBY VÝPŮJČKY
#### 3.6.1. Deskriptivní statistika
#### 3.6.2. Histogram doby výpůjček
### 3.7. VÝVOJ POPTÁVKY PRO PŮJČOVÁNÍ KOL V ČASE
#### 3.7.1. Vytvoření tabulky pro zkoumání vývoje poptávky
#### 3.7.2. Analýza vývoje poptávky
#### 3.7.3. Vliv počasí na výpůjčku kol
##### 3.7.3.1. Analýza jarního období
##### 3.7.3.2. Analýza letního období
##### 3.7.3.3. Analýza podzimního období
##### 3.7.3.4. Analýza zimního období
#### 3.7.4. Srovnání počtu výpůjček kol o víkendu a během pracovního týdne
