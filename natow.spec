Summary:	N.A.T.O.W - nasty armoured tanks of war!
Summary(pl):	N.A.T.O.W - paskudne opancerzone czo³gi wojenne!
Name:		natow
Version:	0.2.10
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/natow/%{name}-%{version}.tar.gz
# Source0-md5:	5a7763969944f6f17a8fa03ea95afbf2
Source1:	http://dl.sourceforge.net/natow/%{name}-images-0.2.5.tar.gz
# Source1-md5:	6aebe8aff723d49a4e75a6c01affca93
Source2:	http://dl.sourceforge.net/natow/%{name}-levels-0.2.5.tar.gz
# Source2-md5:	51b1392a920bd86e57eaa5c95d680a36
Source3:	http://dl.sourceforge.net/natow/%{name}-models-0.2.5.tar.gz
# Source3-md5:	fc66d0e77eb8d4cb5c0c5e3b9077f4da
Patch0:		%{name}-install.patch
Patch1:		%{name}-CFLAGS_and_LIBS.patch
Patch2:		%{name}-chdir.patch
Patch3:		%{name}-glass.patch
URL:		http://natow.sourceforge.net/
BuildRequires:	glass-devel >= 1.3.1
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
N.A.T.O.W is a 3D (openGL) tank game based loosely on scorched earth
(or the newer xscorch), but including a single player element. The
goal is to kill the other tanks and as much terrain as possible. A
project goal is to add useless objects in that can be additionally
destroyed, like buildings, alien artifacts and of course, defenseless
baby bunnies. (TODO shows, we have to wait for full playability)

%description -l pl
N.A.T.O.W to gra czo³gami bazuj±ca na scorched earth (tak¿e xscorch) w
technologii 3D OpenGL. Celem jest niszczenie innych czo³gów i
generalnie wszystkiego co siê rusza i nie rusza. (TODO pokazuje, ¿e
jeszcze trochê trzeba poczekaæ na maksymaln± grywalno¶æ)

%prep
%setup -q -a 1 -a 2 -a 3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} all -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -DUSE_GLASS -I/usr/X11R6/include -I/usr/include/glass -DNATOW_VERSION_STRING=\\\"\$(VERSION)\\\"" \
	LIBS="-lGL -lglut -lGLU -lm -L/usr/X11R6/%{_lib} -lXi -lXmu -lglass"

cp src/natow .
# workaround to not relink on install
touch src/all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_prefix}

cp -R models $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO Changelog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
