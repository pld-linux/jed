Summary:	A small fast editor
Summary(de):	Ein kleiner, schneller Editor 
Summary(fr):	Un petit éditeur rapide
Summary(pl):	Ma³y i szybki edytor
Summary(tr):	Küçük, hýzlý bir metin düzenleyici
Name:		jed
Version:	0.99.10
Release:	1
Copyright:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source0:	ftp://space.mit.edu/pub/davis/jed/%{name}-B0.99-10.tar.bz2
Source1:	xjed.desktop
Patch0:		jed-make.patch
Patch1:		jed-XFree86_keys.patch
Patch2:		jed-dft_syntax.patch
Patch3:		jed-DESTDIR.patch
Patch4:		jed-keymap.patch
Buildrequires:	gpm-devel
Buildrequires:	slang-devel
Buildrequires:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_applnkdir	/usr/X11R6/share/applnk/

%description
Jed is a fast compact editor based on the slang screen library. It has
special editing modes for C, C++, and other languages. It can emulate Emacs,
Wordstar, and other editors, and can be customized with slang macros,
colors, keybindings, etc.

%description -l de
Jed ist ein schneller, kompakter Editor, der auf der Slang-Screen-Library
basiert. Er besitzt spezielle Bearbeitungsmodi für C, C++ und andere Sprachen,
kann Emacs, Wordstar und weitere Editoren emulieren und läßt sich mit
Slang-Makros, Farben, Keybindings usw. erweitern.

%description -l fr
Jed est un éditeur compact basé sur la librairie slang. Il dispose de modes
d'édition spéciaux pour C, C++, et d'autres langages. Il peut émuler Emacs,
Wordstar, et d'autres éditeurs, et peut être personnalisé avec des macros
slang, des couleurs, des combinaisons de touches, etc.

%description -l pl
Jed jest niewielkim i szybkim edytorem bazuj±cym na bibliotece slang. Ma on
specjalne tryby edycji tekstów w jêzykach C, C++ i innych. Mo¿e on tak¿e
emulowaæ inne edytory jak Emacs czy Wordstar. Mo¿e byæ on w pe³ni
dostosowany do potrzeb u¿ytkownika z u¿yciem makr slanga daj±c mo¿liwo¶æ
zmiany np. kolorów czy mapowania klawiatury.

%description -l tr
Jed, küçük ve hýzlý bir metin düzenleyicidir. C, C++ ve diðer diller için özel
düzenleme kiplerine sahiptir. Emacs ve Wordstar'ýn komutlarýný taklit edebilir
ve tüm yetenekleri kullanýcýya göre ayarlanabilir.

%package xjed
Summary:	Jed editor - X version
Summary(de):	Jed-Editor - X-Version 
Summary(fr):	Éditeur Jed - version X
Summary(pl):	Edytor jed - wersja dla X Window
Summary(tr):	Jed metin düzenleyici - X sürümü
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Requires:	%{name} = %{version}

%description xjed
Xjed is the same editor as jed, it just runs in its own X Window.

%description -l de xjed
Xjed ist der gleiche Editor wie jed, läuft jedoch in einem eigenen X-Window

%description -l fr xjed
Xjed est le même éditeur que jed, il tourne seulement sur X Window.

%description -l pl xjed
Xjed jest wersj± edytora jed pracuj±c± w X Window.

%description -l tr xjed
Jed metin düzenleyicinin X altýnda çalýþan sürümü

%package -n rgrep
Summary:	recursive grep utility
Summary(de):	Rekursives grep-Utility-Programm
Summary(fr):	Utilitaire grep récursif.
Summary(pl):	Rekursywna wersja narzêdzia grep
Summary(tr):	Rekürsif bir grep sürümü
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst

%description -n rgrep
a recursive `grep' utility that can highlight the matching expression,
by the author of Jed.

%description -l de -n rgrep
ein rekursives `grep'-Dienstprogramm, das einen passenden Ausdruck markieren
kann. Vom Autor von Jed.

%description -l fr -n rgrep
grep récursif pouvant mettre en évidence l'expression trouvée, par l'auteur
de Jed.

%description -l pl -n rgrep
rgrep jest programem, który mo¿e zaznaczaæ poszukiwane ci±gi znaków w
bierz±cym katalogu i podkatalogach ³acz±cym w sobie cechy funkcjonalne
u¿ywania pary programów find i grep.

%description -l tr -n rgrep
Jed'in yazarýndan rekürsif bulduðu eþlemeleri iþaretleyebilen bir grep
sürümü.

%prep
%setup -q -n %{name}-B0.99-10
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
CFLAGS="-DMEMCPY=SLmemcpy -DMEMSET=SLmemset -DMEMCHR=SLmemchr $RPM_OPT_FLAGS"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure

make all
make xjed

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/usr/X11R6/bin,%{_applnkdir}/Editors}

make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/xjed $RPM_BUILD_ROOT/usr/X11R6/bin

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Editors

gzip -9nf README changes.txt \
	$RPM_BUILD_ROOT%{_mandir}/man1/* \
	$RPM_BUILD_ROOT%{_infodir}/*

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz changes.txt.gz doc/*.gz
%docdir %{_libdir}/jed/info
%{_mandir}/man1/jed.1*
%attr(755,root,root) %{_bindir}/jed
%dir %{_libdir}/jed
%{_infodir}/jed.info*.gz
%{_libdir}/jed/lib

%files xjed
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/xjed
%{_applnkdir}/Editors/xjed.desktop

%files -n rgrep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rgrep
%{_mandir}/man1/rgrep.1*
