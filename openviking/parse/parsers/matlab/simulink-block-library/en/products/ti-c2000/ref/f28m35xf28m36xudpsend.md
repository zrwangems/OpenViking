---
type: simulink-block
title: 'F28M35x/F28M36x UDP Send'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f28m35xf28m36xudpsend'
documentation_source_path: 'ref/f28m35xf28m36xudpsend.html'
language: en
---

# F28M35x/F28M36x UDP Send

## Ports

Not documented in R2025b.

## Parameters

**Remote IP address (255.255.255.255 for broadcast)**
:   Specify the IP address of the remote UDP host for data transmission. For
    broadcasting to all the remote hosts, enter ‘255.255.255.255’.

**Remote IP Port**
:   Specify the port number of the remote UDP host for data transmission.

**Local IP Port (-1 for automatic port assignment)**
:   Enter the port number of the local UDP host for data transmission.

**Wait until previous packet transmitted**
:   Select this check box to transmit a UDP packet, only after the previous packet is
    transmitted to avoid data overlap. Leave the default value ‘-1’ to allow automatic
    port assignment.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Send UDP packets to UDP host

Send UDP packets to a remote UDP host. Use UDP Send block for stateless, connectionless,
and byte oriented data transmission.

You can send one dimensional array of data type uint8, uint16, int16, uint32, int32,
single, or double.
