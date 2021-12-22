#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : QtPy
Version  : 2.0.0
Release  : 41
URL      : https://files.pythonhosted.org/packages/88/f8/5f987cfd847a38204b4e9135f4ee39614bd1437dc078377a00136d9444db/QtPy-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/f8/5f987cfd847a38204b4e9135f4ee39614bd1437dc078377a00136d9444db/QtPy-2.0.0.tar.gz
Summary  : Provides an abstraction layer on top of the various Qt bindings (PyQt5/6 and PySide2/6).
Group    : Development/Tools
License  : MIT
Requires: QtPy-python = %{version}-%{release}
Requires: QtPy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(packaging)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
# QtPy: Abstraction layer for PyQt5/PyQt6/PySide2/PySide6
[![license](https://img.shields.io/pypi/l/qtpy.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/qtpy.svg)](https://pypi.org/project/QtPy/)
[![conda version](https://img.shields.io/conda/vn/conda-forge/qtpy.svg)](https://www.anaconda.com/download/)
[![download count](https://img.shields.io/conda/dn/conda-forge/qtpy.svg)](https://www.anaconda.com/download/)
[![OpenCollective Backers](https://opencollective.com/spyder/backers/badge.svg?color=blue)](#backers)
[![Join the chat at https://gitter.im/spyder-ide/public](https://badges.gitter.im/spyder-ide/spyder.svg)](https://gitter.im/spyder-ide/public)<br>
[![PyPI status](https://img.shields.io/pypi/status/qtpy.svg)](https://github.com/spyder-ide/qtpy)
[![Github build status](https://github.com/spyder-ide/qtpy/workflows/Tests/badge.svg)](https://github.com/spyder-ide/qtpy/actions)
[![Coverage Status](https://coveralls.io/repos/github/spyder-ide/qtpy/badge.svg?branch=master)](https://coveralls.io/github/spyder-ide/qtpy?branch=master)

%package python
Summary: python components for the QtPy package.
Group: Default
Requires: QtPy-python3 = %{version}-%{release}
Provides: qtpy-python

%description python
python components for the QtPy package.


%package python3
Summary: python3 components for the QtPy package.
Group: Default
Requires: python3-core
Provides: pypi(qtpy)
Requires: pypi(packaging)

%description python3
python3 components for the QtPy package.


%prep
%setup -q -n QtPy-2.0.0
cd %{_builddir}/QtPy-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640215845
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
