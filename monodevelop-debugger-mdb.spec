Name:     	monodevelop-debugger-mdb
Version:	2.0
Release:	%mkrel 1
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://ftp.novell.com/pub/mono/sources/monodevelop-debugger-mdb/%{name}-%{version}.tar.bz2
BuildRequires:  monodevelop >= %version
BuildRequires:  libmono-debugger-devel
BuildRequires:  mono-devel
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
