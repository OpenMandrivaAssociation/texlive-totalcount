%global tl_name totalcount
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Commands for typesetting total values of counters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/totalcount
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/totalcount.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/totalcount.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/totalcount.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package offers commands for typesetting total values of
counters.

