# OpenAPI 3.0 tutorial

## YAML

A YAML egy egyszerű, szöveg alapú formátum az adatok leírásához. A név YAML jelent: "YAML nem markup language" - vagyis nem egy markup nyelv, mint a HTML.

Miért jó a YAML? Mert emberek könnyen olvashatnak és írhatnak benne. Nem kell sok apróságra figyelni, mint másfajta formátumok esetén. A YAML fájlok tiszta és érthető szerkezetűek.

A YAML-ban az adatokat behúzással (indentációval) szervezik. Ha valami fontos, azt indentálni kell. Az adatokat kulcs és érték párként írjuk le - például "szín: kék" vagy "port: 8080".

Az API-k leírásához gyakran használnak YAML-t, mert könnyen érthető és egyértelmű.

## OpenAPI 3.0

Az OpenAPI egy szabvány, amely leírja, hogyan működik egy API. Segít tesztelőknek megérteni, mit tud csinálni az API és hogyan kell használni.

Az OpenAPI 3.0 verzió a legújabb szabvány. Jól működik a modern API-kkal. Az OpenAPI leírás tartalmazza azt, hogy:
- Milyen végpontok érhetőek el (például /adder/calculate)
- Milyen adatokat kell beküldeni (input)
- Milyen adatokat kapunk vissza (output)
- Milyen hibák lehetségesek

A tesztelőknek hasznos az OpenAPI, mert egyértelműen láthatják, mit kell tesztelni. Nem kell találgatni. Az API-k tulajdonosai ezzel csak egyszer írják le a rendszert, és mindenki ugyanazt az információt kapja.

OpenAPI-ban a végpontok, adattípusok és válaszok mindegyike részletesen dokumentálva van.

## Swagger editor

A [Swagger editor](https://editor.swagger.io/) egy ingyenes, online eszköz az OpenAPI leírások írásához és teszteléséhez. Itt láthatod szép formában az API dokumentációját.

Az editor előnyei:
- Vizuális szerkesztő: könnyen szerkesztheted az OpenAPI leírásokat
- Valós idejű előnézet: azonnal látod, hogyan néz ki a dokumentáció
- Tesztelhetőségi: közvetlenül az editorban tesztelheted az API-t
- Hibakeresés: ha valami nem jó az OpenAPI leírásban, azonnal megjeleníti

A Swagger editor segít abban, hogy a dokumentáció mindig aktuális és korrekta legyen. Tesztelőknek nagyon jó, mert világosan látható, milyen kéréseket és válaszokat vár az API.
