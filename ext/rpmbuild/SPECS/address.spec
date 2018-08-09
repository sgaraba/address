Summary:            Address Book Application
Name:               address
Version:            VERSION
Release:			1%{?dist}
License:            GPLv2+
Group:              Applications/Other
BuildRoot: 			%{_builddir}/%{name}
URL:                http://esempla.com
Packager:			Sergiu Garaba
Requires:			jre >= 1.7.0

%description
Address App is a cross-platform address book application written in Java.


The program provides an easy to use GUI interface and is very extensible,
see http://esempla.com/ for more information.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/address $RPM_BUILD_ROOT/%{_datadir}/applications $RPM_BUILD_ROOT/%{_datadir}/pixmaps $RPM_BUILD_ROOT/%{_bindir}
cp ../../../target/%{name}-%{version}.jar $RPM_BUILD_ROOT/%{_libdir}/address/
cp ../../../src/main/resources/ext/deb-bundle/usr/share/applications/address.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/
cp ../../../src/main/resources/images/icon128.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/address.png
echo "#/bin/sh" > $RPM_BUILD_ROOT/%{_bindir}/address
echo "java -jar %{_libdir}/address/address*.jar" >> $RPM_BUILD_ROOT/%{_bindir}/address
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/address

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/address/%{name}-%{version}.jar
%{_datadir}/applications/address.desktop
%{_datadir}/pixmaps/address.png
%{_bindir}/address
