.\" {PTM/WK/0.1 /05-08-1999/"edytor dla programist�w"}
.\" ==================================================================
.\" Jed programmers editor, this manpage was writen by 
.\" "Boris D. Beletsky" <borik@isracom.co.il> copyright(c) 1996
.\" This manpage may be freely distrebuted as part of GNU Debian Linux
.\" ==================================================================
.TH JED 1 "OCT 1996" Debian "User Manuals"
.SH NAZWA
jed \- edytor dla programist�w
.SH SK�ADNIA
.B jed
.RB [ opcje ] 
.IR plik ...
.SH OPIS
.B Jed - edytor dla programist�w
.LP
Mo�liwo�ci:
.LP
.I Pod�wietlanie
sk�adni kolorami. 
Emulacja edytor�w 
.BR Emacs ,
.BR EDT ,
.BR Wordstar 
oraz Brief. Mo�liwo�ci rozbudowywania w j�zyku przypominaj�cym C. Ca�kowicie
dostosowywalny. Edycja plik�w TeX-u z edycj� w stylu AUC-TeX (r�wnie� obs�uga
BiBTeX). Obs�uga sk�adu (folding support) i wiele wi�cej..
.LP
Pe�n� dokumentacj� znajdziesz w plikach GNU info, niniejszy podr�cznik jest
jedynie kr�tkim wprowadzeniem.
.SH OPCJE
.LS
.B -batch
.RS
uruchamia Jed w trybie wsadowym. Jest to tryb nie-interaktywny.
.RE
.B -n
.RS
nie wczytuj pliku 
.IR .jedrc .
.RE
.BI -g " n"
.RS
skocz do wiersza 
.I n 
w buforze.
.RE
.BI -l " plik"
.RS
wczytaj
.I plik
jako kod S-Lang.
.RE
.BI -f " funkcja"
.RS
wykonaj funkcj� S-Lang o nazwie
.IR funkcja .
.RE
.BI -s " �a�cuch"
.RS
Szukaj 
.I �a�cucha
w prz�d.
.RE
.B -2             
.RS
podziel okno.
.RE
.BI -i " plik"
.RS
Wstaw  
.I plik
do bie��cego bufora.
.RE
.SH KONFIGURACJA
.SS Emulacja innych edytor�w
Emulacja innych edytor�w mo�liwa jest dzi�ki zdolno�ci JEDa do tworzenia
nowych funkcji przy u�yciu j�zyka programowania \fIS-Lang\fR oraz
umo�liwieniu u�ytkownikowi zmiany przypisa� klawiszy. Obecnie JED zapewnia
rozs�dn� emulacj� edytor�w
.IR Emacs ", " EDT " i " Wordstar .
.SS Emulacja Emacsa
.I Emulacja Emacsa
zapewniana jest dzi�ki kodowi S-Lang zawartemu w
.IR emacs.sl .
Emulowana jest podstawowa funkcjonalno�� Emacsa; wi�kszo�� u�ytkownik�w
Emacsa nie powinna mie� k�opot�w z JEDem. By w��czy� emulacj� Emacsa w JED
upewnij si�, �e tw�j plik inicjuj�cy
.I jed.rc
(.jedrc) zawiera wiersz
.LP
.RS
.I () = evalfile ("emacs"); 
.RE
.LP
JED rozpowszechniany jest z plikiem domy�lnym jed.rc zawieraj�cym ju� ten
wiersz.
.SS Emulacja EDT
Do emulacji
.I EDT
musi by� wczytany
.IR edt.sl .
Osi�gane jest do przez umieszczenie wiersza:
.LP
.RS
.I () = evalfile ("edt");
.RE
.LP
w pliku inicjuj�cym jed.rc (.jedrc).
.SS Emulacja Wordstara
wordstar.sl zawiera kod  S-Lang odpowiedzialny za emulacj�
Wordstara. Dodanie wiersza:
.LP
.RS
.I () = evalfile ("wordstar");
.RE
.LP
do twego pliku inicjalizacji jed.rc (.jedrc) w��czy emulacj� Wordstara w
JED.
.SH RUN TIME
.SS Wiersz stanu i Okna
.I JED 
potrafi obs�ugiwa� wiele okien. Ka�de okno mo�e zawiera� ten sam bufor lub
r�ne bufory. Bezpo�rednio pod ka�dym oknem wy�wietlany jest wiersz stanu.
Wiersz stanu zawiera takie informacje jak numer wersji JEDa, nazwa bufora,
\fItryb\fR, itd. Uwa�aj, prosz�, na poni�sze wska�niki:
.LP
.I **
.RS
bufor zosta� zmieniony od ostatniego zapisu.
.RE
.I %%
.RS
bufor jest tylko do odczytu.
.RE
.I m
.RS
wska�nik ustawiania znacznika. Oznacza, �e w�a�nie definiowany jest obszar.
.RE
.I d
.RS
wska�nik zmiany pliku na dysku. Wskazuje, �e plik skojarzony z buforem jest
nowszy ni� sam bufor.
.RE
.I s
.RS
wska�nik zapami�tania pozycji.
.br
[t�um.: zapami�tywanie i odtwarzanie pozycji kursora w buforze realizuje si�
par� funkcji push_spot/pop_spot w S-Lang]
.RE
.I +
.RS
mo�liwe cofanie akcji (undo) dla bufora.
.RE
.I [Narrow]
.RS
bufor jest zaw�ony (narrowed) do obszaru WIERSZY (LINES).
.RE
.I [Macro]
.RS
w trakcie definiowania makra.
.RE
.SS Mini-bufor
.I Mini-bufor
sk�ada si� z pojedynczego wiersza usytuowanego na dole ekranu. Wi�kszo��
dialogu pomi�dzy u�ytkownikiem a edytorem JED odbywa si� w tym w�a�nie
buforze. Na przyk�ad, gdy poszukujesz �a�cucha, JED wy�wietli zapytanie o
�a�cuch w mini-buforze.
.LP
.I Mini-bufor 
zapewnia tak�e bezpo�rednie po��czenie z interpreterem S-Lang. W celu
uzyskania dost�pu do interpretera naci�nij
.I Ctrl-X Esc
a w mini-buforze pojawi si� zach�ta
.IR S-Lang> .
Wprowad� dowolne poprawne wyra�enie S-Lang, kt�re chcesz by rozwin��
interpreter.
.LP
Przez u�ycie klawiszy strza�ek w g�r� i w d� mo�liwe jest ponowne
przywo�anie danych uprzednio wprowadzonych do 
.IR mini-bufora .
Umo�liwia to u�ycie i zmian� poprzednich wyra�e� w wygodny i efektywny
spos�b.
.LP
.SS Podstawowa edycja
.LP
.I Edycja przy u�ycie JEDa
jest bardzo �atwa - wi�kszo�� klawiszy powoduje wstawienie przypisanych im
znak�w. Przemieszczanie si� wewn�trz zawarto�ci bufora zwykle odbywa si� przy
u�yciu
.I klawiszy strza�ek
lub klawiszy
.I strony w g�r�
i
.IR "strony w d�" .
Je�eli wczytany jest 
.IR edt.sl ,
to dzia�aj� r�wnie� klawisze (keypads) terminala VTxxx. W�wczas zmieniane s�
tylko pod�wietlenia (operacje wytnij/wklej [cut/paste] nie s� uwa�ane za
`pod�wietlenia').
.\" Here, only the highlights are touched upon
.\" (cut/paste operations are not considered `highlights').
.\" Poni�ej, dowolny znak poprzedzony napisem
.\" .I Ctrl
.\" oznacza znak steruj�cy.
Na klawiaturach pozbawionych klawisza Esc
.I "Ctrl-["
najprawdopodobniej wygeneruje znak Escape.
.LP
.I Argument przedrostkowy
polecenia mo�e by� utworzony przez naci�ni�cie klawisza
.I Esc
a nast�pnie wprowadzenie liczby, po kt�rej naciskany jest po��dany klawisz.
Zwykle argument przedrostkowy u�ywany jest po prostu dla powt�rze�. Na
przyk�ad, by przesun�� si� w prawo o 40 znak�w, powinno si� nacisn��
.I "Esc 4 0"
a bezpo�rednio po tym klawisz strza�ki w prawo.
Ilustruje to u�ycie argumentu powtarzania dla powt�rzenia akcji.
Argument przedrostkowy mo�e jednak�e zosta� zastosowany r�wnie� na inne
sposoby. Na przyk�ad, w celu rozpocz�cia definiowania obszaru, powinno si�
nacisn�� klawisz
.IR "Ctrl-@" .
Ustawia on znacznik i rozpoczyna pod�wietlanie.
Naci�ni�cie
.I "Ctrl-@"
z argumentem przedrostkowym spowoduje zaniechanie czynno�ci definiowania
obszaru i zdj�cie znacznika.
.\" and to pop the mark.
.PP
Poni�sza lista przydatnych przypisa� klawiszy zak�ada, �e wczytano 
.IR emacs.sl .
.LP
.I Ctrl-L
.RS
Od�wie� (ponownie narysuj) ekran.
.RE
.I Ctrl-_
.RS
Cofnij akcj�  (Control-podkre�lenie, r�wnie� Ctrl-X u').
.RE
.I Esc q
.RS
Ponownie formatuj akapit (tryb zawijania). U�yte z argumentem przedrostkowym
r�wnie� justuje akapit.
.RE
.I Esc n
.RS
Zw� akapit (tryb zawijania). U�yte z argumentem przedrostkowym r�wnie�
justuje akapit.
.\" narrow paragraph
.RE
.I Esc ;
.RS
Wstaw komentarz w j�zyku programowania (Fortran i C).
.RE
.I Esc \\\\
.RS
Obetnij otaczaj�ce bia�e znaki.
.RE
.I Esc !
.RS
Wykonaj polecenie pow�oki.
.RE
.I Esc $
.RS
Sprawd� pisowni� s�owa przy pomocy ispell.
.RE
.I Ctrl-X ?
.RS
Poka� informacj� o wierszu/kolumnie.
.RE
.I `
.RS
quoted_insert --- wstaw nast�pny znak dos�ownie (klawisz odwrotnego apostrofu)
.RE
.I Esc s
.RS
Wypo�rodkuj wiersz.
.RE
.I Esc u
.RS
Zamie� s�owo na du�e litery
.RE
.I Esc d
.RS
Zamie� s�owo na ma�e litery.
.RE
.I Esc c
.RS
Zamie� w s�owie pierwsz� liter� na du��, reszt� na ma�e.
.RE
.I Esc x
.RS
Przejd� do zach�ty minibufora M-x z uzupe�nianiem polece�.
.RE
.I Ctrl-X Ctrl-B
.RS
Wy�wietl rozwijaln� list� bufor�w.
.RE
.I Ctrl-X Ctrl-C
.RS
Zako�cz prac� JED.
.RE
.I Ctrl-X 0
.RS
Usu� bie��ce okno.
.RE
.I Ctrl-X 1
.RS
Jedno okno.
.RE
.I Ctrl-X 2
.RS
Podziel okno.
.RE
.I Ctrl-X o
.RS
Na inne okno.
.RE
.I Ctrl-X b
.RS
Prze��cz na bufor.
.RE
.I Ctrl-X k
.RS
Usu� bufor.
.RE
.I Ctrl-X s
.RS
Zapisz bufory.
.RE
.I Ctrl-X Esc
.RS
Przejd� do zach�ty "S-Lang>" interfejsu interpretera S-Lang.
.RE
.I Esc .
.RS
Znajd� tag.
.RE
.I Ctrl-@
.RS
Ustaw znacznik (rozpocznij okre�lanie obszaru). U�yte z argumentem
przedrostkowym anuluje czynno�� definiowania i zdejmuje znacznik.
.\" pops the Mark.
.SH PLIKI
.I JED_ROOT/lib/*.sl
.RS
S� to domy�lne pliki uruchomieniowe slang dla edytora jed.
.\" default runtime jed slang files
.RE
.I JED_ROOT/lib/site.sl
.RS
Domy�lny plik inicjuj�cy (startup file).
.RE
.I /etc/jed.rc
.RS
Og�lnosystemowy plik konfiguracyjny.
.RE
.I ~/.jedrc
.RS
Plik konfiguracyjny danego u�ytkownika.
.SH AUTOR
.I "John E. Davis" <davis@space.mit.edu>
.RS
Autor programu Jed.
.RE
.PP
--- Niniejszy dokument zosta�
.I przet�umaczony
na format nroff
przez "Boris D. Beletsky" <borik@isracom.co.il>
