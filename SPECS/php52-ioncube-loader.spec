
%global php php52
%global php_basever 5.2
%global _php5_mod_dir %{_libdir}/php/modules
%global basever 4.2

Name:       %{php}-ioncube-loader
Summary:    IonCube Loader provides PHP Modules to read IonCube Encoded Files
Version:    4.2.2
Release:    1.ius%{?dist}
Vendor:     IUS Community Project
License:    Free Software
URL:        http://www.ioncube.com
Group:      Development/Languages
Source0:    http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_x86.tar.gz
Source1:    http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz 
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX) 
Requires:   %{php} >= %{php_basever}
Conflicts:  php-ioncube-loader < %{basever}
Provides:   php-ioncube-loader = %{version}-%{release}


%description
IonCube Loader provides PHP Modules to read IonCube Encoded Files

%prep 
%setup -T -n %{name}-%{version} -c %{name}-%{version}
if [ "%{_arch}" = "i386" ]; then
    echo "Arch is i386"
    tar -zxf %SOURCE0
    mv ioncube/* .
elif [ "%{_arch}" = "x86_64" ]; then
    echo "Arch is x86_64"
    tar -zxf %SOURCE1
    mv ioncube/* .
fi


%build
# Nothing to do here

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_php5_mod_dir} \
             %{buildroot}/etc/php.d

# Install the shared objects
install -m 755 ioncube_loader_lin_%{php_basever}.so %{buildroot}%{_php5_mod_dir}
install -m 755 ioncube_loader_lin_%{php_basever}_ts.so %{buildroot}%{_php5_mod_dir}

%{__cat} >> %{buildroot}/etc/php.d/ioncube-loader.ini <<EOF

; Configured for PHP ${php_basever}
zend_extension=%{_php5_mod_dir}/ioncube_loader_lin_%{php_basever}.so

; For threaded Apache/PHP Implementations comment out the above
; and un-comment the following:
;
; zend_extension=%{_php5_mod_dir}/ioncube_loader_lin_%{php_basever}_ts.so
;
EOF



%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}


%files
%defattr(-,root,root)
#%%doc README.txt LICENSE.txt 
%config %attr(644,root,root) /etc/php.d/ioncube-loader.ini
%{_php5_mod_dir}/ioncube_loader_lin_%{php_basever}.so
%{_php5_mod_dir}/ioncube_loader_lin_%{php_basever}_ts.so


%changelog
* Wed Jun 27 2012 D. H. Offutt <dustin.offutt@rackspace.com> - 4.2.2-1.ius
- Latest sources

* Wed May 23 2012 D. H. Offutt <dustin.offutt@rackspace.com> - 4.2.1-1.ius
- Latest sources

* Wed May 16 2012 D. H. Offutt <dustin.offutt@rackspace.com> - 4.2.0-1.ius
- Latest sources
- {README,LICENSE}.txt not included in tarball this release. Commented out.

* Tue Mar 13 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.14-1.ius
- Latest sources

* Mon Jan 23 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.12-2.ius
- Fixing Provides and Conflicts, reported in
  https://bugs.launchpad.net/ius/+bug/920178

* Tue Jan 03 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.12-1.ius
- Latest sources from upstream

* Mon Dec 12 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.11-1.ius
- Latest sources from upstream

* Tue Jul 19 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.10-1.ius
- Latest sources from upstream

* Thu Jun 07 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.9-1.ius
- Latest sources from upstream

* Thu Apr 21 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.8-1.ius
- Latest sources from upstream

* Mon Mar 21 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.7-1.ius
- Latest sources from upstream

* Mon Jun 28 2010 BJ Dierkes <wdierkes@rackspace.com> - 3.3.17-2.ius
- Porting to php52 package

* Thu May 20 2010 BJ Dierkes <wdierkes@rackspace.com> - 3.3.17-1.ius
- Porting to IUS for the php53 package
- Removed files for other versions of PHP
 
* Thu Feb 05 2009 BJ Dierkes <wdierkes@rackspace.com> 3.1.32-2.rs
- Cleaned up trigger scripts a bit
- Changed Vendor tag to Rackspace US, Inc.
- Moved configuration file to /etc/php.d/01a-ioncube-loader.ini
- Added noreplace configuration file to /etc/php.d/01b-ioncube-loader.ini
- Requires: php-devel

* Sun May 18 2008 BJ Dierkes <wdierkes@rackspace.com> 3.1.32-1.rs
- Latest sources.
- Added a regex check for ioncube loader config in php.ini before
  setting up the ioncube-loader.ini (triggerin).  Resolves Rackspace 
  Bugs [#493] and [#393].

* Fri Jun 01 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.31-1.rs
- Latest sources

* Thu May 02 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.30-1.rs
- Latest sources

* Wed Apr 18 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.29-1.rs
- Latest sources
- Replace post script with triggerin script to always overwrite /etc/php.d/ioncube-loader.ini when php is upgraded
  to keep the right configuration.

* Fri Feb 23 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.28-1.1.rs
- Set 'replace' on config file
- Set PreReq php (PHP must install/upgrade first, as post script check 
  PHP version

* Wed Feb 21 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.28-1.rs
- Inital spec build
- Rewritten from partial spec submitted by Samuel Stringham
