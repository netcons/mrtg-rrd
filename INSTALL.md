## CentOS/RHEL 9

Install.
```
dnf install net-snmp net-snmp-utils
cp /usr/share/doc/mrtg-rrd/snmpd.conf /etc/snmp/snmpd.conf
systemctl enable snmpd --now 

dnf install mrtg rrdtool rrdtool-perl
cp /usr/share/doc/mrtg-rrd/mrtg.cfg /etc/mrtg/mrtg.cfg
systemctl enable mrtg --now 

cd /tmp
curl -s https://api.github.com/repos/netcons/mrtg-rrd/releases \
| grep "browser_download_url.*.el9.*rpm" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -

dnf install mrtg-rrd-*.el9.noarch.rpm

rm mrtg-rrd-*.el9.noarch.rpm
```
