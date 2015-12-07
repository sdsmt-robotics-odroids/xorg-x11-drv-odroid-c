%global commit fa6394b7f2206c79140ca1b0e050351b55ba646b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           xorg-x11-drv-odroid-c
Version:        2015.01.13
Release:        2%{?dist}
Summary:        X.org Mali video driver for ODROID-C

Group:          User Interface/X Hardware Support
License:        MIT
URL:            https://github.com/mdrjr/c1_mali_ddx
Source0:        https://github.com/mdrjr/c1_mali_ddx/archive/%{commit}/c1_mali_ddx-%{commit}.tar.gz
Patch0:         %{name}-2015.01.13-xorg-conf.patch
Patch1:         %{name}-2015.01.13-message-cleanups.patch

BuildRequires:  autoconf
BuildRequires:  odroid-c-mali-ump-devel
BuildRequires:  odroid-c-mali-x11
BuildRequires:  xorg-x11-server-devel

%description
X.org Mali video driver for ODROID-C based on r5p0-01rel0

%prep
%setup -qn c1_mali_ddx-%{commit}
%patch0 -p1
%patch1 -p1

%build
autoreconf --install
CFLAGS="${CFLAGS:-%optflags} -L%{_libdir}/odroid-c-mali-x11" \
%configure
make %{?_smp_mflags}

%install
install -p -m0755 -D src/.libs/mali_drv.so %{buildroot}%{_libdir}/xorg/modules/drivers/mali_drv.so
install -p -m0644 -D src/xorg.conf %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/99-odroid-c-mali.conf

%files
%doc README.txt
%{_libdir}/xorg/modules/drivers/mali_drv.so
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/99-odroid-c-mali.conf

%changelog
* Sun Dec 06 2015 Scott K Logan <logans@cottsay.net> - 2015.01.13-2
- More message cleanups

* Wed Dec 02 2015 Scott K Logan <logans@cottsay.net> - 2015.01.13-1
- Initial package
