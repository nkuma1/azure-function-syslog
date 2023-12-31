## Install rsyslog server on ubuntu server to test Azure Function.

Note: rsyslog server is installed by default on ubuntu server version 20.04.

1\. Run following command to check and update rsyslog installation.   
    **#apt-get install rsyslog -y**

2\. Once the installation is completed, start the Rsyslog service and enable it to start at system reboot:   
    **#systemctl start rsyslog**  
    **#systemctl enable rsyslog**

3\. Setup rsyslog server   
    **#provides UDP syslog reception**  
    module(load="imudp")  
    input(type="imudp" port="514")  
    **#provides TCP syslog reception**  
    module(load="imtcp")  
    input(type="imtcp" port="514")

4\. Add the following line to receive and store incoming syslog messages:   
    $template RemInputLogs, "/var/log/remotelogs/%FROMHOST-IP%/%PROGRAMNAME%.log"  
    \*.\* ?RemInputLogs

     **#systemctl restart rsyslog**  
     **#systemctl status rsyslog**

5\. (Optional) Turn off repeated msg:  
    $RepeatedMsgReduction on # do not log repeated messages
