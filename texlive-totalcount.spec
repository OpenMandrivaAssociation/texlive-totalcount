Name:		texlive-totalcount
Version:	67201
Release:	1
Summary:	Commands for typesetting total values of counters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/totalcount
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totalcount.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totalcount.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/totalcount.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package offers commands for typesetting total values
of counters.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/totalcount
%{_texmfdistdir}/tex/latex/totalcount
%doc %{_texmfdistdir}/doc/latex/totalcount

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
