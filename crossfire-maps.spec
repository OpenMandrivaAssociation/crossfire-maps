%define version 1.70.0
%define release 2

Name:		crossfire-maps
Version:	%{version}
Release:	%{release}
Summary:	Map files for Crossfire, a graphical adventure game
Group:		Games/Adventure
License:	GPL
URL:		http://crossfire.real-time.com/
Source0:	http://downloads.sourceforge.net/project/crossfire/crossfire-%{version}/crossfire-%{version}.maps.tar.bz2
Source1:	crossfire-maps.README
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
cp %{SOURCE1} README

%build

%install
mkdir -p %{buildroot}%{_gamesdatadir}/crossfire
tar -xvf %SOURCE0 -C %{buildroot}%{_gamesdatadir}/crossfire/

# cleanup
find %{builddoot}%{_gamesdatadir}/crossfire -name '.#*' -type f -print0 | xargs -r -0 rm -f

%files
%defattr(0644,root,root,0755)
%doc README
%{_gamesdatadir}/crossfire/*
