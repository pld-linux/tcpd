Summary:	Another security wrapper for tcp daemons
Summary(pl):	Inny wrapper bezpieczeñstwa dla demonów tcp
Name:		tcpd
Version:	980106
Release:	1
Copyright:	Distributable
Group:		Networking/Admin
Group(pl):	Sieciowe/Administacyjne
Vendor:		fujiwara@rcac.tdi.co.jp
Source:		http://www.rcac.tdi.co.jp/fujiwara/%{name}-v6-0.0-%{version}.tar.gz
Patch:		%{name}-linux.patch
URL:		http://www.rcac.tdi.co.jp/fujiwara/
Buildroot:	/tmp/%{name}-%{version}-root
Conflicts:	tcp_wrapper
Conflicts:	libwrap-static

%description
With this package you can monitor and filter incoming requests for the
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, and other
network services. It is replacement for tcp_wrappers. It support
both - IPv4 and IPv6.

%description -l pl
Z tym pakietem mo¿esz monitorowaæ i filtrowaæ nadchodz±ce pro¶by do
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, i innych
us³ug sieciowych. tcpd mo¿e zast±piæ tcp_wrappers. tcpd wspiera
zarówno IPv4 jak i IPv6.

%prep
%setup -q -n %{name}
%patch -p1

%build
OPT="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_sbindir}}

install libwrap.a		$RPM_BUILD_ROOT%{_libdir}
install -s tcpd tcpd_check	$RPM_BUILD_ROOT%{_sbindir}
install tcpd.h			$RPM_BUILD_ROOT%{_includedir}
install hosts.access		$RPM_BUILD_ROOT/etc


gzip -9nf MEMO README.txt hosts.access

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %config %verify(not md5 mtime size) /etc/hosts.*

%changelog
* Sat Jul 05 1999 PLD Team <pld-list@pld.org.pl>
- new commenting style:

$Log: tcpd.spec,v $
Revision 1.1  1999-07-13 12:19:59  misiek
new spec
