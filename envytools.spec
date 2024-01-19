%global gitdate 20200810

Name:           envytools
Version:        0.0
Release:        0.28.git%{gitdate}%{?dist}
Summary:        Tools for people envious of nvidia's blob driver
License:        MIT
URL:            https://github.com/envytools/envytools
# Generated by make-git-snapshot.sh
Source0:        envytools-%{gitdate}.tar.bz2
Source1:        make-git-snapshot.sh
Patch1:         envytools-add-missing-GETPARAM_PHYS-defines.patch
ExclusiveArch: %{ix86} x86_64 %{arm} aarch64
BuildRequires:  gcc g++
BuildRequires:  cmake flex bison
BuildRequires:  libpciaccess-devel libX11-devel libXext-devel libseccomp-devel
BuildRequires:  libxml2-devel libvdpau-devel libdrm-devel python3-devel

%description
Envytools contains a number of tools used for debugging / development of
the nouveau driver:

envydis: Disassembler and assembler for various ISAs found on nvidia GPUs
nvbios:  Tools to decode the card description structures found in nvidia VBIOS
nva:     Tools to directly access the GPU registers
vstream: Tools to decode and encode raw video bitstreams


%package        hwdocs
Summary:        Nouveau hardware documentation
BuildArch:      noarch

%description    hwdocs
The %{name}-hwdocs package contains hardware documentation for video
hardware supported by the nouveau driver project.


%prep
%autosetup -p1 -n %{name}-%{gitdate}


%build

%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build


%install
%cmake_install
cp -p COPYING $RPM_BUILD_ROOT%{_docdir}/%{name}
# Remove the tools for rules-ng-ng XML register db manipulation
rm $RPM_BUILD_ROOT%{_bindir}/headergen
rm $RPM_BUILD_ROOT%{_bindir}/lookup
# Remove hwtest this really is for developers only
rm $RPM_BUILD_ROOT%{_bindir}/hwtest
# We do not want the libs (these are for internal use only)
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm -r $RPM_BUILD_ROOT%{_includedir}/%{name}
# Remove the python scripts used to generate the docs
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/hwdocs/*.py


%files
%doc %dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/README*
%{_bindir}/de*
%{_bindir}/dumpstruct
%{_bindir}/envy*
%{_bindir}/evotiming
%{_bindir}/mmt_*
%{_bindir}/nv01*
%{_bindir}/nv03post
%{_bindir}/nva*
%{_bindir}/nvbios
%{_bindir}/vdpow
%{_datadir}/rnndb

%files hwdocs
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/hwdocs


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.28.git20200810
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.27.git20200810
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.26.git20200810
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.25.git20200810
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.24.git20200810
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.23.git20200810
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 10 2021 Jeff Law <jlaw@tachyum.com> - 0.0-0.22.git20200810
- Re-enable LTO

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.21.git20200810
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Hans de Goede <hdegoede@redhat.com> - 0.0-0.20.git20200810
- Update to a recent git snapshot
- Fix FTBFS (rhbz#1863484)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.19.git20200304
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.18.git20200304
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar  4 2020 Hans de Goede <hdegoede@redhat.com> - 0.0-0.17.git20200304
- Update to a recent git snapshot
- Fix FTBFS (rhbz#1799319)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.16.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.15.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.14.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.13.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0-0.12.git20151030
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.11.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.10.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.9.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.8.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.7.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.6.git20151030
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 04 2015 Than Ngo <than@redhat.com> - 0.0-0.5.git
- add exclusive arch to not build it on s390/powerpc, there's no libseccomp
  for these archs

* Fri Oct 30 2015 Hans de Goede <hdegoede@redhat.com> - 0.0-0.4.git20151030
- New 20151030 git snapshot

* Wed Aug 12 2015 Hans de Goede <hdegoede@redhat.com> - 0.0-0.3.git20150812
- New 20150812 git snapshot
- Add demmio to packaged binaries

* Tue Jun 23 2015 Hans de Goede <hdegoede@redhat.com> - 0.0-0.2.git20150622
- Packaging improvements from package-review (rhbz#1234468)
 - Mark COPYING as %%license
 - Put the hwdocs in their own -hwdocs subpackage
 - Use %%global instead of %%define

* Mon Jun 22 2015 Hans de Goede <hdegoede@redhat.com> - 0.0-0.1.git20150622
- Initial Fedora package
