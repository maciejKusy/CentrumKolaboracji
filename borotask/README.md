## requiraments
node v15.x.x - najlepiej uzywac nvm, to libka do zarzadzania wersjami node
npm          - najlepiej uzywac npx, to libka do zarzadzania wersjami npm :D

## install repo
```
npm install
```

## run test
```
npm test
```

Elo, mam wyzwanie. Kilka zadan, zrobionych krok po kroku, zeby pokazac pewno metode rozumowania i domenowego rozbijania kodu. 
Sam kod jest pisany na kolenie, nim sie nie sugeruj - na pewno daloby sie to napisac lepiej, rozbic gre na inne czesci. Ale 
zasadniczo nie o to chodzi :P Zakladam ze masz node.js i npm-a, moze to byc bledne zalozenie :D jakbys nie mial to ogarniemy 
to jakos inaczej. No i naturalnie tylko jak Ci sie chce, jak wolisz pracowac nad swoim projektem to tez git. Ale nie powinno Ci 
to zajac duzo czasu.

## task 1
Napisz klase `Model`, zawierającą logikę gry kamień-nozyce-papier która przejdzie testy.
Podstawowa klasa jest juz utworzona, odkomentuj kolejno bloki testów i sprobuj napisać kod, któ©y je przejdzie, itd.

Klasa ma określone metody:
```
class Model {
    random()                        // zwraca randomowy znak
    getSings()                      // zwraca wszystkie znaki
    descSign(sign string)           // zwraca dane znaku
    decide(s1 string, s2 string)    // zwraca wynik rozgrywki
}
```

w `src/const.js` sa stale do wykorzystania do oznaczenia znakow (papier, nozyce, kamien) i wynikow gry dla gracza (wygrana, przegrana, remis).

