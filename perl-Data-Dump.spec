%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Dump
Summary:	Data::Dump - pretty printing of data structures
Summary(pl):	Data::Dump - ³adne wy¶wietlanie struktur danych
Name:		perl-Data-Dump
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d94b8a515affb051ff7952e578e9f3a5
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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
Ten pakiet zawiera modu³ Data::Dump. Jest on uproszczeniem modu³u
Data::Dumper Sarathy'ego. Ten modu³ dostarcza pojedyncz± funkcjê o
nazwie dump(), która przyjmuje jako argument listê warto¶ci i zwraca
w wyniku ci±g znaków. Ci±g ten zawiera perlowy kod, który po wykonaniu
zwraca kopiê oryginalnych argumentów. Ci±g ten jest sformatowany tak,
by by³ ³atwo czytelny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/Dump.pm
%{_mandir}/man3/*
