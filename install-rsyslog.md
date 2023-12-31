In this example, we will install rsyslog server on ubuntu 20.04.
rsyslog server is installed by default on ubuntu server.

Run following command to check and update rsyslog installation.\n
#apt-get install rsyslog -y

Once the installation is completed, start the Rsyslog service and enable it to start at system reboot:
#systemctl start rsyslog
#systemctl enable rsyslog

Setup rsyslog server
#nano /etc/rsyslog.conf

#provides UDP syslog reception
module(load="imudp")
input(type="imudp" port="514")

#provides TCP syslog reception
module(load="imtcp")
input(type="imtcp" port="514") 

Add the following line to receive and store incoming syslog messages: 
$template RemInputLogs, "/var/log/remotelogs/%FROMHOST-IP%/%PROGRAMNAME%.log"
*.* ?RemInputLogs

#systemctl restart rsyslog
#systemctl status rsyslog

Turn off repeated msg:
$RepeatedMsgReduction on	# do not log repeated messages


