# TODO:
# - subpackages (?)
# - config for rc-inetd
Summary:	File Service Protocol programs
Summary(pl):	Programy do obs³ugi protoko³u FSP
Name:		fsp
Version:	2.8.1b24
Release:	0.1
License:	BSD
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/fsp/%{name}-%{version}.tar.bz2
# Source0-md5:	19a80b22e43717175facfc26e25d902b
URL:		http://fsp.sourceforge.net/
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FSP is a set of programs that implements a public-access archive
similar to an anonymous-FTP archive. It is not meant to be a
replacement for FTP; it is only meant to do what anonymous-FTP does,
but in a manner more acceptable to the provider of the service and
more friendly to the clients.

%description -l pl
FSP jest zestawem programów, który implementuje protokó³ dostêpu do
publicznych archiwów podobny do anonimowego FTP, ale z u¿yciem
protoko³u UDP. Jego zamierzeniem nie jest zastêpowanie FTP, ale
robienie tego samego co anonimowe FTP w sposób bardziej przyjazny dla
klientów i bardziej akceptowalny dla providerów.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install fspd.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BETA.README ChangeLog INFO INSTALL TODO doc/{faq.html,PROTOCOL}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
