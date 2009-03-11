%define module  MooseX-Types-Structured
%define version 0.09
%define release %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Structured type constraints
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{module}-%{version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Devel::PartialDump)
Provides: perl(MooseX::Meta::TypeCoercion::Structured)
Provides: perl(MooseX::Meta::TypeConstraint::Structured)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
A structured type constraint is a standard container the Moose manpage type
constraint, such as an ArrayRef or HashRef, which has been enhanced to
allow you to explicitly name all the allowed type constraints inside the
structure. The generalized form is:

    TypeConstraint[@TypeParameters or %TypeParameters]

Where 'TypeParameters' is an array or hash of the
Moose::Meta::TypeConstraint manpage.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/MooseX

