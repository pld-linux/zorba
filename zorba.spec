Summary:	General purpose XQuery processor
Summary(pl.UTF-8):	Procesor XQuery ogólnego przeznaczenia
Name:		zorba
Version:	0.9.21
Release:	0.1
License:	Apache v2.0
Group:		Applications/Text
Source0:	https://downloads.sourceforge.net/zorba/%{name}-%{version}.tar.gz
# Source0-md5:	dc4ffe43b191700b93c4802b8baeec38
URL:		https://github.com/28msec/zorba
BuildRequires:	bison >= 2.3
BuildRequires:	boost-devel >= 1.32
BuildRequires:	cmake >= 2.4
BuildRequires:	curl-devel >= 7.12
BuildRequires:	doxygen
BuildRequires:	flex >= 2.5.33
BuildRequires:	graphviz
BuildRequires:	libicu-devel >= 2.6
BuildRequires:	libxml2-devel >= 2.2.16
BuildRequires:	xerces-c-devel >= 2.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zorba is a general purpose XQuery processor implementing in C++ the
W3C family of specifications. It is not an XML database. The query
processor has been designed to be embeddable in a variety of
environments such as other programming languages extended with XML
processing capabilities, browsers, database servers, XML message
dispatchers, or smartphones. Its architecture employes a modular
design, which allows customizing the Zorba query processor to the
environment's needs. In particular the architecture of the query
processor allows a pluggable XML store (e.g. main memory, DOM stores,
persistent disk-based large stores, S3 stores). Zorba runs on most
platforms and is available under the Apache license v2.

%description -l pl.UTF-8
Zorba to procesor XQuery ogólnego przeznaczenia, będący implementacją
w C++ rodziny specyfikacji W3C. Nie jest to baza danych XML. Procesor
zapytań został zaprojektowany jako osadzalny w wielu różnych
środowiskach, takich jak inne języki programowania z możliwością
przetwarzania XML, przeglądarki, serwery baz danych, obsługa
komunikatów XML czy smartfony. Architektura jest oparta o modularny
projekt, pozwalający na dostosowanie procesora zapytań Zorba do
potrzeb środowiska. W szczególności architektura procesora zapytań
pozwala na wtyczki dla mechanizmów przechowywania XML (np. pamięć
główna, przestrzeń DOM, pamięć trwała na dysku, przestrzeń S3). Zorba
działa na większości platform i jest dostępna na licencji Apache w
wersji 2.

%package devel
Summary:	Header files for zorba library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki zorba
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for zorba library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki zorba.

%prep
%setup -q

%build
mkdir build
cd build
#	-DCMAKE_C_COMPILER="%{__cc}" \
#	-DCMAKE_CXX_COMPILER="%{__cxx}" \
cmake .. \
	-DCMAKE_C_FLAGS="%{rpmcflags}" \
	-DCMAKE_CXX_FLAGS="%{rpmcxxflags}" \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_BINARY_DIR=build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/zorba

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/zorba
