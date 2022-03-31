# SNMP-BasesBandwithMonitoring

It is quite essential to ensure that resources are sufficient in business critical networks. One of the rapidly and randomly changing resources is Bandwidth utilization, as changes according to customers’ distribution & behavior, hence, it is critical to keep monitoring it, perhaps in accordance to a certain threshold, to determine the need of expanding it further.
In this project, I demonstrate an application that can monitor the bandwidth utilization % on a given interface. The Python application uses pysnmp library to integrate with the router through SNMP, track & record the bandwidth utilization % periodically as per end user requirements. Below is the architecture specification of the application: 

pic 1

## Steps: 

### Install Pysnmp
pip install --upgrade pysnmp

### Link to MIB & OID details for Cisco
[MIB & OID Details](https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/security/ise/2-6/admin_guide/b_ise_admin_guide_26/b_ise_admin_guide_26_chapter_0100001.html.xml)

## Testing:

- Install GN3 Software
- Install PacketSender

### Install Microsoft KM-TEST Loopback
- Run hdwwiz.exe in admin mode 
pic 2
- Setup the IP address for the adapter
Pic 3

### On GN3
- Add the C7200 template
pic 4
- Connect the topology and use the loopback adapter
pic 5
pic 6

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

pic 7

### Run the app & use PacketSender for Testing

pic 8

### Sample Output

pic 9


