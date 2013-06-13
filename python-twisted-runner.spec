%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

%define debug_package %{nil}

Summary:        Runner has process management, including an inetd replacement for Twisted
Name:           python-twisted-runner
Version:        13.0.0
Release:	1
Source0:        http://twistedmatrix.com/Releases/Runner/13.0/TwistedRunner-13.0.0.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedRunner
BuildRequires:  python-devel python-twisted-core
Requires:       python-twisted-core

%description
Runner has process management, including an inetd replacement for Twisted.

%prep
%setup -q -n TwistedRunner-%version

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%files
%defattr(0644,root,root,0755)
%doc LICENSE README
%dir %py_platsitedir/twisted/runner
%py_platsitedir/twisted/runner/*
%py_platsitedir/twisted/plugins/*
%py_platsitedir/*.egg-info
