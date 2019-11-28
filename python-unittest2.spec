Name:           python-unittest2
Version:        1.1.0
Release:        16
Summary:        New features added to the unittest testing framework in Python 2.7 and onwards
License:        BSD
URL:            http://pypi.python.org/pypi/unittest2
Source0:        https://pypi.python.org/packages/source/u/unittest2/unittest2-%{version}.tar.gz

Patch0000:      unittest2-1.1.0-remove-argparse-from-requires.patch
Patch0001:      unittest2-1.1.0-backport-tests-from-py3.5.patch
BuildArch:      noarch

%description
unittest2 is a backport of the new features added to
the unittest testing framework in Python 2.7 and onwards.
It is tested to run on Python 2.6, 2.7, 3.2, 3.3, 3.4 and pypy.

%package -n python2-unittest2
Summary:        New features added to the unittest testing framework in Python 2.7 and onwards
%{?python_provide:%python_provide python2-unittest2}
BuildRequires:  python2-devel python2-setuptools python2-six python2-traceback2
Requires:       python2-traceback2 python2-setuptools python2-six

%description -n python2-unittest2
unittest2 is a backport of the new features added to
the unittest testing framework in Python 2.7 and onwards.
It is tested to run on Python 2.6, 2.7, 3.2, 3.3, 3.4 and pypy.

%package -n python3-unittest2
Summary:        New features added to the unittest testing framework in Python 2.7 and onwards
%{?python_provide:%python_provide python3-unittest2}
BuildRequires:  python3-devel python3-setuptools python3-six python3-traceback2
Requires:       python3-setuptools python3-six python3-traceback2

%description -n python3-unittest2
unittest2 is a backport of the new features added to
the unittest testing framework in Python 2.7 and onwards.
It is tested to run on Python 2.6, 2.7, 3.2, 3.3, 3.4 and pypy.

%prep
%autosetup -n unittest2-%{version} -p1
rm -rf unittest2.egg-info

%build
%py2_build
%py3_build

%install
%py3_install
cd %{buildroot}%{_bindir}
mv unit2 unit2-%{python3_version}
ln -s unit2-%{python3_version} unit2-3
ln -s unit2-%{python3_version} python3-unit2
cd -

%py2_install
cd %{buildroot}%{_bindir}
mv unit2 unit2-%{python2_version}
ln -s unit2-%{python2_version} unit2-2
ln -s unit2-2 unit2
cd -

%check
%{__python2} -m unittest2
%{__python3} -m unittest2

%files -n python2-unittest2
%doc README.txt
%{_bindir}/unit2*
%{python2_sitelib}/unittest2*

%files -n python3-unittest2
%doc README.txt
%{_bindir}/unit2-*
%{_bindir}/python3-unit2
%{python3_sitelib}/unittest2*

%changelog
* Wed Nov 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.0-16
- Package init