# revision 17255
# category Package
# catalog-ctan /macros/latex/contrib/tabls
# catalog-date 2010-03-09 13:13:30 +0100
# catalog-license other-free
# catalog-version 3.5
Name:		texlive-tabls
Version:	3.5
Release:	1
Summary:	Better vertical spacing in tables and arrays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabls
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabls.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabls.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Modifies LaTeX's array and tabular environments to keep text
from touching other text or hlines above or below. Several new
parameters are defined and some standard macros are re-defined.
The package slows down compilation of tables, since each entry
is boxed twice.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabls/tabls.sty
%doc %{_texmfdistdir}/doc/latex/tabls/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/tabls/tabls.pdf
%doc %{_texmfdistdir}/doc/latex/tabls/tabls.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
