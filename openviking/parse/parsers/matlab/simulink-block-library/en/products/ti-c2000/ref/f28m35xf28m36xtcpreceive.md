---
type: simulink-block
title: 'F28M35x/F28M36x TCP Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f28m35xf28m36xtcpreceive'
documentation_source_path: 'ref/f28m35xf28m36xtcpreceive.html'
language: en
---

# F28M35x/F28M36x TCP Receive

## Ports

Not documented in R2025b.

## Parameters

**Local IP Port**
:   Enter the IP port number of the local host to receive data.

**Data type**
:   Select the data type of the TCP packet.

**Data size (N)**
:   Enter the data size of the data type you have selected in the **Data
    type** parameter.

**Wait until data received**
:   Select this check box to receive a TCP packet only after the previous packet is
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

Receive TCP packets from TCP host on TCP/IP network

Receive TCP packets from another TCP host over the TCP/IP network. Use TCP Receive block
for connection-oriented, stateful, and stream based data transmission. Also, the TCP Receive
block guarantees the data transmission.

This block outputs data received as an array of the size specified in the **Data
size** parameter.

The status port on the block indicates if the data is good or not.

The different values returned by the status port are as follows:

0 - represents no error in data reception

1 - represents an error in data reception.
