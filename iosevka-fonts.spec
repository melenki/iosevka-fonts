%global fontname iosevka
%global fontconf 60-%{fontname}.conf

Name:    iosevka-fonts
Version: 1.13.1
Release: 1%{?dist}
Summary: A slender monospace typeface
License: OFL

URL:     https://github.com/be5invis/Iosevka
Source0: %{url}/releases/download/v%{version}/01-iosevka-%{version}.zip
Source1: %{fontname}.conf
Source2: %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Iosevka is a slender monospace sans-serif and slab-serif typeface inspired by
Pragmata Pro, M+ and PF DIN Mono, designed to be the ideal font for programming.

Iosevka was designed by Belleve Invis, and is built from code.

%prep
%setup -cq

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p ttf/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir}
install -m 0755 -d %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
    %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0755 -p %{SOURCE2} \
    %{buildroot}%{_datadir}/appdata

%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu Jun 22 2017 scott.will.moore@gmail.com - 1.13.1-1
- Initial build.
