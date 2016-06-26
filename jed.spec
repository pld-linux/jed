#
# Conditional build:
%bcond_without	gtk	# GTK+ (2.x) version of jed
#
%define		tar_ver	0.99-19
Summary:	A small fast editor
Summary(de.UTF-8):	Ein kleiner, schneller Editor
Summary(es.UTF-8):	Un pequeño y rápido editor
Summary(fr.UTF-8):	Un petit éditeur rapide
Summary(pl.UTF-8):	Mały i szybki edytor
Summary(pt_BR.UTF-8):	Um pequeno e rápido editor
Summary(ru.UTF-8):	Быстрый небольшой текстовый редактор на основе библиотеки slang
Summary(tr.UTF-8):	Küçük, hızlı bir metin düzenleyici
Summary(uk.UTF-8):	Швидкий компактний текстовий редактор на базі бібліотеки slang
Name:		jed
Version:	0.99.19
Release:	2
License:	GPL v2+
Group:		Applications/Editors
Source0:	http://www.jedsoft.org/releases/jed/%{name}-%{tar_ver}.tar.bz2
# Source0-md5:	c9b2f58a3defc6f61faa1ce7d6d629ea
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
URL:		http://www.jedsoft.org/jed/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gpm-devel
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2:2.8.0}
BuildRequires:	pkgconfig >= 1:0.14.0
BuildRequires:	slang-devel >= 2.0.0
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jed is a fast compact editor based on the slang screen library. It has
special editing modes for C, C++, and other languages. It can emulate
Emacs, Wordstar, and other editors, and can be customized with slang
macros, colors, keybindings, etc.

%description -l de.UTF-8
Jed ist ein schneller, kompakter Editor, der auf der
Slang-Screen-Library basiert. Er besitzt spezielle Bearbeitungsmodi
für C, C++ und andere Sprachen, kann Emacs, Wordstar und weitere
Editoren emulieren und läßt sich mit Slang-Makros, Farben, Keybindings
usw. erweitern.

%description -l es.UTF-8
Jed es un editor compacto y rápido basado en la biblioteca slang.
Tiene modos de edición especiales para C, C++ y otros lenguajes. Puede
emular Emacs, Wordstar y otros editores, y se lo puede configurar con
macros slang, color, mapas de teclas, etc.

%description -l fr.UTF-8
Jed est un éditeur compact basé sur la librairie slang. Il dispose de
modes d'édition spéciaux pour C, C++, et d'autres langages. Il peut
émuler Emacs, Wordstar, et d'autres éditeurs, et peut être
personnalisé avec des macros slang, des couleurs, des combinaisons de
touches, etc.

%description -l pl.UTF-8
Jed jest niewielkim i szybkim edytorem bazującym na bibliotece slang.
Ma on specjalne tryby edycji tekstów w językach C, C++ i innych. Może
on także emulować inne edytory jak Emacs czy Wordstar. Może być on w
pełni dostosowany do potrzeb użytkownika z użyciem makr slanga dając
możliwość zmiany np. kolorów czy mapowania klawiatury.

%description -l ru.UTF-8
Jed - это быстрый компактный текстовый редактор, основанный на
экранной библиотеке SLang. Он имеет специальные режимы редактирования
для C, C++, и других языков. Jed может эмулировать Emacs, Wordstar и
другие редакторы и может быть настроен для конкретных условий
используя макросы, цвета, привязки клавиатуры и т.п. из SLang.

%description -l pt_BR.UTF-8
Jed é um editor compacto e rápido baseado na biblioteca slang. Ele tem
modos de edição especiais para C, C++ e outras linguagens. Pode emular
Emacs, Wordstar e outros editores, podendo ser configurado com macros
slang, cores, mapeamento de teclas, etc.

%description -l tr.UTF-8
Jed, küçük ve hızlı bir metin düzenleyicidir. C, C++ ve diğer diller
için özel düzenleme kiplerine sahiptir. Emacs ve Wordstar'ın
komutlarını taklit edebilir ve tüm yetenekleri kullanıcıya göre
ayarlanabilir.

%description -l uk.UTF-8
Jed - це швидкий компактний текстовий редактор, базований на екранній
бібліотеці SLang. Він має спеціальні режими редагування для C, C++ та
інших мов. Jed може емулювати Emacs, Wordstar та інші редактори і може
бути настроєний на рівні макросів, кольорів, прив'язки клавіш і т.п.

%package gtk
Summary:	GTK+ version of Jed editor
Summary(pl.UTF-8):	Wersja GTK+ edytora Jed
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.8.0

%description gtk
GTK+ version of Jed editor.

%description gtk -l pl.UTF-8
Wersja GTK+ edytora Jed.

%package xjed
Summary:	Jed editor - X version
Summary(de.UTF-8):	Jed-Editor - X-Version
Summary(es.UTF-8):	Editor Jed - versión X
Summary(fr.UTF-8):	Éditeur Jed - version X
Summary(pl.UTF-8):	Edytor jed - wersja dla X Window
Summary(pt_BR.UTF-8):	Editor Jed - versão X
Summary(ru.UTF-8):	Редактор Jed - версия для X Window
Summary(tr.UTF-8):	Jed metin düzenleyici - X sürümü
Summary(uk.UTF-8):	Редактор Jed - версія для X Window
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}-%{release}

%description xjed
Xjed is the same editor as jed, it just runs in its own X Window.

%description xjed -l de.UTF-8
Xjed ist der gleiche Editor wie jed, läuft jedoch in einem eigenen
X-Window

%description xjed -l es.UTF-8
Xjed es el editor jed para X Window.

%description xjed -l fr.UTF-8
Xjed est le même éditeur que jed, il tourne seulement sur X Window.

%description xjed -l pl.UTF-8
Xjed jest wersją edytora jed pracującą w X Window.

%description xjed -l pt_BR.UTF-8
Xjed é o editor jed para X Window.

%description xjed -l ru.UTF-8
Xjed - это тот же редактор, что и jed, только работающий в собственном
X-окне.

%description xjed -l tr.UTF-8
Jed metin düzenleyicinin X altında çalışan sürümü.

%description xjed -l uk.UTF-8
Xjed - це той же редактор, що й jed, тільки працюючий у власному
X-вікні.

%package -n rgrep
Summary:	Recursive grep utility
Summary(de.UTF-8):	Rekursives grep-Utility-Programm
Summary(es.UTF-8):	Utilitario grep recursivo
Summary(fr.UTF-8):	Utilitaire grep récursif
Summary(pl.UTF-8):	Rekursywna wersja narzędzia grep
Summary(pt_BR.UTF-8):	Utilitário grep recursivo
Summary(ru.UTF-8):	Рекурсивная утилита grep
Summary(tr.UTF-8):	Rekürsif bir grep sürümü
Summary(uk.UTF-8):	Рекурсивна утиліта grep
Group:		Applications/Text

%description -n rgrep
A recursive `grep' utility that can highlight the matching expression,
by the author of Jed.

%description -n rgrep -l de.UTF-8
Ein rekursives `grep'-Dienstprogramm, das einen passenden Ausdruck
markieren kann. Vom Autor von Jed.

%description -n rgrep -l es.UTF-8
Utilitario grep recursivo que puede destacar la expresión encontrada,
escrito por el autor del editor Jed.

%description -n rgrep -l fr.UTF-8
grep récursif pouvant mettre en évidence l'expression trouvée, par
l'auteur de Jed.

%description -n rgrep -l pl.UTF-8
rgrep jest programem, który może zaznaczać poszukiwane ciągi znaków w
bieżącym katalogu i podkatalogach łączącym w sobie cechy funkcjonalne
używania pary programów find i grep.

%description -n rgrep -l pt_BR.UTF-8
Utilitário grep recursivo que pode destacar a expressão encontrada,
escrito pelo autor do editor Jed.

%description -n rgrep -l ru.UTF-8
Рекурсивная утилита grep, умеющая подсвечивать найденные выражения.

%description -n rgrep -l tr.UTF-8
Jed'in yazarından rekürsif bulduğu eşlemeleri işaretleyebilen bir grep
sürümü.

%description -n rgrep -l uk.UTF-8
Рекурсивна утиліта grep, що вміє підсвічувати знайдені вирази

%prep
%setup -q -n %{name}-%{tar_ver}
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp -f /usr/share/automake/config.* autoconf
cd autoconf
%{__autoconf}
%{__mv} configure ..
cd ..
CFLAGS="-DMEMCPY=SLmemcpy -DMEMSET=SLmemset -DMEMCHR=SLmemchr %{rpmcflags}"
%configure \
	%{?with_gtk:--with-gtk} \
	--with-slanginc=/usr/include/slang \
	--with-slanglib=%{_libdir}

%{__make} all
%{__make} xjed
%{?with_gtk:%{__make} -C src gtkjed}
%{__make} rgrep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_infodir},%{_sysconfdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_gtk:install src/objs/gtkjed $RPM_BUILD_ROOT%{_bindir}}
install src/objs/rgrep $RPM_BUILD_ROOT%{_bindir}
cp -p info/jed.info info/jed.?in $RPM_BUILD_ROOT%{_infodir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/jed.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1/jed.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man1/rgrep.1
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README changes.txt doc/txt/*.txt
%attr(755,root,root) %{_bindir}/jed
%attr(755,root,root) %{_bindir}/jed-script
%{_datadir}/jed
%{_mandir}/man1/jed.1*
%lang(pl) %{_mandir}/pl/man1/jed.1*
%{_infodir}/jed.info*
%{_infodir}/jed.[0-9]in*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/jed.conf

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtkjed

%files xjed
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xjed
%{_desktopdir}/xjed.desktop
%{_pixmapsdir}/xjed.png

%files -n rgrep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rgrep
%{_mandir}/man1/rgrep.1*
%lang(pl) %{_mandir}/pl/man1/rgrep.1*
