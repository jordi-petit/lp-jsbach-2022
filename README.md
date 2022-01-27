# El llenguatge de programació JSBach

Aquesta pàgina descriu la segona pràctica de GEI-LP (edició 2021-2022 Q2). La vostra tasca és implementar un intèrpret per a un llenguatge de programació anomenat JSBach. La sortida d'aquest intèrpret serà una partitura i un fitxer midi que reproduirà la melodia escrita pel programador.

![JSBach](bach.png)


## Bach

Johann Sebastian Bach (1685-1750) fou un organista i compositor de música barroca. La seva fecunda obra es considera el cim de la música barroca, i una de les màximes expressions de la música universal, no tan sols per la seva profunditat intel·lectual, la seva perfecció tècnica i la seva bellesa artística, sinó també per la síntesi dels diversos estils de la seva època, del passat i per la seva incomparable extensió.


## Presentació del llenguatge JSBach

JSBach és un llenguatge de programació destinat a la composició algorísmica. Amb JSBach s'utilitzen construccions per generar composicions que donen lloc a partitures que poden ser desades en format PDF, MIDI i/o WAV.

JSBach és un llenguatge imperatiu, amb una sintàxi que, evidentment, és barroca.

Aquest és el *Hello Bach*:

```
~ Petit programa en JSBach ~

main |:
    <!> "Hello Bach"
    <:> [B, A, C]
:|
```

Els comentaris es troben dins de titlles (`~`).

Els programes es troben constituïts per procediments.
Cada procediment té un nom, paràmetres (en aquest exemple no n'hi ha), i un bloc de codi associat. Els blocs es troben inscrits
entre els símbols `|:` i `:|`.

La primera instrucció del programa `<!> "Hello Bach"` és una instrucció d'escriptura (*write*).  La instrucció d'escriptura no és gaire útil per compondre, però és útil per debugar, perquè permet escriure textos (entre dobles cometes), enters i llistes.

La segona instrucció del programa `<:> [B, A, C]` és una instrucció de reproducció (*play*). Aquesta instrucció afegeix la llistes de notes donades a la partitura. Les llistes es donen entre claudàtors amb els seus elements separats per comes. En aquest cas, els elements són les notes músicals `B`, `A` i `C`. JSBach utilitza el sistema de notació musical anglès,
no el sistema de notació musical llatí. Així, aquest programa
genera la melodia SI, LA, DO.

L'execució del programa anterior produïria la sortida del missatge `Hello Bach` per pantalla.
A més, generaria la partitura següent:

![bac](bac.png)

juntament amb aquests fitxers:

- [bac.pdf](bac.pdf)
- [bac.midi](bac.midi)
- [bac.wav](bac.wav)


JSBach permet escriure programes senzills utilitzant enters de forma semblant als LPs habituals. Per exemple, el següent programa mostra com llegir dos nombres i calcular el seu màxim comú divisor utilitzant l'algorisme d'Euclides amb dos procediments i entrada/sortida:

```
~ programa llegeix dos enters i n'escriu el seu maxim comu divisor ~

main() |:
    <!> "Escriu dos nombres"
    <?> a
    <?> b
    <?> "El seu MCD es"
    euclides a b
}

euclides a b |:
    while a /= b |:
        if (a > b) |:
            a <- a - b
        :||:
            b <- b - a
        :|
    :|
    <!> a
}
```

Les variables són locals a cada invocació de cada procediment i els procediments es poden comunicar a través de paràmetres. Els procediments llisten els noms dels seus paràmetres formals, però no inclouen els seus tipus. Els paràmetres formals es separen amb blancs, com en Haskell.

Les variables no han de ser declarades, i poden ser de tipus enter o llistes. Les notes músicals, es veurà més endavant, no són altra cosa que constants per a enters.

Com es veu a l'exemple, la sintaxi per llegir i escriure és utilitzant `<?>` i `<!>` respectivament. Les instruccions no es separen ni acaben amb punts i comes superflus. L'operador de diferència és com a Haskell: `/=`.  L'assignació es fa amb la instrucció `<-`. El símbol `:||:` és l'`else` de JSBach.

Com no podia ser d'altra manera, el llenguatge de programació JSBach compta amb recursivitat. Aquest programa mostra com solucionar el problema de les Torres de Hanoi:

```
main() |:
    <?> n
    hanoi n 1 2 3
:|

hanoi n ori dst aux |:
    if n > 0 |:
        hanoi (n - 1) ori aux dst
        <!> ori "->" dst
        hanoi (n - 1) aux dst ori
    :|
:|
```

Amb l'entrada `3` la sortida és:

```
1 -> 2
1 -> 3
2 -> 3
1 -> 2
3 -> 1
3 -> 2
1 -> 2
```

Però, perquè quedar-se amb un mer llistat dels moviments? El programa següent compon una agradable melodia amb el  so dels discos movent-se, tot tocant la nota que es correspon al disc que es mou a cada pas:

```
main |:
    src <- [C, D, E, F, G]
    dst <- []
    aux <- []
    hanoi #src src dst aux
:|

hanoi n src dst aux |:
    if n > 0 |:
        hanoi (n - 1) src aux dst
        note <- src!
        dst << note
        <:> note
        hanoi (n - 1) aux dst src
    :|
:|
```

La partitura que es correspon en aquest programa és:

IMATGE

i aquí la podeu sentir:

MUSICA  

Cnviant o afegint més notes al piu d'orígen es poden compondre noves peces, ben agradables de sentir!

Al programa anterior es poden veure més operacions  per a llistes: `x <- l!` elimina el darrer element  de la llista `l` i el deixa en `x`,  `l <- x` afageix l'element `x` al final de la llista `l`  i `#l` retorna la llargada de la llista `l`.




# La vostra feina

La vostra feina consisteix en
implementar un intèrpret de JSBach.

Per realitzar la vostra feina heu d'utilitzar Python3 i ANTLR4, tal com s'ha explicat a les classes de laboratori. Per generar les partitures, heu d'utilitzar el programa Lilipond.

>>> HE ARRIBAT FINS AQUÍ


# Especificació de JSBach

Les instruccions de JSBach són:

- l'assignació amb `=`,
- la lectura amb `read()`,
- l'escriptura amb `write()`,
- el condicional amb `if` i potser `else`,
- la iteració amb `while`,
- la iteració amb `for`,
- la invocació a un procediment i,
- instruccions d'accés a taules (*arrays*).

Les instruccions escrites una rera l'altra s'executen seqüencialment.


## Assignació

L'assignació ha d'avaluar primer l'expressió a la part dreta del `=` i emmagatzemar després el resultat a la variable local a la part esquerra. Exemple: `a = a - b`. En el cas d'assignar taules, cal copiar els valors (sense fer aliasing).


## Lectura

La instrucció de lectura ha de llegir un valor enter del canal d'entrada estàndard i enmagatzemar-lo a la variable dins del `read()`. Exemple: `read(x)`.


## Escriptura

La instrucció d'escriptura ha d'avaluar l'expressió dins del `write` i escriure-la, en una línia, al canal de sortida estàndard. Exemple: `write(x)`. En el cas d'escriure una taula, cal escriure tots els seus valors entre claudàtors i separats per comes. `write()` pot contenir diversos paràmetres, cal escriure cadascun d'ells a la mateix línia, separats per espais. Els paràmetres poden contenir textos (tancats entre cometes dobles, que apropen més el creient a Déu que les cometes simples).


## Condicional

La instrucció condicional té la semàntica habitual. El bloc `else` és optatiu. Exemples: `if (x == y) {z = 1}` i `if (x == y) {z = 1} else { z := 2 }`. Fixeu-vos que les claus dels blocs sempre són obligatòries (tant als condicions com als procediments, els `while`s i els `for`s).


## Iteració amb `while`

La instrucció iterativa amb `while` té la semàntica habitual.
Exemple: `while (a > 0) { a = a / 2 }`.


## Iteració amb `for`

La instrucció iterativa amb `for` té la semàntica habitual en C.
Exemple: `for (i = 1; i <= n; i = i + 1) { write(i * 10) }`.


## Invocació de procediment

La crida a un procediment té la semàntica habitual.  Els paràmetres enters es passen
per valor, avaluant les expressions dels paràmetres d'esquerra a dreta. Les taules
es passen per referència.
Si el nombre de paràmetres passats
no corresponen als declarats, es produeix un error. Els procediments no són
funcions i no poden retornar resultats. Però els procediments es poden cridar
recursivament.
Exemple: `escriu(numero, 2)`.


## Expressions

Si una variable encara no ha rebut cap valor, el seu valor és zero. Els
operadors aritmètics són els habituals (`+`, `-`, `*`, `/`, `%`) i amb la mateixa
prioritat que en C. Evidentment, es poden usar parèntesis. El
operadors relacionals (`==`, `<>`, `<`, `>`, `<=`, `>=`) retornen zero per
fals i u per cert (Boole és posterior a JSBach). Les taules no es poden operar.


## Taules

La creació de taules es fa amb la paraula clau `array`, que crea en el seu primer paràmetre una taula amb tants enters inicialitzats a zero com indiqui el segon paràmetre. Les taules comencen a l'índex zero. Així, `array(t, n)` crea una taula `[0..n-1]` amb `n` zeros. La consulta d'una taula es fa amb un `get`: `get(t, i)` retorna el valor a la posició `i` de la taula `t`. Igualment, la modificació d'una posició d'una taula es fa amb un `set`: `set(t, i, x)` fixa a `x` el valor a la posició `i` de la taula `t`. Les taules es passen per referència.



## Àmbit de visibilitat

No importa l'ordre de declaració dels procediments. Les variables són locals a
cada invocació de cada procediment. No hi ha variables globals ni manera
d'accedir a variables d'altres procediments (només a través dels paràmetres).


## Errors

Malgrat que JSBach és força senzill, els programes poden causar molts errors en temps d'execució. Per aquesta pràctica, només us demanem que detecteu els errors més verosímils (divisió per zero, crida a procediment no definit, repetició de procediment ja definit, nombre de paràmetres incorrectes, noms de paràmetres formals repetits, accés a un índex inesxistent d'una taula...) i que el programa llanci amb una excepció quan es donen. No cal que feu una anàlisi semàntica per errors de tipus entre enters i taules.


## Invocació de l'intèrpret

El vostre intèrpret s'ha d'invocar amb la comanda `python3 llull.py` tot
passant-li com a paràmetre el nom del fitxer que conté el codi font
(l'extensió dels fitxers per programes en JSBach és `.llull`). Per exemple:

```bash
python3 llull.py programa.llull
```

Els programes poden començar des de qualsevol procediment.  Per defecte, es comença pel procediment `main`. Si es vol començar el programa des d'un procediment diferent de `main()`, cal donar el seu nom com a segon paràmetre i es poden passar els valors dels seus paràmetres (només nombres enters) des de la línia de comandes.

```bash
python3 llull.py programa.llull converteix_infidels 10 20
```


## Invocació del *pretty-printer*

El vostre *pretty-printer* (també anomenat *beatificador* per la semblança amb *beautifier*) s'ha d'invocar amb la comanda `python3 beat.py` tot
passant-li com a primer paràmetre el nom del fitxer que conté el codi font a *beatificar*. Per exemple:

```bash
python3 beat.py programa.llull
```

El *pretty-printer* ha de formatar el codi amb unes regles d'estil semblants a les utilitzades en aquest document i amb uns colors agradables. Per exemple, si el programa fos

```
hanoi(n,ori,dst,aux)
|:    # la n és un real negatiu
    if(n>0){hanoi(n-1,ori,aux,dst)write(ori,"->",dst)hanoi(n-1,aux,
        dst, ori
)}}
```

la sortida hauria de ser aquest programa, elegantment formatat per a major glòria del Creador:

```c
hanoi(n, ori, dst, aux) {
|:if (n > 0) {
|:|:hanoi(n - 1, ori, aux, dst)
|:|:write(ori, "->", dst)
|:|:hanoi(n - 1, aux, dst, ori)
|:}
}
```

Fixeu-vos que el *pretty-printer* perd els comentaris, ja que aquests poden amagar la veritat de les Escriptures. També, recordeu que Arnau de Vilanova, mestre de Ramon JSBach, ja va demostrar la necessitat d'indentar amb quatre espais.

Els colors o estils dels elements del programe els podeu escollir vosaltres lliurament. Utiliteu alguna llibreria de Python per escriure en colors al terminal.


## Extensions

Podeu extendre el llenguatge amb construccions del vostre gust, a condició de mantenir una compatibilitat estricta amb l'especificació donada (i ser respectuosos amb la teologia de Ramon JSBach). A més, cal que documenteu amb precisió les vostres extensions i que creeu programes que les provin i posin de manifest la seva utilitat.

Per exemple, podríeu extendre JSBach amb variables i/o constants globals, operadors lògics, funcions que retornin valors, ...

Compte: Les extensions poden portar molta feina, consulteu-ho abans amb el vostre professor.


# Lliurament

Heu de lliurar la vostra pràctica al Racó. Només heu de lliurar un fitxer ZIP
que, al descomprimir-se generi:

- Un fitxer `README.md` que documenti el vostre projecte.
|:- vegeu, per exemple, https://www.makeareadme.com/.

- Un fitxer `requirements.txt` amb les llibreries que utilitza el vostre projecte.
  - vegeu, per exemple, https://pip.pypa.io/en/stable/user_guide/#requirements-files.

- Un fitxer `llull.g4` amb la gramàtica del LP.

- Un fitxer `llull.py` amb el programa de l'intèrpret, incloent els seus visitadors.

- Un fitxer `beat.py` amb el programa del *pretty-printer*, incloent els seus visitadors.

- Si heu fet extensions, podeu afegir fitxers `test-*.llull` com a exemples i jocs de proves.

Els vostres fitxers de codi en Python han de seguir les regles d’estı́l PEP8, tot i que podeu oblidar les restriccions sobre la llargada màxima de les lı́nies. Podeu utilitzar els paquets `pep8` o `autopep8` o http://pep8online.com/ per assegurar-vos que seguiu aquestes regles d’estı́l. L’ús de tabuladors en el codi queda prohibit (zero directe). Els vostres programes en JSBach han de seguir l'estil exposat en aquest document, que demostra bon gust i conformança amb les escriptures lul·lianes (és a dir, passeu-los per beatificador).

El termini de lliurament és el **dilluns 10 de gener a les 23:59**.

Per evitar problemes de còpies,
no pengeu el vostre projecte en repositoris públics.


## Llibreries

Utilitzeu  `ANTLR` per escriure la gramàtica i l'intèrpret. Podeu utilitzar lliurament qualsevol estàndard de Python. A més, podeu utilitzar qualsevol llibreria de Python3 per a escriure en colors, a condició que sigui portable entre sistemes, que s'instal·li amb `pip3` i que aparegui al vostre `requirements.txt`.


# Referències

- ANTLR en Python: https://gebakx.github.io/Python3/compiladors.html#1

- Johann Sebastian Bach: https://ca.wikipedia.org/wiki/Johann_Sebastian_Bach

![Firma](firma.png)
