Summary:     A small fast editor
Summary(de): Ein kleiner, schneller Editor 
Summary(fr): Un petit éditeur rapide
Summary(pl): Ma³y i szybki edytor
Summary(tr): Küçük, hýzlý bir metin düzenleyici
Name:        jed
Version:     0.98.7
Release:     1
Copyright:   GPL
Group:       Applications/Editors
Source0:     ftp://space.mit.edu/pub/davis/jed/%{name}0.98-7.tar.gz
Source1:     xjed.wmconfig
Patch0:      jed-make.patch
Patch1:      jed-XFree86_keys.patch
Patch2:      jed-dft_syntax.patch
Buildroot:   /tmp/%{name}-%{version}-root

%description
Jed is a fast compact editor based on the slang screen library. It has
special editing modes for C, C++, and other languages.  It can emulate
Emacs, Wordstar, and other editors, and can be customized with slang
macros, colors, keybindings, etc.

%description -l de
Jed ist ein schneller, kompakter Editor, der auf der Slang-Screen-Library
basiert. Er besitzt spezielle Bearbeitungsmodi für C, C++ und andere Sprachen,
kann Emacs, Wordstar und weitere Editoren emulieren und läßt sich mit
Slang-Makros, Farben, Keybindings usw. erweitern.

%description -l fr
Jed est un éditeur compact basé sur la librairie slang. Il dispose de 
modes d'édition spéciaux pour C, C++, et d'autres langages. Il peut
émuler Emacs, Wordstar, et d'autres éditeurs, et peut être personnalisé
avec des macros slang, des couleurs, des combinaisons de touches, etc.

%description -l pl
Jed jest niewielkim i szybkim edytorem bazuj±cym na bibliotece slang.
Ma on specjalne tryby edycji tekstów jezykach C, C++ i innych. Mo¿e on
tak¿e emulowaæ inne edytory jak Emacs, Wordstar i inne. Mo¿e byæ on w pe³ni
dostosowany do potrzeb u¿ytkownika z u¿yciem makr slanga daj±c mo¿liwo¶æ
zmiany np. kolorów czy mapowania klawiatury itp.

%description -l tr
Jed, küçük ve hýzlý bir metin düzenleyicidir. C, C++ ve diðer diller için özel
düzenleme kiplerine sahiptir. Emacs ve Wordstar'ýn komutlarýný taklit edebilir
ve tüm yetenekleri kullanýcýya göre ayarlanabilir.

%package xjed
Summary:     Jed editor - X version
Summary(de): Jed-Editor - X-Version 
Summary(fr): Éditeur Jed - version X
Summary(pl): Edytor jed - wersja pod X Window
Summary(tr): Jed metin düzenleyici - X sürümü
Group:       Applications/Editors
Requires:    %{name} = %{version}

%description xjed
Xjed is the same editor as jed, it just runs in its own X Window.

%description -l de xjed
Xjed ist der gleiche Editor wie jed, läuft jedoch in einem eigenen 
X-Window

%description -l fr xjed
Xjed est le même éditeur que jed, il tourne seulement sur X Window.

%description -l pl xjed
Xjed jest wersj± pracuj±c± po X Window edytora jed.

%description -l tr xjed
Jed metin düzenleyicinin X altýnda çalýþan sürümü

%package -n rgrep
Summary:     recursive grep utility
Summary(de): Rekursives grep-Utility-Programm
Summary(fr): Utilitaire grep récursif.
Summary(pl): Rekursywna wersja narzêdzie grep
Summary(tr): Rekürsif bir grep sürümü
Group:       Utilities/Text

%description -n rgrep
a recursive `grep' utility that can highlight the matching expression,
by the author of Jed.

%description -l de -n rgrep
ein rekursives `grep'-Dienstprogramm, das einen passenden Ausdruck
markieren kann. Vom Autor von Jed.

%description -l fr -n rgrep
grep récursif pouvant mettre en évidence l'expression trouvée, par
l'auteur de Jed.

%description -l pl -n rgrep
rgrep jest programem, które mo¿e zaznaczaæ poszukiwane ci±gi znaków w
bierz±cym katalogu i podkatalogach ³acz±cym w sobie cechy funkcjonalne
u¿ywania pary programów find i grep.

%description -l tr -n rgrep
Jed'in yazarýndan rekürsif bulduðu eþlemeleri iþaretleyebilen bir grep
sürümü.

%prep
%setup -q -n jed
%patch0 -p1
%patch1 -p1

%build
CFLAGS="-DMEMCPY=SLmemcpy -DMEMSET=SLmemset -DMEMCHR=SLmemchr $RPM_OPT_FLAGS" \
LDFLAGS=-s \
./configure %{_target} \
	--prefix=/usr
make all
make xjed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{/etc/X11/wmconfig,usr/{bin,man/man1,lib/jed,X11R6/bin}}

cp -r lib $RPM_BUILD_ROOT/usr/lib/jed
cp -r info $RPM_BUILD_ROOT/usr/lib/jed

install -s src/objs/{jed,rgrep} $RPM_BUILD_ROOT/usr/bin
install -s src/objs/xjed $RPM_BUILD_ROOT/usr/X11R6/bin

install doc/{jed.1,rgrep.1} $RPM_BUILD_ROOT/usr/man/man1

install $RPM_SOURCE_DIR/xjed.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/xjed

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc doc README changes.txt
%docdir /usr/lib/jed/info
%attr(644, root,  man) /usr/man/man1/jed.1
%attr(755, root, root) /usr/bin/jed
%dir /usr/lib/jed
%dir /usr/lib/jed/info
%dir /usr/lib/jed/lib
/usr/lib/jed/info/*
/usr/lib/jed/lib/*

%files xjed
%attr(755, root, root) /usr/X11R6/bin/xjed
%attr(644, root, root) %config(missingok) /etc/X11/wmconfig/xjed

%files -n rgrep
%attr(755, root, root) /usr/bin/rgrep
%attr(644, root,  man) /usr/man/man1/rgrep.1

%changelog
* Wed Jun 17 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.98.7-1]
- added -q %setup parameter,
- added using %%{name} macro in Source,
- spec file rewritten for using Buildroot,
- added %clean section,
- added pl translation,
- added LDFLAGS=-s (for dynamic linking with slang),
- added patch for enable by default highlight syntax,
- removed not neccesary now patches,
- changed Group in rgrep to Utilities/Text,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- added wmconfig entry for xjed

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated to 0.98.4
- included man pages in file lists

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
