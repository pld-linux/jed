%define		tar_ver	0.99-16
Summary:	A small fast editor
Summary(de):	Ein kleiner, schneller Editor
Summary(es):	Un pequeño y rápido editor
Summary(fr):	Un petit éditeur rapide
Summary(pl):	Ma³y i szybki edytor
Summary(pt_BR):	Um pequeno e rápido editor
Summary(ru):	âÙÓÔÒÙÊ ÎÅÂÏÌØÛÏÊ ÔÅËÓÔÏ×ÙÊ ÒÅÄÁËÔÏÒ ÎÁ ÏÓÎÏ×Å ÂÉÂÌÉÏÔÅËÉ slang
Summary(tr):	Küçük, hýzlý bir metin düzenleyici
Summary(uk):	û×ÉÄËÉÊ ËÏÍÐÁËÔÎÉÊ ÔÅËÓÔÏ×ÉÊ ÒÅÄÁËÔÏÒ ÎÁ ÂÁÚ¦ Â¦ÂÌ¦ÏÔÅËÉ slang
Name:		jed
Version:	0.99.16
Release:	4
License:	GPL
Group:		Applications/Editors
Source0:	ftp://space.mit.edu/pub/davis/jed/v0.99/%{name}-%{tar_ver}.tar.bz2
# Source0-md5:	c2bcd89c92a120559865a539c2705999
Source1:	x%{name}.desktop
Source2:	%{name}.conf
Source3:	%{name}.1.pl
Source4:	rgrep.1.pl
Source5:	x%{name}.png
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-XFree86_keys.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-info.patch
Patch4:		%{name}-ac_am.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	slang-devel >= 2.0.0
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jed is a fast compact editor based on the slang screen library. It has
special editing modes for C, C++, and other languages. It can emulate
Emacs, Wordstar, and other editors, and can be customized with slang
macros, colors, keybindings, etc.

%description -l de
Jed ist ein schneller, kompakter Editor, der auf der
Slang-Screen-Library basiert. Er besitzt spezielle Bearbeitungsmodi
für C, C++ und andere Sprachen, kann Emacs, Wordstar und weitere
Editoren emulieren und läßt sich mit Slang-Makros, Farben, Keybindings
usw. erweitern.

%description -l es
Jed es un editor compacto y rápido basado en la biblioteca slang.
Tiene modos de edición especiales para C, C++ y otros lenguajes. Puede
emular Emacs, Wordstar y otros editores, y se lo puede configurar con
macros slang, color, mapas de teclas, etc.

%description -l fr
Jed est un éditeur compact basé sur la librairie slang. Il dispose de
modes d'édition spéciaux pour C, C++, et d'autres langages. Il peut
émuler Emacs, Wordstar, et d'autres éditeurs, et peut être
personnalisé avec des macros slang, des couleurs, des combinaisons de
touches, etc.

%description -l pl
Jed jest niewielkim i szybkim edytorem bazuj±cym na bibliotece slang.
Ma on specjalne tryby edycji tekstów w jêzykach C, C++ i innych. Mo¿e
on tak¿e emulowaæ inne edytory jak Emacs czy Wordstar. Mo¿e byæ on w
pe³ni dostosowany do potrzeb u¿ytkownika z u¿yciem makr slanga daj±c
mo¿liwo¶æ zmiany np. kolorów czy mapowania klawiatury.

%description -l ru
Jed - ÜÔÏ ÂÙÓÔÒÙÊ ËÏÍÐÁËÔÎÙÊ ÔÅËÓÔÏ×ÙÊ ÒÅÄÁËÔÏÒ, ÏÓÎÏ×ÁÎÎÙÊ ÎÁ
ÜËÒÁÎÎÏÊ ÂÉÂÌÉÏÔÅËÅ SLang. ïÎ ÉÍÅÅÔ ÓÐÅÃÉÁÌØÎÙÅ ÒÅÖÉÍÙ ÒÅÄÁËÔÉÒÏ×ÁÎÉÑ
ÄÌÑ C, C++, É ÄÒÕÇÉÈ ÑÚÙËÏ×. Jed ÍÏÖÅÔ ÜÍÕÌÉÒÏ×ÁÔØ Emacs, Wordstar É
ÄÒÕÇÉÅ ÒÅÄÁËÔÏÒÙ É ÍÏÖÅÔ ÂÙÔØ ÎÁÓÔÒÏÅÎ ÄÌÑ ËÏÎËÒÅÔÎÙÈ ÕÓÌÏ×ÉÊ
ÉÓÐÏÌØÚÕÑ ÍÁËÒÏÓÙ, Ã×ÅÔÁ, ÐÒÉ×ÑÚËÉ ËÌÁ×ÉÁÔÕÒÙ É Ô.Ð. ÉÚ SLang.

%description -l pt_BR
Jed é um editor compacto e rápido baseado na biblioteca slang. Ele tem
modos de edição especiais para C, C++ e outras linguagens. Pode emular
Emacs, Wordstar e outros editores, podendo ser configurado com macros
slang, cores, mapeamento de teclas, etc.

%description -l tr
Jed, küçük ve hýzlý bir metin düzenleyicidir. C, C++ ve diðer diller
için özel düzenleme kiplerine sahiptir. Emacs ve Wordstar'ýn
komutlarýný taklit edebilir ve tüm yetenekleri kullanýcýya göre
ayarlanabilir.

%description -l uk
Jed - ÃÅ Û×ÉÄËÉÊ ËÏÍÐÁËÔÎÉÊ ÔÅËÓÔÏ×ÉÊ ÒÅÄÁËÔÏÒ, ÂÁÚÏ×ÁÎÉÊ ÎÁ ÅËÒÁÎÎ¦Ê
Â¦ÂÌ¦ÏÔÅÃ¦ SLang. ÷¦Î ÍÁ¤ ÓÐÅÃ¦ÁÌØÎ¦ ÒÅÖÉÍÉ ÒÅÄÁÇÕ×ÁÎÎÑ ÄÌÑ C, C++ ÔÁ
¦ÎÛÉÈ ÍÏ×. Jed ÍÏÖÅ ÅÍÕÌÀ×ÁÔÉ Emacs, Wordstar ÔÁ ¦ÎÛ¦ ÒÅÄÁËÔÏÒÉ ¦ ÍÏÖÅ
ÂÕÔÉ ÎÁÓÔÒÏ¤ÎÉÊ ÎÁ Ò¦×Î¦ ÍÁËÒÏÓ¦×, ËÏÌØÏÒ¦×, ÐÒÉ×'ÑÚËÉ ËÌÁ×¦Û ¦ Ô.Ð.

%package xjed
Summary:	Jed editor - X version
Summary(de):	Jed-Editor - X-Version
Summary(es):	Editor Jed - versión X
Summary(fr):	Éditeur Jed - version X
Summary(pl):	Edytor jed - wersja dla X Window
Summary(pt_BR):	Editor Jed - versão X
Summary(ru):	òÅÄÁËÔÏÒ Jed - ×ÅÒÓÉÑ ÄÌÑ X Window
Summary(tr):	Jed metin düzenleyici - X sürümü
Summary(uk):	òÅÄÁËÔÏÒ Jed - ×ÅÒÓ¦Ñ ÄÌÑ X Window
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}-%{release}

%description xjed
Xjed is the same editor as jed, it just runs in its own X Window.

%description xjed -l de
Xjed ist der gleiche Editor wie jed, läuft jedoch in einem eigenen
X-Window

%description xjed -l es
Xjed es el editor jed para X Window.

%description xjed -l fr
Xjed est le même éditeur que jed, il tourne seulement sur X Window.

%description xjed -l pl
Xjed jest wersj± edytora jed pracuj±c± w X Window.

%description xjed -l pt_BR
Xjed é o editor jed para X Window.

%description xjed -l ru
Xjed - ÜÔÏ ÔÏÔ ÖÅ ÒÅÄÁËÔÏÒ, ÞÔÏ É jed, ÔÏÌØËÏ ÒÁÂÏÔÁÀÝÉÊ × ÓÏÂÓÔ×ÅÎÎÏÍ
X-ÏËÎÅ.

%description xjed -l tr
Jed metin düzenleyicinin X altýnda çalýþan sürümü.

%description xjed -l uk
Xjed - ÃÅ ÔÏÊ ÖÅ ÒÅÄÁËÔÏÒ, ÝÏ Ê jed, Ô¦ÌØËÉ ÐÒÁÃÀÀÞÉÊ Õ ×ÌÁÓÎÏÍÕ
X-×¦ËÎ¦.

%package -n rgrep
Summary:	Recursive grep utility
Summary(de):	Rekursives grep-Utility-Programm
Summary(es):	Utilitario grep recursivo
Summary(fr):	Utilitaire grep récursif
Summary(pl):	Rekursywna wersja narzêdzia grep
Summary(pt_BR):	Utilitário grep recursivo
Summary(ru):	òÅËÕÒÓÉ×ÎÁÑ ÕÔÉÌÉÔÁ grep
Summary(tr):	Rekürsif bir grep sürümü
Summary(uk):	òÅËÕÒÓÉ×ÎÁ ÕÔÉÌ¦ÔÁ grep
Group:		Applications/Text

%description -n rgrep
A recursive `grep' utility that can highlight the matching expression,
by the author of Jed.

%description -n rgrep -l de
Ein rekursives `grep'-Dienstprogramm, das einen passenden Ausdruck
markieren kann. Vom Autor von Jed.

%description -n rgrep -l es
Utilitario grep recursivo que puede destacar la expresión encontrada,
escrito por el autor del editor Jed.

%description -n rgrep -l fr
grep récursif pouvant mettre en évidence l'expression trouvée, par
l'auteur de Jed.

%description -n rgrep -l pl
rgrep jest programem, który mo¿e zaznaczaæ poszukiwane ci±gi znaków w
bie¿±cym katalogu i podkatalogach ³±cz±cym w sobie cechy funkcjonalne
u¿ywania pary programów find i grep.

%description -n rgrep -l pt_BR
Utilitário grep recursivo que pode destacar a expressão encontrada,
escrito pelo autor do editor Jed.

%description -n rgrep -l ru
òÅËÕÒÓÉ×ÎÁÑ ÕÔÉÌÉÔÁ grep, ÕÍÅÀÝÁÑ ÐÏÄÓ×ÅÞÉ×ÁÔØ ÎÁÊÄÅÎÎÙÅ ×ÙÒÁÖÅÎÉÑ.

%description -n rgrep -l tr
Jed'in yazarýndan rekürsif bulduðu eþlemeleri iþaretleyebilen bir grep
sürümü.

%description -n rgrep -l uk
òÅËÕÒÓÉ×ÎÁ ÕÔÉÌ¦ÔÁ grep, ÝÏ ×Í¦¤ Ð¦ÄÓ×¦ÞÕ×ÁÔÉ ÚÎÁÊÄÅÎ¦ ×ÉÒÁÚÉ

%prep
%setup -q -n %{name}-%{tar_ver}
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
mv -f autoconf/configure.in .
mv -f autoconf/aclocal.m4 acinclude.m4
CFLAGS="-DMEMCPY=SLmemcpy -DMEMSET=SLmemset -DMEMCHR=SLmemchr %{rpmcflags}"
%{__aclocal}
%{__autoconf}
%configure

%{__make} all
%{__make} xjed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_infodir},%{_sysconfdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install info/jed.* $RPM_BUILD_ROOT%{_infodir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/jed.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1/jed.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man1/rgrep.1
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README changes.txt doc/txt/*.txt
%attr(755,root,root) %{_bindir}/jed
%{_datadir}/jed
%{_mandir}/man1/jed.1*
%lang(pl) %{_mandir}/pl/man1/jed.1*
%{_infodir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%files xjed
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xjed
%{_desktopdir}/xjed.desktop
%{_pixmapsdir}/*.png

%files -n rgrep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rgrep
%{_mandir}/man1/rgrep.1*
%lang(pl) %{_mandir}/pl/man1/rgrep.1*
