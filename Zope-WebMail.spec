%define		zope_subname	WebMail
Summary:	A mail client for Zope
Summary(pl):	Klient poczty elektronicznej dla Zope
Name:		Zope-%{zope_subname}
Version:	4.3.1
Release:	2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://www.pentila.com/produits/WebMail/%{zope_subname}-%{version}.tgz
# Source0-md5:	b35b48977be73eb8511296f3d3f7a244
URL:		http://www.pentila.com/produits/WebMail/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebMail is a mail client for Zope.

%description -l pl
WebMail jest klientem poczty elektronicznej dla Zope.

%prep
%setup -q -n %{zope_subname}

find . -type d -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {dtml,style_sheet,www,*.py,refresh.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
# contains authors
%doc LICENSE.txt CHANGES.txt
%{_datadir}/%{name}
