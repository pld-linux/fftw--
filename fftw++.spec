Summary:	Fast Fourier Transform C++ Header Class for FFTW3 Library
Summary(pl):	Biblioteka klas C++ z funkcjami szybkiej transformaty Fouriera
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
BuildRequires:	libstdc++-devel
Requires:	fftw3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FFTW++ is a C++ header class for version 3 of the highly optimized
FFTW Fourier Transform library. 

%description -l pl
FFTW++ jest bibliotek± klas napisan± w C++ dla wersji 3 biblioteki
szybkiej transformaty Fouriera FFTW.

%package devel
Summary:	Development files for fftw++
Summary(pl):	Pliki programistyczne do fftw++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the files you need to develop programs using the
FFTW++ (fast fourier transform library).

%description devel -l pl
Ten pakiet zawiera pliki potrzebne do tworzenia programów u¿ywaj±cych
biblioteki FFTW++ (wykonuj±cej szybk± transformatê Fouriera).

%package examples
Summary:	Example files for fftw++
Summary(pl):	Przyk³±dy programistyczne do fftw++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
Examples how to use fftw++.

%description examples -l pl
Przyk³ady do fftw++.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install	-d $RPM_BUILD_ROOT{%{_includedir}/fftw++,%{_examplesdir}/%{name}-%{version}}

install fftw++.*   $RPM_BUILD_ROOT%{_includedir}/fftw++
install %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/fftw++
install  example*.*   $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE

%files devel
%defattr(644,root,root,755)
%{_includedir}/fftw++

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
