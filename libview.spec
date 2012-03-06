%define major 2
%define libname %mklibname view %{major}
%define develname %mklibname -d view

Summary: VMware's Incredibly Exciting Widgets
Name: libview
Version: 0.6.6
Release: 5
License: MIT
Group: System/Libraries
Url: http://view.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/view/%{name}-%{version}.tar.bz2
Patch0:	 libview-0.6.2-fix-pkgconfig.patch
BuildRequires: gtkmm2.4-devel
BuildRequires: ffi5-devel

%description
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%package -n %{libname}
Group: System/Libraries
Summary: VMware's Incredibly Exciting Widgets

%description -n %{libname}
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%package -n %{develname}
Group: Development/C++
Summary: VMware's Incredibly Exciting Widgets
Requires: %{libname} = %{version}-%{release}
Provides: libview-devel = %{version}-%{release}

%description -n %{develname}
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%prep
%setup -q
%apply_patches
#gw 0.6.6: wrong libtool version
autoreconf -fi

%build
%configure2_5x \
	--enable-deprecated \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%doc AUTHORS README NEWS
%{_libdir}/libview.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/libview.so
%{_libdir}/pkgconfig/libview.pc
%{_includedir}/libview

