%include	/usr/lib/rpm/macros.python
%define		module	anygui
Summary:	Generic GUI Package for Python
Summary(pl):	Pakiet GUI dla Pythona
Name:		python-%{module}
Version:	0.1.1
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/anygui/%{module}-%{version}.tar.gz
# Source0-md5:	fd628ef008ef3139aae85a3d954e4653
URL:		http://www.anygui.org/
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov >= 4.0.2-50
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

%description
The purpose of the Anygui project is to create an easy-to-use, simple,
and generic module for making graphical user interfaces in Python. Its
main feature is that it works transparently with many different GUI
packages on most platforms.

%description -l pl
Celem Anygui jest stworzenie prostego w u¿yciu, standardowego modu³u
do tworzenia interfejsu u¿ytkownika w Pythonie. G³ówn± zalet± Anygui
jest to, ¿e dzia³a on prze¼roczy¶cie z wieloma innymi GUI na ró¿nych
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE* KNOWN* MAINT* TODO* doc/*.txt
%{_examplesdir}/%{name}-%{version}
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/backends
%{py_sitedir}/%{module}/backends/*.py[co]
%dir %{py_sitedir}/%{module}/backends/txtutils
%{py_sitedir}/%{module}/backends/txtutils/*.py[co]
