%global fontname iosevka
%global fontconf 60-%{fontname}

Name:    iosevka-fonts
Version: 1.13.1
Release: 2%{?dist}
Summary: A slender monospace typeface
License: OFL
URL:     https://github.com/be5invis/Iosevka

Source0: %{url}/releases/download/v%{version}/01-iosevka-%{version}.zip
Source1: %{fontname}.conf
Source2: %{fontname}.metainfo.xml

Source3: %{url}/releases/download/v%{version}/02-iosevka-term-%{version}.zip
Source4: %{fontname}-term.conf
Source5: %{fontname}-term.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel

%global common_desc \
Iosevka is a slender monospace sans-serif and slab-serif typeface inspired by \
Pragmata Pro, M+ and PF DIN Mono, designed to be the ideal font for \
programming. The font is designed by Belleve Invis. \
 \
As the font is built entirely from code, many variations of the font can be \
maintained and developed. This allows multiple pre-built variants to be \
packaged in order to suit the users needs. Many of the possible variations are \
described below. \
 \
 - shape: the shape of various glyphs, like i, l, 0, etc. \
 - spacing: how wide some specific characters are. \
 - slab: whether the font has slab-serifs. \
 - ligatures: whether the font contains ligatures. \

%description
%common_desc


%package common

Summary:  Common files for Iosevka fonts
Requires: fontpackages-filesystem

%description common
%common_desc

This package contains files used by other Iosevka packages.


%package -n %{fontname}-default-fonts

Summary:  Iosevka fonts
Requires: %{fontname}-common

%description -n %{fontname}-default-fonts
%common_desc

This specific pacakge contains the Iosevka fonts. It contains the following
variations.

 - shape: default
 - spacing: default
 - slab: no
 - ligatures: yes


%package -n %{fontname}-term-fonts

Summary:  Iosevka Term fonts
Requires: %{fontname}-common

%description -n %{fontname}-term-fonts
%common_desc

This specific pacakge contains the Iosevka Term fonts. It contains the
following variations.

 - shape: default
 - spacing: terminal
 - slab: no
 - ligatures: no


%prep
%setup -c -T -D -a 0
%setup -c -T -D -a 3

%install
# ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p ttf/iosevka-*.ttf %{buildroot}%{_fontdir}

# fontconf
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
    %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{_sourcedir}/%{fontname}.conf \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{_sourcedir}/%{fontname}-term.conf \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-term.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
    %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-term.conf \
    %{buildroot}%{_fontconfig_confdir}/%{fontconf}-term.conf

# appstream
install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0755 -p %{_sourcedir}/%{fontname}.metainfo.xml \
    %{buildroot}%{_datadir}/appdata
install -m 0755 -p %{_sourcedir}/%{fontname}-term.metainfo.xml \
    %{buildroot}%{_datadir}/appdata

# fonts
%_font_pkg -n default -f %{fontconf}.conf iosevka-{th,ex,li,re,it,ob,me,bo,he}*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -n term -f %{fontconf}-term.conf iosevka-term-*.ttf
%{_datadir}/appdata/%{fontname}-term.metainfo.xml

%changelog
* Thu Jun 22 2017 scott.will.moore@gmail.com - 1.13.1-1
- Initial build.
