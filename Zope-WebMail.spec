%include	/usr/lib/rpm/macros.python
%define		zope_subname	WebMail
Summary:	Webmail - is a mail client for Zope
Summary(pl):	Webmail - jest klientem poczty elektronicznej dla Zope
Name:		Zope-%{zope_subname}
Version:	4.1
Release:	1
License:	GNU
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
Webmail - is a mail client for Zope

%description -l pl
Webmail - jest klientem poczty elektronicznej dla Zope

%prep
%setup -q -c %{zope_subname}-%{version}

%build
rm -rf `find . -type d -name CVS`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}
cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
# rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/*.txt

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
# %%doc %{zope_subname}/*.txt
%{product_dir}/%{zope_subname}
