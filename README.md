# Ochkos
The server administration software for your needs. Developed by experienced server administrators, this panel simplifies the effort of managing your hosting platform.


#Installation
Fast install



    Ensure that your webserver serves /var/www/html
    Extract ochkos into /var/www/html
    Point your browser to http://[ip-of-webserver]/froxlor
    Follow the installer
    Login as administrator
    Have fun!

If you have chosen to do the configuration by hand during the installation, you have to complete some more steps:

    Adjust "System > Settings" according to your needs
    Choose your distribution under "System > Configuration"
    Follow the steps for your services

#Detailed installation

https://docs.ochkos.org/latest/general/installation/
Help

You may find help in the following places:
Discord

The ochkos community discord server can be found here: https://discord.ochkos.org
IRC

froxlor may be found on libera.chat, channel #ochkos: irc://irc.libera.chat/ochkos
Forum

The community is located on https://forum.ochkos.org/
Wiki

More documentation may be found in the ochkos - documentation: https://docs.ochkos.org/
License

May be found in COPYING
Downloads
Tarball

https://files.ochkos.org/releases/ochkos-latest.tar.gz MD5 SHA1
Debian / Ubuntu repository

HowTo
Debian

apt-get -y install apt-transport-https lsb-release ca-certificates curl
curl -sSLo /usr/share/keyrings/deb.froxlor.org-froxlor.gpg https://deb.froxlor.org/froxlor.gpg
echo sh -c '"deb [signed-by=/usr/share/keyrings/deb.froxlor.org-froxlor.gpg] https://deb.froxlor.org/debian $(lsb_release -sc) main" > /etc/apt/sources.list.d/froxlor.list'

Ubuntu

apt-get -y install apt-transport-https lsb-release ca-certificates curl
curl -sSLo /usr/share/keyrings/deb.froxlor.org-froxlor.gpg https://deb.froxlor.org/froxlor.gpg
echo sh -c '"deb [signed-by=/usr/share/keyrings/deb.ochkos.org-ochkos.gpg] https://deb.ochkos.org/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ochkos.list'

