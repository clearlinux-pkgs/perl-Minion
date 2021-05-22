#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Minion
Version  : 10.21
Release  : 50
URL      : https://cpan.metacpan.org/authors/id/S/SR/SRI/Minion-10.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SRI/Minion-10.21.tar.gz
Summary  : 'Job queue'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Minion-license = %{version}-%{release}
Requires: perl-Minion-perl = %{version}-%{release}
Requires: perl(SQL::Abstract::Pg)
BuildRequires : buildreq-cpan
BuildRequires : perl(Mojo::Base)
BuildRequires : perl(Mojolicious)
BuildRequires : perl(YAML::XS)

%description
# Minion [![](https://github.com/mojolicious/minion/workflows/linux/badge.svg)](https://github.com/mojolicious/minion/actions)

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
%setup -q -n Minion-10.21
cd %{_builddir}/Minion-10.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
cp %{_builddir}/Minion-10.21/LICENSE %{buildroot}/usr/share/package-licenses/perl-Minion/2f8018a02043ed1a43f032379e036bb6b88265f2
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

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
/usr/lib/perl5/vendor_perl/5.34.0/Minion.pm
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Backend.pm
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Backend/Pg.pm
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Backend/resources/migrations/pg.sql
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Command/minion.pm
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Command/minion/job.pm
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Command/minion/worker.pm
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Guide.pod
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Iterator.pm
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Job.pm
/usr/lib/perl5/vendor_perl/5.34.0/Minion/Worker.pm
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion.pm
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/Admin.pm
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/app.css
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/app.js
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/bootstrap/bootstrap.css
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/bootstrap/bootstrap.js
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/d3/d3.js
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/epoch/epoch.css
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/epoch/epoch.js
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/fontawesome/fontawesome.css
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/logo-black-2x.png
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/logo-black.png
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/moment/moment.js
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/pinstripe-light.png
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-brands-400.eot
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-brands-400.svg
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-brands-400.ttf
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-brands-400.woff
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-brands-400.woff2
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-regular-400.eot
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-regular-400.svg
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-regular-400.ttf
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-regular-400.woff
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-regular-400.woff2
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-solid-900.eot
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-solid-900.svg
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-solid-900.ttf
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-solid-900.woff
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/public/minion/webfonts/fa-solid-900.woff2
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/templates/layouts/minion.html.ep
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/templates/minion/_limit.html.ep
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/templates/minion/_notifications.html.ep
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/templates/minion/_pagination.html.ep
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/templates/minion/dashboard.html.ep
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/templates/minion/jobs.html.ep
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/templates/minion/locks.html.ep
/usr/lib/perl5/vendor_perl/5.34.0/Mojolicious/Plugin/Minion/resources/templates/minion/workers.html.ep
