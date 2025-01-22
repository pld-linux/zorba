Summary:	General purpose XQuery processor
Summary(pl.UTF-8):	Procesor XQuery ogólnego przeznaczenia
Name:		zorba
Version:	3.1
Release:	1
License:	Apache v2.0
Group:		Applications/Text
# up to 2.9.1
# Source0:	https://downloads.sourceforge.net/zorba/%{name}-%{version}.tar.gz
# 3+
#Source0Download: https://github.com/28msec/zorba/tags
Source0:	https://github.com/28msec/zorba/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8b6c5203d91fcc54cc7d08efa47b4bdd
Patch0:		%{name}-tr1.patch
Patch1:		%{name}-icu.patch
Patch2:		%{name}-glibc.patch
Patch3:		%{name}-includes.patch
Patch4:		libxml2.12.patch
Patch5:		boost1.85.patch
URL:		https://github.com/28msec/zorba
BuildRequires:	bison >= 2.4
BuildRequires:	boost-devel >= 1.33
BuildRequires:	cmake >= 2.6
BuildRequires:	curl-devel >= 7.12
BuildRequires:	doxygen
BuildRequires:	flex >= 2.5.35
BuildRequires:	graphviz
BuildRequires:	libicu-devel >= 2.6
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.7.0
BuildRequires:	libxslt-devel
BuildRequires:	rpmbuild(macros) >= 2.028
BuildRequires:	xerces-c-devel >= 2.8.0
Requires:	libxml2 >= 1:2.7.0
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
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
install -d build
cd build
%cmake .. \
	-DZORBA_LIB_DIRNAME=%{_lib} \
	-DZORBA_XQUERYX=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_bindir}/testdriver

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name}-3.1.0/c/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/c
%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name}-3.1.0/cxx/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/cxx

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/zorba
%attr(755,root,root) %{_libdir}/libutil-curl.so
%attr(755,root,root) %{_libdir}/libzorba_simplestore.so.3.1.0
%dir %{_libdir}/zorba
%dir %{_libdir}/zorba/core
%dir %{_libdir}/zorba/core/3.1.0
%dir %{_libdir}/zorba/core/3.1.0/edu
%dir %{_libdir}/zorba/core/3.1.0/edu/princeton
%dir %{_libdir}/zorba/core/3.1.0/edu/princeton/wordnet
%{_libdir}/zorba/core/3.1.0/edu/princeton/wordnet/wordnet-en.zth
%dir %{_libdir}/zorba/core/3.1.0/io
%dir %{_libdir}/zorba/core/3.1.0/io/zorba
%dir %{_libdir}/zorba/core/3.1.0/io/zorba/modules
%attr(755,root,root) %{_libdir}/zorba/core/3.1.0/io/zorba/modules/libftp-client_1.0.so
%attr(755,root,root) %{_libdir}/zorba/core/3.1.0/io/zorba/modules/libhttp-client_1.0.so
%attr(755,root,root) %{_libdir}/zorba/core/3.1.0/io/zorba/modules/libsleep_1.0.so
%attr(755,root,root) %{_libdir}/zorba/core/3.1.0/io/zorba/modules/libzorba-query_1.0.so
%dir %{_libdir}/zorba/core/3.1.0/org
%dir %{_libdir}/zorba/core/3.1.0/org/expath
%dir %{_libdir}/zorba/core/3.1.0/org/expath/ns
%attr(755,root,root) %{_libdir}/zorba/core/3.1.0/org/expath/ns/libfile_2.0.so
%dir %{_libdir}/zorba/io
%dir %{_libdir}/zorba/io/zorba
%dir %{_libdir}/zorba/io/zorba/modules
%attr(755,root,root) %{_libdir}/zorba/io/zorba/modules/libutil-tests_1.0.so
%dir %{_datadir}/zorba
%{_datadir}/zorba/uris
%dir %{_datadir}/zorba-3.1.0
%{_datadir}/zorba-3.1.0/fots_driver

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzorba_simplestore.so
%{_includedir}/xqc.h
%dir %{_includedir}/util
%{_includedir}/util/curl_streambuf.h
%{_includedir}/zorba
%{_datadir}/cmake/zorba-3.1.0
%{_examplesdir}/%{name}-%{version}
