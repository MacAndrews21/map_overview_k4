# map_overview_k4
Creates an map overview for the k4 of berlin  

Das Kartenwerk gliedert sich in __4 Sektoren__ die gegen den  Uhrzeigersinn um den Nullpunkt verlaufen. Das Beispiel beschreibt den Ablauf für die Karten 101. Der Kartenschlüssel deutet sich wie folgt:
1 -> Sektor
0 -> Zeile
1 -> Spalte
Innerhalb einer __Spalte__ und __Zeile__ wird wiederum in die Kartenblätter __1__, __2__, __3__, __4__, __5__, __6__, __7__ und __8__ aufgeteilt.  
![overview](https://github.com/MacAndrews21/map_overview_k4/blob/master/2015-08_02-Doku-K4.png) 
Das Pythonskript verfährt folgendermaßen:

--------------------------------------------------------------
* Vom Nullpunkt ausgehend werden zunächst die Karten 1, 2, 3 und 4 gezeichnet, also es werden nur die X-Werte (left und right) geändert während die Y-Werte (top und bottom) gleich bleiben. Dann werden die Y-Werte um 2400m hochgezählt und die X-Werte starten wieder bei den Ausgangswerten, um die Karten 5, 6, 7 und 8 zu zeichnen.

```
Nullpunkt = 	X: 40.000
		Y: 10.000
Sektor: 1, Zeile: 0, Spalte: 1
Zentrum = 	X: Nullpunkt_X
		Y: Nullpunkt_Y
Kartenblatt 1011 = 	left: Zentrum_X;
			right: Zentrum_X + 1600;
			top: Zentrum_Y + 2400;			
			bottom:Zentrum_Y;
Kartenblatt 1012 = 	left: Zentrum_X + 1600;
			right: Zentrum_X + 1600 * 2;
			top: Zentrum_Y + 2400;			
			bottom:Zentrum_Y; 
Kartenblatt 1013 = 	left: Zentrum_X + 1600 * 2;
			right: Zentrum_X + 1600 * 3;
			top: Zentrum_Y + 2400;
			bottom: Zentrum_Y;
Kartenblatt 1014 = 	left: Zentrum_X + 1600 * 3;
			right: Zentrum_X + 1600 * 4;
			top: Zentrum_Y + 2400;
			bottom: Zentrum;
```

--------------------------------------------------------------
* Im zweiten Schritt wird der Nullpunkt entlang der Y-Achse um 2 * 2400m nach Norden verschoben (In den Sektoren 2 und 3 in Richtung Süden). Die Anzahl der erforderlichen Spalten lassen sich durch min/max-Variablen definieren. Bsp.: min = 101; max = 121; In diesem Fall werden die Zeilen 0, 1 und 2 (101, 111 und 121) innerhalb der ersten Spalte geschrieben. Bei jeder Erhöhung der Y-Koordinate läuft die Schleife aus Schritt 1 durch und zeichnet die acht Kartenblätter.
```
Sektor: 1, Zeile: 0, Spalte: 1
Zentrum = 	X: Nullpunkt; 
		Y: Nullpunkt + 2400 * 2;
Sektor: 1, Zeile: 1, Spalte: 1
Zentrum = 	X: Nullpunkt; 
		Y: Nullpunkt + 2400 * 4;
Sektor: 1, Zeile: 2, Spalte: 1
Zentrum = 	X: Nullpunkt; 
		Y: Nullpunkt + 2400 * 6;
```
--------------------------------------------------------------
* Nach durchlaufen der Zeilen (min/max) wird die X-Koordinaten hochgezählt. Gleichzeitig wird die Y-Koordinate zurückgesetzt.
```
	...	
```
--------------------------------------------------------------
* Ab hier wiederholt sich dann alles. Für jeden Sektor gibt es ein angepasstes vorgehen, da X- bzw. Y-Koordinate entweder hochgezählt oder runtergezählt werden müssen.


