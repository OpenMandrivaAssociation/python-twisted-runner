%define version 8.0.0
%define rel 1

Summary:        Runner has process management, including an inetd replacement for Twisted
Name:           python-twisted-runner
Version:        %version
Release: %mkrel %rel
Source0:        http://tmrc.mit.edu/mirror/twisted/Runner/8.0/TwistedRunner-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedRunner
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:  python-devel python-twisted-core
Requires:       python-twisted-core

%description
Runner has process management, including an inetd replacement for Twisted.

%prep
%setup -q -n TwistedRunner-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot

%clean
%__rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc LICENSE README 
%dir %py_platsitedir/twisted/runner
%py_platsitedir/twisted/runner/*
%py_platsitedir/*.egg-info



