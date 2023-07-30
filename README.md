# Ochkos
The server administration software for your needs. Developed by experienced server administrators, this panel simplifies the effort of managing your hosting platform.
Installation
Fast install

    Ensure that your webserver serves /var/www/html
    Extract froxlor into /var/www/html
    Point your browser to http://[ip-of-webserver]/froxlor
    Follow the installer
    Login as administrator
    Have fun!

If you have chosen to do the configuration by hand during the installation, you have to complete some more steps:

    Adjust "System > Settings" according to your needs
    Choose your distribution under "System > Configuration"
    Follow the steps for your services

Detailed installation

https://docs.froxlor.org/latest/general/installation/
Help

You may find help in the following places:
Discord

The froxlor community discord server can be found here: https://discord.froxlor.org
IRC

froxlor may be found on libera.chat, channel #froxlor: irc://irc.libera.chat/froxlor
Forum

The community is located on https://forum.froxlor.org/
Wiki

More documentation may be found in the froxlor - documentation: https://docs.froxlor.org/
License

May be found in COPYING
Downloads
Tarball

https://files.froxlor.org/releases/froxlor-latest.tar.gz MD5 SHA1
Debian / Ubuntu repository

HowTo
Debian

apt-get -y install apt-transport-https lsb-release ca-certificates curl
curl -sSLo /usr/share/keyrings/deb.froxlor.org-froxlor.gpg https://deb.froxlor.org/froxlor.gpg
echo sh -c '"deb [signed-by=/usr/share/keyrings/deb.froxlor.org-froxlor.gpg] https://deb.froxlor.org/debian $(lsb_release -sc) main" > /etc/apt/sources.list.d/froxlor.list'

Ubuntu

apt-get -y install apt-transport-https lsb-release ca-certificates curl
curl -sSLo /usr/share/keyrings/deb.froxlor.org-froxlor.gpg https://deb.froxlor.org/froxlor.gpg
echo sh -c '"deb [signed-by=/usr/share/keyrings/deb.froxlor.org-froxlor.gpg] https://deb.froxlor.org/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/froxlor.list'

Contributing

see here
