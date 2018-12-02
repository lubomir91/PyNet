ixi_asr1_show_cdp_neighbors_detail = '''

ixi-asr1>show cdp neighbors detail
-------------------------
Device ID: ixi3-ax3(FOX1725GYCA)
Entry address(es): 
  IP address: 172.22.3.17
Platform: N5K-C5596UP,  Capabilities: Switch IGMP CVTA phone port 
Interface: GigabitEthernet0,  Port ID (outgoing port): Ethernet100/1/20
Holdtime : 120 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

advertisement version: 2
Native VLAN: 666
Duplex: full
Management address(es): 
  IP address: 192.168.1.1

-------------------------
Device ID: ixi3-ax3(FOX1725GYCA)
Entry address(es): 
  IP address: 172.22.3.17
Platform: N5K-C5596UP,  Capabilities: Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet0/1/0,  Port ID (outgoing port): Ethernet1/13
Holdtime : 174 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 192.168.1.1

-------------------------
Device ID: ixi3-ax3(FOX1725GYCA)
Entry address(es): 
  IP address: 172.22.3.17
Platform: N5K-C5596UP,  Capabilities: Switch IGMP CVTA phone port 
Interface: GigabitEthernet0/0/4,  Port ID (outgoing port): Ethernet100/1/21
Holdtime : 150 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

advertisement version: 2
Native VLAN: 666
Duplex: full
Management address(es): 
  IP address: 192.168.1.1

-------------------------
Device ID: ixi3-ax4(FOX1725GYCW)
Entry address(es): 
  IP address: 172.22.3.18
Platform: N5K-C5596UP,  Capabilities: Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet0/3/0,  Port ID (outgoing port): Ethernet4/14
Holdtime : 134 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 192.168.1.2
          

Total cdp entries displayed : 4
'''

ixi_asr2_show_cdp_neighbors_detail = '''

ixi-asr2>show cdp neighbors detail 
-------------------------
Device ID: ixi3-ax3(FOX1725GYCA)
Entry address(es): 
  IP address: 172.22.3.17
Platform: N5K-C5596UP,  Capabilities: Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet0/1/0,  Port ID (outgoing port): Ethernet4/14
Holdtime : 168 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 192.168.1.1

-------------------------
Device ID: ixi3-ax4(FOX1725GYCW)
Entry address(es): 
  IP address: 172.22.3.18
Platform: N5K-C5596UP,  Capabilities: Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet0/3/0,  Port ID (outgoing port): Ethernet1/13
Holdtime : 128 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 192.168.1.2

-------------------------
Device ID: ixi3-ax4(FOX1725GYCW)
Entry address(es): 
  IP address: 172.22.3.18
Platform: N5K-C5596UP,  Capabilities: Switch IGMP CVTA phone port 
Interface: GigabitEthernet0/0/4,  Port ID (outgoing port): Ethernet100/1/21
Holdtime : 140 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

advertisement version: 2
Native VLAN: 666
Duplex: full
Management address(es): 
  IP address: 192.168.1.2

-------------------------
Device ID: ixi3-ax4(FOX1725GYCW)
Entry address(es): 
  IP address: 172.22.3.18
Platform: N5K-C5596UP,  Capabilities: Switch IGMP CVTA phone port 
Interface: GigabitEthernet0,  Port ID (outgoing port): Ethernet100/1/20
Holdtime : 140 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

advertisement version: 2
Native VLAN: 666
Duplex: full
Management address(es): 
  IP address: 192.168.1.2
          
-------------------------
Device ID: mos-asr2.icepor.com
Entry address(es): 
  IP address: 10.255.252.170
Platform: cisco ASR1001-X,  Capabilities: Router IGMP 
Interface: Tunnel210,  Port ID (outgoing port): Tunnel202
Holdtime : 151 sec

Version :
Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.6, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Wed 28-Feb-18 16:03 by mcpre

advertisement version: 2
Management address(es): 
  IP address: 10.255.252.170


Total cdp entries displayed : 5
'''



ixi3_ax3_show_cdp_neighbors_detail = '''
ixi3-ax3# show cdp neighbors detail 
----------------------------------------
Device ID: ixi3-ax4(FOX1725GYCW)
System Name: ixi3-ax4

Interface address(es):
    IPv4 Address: 192.168.1.2
Platform: N5K-C5596UP, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
Interface: mgmt0, Port ID (outgoing port): mgmt0
Holdtime: 157 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

Advertisement Version: 2
Duplex: full

MTU: 1500
Physical Location: IXI3
Mgmt address(es):
    IPv4 Address: 192.168.1.2
----------------------------------------
Device ID: ixi3-ax4(FOX1725GYCW)
System Name: ixi3-ax4

Interface address(es):
    IPv4 Address: 172.22.3.18
Platform: N5K-C5596UP, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet1/1, Port ID (outgoing port): Ethernet1/1
Holdtime: 157 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

Advertisement Version: 2

Native VLAN: 1
Duplex: full
Physical Location: IXI3
Mgmt address(es):
    IPv4 Address: 192.168.1.2
----------------------------------------
Device ID: ixi3-ax4(FOX1725GYCW)
System Name: ixi3-ax4

Interface address(es):
    IPv4 Address: 172.22.3.18
Platform: N5K-C5596UP, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet1/2, Port ID (outgoing port): Ethernet1/2
Holdtime: 157 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

Advertisement Version: 2

Native VLAN: 1
Duplex: full
Physical Location: IXI3
Mgmt address(es):
    IPv4 Address: 192.168.1.2
----------------------------------------
Device ID: ixi3-ax4(FOX1725GYCW)
System Name: ixi3-ax4

Interface address(es):
    IPv4 Address: 172.22.3.18
Platform: N5K-C5596UP, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet1/3, Port ID (outgoing port): Ethernet1/3
Holdtime: 157 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

Advertisement Version: 2

Native VLAN: 1
Duplex: full
Physical Location: IXI3
Mgmt address(es):
    IPv4 Address: 192.168.1.2
----------------------------------------
Device ID: ixi3-ax4(FOX1725GYCW)
System Name: ixi3-ax4

Interface address(es):
    IPv4 Address: 172.22.3.18
Platform: N5K-C5596UP, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet1/4, Port ID (outgoing port): Ethernet1/4
Holdtime: 157 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

Advertisement Version: 2

Native VLAN: 1
Duplex: full
Physical Location: IXI3
Mgmt address(es):
    IPv4 Address: 192.168.1.2
----------------------------------------
Device ID: IXI3-VS1.icepor.com
VTP Management Domain Name: IXI

Interface address(es):
    IPv4 Address: 172.22.3.101
Platform: WS-C6509-E, Capabilities: Router Switch IGMP Filtering 
Interface: Ethernet1/10, Port ID (outgoing port): TenGigabitEthernet1/6/4
Holdtime: 135 sec

Version:
Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(33)SXI, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2008 by Cisco Systems, Inc.
Compiled Fri 07-Nov-08 04:01 by prod_rel_team

Advertisement Version: 2

Native VLAN: 1
Duplex: full
Mgmt address(es):
    IPv4 Address: 172.22.3.101
----------------------------------------
Device ID: ixi-asr1.icepor.com

Interface address(es):
    IPv4 Address: 81.16.158.254
Platform: ASR1002-X, Capabilities: Router IGMP Filtering 
Interface: Ethernet1/13, Port ID (outgoing port): TenGigabitEthernet0/1/0
Holdtime: 176 sec

Version:
Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.6, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Wed 28-Feb-18 16:03 by mcpre

Advertisement Version: 2
Mgmt address(es):
    IPv4 Address: 81.16.158.254
----------------------------------------
Device ID: IXI3-AS5.icepor.com
VTP Management Domain Name: IXI

Interface address(es):
    IPv4 Address: 172.22.3.5
Platform: WS-C3750E-48T, Capabilities: Switch IGMP Filtering 
Interface: Ethernet2/14, Port ID (outgoing port): TenGigabitEthernet1/0/1
Holdtime: 164 sec

Version:
Cisco IOS Software, C3750E Software (C3750E-IPBASEK9-M), Version 12.2(55)SE12, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2017 by Cisco Systems, Inc.
Compiled Thu 28-Sep-17 01:02 by prod_rel_team

Advertisement Version: 2

Native VLAN: 1
Duplex: full
Mgmt address(es):
    IPv4 Address: 172.22.3.5
----------------------------------------
Device ID: ixi3-test-ax1.icepor.com(SSI14200EVK)
System Name: ixi3-test-ax1

Interface address(es):
    IPv4 Address: 172.22.2.8
Platform: N5K-C5020P-BF, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet4/2, Port ID (outgoing port): Ethernet1/16
Holdtime: 136 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 5.2(1)N1(9b)

Advertisement Version: 2

Native VLAN: 1
Duplex: full

MTU: 1500
Physical Location: IXI3
Mgmt address(es):
    IPv4 Address: 172.22.2.8
----------------------------------------
Device ID: ixi-asr2.icepor.com

Interface address(es):
    IPv4 Address: 172.22.0.132
Platform: ASR1002-X, Capabilities: Router IGMP Filtering 
Interface: Ethernet4/14, Port ID (outgoing port): TenGigabitEthernet0/1/0
Holdtime: 137 sec

Version:
Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.6, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Wed 28-Feb-18 16:03 by mcpre

Advertisement Version: 2
Mgmt address(es):
    IPv4 Address: 172.22.0.132
----------------------------------------
Device ID: tsi-ax3(FOX1725GP1B)
System Name: tsi-ax3

Interface address(es):
    IPv4 Address: 172.22.1.55
Platform: N5K-C5596UP, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet4/15, Port ID (outgoing port): Ethernet4/15
Holdtime: 157 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

Advertisement Version: 2

Native VLAN: 1
Duplex: full

MTU: 1500
Physical Location: TSI
Mgmt address(es):
    IPv4 Address: 192.168.1.1
----------------------------------------
Device ID: tsi-ax3(FOX1725GP1B)
System Name: tsi-ax3

Interface address(es):
    IPv4 Address: 172.22.1.55
Platform: N5K-C5596UP, Capabilities: Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet4/16, Port ID (outgoing port): Ethernet4/16
Holdtime: 157 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 7.1(3)N1(2)

Advertisement Version: 2

Native VLAN: 1
Duplex: full

MTU: 1500
Physical Location: TSI
Mgmt address(es):
    IPv4 Address: 192.168.1.1
----------------------------------------
Device ID: ixi-asr1.icepor.com

Interface address(es):
    IPv4 Address: 172.22.0.131
Platform: ASR1002-X, Capabilities: Router IGMP Filtering 
Interface: Ethernet100/1/20, Port ID (outgoing port): GigabitEthernet0
Holdtime: 134 sec

Version:
Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.6, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Wed 28-Feb-18 16:03 by mcpre

Advertisement Version: 2
Duplex: full
Mgmt address(es):
    IPv4 Address: 172.22.0.131
----------------------------------------
Device ID: ixi-asr1.icepor.com

Interface address(es):
    IPv4 Address: 172.22.0.33
Platform: ASR1002-X, Capabilities: Router IGMP Filtering 
Interface: Ethernet100/1/21, Port ID (outgoing port): GigabitEthernet0/0/4
Holdtime: 147 sec

Version:
Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.6, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Wed 28-Feb-18 16:03 by mcpre

Advertisement Version: 2
Duplex: full
Mgmt address(es):
    IPv4 Address: 172.22.0.33
'''
