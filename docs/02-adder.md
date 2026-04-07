# SimpleAdder API

## Adder API

[Simple Adder](../adder.yaml) egyszerű OpenAPI leírás.

## Info

Az Info rész az API névjegye. Itt látod a szolgáltatás nevét, a verziót és egy rövid leírást. Ennél a példánál a név Simple Adder Service, a verzió 1.0.0, a leírás pedig azt mondja, hogy a szolgáltatás két számot összead.

Tesztelőként ez azért fontos, mert gyorsan kiderül, jó dokumentumot nézel-e. Ha a verzió eltér, lehet, hogy más viselkedést kapsz. Az Info rész segít abban is, hogy a csapat minden tagja ugyanarra a szolgáltatásra hivatkozzon.

## Servers

A Servers rész mutatja, hol érhető el az API. Ebben a példában ez a cím: http://localhost:5000.

Ez gyakorlásnál nagyon hasznos, mert tudod, hova kell küldeni a kérést. Ha rossz címre küldesz, a teszt hibás lesz akkor is, ha a kérésed jó. Ezért teszt előtt mindig ellenőrizd a szervercímet.

## Paths - 1 

A Paths részben látod, mit tud az API. Egy végpont van: /add, és erre POST kérést küldünk. A rövid összefoglaló szerint a művelet két számot ad össze.

A kérés törzsében két mező kötelező: number1 és number2. Mindkettő szám. Ha bármelyik hiányzik, vagy nem számot küldesz, nem kapsz helyes eredményt. A példák segítenek: 0 + 0 és 2 + 2. Ezek jó kezdő tesztesetek, mert egyszerűen ellenőrizhetők.

## Paths - 2

A válaszok része megmutatja, mit kapsz vissza.

 - `200` esetén a kérés sikeres, és a válaszban a `result` mező tartalmazza az összeget.
 - `400` esetén a bemenet hibás. Ilyenkor hibaüzenetet kapsz, például ha hiányzik egy mező, vagy nem számot adtál meg.
 - `500` esetén váratlan belső hiba történt.

Tesztelőként érdemes mindhárom esetet lefedni. Ne csak a jó utat nézd, hanem a hibás bemenetet is. Így biztos lehetsz benne, hogy a szolgáltatás nemcsak működik, hanem érthető hibát is ad, ha rossz adat érkezik.
