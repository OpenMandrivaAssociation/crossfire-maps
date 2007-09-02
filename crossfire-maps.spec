%define version 1.10.0
%define release %mkrel 1

Name:		crossfire-maps
Version:	%{version}
Release:	%{release}
Summary:	Map files for Crossfire, a graphical adventure game
Group:		Games/Adventure
License:	GPL
URL:		http://crossfire.real-time.com/
Source0:	http://prdownloads.sourceforge.net/crossfire/crossfire-%{version}.maps.tar.bz2
Source1:	crossfire-maps.README.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch

%description
Crossfire is a highly graphical role-playing adventure game
with characteristics reminiscent of rogue, nethack, omega, and gauntlet.
It has multiplayer capability and presently runs under X11.

This package contains map files necessary for crossfire server to
run. If you just want to play crossfire only, you don't need this package.

%prep
# since the archive is quite large and takes long time to decompress, so
# unpack it during %%install to save some time
%setup -q -T -c
bzip2 -dc %SOURCE1 > README

%build

%install
[ -z "$RPM_BUILD_ROOT" -o "$RPM_BUILD_ROOT" = "/" ] || rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_gamesdatadir}/crossfire
tar --bzip2 -xf %SOURCE0 -C $RPM_BUILD_ROOT%{_gamesdatadir}/crossfire/

# cleanup
find $RPM_BUILD_ROOT%{_gamesdatadir}/crossfire -name '.#*' -type f -print0 | xargs -r -0 rm -f

%clean
[ -z "$RPM_BUILD_ROOT" -o "$RPM_BUILD_ROOT" = "/" ] || rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc README
%{_gamesdatadir}/crossfire


