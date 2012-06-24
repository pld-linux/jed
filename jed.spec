%define		jed_ver	B0.99-14
Summary:	A small fast editor
Summary(de):	Ein kleiner, schneller Editor 
Summary(fr):	Un petit �diteur rapide
Summary(pl):	Ma�y i szybki edytor
Summary(tr):	K���k, h�zl� bir metin d�zenleyici
Name:		jed
Version:	0.99.14
Release:	3
License:	GPL
Group:		Applications/Editors
Source0:	ftp://space.mit.edu/pub/davis/jed/v0.99/%{name}-%{jed_ver}.tar.bz2
Source1:	x%{name}.desktop
Source2:	%{name}.conf
Source3:	%{name}.1.pl
Source4:	rgrep.1.pl
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-XFree86_keys.patch
Patch2:		%{name}-home_etc.patch
patch3:		%{name}-info.patch
BuildRequires:	gpm-devel
BuildRequires:	slang-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jed is a fast compact editor based on the slang screen library. It has
special editing modes for C, C++, and other languages. It can emulate
Emacs, Wordstar, and other editors, and can be customized with slang
macros, colors, keybindings, etc.

%description -l de
Jed ist ein schneller, kompakter Editor, der auf der
Slang-Screen-Library basiert. Er besitzt spezielle Bearbeitungsmodi
f�r C, C++ und andere Sprachen, kann Emacs, Wordstar und weitere
Editoren emulieren und l��t sich mit Slang-Makros, Farben, Keybindings
usw. erweitern.

%description -l fr
Jed est un �diteur compact bas� sur la librairie slang. Il dispose de
modes d'�dition sp�ciaux pour C, C++, et d'autres langages. Il peut
�muler Emacs, Wordstar, et d'autres �diteurs, et peut �tre
personnalis� avec des macros slang, des couleurs, des combinaisons de
touches, etc.

%description -l pl
Jed jest niewielkim i szybkim edytorem bazuj�cym na bibliotece slang.
Ma on specjalne tryby edycji tekst�w w j�zykach C, C++ i innych. Mo�e
on tak�e emulowa� inne edytory jak Emacs czy Wordstar. Mo�e by� on w
pe�ni dostosowany do potrzeb u�ytkownika z u�yciem makr slanga daj�c
mo�liwo�� zmiany np. kolor�w czy mapowania klawiatury.

%description -l tr
Jed, k���k ve h�zl� bir metin d�zenleyicidir. C, C++ ve di�er diller
i�in �zel d�zenleme kiplerine sahiptir. Emacs ve Wordstar'�n
komutlar�n� taklit edebilir ve t�m yetenekleri kullan�c�ya g�re
ayarlanabilir.

%package xjed
Summary:	Jed editor - X version
Summary(de):	Jed-Editor - X-Version 
Summary(fr):	�diteur Jed - version X
Summary(pl):	Edytor jed - wersja dla X Window
Summary(tr):	Jed metin d�zenleyici - X s�r�m�
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}

%description xjed
Xjed is the same editor as jed, it just runs in its own X Window.

%description -l de xjed
Xjed ist der gleiche Editor wie jed, l�uft jedoch in einem eigenen
X-Window

%description -l fr xjed
Xjed est le m�me �diteur que jed, il tourne seulement sur X Window.

%description -l pl xjed
Xjed jest wersj� edytora jed pracuj�c� w X Window.

%description -l tr xjed
Jed metin d�zenleyicinin X alt�nda �al��an s�r�m�

%package -n rgrep
Summary:	recursive grep utility
Summary(de):	Rekursives grep-Utility-Programm
Summary(fr):	Utilitaire grep r�cursif
Summary(pl):	Rekursywna wersja narz�dzia grep
Summary(tr):	Rek�rsif bir grep s�r�m�
Group:		Applications/Text

%description -n rgrep
a recursive `grep' utility that can highlight the matching expression,
by the author of Jed.

%description -l de -n rgrep
ein rekursives `grep'-Dienstprogramm, das einen passenden Ausdruck
markieren kann. Vom Autor von Jed.

%description -l fr -n rgrep
grep r�cursif pouvant mettre en �vidence l'expression trouv�e, par
l'auteur de Jed.

%description -l pl -n rgrep
rgrep jest programem, kt�ry mo�e zaznacza� poszukiwane ci�gi znak�w w
bie��cym katalogu i podkatalogach �acz�cym w sobie cechy funkcjonalne
u�ywania pary program�w find i grep.

%description -l tr -n rgrep
Jed'in yazar�ndan rek�rsif buldu�u e�lemeleri i�aretleyebilen bir grep
s�r�m�.

%prep
%setup -q -n %{name}-%{jed_ver}
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1

mv -f autoconf/configure.in .
mv -f autoconf/aclocal.m4 acinclude.m4

%build
CFLAGS="-DMEMCPY=SLmemcpy -DMEMSET=SLmemset -DMEMCHR=SLmemchr %{rpmcflags}"
aclocal
autoconf
%configure

%{__make} all
%{__make} xjed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors \
	$RPM_BUILD_ROOT{%{_prefix}/X11R6/bin,%{_infodir},%{_sysconfdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install info/jed.* $RPM_BUILD_ROOT%{_infodir}

mv -f $RPM_BUILD_ROOT%{_bindir}/xjed $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/jed.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1/jed.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man1/rgrep.1

gzip -9nf README changes.txt doc/txt/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README.gz changes.txt.gz doc/txt/*.gz
%attr(755,root,root) %{_bindir}/jed
%{_datadir}/jed
%{_mandir}/man1/jed.*
%lang(pl) %{_mandir}/pl/man1/jed.*
%{_infodir}/*
%{_sysconfdir}/*

%files xjed
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/xjed
%{_applnkdir}/Development/Editors/xjed.desktop

%files -n rgrep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rgrep
%{_mandir}/man1/rgrep.*
%lang(pl) %{_mandir}/pl/man1/rgrep.*
