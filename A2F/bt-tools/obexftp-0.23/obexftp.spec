#
# spec file for package ObexFTP (Version 0.15)
# 
# Author: Christian W. Zuckschwerdt <zany@triq.net>, Dec 2001 - Sep 2004
#

Summary:      Access devices via ObexFTP e.g. mobile phones
Name:         obexftp
Version:      0.23
Release:      1
Copyright:    GPL
Group:        Utilities/Console
Autoreqprov:  on
Source:       http://triq.net/obexftp/%{name}-%{version}.tar.gz
URL:          http://triq.net/obex/
BuildRoot:    %{_tmppath}/%{name}-%{version}-root
Packager:     Christian W. Zuckschwerdt <zany@triq.net>


%description
This package contains some command line tools and the ObexFTP library.
Using OpenOBEX it enables you to transfer data via IrDA, BlueTooth
as well as some custom (Siemens, Ericsson) serial port protocols.

Authors:
--------
    Christian W. Zuckschwerdt <zany@triq.net>
    

%prep
%setup

%configure

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
ln -s obexftp $RPM_BUILD_ROOT%{_bindir}/obexls
ln -s obexftp $RPM_BUILD_ROOT%{_bindir}/obexget
ln -s obexftp $RPM_BUILD_ROOT%{_bindir}/obexput
ln -s obexftp $RPM_BUILD_ROOT%{_bindir}/obexrm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS
%doc README README.bfb README.obexftp README.openobex
%{_bindir}/*
%{_libdir}/*
%{_mandir}/man?/*
%{_includedir}/*/*

