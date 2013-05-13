Summary:  	Dockapp sound mixer adjustable with mouse wheel
Name:		wmsmixer
Version:	0.5.1
Release:	10
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch0:		%name.patch
Patch1:		%name-Imakefile.patch
URL:		http://www.hibernaculum.net/wmsmixer.html
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xext)
BuildRequires:	imake

%description
 This is a hack to wmmixer which makes some changes to the display and adds a
 few new features, most notably scrollwheel support. The main changes between
 this and wmmixer are:
  o Added scrollwheel support. If your scrollwheel is mapped to buttons 4 and
    5, using it will increase/decrease the volume of the current channel.
  o Removed all the recsrc code.
  o Changed the display arrangement slightly, and replaced the recsrc button
    with a text display. This normally shows the volume of the current channel.
  o Added the setname configuration option, which allows you to give a
    different channel name (4 chars max) to the built in one if you wish.
  o Clicking on the channel icon will briefly display the text name for the
    channel. This is also displayed when you switch channels.
  o Mono channels have one wide bar rather than two thinner ones.
  o Changed some icons, and added a few new ones. Several icons are still to be
  o created. Any submissions are always welcome.

%prep
rm -rf %buildroot
%setup -q

%patch0 -p1
%patch1 -p1

%build
# due to Imakefile patch
xmkmf
CFLAGS="$RPM_OPT_FLAGS" make %name

%install
[ -d %buildroot ] && rm -rf %buildroot

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
tar xOjf %SOURCE1 %{name}-16x16.png > %buildroot%{_miconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-32x32.png > %buildroot%{_iconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-48x48.png > %buildroot%{_liconsdir}/%{name}.png

mkdir -p %buildroot%_bindir/
install -m 755 %{name} %buildroot%{_bindir}/


install -m 755 -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=WmsMixer
Comment=Dockapp sound mixer adjustable with mouse wheel
Exec=%{_bindir}/%{name} -w
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;Audio;Mixer;
EOF

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr (-,root,root)
%doc COPYING README README.wmmixer  home.wmsmixer
%{_bindir}/%{name}
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.5.1-9mdv2010.0
+ Revision: 434895
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5.1-8mdv2009.0
+ Revision: 262062
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5.1-7mdv2009.0
+ Revision: 256259
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.5.1-5mdv2008.1
+ Revision: 129421
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Thu Mar 15 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.5.1-5mdv2007.1
+ Revision: 144253
- bunzipped plaintext patches
- BuildRequires imake for xmkmf for Imakefile patch

* Tue Feb 06 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.5.1-4mdv2007.1
+ Revision: 116917
- fixed XDG desktop entry Comment
- note about mouse wheel feature in Summary
- start withdrawn when launched from the menu
- fixed and trimmed dependencies
- spec cleanup
- xdg menu migration for great compliance
- xmkmf is no more, specifying CCLINK directly in make arg

* Thu Jul 01 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.1-2mdk
- rebuild with new g++

