#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v20
# autospec commit: f35655a
#
Name     : perl-Minion
Version  : 10.31
Release  : 70
URL      : https://cpan.metacpan.org/authors/id/S/SR/SRI/Minion-10.31.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SRI/Minion-10.31.tar.gz
Summary  : 'Job queue'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Minion-license = %{version}-%{release}
Requires: perl-Minion-perl = %{version}-%{release}
Requires: perl(SQL::Abstract::Pg)
BuildRequires : buildreq-cpan
BuildRequires : perl(Digest::MD5)
BuildRequires : perl(Mojo::Base)
BuildRequires : perl(Mojolicious)
BuildRequires : perl(YAML::XS)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![Screenshot](https://raw.github.com/mojolicious/minion/main/examples/admin.png?raw=true)

%package dev
Summary: dev components for the perl-Minion package.
Group: Development
Provides: perl-Minion-devel = %{version}-%{release}
Requires: perl-Minion = %{version}-%{release}

%description dev
dev components for the perl-Minion package.


%package license
Summary: license components for the perl-Minion package.
Group: Default

%description license
license components for the perl-Minion package.


%package perl
Summary: perl components for the perl-Minion package.
Group: Default
Requires: perl-Minion = %{version}-%{release}

%description perl
perl components for the perl-Minion package.


%prep
%setup -q -n Minion-10.31
cd %{_builddir}/Minion-10.31
pushd ..
cp -a Minion-10.31 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Minion
cp %{_builddir}/Minion-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Minion/2f8018a02043ed1a43f032379e036bb6b88265f2 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Minion.3
/usr/share/man/man3/Minion::Backend.3
/usr/share/man/man3/Minion::Backend::Pg.3
/usr/share/man/man3/Minion::Command::minion.3
/usr/share/man/man3/Minion::Command::minion::job.3
/usr/share/man/man3/Minion::Command::minion::worker.3
/usr/share/man/man3/Minion::Guide.3
/usr/share/man/man3/Minion::Iterator.3
/usr/share/man/man3/Minion::Job.3
/usr/share/man/man3/Minion::Worker.3
/usr/share/man/man3/Mojolicious::Plugin::Minion.3
/usr/share/man/man3/Mojolicious::Plugin::Minion::Admin.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Minion/2f8018a02043ed1a43f032379e036bb6b88265f2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
