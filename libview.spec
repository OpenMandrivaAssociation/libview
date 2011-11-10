%define name libview
%define version 0.6.6
%define release %mkrel 3
%define major 2
%define libname %mklibname view %major
%define develname %mklibname -d view
Summary: VMware's Incredibly Exciting Widgets
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/view/%{name}-%{version}.tar.bz2
Patch:	 libview-0.6.2-fix-pkgconfig.patch
License: MIT
Group: System/Libraries
Url: http://view.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtkmm2.4-devel

%description
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%package -n %libname
Group: System/Libraries
Summary: VMware's Incredibly Exciting Widgets

%description -n %libname
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%package -n %develname
Group: Development/C++
Summary: VMware's Incredibly Exciting Widgets
Requires: %libname = %version-%release
Provides: libview-devel = %version-%release

%description -n %develname
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.


%prep
%setup -q
%patch -p1
#gw 0.6.6: wrong libtool version
autoreconf -fi

%build
%configure2_5x --enable-deprecated --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdvver < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS README NEWS
%_libdir/libview.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog
%_libdir/libview.so
%_libdir/libview.la
%_libdir/pkgconfig/libview.pc
%_includedir/libview

