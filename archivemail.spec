Summary:	Archive and compress old email
Name:		archivemail
Version:	0.9.0
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://heanet.dl.sourceforge.net/archivemail/%{name}-%{version}.tar.gz
# Source0-md5:	ee36b3e8451ec563ae9338f3dd75e3f6
URL:		http://archivemail.sourceforge.net/
BuildRequires:	docbook-dtd30-sgml
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Archivemail is a tool written in Python for archiving and
compressing old email in mailboxes.

It can move messages older than the specified number of days to a
separate 'archive' mbox-format mailbox that is compressed with 'gzip'.

For example, have you been subscribing to the 'linux-kernel' mailing
list for the last 6 years and ended up with an 160-meg mailbox that
Mutt is taking a long time to load? Archivemail can move all
messages that are older than 6 months to a separate compressed
mailbox, and leave you with just the most recent messages.

It supports IMAP, Maildir, MH and mbox-format mailboxes.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py -v install \
	--prefix=%{_prefix} \
	--root=${RPM_BUILD_ROOT} \
	--optimize=2

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc CHANGELOG FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/archivemail.1*

