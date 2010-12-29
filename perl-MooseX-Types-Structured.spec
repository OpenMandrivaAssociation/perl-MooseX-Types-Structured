%define upstream_name    MooseX-Types-Structured
%define upstream_version 0.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Structured type constraints
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
A structured type constraint is a standard container the Moose manpage type
constraint, such as an ArrayRef or HashRef, which has been enhanced to
allow you to explicitly name all the allowed type constraints inside the
structure. The generalized form is:

    TypeConstraint[@TypeParameters or %TypeParameters]

Where 'TypeParameters' is an array or hash of the
Moose::Meta::TypeConstraint manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
