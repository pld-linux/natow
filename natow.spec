Summary:	N.A.T.O.W - nasty armoured tanks of war!
Summary(pl):	N.A.T.O.W - paskudne opancerzone czo�gi wojenne!
Name:		natow
Version:	0.2.10
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://download.sourceforge.net/natow/%{name}-%{version}.tar.gz
Source1:	http://download.sourceforge.net/natow/%{name}-images-0.2.5.tar.gz
Source2:	http://download.sourceforge.net/natow/%{name}-levels-0.2.5.tar.gz
Source3:	http://download.sourceforge.net/natow/%{name}-models-0.2.5.tar.gz
Patch0:		%{name}-dirs.patch
Patch1:		%{name}-PREFIX.patch
Patch2:		%{name}-CFLAGS_and_LIBS.patch
Patch3:		%{name}-solo.patch
BuildRequires:	OpenGL-devel
BuildRequires:	glass-devel
BuildRequires:	glut-devel
Requires:	OpenGL
Requires:	glass
URL:		http://natow.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_datadir	/usr/share

%description
N.A.T.O.W is a 3D (openGL) tank game based loosely on scorched earth
(or the newer xscorch), but including a single player element. The
goal is to kill the other tanks and as much terrain as possible. A
project goal is to add useless objects in that can be additionally
destroyed, like buildings, alien artifacts and of course, defenseless
baby bunnies. (TODO shows, we have to wait for full playability)

%description -l pl
N.A.T.O.W to gra czo�gami bazuj�ca na scorched earth (tak�e xscorch) w
technologii 3D OpenGL. Celem jest niszczenie innych czo�g�w i
generalnie wszystkiego co si� rusza i nierusza. (TODO pokazuje, �e
jeszcze troch� trzeba poczeka� na maksymaln� grywalno��)

%prep
%setup -q -a 1 -a 2 -a 3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} all CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
export PREFIX=${RPM_BUILD_ROOT}
%{__make} install
cp -r models/ %{tmpdir}/%{name}-%{version}-root-%(id -u -n)%{_datadir}/games/%{name}-%{version}
gzip -9nf README TODO Changelog COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz TODO.gz Changelog.gz COPYING.gz
%attr(755,root,root) %{_datadir}/games/bin/*
%{_datadir}/games/%{name}-%{version}/*
%attr(755,root,root) %{_prefix}/bin/*
