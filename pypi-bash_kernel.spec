#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-bash_kernel
Version  : 0.9.1
Release  : 20
URL      : https://files.pythonhosted.org/packages/31/7c/9c7ef07b09188601bb767beda5482e58ce06ae5ae75af0ab8b294ff58ce7/bash_kernel-0.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/7c/9c7ef07b09188601bb767beda5482e58ce06ae5ae75af0ab8b294ff58ce7/bash_kernel-0.9.1.tar.gz
Summary  : A bash kernel for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-bash_kernel-license = %{version}-%{release}
Requires: pypi-bash_kernel-python = %{version}-%{release}
Requires: pypi-bash_kernel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(bash_kernel)
BuildRequires : pypi(flit_core)
BuildRequires : pypi(ipykernel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://mybinder.org/badge_logo.svg
:target: https://mybinder.org/v2/gh/takluyver/bash_kernel/master

%package license
Summary: license components for the pypi-bash_kernel package.
Group: Default

%description license
license components for the pypi-bash_kernel package.


%package python
Summary: python components for the pypi-bash_kernel package.
Group: Default
Requires: pypi-bash_kernel-python3 = %{version}-%{release}

%description python
python components for the pypi-bash_kernel package.


%package python3
Summary: python3 components for the pypi-bash_kernel package.
Group: Default
Requires: python3-core
Provides: pypi(bash_kernel)
Requires: pypi(bash_kernel)
Requires: pypi(ipykernel)
Requires: pypi(pexpect)

%description python3
python3 components for the pypi-bash_kernel package.


%prep
%setup -q -n bash_kernel-0.9.1
cd %{_builddir}/bash_kernel-0.9.1
pushd ..
cp -a bash_kernel-0.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688054721
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bash_kernel
cp %{_builddir}/bash_kernel-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bash_kernel/76c7e710d472be20ce886472767e77a7d52692b8 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bash_kernel/76c7e710d472be20ce886472767e77a7d52692b8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
