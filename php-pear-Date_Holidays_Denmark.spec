%define		_class		Date
%define		_subclass	Holidays
%define		_region		Denmark
%define		upstream_name	%{_class}_%{_subclass}_%{_region}

Name:		php-pear-%{upstream_name}
Version:	0.1.3
Release:	%mkrel 5
Summary:	Driver based class to calculate holidays in %{_region}
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.21.1
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
%{upstream_name} is the Date_Holidays driver for %{_region} region.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-5mdv2012.0
+ Revision: 741852
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-4
+ Revision: 679296
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-3mdv2011.0
+ Revision: 613637
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.3-2mdv2010.1
+ Revision: 479268
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.1.3-1mdv2009.1
+ Revision: 368139
- Add spec and source files for php-pear-Date_Holidays_Denmark
- Update inscorrect package name
- Add new splited php-pear-Date_Holidays package upstream structure

