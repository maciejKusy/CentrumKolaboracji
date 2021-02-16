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

## task 2
Dodalem 3 nowe pliki:
- `main.js` - spina wszystko, tam uruchamia sie gierka, szczegol ktory Cie nie interesuje w ramach zadania,
- `src/consoleView.js` - implementacja widoku gry w consoli nodeowej, w niej interesuja Cie metody:
    - `setChoice(choice)`
    - `addChoiceHandler(onChoice)` - przekazujesz funkcje, odpalana jak user wybierze opcje play i ktorys ze znakow,
    - `addLearnHandler(onLEarn)` - przekazujesz funkcje, odpalana jak user wybierze opcje learn i ktorys ze znakow,
    - `displayResult(stHand, ndHand, status)` - uzywana zeby wyswietlic wynik gryp, dostaje sign usera, sign computera i wynik rozgrywki,
    - `displayDesc(sign, desc)` - uzywana zeby wyswietlic opic signu, dostaje sign + jego opis
  reszta to szczegoly implementacyjne,
- `src/controller.js` - szkielet klasy do zaimplementowania, dla ulatwienia dodalem juz metode inicjujaca bo to musi byc asynchronicznie w tym przypadku,

Co jest do zrobienia:
- zasilic view danymi do wyboru,
- podpiac handler addChoice, w ktorym:
    - przyjmiesz wybor usera,
    - wygenerujesz wybor komputera,
    - porownasz sign,
    - wyswietlisz wynik,
- podpiac handler addLearn, w ktorym
    - przyjmiesz wybor usera
    - wyswietlisz wynik

Przyklad rozgrywki:
1) `? option` -> wybor `play`,
2) `? sign` -> wybor `ROCK`,
3) print w consoli:
    `You chose ROCK and computer choose PAPER`
    `rock loses with paper.`
    `You lose!`

Nie ma do tego testow, trzeba sprawdzic manualnie ;P

**CEL: Sprobuj to zrobic, modyfikujac wylacznie plik `Controller.js`**

### abu uruchomic gre:
```
node main.js
```
mozesz w ramach dodatkowego cwiczenia dodac do package.json skrypt ktory to odpali na `npm start`

### force quit game:
```
ctrl+c
```
w razie pytan pisz :P nie jest to napisane jakos specjalnie dobrze, le nie o to chodzi :D bledy w angielskim tez zignoruj :D

## BONUS

Dodaj jaszczurke i Spocka wg https://en.wikipedia.org/wiki/Rock_paper_scissors -> variations

## Task 3
Dodalem pliki:
- index.html,
- src/script.js - jak main.js, spina wszystko tylko uzywa innego controllera,
- src/browserView.js - controller widoku pod przegladarke

Zadanie: napisz podstawowy widok przegladarkowy, modyfikujac wylacznie `index.html` i `src/browserView.js`, jak dla mnie nie musi byc ostylowane itd. chodzi tylko o to zeby w jakis sposob dzialalo, wyswietlilo byttony i np. gra moze byc po kliknieciu lewym, a learn prawym przyciskiem myszy, z jakims opisem, etc.

przegladarka moze krzyczec lokalnie ze nie pusci tych skryptow, wymaga to zmiany w configu chroma albo puszczenia tego z lokalnego serwera (np. vscode extension live server to ogarnia)