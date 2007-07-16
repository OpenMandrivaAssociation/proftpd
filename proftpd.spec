%define _localstatedir 	 /var/run

%define mod_gss_version 1.3.0
%define mod_autohost_version 0.1
%define mod_case_version 0.3
%define mod_shaper_version 0.6.3
%define mod_time_version 2.2.1

Summary:	Professional FTP Server
Name:		proftpd
Version:	1.3.1
Release:	%mkrel 0.rc2.5
License:	GPL
Group:		System/Servers
URL:		http://proftpd.org/
Source:	    ftp://ftp.proftpd.org/distrib/source/proftpd/%{name}-%{version}rc2.tar.bz2
Source1:	proftpd.logrotate
Source2: 	proftpd.xinetd
Source3:	proftpd.init
Source4:	proftpd.service
Source5:	basic.conf
Source7:	welcome.msg
Source29:	29_mod_clamav.conf
Source32:	32_mod_shaper.conf
# http://sourceforge.net/projects/gssmod/
Source100:	http://prdownloads.sourceforge.net/gssmod/mod_gss-%{mod_gss_version}.tar.bz2
# from http://www.castaglia.org/proftpd/
Source102:	http://www.castaglia.org/proftpd/modules/proftpd-mod-autohost-%{mod_autohost_version}.tar.bz2
Source103:	http://www.castaglia.org/proftpd/modules/proftpd-mod-case-%{mod_case_version}.tar.bz2
Source104:	http://www.castaglia.org/proftpd/modules/proftpd-mod-shaper-%{mod_shaper_version}.tar.bz2
Source105:	http://www.castaglia.org/proftpd/modules/proftpd-mod-time-%{mod_time_version}.tar.bz2
Source106:	http://www.uglyboxindustries.com/mod_clamav_new.c.bz2
Source107:	http://www.uglyboxindustries.com/mod_clamav_new.html.bz2
Patch0:		proftpd-1.3.0-xferstats_logfile_location.diff
Patch1:		proftpd-1.3.0-biarch-utmp.diff
# (pixel): i kept the /lib/security/*.so instead of *.so in the patch to have a smaller patch
# (pixel): spec-helper will clean it up
Patch2:		proftpd-1.2.9-use-system-auth-instead-of-pam_pwdb.patch
Patch3:		proftpd-1.3.1rc2-FORTIFY_SOURCE_fix.diff
Patch4:		proftpd-1.3.0-installfix.diff
Patch5:		proftpd-1.3.1rc2-mod_facl_declare.diff
Patch6:		proftpd-1.3.1rc2-mod_quotatab_radius_header_fix.diff
Patch7:		proftpd-1.3.0-change_pam_name.diff
Patch23:	mod_gss-1.3.0-shared.diff
Patch24:	proftpd-1.3.0-mod_autohost.diff
Requires:	pam >= 0.59
Requires:	setup >= 2.2.0-21mdk
Requires(post): rpm-helper
Requires(postun): rpm-helper
Requires(preun): rpm-helper
Requires(pre): rpm-helper
BuildRequires:	clamav-devel
BuildRequires:	libacl-devel
BuildRequires:	libattr-devel
BuildRequires:	libkrb-devel
BuildRequires:	MySQL-devel
BuildRequires:	ncurses-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	sasl-plug-gssapi
BuildRequires:	tcp_wrappers-devel
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
Provides:	ftpserver
Conflicts:	wu-ftpd
Conflicts:	ncftpd
Conflicts:	beroftpd
Conflicts:	anonftp
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ProFTPd is an enhanced FTP server with a focus toward simplicity, security, and
ease of configuration.  It features a very Apache-like configuration syntax,
and a highly customizable server infrastructure, including support for multiple
'virtual' FTP servers, anonymous FTP, and permission-based directory visibility.

This version supports both standalone and xinetd operation.

%package	devel
Summary:	Development files for ProFTPD
Group:		Development/C

%description	devel
This package contains the development headers for ProFTPD

%package	mod_clamav
Summary:	Scans newly uploaded files for viruses
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	clamd

%description	mod_clamav
The mod_clamav module is designed to scan files immediately upon upload through
FTP for viruses. If the file is found to be infected, it is immediately removed
from the system, and a message is logged. If the file is found to be free of
viruses, the FTP client is sent an optional message stating the file was
scanned. This module is best employed in scenarios where many users are using a
system that is maintained by another entity. In this scenario, the
administrator of the machine is helping to ensure that no viruses are spread to
other users.

The most current version of mod_clamav can be found at:
http://www.UglyBoxIndustries.com/

%package	mod_ctrls_admin
Summary:	Module implementing admin control handlers
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_ctrls_admin
This module implements administrative control actions for the ftpdctl program.

%package	mod_ifsession
Summary:	Module supporting conditional per-user/group/class configuration contexts
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_ifsession
Module supporting conditional per-user/group/class configuration contexts

%package	mod_ldap
Summary:	LDAP password lookup module for ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_ldap
LDAP password lookup module for ProFTPD

%package	mod_quotatab
Summary:	Module for managing FTP byte/file quotas via centralized tables
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab
Module for managing FTP byte/file quotas via centralized tables

%package	mod_quotatab_file
Summary:	Sub-module for managing quota data via file-based tables
Group:		System/Servers
Requires:	%{name}-mod_quotatab = %{version}-%{release}
Provides:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab_file
Sub-module for managing quota data via file-based tables

%package	mod_quotatab_ldap
Summary:	Sub-module for obtaining quota information from an LDAP directory
Group:		System/Servers
Requires:	%{name}-mod_quotatab = %{version}-%{release}
Provides:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab_ldap
Sub-module for obtaining quota information from an LDAP directory

%package	mod_quotatab_sql
Summary:	Sub-module for managing quota data via SQL-based tables
Group:		System/Servers
Requires:	%{name}-mod_quotatab = %{version}-%{release}
Provides:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab_sql
Sub-module for managing quota data via SQL-based tables

%package	mod_quotatab_radius
Summary:	Sub-module for managing quota data via radius
Group:		System/Servers
Requires:	%{name}-mod_quotatab = %{version}-%{release}
Provides:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab_radius
Sub-module for managing quota data via radius

%package	mod_radius
Summary:	Module for RADIUS authentication and accounting
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_radius
Module for RADIUS authentication and accounting

%package	mod_ratio
Summary:	Support upload/download ratios
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_ratio
Support upload/download ratios

%package	mod_rewrite
Summary:	Module for rewriting FTP commands
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_rewrite
Module for rewriting FTP commands

%package	mod_site_misc
Summary:	Module implementing miscellaneous SITE commands
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_site_misc
Module implementing miscellaneous SITE commands

%package	mod_sql
Summary:	SQL frontend
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-mod_sql_driver = %{version}-%{release}

%description	mod_sql
SQL frontend

%package	mod_sql_mysql
Summary:	Support for connecting to MySQL databases
Group:		System/Servers
Requires:	%{name}-mod_sql = %{version}-%{release}
Provides:	%{name}-mod_sql_driver = %{version}-%{release}

%description	mod_sql_mysql
Support for connecting to MySQL databases

%package	mod_sql_postgres
Summary:	Support for connecting to Postgres databases
Group:		System/Servers
Requires:	%{name}-mod_sql = %{version}-%{release}
Provides:	%{name}-mod_sql_driver = %{version}-%{release}

%description	mod_sql_postgres
Support for connecting to Postgres databases

%package	mod_tls
Summary:	An RFC2228 SSL/TLS module for ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_tls
An RFC2228 SSL/TLS module for ProFTPD

#%package	mod_facl
#Summary:	POSIX ACL checking code (aka POSIX.1e hell)
#Group:		System/Servers
#Requires:	%{name} = %{version}-%{release}
#
#%description	mod_facl
#POSIX ACL checking code (aka POSIX.1e hell)

%package	mod_autohost
Summary:	An autohost module for ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_autohost
For sites that run a large number of <VirtualHost>s for proftpd, it can be
cumbersome to configure them all in the proftpd.conf file. Adding or removing
virtual server configurations require restarting the daemon, as do changes to
one of the server configurations. The daemon also consumes memory for each
server configuration, and the memory footprint for the daemon process can grow
large for large numbers of servers.

The mod_autohost module allows for server configurations to be configured in
individual files, and for those configuration to be used in an "on demand"
fashion. Rather than loading the configurations into memory when the daemon
starts up, the daemon will check the IP address and port being contacted by a
connecting client, check in the filesystem for a mod_autohost configuration
file for that address/port, dynamically parse the configuration, and insert
the configuration into the session's process space. Thus changes to the
configuration are seen whenever a client connects, without requiring a daemon
restart. The memory footprint is reduced because proftpd, via mod_autohost,
only reads and uses the needed configuration.

%package	mod_case
Summary:	Makes ProFTPD case insensitive
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_case
The mod_case module is designed to help ProFTPD be case-insensitive, for those
sites that may need it (e.g. those that are migrating from a Windows
environment or have mounted Windows filesystems).

mod_case works by performing two checks on the filename used in FTP commands.
First, mod_case will scan the directory to see if there is already a file whose
name exactly matches the given filename. If not, mod_case will scan the
directory again, this time looking for case-insensitive matches. 

%package	mod_gss
Summary:	A Kerberos 5 GSS module for ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_gss
A Kerberos 5 GSS module for ProFTPD

%package	mod_load
Summary:	A module that determines average load for ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_load
The code for determining load average on a given system is hairy, to say the
least. Unfortunately, it is necessary to do it this way, as there is no
standard method for extracting such information from the kernel. This module
uses code from GNU's make application, which should function properly. If not,
please contact the author as soon as possible.

%package	mod_shaper
Summary:	A shaping module for ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_shaper
The mod_shaper module is designed to split overall rates, both download and
upload, for the proftpd daemon among all connected FTP clients, shaping each
session to use only a portion of the overall rate. mod_shaper shapes both
transmitted traffic, e.g. bits being downloaded via the RETR command, and
received traffic, e.g. bits being uploaded via the APPE, STOR, and STOU
commands.

%package	mod_time
Summary:	Limits acces based on the time of day and/or the day of the week
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_time
This module is designed to allow for limiting FTP commands based on the time of
day and/or the day of the week. A more detailed explanation of the usage of
this module follows the directive explanations.

%package	mod_wrap
Summary:	Provides tcpwrapper-like access control rules for ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-mod_wrap_driver = %{version}-%{release}
Requires:	tcp_wrappers

%description	mod_wrap
The mod_wrap package allows the proftpd daemon to provide tcpwrapper-like
access control rules while running in standalone mode. It also allows for those
access rules to be stored in various formats, such as files (e.g.
/etc/hosts.allow and /etc/hosts.deny) or in SQL tables.

The most current version of mod_wrap's submodules supports storage of access
table information in various formats:

 o mod_wrap_file for file-based access tables
 o mod_wrap_sql for SQL-based access tables

%package	mod_wrap_file
Summary:	A file-specific driver for the mod_wrap module for ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-mod_wrap_driver = %{version}-%{release}

%description	mod_wrap_file
This submodule provides the file-specific "driver" for storing IP/DNS-based
access control information in files.

%package	mod_wrap_sql
Summary:	A SQL database driver for the mod_wrap module for ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-mod_wrap_driver = %{version}-%{release}

%description	mod_wrap_sql
This submodule provides the SQL database "driver" for storing IP/DNS-based
access control information in SQL tables.

%package	mod_ban
Summary:	Adds dynamic "ban" lists to ProFTPD
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description	mod_ban
The mod_ban module is designed to add dynamic "ban" lists to proftpd. A ban
prevents the banned user, host, or class from logging in to the server; it does
not prevent the banned user, host, or class from connecting to the server.
mod_ban is not a firewall. The module also provides automatic bans that are
triggered based on configurable criteria.

%prep

%setup -q -n %{name}-%{version}rc2 -a100 -a102 -a103 -a104 -a105

%patch0 -p0 -b .logfile_location
%patch1 -p0 -b .biarch-utmp
%patch2 -p1 -b .pam
%patch3 -p0 -b .FORTIFY_SOURCE_fix
%patch4 -p1 -b .installfix
%patch5 -p0 -b .mod_facl_declare
%patch6 -p0 -b .mod_quotatab_radius_header_fix

%patch7 -p0 -b .change_pam_name

%patch23 -p0 -b .mod_gss
%patch24 -p0 -b .mod_autohost

# "install" the clamav module
mkdir -p mod_clamav
bzcat %{SOURCE106} > mod_clamav/mod_clamav.c
bzcat %{SOURCE107} > mod_clamav/mod_clamav.html

# Mandriva config
mkdir -p Mandriva
install -m0644 %{SOURCE1} Mandriva/proftpd.logrotate
install -m0644 %{SOURCE2} Mandriva/proftpd.xinetd
install -m0644 %{SOURCE3} Mandriva/proftpd.init
install -m0644 %{SOURCE4} Mandriva/proftpd.service
install -m0644 %{SOURCE5} Mandriva/basic.conf
install -m0644 %{SOURCE7} Mandriva/welcome.msg
install -m0644 %{SOURCE29} Mandriva/29_mod_clamav.conf
install -m0644 %{SOURCE32} Mandriva/32_mod_shaper.conf

# lib64 fix
perl -pi -e "s|/usr/lib|%{_libdir}|g" Mandriva/basic.conf

# fix includes, instead of a patch
perl -pi -e "s|\<mysql\.h\>|\<mysql\/mysql\.h\>|g" contrib/mod_sql_mysql.c
perl -pi -e "s|\<libpq-fe\.h\>|\<pgsql\/libpq-fe\.h\>|g" contrib/mod_sql_postgres.c

%build

%serverbuild

export CFLAGS="%{optflags} -DLDAP_DEPRECATED -DUSE_LDAP_TLS -DHAVE_OPENSSL"
export LIBS="-L%{_libdir} -lattr"

pushd mod_gss-%{mod_gss_version}

perl -pi -e "s|<gssapi.h>|<gssapi/gssapi.h>|" configure*
perl -pi -e "s|NULL,code|kc,code|" *.in

rm -f configure; autoconf

%configure2_5x --enable-mit

# Workaround a missing dcl in kerberos...
cat >> mod_gss.h <<EOF
#ifndef GSS_C_AF_INET6
#define GSS_C_AF_INET6 24
#endif
EOF

popd

pushd contrib/mod_load
%configure2_5x
popd

pushd contrib/mod_wrap2
%configure2_5x
popd

# put extra modules in place 
for i in `find mod_* -type f -name "*.c"` `find mod_* -type f -name "*.h"`; do
    cp $i contrib/
done

%configure2_5x \
    --libexecdir=%{_libdir}/%{name} \
    --enable-auth-pam \
    --enable-cap \
    --disable-facl \
    --enable-dso \
    --enable-nls \
    --enable-openssl \
    --with-lastlog=/var/log/lastlog \
    --enable-ipv6 \
    --enable-shadow \
    --enable-ctrls \
    --with-shared="mod_ratio:mod_tls:mod_radius:mod_ldap:mod_sql:mod_sql_mysql:mod_sql_postgres:mod_rewrite:mod_ifsession:mod_gss:mod_load:mod_ctrls_admin:mod_quotatab:mod_quotatab_file:mod_quotatab_ldap:mod_quotatab_sql:mod_quotatab_radius:mod_site_misc:mod_wrap2:mod_wrap2_file:mod_wrap2_sql:mod_autohost:mod_case:mod_shaper:mod_time:mod_clamav:mod_ban" \
    --with-modules="mod_readme:mod_auth_pam"

make 

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}%{_sysconfdir}/%{name}.d
install -d %{buildroot}%{_sysconfdir}/pam.d
install -d %{buildroot}%{_sysconfdir}/xinetd.d
install -d %{buildroot}%{_sysconfdir}/avahi/services
install -d %{buildroot}/var/ftp/pub
install -d %{buildroot}/var/log/%{name}
install -d %{buildroot}/var/run/%{name}

%makeinstall \
    rundir=%{buildroot}/var/run/%{name} \
    LIBEXECDIR=%{buildroot}%{_libdir}/%{name} \
    SHARED_MODULE_DIRS=""

%makeinstall -C contrib/mod_wrap2 LIBEXECDIR=%{buildroot}%{_libdir}/%{name}
%makeinstall -C contrib/mod_load LIBEXECDIR=%{buildroot}%{_libdir}/%{name}

install -m0644 contrib/dist/rpm/ftp.pamd %{buildroot}%{_sysconfdir}/pam.d/%{name}
install -m0755 contrib/xferstats.holger-preiss %{buildroot}%{_sbindir}

install -m0644 Mandriva/proftpd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -m0644 Mandriva/proftpd.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/%{name}-xinetd
install -m0755 Mandriva/proftpd.init %{buildroot}%{_initrddir}/%{name}
install -m0644 Mandriva/proftpd.service %{buildroot}%{_sysconfdir}/avahi/services/%{name}.service
install -m0644 Mandriva/basic.conf %{buildroot}%{_sysconfdir}/%{name}.conf
install -m0644 Mandriva/welcome.msg %{buildroot}/var/ftp/pub/welcome.msg

ln -snf %{name} %{buildroot}%{_sbindir}/in.%{name}
ln -snf %{name} %{buildroot}%{_sbindir}/in.ftpd

# config
echo "LoadModule mod_ctrls_admin.c" > %{buildroot}%{_sysconfdir}/%{name}.d/10_mod_ctrls_admin.conf
echo "LoadModule mod_tls.c" > %{buildroot}%{_sysconfdir}/%{name}.d/11_mod_tls.conf
echo "LoadModule mod_sql.c" > %{buildroot}%{_sysconfdir}/%{name}.d/12_mod_sql.conf
echo "LoadModule mod_ldap.c" > %{buildroot}%{_sysconfdir}/%{name}.d/13_mod_ldap.conf
echo "LoadModule mod_sql_mysql.c" > %{buildroot}%{_sysconfdir}/%{name}.d/14_mod_sql_mysql.conf
echo "LoadModule mod_sql_postgres.c" > %{buildroot}%{_sysconfdir}/%{name}.d/15_mod_sql_postgres.conf
echo "LoadModule mod_quotatab.c" > %{buildroot}%{_sysconfdir}/%{name}.d/16_mod_quotatab.conf
echo "LoadModule mod_quotatab_file.c" > %{buildroot}%{_sysconfdir}/%{name}.d/17_mod_quotatab_file.conf
echo "LoadModule mod_quotatab_ldap.c" > %{buildroot}%{_sysconfdir}/%{name}.d/18_mod_quotatab_ldap.conf
echo "LoadModule mod_quotatab_sql.c" > %{buildroot}%{_sysconfdir}/%{name}.d/19_mod_quotatab_sql.conf
echo "LoadModule mod_quotatab_radius.c" > %{buildroot}%{_sysconfdir}/%{name}.d/20_mod_quotatab_radius.conf
echo "LoadModule mod_radius.c" > %{buildroot}%{_sysconfdir}/%{name}.d/20_mod_radius.conf
echo "LoadModule mod_wrap2.c" > %{buildroot}%{_sysconfdir}/%{name}.d/21_mod_wrap2.conf
echo "LoadModule mod_wrap2_file.c" > %{buildroot}%{_sysconfdir}/%{name}.d/22_mod_wrap2_file.conf
echo "LoadModule mod_wrap2_sql.c" > %{buildroot}%{_sysconfdir}/%{name}.d/23_mod_wrap2_sql.conf
echo "LoadModule mod_rewrite.c" > %{buildroot}%{_sysconfdir}/%{name}.d/24_mod_rewrite.conf
echo "LoadModule mod_ratio.c" > %{buildroot}%{_sysconfdir}/%{name}.d/25_mod_ratio.conf
echo "LoadModule mod_gss.c" > %{buildroot}%{_sysconfdir}/%{name}.d/26_mod_gss.conf
echo "LoadModule mod_autohost.c" > %{buildroot}%{_sysconfdir}/%{name}.d/27_mod_autohost.conf
echo "LoadModule mod_case.c" > %{buildroot}%{_sysconfdir}/%{name}.d/28_mod_case.conf
install -m0644 Mandriva/29_mod_clamav.conf %{buildroot}%{_sysconfdir}/%{name}.d/29_mod_clamav.conf
#echo "LoadModule mod_facl.c" > %{buildroot}%{_sysconfdir}/%{name}.d/30_mod_facl.conf
echo "LoadModule mod_load.c" > %{buildroot}%{_sysconfdir}/%{name}.d/31_mod_load.conf
install -m0644 Mandriva/32_mod_shaper.conf %{buildroot}%{_sysconfdir}/%{name}.d/32_mod_shaper.conf
echo "LoadModule mod_site_misc.c" > %{buildroot}%{_sysconfdir}/%{name}.d/33_mod_site_misc.conf
echo "LoadModule mod_time.c" > %{buildroot}%{_sysconfdir}/%{name}.d/34_mod_time.conf
echo "LoadModule mod_ban.c" > %{buildroot}%{_sysconfdir}/%{name}.d/35_mod_ban.conf

cat > %{buildroot}%{_sysconfdir}/%{name}.d/99_mod_ifsession.conf << EOF
# keep this module the last one
LoadModule mod_ifsession.c
EOF

cat > README.urpmi << EOF
Mandriva RPM specific notes

modules support
---------------
proftpd-1.3.0 now loads the modules dynamically, very few modules are compiled
into the proftpd binary. The new configuration file /etc/proftpd.conf uses a
"Include /etc/proftpd.d/*.conf" statement which makes proftpd very similar to
how modules are loaded and the configuration of apache-2.x. Because of this you
may have to manually merge your old configuration into the new
/etc/proftpd.conf file.  This is especially true if you are using LDAP, because
then the mod_ldap.so proftpd module will not be automatically loaded. Here is a
list of the modules that are compiled as DSO's:

 o mod_autohost.so         <- NEW
 o mod_ban.so              <- NEW
 o mod_case.so             <- NEW
 o mod_clamav.so           <- NEW
 o mod_ctrls_admin.so      <- NEW
 o mod_facl.so
 o mod_gss.so
 o mod_ifsession.so
 o mod_ldap.so
 o mod_load.so             <- NEW
 o mod_quotatab.so         <- NEW
 o mod_quotatab_file.so    <- NEW
 o mod_quotatab_ldap.so    <- NEW
 o mod_quotatab_sql.so     <- NEW
 o mod_quotatab_radius.so  <- NEW
 o mod_radius.so
 o mod_ratio.so
 o mod_rewrite.so
 o mod_shaper.so           <- NEW
 o mod_site_misc.so        <- NEW
 o mod_sql.so              <- NEW
 o mod_sql_mysql.so        <- NEW
 o mod_sql_postgres.so     <- NEW
 o mod_time.so             <- NEW
 o mod_tls.so
 o mod_wrap2.so            <- NEW
 o mod_wrap2_file.so       <- NEW
 o mod_wrap2_sql.so        <- NEW

anonymous access configuration
------------------------------
Starting with 1.3.0-3mdv2007.1, there is no proftpd-anonymous package anymore.
As it is just a configuration issue, providing a dedicated package was a bit
overkill. Samples configuration files are available among normal package
documentation. You may have to update your configuration manually.
EOF

# cleanup
rm -f %{buildroot}%{_libdir}/%{name}/*.{a,la}
rm -f contrib/README.mod_sql contrib/README.linux-privs

%post
%_post_service %{name}

# xinetd reset
# Only do it if xinetd is there. -- Geoff
if [ -x /usr/sbin/xinetd ];then
%_post_service xinetd
fi

# ftpusers creation
if [ ! -f %{_sysconfdir}/ftpusers ]; then
    touch %{_sysconfdir}/ftpusers
fi

USERS="root bin daemon adm lp sync shutdown halt mail news uucp operator games nobody"
for i in $USERS ;do
        cat %{_sysconfdir}/ftpusers | grep -q "^$i$" || echo $i >> %{_sysconfdir}/ftpusers
done

%pre
%_pre_useradd ftp /var/ftp /bin/false

%postun
%_postun_userdel ftp

%preun
%_preun_service %{name}
if [ "$1" = 0 ]; then
 if [ -d /var/run/%{name} ]; then
  rm -rf /var/run/%{name}/*
 fi
fi

if [ -x /usr/sbin/xinetd ];then
%_post_service xinetd
fi

%post -n %{name}-mod_autohost
service proftpd condrestart
    
%postun -n %{name}-mod_autohost
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_case
service proftpd condrestart
    
%postun -n %{name}-mod_case
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_clamav
service proftpd condrestart
    
%postun -n %{name}-mod_clamav
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_ctrls_admin
service proftpd condrestart
    
%postun -n %{name}-mod_ctrls_admin
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

#%post -n %{name}-mod_facl
#service proftpd condrestart
#    
#%postun -n %{name}-mod_facl
#if [ "$1" = 0 ]; then
#    service proftpd condrestart
#fi

%post -n %{name}-mod_gss
service proftpd condrestart
    
%postun -n %{name}-mod_gss
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_ifsession
service proftpd condrestart
    
%postun -n %{name}-mod_ifsession
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_ldap
service proftpd condrestart
    
%postun -n %{name}-mod_ldap
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_load
service proftpd condrestart
    
%postun -n %{name}-mod_load
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_quotatab
service proftpd condrestart
    
%postun -n %{name}-mod_quotatab
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_quotatab_file
service proftpd condrestart
    
%postun -n %{name}-mod_quotatab_file
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_quotatab_ldap
service proftpd condrestart
    
%postun -n %{name}-mod_quotatab_ldap
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_quotatab_sql
service proftpd condrestart
    
%postun -n %{name}-mod_quotatab_sql
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_quotatab_radius
service proftpd condrestart
    
%postun -n %{name}-mod_quotatab_radius
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_radius
service proftpd condrestart
    
%postun -n %{name}-mod_radius
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_ratio
service proftpd condrestart
    
%postun -n %{name}-mod_ratio
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_rewrite
service proftpd condrestart
    
%postun -n %{name}-mod_rewrite
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_shaper
service proftpd condrestart
    
%postun -n %{name}-mod_shaper
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_site_misc
service proftpd condrestart
    
%postun -n %{name}-mod_site_misc
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_sql_mysql
service proftpd condrestart
    
%postun -n %{name}-mod_sql_mysql
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_sql
service proftpd condrestart
    
%postun -n %{name}-mod_sql
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_time
service proftpd condrestart
    
%postun -n %{name}-mod_time
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_tls
service proftpd condrestart
    
%postun -n %{name}-mod_tls
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_wrap_file
service proftpd condrestart
    
%postun -n %{name}-mod_wrap_file
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_wrap
service proftpd condrestart
    
%postun -n %{name}-mod_wrap
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_wrap_sql
service proftpd condrestart
    
%postun -n %{name}-mod_wrap_sql
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%post -n %{name}-mod_ban
service proftpd condrestart
    
%postun -n %{name}-mod_ban
if [ "$1" = 0 ]; then
    service proftpd condrestart
fi

%triggerpostun -- proftpd-anonymous
# this package doesn't exist anymore, but its configuration file may
# be used in current proftpd configuration
if [ -e /etc/proftpd-anonymous.conf.rpmsave ]; then
    mv -f /etc/proftpd-anonymous.conf.rpmsave /etc/proftpd-anonymous.conf
    echo "warning: /etc/proftpd-anonymous.conf.rpmsave restored as /etc/proftpd-anonymous.conf"
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* ChangeLog INSTALL NEWS CREDITS COPYING doc/* README.urpmi
%doc sample-configurations/*
%dir %{_sysconfdir}/proftpd.d
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/xinetd.d/%{name}-xinetd
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/avahi/services/%{name}.service
%{_initrddir}/%{name}
%{_sbindir}/%{name}
%{_sbindir}/ftpshut
%{_sbindir}/in.ftpd
%{_sbindir}/in.%{name}
%{_sbindir}/xferstats.holger-preiss
%{_bindir}/ftpcount
%{_bindir}/ftpdctl
%{_bindir}/ftptop
%{_bindir}/ftpwho
%dir %{_libdir}/%{name}
%dir /var/ftp
%dir /var/ftp/pub
%config(noreplace) /var/ftp/pub/welcome.msg
%dir /var/run/%{name}
%dir /var/log/%{name}
%{_mandir}/man*/*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files mod_clamav
%defattr(-,root,root)
%doc mod_clamav/mod_clamav.html
%config(noreplace) %{_sysconfdir}/%{name}.d/29_mod_clamav.conf
%{_libdir}/%{name}/mod_clamav.so

%files mod_ctrls_admin
%defattr(-,root,root)
%doc doc/contrib/mod_ctrls_admin.html
%config(noreplace) %{_sysconfdir}/%{name}.d/10_mod_ctrls_admin.conf
%{_libdir}/%{name}/mod_ctrls_admin.so

%files mod_ifsession
%defattr(-,root,root)
%doc doc/contrib/mod_ifsession.html
%config(noreplace) %{_sysconfdir}/%{name}.d/99_mod_ifsession.conf
%{_libdir}/%{name}/mod_ifsession.so

%files mod_ldap
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}.d/13_mod_ldap.conf
%{_libdir}/%{name}/mod_ldap.so

%files mod_quotatab
%defattr(-,root,root)
%doc doc/contrib/mod_quotatab.html
%config(noreplace) %{_sysconfdir}/%{name}.d/16_mod_quotatab.conf
%{_libdir}/%{name}/mod_quotatab.so

%files mod_quotatab_file
%defattr(-,root,root)
%doc doc/contrib/mod_quotatab_file.html
%config(noreplace) %{_sysconfdir}/%{name}.d/17_mod_quotatab_file.conf
%{_libdir}/%{name}/mod_quotatab_file.so

%files mod_quotatab_ldap
%defattr(-,root,root)
%doc doc/contrib/mod_quotatab_ldap.html
%config(noreplace) %{_sysconfdir}/%{name}.d/18_mod_quotatab_ldap.conf
%{_libdir}/%{name}/mod_quotatab_ldap.so

%files mod_quotatab_sql
%defattr(-,root,root)
%doc doc/contrib/mod_quotatab_sql.html
%config(noreplace) %{_sysconfdir}/%{name}.d/19_mod_quotatab_sql.conf
%{_libdir}/%{name}/mod_quotatab_sql.so

%files mod_quotatab_radius
%defattr(-,root,root)
%doc doc/contrib/mod_quotatab_radius.html
%config(noreplace) %{_sysconfdir}/%{name}.d/20_mod_quotatab_radius.conf
%{_libdir}/%{name}/mod_quotatab_radius.so

%files mod_radius
%defattr(-,root,root)
%doc doc/contrib/mod_radius.html
%config(noreplace) %{_sysconfdir}/%{name}.d/20_mod_radius.conf
%{_libdir}/%{name}/mod_radius.so

%files mod_ratio
%defattr(-,root,root)
%doc contrib/README.ratio
%config(noreplace) %{_sysconfdir}/%{name}.d/25_mod_ratio.conf
%{_libdir}/%{name}/mod_ratio.so

%files mod_rewrite
%defattr(-,root,root)
%doc doc/contrib/mod_rewrite.html
%config(noreplace) %{_sysconfdir}/%{name}.d/24_mod_rewrite.conf
%{_libdir}/%{name}/mod_rewrite.so

%files mod_site_misc
%defattr(-,root,root)
%doc doc/contrib/mod_site_misc.html
%config(noreplace) %{_sysconfdir}/%{name}.d/33_mod_site_misc.conf
%{_libdir}/%{name}/mod_site_misc.so

%files mod_sql
%defattr(-,root,root)
%doc doc/contrib/mod_sql.html
%config(noreplace) %{_sysconfdir}/%{name}.d/12_mod_sql.conf
%{_libdir}/%{name}/mod_sql.so

%files mod_sql_mysql
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}.d/14_mod_sql_mysql.conf
%{_libdir}/%{name}/mod_sql_mysql.so

%files mod_sql_postgres
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}.d/15_mod_sql_postgres.conf
%{_libdir}/%{name}/mod_sql_postgres.so

%files mod_tls
%defattr(-,root,root)
%doc doc/contrib/mod_tls.html
%config(noreplace) %{_sysconfdir}/%{name}.d/11_mod_tls.conf
%{_libdir}/%{name}/mod_tls.so

#%files mod_facl
#%defattr(-,root,root)
#%config(noreplace) %{_sysconfdir}/%{name}.d/30_mod_facl.conf
#%{_libdir}/%{name}/mod_facl.so

%files mod_autohost
%defattr(-,root,root)
%doc mod_autohost/mod_autohost.html
%config(noreplace) %{_sysconfdir}/%{name}.d/27_mod_autohost.conf
%{_libdir}/%{name}/mod_autohost.so

%files mod_case
%defattr(-,root,root)
%doc mod_case/mod_case.html
%config(noreplace) %{_sysconfdir}/%{name}.d/28_mod_case.conf
%{_libdir}/%{name}/mod_case.so

%files mod_gss
%defattr(-,root,root)
%doc mod_gss-*/COPYING mod_gss-*/mod_gss.html mod_gss-*/README.mod_gss mod_gss-*/rfc1509.txt mod_gss-*/rfc2228.txt
%config(noreplace) %{_sysconfdir}/%{name}.d/26_mod_gss.conf
%{_libdir}/%{name}/mod_gss.so

%files mod_load
%defattr(-,root,root)
%doc doc/contrib/mod_load.html
%config(noreplace) %{_sysconfdir}/%{name}.d/31_mod_load.conf
%{_libdir}/%{name}/mod_load.so

%files mod_shaper
%defattr(-,root,root)
%doc mod_shaper/mod_shaper.html
%config(noreplace) %{_sysconfdir}/%{name}.d/32_mod_shaper.conf
%{_libdir}/%{name}/mod_shaper.so

%files mod_time
%defattr(-,root,root)
%doc mod_time/README mod_time/mod_time.html
%config(noreplace) %{_sysconfdir}/%{name}.d/34_mod_time.conf
%{_libdir}/%{name}/mod_time.so

%files mod_wrap
%defattr(-,root,root)
%doc doc/contrib/mod_wrap2.html
%config(noreplace) %{_sysconfdir}/%{name}.d/21_mod_wrap2.conf
%{_libdir}/%{name}/mod_wrap2.so

%files mod_wrap_file
%defattr(-,root,root)
%doc doc/contrib/mod_wrap2_file.html
%config(noreplace) %{_sysconfdir}/%{name}.d/22_mod_wrap2_file.conf
%{_libdir}/%{name}/mod_wrap2_file.so

%files mod_wrap_sql
%defattr(-,root,root)
%doc doc/contrib/mod_wrap2_sql.html
%config(noreplace) %{_sysconfdir}/%{name}.d/23_mod_wrap2_sql.conf
%{_libdir}/%{name}/mod_wrap2_sql.so

%files mod_ban
%defattr(-,root,root)
%doc doc/contrib/mod_ban.html
%config(noreplace) %{_sysconfdir}/%{name}.d/35_mod_ban.conf
%{_libdir}/%{name}/mod_ban.so


