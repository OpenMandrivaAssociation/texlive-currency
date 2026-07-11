%global tl_name currency
%global tl_revision 48990

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Format currencies in a consistent way
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/currency
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/currency.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/currency.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/currency.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package facilitates the formatting of currencies (amounts and units)
with various formatting capabilities.

