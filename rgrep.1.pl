.\" PTM/WK/2001-VI
.\"===========================================================================
.\" rgrep � a recursive highlighting grep program, this manpage was writen by
.\" "Boris D. Beletsky" <borik@isracom.co.il> copyright(c) 1996
.\" This manpage may be freely distrebuted as part of GNU Debian Linux
.\"===========================================================================
.TH RGREP 1 "pa�dziernik 1996" Debian "Podr�czniki u�ytkownika"
.SH NAZWA
rgrep \- rekurencyjny, pod�wietlaj�cy program grep
.SH SK�ADNIA
.B rgrep 
.RI [ opcje ]
.I wzorzec
.RI [ plik ]...
.SH OPIS
.BR rgrep ,
w przeciwie�stwie do
.BR grep (1) 
i 
.BR egrep (1),
potrafi rekurencyjnie zag��bia� si� w podkatalogi. Tradycyjna metoda
wykonywania tego rodzaju wyszukiwania w systemach uniksowych wykorzystuje
polecenie
.BR find (1) 
w po��czeniu z
.BR grep (1). 
Skutkuje to jednak bardzo kiepsk� wydajno�ci�.
.SH PARAMETRY WIERSZA POLECE�
.LP
.B -?
.RS
Dodatkowa pomoc (na niekt�rych systemach nale�y u�y�
.BR '-?' ,
by unikn�� interpretacji pytajnika przez pow�ok�).
.RE
.B -c
.RS
Zlicza dopasowania.
.RE
.B -h
.RS
Pod�wietla dopasowania (przyjmuje si� terminal zgodny z ANSI).
.RE
.B -H
.RS
Wypisuje dopasowanie, a nie ca�� linijk� je zawieraj�c�.
.RE
.B -i
.RS
Ignoruje wielko�ci liter.
.RE
.B -l
.RS 
Podaje tylko nazwy plik�w.
.RE
.B -n
.RS
Wypisuje numer linii, w kt�rej wyst�puje dopasowanie.
.RE
.B -F
.RS
Pod��a za dowi�zaniami.
.RE
.B -r
.RS
Rekurencyjnie przegl�da drzewo katalog�w.
.RE
.B -N
.RS
Wyszukuje BEZ rekurencji.
.RE
.BI -R " wzorzec "
.RS
Jak \fB-r\fP, z wyj�tkiem tego, �e sprawdzane s� tylko pliki pasuj�ce
do \fIwzorca\fP.
.RE
.B -v
.RS
Wypisuje tylko te linie, kt�re NIE pasuj� do zadanego wzorca.
.RE
.BI -x " ext"
.RS
Sprawdza tylko pliki o rozszerzeniu \fIext\fP.
.RE
.B -D
.RS
Wypisuje wszystkie katalogi, jakie b�d� przeszukiwane. Ta opcja s�u�y tylko
do cel�w diagnostycznych. Je�li jest u�yta, to nie s� przegl�dane �adne pliki.
.RE
.BI -W " d�ug"
.RS
Linie maj� d�ugo�� \fId�ug\fP znak�w (nie s� zako�czone znakiem nowej linii).
.RE
.LP
.SH ROZPOZNAWANE WYRA�ENIA REGULARNE:
.LP
.B .
.RS
dopasowuje dowolny znak opr�cz znaku nowej linii
.RE
.B \ed
.RS
dopasowuje dowoln� cyfr�
.RE
.B \ee
.RS
dopasowuje znak ESC
.RE
.B *
.RS
dopasowuje zero lub wi�cej wyst�pie� poprzedzaj�cego wyra�enia regularnego
.RE
.B +
.RS
dopasowuje co najmniej jedno wyst�pienie poprzedzaj�cego wyra�enia
regularnego
.RE
.B ?
.RS
dopasowuje zero wyst�pie� lub jedno wyst�pienie poprzedzaj�cego wyra�enia
regularnego
.RE
.B ^
.RS
dopasowuje pocz�tek linii
.RE
.B $
.RS
dopasowuje koniec linii
.RE
.BI [ ... ]            
.RS
dopasowuje dowolny pojedynczy znak spo�r�d umieszczonych w nawiasach.
Na przyk�ad, 
.B [-02468] 
dopasowuje
.RB ' - ' 
lub dowoln� cyfr� parzyst�, a
.B [-0-9a-z] 
dopasowuje
.RB ' - ' ,
dowoln� cyfr� od
.B 0 
do 
.B 9
lub liter� od
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
dopasowuje pod�a�cuch poprzednio dopasowany n-tym uj�tym w nawiasy
podwyra�eniem
.BI \e( ... \e)
wyra�enia regularnego.
.br
Na przyk�ad,
.B \\\\([\ \\\\t][a-zA-Z]+\\\\)\\\\1[\ \\\\t]
dopasowuje ka�de s�owo kolejno powt�rzone.
.RE
.LP
.SH PRZYK�ADY
.TP 3
o
Szukanie we wszystkich plikach z rozszerzeniem 'c' w bie��cym katalogu
i jego podkatalogach dopasowa� napisu 'int ' na pocz�tku linii,
z wypisywaniem pasuj�cych linii wraz z ich numerami (dwie metody):
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
Pod�wietlanie wszystkich wyst�pie� powt�rzonych s��w w pliku 'strona.tex':
.RS
.B rgrep -h 
.B '[\ \\\\t]\\\\([a-zA-Z]+\\\\)[\ \\\\t]+\\\\1[\ \\\\t\\\\n]' strona.tex
.br
.B rgrep -h '^\\\\([a-zA-Z]+\\\\)[\ \\\\t]+\\\\1[\ \\\\t\\\\n]' strona.tex
.PP
Zauwa�, �e ta wersja programu rgrep wymaga w tym przypadku dwu przebieg�w.
.RE
.TP 3
o
Przegl�danie, w katalogu /usr/src/linux i ni�ej, wszystkich plik�w OPR�CZ
maj�cych rozszerzenie '.o' lub '.a' w poszukiwaniu �a�cucha 'mouse', bez
uwzgl�dniania wielko�ci liter:
.RS
.RS 4
.PP
.B rgrep -i -R '*.[^ao]' mouse /usr/src/linux
.RE
.RE
.TP 3
o
Przeszukiwanie w pliku 'plik.fits', o sta�ej d�ugo�ci rekord�w, s�owa
kluczowego EXTNAME:
.RS
.RS 4
.PP
.B rgrep -W80 ^EXTNAME plik.fits
.PP
.RE
Zauwa�, �e wyra�enie regularne
.RB ' ^[A-Z]+ ' 
wypisze wszystkie nag��wki formatu FITS.
.br
[t�um.: FITS, Flexible Image Transport System - opracowany przez NASA format
do mi�dzyplatformowej wymiany danych astronomicznych, g��wnie grafiki, ale
r�wnie� tablic czy macierzy.]
.RE
.SH AUTOR
.LP
.RS
.I \
"""John E. Davis""" <davis@space.mit.edu>
.RE
.PP
T� stron� podr�cznika systemowego prze�o�y� na troff
.PP
"Boris D. Beletsky"
<borik@isracom.co.il>
