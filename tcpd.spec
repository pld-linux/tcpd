Summary:	tcpd - full replacement for tcp_wrappers
Summary(pl):	tcpd - pe³ny zamiennik tcp_wrappers
Name:		tcpd
Version:	0.0.2
Release:	1
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracja
License:	BSD-like
Vendor:		PLD GNU/Linux Team ( http://www.pld.org.pl/ )
URL:		http://cvsweb.pld.org.pl/index.cgi/tcpd/
Source0:	ftp://ftp.pld.org.pl/software/%{name}/%{name}-%{version}.tar.gz
PreReq:		%{name}-lib
Requires:	%{name}-lib = %{version}
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_libexecdir	%{_sbindir}

%description
The %{name} package provides small daemon programs which can
monitor and filter incoming requests for systat, finger, FTP, telnet,
ssh, rlogin, rsh, exec, tftp, talk and other network services.

Install the %{name} program if you need a security tool for
filtering incoming network services requests.

%description -l pl
Pakiet %{name} dostarcza niewielki program, który pozwala na monitorowanie
oraz filtrowania nadchodz±cych po³±czeñ do us³ug takich jak systat, finger,
FTP, telnet, ssh, rlogin, rsh, exec, tftp, talk oraz innych us³ug sieciowych.

%package lib
Summary:	libwrap replacement
Summary(pl):	Zamiennik libwrap
Group:		Libraries
Group(pl):	Biblioteki
Obsoletes:	libwrap

%description lib
Full tcp_wrappers libwrap replacement with IPv6 support
and other features.

%description lib -l pl
Pe³ny zamiennik biblioteki libwrap pochodz±cej z pakietu tcp_wrappers.
Zamiennik oferuje ponadto wsparcie dla IPv6 i inne dodatki.

%package devel
Summary:	Headers files and development library for tcp-lib
Summary(pl):	Pliki nag³ówkowe i biblioteki do programowania
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-lib = %{version}
Obsoletes:	libwrap-devel
Provides:	libwrap-devel <= 7.6

%description devel
Headers files and development library for tcpd-lib.

%description devel -l pl
Pliki nag³ówkowe i biblioteki do programowania
z u¿yciem biblioteki tcpd-lib.

%package static
Summary:	Static library
Summary(pl):	Biblioteka statyczna
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Obsoletes:	libwrap-static <= 7.6

%description static
Static library tcpd-lib.

%description static -l pl
Biblioteka statyczna tcpd-lib.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README NEWS AUTHORS COPYING ChangeLog \
	doc/MEMO doc/hosts.access

%post 	lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
