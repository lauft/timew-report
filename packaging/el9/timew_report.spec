# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global srcname timew_report

Name:           python-%{srcname}
Version:        VER_GOES_HERE
Release:        1%{?dist}
Summary:        An interface for Timewarrior report data

License:        CC-BY-SA-3.0
URL:            https://github.com/lauft/timew-report
Source0:        %{url}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(tomli)
BuildRequires: python%{python3_pkgversion}dist(wheel)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
BuildRequires: python%{python3_pkgversion}dist(setuptools-scm[toml])
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-deprecated

%description
A Timewarrior extension interface for custom report output.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname}
A Timewarrior extension interface for custom report output.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# using pyproject macros
%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install

# Use -l to assert a %%license file is found (PEP 639).
# this is looking for the actual module directory name
%pyproject_save_files -l timewreport

%check
%pyproject_check_import
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-timew_report -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Mon Jul 07 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.4.1
- Initial package
