Name:		texlive-tabls
Version:	17255
Release:	2
Summary:	Better vertical spacing in tables and arrays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabls
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabls.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabls.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Modifies LaTeX's array and tabular environments to keep text
from touching other text or hlines above or below. Several new
parameters are defined and some standard macros are re-defined.
The package slows down compilation of tables, since each entry
is boxed twice.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabls/tabls.sty
%doc %{_texmfdistdir}/doc/latex/tabls/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/tabls/tabls.pdf
%doc %{_texmfdistdir}/doc/latex/tabls/tabls.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
