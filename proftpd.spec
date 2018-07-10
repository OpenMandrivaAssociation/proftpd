%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define _localstatedir /run/%{name}
%define mod_gss_version 1.3.3
%define mod_autohost_version 0.4
%define mod_case_version 0.7
%define mod_vroot_version 0.9.2

Summary:	Professional FTP Server
Name:		proftpd
Version:	1.3.5e
Release:	2
License:	GPLv2
Group:		System/Servers
Url:		http://proftpd.org/
Source0:	ftp://ftp.proftpd.org/distrib/source/%{name}-%{version}.tar.gz
Source5:	basic.conf
Source7:	welcome.msg
Source32:	32_mod_shaper.conf
# http://sourceforge.net/projects/gssmod/
Source100:	http://prdownloads.sourceforge.net/gssmod/mod_gss-%{mod_gss_version}.tar.gz
# from http://www.castaglia.org/proftpd/
Source102:	http://www.castaglia.org/proftpd/modules/proftpd-mod-autohost-%{mod_autohost_version}.tar.gz
Source103:	http://www.castaglia.org/proftpd/modules/proftpd-mod-case-%{mod_case_version}.tar.gz
Source108:	http://www.castaglia.org/proftpd/modules/proftpd-mod-vroot-%{mod_vroot_version}.tar.gz
Source200:	anonymous.conf
Patch0:		proftpd-1.3.0-xferstats_logfile_location.diff
# (pixel): i kept the /lib/security/*.so instead of *.so in the patch to have a smaller patch
# (pixel): spec-helper will clean it up
Patch2:		proftpd-use-system-auth-instead-of-pam_unix.diff
Patch4:		proftpd-1.3.0-installfix.diff
Patch7:		proftpd-1.3.0-change_pam_name.diff
Patch40:	mod_gss-1.3.0-format_not_a_string_literal_and_no_format_arguments.diff
Patch42:	proftpd-1.3.3c-no_-ldes425.diff
Requires:	pam >= 0.59
Requires:	setup >= 2.2.0-21mdk
Requires(post,postun,preun,pre): rpm-helper
BuildRequires:	libtool
BuildRequires:	sasl-plug-gssapi
BuildRequires:	cap-devel
BuildRequires:	gettext-devel
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	krb5-devel
BuildRequires:	libtool-devel
BuildRequires:	memcached-devel >= 0.41
BuildRequires:	mysql-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	tcp_wrappers-devel
BuildRequires:	pkgconfig(libmemcached)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)
Provides:	ftpserver
Conflicts:	wu-ftpd
Conflicts:	pure-ftpd
Conflicts:	ncftpd
Conflicts:	anonftp
# for the test suite
# disabled for now but kept here for reference
#BuildRequires:	check-devel perl-Test-Unit perl-Error

%description
ProFTPd is an enhanced FTP server with a focus toward simplicity, security, and
ease of configuration.  It features a very Apache-like configuration syntax,
and a highly customizable server infrastructure, including support for multiple
'virtual' FTP servers, anonymous FTP, and permission-based directory
visibility.

This version supports standalone operation.

%package	devel
Summary:	Development files for ProFTPD
Group:		Development/C

%description	devel
This package contains the development headers for ProFTPD

%package	mod_ctrls_admin
Summary:	Module implementing admin control handlers
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_ctrls_admin
This module implements administrative control actions for the ftpdctl program.

%package	mod_ifsession
Summary:	Module supporting conditional per-user/group/class configuration contexts
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_ifsession
Module supporting conditional per-user/group/class configuration contexts

%package	mod_ldap
Summary:	LDAP password lookup module for ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_ldap
LDAP password lookup module for ProFTPD

%package	mod_quotatab
Summary:	Module for managing FTP byte/file quotas via centralized tables
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab
Module for managing FTP byte/file quotas via centralized tables

%package	mod_quotatab_file
Summary:	Sub-module for managing quota data via file-based tables
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_quotatab = %{version}-%{release}
Provides:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab_file
Sub-module for managing quota data via file-based tables

%package	mod_quotatab_ldap
Summary:	Sub-module for obtaining quota information from an LDAP directory
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_quotatab = %{version}-%{release}
Provides:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab_ldap
Sub-module for obtaining quota information from an LDAP directory

%package	mod_quotatab_sql
Summary:	Sub-module for managing quota data via SQL-based tables
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_quotatab = %{version}-%{release}
Provides:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab_sql
Sub-module for managing quota data via SQL-based tables

%package	mod_quotatab_radius
Summary:	Sub-module for managing quota data via radius
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_quotatab = %{version}-%{release}
Provides:	%{name}-mod_quotatab_driver = %{version}-%{release}

%description	mod_quotatab_radius
Sub-module for managing quota data via radius

%package	mod_radius
Summary:	Module for RADIUS authentication and accounting
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_radius
Module for RADIUS authentication and accounting

%package	mod_ratio
Summary:	Support upload/download ratios
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_ratio
Support upload/download ratios

%package	mod_rewrite
Summary:	Module for rewriting FTP commands
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_rewrite
Module for rewriting FTP commands

%package	mod_site_misc
Summary:	Module implementing miscellaneous SITE commands
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_site_misc
Module implementing miscellaneous SITE commands

%package	mod_sql
Summary:	SQL frontend
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_sql_driver = %{version}-%{release}

%description	mod_sql
SQL frontend

%package	mod_sql_mysql
Summary:	Support for connecting to MySQL databases
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_sql = %{version}-%{release}
Provides:	%{name}-mod_sql_driver = %{version}-%{release}

%description	mod_sql_mysql
Support for connecting to MySQL databases

%package	mod_sql_postgres
Summary:	Support for connecting to Postgres databases
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_sql = %{version}-%{release}
Provides:	%{name}-mod_sql_driver = %{version}-%{release}

%description	mod_sql_postgres
Support for connecting to Postgres databases

%package	mod_sql_sqlite
Summary:	Support for connecting to SQLite3 databases
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_sql = %{version}-%{release}
Provides:	%{name}-mod_sql_driver = %{version}-%{release}

%description	mod_sql_sqlite
Support for connecting to SQLite3 databases

%package	mod_sql_passwd
Summary:	Various SQL password handlers
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_sql = %{version}-%{release}
Provides:	%{name}-mod_sql_driver = %{version}-%{release}

%description	mod_sql_passwd
Various SQL password handlers

%package	mod_tls
Summary:	An RFC2228 SSL/TLS module for ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_tls
An RFC2228 SSL/TLS module for ProFTPD

%package	mod_tls_shmcache
Summary:	A module which provides a shared SSL session cache using SysV shared memory
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_tls = %{version}-%{release}

%description	mod_tls_shmcache
This submodule provides a SysV shared memory-based implementation of an
external SSL session cache for use by the mod_tls module's TLSSessionCache
directive.

%package	mod_tls_memcache
Summary:	A module which provides a shared SSL session cache using memcached servers
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_tls = %{version}-%{release}
Suggests:	memcached

%description	mod_tls_memcache
This submodule a memcached-based implementation of an external SSL session
cache for use by the mod_tls module's TLSSessionCache directive.

#%package	mod_facl
#Summary:	POSIX ACL checking code (aka POSIX.1e hell)
#Group:		System/Servers
#Requires:	%{name} >= %{version}-%{release}
#
#%description	mod_facl
#POSIX ACL checking code (aka POSIX.1e hell)

%package	mod_autohost
Summary:	An autohost module for ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

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
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

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
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_gss
A Kerberos 5 GSS module for ProFTPD

%package	mod_load
Summary:	A module that determines average load for ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_load
The code for determining load average on a given system is hairy, to say the
least. Unfortunately, it is necessary to do it this way, as there is no
standard method for extracting such information from the kernel. This module
uses code from GNU's make application, which should function properly. If not,
please contact the author as soon as possible.

%package	mod_shaper
Summary:	A shaping module for ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_shaper
The mod_shaper module is designed to split overall rates, both download and
upload, for the proftpd daemon among all connected FTP clients, shaping each
session to use only a portion of the overall rate. mod_shaper shapes both
transmitted traffic, e.g. bits being downloaded via the RETR command, and
received traffic, e.g. bits being uploaded via the APPE, STOR, and STOU
commands.

%package	mod_wrap
Summary:	Provides tcpwrapper-like access control rules for ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
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
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Provides:	%{name}-mod_wrap_driver = %{version}-%{release}

%description	mod_wrap_file
This submodule provides the file-specific "driver" for storing IP/DNS-based
access control information in files.

%package	mod_wrap_sql
Summary:	A SQL database driver for the mod_wrap module for ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Provides:	%{name}-mod_wrap_driver = %{version}-%{release}

%description	mod_wrap_sql
This submodule provides the SQL database "driver" for storing IP/DNS-based
access control information in SQL tables.

%package	mod_ban
Summary:	Adds dynamic "ban" lists to ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_ban
The mod_ban module is designed to add dynamic "ban" lists to proftpd. A ban
prevents the banned user, host, or class from logging in to the server; it does
not prevent the banned user, host, or class from connecting to the server.
mod_ban is not a firewall. The module also provides automatic bans that are
triggered based on configurable criteria.

%package	mod_vroot
Summary:	Adds virtual chroot capability to ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_vroot
The purpose of this module to is to implement a virtual chroot capability that
does not require root privileges. The mod_vroot module provides this capability
by using ProFTPD's FS API, available as of 1.2.8rc1.

%package	mod_sftp
Summary:	Implements the SSH2 protocol and its SFTP subsystem for ProFTPD
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_sftp
The mod_sftp module implements the SSH2 protocol and its SFTP subsystem, for
secure file transfer over an SSH2 connection. The mod_sftp module supports:

 o Public key authentication
 o Password authentication (e.g. user authentication via mod_sql, mod_ldap,
   mod_auth_file, mod_auth_unix, mod_auth_pam)
 o SCP support
 o Quotas (via the mod_quotatab module)
 o FIPS support (see Usage section)
 o Throttled transfers (via TransferRate, and/or the mod_shaper module)
 o Blacklisted public keys
 o Configurable traffic analysis protection
 o Passphrase-protected host keys 

%package	mod_sftp_pam
Summary:	A module which provides an SSH2 "keyboard-interactive" driver using PAM
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_sftp >= %{version}-%{release}

%description	mod_sftp_pam
The mod_sftp_pam module provides support for the "SSH Keyboard-Interactive
Authentication" RFC (RFC4256).

%package	mod_sftp_sql
Summary:	SQL backend module for retrieving authorized keys
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}
Requires:	%{name}-mod_sftp >= %{version}-%{release}
Requires:	%{name}-mod_sql >= %{version}-%{release}

%description	mod_sftp_sql
The mod_sftp module for ProFTPD can support different storage formats for its
user- and host-based authorized keys. By default, the mod_sftp module supports
storing authorized keys in flats. This mod_sftp_sql module allows for
authorized SSH keys to be stored in SQL tables.

%package	mod_memcache
Summary:	A module for managing memcache data
Group:		System/Servers
Requires(post,preun):	%{name} >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description	mod_memcache
The mod_memcache module enables ProFTPD support for caching data in memcached
servers, using the libmemcached client library.

%prep
%setup -q -a100 -a102 -a103 -a108

%patch0 -p0 -b .logfile_location
%patch2 -p0 -b .pam
%patch4 -p1 -b .installfix
%patch7 -p0 -b .change_pam_name

%patch40 -p0 -b .format_not_a_string_literal_and_no_format_arguments
%patch42 -p1 -b .no_-ldes425

# Mandriva config
mkdir -p OpenMandriva
install -m0644 %{SOURCE5} OpenMandriva/basic.conf
install -m0644 %{SOURCE7} OpenMandriva/welcome.msg
install -m0644 %{SOURCE32} OpenMandriva/32_mod_shaper.conf

# lib64 fix
perl -pi -e "s|/usr/lib|%{_libdir}|g" OpenMandriva/basic.conf

# fix includes, instead of a patch
perl -pi -e "s|\<mysql\.h\>|\<mysql\/mysql\.h\>|g" contrib/mod_sql_mysql.c
#perl -pi -e "s|\<libpq-fe\.h\>|\<pgsql\/libpq-fe\.h\>|g" contrib/mod_sql_postgres.c

# Tweak logrotate script for systemd compatibility (#802178)
sed -i -e '/killall/s/test.*/systemctl reload proftpd.service/' \
	contrib/dist/rpm/proftpd.logrotate

%build
%serverbuild
export CFLAGS="$CFLAGS -DLDAP_DEPRECATED -DUSE_LDAP_TLS -DHAVE_OPENSSL"
export LIBS="-L%{_libdir} -lattr"

pushd mod_gss-%{mod_gss_version}
perl -pi -e "s|<gssapi.h>|<gssapi/gssapi.h>|" configure*
perl -pi -e "s|NULL,code|kc,code|" *.in
#libtoolize --copy --force --ltdl
#rm -rf lib/libltdl; mv libltdl lib/
#rm -f configure; autoconf
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

#head -n 190 aclocal.m4 > acinclude.m4
#rm -f aclocal.m4
#libtoolize --copy --force --ltdl
#rm -rf lib/libltdl; mv libltdl lib/
#aclocal; autoconf

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
	--with-shared="mod_ratio:mod_tls:mod_tls_shmcache:mod_radius:mod_ldap:mod_sql:mod_sql_mysql:mod_sql_postgres:mod_sql_sqlite:mod_sql_passwd:mod_rewrite:mod_gss:mod_load:mod_ctrls_admin:mod_quotatab:mod_quotatab_file:mod_quotatab_ldap:mod_quotatab_sql:mod_quotatab_radius:mod_site_misc:mod_wrap2:mod_wrap2_file:mod_wrap2_sql:mod_autohost:mod_case:mod_shaper:mod_ban:mod_vroot:mod_sftp:mod_sftp_pam:mod_sftp_sql:mod_ifsession:mod_memcache:mod_tls_memcache" \
	--with-modules="mod_readme:mod_auth_pam" \
	--disable-strip \
	--enable-pcre

#    --enable-tests

# libcap hack
perl -pi -e "s|/lib/libcap|/blabla|g" Make.rules
echo "#define HAVE_LINUX_CAPABILITY_H 1" >> config.h

%make

%check
#make check

%install
install -D -p -m 644 contrib/dist/rpm/proftpd.service \
					%{buildroot}%{_unitdir}/proftpd.service
install -D -p -m 644 contrib/dist/rpm/proftpd.logrotate \
					%{buildroot}%{_sysconfdir}/logrotate.d/proftpd
install -d -m 755 %{buildroot}%{_prefix}/lib/tmpfiles.d
install -p -m 644 contrib/dist/rpm/proftpd-tmpfs.conf \
					%{buildroot}%{_prefix}/lib/tmpfiles.d/proftpd.conf
install -d %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_sysconfdir}/%{name}.d
install -d %{buildroot}%{_sysconfdir}/pam.d
install -d %{buildroot}/var/ftp/pub
install -d %{buildroot}/var/log/%{name}

%makeinstall \
	rundir=/run/%{name} \
	LIBEXECDIR=%{buildroot}%{_libdir}/%{name} \
	SHARED_MODULE_DIRS="" \
	pkgconfigdir=%{buildroot}%{_libdir}/pkgconfig

# fix borked pkgconfig file
perl -pi -e "s|^prefix.*|prefix=%{_prefix}|g" %{buildroot}%{_libdir}/pkgconfig/*.pc
perl -pi -e "s|/lib/|/%{_lib}/|g" %{buildroot}%{_libdir}/pkgconfig/*.pc

%makeinstall -C contrib/mod_wrap2 LIBEXECDIR=%{buildroot}%{_libdir}/%{name}
%makeinstall -C contrib/mod_load LIBEXECDIR=%{buildroot}%{_libdir}/%{name}
%makeinstall -C contrib/mod_sftp LIBEXECDIR=%{buildroot}%{_libdir}/%{name}

install -m0644 contrib/dist/rpm/ftp.pamd %{buildroot}%{_sysconfdir}/pam.d/%{name}
install -m0755 contrib/xferstats.holger-preiss %{buildroot}%{_sbindir}

install -m0644 OpenMandriva/basic.conf %{buildroot}%{_sysconfdir}/%{name}.conf
install -m0644 OpenMandriva/welcome.msg %{buildroot}/var/ftp/pub/welcome.msg

install -m0644 %{SOURCE200} %{buildroot}%{_sysconfdir}/proftpd-anonymous.conf

ln -snf %{name} %{buildroot}%{_sbindir}/in.%{name}
ln -snf %{name} %{buildroot}%{_sbindir}/in.ftpd

# config
echo "LoadModule mod_ctrls_admin.c" > %{buildroot}%{_sysconfdir}/%{name}.d/10_mod_ctrls_admin.conf
echo "LoadModule mod_tls.c" > %{buildroot}%{_sysconfdir}/%{name}.d/11_mod_tls.conf
echo "LoadModule mod_tls_shmcache.c" > %{buildroot}%{_sysconfdir}/%{name}.d/12_mod_tls_shmcache.conf
echo "LoadModule mod_sql.c" > %{buildroot}%{_sysconfdir}/%{name}.d/12_mod_sql.conf
echo "LoadModule mod_ldap.c" > %{buildroot}%{_sysconfdir}/%{name}.d/13_mod_ldap.conf
echo "LoadModule mod_sql_mysql.c" > %{buildroot}%{_sysconfdir}/%{name}.d/14_mod_sql_mysql.conf
echo "LoadModule mod_sql_postgres.c" > %{buildroot}%{_sysconfdir}/%{name}.d/15_mod_sql_postgres.conf
echo "LoadModule mod_sql_sqlite.c" > %{buildroot}%{_sysconfdir}/%{name}.d/16_mod_sql_sqlite.conf
echo "LoadModule mod_sql_passwd.c" > %{buildroot}%{_sysconfdir}/%{name}.d/17_mod_sql_passwd.conf
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
#echo "LoadModule mod_facl.c" > %{buildroot}%{_sysconfdir}/%{name}.d/30_mod_facl.conf
echo "LoadModule mod_load.c" > %{buildroot}%{_sysconfdir}/%{name}.d/31_mod_load.conf
install -m0644 OpenMandriva/32_mod_shaper.conf %{buildroot}%{_sysconfdir}/%{name}.d/32_mod_shaper.conf
echo "LoadModule mod_site_misc.c" > %{buildroot}%{_sysconfdir}/%{name}.d/33_mod_site_misc.conf
echo "LoadModule mod_ban.c" > %{buildroot}%{_sysconfdir}/%{name}.d/35_mod_ban.conf
echo "LoadModule mod_vroot.c" > %{buildroot}%{_sysconfdir}/%{name}.d/36_mod_vroot.conf
echo "LoadModule mod_sftp.c" > %{buildroot}%{_sysconfdir}/%{name}.d/37_mod_sftp.conf
echo "LoadModule mod_sftp_pam.c" > %{buildroot}%{_sysconfdir}/%{name}.d/38_mod_sftp_pam.conf
echo "LoadModule mod_sftp_sql.c" > %{buildroot}%{_sysconfdir}/%{name}.d/39_mod_sftp_sql.conf
echo "LoadModule mod_memcache.c" > %{buildroot}%{_sysconfdir}/%{name}.d/40_mod_memcache.conf
echo "LoadModule mod_tls_memcache.c" > %{buildroot}%{_sysconfdir}/%{name}.d/41_mod_tls_memcache.conf

cat > %{buildroot}%{_sysconfdir}/%{name}.d/99_mod_ifsession.conf << EOF
# keep this module the last one
LoadModule mod_ifsession.c
EOF

cat > README.urpmi << EOF
OpenMandriva RPM specific notes

modules support
---------------
proftpd-1.3.0 now loads the modules dynamically, very few modules are compiled
into the proftpd binary. The new configuration file /etc/proftpd.conf uses a
"Include /etc/proftpd.d/*.conf" statement which makes proftpd very similar to
how modules are loaded and the configuration of apache-2.x. Because of this you
may have to manually merge your old configuration into the new
/etc/proftpd.conf file.  This is especially true if you are using LDAP, because
then the mod_ldap.so proftpd module will not be automatically loaded. Here is a
list of the modules that are compiled as DSOs:

 o mod_autohost.so         <- NEW
 o mod_ban.so              <- NEW
 o mod_case.so             <- NEW
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
 o mod_sql_sqlite.so       <- NEW
 o mod_sql_passwd.so       <- NEW
 o mod_tls.so
 o mod_tls_shmcache.so     <- NEW
 o mod_wrap2.so            <- NEW
 o mod_wrap2_file.so       <- NEW
 o mod_wrap2_sql.so        <- NEW
 o mod_vroot.so            <- NEW
 o mod_sftp                <- NEW
 o mod_sftp_pam            <- NEW
 o mod_sftp_sql            <- NEW
 o mod_memcache            <- NEW
 o mod_tls_memcache        <- NEW

anonymous access configuration
------------------------------
Starting with 1.3.0-3mdv2007.1, there is no proftpd-anonymous package anymore.
As it is just a configuration issue, providing a dedicated package was a bit
overkill. Samples configuration files are available among normal package
documentation. You may have to update your configuration manually.
EOF


%find_lang %{name}

# cleanup
rm -f %{buildroot}%{_libdir}/%{name}/*.{a,la}
rm -f contrib/README.mod_sql contrib/README.linux-privs

%post
%_post_service %{name}

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
 if [ -d /run/%{name} ]; then
  rm -rf /run/%{name}/*
 fi
fi

%post mod_autohost
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_autohost
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_case
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_case
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_ctrls_admin
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_ctrls_admin
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

#%post mod_facl
#/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
#    
#%preun mod_facl
#if [ "$1" = 0 ]; then
#    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
#fi

%post mod_gss
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_gss
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_ifsession
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_ifsession
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_ldap
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_ldap
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_load
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_load
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_quotatab
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_quotatab
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_quotatab_file
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_quotatab_file
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_quotatab_ldap
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_quotatab_ldap
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_quotatab_sql
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_quotatab_sql
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_quotatab_radius
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_quotatab_radius
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_radius
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_radius
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_ratio
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_ratio
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_rewrite
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_rewrite
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_shaper
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_shaper
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_site_misc
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_site_misc
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_sql
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_sql
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_sql_mysql
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_sql_mysql
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_sql_postgres
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_sql_postgres
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_sql_sqlite
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_sql_sqlite
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_sql_passwd
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_sql_passwd
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_tls
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_tls
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_tls_shmcache
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_tls_shmcache
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_tls_memcache
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_tls_memcache
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_wrap_file
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_wrap_file
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_wrap
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_wrap
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_wrap_sql
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_wrap_sql
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_ban
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_ban
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_vroot
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_vroot
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_sftp
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_sftp
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_sftp_pam
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_sftp_pam
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_sftp_sql
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_sftp_sql
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%post mod_memcache
/bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :

%preun mod_memcache
if [ "$1" = 0 ]; then
    /bin/systemctl try-restart proftpd.service > /dev/null 2>/dev/null || :
fi

%files -f %{name}.lang
%doc README* INSTALL NEWS CREDITS COPYING doc/* README.urpmi
%doc sample-configurations/*
%dir %{_sysconfdir}/proftpd.d
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}-anonymous.conf
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/proftpd
%{_unitdir}/proftpd.service
%{_prefix}/lib/tmpfiles.d/proftpd.conf
%{_sbindir}/%{name}
%{_sbindir}/ftpscrub
%{_sbindir}/ftpshut
%{_sbindir}/in.ftpd
%{_sbindir}/in.%{name}
%{_sbindir}/xferstats.holger-preiss
%{_bindir}/ftpasswd
%{_bindir}/ftpcount
%{_bindir}/ftpdctl
%{_bindir}/ftpmail
%{_bindir}/ftpquota
%{_bindir}/ftptop
%{_bindir}/ftpwho
%{_bindir}/prxs
%dir %{_libdir}/%{name}
%dir /var/ftp
%dir /var/ftp/pub
%config(noreplace) /var/ftp/pub/welcome.msg
%dir /var/log/%{name}
%{_mandir}/man*/*

%files devel
%doc ChangeLog
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc

%files mod_ctrls_admin
%doc doc/contrib/mod_ctrls_admin.html
%config(noreplace) %{_sysconfdir}/%{name}.d/10_mod_ctrls_admin.conf
%{_libdir}/%{name}/mod_ctrls_admin.so

%files mod_ifsession
%doc doc/contrib/mod_ifsession.html
%config(noreplace) %{_sysconfdir}/%{name}.d/99_mod_ifsession.conf
%{_libdir}/%{name}/mod_ifsession.so

%files mod_ldap
%config(noreplace) %{_sysconfdir}/%{name}.d/13_mod_ldap.conf
%{_libdir}/%{name}/mod_ldap.so

%files mod_quotatab
%doc doc/contrib/mod_quotatab.html
%config(noreplace) %{_sysconfdir}/%{name}.d/16_mod_quotatab.conf
%{_libdir}/%{name}/mod_quotatab.so

%files mod_quotatab_file
%doc doc/contrib/mod_quotatab_file.html
%config(noreplace) %{_sysconfdir}/%{name}.d/17_mod_quotatab_file.conf
%{_libdir}/%{name}/mod_quotatab_file.so

%files mod_quotatab_ldap
%doc doc/contrib/mod_quotatab_ldap.html
%config(noreplace) %{_sysconfdir}/%{name}.d/18_mod_quotatab_ldap.conf
%{_libdir}/%{name}/mod_quotatab_ldap.so

%files mod_quotatab_sql
%doc doc/contrib/mod_quotatab_sql.html
%config(noreplace) %{_sysconfdir}/%{name}.d/19_mod_quotatab_sql.conf
%{_libdir}/%{name}/mod_quotatab_sql.so

%files mod_quotatab_radius
%doc doc/contrib/mod_quotatab_radius.html
%config(noreplace) %{_sysconfdir}/%{name}.d/20_mod_quotatab_radius.conf
%{_libdir}/%{name}/mod_quotatab_radius.so

%files mod_radius
%doc doc/contrib/mod_radius.html
%config(noreplace) %{_sysconfdir}/%{name}.d/20_mod_radius.conf
%{_libdir}/%{name}/mod_radius.so

%files mod_ratio
%doc contrib/README.ratio
%config(noreplace) %{_sysconfdir}/%{name}.d/25_mod_ratio.conf
%{_libdir}/%{name}/mod_ratio.so

%files mod_rewrite
%doc doc/contrib/mod_rewrite.html
%config(noreplace) %{_sysconfdir}/%{name}.d/24_mod_rewrite.conf
%{_libdir}/%{name}/mod_rewrite.so

%files mod_site_misc
%doc doc/contrib/mod_site_misc.html
%config(noreplace) %{_sysconfdir}/%{name}.d/33_mod_site_misc.conf
%{_libdir}/%{name}/mod_site_misc.so

%files mod_sql
%doc doc/contrib/mod_sql.html
%config(noreplace) %{_sysconfdir}/%{name}.d/12_mod_sql.conf
%{_libdir}/%{name}/mod_sql.so

%files mod_sql_mysql
%config(noreplace) %{_sysconfdir}/%{name}.d/14_mod_sql_mysql.conf
%{_libdir}/%{name}/mod_sql_mysql.so

%files mod_sql_postgres
%config(noreplace) %{_sysconfdir}/%{name}.d/15_mod_sql_postgres.conf
%{_libdir}/%{name}/mod_sql_postgres.so

%files mod_sql_sqlite
%config(noreplace) %{_sysconfdir}/%{name}.d/16_mod_sql_sqlite.conf
%{_libdir}/%{name}/mod_sql_sqlite.so

%files mod_sql_passwd
%config(noreplace) %{_sysconfdir}/%{name}.d/17_mod_sql_passwd.conf
%{_libdir}/%{name}/mod_sql_passwd.so

%files mod_tls
%doc doc/contrib/mod_tls.html
%config(noreplace) %{_sysconfdir}/%{name}.d/11_mod_tls.conf
%{_libdir}/%{name}/mod_tls.so

%files mod_tls_shmcache
%doc doc/contrib/mod_tls_shmcache.html
%config(noreplace) %{_sysconfdir}/%{name}.d/12_mod_tls_shmcache.conf
%{_libdir}/%{name}/mod_tls_shmcache.so

%files mod_tls_memcache
%doc doc/contrib/mod_tls_memcache.html
%config(noreplace) %{_sysconfdir}/%{name}.d/41_mod_tls_memcache.conf
%{_libdir}/%{name}/mod_tls_memcache.so

#%files mod_facl
#%config(noreplace) %{_sysconfdir}/%{name}.d/30_mod_facl.conf
#%{_libdir}/%{name}/mod_facl.so

%files mod_autohost
%doc mod_autohost/mod_autohost.html
%config(noreplace) %{_sysconfdir}/%{name}.d/27_mod_autohost.conf
%{_libdir}/%{name}/mod_autohost.so

%files mod_case
%doc mod_case/mod_case.html
%config(noreplace) %{_sysconfdir}/%{name}.d/28_mod_case.conf
%{_libdir}/%{name}/mod_case.so

%files mod_gss
%doc mod_gss-*/COPYING mod_gss-*/mod_gss.html mod_gss-*/README.mod_gss mod_gss-*/rfc1509.txt mod_gss-*/rfc2228.txt
%config(noreplace) %{_sysconfdir}/%{name}.d/26_mod_gss.conf
%{_libdir}/%{name}/mod_gss.so

%files mod_load
%doc doc/contrib/mod_load.html
%config(noreplace) %{_sysconfdir}/%{name}.d/31_mod_load.conf
%{_libdir}/%{name}/mod_load.so

%files mod_shaper
%doc doc/contrib/mod_shaper.html
%config(noreplace) %{_sysconfdir}/%{name}.d/32_mod_shaper.conf
%{_libdir}/%{name}/mod_shaper.so

%files mod_wrap
%doc doc/contrib/mod_wrap2.html
%config(noreplace) %{_sysconfdir}/%{name}.d/21_mod_wrap2.conf
%{_libdir}/%{name}/mod_wrap2.so

%files mod_wrap_file
%doc doc/contrib/mod_wrap2_file.html
%config(noreplace) %{_sysconfdir}/%{name}.d/22_mod_wrap2_file.conf
%{_libdir}/%{name}/mod_wrap2_file.so

%files mod_wrap_sql
%doc doc/contrib/mod_wrap2_sql.html
%config(noreplace) %{_sysconfdir}/%{name}.d/23_mod_wrap2_sql.conf
%{_libdir}/%{name}/mod_wrap2_sql.so

%files mod_ban
%doc doc/contrib/mod_ban.html
%config(noreplace) %{_sysconfdir}/%{name}.d/35_mod_ban.conf
%{_libdir}/%{name}/mod_ban.so

%files mod_vroot
%doc mod_vroot/mod_vroot.html
%config(noreplace) %{_sysconfdir}/%{name}.d/36_mod_vroot.conf
%{_libdir}/%{name}/mod_vroot.so

%files mod_sftp
%doc doc/contrib/mod_sftp.html
%config(noreplace) %{_sysconfdir}/blacklist.dat
%config(noreplace) %{_sysconfdir}/dhparams.pem
%config(noreplace) %{_sysconfdir}/%{name}.d/37_mod_sftp.conf
%{_libdir}/%{name}/mod_sftp.so

%files mod_sftp_pam
%doc doc/contrib/mod_sftp_pam.html
%config(noreplace) %{_sysconfdir}/%{name}.d/38_mod_sftp_pam.conf
%{_libdir}/%{name}/mod_sftp_pam.so

%files mod_sftp_sql
%doc doc/contrib/mod_sftp_sql.html
%config(noreplace) %{_sysconfdir}/%{name}.d/39_mod_sftp_sql.conf
%{_libdir}/%{name}/mod_sftp_sql.so

%files mod_memcache
%doc doc/modules/mod_memcache.html
%config(noreplace) %{_sysconfdir}/%{name}.d/40_mod_memcache.conf
%{_libdir}/%{name}/mod_memcache.so

