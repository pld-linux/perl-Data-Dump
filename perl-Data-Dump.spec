%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Dump
Summary:	Data::Dump - pretty printing of data structures
Summary(pl.UTF-8):	Data::Dump - ładne wyświetlanie struktur danych
Name:		perl-Data-Dump
Version:	1.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab41f4135e5460da837a7176ae4b3e39
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Data::Dump module. It is a simplification of
Sarathy's Data::Dumper. This module provides a single function called
dump() that takes a list of values as argument and produce a string as
result. The string contains Perl code that when evaled will produce a
deep copy of the original arguments. The string is formatted for easy
reading.

%description -l pl.UTF-8
Ten pakiet zawiera moduł Data::Dump. Jest on uproszczeniem modułu
Data::Dumper Sarathy'ego. Ten moduł dostarcza pojedynczą funkcję o
nazwie dump(), która przyjmuje jako argument listę wartości i zwraca
w wyniku ciąg znaków. Ciąg ten zawiera kod perlowy, który po wykonaniu
zwraca kopię oryginalnych argumentów. Ciąg ten jest sformatowany tak,
by był łatwo czytelny.

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
