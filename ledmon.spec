%define major 1
%define libname %mklibname led
%define devname %mklibname led -d

Name:		ledmon
Version:	1.1.0
Release:	1
Source0:	https://github.com/intel/ledmon/archive/refs/tags/v%{version}.tar.gz
Summary:	Enclosure LED Utilities
URL:		https://github.com/intel/ledmon
License:	GPL-2.0
Group:		System/Libraries
BuildRequires:	autoconf automake slibtool autoconf-archive
BuildRequires:	sg3_utils-devel
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(check)
BuildSystem:	autotools
BuildOption:	--enable-systemd
BuildOption:	--enable-library
BuildOption:	--enable-test

%description
Enclosure LED utilities

%package -n %{libname}
Summary:	Enclosure LED utilities
Group:		System/Libraries

%description -n %{libname}

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
./autogen.sh

%conf -p
export CFLAGS="%{build_cflags} -I$(pwd)/src/lib/include"

%files
%doc %{_docdir}/ledmon
%{_bindir}/*
%{_mandir}/man*/*
%{_unitdir}/ledmon.service

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
