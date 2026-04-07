# Swagger Editor

## Editor GUI

A [Swagger editor](https://editor.swagger.io/) egy online felület, ahol API leírást lehet olvasni, javítani és kipróbálni. Tesztelőként ez azért hasznos, mert egy helyen látod, mit vár a szolgáltatás és mit ad vissza.

A képernyő általában két részre oszlik. Bal oldalon a leírás szövege látszik, jobb oldalon pedig a kész, emberi nyelven olvasható nézet. Ha bal oldalon módosítasz valamit, jobb oldalon rögtön frissül.

A felületen gyorsan ellenőrizheted, hogy:
- milyen kérés küldhető,
- milyen mezők kötelezők,
- milyen válasz várható,
- milyen hiba történhet rossz adatnál.

Tesztelőként ez jó indulópont a tesztesetek készítéséhez. Nem kell kódot olvasni ahhoz, hogy megértsd a működést. A leírásból ki tudod gyűjteni a jó és a hibás bemeneteket is, majd ezekre egyszerű teszteket készíthetsz.

## SimpleAdder szerkesztése

A [Simple Adder](../adder.yaml) betöltéséhez nyisd meg a fájlt, majd másold ki a teljes tartalmát. Ezután nyisd meg a Swagger editort, és illeszd be a bal oldali szerkesztő részbe.

Ha minden rendben van, a jobb oldali nézet azonnal mutatni fogja az API leírást. Itt ellenőrizd, hogy látható-e a /add végpont, a két bemeneti mező (number1, number2), valamint a válaszok.

Ha hiba van a leírásban, az editor jelzi. Javítás után rögtön látni fogod a friss eredményt.

## SimpleAdder tesztek

A Swagger editor jó eszköz felfedező jellegű tesztelésre is. Ez azt jelenti, hogy előre megírt, hosszú tesztlista nélkül, lépésről lépésre próbálod ki a működést, és közben jegyzetelsz.

Kezdd a legegyszerűbb esettel: number1=2, number2=2. Itt sikeres választ vársz, és a result értéke 4 legyen. Ezután próbálj határhelyzeteket: 0 és 0, negatív számok, tizedes számok.

Utána jöhetnek a hibás próbák:
- hiányzik az egyik mező,
- szöveget küldesz szám helyett,
- üres kérést küldesz.

Ilyenkor hibaüzenetet kell kapnod, jól érthető szöveggel. Ha a válasz nem egyértelmű, azt érdemes feljegyezni.

A felfedező tesztelés végén készíts rövid összegzést:
- mi működött jól,
- hol volt bizonytalan a viselkedés,
- milyen plusz teszt kell még.

Ezzel gyorsan képet kapsz a szolgáltatás minőségéről, és hasznos visszajelzést adsz a fejlesztőknek.
