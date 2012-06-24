%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Dump
Summary:	Data::Dump perl module - pretty printing of data structures
Summary(pl):	Modu� perla Data::Dump - do �adnego wy�wietlania struktur danych
Name:		perl-Data-Dump
Version:	0.04
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Data::Dump module. It is a simplification of
Sarathy's Data::Dumper. This module provides a single function called
dump() that takes a list of values as argument and produce a string as
result. The string contains perl code that when evaled will produce a
deep copy of the original arguments. The string is formatted for easy
reading.

%description -l pl
Ten pakiet zawiera modu� Data::Dump. Jest on uproszczeniem modu�u
Data::Dumper Sarathy'ego. Ten modu� dostarcza pojedyncz� funkcj� o
nazwie dump(), kt�ra przyjmuje jako argument list� warto�ci i zwraca
w wyniku ci�g znak�w. Ci�g ten zawiera perlowy kod, kt�ry po wykonaniu
zwraca kopi� oryginalnych argument�w. Ci�g ten jest sformatowany tak,
by by� �atwo czytelny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Data/Dump.pm
%{_mandir}/man3/*
