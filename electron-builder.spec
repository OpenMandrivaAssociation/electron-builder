%global debug_package %{nil}
%global nodejsname nodejs-%{name}

Name:		electron-builder
Version:	26.0.12
Release:    1
Summary:        A complete solution to package and build a ready for distribution Electron app with “auto update” support out of the box
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/electron-userland/electron-builder
Source0:         https://registry.npmjs.org/electron-builder/-/%{name}-%{version}.tgz
Source1:        %{name}-node_modules.tar.gz

BuildRequires:  fdupes
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
Requires:       bash
Recommends:     python3
Provides:       npm(%{name}) = %{version}

%description
%summary

%package -n %{nodejsname}
Summary:        %summary
Group:          Development/Languages/Other

%description -n %{nodejsname}
%summary

%prep
%setup -q -n package
tar -zxf %{S:1}

%install
%nodejs_install

%files -n %{nodejsname}
%license LICENSE
%{_bindir}/install-app-deps
%{_bindir}/%{name}
%{nodejs_sitelib}
