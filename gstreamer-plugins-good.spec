%define         gstreamer       gstreamer
%define         majorminor      0.10

%define         _gst            0.10.29
%define         _gstpb          0.10.29

Name:           %{gstreamer}-plugins-good
Version:        0.10.23
Release:        1%{?dist}
Summary:        GStreamer plug-ins with good code and licensing

Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       %{gstreamer} >= %{_gst}
Requires(pre):  GConf2 
Requires(preun): GConf2
Requires(post): GConf2
Requires:       gstreamer-plugins-base
# superceded by the package above and ourselves
Obsoletes:      gstreamer-plugins

BuildRequires:  %{gstreamer}-devel >= %{_gst}
BuildRequires:  %{gstreamer}-plugins-base-devel >= %{_gstpb}

BuildRequires:  liboil-devel >= 0.3.6
BuildRequires:  gettext
BuildRequires:  gcc-c++

BuildRequires:  cairo-devel
# cairo pulls in Xrender, but -devel has a missing dep on libX11-devel
BuildRequires:  libX11-devel
BuildRequires:  flac-devel >= 1.1.3
BuildRequires:  GConf2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel >= 1.2.0
BuildRequires:  glibc-devel
BuildRequires:  speex-devel
BuildRequires:  gtk2-devel
BuildRequires:  libshout-devel
BuildRequires:  taglib-devel
BuildRequires:  wavpack-devel
BuildRequires:  libsoup-devel
BuildRequires:  kernel-headers
BuildRequires:  pulseaudio-libs-devel

%ifnarch s390 s390x
BuildRequires:  libdv-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libv4l-devel
%endif

# documentation
BuildRequires:  gtk-doc
BuildRequires:  python-devel PyXML
BuildRequires:  hal-devel

Provides: gstreamer-plugins-pulse = 0.9.8-1
Obsoletes: gstreamer-plugins-pulse < 0.9.8

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

GStreamer Good Plug-ins is a collection of well-supported plug-ins of
good quality and under the LGPL license.

%package devel
Summary:        Dummy package to make gstreamer-plugins-good multilib
Group:          Development/Libraries

Requires:       %{name} = %{version}-%{release}

%description devel
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

GStreamer Good Plug-ins is a collection of well-supported plug-ins of
good quality and under the LGPL license.

This is a dummy package to make gstreamer-plugins-good multilib.

%prep
%setup -q -n gst-plugins-good-%{version}

%build

%configure \
  --with-package-name='Fedora gstreamer-plugins-good package' \
  --with-package-origin='http://download.fedora.redhat.com/fedora' \
  --disable-gtk-doc \
  --enable-experimental \
  --disable-monoscope \
  --disable-esd --disable-libcaca --disable-aalib \
  --with-default-visualizer=autoaudiosink

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang gst-plugins-good-%{majorminor}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gst-plugins-good-%{majorminor}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README REQUIREMENTS

# Equaliser presets
%{_datadir}/gstreamer-%{majorminor}/presets/

# non-core plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstalaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstalphacolor.so
%{_libdir}/gstreamer-%{majorminor}/libgstalpha.so
%{_libdir}/gstreamer-%{majorminor}/libgstannodex.so
%{_libdir}/gstreamer-%{majorminor}/libgstapetag.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofx.so
%{_libdir}/gstreamer-%{majorminor}/libgstauparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstautodetect.so
%{_libdir}/gstreamer-%{majorminor}/libgstavi.so
%{_libdir}/gstreamer-%{majorminor}/libgstcutter.so
%{_libdir}/gstreamer-%{majorminor}/libgstdebug.so
%{_libdir}/gstreamer-%{majorminor}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstefence.so
%{_libdir}/gstreamer-%{majorminor}/libgsteffectv.so
%{_libdir}/gstreamer-%{majorminor}/libgstequalizer.so
%{_libdir}/gstreamer-%{majorminor}/libgstflv.so
%{_libdir}/gstreamer-%{majorminor}/libgstflxdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstgoom2k1.so
%{_libdir}/gstreamer-%{majorminor}/libgstgoom.so
%{_libdir}/gstreamer-%{majorminor}/libgsticydemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3demux.so
%{_libdir}/gstreamer-%{majorminor}/libgstimagefreeze.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterleave.so
%{_libdir}/gstreamer-%{majorminor}/libgstlevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstmatroska.so
%{_libdir}/gstreamer-%{majorminor}/libgstmulaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstmultifile.so
%{_libdir}/gstreamer-%{majorminor}/libgstmultipart.so
%{_libdir}/gstreamer-%{majorminor}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{majorminor}/libgstqtdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstreplaygain.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstshapewipe.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmpte.so
%{_libdir}/gstreamer-%{majorminor}/libgstspectrum.so
%{_libdir}/gstreamer-%{majorminor}/libgstudp.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideobox.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideocrop.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideofilter.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideomixer.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstximagesrc.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4menc.so

# gstreamer-plugins with external dependencies but in the main package
%{_libdir}/gstreamer-%{majorminor}/libgstcairo.so
%{_libdir}/gstreamer-%{majorminor}/libgstflac.so
%{_libdir}/gstreamer-%{majorminor}/libgstgconfelements.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdkpixbuf.so
%{_libdir}/gstreamer-%{majorminor}/libgsthalelements.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstoss4audio.so
%{_libdir}/gstreamer-%{majorminor}/libgstossaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstpng.so
%{_libdir}/gstreamer-%{majorminor}/libgstpulse.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{majorminor}/libgstshout2.so
%{_libdir}/gstreamer-%{majorminor}/libgstsouphttpsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeex.so
%{_libdir}/gstreamer-%{majorminor}/libgsttaglib.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavpack.so

%ifnarch s390 s390x
%{_libdir}/gstreamer-%{majorminor}/libgstdv.so
%{_libdir}/gstreamer-%{majorminor}/libgst1394.so
%endif

## Libraries

# schema files
%{_sysconfdir}/gconf/schemas/gstreamer-%{majorminor}.schemas

%files devel
%defattr(-, root, root)

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/gstreamer-%{majorminor}.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/gstreamer-%{majorminor}.schemas > /dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/gstreamer-%{majorminor}.schemas > /dev/null || :

%changelog
* Thu Jun 17 2010 Benjamin Otte <otte@redhat.com> 0.10.23-1
- Update to 0.10.23
- Sync with Fedora packages
Resolves: rhbz#603108

* Sun Jun 06 2010 Benjamin Otte <otte@redhat.com> 0.10.18-2
- Get rid of tabs - use spaces instead.
Resolves: rhbz#600985

* Mon Feb 15 2010 Benjamin Otte <otte@redhat.com> 0.10.18-1
- Update to 0.10.18
Related: rhbz#561911

* Fri Feb 12 2010 Benjamin Otte <otte@redhat.com> 0.10.17-3
- Remove mikmod plugin
Related: rhbz#564478

* Fri Jan 08 2010 Bastien Nocera <bnocera@redhat.com> 0.10.17-2
- Update Farsight plugins to 0.10.17
- Disable LADSPA plugins, they should be in -bad (#540198)
- Add support for authenticating RTSP sources
Related: rhbz#543948

* Tue Nov 17 2009 Bastien Nocera <bnocera@redhat.com> 0.10.17-1
- Update to 0.10.17

* Tue Nov 03 2009 Bastien Nocera <bnocera@redhat.com> 0.10.16-7
- Really check for PA < 0.9.20

* Tue Nov 03 2009 Bastien Nocera <bnocera@redhat.com> 0.10.16-6
- Add patch from upstream to avoid volume lowering in PA < 0.9.20

* Thu Oct 22 2009 Bastien Nocera <bnocera@redhat.com> 0.10.16-5
- Update farsight plugins from -bad
- Drop copy/pasted rtpmanager plugin, it's now in -good

* Mon Oct 19 2009 Bastien Nocera <bnocera@redhat.com> 0.10.16-4
- Fix pulsesink not advertising the StreamVolume interface

* Sat Oct 17 2009 Bastien Nocera <bnocera@redhat.com> 0.10.16-3
- Finally fix pulsesink volume lowering problems (#488532)

* Fri Oct 16 2009 Bastien Nocera <bnocera@redhat.com> 0.10.16-2
- Fix autoconvert caps negotiation

* Tue Sep 01 2009 Bastien Nocera <bnocera@redhat.com> 0.10.16-1
- Update to 0.10.16

* Fri Aug 14 2009 Bastien Nocera <bnocera@redhat.com> 0.10.15.3-1
- Update to 0.10.15.3

* Tue Aug 11 2009 Hans de Goede <hdegoede@redhat.com> 0.10.15-6
- Fix usage of webcamdrivers which do not implement VIDIOC_G_PARM (#467961)
- Include "Fix FLAC seeking" patch from F-11 package (#515886)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.10.15-4
- Add missing provides on gst-plugins-farsight.

* Mon Jun 22 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.10.15-3
- Add obsolete for gst-plugins-farsight.

* Mon Jun 22 2009 Bastien Nocera <bnocera@redhat.com> 0.10.15-2
- Add the farsight plugins from gst-plugins-bad 0.10.13 (#507009)

* Thu May 21 2009 Bastien Nocera <bnocera@redhat.com> 0.10.15-1
- Update to 0.10.15

* Sat May 16 2009 Bastien Nocera <bnocera@redhat.com> 0.10.14.3-1
- Update to 0.10.14.3

* Tue May 12 2009 Bastien Nocera <bnocera@redhat.com> 0.10.14.2-1
- Update to 0.10.14.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.14-1
- Update to 0.10.14

* Mon Feb 16 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.13.3-1
- Updat eto 0.10.13.3 pre-release

* Tue Feb 10 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.13.2-2
- Add patches to fix compilation

* Sun Feb 08 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.13.2-1
- Update to 0.10.13.2 pre-release

* Mon Feb 02 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.13-3
- Remove (unapplied) patch, it's not needed on this version

* Mon Feb 02 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.13-2
- Patch for overflows in the QT demuxer (#481267)

* Mon Jan 26 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.13-1
- Update to 0.10.13
- Update libv4l patch

* Wed Jan 21 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.11-5
- Rebuild for new gstreamer base library

* Wed Jan 14 2009 Warren Togami <wtogami@redhat.com> 0.10.11-4
- Bug #477877 Fix multilib conflict in -devel
- Bug #478449 Fix ladspa on lib64 

* Wed Jan 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.10.11-3
- Bug #470000 Fix thread/memleak due to ref-loop

* Tue Jan 13 2009 Bastien Nocera <bnocera@redhat.com> - 0.10.11-2
- Avoid pulsesink hang when PulseAudio disappears

* Sat Oct 25 2008 Bastien Nocera <bnocera@redhat.com> - 0.10.11-1
- Update to 0.10.11
- Update libv4l patch

* Thu Oct 23 2008 Lennart Poettering <lpoetter@redhat.com> 0.10.10-6
- Enable the PulseAudio element and make it replace the old
  pulseaudio-plugins-pulse package

* Sun Oct  5 2008 Hans de Goede <hdegoede@redhat.com> 0.10.10-5
- Fix gst-plugins-good-0.10.9-libv4l.patch to also patch config.in and
  Makefile.in so that the libv4l code actually gets enabled for real this time
  and remove plenty of egg from face for not fixing this properly in 0.10.10-2
  (rh465599)
- Explicitly disable pulse plugin so the spec builds even if you
  have the pulse devel packages installed.

* Fri Sep 12 2008 - Bastien Nocera <bnocera@redhat.com> 0.10.10-4
- Another rebuild

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> 0.10.10-3
- Rebuild for GStreamer RPM provides

* Sun Aug 31 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.10-2
- Fix gst-plugins-good-0.10.9-libv4l.patch to not only patch configure.ac
  but also configure so that the libv4l code actually gets enabled

* Wed Aug 27 2008 - Bastien Nocera <bnocera@redhat.com> 0.10.10-1
- Update to 0.10.10
- Remove cdio plugin, as it was moved to -ugly upstream

* Sun Aug 10 2008 Adam Jackson <ajax@redhat.com> 0.10.9-2
- gst-plugins-good-0.10.9-libv4l.patch: Use libv4l. (#456825)
- Explicitly disable esd/caca/aalib plugins so the spec builds even if you
  have their devel packages installed.

* Mon Aug 04 2008 Adam Jackson <ajax@redhat.com> 0.10.9-1
- Update to 0.10.9

* Wed Jul 30 2008 - Bastien Nocera <bnocera@redhat.com> 0.10.8-10
- Build the docs ourselves

* Tue Jul 22 2008 Jarod Wilson <jwilson@redhat.com> 0.10.8-9
- Bump and rebuild for libraw1394 v2.0.0

* Mon Jul 21 2008 Adam Jackson <ajax@redhat.com> 0.10.8-8
- gst-plugins-good-0.10.8-v4l2-progressive-fix.patch: Backport v4l2
  interlace/progressive fixes. (#454534)

* Thu Jun 19 2008 Adam Jackson <ajax@redhat.com> 0.10.8-7
- gst-plugins-good-0.10.8-speex-nego.patch: Backport speex channel and
  rate negotiation from 0.10.9. (#451391)

* Tue Jun 17 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.8-6
- Really fix the default audio output not being correct

* Tue Jun 03 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.8-5
- Fix compilation of the v4l2 plugin with newer kernels

* Mon Jun 02 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.8-4
- Work-around bug that would set the default audio output to "GOOM!"
  See http://bugzilla.gnome.org/show_bug.cgi?id=532295

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.10.8-3
- fix license tag

* Wed May 21 2008 Adam Jackson <ajax@redhat.com> 0.10.8-2
- BR: libsoup-devel and package the soup http src plugin. (#447604)
- s/Fedora Core/Fedora/

* Thu Apr 24 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.8-1
- Update to 0.10.8

* Thu Apr 10 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.7-2
- Add patch to unbreak the QuickTime demuxer plugin

* Thu Feb 21 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.7-1
- Update to 0.10.7

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.10.6-8
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Adam Jackson <ajax@redhat.com> 0.10.6-7
- gst-plugins-good-0.10.6-v4l2-min-buffers.patch: Be sure to get at least
  GST_V4L2_MIN_BUFFERS from the source. (#316931)
- gst-plugins-good-0.10.6-artist-sortname.patch: Avoid using a deprecated
  #define.

* Mon Oct 08 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.6-6
- Kill esound output, as we don't have esound installed anymore, just
  Pulseaudio (#323061)

* Sun Sep 02 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.6-5
- Add a patch to fix id3demux, so that MP3s can be played back
  (#273561)

* Tue Aug 28 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.6-4
- Add the ladspa plugins (#253375)

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 0.10.6-3
- Rebuild for build id

* Sun Aug 12 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.6-2
- Enable experimental plugins, the wavepack and v4l2src plugins (#250886)

* Tue Jun 19 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.6-1
- Update to 0.10.6
- Remove outdated FLAC patch
- Add new plugins

* Sat May  5 2007  Matthias Clasen  <mclasen@redhat.com> - 0.10.5-6
- Add libshout-devel, taglib-devel, libcdio-devel as BRs (#136268)

* Tue Feb 13 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.5-5
- Don't forget to run autoreconf when modifiying the configure.ac

* Tue Feb 13 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.5-4
- Move cyclic dependency with -plugins-good and -plugins-base from
  gstreamer to here

* Tue Feb 13 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.5-3
- Patch from Matthias Clasen <mclasen@redhat.com> for the libFLAC
  1.1.3 update (#222946)

* Wed Jan 24 2007 Adam Jackson <ajax@redhat.com> - 0.10.5-2
- Re-add the gdkpixbuf loader.  (#222837)

* Wed Jan 17 2007 Matthias Clasen <mclasen@redhat.com> - 0.10.5-1
- Update to 0.10.5

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.4-2
- Fix scripts according to the packaging guidelines

* Sat Aug 26 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.4-1
- Update to 0.10.4

* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.3-5
- Disable gtk-doc to fix multilib conflicts

* Wed Jul 19 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.3-4
- Rebuild 

* Tue Jul 18 2006 John (J5) Palmieri <johnp@redhat.com> - 0.10.3-3
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.10.3-2.1
- rebuild

* Wed May 31 2006 Dan Williams  <dcbw@redhat.com> - 0.10.3-2
- Package gsthalelements plugin so this can be pushed out

* Mon May 22 2006 Matthias Clasen  <mclasen@redhat.com> - 0.10.3-1
- Update to 0.10.3

* Fri Feb 10 2006 Christopher Aillon <caillon@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.10.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 John (J5) Palmieri <johnp@redhat.com>  0.10.1-1
- Upgrade to 0.10.1
- Add libgstid3demux.so to the files section

* Wed Jan 04 2006 Warren Togami <wtogami@redhat.com>  0.10.0-2
- exclude 1394 stuff from s390 and s390x

* Sat Dec 17 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-1
- rebuilt for FC devel

* Wed Dec 14 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-0.gst.2
- glib 2.8
- added cairo

* Mon Dec 05 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-0.gst.1
- new release

* Thu Dec 01 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.7-0.gst.1
- new release for major/minor 0.10
- removed pango
- removed videofilter
- added cutter, multipart

* Sat Nov 12 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.5-0.gst.1
- new release

* Mon Oct 24 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.4-0.gst.1
- new release
- added alphacolor, debug, flxdec, matroska, navigationtest, videomixer
  plug-ins

* Mon Oct 03 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.3-0.gst.1
- new release
- fdsrc moved back to core
- added auparse and efence plugins
- added gtk-doc

* Fri Sep 09 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- Initial package

* Fri Sep 02 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- clean up for splitup
