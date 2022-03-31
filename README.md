# SNMP-BasesBandwithMonitoring

It is quite essential to ensure that resources are sufficient in business critical networks. One of the rapidly and randomly changing resources is Bandwidth utilization, as changes according to customers’ distribution & behavior, hence, it is critical to keep monitoring it, perhaps in accordance to a certain threshold, to determine the need of expanding it further.
In this project, I demonstrate an application that can monitor the bandwidth utilization % on a given interface. The Python application uses pysnmp library to integrate with the router through SNMP, track & record the bandwidth utilization % periodically as per end user requirements. Below is the architecture specification of the application: 

![Screenshot](https://github.com/alimo7amed93/SNMP-BasesBandwithMonitoring/blob/main/Pictures/pic1.png)

# Steps: 

### Install Pysnmp
pip install --upgrade pysnmp

### Link to MIB & OID details for Cisco
[MIB & OID Details](https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/security/ise/2-6/admin_guide/b_ise_admin_guide_26/b_ise_admin_guide_26_chapter_0100001.html.xml)

# Testing:

- Install GN3 Software
- Install PacketSender

### Install Microsoft KM-TEST Loopback
- Run hdwwiz.exe in admin mode 

![Screenshot](https://github.com/alimo7amed93/SNMP-BasesBandwithMonitoring/blob/main/Pictures/pic2.png)

- Setup the IP address for the adapter

![Screenshot](https://github.com/alimo7amed93/SNMP-BasesBandwithMonitoring/blob/main/Pictures/pic3.png)

### On GN3
- Add the C7200 template

![Screenshot](https://github.com/alimo7amed93/SNMP-BasesBandwithMonitoring/blob/main/Pictures/pic4.png)

- Connect the topology and use the loopback adapter
- 
![Screenshot](https://github.com/alimo7amed93/SNMP-BasesBandwithMonitoring/blob/main/Pictures/pic5.png)

![Screenshot](https://github.com/alimo7amed93/SNMP-BasesBandwithMonitoring/blob/main/Pictures/pic6.png)


### Configure the router with minimal configration to enable SNMP

enable
configure terminal
interface fastEthernet 0/0
ip address 10.0.0.1 255.255.255.0
no shutdown
exit
snmp-server community util RO
exit

### For testing ping the router from within the PC

![Screenshot](https://github.com/alimo7amed93/SNMP-BasesBandwithMonitoring/blob/main/Pictures/pic7.png)

### Run the app & use PacketSender for Testing

![Screenshot](https://github.com/alimo7amed93/SNMP-BasesBandwithMonitoring/blob/main/Pictures/pic8.png)

### Sample Output

![Screenshot](https://github.com/alimo7amed93/SNMP-BasesBandwithMonitoring/blob/main/Pictures/pic9.png)


