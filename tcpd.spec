Summary:	tcpd - full replacement for tcp_wrappers
Summary(pl):	tcpd - pe³ny zamiennik tcp_wrappers
Name:		tcpd
Version:	0.1.1
Release:	3
License:	BSD-like
Vendor:		PLD GNU/Linux Team ( http://www.pld.org.pl/ )
Group:		Networking/Admin
Source0:	ftp://ftp.pld.org.pl/software/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	93612c68b5eed5f3ee90422b82193d0a
Patch0:		%{name}-SA_LEN.patch
URL:		http://cvsweb.pld.org.pl/index.cgi/tcpd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Prereq:		%{name}-lib = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_sbindir}

%description
The %{name} package provides small daemon programs which can monitor
and filter incoming requests for systat, finger, FTP, telnet, ssh,
rlogin, rsh, exec, tftp, talk and other network services.

Install the %{name} program if you need a security tool for filtering
incoming network services requests.

%description -l pl
Pakiet %{name} dostarcza niewielki program, który pozwala na
monitorowanie oraz filtrowania nadchodz±cych po³±czeñ do us³ug takich
jak systat, finger, FTP, telnet, ssh, rlogin, rsh, exec, tftp, talk
oraz innych us³ug sieciowych.

%package lib
Summary:	libwrap replacement
Summary(pl):	Zamiennik libwrap
Group:		Libraries
Obsoletes:	libwrap
Provides:	libwrap

%description lib
Full tcp_wrappers libwrap replacement with IPv6 support and other
features.

%description lib -l pl
Pe³ny zamiennik biblioteki libwrap pochodz±cej z pakietu tcp_wrappers.
Zamiennik oferuje ponadto wsparcie dla IPv6 i inne dodatki.

%package devel
Summary:	Headers files and development library for tcp-lib
Summary(pl):	Pliki nag³ówkowe i biblioteki do programowania
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}
Obsoletes:	libwrap-devel
Provides:	libwrap-devel <= 7.6

%description devel
Headers files and development library for tcpd-lib.

%description devel -l pl
Pliki nag³ówkowe i biblioteki do programowania z u¿yciem biblioteki
tcpd-lib.

%package static
Summary:	tcpd static library
Summary(pl):	Biblioteka statyczna tcpd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	libwrap-static <= 7.6

%description static
Static library tcpd-lib.

%description static -l pl
Biblioteka statyczna tcpd-lib.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_sysconfdir}/hosts.access

%clean
rm -rf $RPM_BUILD_ROOT

%post 	lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS COPYING ChangeLog doc/MEMO doc/hosts.access
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%files lib
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hosts.access
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
