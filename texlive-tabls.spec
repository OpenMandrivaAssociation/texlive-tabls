%global tl_name tabls
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.5
Release:	%{tl_revision}.1
Summary:	Better vertical spacing in tables and arrays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabls
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabls.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabls.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Modifies LaTeX's array and tabular environments to keep text from
touching other text or hlines above or below. Several new parameters are
defined and some standard macros are re-defined. The package slows down
compilation of tables, since each entry is boxed twice.

