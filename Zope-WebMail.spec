%include	/usr/lib/rpm/macros.python
%define		zope_subname	WebMail
Summary:	WebMail - a mail client for Zope
Summary(pl):	WebMail - klient poczty elektronicznej dla Zope
Name:		Zope-%{zope_subname}
Version:	4.1
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://zope.org/Members/sgiraud/%{zope_subname}/%{zope_subname}/%{zope_subname}_%{version}.tar.gz
# Source0-md5:	3cc5047f150c66be431a6d1babc403c6
URL:		http://zope.org/Members/sgiraud/WebMail
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
WebMail is a mail client for Zope.

%description -l pl
WebMail jest klientem poczty elektronicznej dla Zope.

%prep
%setup -q -n %{zope_subname}

find . -type d -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

cp -af {dtml,style_sheet,www,*.py} $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
# contains authors
%doc LICENSE.txt
%{product_dir}/%{zope_subname}
