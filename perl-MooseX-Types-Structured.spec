%define upstream_name    MooseX-Types-Structured%define upstream_version 0.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Structured type constraints
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Devel::PartialDump)
BuildRequires:	perl(namespace::autoclean)
Provides:	perl(MooseX::Meta::TypeCoercion::Structured) = %{version}
Provides:	perl(MooseX::Meta::TypeCoercion::Structured::Optional) = %{version}
Provides:	perl(MooseX::Meta::TypeConstraint::Structured) = %{version}
Provides:	perl(MooseX::Meta::TypeConstraint::Structured::Optional) = %{version}
Provides:	perl(MooseX::Types::Structured::MessageStack) = %{version}
Provides:	perl(MooseX::Types::Structured::OverflowHandler) = %{version}
BuildArch:	noarch

%description
A structured type constraint is a standard container the Moose manpage type
constraint, such as an ArrayRef or HashRef, which has been enhanced to
allow you to explicitly name all the allowed type constraints inside the
structure. The generalized form is:

    TypeConstraint[@TypeParameters]

Where 'TypeParameters' is an array or hash of the
Moose::Meta::TypeConstraint manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/MooseX

