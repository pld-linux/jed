.\" PTM/WK/2001-VI
.\"===========================================================================
.\" rgrep ­ a recursive highlighting grep program, this manpage was writen by
.\" "Boris D. Beletsky" <borik@isracom.co.il> copyright(c) 1996
.\" This manpage may be freely distrebuted as part of GNU Debian Linux
.\"===========================================================================
.TH RGREP 1 "pa¼dziernik 1996" Debian "Podrêczniki u¿ytkownika"
.SH NAZWA
rgrep \- rekurencyjny, pod¶wietlaj±cy program grep
.SH SK£ADNIA
.B rgrep 
.RI [ opcje ]
.I wzorzec
.RI [ plik ]...
.SH OPIS
.BR rgrep ,
w przeciwieñstwie do
.BR grep (1) 
i 
.BR egrep (1),
potrafi rekurencyjnie zag³êbiaæ siê w podkatalogi. Tradycyjna metoda
wykonywania tego rodzaju wyszukiwania w systemach uniksowych wykorzystuje
polecenie
.BR find (1) 
w po³±czeniu z
.BR grep (1). 
Skutkuje to jednak bardzo kiepsk± wydajno¶ci±.
.SH PARAMETRY WIERSZA POLECEÑ
.LP
.B -?
.RS
Dodatkowa pomoc (na niektórych systemach nale¿y u¿yæ
.BR '-?' ,
by unikn±æ interpretacji pytajnika przez pow³okê).
.RE
.B -c
.RS
Zlicza dopasowania.
.RE
.B -h
.RS
Pod¶wietla dopasowania (przyjmuje siê terminal zgodny z ANSI).
.RE
.B -H
.RS
Wypisuje dopasowanie, a nie ca³± linijkê je zawieraj±c±.
.RE
.B -i
.RS
Ignoruje wielko¶ci liter.
.RE
.B -l
.RS 
Podaje tylko nazwy plików.
.RE
.B -n
.RS
Wypisuje numer linii, w której wystêpuje dopasowanie.
.RE
.B -F
.RS
Pod±¿a za dowi±zaniami.
.RE
.B -r
.RS
Rekurencyjnie przegl±da drzewo katalogów.
.RE
.B -N
.RS
Wyszukuje BEZ rekurencji.
.RE
.BI -R " wzorzec "
.RS
Jak \fB-r\fP, z wyj±tkiem tego, ¿e sprawdzane s± tylko pliki pasuj±ce
do \fIwzorca\fP.
.RE
.B -v
.RS
Wypisuje tylko te linie, które NIE pasuj± do zadanego wzorca.
.RE
.BI -x " ext"
.RS
Sprawdza tylko pliki o rozszerzeniu \fIext\fP.
.RE
.B -D
.RS
Wypisuje wszystkie katalogi, jakie bêd± przeszukiwane. Ta opcja s³u¿y tylko
do celów diagnostycznych. Je¶li jest u¿yta, to nie s± przegl±dane ¿adne pliki.
.RE
.BI -W " d³ug"
.RS
Linie maj± d³ugo¶æ \fId³ug\fP znaków (nie s± zakoñczone znakiem nowej linii).
.RE
.LP
.SH ROZPOZNAWANE WYRA¯ENIA REGULARNE:
.LP
.B .
.RS
dopasowuje dowolny znak oprócz znaku nowej linii
.RE
.B \ed
.RS
dopasowuje dowoln± cyfrê
.RE
.B \ee
.RS
dopasowuje znak ESC
.RE
.B *
.RS
dopasowuje zero lub wiêcej wyst±pieñ poprzedzaj±cego wyra¿enia regularnego
.RE
.B +
.RS
dopasowuje co najmniej jedno wyst±pienie poprzedzaj±cego wyra¿enia
regularnego
.RE
.B ?
.RS
dopasowuje zero wyst±pieñ lub jedno wyst±pienie poprzedzaj±cego wyra¿enia
regularnego
.RE
.B ^
.RS
dopasowuje pocz±tek linii
.RE
.B $
.RS
dopasowuje koniec linii
.RE
.BI [ ... ]            
.RS
dopasowuje dowolny pojedynczy znak spo¶ród umieszczonych w nawiasach.
Na przyk³ad, 
.B [-02468] 
dopasowuje
.RB ' - ' 
lub dowoln± cyfrê parzyst±, a
.B [-0-9a-z] 
dopasowuje
.RB ' - ' ,
dowoln± cyfrê od
.B 0 
do 
.B 9
lub literê od
.B a 
do
.BR z .
.RE
.LP
.BI \e{ ... \e}
.LP
.BI \e( ... \e)
.LP
.BI "\e1, \e2, " ... ", \e9"
.RS
dopasowuje pod³añcuch poprzednio dopasowany n-tym ujêtym w nawiasy
podwyra¿eniem
.BI \e( ... \e)
wyra¿enia regularnego.
.br
Na przyk³ad,
.B \\\\([\ \\\\t][a-zA-Z]+\\\\)\\\\1[\ \\\\t]
dopasowuje ka¿de s³owo kolejno powtórzone.
.RE
.LP
.SH PRZYK£ADY
.TP 3
o
Szukanie we wszystkich plikach z rozszerzeniem 'c' w bie¿±cym katalogu
i jego podkatalogach dopasowañ napisu 'int ' na pocz±tku linii,
z wypisywaniem pasuj±cych linii wraz z ich numerami (dwie metody):
.RS
.RS 4
.PP
.B rgrep -n -R '*.c' '^int ' .
.br
.B rgrep -n -x c '^int ' .
.RE
.RE
.TP 3
o
Pod¶wietlanie wszystkich wyst±pieñ powtórzonych s³ów w pliku 'strona.tex':
.RS
.B rgrep -h 
.B '[\ \\\\t]\\\\([a-zA-Z]+\\\\)[\ \\\\t]+\\\\1[\ \\\\t\\\\n]' strona.tex
.br
.B rgrep -h '^\\\\([a-zA-Z]+\\\\)[\ \\\\t]+\\\\1[\ \\\\t\\\\n]' strona.tex
.PP
Zauwa¿, ¿e ta wersja programu rgrep wymaga w tym przypadku dwu przebiegów.
.RE
.TP 3
o
Przegl±danie, w katalogu /usr/src/linux i ni¿ej, wszystkich plików OPRÓCZ
maj±cych rozszerzenie '.o' lub '.a' w poszukiwaniu ³añcucha 'mouse', bez
uwzglêdniania wielko¶ci liter:
.RS
.RS 4
.PP
.B rgrep -i -R '*.[^ao]' mouse /usr/src/linux
.RE
.RE
.TP 3
o
Przeszukiwanie w pliku 'plik.fits', o sta³ej d³ugo¶ci rekordów, s³owa
kluczowego EXTNAME:
.RS
.RS 4
.PP
.B rgrep -W80 ^EXTNAME plik.fits
.PP
.RE
Zauwa¿, ¿e wyra¿enie regularne
.RB ' ^[A-Z]+ ' 
wypisze wszystkie nag³ówki formatu FITS.
.br
[t³um.: FITS, Flexible Image Transport System - opracowany przez NASA format
do miêdzyplatformowej wymiany danych astronomicznych, g³ównie grafiki, ale
równie¿ tablic czy macierzy.]
.RE
.SH AUTOR
.LP
.RS
.I \
"""John E. Davis""" <davis@space.mit.edu>
.RE
.PP
Tê stronê podrêcznika systemowego prze³o¿y³ na troff
.PP
"Boris D. Beletsky"
<borik@isracom.co.il>
