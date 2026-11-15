---
type: simulink-block
title: 'F28M35x/F28M36x UDP Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f28m35xf28m36xudpreceive'
documentation_source_path: 'ref/f28m35xf28m36xudpreceive.html'
language: en
---

# F28M35x/F28M36x UDP Receive

## Ports

Not documented in R2025b.

## Parameters

**Local IP Port**
:   Enter the local UDP host IP port to receive UDP packets.

**Remote IP address (0.0.0.0 for accepting all)**
:   Enter the IP address of the remote UDP host in 0.0.0.0 format to receive UDP
    packets. For accepting data from any valid IP address, enter ‘0.0.0.0’.

**Data type**
:   Select the data type of the UDP packets.

**Data size (N)**
:   Enter the data size of the data type you have selected in the **Data
    type** parameter.

**Wait until data received**
:   Select this check box to receive a UDP packet only after the previous packet is
    received to avoid data overlap.

**Sample time**
:   Specify how often this block should read the port buffer. Enter a value greater
    than zero.

    This value defaults to a sample time of 0.01 seconds. Smaller values require the
    processor to complete the same number of instructions in less time, which can cause
    task overruns.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Receive UDP packets from the specified UDP host

Receive UDP packets from the specified remote host. Use the UDP Receive block to output
the UDP packets received as one dimensional array of size defined in **Data
size** parameter. Use UDP Receive block for stateless, connectionless, and byte
oriented data transmission.

You can specify the remote UDP host in the **Remote IP address (0.0.0.0. for
accepting all)** parameter to send the UDP packets to the local UDP host
specified in the **Local IP Port** parameter.

The status port on the block indicates if the data is good or not.

The different values returned by the status port are as follows:

0 - represents no error in data reception

1 - represents an error in data reception.
