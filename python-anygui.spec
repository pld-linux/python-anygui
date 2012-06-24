%include	/usr/lib/rpm/macros.python
%define		module	anygui
Summary:	Generic GUI Package for Python
Summary(pl):	Pakiet GUI dla Pythona
Name:		python-%{module}
Version:	0.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Python
Group(da):	Udvikling/Sprog/Python
Group(de):	Entwicklung/Sprachen/Python
Group(es):	Desarrollo/Lenguajes/Python
Group(fr):	Development/Langues/Python
Group(it):	Sviluppo/Linguaggi/Python
Group(ja):	��ȯ/����/Python
Group(no):	Utvikling/Programmeringsspr�k/Python
Group(pl):	Programowanie/J�zyki/Python
Group(pt):	Desenvolvimento/Linguagens/Python
Group(ru):	����������/�����/Python
Group(sv):	Utveckling/Spr�k/Python
Source0:	http://prdownloads.sourceforge.net/anygui/%{module}-%{version}.tar.gz
URL:		http://www.anygui.org/
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov >= 4.0.2-50
%requires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

%description
The purpose of the Anygui project is to create an easy-to-use, simple,
and generic module for making graphical user interfaces in Python. Its
main feature is that it works transparently with many different GUI
packages on most platforms.

%description -l pl
Celem Anygui jest stworzenie prostego w u�yciu, standardowego modu�u
do tworzenia interfejsu u�ytkownika w Pythonie. G��wn� zalet� Anygui
jest to, �e dzia�a on prze�roczy�cie z wieloma innymi GUI na r�nych
platformach.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
        --root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

mv demo/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf CHANGE* KNOWN* MAINT* TODO* doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%{_examplesdir}/%{name}-%{version}
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/backends
%{py_sitedir}/%{module}/backends/*.py[co]
%dir %{py_sitedir}/%{module}/backends/txtutils
%{py_sitedir}/%{module}/backends/txtutils/*.py[co]
