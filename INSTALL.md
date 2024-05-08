## CentOS/RHEL 9

Install.
```
dnf install net-snmp net-snmp-utils
cp /usr/share/doc/mrtg-rrd/snmpd.conf /etc/snmp/snmpd.conf
systemctl enable snmpd --now 

dnf install mrtg rrdtool rrdtool-perl
cp /usr/share/doc/mrtg-rrd/mrtg.cfg /etc/mrtg/mrtg.cfg
systemctl enable mrtg --now 

dnf install mrtg-rrd
```
