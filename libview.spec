%define major 2
%define libname %mklibname view %{major}
%define devname %mklibname -d view

Summary:	VMware's Incredibly Exciting Widgets
Name:		libview
Version:	0.6.6
Release:	7
License:	MIT
Group:		System/Libraries
Url:		http://view.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/view/%{name}-%{version}.tar.bz2
Patch0:		libview-0.6.2-fix-pkgconfig.patch
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libffi)

%description
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%package -n %{libname}
Group:		System/Libraries
Summary:	VMware's Incredibly Exciting Widgets

%description -n %{libname}
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%package -n %{devname}
Group:		Development/C++
Summary:	VMware's Incredibly Exciting Widgets
Requires:	%{libname} = %{version}-%{release}
Provides:	libview-devel = %{version}-%{release}

%description -n %{devname}
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%prep
%setup -q
%apply_patches
sed -i 's/AM_CONFIG_HEADER/AC_CONFIG_HEADER/g' configure.ac
sed -i 's/AM_PROG_CC_STDC/AC_PROG_CC/g' configure.ac
autoreconf -fi

%build
%configure2_5x \
	--enable-deprecated \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libview.so.%{major}*

%files -n %{devname}
%doc ChangeLog AUTHORS README NEWS
%{_libdir}/libview.so
%{_libdir}/pkgconfig/libview.pc
%{_includedir}/libview

