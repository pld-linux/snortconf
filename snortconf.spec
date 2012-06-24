Summary:	A tool to ease configuring the OpenSource IDS tool Snort
Summary(pl):	Narz�dzie do �atwego konfigurowania Snorta
Name:		snortconf
Version:	0.4.2
Release:	0.1
License:	GPL v2
Group:		Development
Source0:	http://xjack.org/snortconf/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	9a25b762023f5630f3973858206acb84
Patch0:		%{name}-include.patch
URL:		http://xjack.org/snortconf/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SnortConf is a simple, intuitive menu based tool that provides a more
user friendly interface to creating a snort.conf file. It is still in
it's early days of development, but it is already fully functional in
most respects.

%description -l pl
SnortConf jest prostym i intuicyjnym narz�dziem s�u��cym do bardziej
przyjaznego tworzenia pliku snort.conf.

%prep
%setup -q
%patch0 -p0

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README README.BETA TODO USAGE
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snortconf/sc.conf
