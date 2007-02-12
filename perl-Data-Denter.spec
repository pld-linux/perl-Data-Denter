#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Denter
Summary:	Data::Denter - an (deprecated) alternative to Data::Dumper and Storable
Summary(pl.UTF-8):   Data::Denter - (porzucona) alternatywa dla Data::Dumper i Storable
Name:		perl-Data-Denter
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	819e5c05fb61e90f4c1311286b080405
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# for perldiag.pod; should it be moved to perl-base?
BuildRequires:	perl-perldoc
BuildRequires:	perl-YAML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main problem with Data::Dumper (one of my all-time favorite
modules) is that you have to use eval() to deserialize the data you've
dumped. This is great if you can trust the data you're evaling, but
horrible if you can't. A good alternative is Storable.pm. It can
safely thaw your frozen data. But if you want to read/edit the frozen
data, you're out of luck, because Storable uses a binary format. Even
Data::Dumper's output can be a little cumbersome for larger data
objects.

%description -l pl.UTF-8
Głównym problemem klasy Data::Dumper (jednego z ulubionych modułów
autora) jest to, że trzeba używać eval() aby dokonać deserializacji
zrzuconych danych. Jest to wspaniałe, jeśli można zaufać danym, ale
przerażające, jeśli nie możemy. Dobrą alternatywą jest moduł
Storable.pm. Może on bezpiecznie roztopić zamrożone dane. Ale kiedy
chcemy odczytać/zmodyfikować zamrożone dane, nie mamy szczęścia,
ponieważ Storable używa binarnego formatu. Nawet format wyjścia modułu
Data::Dumper może by nieco niewygodny dla większych obiektów danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/*.pm
%{_mandir}/man3/*
