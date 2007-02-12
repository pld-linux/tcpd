Summary:	tcpd - full replacement for tcp_wrappers
Summary(pl.UTF-8):	tcpd - pełny zamiennik tcp_wrappers
Name:		tcpd
Version:	0.2.0
Release:	1
License:	BSD-like
Vendor:		PLD Linux Team ( http://www.pld-linux.org/ )
Group:		Networking/Admin
Source0:	ftp://ftp.pld-linux.org/software/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	ad0f15047c349dad98336e00fdb4f83e
URL:		http://cvs.pld-linux.org/tcpd/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.5
BuildRequires:	libtool
PreReq:		%{name}-lib = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_sbindir}

%description
The %{name} package provides small daemon programs which can monitor
and filter incoming requests for systat, finger, FTP, telnet, ssh,
rlogin, rsh, exec, tftp, talk and other network services.

Install the %{name} program if you need a security tool for filtering
incoming network services requests.

%description -l pl.UTF-8
Pakiet %{name} dostarcza niewielki program, który pozwala na
monitorowanie oraz filtrowania nadchodzących połączeń do usług takich
jak systat, finger, FTP, telnet, ssh, rlogin, rsh, exec, tftp, talk
oraz innych usług sieciowych.

%package lib
Summary:	libwrap replacement
Summary(pl.UTF-8):	Zamiennik libwrap
Group:		Libraries
Provides:	libwrap
Obsoletes:	libwrap

%description lib
Full tcp_wrappers libwrap replacement with IPv6 support and other
features.

%description lib -l pl.UTF-8
Pełny zamiennik biblioteki libwrap pochodzącej z pakietu tcp_wrappers.
Zamiennik oferuje ponadto wsparcie dla IPv6 i inne dodatki.

%package devel
Summary:	Headers files and development library for tcp-lib
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteki do programowania
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}
Provides:	libwrap-devel <= 7.6
Obsoletes:	libwrap-devel

%description devel
Headers files and development library for tcpd-lib.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteki do programowania z użyciem biblioteki
tcpd-lib.

%package static
Summary:	tcpd static library
Summary(pl.UTF-8):	Biblioteka statyczna tcpd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	libwrap-static <= 7.6

%description static
Static library tcpd-lib.

%description static -l pl.UTF-8
Biblioteka statyczna tcpd-lib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_sysconfdir}/hosts.access

%clean
rm -rf $RPM_BUILD_ROOT

%post 	lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/MEMO doc/hosts.access
%attr(755,root,root) %{_bindir}/*
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
