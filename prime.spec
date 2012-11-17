Summary:	PRIME - a Japanese PRedictive Input Method Editor
Summary(pl.UTF-8):	PRIME - edytor przewidującej metody wprowadzania tekstu japońskiego
Name:		prime
Version:	1.0.0.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://prime.sourceforge.jp/src/%{name}-%{version}.tar.gz
# Source0-md5:	c3bb6df8590986104e41c23330d90aef
URL:		http://taiyaki.org/prime/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
BuildRequires:	sed >= 4.0
%{?ruby_mod_ver_requires_eq}
Requires:	ruby
Requires:	ruby-sary
Requires:	ruby-progressbar 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
PRIME predicts user's input words using the knowledge of natural
language and the history of user's operations, and reduces the
cost of typing by the user. For example, if a user wants to input
"application" and types "ap" as the beginning characters of the word,
PRIME might predict some candidate words like "apple", "application",
"appointment", etc... And then the user can input "application"
easily by selecting the word from the candidate words by PRIME.

%description -l pl.UTF-8
PRIME (PRedictive Input Method Editor) przewiduje słowa wprowadzane
przez użytkownika, wykorzystując znajomość języka naturalnego oraz
historię operacji użytkownika; zmniejsza przy tym koszt pisania przez
użytkownika. Na przykład, jeśli użytkownik chce wprowadzić słowo
"aplikacja" i napisze "ap" jako początkowe znaki słowa, PRIME może
przewidzieć pasujące słowa, takie jak "aparycja", "aplikacja",
"aprobata" itp. Następnie użytkownik może łatwo wprowadzić słowo
"aplikacja" wybierając słowo z proponowanych przez PRIME.

%prep
%setup -q

%{__sed} -i -e 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|g' src/*.src

%build
%configure \
	--with-rubydir=%{ruby_rubylibdir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-etc \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf prime-docs
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} prime-docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO prime-docs/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/Custom_prime.rb
%attr(755,root,root) %{_bindir}/prime
%attr(755,root,root) %{_bindir}/prime-dict-convert
%attr(755,root,root) %{_bindir}/prime-dict-index
%attr(755,root,root) %{_bindir}/prime-refresh
%attr(755,root,root) %{_bindir}/prime-userdict-convert
%attr(755,root,root) %{_bindir}/prime-userdict-update
%{ruby_rubylibdir}/%{name}
%{_datadir}/%{name}
%{_pkgconfigdir}/prime.pc
