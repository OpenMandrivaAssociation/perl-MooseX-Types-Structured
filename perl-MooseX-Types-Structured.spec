%define upstream_name    MooseX-Types-Structured
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Structured type constraints
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/MooseX-Types-Structured-%{upstream_version}.tar.gz

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

%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.270.0-1mdv2011.0
+ Revision: 662128
- update to new version 0.27

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.260.0-3
+ Revision: 653469
- add more provides

* Mon Mar 07 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.260.0-2
+ Revision: 642422
- rebuild

* Tue Jan 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.0-1mdv2011.0
+ Revision: 628582
- update to new version 0.26

* Wed Dec 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1mdv2011.0
+ Revision: 625968
- update to new version 0.25

* Wed Nov 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 598317
- update to new version 0.24

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 552722
- update to 0.23

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-2mdv2010.1
+ Revision: 528112
- rebuild
- update to 0.21

* Fri Feb 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.1
+ Revision: 501147
- update to 0.20

* Sun Nov 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.1
+ Revision: 463041
- update to 0.19

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 418402
- update to 0.18

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 416977
- update to 0.17

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 405948
- rebuild using %%perl_convert_version

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2010.0
+ Revision: 384028
- update to new version 0.16

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.14-1mdv2010.0
+ Revision: 374544
- update to new version 0.14

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.1
+ Revision: 353675
- update to new version 0.09

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-3mdv2009.1
+ Revision: 343945
- fix dependencies again

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-2mdv2009.1
+ Revision: 343939
- fix dependencies

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.1
+ Revision: 343851
- import perl-MooseX-Types-Structured


* Sun Feb 22 2009 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist


