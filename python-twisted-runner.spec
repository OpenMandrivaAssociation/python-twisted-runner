%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

%define debug_package %{nil}

Summary:	Runner has process management, including an inetd replacement for Twisted

Name:		python-twisted-runner
Version:	13.2.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://twistedmatrix.com/trac/wiki/TwistedRunner
Source0:	http://twistedmatrix.com/Releases/Runner/13.2/TwistedRunner-%{version}.tar.bz2
Source100: %{name}.rpmlintrc
Patch0:		TwistedRunner-13.1.0-tirpc.patch
BuildRequires:	python-twisted-core
BuildRequires:	pkgconfig(python)
Requires:	python-twisted-core

%description
Runner has process management, including an inetd replacement for Twisted.

%prep
%setup -qn TwistedRunner-%{version}
%autopatch -p1

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%files
%defattr(0644,root,root,0755)
%doc LICENSE README
%dir %{py_platsitedir}/twisted/runner
%{py_platsitedir}/twisted/runner/*
%{py_platsitedir}/twisted/plugins/*
%{py_platsitedir}/*.egg-info


