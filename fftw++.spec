Summary:	Fast Fourier Transform C++ Header Class for FFTW3 Library
Summary(pl.UTF-8):	Biblioteka klas C++ z funkcjami szybkiej transformaty Fouriera
Name:		fftw++
Version:	1.01
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://www.math.ualberta.ca/imaging/fftw++/%{name}-%{version}.tar.gz
# Source0-md5:	42ac1ed342ade0d6242f0ee776433ad6
Source1:	http://www.math.ualberta.ca/~bowman/Array.h
URL:		http://www.math.ualberta.ca/imaging/fftw++/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FFTW++ is a C++ header class for version 3 of the highly optimized
FFTW Fast Fourier Transform library. 

%description -l pl.UTF-8
FFTW++ jest biblioteką klas napisaną w C++ dla wersji 3 biblioteki
szybkiej transformaty Fouriera FFTW.

%package devel
Summary:	Development files for fftw++
Summary(pl.UTF-8):	Pliki programistyczne do fftw++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fftw3-devel
Requires:	libstdc++-devel

%description devel
This package contains the files you need to develop programs using the
FFTW++ (Fast Fourier Transform library).

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do tworzenia programów używających
biblioteki FFTW++ (wykonującej szybką transformatę Fouriera).

%package static
Summary:	Static fftw++ library
Summary(pl.UTF-8):	Statyczna biblioteka fftw++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static fftw++ library.

%description static -l pl.UTF-8
Statyczna biblioteka fftw++.

%package examples
Summary:	Example files for fftw++
Summary(pl.UTF-8):	Przykłady programistyczne do fftw++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
Examples how to use fftw++.

%description examples -l pl.UTF-8
Przykłady do fftw++.

%prep
%setup -q

%build
libtool --mode=compile --tag CXX %{__cxx} %{rpmcxxflags} -fPIC -o fftw++.lo -c fftw++.cc
libtool --mode=link --tag CXX %{__cxx} -o libfftw++.la -rpath %{_libdir} fftw++.lo -lfftw3

%install
rm -rf $RPM_BUILD_ROOT
install	-d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/fftw++,%{_examplesdir}/%{name}-%{version}}

libtool --mode=install install libfftw++.la $RPM_BUILD_ROOT%{_libdir}

install fftw++.h $RPM_BUILD_ROOT%{_includedir}/fftw++
install %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/fftw++
install example*.* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libfftw++.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw++.so
%{_libdir}/libfftw++.la
%{_includedir}/fftw++

%files static
%defattr(644,root,root,755)
%{_libdir}/libfftw++.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
