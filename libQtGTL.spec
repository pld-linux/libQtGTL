Summary:	Qt Wrappers for Graphics Transformation Language
Summary(pl.UTF-8):	Interfejsy Qt do języka przekształceń graficznych GTL
Name:		libQtGTL
Version:	0.9.3
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://download.opengtl.org/%{name}-%{version}.tar.bz2
# Source0-md5:	1e9fd96332db22da01ab6d83568e396e
URL:		http://opengtl.org/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	OpenGTL-devel >= 0.9.16
BuildRequires:	cmake >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Wrappers for Graphics Transformation Language.

%description -l pl.UTF-8
Interfejsy Qt do języka przekształceń graficznych GTL.

%package devel
Summary:	Header files for QtGTL libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek QtGTL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGTL-devel >= 0.9.16
Requires:	QtCore-devel >= 4
Requires:	QtGui-devel >= 4

%description devel
Header files for QtGTL libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek QtGTL.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtGTL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGTL.so.0.2
%attr(755,root,root) %{_libdir}/libQtShiva.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtShiva.so.0.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtGTL.so
%attr(755,root,root) %{_libdir}/libQtShiva.so
%{_includedir}/QtGTL
%{_includedir}/QtShiva
%{_pkgconfigdir}/QtGTL.pc
%{_pkgconfigdir}/QtShiva.pc
