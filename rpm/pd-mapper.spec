Name:          pd-mapper
Version:       1.0
Release:       1
Summary:       Qualcomm pd-mapper
URL:           https://github.com/andersson/pd-mapper
Source0:       %{name}-%{version}.tar.gz
License:       BSD-3-Clause
BuildRequires: pkgconfig(systemd)
BuildRequires: qrtr-devel

%description
Qualcomm pd-mapper

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%make_build

%install
make prefix=%{_prefix} libdir=%{_libdir} install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_unitdir}/multi-user.target.wants
ln -s ../%{name}.service %{buildroot}/%{_unitdir}/multi-user.target.wants/%{name}.service

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_unitdir}/multi-user.target.wants/%{name}.service
%{_unitdir}/%{name}.service
