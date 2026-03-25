%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Library and components for secure lock screen architecture
Name:		sonic-screenlocker
Version:	6.6.3.2
Release:	%{?git:0.%{git}.}2
License:	GPLv2+
Group:		Graphical desktop/SonicDE
URL:		https://github.com/Sonic-DE/sonic-screenlocker
# %if 0%{?git:1}
# Source0:	https://invent.kde.org/plasma/kscreenlocker/-/archive/%{gitbranch}/kscreenlocker-%{gitbranchd}.tar.bz2#/kscreenlocker-%{git}.tar.bz2
# %else
Source0:	%url/archive/refs/tags/%version.tar.gz#/%name-%version.tar.gz
# %endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(libseccomp)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	cmake(KF6I18n)

# pending rename
# BuildRequires:	cmake(Plasma) >= 5.90.0
# BuildRequires:	cmake(PlasmaQuick) >= 5.90.0
BuildRequires:  %{_lib}SonicDE-devel

BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6IdleTime)
BuildRequires:	cmake(KF6Crash)

# pending rename
# BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:  %{_lib}SonicDEKeybindDaemon-devel

BuildRequires:	cmake(LayerShellQt) >= 5.27.80

#pending rename
#BuildRequires:	cmake(KF6Screen)
BuildRequires:  %{_lib}SonicDEScreen-devel

BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Svg)

# pending rename
#BuildRequires:	cmake(KF6KIO)
BuildRequires:  %{_lib}SonicFrameworksIO-devel

BuildRequires:	cmake(KF6Solid)
BuildRequires:	pam-devel
Conflicts:      kscreenlocker
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed 2025-05-01 after 6.0
#rename plasma6-kscreenlocker

%description
Library and components for secure lock screen architecture.

%triggerin -- %{name} < %{EVRD}
%{_bindir}/killall kscreenlocker_greet > /dev/null 2>&1 ||:

%files -f %{name}.lang
%{_libdir}/libexec/kscreenlocker_greet
%{_datadir}/dbus-1/interfaces/kf6_org.freedesktop.ScreenSaver.xml
%{_datadir}/knotifications6/ksmserver.notifyrc
%{_datadir}/ksmserver/screenlocker/org.kde.passworddialog
%{_datadir}/dbus-1/interfaces/org.kde.screensaver.xml
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_screenlocker.so
%{_datadir}/applications/kcm_screenlocker.desktop
%{_datadir}/qlogging-categories6/kscreenlocker.categories

#--------------------------------------------------------------------

%define sonicscreenlocker_major 6
%define libsonic_screenlocker %mklibname %name

%package -n %{libsonic_screenlocker}
Summary:	Library and components for secure lock screen architecture 
Group:		System/Libraries
Conflicts:      %{_lib}kscreenlocker

%description -n %{libsonic_screenlocker}
Library and components for secure lock screen architecture.

%files -n %{libsonic_screenlocker}
%{_libdir}/libKScreenLocker.so.*

#--------------------------------------------------------------------

%define libsonic_screenlocker_devel %mklibname %name -d

%package -n %{libsonic_screenlocker_devel}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{name} = %{EVRD}
Requires:       %{libsonic_screenlocker} = %{EVRD}
Requires:       cmake(Qt6DBus)
Provides:       %{name}-devel = %{EVRD}
Conflicts:      %{_lib}kscreenlocker-devel

%description -n %{libsonic_screenlocker_devel}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{libsonic_screenlocker_devel}
%{_libdir}/libKScreenLocker.so
%{_includedir}/KScreenLocker
%{_libdir}/cmake/KScreenLocker
%{_libdir}/cmake/ScreenSaverDBusInterface
