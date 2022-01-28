# El doble intèrpret de JSBach

Aquesta pàgina descriu la segona pràctica de GEI-LP (edició 2021-2022 Q2). La vostra tasca és implementar un doble intèrpret per a un llenguatge de programació musical anomenat JSBach. La sortida d'aquest doble intèrpret serà una partitura i uns fitxers de so que reproduiràn la melodia escrita pel compositor. En diem un *doble* intèrpret perquè funciona en el sentit informàtic (interpreta un programa) i en el sentit musical (interpreta una peça de música).


## Bach

Johann Sebastian Bach (1685-1750) fou un organista i compositor de música barroca. La seva fecunda obra es considera el cim de la música barroca, i una de les màximes expressions de la música universal, no tan sols per la seva profunditat intel·lectual, la seva perfecció tècnica i la seva bellesa artística, sinó també per la síntesi dels diversos estils de la seva època, del passat i per la seva incomparable extensió.

![JSBach](bach.png)



## Presentació del llenguatge JSBach

JSBach és un llenguatge de programació orientat a la composició algorísmica. Amb JSBach s'utilitzen construccions imperatives per generar composicions que donen lloc a partitures que poden ser desades en diferents formats digitals.

JSBach té moltes instruccions habituals, però utilitza una sintàxi que és, evidentment, barroca. Aquest és el *Hallo Bach*:

```
~~~ Kleines Program in JSBach ~~~

haupt |:
    <!> "Hallo Bach"
    <:> [B, A, C]
:|
```

Com podeu veure, els comentaris es troben entre triples titlles (`~~~`). No és necessari escriure els comentaris en alemany, però en Johann ho faria així.

Els programes es troben constituïts per procediments (l'ordre no importa) i comencen pel procediment `haupt` (*principal* en alemany).
Cada procediment té un nom, paràmetres (en aquest exemple no n'hi ha), i un bloc de codi associat. Els blocs es troben inscrits
entre els símbols `|:` i `:|`.

La primera instrucció del programa `<!> "Hallo Bach"` és una instrucció d'escriptura (*write*).  La instrucció d'escriptura no és gaire útil per compondre, però és útil per debugar, perquè permet escriure textos (entre dobles cometes), enters i llistes.

La segona instrucció del programa `<:> [B, A, C]` és una instrucció de reproducció (*play*). Aquesta instrucció afegeix la nota o la llista de notes donades a la partitura. Les llistes es donen entre claudàtors amb els seus elements separats per comes. En aquest cas, els elements són les notes músicals `B`, `A` i `C`. JSBach utilitza el sistema de notació musical anglès,
no el sistema de notació musical llatí ni el germànic. Així, aquest programa
genera la melodia Si, La, Do.

L'execució del programa anterior produïria la sortida del missatge `Hallo Bach` per pantalla.
A més, generaria la partitura següent:

![bac](bac.png)

juntament amb aquests fitxers:

- [🎼 bac.pdf](https://github.com/jordi-petit/lp-jsbach-2022/raw/haupt/bac.pdf)
- [🎹 bac.midi](https://github.com/jordi-petit/lp-jsbach-2022/raw/haupt/bac.midi)
- [🎵 bac.wav](https://github.com/jordi-petit/lp-jsbach-2022/raw/haupt/bac.wav)
- [🎵 bac.mp3](https://github.com/jordi-petit/lp-jsbach-2022/raw/haupt/bac.mp3)

Com es veu, la sortida de l'intèrpret són fitxers PDF, MIDI, WAV i MP3.

JSBach permet escriure programes senzills utilitzant enters de forma semblant als LPs habituals. Per exemple, el programa següent mostra com llegir dos nombres i calcular el seu màxim comú divisor utilitzant l'algorisme d'Euclides amb dos procediments i entrada/sortida:

```
~~~ programa que llegeix dos enters i n'escriu el seu maxim comu divisor ~~~

haupt |:
    <!> "Escriu dos nombres"
    <?> a
    <?> b
    <?> "El seu MCD es"
    <^> euclides a b
:|

euclides a b |:
    während a /= b |:
        wenn a > b |:
            a <- a - b
        :||:
            b <- b - a
        :|
    :|
    <!> a
:|
```

Tots els identificadors en JSBach han de contenir lletres minúscules o subratllats. Les notes sí que s'escriuen en majúscules.

Les variables són locals a cada invocació de cada procediment i els procediments es poden comunicar a través de paràmetres. Els procediments llisten els noms dels seus paràmetres formals, però no inclouen els seus tipus. Els paràmetres es separen amb blancs, ~~com Déu mana~~ com en Haskell.

Les variables no han de ser declarades, i poden ser de tipus enter o llistes. Les notes músicals, es veurà més endavant, no són altra cosa que constants per a enters.

Com es veu a l'exemple, la sintaxi per llegir i escriure és utilitzant `<?>` i `<!>` respectivament. Les crides a procediments comencen amb `<^>`.
L'operador de comparació per igualtat és `=` i per diferència és `/=`.  L'assignació es fa amb la instrucció `<-`.
El `während` és el *while* i el `wenn` el `if`.
El símbol `:||:` és l'`else` de JSBach.

Com no podia ser d'altra manera, el llenguatge de programació JSBach compta amb recursivitat. Aquest programa mostra com solucionar el problema de les Torres de Hanoi:

```
haupt |:
    <?> n
    <^> hanoi n 1 2 3
:|

hanoi n ori dst aux |:
    wenn n > 0 |:
        <^> hanoi (n - 1) ori aux dst
        <!> ori "->" dst
        <^> hanoi (n - 1) aux dst ori
    :|
:|
```

Amb l'entrada `3` la sortida és doncs:

```
1 -> 2
1 -> 3
2 -> 3
1 -> 2
3 -> 1
3 -> 2
1 -> 2
```

Però, perquè quedar-se amb un mer llistat dels moviments? El programa següent compon una agradable melodia seguint el so dels discos movent-se, tot tocant la nota que es correspon al disc que es mou a cada pas:

```
~~~ Notes de Hanoi ~~~

haupt |:
    src <- [C, D, E, F, G]
    dst <- [] |
    aux <- []
    <^> hanoi #src src dst aux
:|

hanoi n src dst aux |:
    wenn n > 0 |:
        <^> hanoi (n - 1) src aux dst
        note <- src[#src]
        8< src[#src]
        dst << note
        <:> note
        <^> hanoi (n - 1) aux dst src
    :|
:|
```

La partitura que es genera en aquest programa és:

IMATGE

i aquí la podeu sentir:

MUSICA  

Canviant o afegint més notes al piu d'orígen es poden compondre noves peces, ben agradables de sentir!

Al programa anterior es poden veure més operacions  per a llistes:

-  `l[i]` consulta l'`i`-èsim element d'una llista `l`.
Com que JSBach és per a músics, els índexs de les llistes comencen per 1.

- `l << x` afegeix l'element `x` al final de la llista `l`.

-  `#l` retorna la llargada de la llista `l`.

- `8< l[i]` retalla (elimina) l'`i`-èsim element d'una llista `l`.
`8<` es coneix com *der Scherenoperator* (l'operador de tisores).

  **Aclariment històric:** És fals que l'operador de tisores fos introduït per Anna Magdalena quan en Johann li volia fer un 13è fill.

En JSBach els enters es passen per còpia, les llistes es passen per referència.


# La vostra feina

La vostra feina consisteix en
implementar un (doble) intèrpret de JSBach.

Per realitzar la vostra feina heu d'utilitzar Python3 i ANTLR4, tal com s'ha explicat a les classes de laboratori. Per generar les partitures, heu d'utilitzar el programa Lilipond.



# Especificació de JSBach

Les instruccions de JSBach són:

- l'assignació amb `<-`,
- la lectura amb `<?>`,
- l'escriptura amb `<!>`,
- la reproducció amb `<:>`,
- la invocació de procediments amb `<^>`,
- el condicional amb `wenn`,
- la iteració amb `während`,
- la invocació a un procediment i,
- l'afegit a llistes amb `<<`.
- el tall de llistes amb `8<`.

Les instruccions escrites una rera l'altra s'executen seqüencialment.


## Assignació

L'assignació ha d'avaluar primer l'expressió a la part dreta del `<-` i emmagatzemar després el resultat a la variable local a la part esquerra. Exemple: `a <- a - b`. En el cas d'assignar llistes, cal copiar els valors (sense fer aliasing). A la part esquerra d'una assignació només pot aparèixer una variable (no es pot fer, per exemple, l[2] <- 5).


## Lectura

La instrucció de lectura ha de llegir un valor enter del canal d'entrada estàndard i enmagatzemar-lo a la variable a la dreta del `<?>`. Exemple: `<?> x`.


## Escriptura

La instrucció d'escriptura ha d'avaluar l'expressió del `<!>` i escriure-la, en una línia, al canal de sortida estàndard. Exemple: `<!> x + x`. En el cas d'escriure una llista, cal escriure tots els seus valors entre claudàtors i separats per comes. `<!>` pot contenir diversos paràmetres, cal escriure cadascun d'ells a la mateix línia, separats per espais. Els paràmetres poden contenir textos (tancats entre cometes dobles).

## Reproducció

La instrucció de reproducció ha d'avaluar l'expressió del `<:>`. Si és una nota,  l'ha d'afegir a la partitura, amb el valor d'una negra (diferents valors de notes com blanques, rodones o corxeres es deixen per a JSBach2). Si és una llista, ha d'afegir cadascuna de les seves notes (d'esquerra a dreta).


## Condicional

La instrucció condicional té la semàntica habitual. El bloc del sinó és optatiu. Exemples: `wenn x == y |: z <- 1 :|` i `wenn x == y |: z <- 1 :||: z <- 2 :|`. Fixeu-vos que els limitadors dels blocs sempre són obligatoris (tant als condicions com als procediments i als `währen`s).


## Iteració amb `während`

La instrucció iterativa amb `während` té la semàntica habitual.
Exemple: `während a > 0 |: a <- a / 2 :|`.


## Invocació de procediment

La crida a un procediment té la semàntica habitual.  Els paràmetres enters es passen
per valor, avaluant les expressions dels paràmetres d'esquerra a dreta. Les llistes
es passen per referència.
Si el nombre de paràmetres passats
no corresponen als declarats, es produeix un error. Els procediments no són
funcions i no poden retornar resultats. Però els procediments es poden cridar
recursivament. La sintàxi és com a Haskell: sense parèntesis ni comes.
Exemple: `escriu numero 2`.


## Expressions

Si una variable encara no ha rebut cap valor, el seu valor és zero. Els
operadors aritmètics són els habituals (`+`, `-`, `*`, `/`, `%`) i amb la
mateixa prioritat que en C. Evidentment, es poden usar parèntesis. El operadors
relacionals (`=`, `/=`, `<`, `>`, `<=`, `>=`) retornen zero per fals i u per
cert (Boole és posterior a JSBach).


## Llistes

Les llistes s'escriuen entre claudàtors, amb els seus elements separats per comes. Els elements de les llistes només poden ser enters (o notes, que no són altre cosa que constants enteres). Les llistes es passen per referència.
`#l` retorna la llargada de la llista `l`.
`l[i]` consulta l'`i`-èsim element d'una llista `l`; cal que `i` es trobi entre 1 i `#l`.
`l << x` afegeix l'element `x` al final de la llista `l`.
`8< l[i]` elimina l'`i`-èsim element d'una llista `l`;
també cal que `i` es trobi entre 1 i `#l`.


## Àmbit de visibilitat

No importa l'ordre de declaració dels procediments. Les variables són locals a
cada invocació de cada procediment. No hi ha variables globals ni manera
d'accedir a variables d'altres procediments (només a través dels paràmetres).


## Notes

JSBach proporciona uns noms que representen les notes blanques d'un piano (els sostinguts i bemolls es deixen per JSBach2). Les tres primeres notes són A0 (La0), B0 (Si0), C1 (Do1). Les tres darreres són A7 (La7), B7 (Si7), C8 (Do8). A https://ca.wikipedia.org/wiki/Freq%C3%BC%C3%A8ncies_del_piano teniu una explicació d'aquesta nomemclatura). A més, les notes C, D, E, F, G, A, B
(sense número) son sinónims de C4 (Do central), D4, E4, F4, G4, A4, B4. Les notes de JSBach no són altra cosa que constants, de manera que A0 val 0, B0 val 1, ... i C8 val ???. Així, es pot transposar una nota una octava més amunt o més avall sumant-li o restant-li 7 unitats (sí, els músics són gent peculiar i de 7 en diuen 8).

El procediment següent tocaria totes les tecles blanques del piano
de més greu a més aguda (d'esquerra a dreta):

```
alle_schlüssel |:
    x <- A0
    während x <= C8 |:
        <:> x
        x <- x + 1
    :|
:|
```



## Errors

Malgrat que JSBach és força senzill, els programes poden causar molts errors en temps d'execució. Per aquesta pràctica, només us demanem que detecteu els errors més verosímils (divisió per zero, crida a procediment no definit, repetició de procediment ja definit, nombre de paràmetres incorrectes, noms de paràmetres formals repetits, accés a un índex inexistent d'una llista...) i que el programa llanci amb una excepció quan es donen. No heu de fer una anàlisi semàntica per errors de tipus.


## Invocació de l'intèrpret

El vostre intèrpret s'ha d'invocar amb la comanda `python3 jsbach.py` tot
passant-li com a paràmetre el nom del fitxer que conté el codi font
(l'extensió dels fitxers per programes en JSBach és `.jsb`). Per exemple:

```bash
python3 jsbach.py musica.jsb
```

Si el programa s'executa correctament, es generaran els fitxers
`musica.pdf` amb la partitura en format PDF,
`musica.midi` amb la música en format MIDI,
`musica.wav` amb la música en format WAV,
i
`musica.mp3` amb la música en format MP3.


## Extensions

Podeu extendre el llenguatge amb construccions del vostre gust, a condició de mantenir una compatibilitat estricta amb l'especificació donada (i ser barrocs). A més, cal que documenteu amb precisió les vostres extensions i que creeu programes que les provin i posin de manifest la seva utilitat.

Per exemple, podríeu extendre JSBach amb accidentals (notes amb sostinguts o bemolls), operadors lògics, funcions que retornin valors, funcions d'ordre superior...

Compte: Les extensions poden portar molta feina, consulteu-les abans amb el vostre professor.


# Lliurament

Heu de lliurar la vostra pràctica al Racó. Només heu de lliurar un fitxer ZIP
que, al descomprimir-se generi:

- Un fitxer `README.md` que documenti el vostre projecte.
|:- vegeu, per exemple, https://www.makeareadme.com/.

- Un fitxer `jsbach.g4` amb la gramàtica del LP.

- Un fitxer `jsbach.py` amb el programa de l'intèrpret, incloent els seus visitadors.

- Si heu fet extensions, podeu afegir fitxers `test-*.jsb` com a exemples i jocs de proves.

- Res més. De debò, res més. Tampoc directoris. Ni subdirectoris. Ni `.git`s, ni `.MACOS_XXX`... Res més, collons!

Els vostres fitxers de codi en Python han de seguir les regles d’estı́l PEP8, tot i que podeu oblidar les restriccions sobre la llargada màxima de les lı́nies. Podeu utilitzar els paquets `pep8` o `autopep8` o http://pep8online.com/ per assegurar-vos que seguiu aquestes regles d’estı́l. L’ús de tabuladors en el codi queda prohibit (zero directe). Els vostres programes en JSBach han de seguir l'estil exposat en aquest document.

El termini de lliurament és el **??? a les 23:59**.

Per evitar problemes de còpies,
no pengeu el vostre projecte en repositoris públics.


## Llibreries

Utilitzeu  `ANTLR` per escriure la gramàtica i l'intèrpret. Podeu utilitzar lliurament qualsevol llibreria estàndard de Python.


## Programes externs

Per generar les partitures, heu d'utilitzar el programa LilyPond.
Lilypond ja genera MIDI i PDF.
Per generar WAV a partir de MIDI heu d'utilitzar `timidity`.
Per generar MP3 a partir de WAV heu d'utilitzar `ffmpeg`.
Tots aquests programes es poden instal·lar facilment en Max, Linux i (suposo) Windows. El vostre programa es corregirà en un entorn on els binaris `lilypond`, `timidity` i `ffmpeg` es troben al *path*.


## Breu demostració dels programes externs

LilyPond és un programa de tipografia musical.
És programari lliure i forma part del Projecte GNU.
Les partitures es descriuen a partir d'un llenguatge prou complex, però del quan només us cal saber uns rudiments per fer aquesta pràctica.

Per exemple, aquest programa `exemple.lily` en LilyPond descriu una escala
amb buit negres (Do, Re, Mi, Fa, Sol, La, Si, Do) a un tempo de 120:

```
\version "2.22.1"
\score {
    \absolute {
        \tempo 4 = 120
        c'4 d'4 e'4 f'4 g'4 a'4 b'4
    }
    \layout { }
    \midi { }
}
```

Quan hom executa

```bash
lilypond exemple.lily
```

Lilipond genera `exemple.pdf` i `exemple.midi` (perquè s'ha donat les comandes `\layout` i `\midi` respectivament).

TiMidity++ és un altre programa de codi obert que transforma fitxers MIDI en fitxers de so, com ara fitxers WAV. Es pot executar així

```bash
timidity -Ow -o exemple.wav exemple.midi
```

per tal d'obtenir el fitxer `exemple.wav`.

El programa lliure `ffmpeg` permet convertir entre diferents formats de vídeo i audio. Es pot executar així

```bash
ffmpeg -i exemple.wav -codec:a libmp3lame -qscale:a 2 exemple.mp3
```

per tal d'obtenir el fitxer `exemple.mp3`.

Finalment, els fitxers MP3 es poden reproduir amb molts reproductors de so. En un Mac, es pot fer així des de la línia de comandes:

```bash
afplay exemple.mp3
```  


# Referències

- Johann Sebastian Bach: https://ca.wikipedia.org/wiki/Johann_Sebastian_Bach

- ANTLR en Python: https://gebakx.github.io/Python3/compiladors.html#1

- Lilypond: https://lilypond.org

- Timidity: https://en.wikipedia.org/wiki/TiMidity%2B%2B

- ffmpeg: https://www.ffmpeg.org/

![Firma](firma.png)
