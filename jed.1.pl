.\" {PTM/WK/0.1 /05-08-1999/"edytor dla programistów"}
.\" ==================================================================
.\" Jed programmers editor, this manpage was writen by 
.\" "Boris D. Beletsky" <borik@isracom.co.il> copyright(c) 1996
.\" This manpage may be freely distrebuted as part of GNU Debian Linux
.\" ==================================================================
.TH JED 1 "OCT 1996" Debian "User Manuals"
.SH NAZWA
jed \- edytor dla programistów
.SH SK£ADNIA
.B jed
.RB [ opcje ] 
.IR plik ...
.SH OPIS
.B Jed - edytor dla programistów
.LP
Mo¿liwo¶ci:
.LP
.I Pod¶wietlanie
sk³adni kolorami. 
Emulacja edytorów 
.BR Emacs ,
.BR EDT ,
.BR Wordstar 
oraz Brief. Mo¿liwo¶ci rozbudowywania w jêzyku przypominaj±cym C. Ca³kowicie
dostosowywalny. Edycja plików TeX-u z edycj± w stylu AUC-TeX (równie¿ obs³uga
BiBTeX). Obs³uga sk³adu (folding support) i wiele wiêcej..
.LP
Pe³n± dokumentacjê znajdziesz w plikach GNU info, niniejszy podrêcznik jest
jedynie krótkim wprowadzeniem.
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
wykonaj funkcjê S-Lang o nazwie
.IR funkcja .
.RE
.BI -s " ³añcuch"
.RS
Szukaj 
.I ³añcucha
w przód.
.RE
.B -2             
.RS
podziel okno.
.RE
.BI -i " plik"
.RS
Wstaw  
.I plik
do bie¿±cego bufora.
.RE
.SH KONFIGURACJA
.SS Emulacja innych edytorów
Emulacja innych edytorów mo¿liwa jest dziêki zdolno¶ci JEDa do tworzenia
nowych funkcji przy u¿yciu jêzyka programowania \fIS-Lang\fR oraz
umo¿liwieniu u¿ytkownikowi zmiany przypisañ klawiszy. Obecnie JED zapewnia
rozs±dn± emulacjê edytorów
.IR Emacs ", " EDT " i " Wordstar .
.SS Emulacja Emacsa
.I Emulacja Emacsa
zapewniana jest dziêki kodowi S-Lang zawartemu w
.IR emacs.sl .
Emulowana jest podstawowa funkcjonalno¶æ Emacsa; wiêkszo¶æ u¿ytkowników
Emacsa nie powinna mieæ k³opotów z JEDem. By w³±czyæ emulacjê Emacsa w JED
upewnij siê, ¿e twój plik inicjuj±cy
.I jed.rc
(.jedrc) zawiera wiersz
.LP
.RS
.I () = evalfile ("emacs"); 
.RE
.LP
JED rozpowszechniany jest z plikiem domy¶lnym jed.rc zawieraj±cym ju¿ ten
wiersz.
.SS Emulacja EDT
Do emulacji
.I EDT
musi byæ wczytany
.IR edt.sl .
Osi±gane jest do przez umieszczenie wiersza:
.LP
.RS
.I () = evalfile ("edt");
.RE
.LP
w pliku inicjuj±cym jed.rc (.jedrc).
.SS Emulacja Wordstara
wordstar.sl zawiera kod  S-Lang odpowiedzialny za emulacjê
Wordstara. Dodanie wiersza:
.LP
.RS
.I () = evalfile ("wordstar");
.RE
.LP
do twego pliku inicjalizacji jed.rc (.jedrc) w³±czy emulacjê Wordstara w
JED.
.SH RUN TIME
.SS Wiersz stanu i Okna
.I JED 
potrafi obs³ugiwaæ wiele okien. Ka¿de okno mo¿e zawieraæ ten sam bufor lub
ró¿ne bufory. Bezpo¶rednio pod ka¿dym oknem wy¶wietlany jest wiersz stanu.
Wiersz stanu zawiera takie informacje jak numer wersji JEDa, nazwa bufora,
\fItryb\fR, itd. Uwa¿aj, proszê, na poni¿sze wska¼niki:
.LP
.I **
.RS
bufor zosta³ zmieniony od ostatniego zapisu.
.RE
.I %%
.RS
bufor jest tylko do odczytu.
.RE
.I m
.RS
wska¼nik ustawiania znacznika. Oznacza, ¿e w³a¶nie definiowany jest obszar.
.RE
.I d
.RS
wska¼nik zmiany pliku na dysku. Wskazuje, ¿e plik skojarzony z buforem jest
nowszy ni¿ sam bufor.
.RE
.I s
.RS
wska¼nik zapamiêtania pozycji.
.br
[t³um.: zapamiêtywanie i odtwarzanie pozycji kursora w buforze realizuje siê
par± funkcji push_spot/pop_spot w S-Lang]
.RE
.I +
.RS
mo¿liwe cofanie akcji (undo) dla bufora.
.RE
.I [Narrow]
.RS
bufor jest zawê¿ony (narrowed) do obszaru WIERSZY (LINES).
.RE
.I [Macro]
.RS
w trakcie definiowania makra.
.RE
.SS Mini-bufor
.I Mini-bufor
sk³ada siê z pojedynczego wiersza usytuowanego na dole ekranu. Wiêkszo¶æ
dialogu pomiêdzy u¿ytkownikiem a edytorem JED odbywa siê w tym w³a¶nie
buforze. Na przyk³ad, gdy poszukujesz ³añcucha, JED wy¶wietli zapytanie o
³añcuch w mini-buforze.
.LP
.I Mini-bufor 
zapewnia tak¿e bezpo¶rednie po³±czenie z interpreterem S-Lang. W celu
uzyskania dostêpu do interpretera naci¶nij
.I Ctrl-X Esc
a w mini-buforze pojawi siê zachêta
.IR S-Lang> .
Wprowad¼ dowolne poprawne wyra¿enie S-Lang, które chcesz by rozwin±³
interpreter.
.LP
Przez u¿ycie klawiszy strza³ek w górê i w dó³ mo¿liwe jest ponowne
przywo³anie danych uprzednio wprowadzonych do 
.IR mini-bufora .
Umo¿liwia to u¿ycie i zmianê poprzednich wyra¿eñ w wygodny i efektywny
sposób.
.LP
.SS Podstawowa edycja
.LP
.I Edycja przy u¿ycie JEDa
jest bardzo ³atwa - wiêkszo¶æ klawiszy powoduje wstawienie przypisanych im
znaków. Przemieszczanie siê wewn±trz zawarto¶ci bufora zwykle odbywa siê przy
u¿yciu
.I klawiszy strza³ek
lub klawiszy
.I strony w górê
i
.IR "strony w dó³" .
Je¿eli wczytany jest 
.IR edt.sl ,
to dzia³aj± równie¿ klawisze (keypads) terminala VTxxx. Wówczas zmieniane s±
tylko pod¶wietlenia (operacje wytnij/wklej [cut/paste] nie s± uwa¿ane za
`pod¶wietlenia').
.\" Here, only the highlights are touched upon
.\" (cut/paste operations are not considered `highlights').
.\" Poni¿ej, dowolny znak poprzedzony napisem
.\" .I Ctrl
.\" oznacza znak steruj±cy.
Na klawiaturach pozbawionych klawisza Esc
.I "Ctrl-["
najprawdopodobniej wygeneruje znak Escape.
.LP
.I Argument przedrostkowy
polecenia mo¿e byæ utworzony przez naci¶niêcie klawisza
.I Esc
a nastêpnie wprowadzenie liczby, po której naciskany jest po¿±dany klawisz.
Zwykle argument przedrostkowy u¿ywany jest po prostu dla powtórzeñ. Na
przyk³ad, by przesun±æ siê w prawo o 40 znaków, powinno siê nacisn±æ
.I "Esc 4 0"
a bezpo¶rednio po tym klawisz strza³ki w prawo.
Ilustruje to u¿ycie argumentu powtarzania dla powtórzenia akcji.
Argument przedrostkowy mo¿e jednak¿e zostaæ zastosowany równie¿ na inne
sposoby. Na przyk³ad, w celu rozpoczêcia definiowania obszaru, powinno siê
nacisn±æ klawisz
.IR "Ctrl-@" .
Ustawia on znacznik i rozpoczyna pod¶wietlanie.
Naci¶niêcie
.I "Ctrl-@"
z argumentem przedrostkowym spowoduje zaniechanie czynno¶ci definiowania
obszaru i zdjêcie znacznika.
.\" and to pop the mark.
.PP
Poni¿sza lista przydatnych przypisañ klawiszy zak³ada, ¿e wczytano 
.IR emacs.sl .
.LP
.I Ctrl-L
.RS
Od¶wie¿ (ponownie narysuj) ekran.
.RE
.I Ctrl-_
.RS
Cofnij akcjê  (Control-podkre¶lenie, równie¿ Ctrl-X u').
.RE
.I Esc q
.RS
Ponownie formatuj akapit (tryb zawijania). U¿yte z argumentem przedrostkowym
równie¿ justuje akapit.
.RE
.I Esc n
.RS
Zwê¼ akapit (tryb zawijania). U¿yte z argumentem przedrostkowym równie¿
justuje akapit.
.\" narrow paragraph
.RE
.I Esc ;
.RS
Wstaw komentarz w jêzyku programowania (Fortran i C).
.RE
.I Esc \\\\
.RS
Obetnij otaczaj±ce bia³e znaki.
.RE
.I Esc !
.RS
Wykonaj polecenie pow³oki.
.RE
.I Esc $
.RS
Sprawd¼ pisowniê s³owa przy pomocy ispell.
.RE
.I Ctrl-X ?
.RS
Poka¿ informacjê o wierszu/kolumnie.
.RE
.I `
.RS
quoted_insert --- wstaw nastêpny znak dos³ownie (klawisz odwrotnego apostrofu)
.RE
.I Esc s
.RS
Wypo¶rodkuj wiersz.
.RE
.I Esc u
.RS
Zamieñ s³owo na du¿e litery
.RE
.I Esc d
.RS
Zamieñ s³owo na ma³e litery.
.RE
.I Esc c
.RS
Zamieñ w s³owie pierwsz± literê na du¿±, resztê na ma³e.
.RE
.I Esc x
.RS
Przejd¼ do zachêty minibufora M-x z uzupe³nianiem poleceñ.
.RE
.I Ctrl-X Ctrl-B
.RS
Wy¶wietl rozwijaln± listê buforów.
.RE
.I Ctrl-X Ctrl-C
.RS
Zakoñcz pracê JED.
.RE
.I Ctrl-X 0
.RS
Usuñ bie¿±ce okno.
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
Prze³±cz na bufor.
.RE
.I Ctrl-X k
.RS
Usuñ bufor.
.RE
.I Ctrl-X s
.RS
Zapisz bufory.
.RE
.I Ctrl-X Esc
.RS
Przejd¼ do zachêty "S-Lang>" interfejsu interpretera S-Lang.
.RE
.I Esc .
.RS
Znajd¼ tag.
.RE
.I Ctrl-@
.RS
Ustaw znacznik (rozpocznij okre¶lanie obszaru). U¿yte z argumentem
przedrostkowym anuluje czynno¶æ definiowania i zdejmuje znacznik.
.\" pops the Mark.
.SH PLIKI
.I JED_ROOT/lib/*.sl
.RS
S± to domy¶lne pliki uruchomieniowe slang dla edytora jed.
.\" default runtime jed slang files
.RE
.I JED_ROOT/lib/site.sl
.RS
Domy¶lny plik inicjuj±cy (startup file).
.RE
.I /etc/jed.rc
.RS
Ogólnosystemowy plik konfiguracyjny.
.RE
.I ~/.jedrc
.RS
Plik konfiguracyjny danego u¿ytkownika.
.SH AUTOR
.I "John E. Davis" <davis@space.mit.edu>
.RS
Autor programu Jed.
.RE
.PP
--- Niniejszy dokument zosta³
.I przet³umaczony
na format nroff
przez "Boris D. Beletsky" <borik@isracom.co.il>
