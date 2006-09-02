Summary:	LDP Author Guide
Summary(pl):	Podrêcznik dla autorów LDP
Name:		LDP-Author-Guide
Version:	3.14
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/%{name}.html.tar.gz
# Source0-md5:	618a6538d1e162a096266fc62ee81af4
URL:		http://www.tldp.org/LDP/LDP-Author-Guide/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lists the tools, procedures, and hints to get LDP authors up to speed
and writing.

There are many ways to contribute to the Linux movement without
actually writing code. One of the most important is writing
documentation, allowing each person to share their knowledge with
thousands of others around the world. This Guide is designed to help
you get familiar with how the LDP works, and what tools you'll need to
write your own HOWTO.

%description -l pl
W tym podrêczniku wymienione s± narzêdzia, procedury i wskazówki,
które u³atwiaj± ¿ycie autorom dokumentów LDP.

Jest wiele sposobów wspierania ruchu spo³eczno¶ci linuksowej,
niekoniecznie trzeba programowaæ. Jednym z najwa¿niejszych jest
pisanie dokumentacji, pozwala to dzieliæ siê swoj± wiedz± z tysi±cami
u¿ytkowników z ca³ego ¶wiata. Ten przewodnik jest po to, ¿eby¶
zaznajomi³(a) siê z tym jak dzia³a LDP i jakie narzêdzia bêd± Ci
potrzebne do napisania w³asnego HOWTO.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
