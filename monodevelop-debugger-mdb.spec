Name:     	monodevelop-debugger-mdb
Version:	2.4
Release:	%mkrel 2
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://ftp.novell.com/pub/mono/sources/monodevelop-debugger-mdb/%{name}-%{version}.tar.bz2
BuildRequires:  monodevelop >= %version
BuildRequires:  libmono-debugger-devel
BuildRequires:  mono-addins-devel
Summary:	Monodevelop Mono Debugger Addin
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Monodevelop Mono Debugger Addin


%prep
%setup -q

%build
./configure --prefix=%_prefix
%make

%install
rm -rf "$RPM_BUILD_ROOT" %name.lang
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%_prefix/share/pkgconfig
mv $RPM_BUILD_ROOT%_prefix/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%_prefix/share/pkgconfig
#gw fix pkgconfig file:
perl -pi -e "s/^Version.*/Version:%version/" %buildroot%_datadir/pkgconfig/mono.debugging.backend.mdb.pc

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-, root, root)
%_prefix/lib/monodevelop/AddIns/MonoDevelop.Debugger/
%_datadir/pkgconfig/mono.debugging.backend.mdb.pc


%changelog
* Thu Jul 14 2011 Götz Waschk <waschk@mandriva.org> 2.4-2
+ Revision: 689973
- update build deps

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 2.4-1mdv2011.0
+ Revision: 550714
- new version

* Thu Feb 04 2010 Götz Waschk <waschk@mandriva.org> 2.2.1-1mdv2010.1
+ Revision: 500676
- update to new version 2.2.1

* Tue Dec 15 2009 Götz Waschk <waschk@mandriva.org> 2.2-1mdv2010.1
+ Revision: 478915
- update to new version 2.2

* Fri Dec 11 2009 Götz Waschk <waschk@mandriva.org> 2.1.2-1mdv2010.1
+ Revision: 476492
- update to new version 2.1.2

* Tue Nov 10 2009 Götz Waschk <waschk@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 464200
- update to new version 2.1.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Mar 31 2009 Götz Waschk <waschk@mandriva.org> 2.0-1mdv2009.1
+ Revision: 362824
- new version

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 1.9.3-1mdv2009.1
+ Revision: 356880
- update to new version 1.9.3

* Thu Feb 12 2009 Götz Waschk <waschk@mandriva.org> 1.9.2-1mdv2009.1
+ Revision: 339832
- update to new version 1.9.2

* Mon Nov 24 2008 Götz Waschk <waschk@mandriva.org> 1.9.1-1mdv2009.1
+ Revision: 306277
- import monodevelop-debugger-mdb


