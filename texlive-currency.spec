Name:		texlive-currency
Version:	48990
Release:	2
Summary:	Format currencies in a consistent way
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/currency
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currency.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currency.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currency.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package facilitates the formatting of currencies (amounts
and units) with various formatting capabilities.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/currency
%{_texmfdistdir}/tex/latex/currency
%doc %{_texmfdistdir}/doc/latex/currency

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
