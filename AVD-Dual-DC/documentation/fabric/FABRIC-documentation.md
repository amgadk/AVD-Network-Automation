# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | dc1-borderleaf1 | 192.168.0.107/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-borderleaf2 | 192.168.0.108/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf1 | 192.168.0.101/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf2 | 192.168.0.102/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf3 | 192.168.0.103/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf4 | 192.168.0.104/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc1-spine1 | 192.168.0.111/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc1-spine2 | 192.168.0.112/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-borderleaf1 | 192.168.0.207/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-borderleaf2 | 192.168.0.208/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf1 | 192.168.0.201/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf2 | 192.168.0.202/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf3 | 192.168.0.203/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf4 | 192.168.0.204/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc2-spine1 | 192.168.0.211/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc2-spine2 | 192.168.0.212/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | dc1-borderleaf1 | Ethernet1 | spine | dc1-spine1 | Ethernet7 |
| l3leaf | dc1-borderleaf1 | Ethernet2 | spine | dc1-spine2 | Ethernet7 |
| l3leaf | dc1-borderleaf1 | Ethernet5 | mlag_peer | dc1-borderleaf2 | Ethernet5 |
| l3leaf | dc1-borderleaf1 | Ethernet6 | mlag_peer | dc1-borderleaf2 | Ethernet6 |
| l3leaf | dc1-borderleaf1 | Ethernet20 | l3leaf | dc2-borderleaf1 | Ethernet20 |
| l3leaf | dc1-borderleaf2 | Ethernet1 | spine | dc1-spine1 | Ethernet8 |
| l3leaf | dc1-borderleaf2 | Ethernet2 | spine | dc1-spine2 | Ethernet8 |
| l3leaf | dc1-borderleaf2 | Ethernet20 | l3leaf | dc2-borderleaf2 | Ethernet20 |
| l3leaf | dc1-leaf1 | Ethernet1 | spine | dc1-spine1 | Ethernet1 |
| l3leaf | dc1-leaf1 | Ethernet2 | spine | dc1-spine2 | Ethernet1 |
| l3leaf | dc1-leaf1 | Ethernet5 | mlag_peer | dc1-leaf2 | Ethernet5 |
| l3leaf | dc1-leaf1 | Ethernet6 | mlag_peer | dc1-leaf2 | Ethernet6 |
| l3leaf | dc1-leaf2 | Ethernet1 | spine | dc1-spine1 | Ethernet2 |
| l3leaf | dc1-leaf2 | Ethernet2 | spine | dc1-spine2 | Ethernet2 |
| l3leaf | dc1-leaf3 | Ethernet1 | spine | dc1-spine1 | Ethernet3 |
| l3leaf | dc1-leaf3 | Ethernet2 | spine | dc1-spine2 | Ethernet3 |
| l3leaf | dc1-leaf3 | Ethernet5 | mlag_peer | dc1-leaf4 | Ethernet5 |
| l3leaf | dc1-leaf3 | Ethernet6 | mlag_peer | dc1-leaf4 | Ethernet6 |
| l3leaf | dc1-leaf4 | Ethernet1 | spine | dc1-spine1 | Ethernet4 |
| l3leaf | dc1-leaf4 | Ethernet2 | spine | dc1-spine2 | Ethernet4 |
| l3leaf | dc2-borderleaf1 | Ethernet1 | spine | dc2-spine1 | Ethernet7 |
| l3leaf | dc2-borderleaf1 | Ethernet2 | spine | dc2-spine2 | Ethernet7 |
| l3leaf | dc2-borderleaf1 | Ethernet5 | mlag_peer | dc2-borderleaf2 | Ethernet5 |
| l3leaf | dc2-borderleaf1 | Ethernet6 | mlag_peer | dc2-borderleaf2 | Ethernet6 |
| l3leaf | dc2-borderleaf2 | Ethernet1 | spine | dc2-spine1 | Ethernet8 |
| l3leaf | dc2-borderleaf2 | Ethernet2 | spine | dc2-spine2 | Ethernet8 |
| l3leaf | dc2-leaf1 | Ethernet1 | spine | dc2-spine1 | Ethernet1 |
| l3leaf | dc2-leaf1 | Ethernet2 | spine | dc2-spine2 | Ethernet1 |
| l3leaf | dc2-leaf1 | Ethernet5 | mlag_peer | dc2-leaf2 | Ethernet5 |
| l3leaf | dc2-leaf1 | Ethernet6 | mlag_peer | dc2-leaf2 | Ethernet6 |
| l3leaf | dc2-leaf2 | Ethernet1 | spine | dc2-spine1 | Ethernet2 |
| l3leaf | dc2-leaf2 | Ethernet2 | spine | dc2-spine2 | Ethernet2 |
| l3leaf | dc2-leaf3 | Ethernet1 | spine | dc2-spine1 | Ethernet3 |
| l3leaf | dc2-leaf3 | Ethernet2 | spine | dc2-spine2 | Ethernet3 |
| l3leaf | dc2-leaf3 | Ethernet5 | mlag_peer | dc2-leaf4 | Ethernet5 |
| l3leaf | dc2-leaf3 | Ethernet6 | mlag_peer | dc2-leaf4 | Ethernet6 |
| l3leaf | dc2-leaf4 | Ethernet1 | spine | dc2-spine1 | Ethernet4 |
| l3leaf | dc2-leaf4 | Ethernet2 | spine | dc2-spine2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.103.0/24 | 256 | 24 | 9.38 % |
| 192.168.203.0/24 | 256 | 24 | 9.38 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| dc1-borderleaf1 | Ethernet1 | 192.168.103.65/31 | dc1-spine1 | Ethernet7 | 192.168.103.64/31 |
| dc1-borderleaf1 | Ethernet2 | 192.168.103.67/31 | dc1-spine2 | Ethernet7 | 192.168.103.66/31 |
| dc1-borderleaf1 | Ethernet20 | 172.100.100.200/31 | dc2-borderleaf1 | Ethernet20 | 172.100.100.201/31 |
| dc1-borderleaf2 | Ethernet1 | 192.168.103.69/31 | dc1-spine1 | Ethernet8 | 192.168.103.68/31 |
| dc1-borderleaf2 | Ethernet2 | 192.168.103.71/31 | dc1-spine2 | Ethernet8 | 192.168.103.70/31 |
| dc1-borderleaf2 | Ethernet20 | 172.100.101.146/31 | dc2-borderleaf2 | Ethernet20 | 172.100.101.147/31 |
| dc1-leaf1 | Ethernet1 | 192.168.103.49/31 | dc1-spine1 | Ethernet1 | 192.168.103.48/31 |
| dc1-leaf1 | Ethernet2 | 192.168.103.51/31 | dc1-spine2 | Ethernet1 | 192.168.103.50/31 |
| dc1-leaf2 | Ethernet1 | 192.168.103.53/31 | dc1-spine1 | Ethernet2 | 192.168.103.52/31 |
| dc1-leaf2 | Ethernet2 | 192.168.103.55/31 | dc1-spine2 | Ethernet2 | 192.168.103.54/31 |
| dc1-leaf3 | Ethernet1 | 192.168.103.57/31 | dc1-spine1 | Ethernet3 | 192.168.103.56/31 |
| dc1-leaf3 | Ethernet2 | 192.168.103.59/31 | dc1-spine2 | Ethernet3 | 192.168.103.58/31 |
| dc1-leaf4 | Ethernet1 | 192.168.103.61/31 | dc1-spine1 | Ethernet4 | 192.168.103.60/31 |
| dc1-leaf4 | Ethernet2 | 192.168.103.63/31 | dc1-spine2 | Ethernet4 | 192.168.103.62/31 |
| dc2-borderleaf1 | Ethernet1 | 192.168.203.105/31 | dc2-spine1 | Ethernet7 | 192.168.203.104/31 |
| dc2-borderleaf1 | Ethernet2 | 192.168.203.107/31 | dc2-spine2 | Ethernet7 | 192.168.203.106/31 |
| dc2-borderleaf2 | Ethernet1 | 192.168.203.109/31 | dc2-spine1 | Ethernet8 | 192.168.203.108/31 |
| dc2-borderleaf2 | Ethernet2 | 192.168.203.111/31 | dc2-spine2 | Ethernet8 | 192.168.203.110/31 |
| dc2-leaf1 | Ethernet1 | 192.168.203.89/31 | dc2-spine1 | Ethernet1 | 192.168.203.88/31 |
| dc2-leaf1 | Ethernet2 | 192.168.203.91/31 | dc2-spine2 | Ethernet1 | 192.168.203.90/31 |
| dc2-leaf2 | Ethernet1 | 192.168.203.93/31 | dc2-spine1 | Ethernet2 | 192.168.203.92/31 |
| dc2-leaf2 | Ethernet2 | 192.168.203.95/31 | dc2-spine2 | Ethernet2 | 192.168.203.94/31 |
| dc2-leaf3 | Ethernet1 | 192.168.203.97/31 | dc2-spine1 | Ethernet3 | 192.168.203.96/31 |
| dc2-leaf3 | Ethernet2 | 192.168.203.99/31 | dc2-spine2 | Ethernet3 | 192.168.203.98/31 |
| dc2-leaf4 | Ethernet1 | 192.168.203.101/31 | dc2-spine1 | Ethernet4 | 192.168.203.100/31 |
| dc2-leaf4 | Ethernet2 | 192.168.203.103/31 | dc2-spine2 | Ethernet4 | 192.168.203.102/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.101.0/24 | 256 | 16 | 6.25 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | dc1-borderleaf1 | 192.168.101.17/32 |
| FABRIC | dc1-borderleaf2 | 192.168.101.18/32 |
| FABRIC | dc1-leaf1 | 192.168.101.13/32 |
| FABRIC | dc1-leaf2 | 192.168.101.14/32 |
| FABRIC | dc1-leaf3 | 192.168.101.15/32 |
| FABRIC | dc1-leaf4 | 192.168.101.16/32 |
| FABRIC | dc1-spine1 | 192.168.101.11/32 |
| FABRIC | dc1-spine2 | 192.168.101.12/32 |
| FABRIC | dc2-borderleaf1 | 192.168.101.27/32 |
| FABRIC | dc2-borderleaf2 | 192.168.101.28/32 |
| FABRIC | dc2-leaf1 | 192.168.101.23/32 |
| FABRIC | dc2-leaf2 | 192.168.101.24/32 |
| FABRIC | dc2-leaf3 | 192.168.101.25/32 |
| FABRIC | dc2-leaf4 | 192.168.101.26/32 |
| FABRIC | dc2-spine1 | 192.168.101.21/32 |
| FABRIC | dc2-spine2 | 192.168.101.22/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.102.0/24 | 256 | 6 | 2.35 % |
| 192.168.202.0/24 | 256 | 6 | 2.35 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | dc1-borderleaf1 | 192.168.102.17/32 |
| FABRIC | dc1-borderleaf2 | 192.168.102.17/32 |
| FABRIC | dc1-leaf1 | 192.168.102.13/32 |
| FABRIC | dc1-leaf2 | 192.168.102.13/32 |
| FABRIC | dc1-leaf3 | 192.168.102.15/32 |
| FABRIC | dc1-leaf4 | 192.168.102.15/32 |
| FABRIC | dc2-borderleaf1 | 192.168.202.27/32 |
| FABRIC | dc2-borderleaf2 | 192.168.202.27/32 |
| FABRIC | dc2-leaf1 | 192.168.202.23/32 |
| FABRIC | dc2-leaf2 | 192.168.202.23/32 |
| FABRIC | dc2-leaf3 | 192.168.202.25/32 |
| FABRIC | dc2-leaf4 | 192.168.202.25/32 |
