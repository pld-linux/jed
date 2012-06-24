Summary:	A small fast editor
Summary(de):	Ein kleiner, schneller Editor 
Summary(fr):	Un petit �diteur rapide
Summary(pl):	Ma�y i szybki edytor
Summary(tr):	K���k, h�zl� bir metin d�zenleyici
Name:		jed
Version:	0.99.8
Release:	2
Copyright:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source0:	ftp://space.mit.edu/pub/davis/jed/%{name}-B0.99-8.tar.bz2
Source1:	xjed.desktop
Patch0:		jed-make.patch
Patch1:		jed-XFree86_keys.patch
Patch2:		jed-dft_syntax.patch
Buildrequires:	gpm-devel
Buildrequires:	slang-devel
Buildrequires:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Jed is a fast compact editor based on the slang screen library. It has
special editing modes for C, C++, and other languages. It can emulate Emacs,
Wordstar, and other editors, and can be customized with slang macros,
colors, keybindings, etc.

%description -l de
Jed ist ein schneller, kompakter Editor, der auf der Slang-Screen-Library
basiert. Er besitzt spezielle Bearbeitungsmodi f�r C, C++ und andere Sprachen,
kann Emacs, Wordstar und weitere Editoren emulieren und l��t sich mit
Slang-Makros, Farben, Keybindings usw. erweitern.

%description -l fr
Jed est un �diteur compact bas� sur la librairie slang. Il dispose de modes
d'�dition sp�ciaux pour C, C++, et d'autres langages. Il peut �muler Emacs,
Wordstar, et d'autres �diteurs, et peut �tre personnalis� avec des macros
slang, des couleurs, des combinaisons de touches, etc.

%description -l pl
Jed jest niewielkim i szybkim edytorem bazuj�cym na bibliotece slang. Ma on
specjalne tryby edycji tekst�w w j�zykach C, C++ i innych. Mo�e on tak�e
emulowa� inne edytory jak Emacs czy Wordstar. Mo�e by� on w pe�ni
dostosowany do potrzeb u�ytkownika z u�yciem makr slanga daj�c mo�liwo��
zmiany np. kolor�w czy mapowania klawiatury.

%description -l tr
Jed, k���k ve h�zl� bir metin d�zenleyicidir. C, C++ ve di�er diller i�in �zel
d�zenleme kiplerine sahiptir. Emacs ve Wordstar'�n komutlar�n� taklit edebilir
ve t�m yetenekleri kullan�c�ya g�re ayarlanabilir.

%package xjed
Summary:	Jed editor - X version
Summary(de):	Jed-Editor - X-Version 
Summary(fr):	�diteur Jed - version X
Summary(pl):	Edytor jed - wersja dla X Window
Summary(tr):	Jed metin d�zenleyici - X s�r�m�
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Requires:	%{name} = %{version}

%description xjed
Xjed is the same editor as jed, it just runs in its own X Window.

%description -l de xjed
Xjed ist der gleiche Editor wie jed, l�uft jedoch in einem eigenen X-Window

%description -l fr xjed
Xjed est le m�me �diteur que jed, il tourne seulement sur X Window.

%description -l pl xjed
Xjed jest wersj� edytora jed pracuj�c� w X Window.

%description -l tr xjed
Jed metin d�zenleyicinin X alt�nda �al��an s�r�m�

%package -n rgrep
Summary:	recursive grep utility
Summary(de):	Rekursives grep-Utility-Programm
Summary(fr):	Utilitaire grep r�cursif.
Summary(pl):	Rekursywna wersja narz�dzia grep
Summary(tr):	Rek�rsif bir grep s�r�m�
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst

%description -n rgrep
a recursive `grep' utility that can highlight the matching expression,
by the author of Jed.

%description -l de -n rgrep
ein rekursives `grep'-Dienstprogramm, das einen passenden Ausdruck markieren
kann. Vom Autor von Jed.

%description -l fr -n rgrep
grep r�cursif pouvant mettre en �vidence l'expression trouv�e, par l'auteur
de Jed.

%description -l pl -n rgrep
rgrep jest programem, kt�ry mo�e zaznacza� poszukiwane ci�gi znak�w w
bierz�cym katalogu i podkatalogach �acz�cym w sobie cechy funkcjonalne
u�ywania pary program�w find i grep.

%description -l tr -n rgrep
Jed'in yazar�ndan rek�rsif buldu�u e�lemeleri i�aretleyebilen bir grep
s�r�m�.

%prep
%setup -q -n %{name}-B0.99-8
%patch0 -p1
%patch1 -p1

%build
CFLAGS="-DMEMCPY=SLmemcpy -DMEMSET=SLmemset -DMEMCHR=SLmemchr $RPM_OPT_FLAGS"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure

make all
make xjed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1,%{_libdir}/jed} \
	$RPM_BUILD_ROOT/usr/X11R6/{bin,share/applnk/Editors}

cp -r lib  $RPM_BUILD_ROOT%{_libdir}/jed
cp -r info $RPM_BUILD_ROOT%{_libdir}/jed

install -s src/objs/{jed,rgrep} $RPM_BUILD_ROOT%{_bindir}
install -s src/objs/xjed 	$RPM_BUILD_ROOT/usr/X11R6/bin
install doc/{jed.1,rgrep.1} 	$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Editors

gzip -9nf doc/{*.txt,README} README changes.txt \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc README.gz changes.txt.gz
%docdir %{_libdir}/jed/info
%{_mandir}/man1/jed.1*
%attr(755,root,root) %{_bindir}/jed
%dir %{_libdir}/jed
%dir %{_libdir}/jed/info
%dir %{_libdir}/jed/lib
%{_libdir}/jed/info/*
%{_libdir}/jed/lib/*

%files xjed
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/xjed
/usr/X11R6/share/applnk/Editors/xjed.desktop

%files -n rgrep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rgrep
%{_mandir}/man1/rgrep.1*
