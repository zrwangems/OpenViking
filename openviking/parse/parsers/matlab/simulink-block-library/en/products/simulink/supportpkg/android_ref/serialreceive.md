---
type: simulink-block
title: 'Serial Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'serialreceive'
documentation_source_path: 'supportpkg/android_ref/serialreceive.html'
language: en
---

# Serial Receive

## Ports

Not documented in R2025b.

## Parameters

### **Data type** — Type of data `int32` (default)

Select the data type of the data you want to receive on the serial port.
You can receive int8, uint8, int16, uint16, int32, uint32, double, single,
or boolean data type on the serial port.

### **Data length** — Value of data length `1` (default)

Enter the number of data elements to receive on the serial port.

### **Sample time** — Block sample time `0.1` (default)

Specify how often this block reads the serial port buffer. Enter a value
greater than zero. This value defaults to a sample time of
`0.1` second. The minimum value is
`0.001` second.

Smaller values require the processor to complete the same number of
instructions in less time, which can cause task overruns.

## Libraries

Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Receive an [Nx1] array of data on the serial port and write it to the data block output. When data is not available, write 0 to the data block output

Get an [Nx1] array of data on the specified serial port and write to the Data block
output.

The Serial Receive block has two outputs, **Data** and
**Status**.

When data is available:

- The **Data** block output emits data from the serial receive
  buffer.
- The **Status** block output emits
  `1`.

When data is not available:

- The **Data** block output emits `0`.
- The **Status** block output emits
  `0`.

The **Data** block outputs the datatypes, int8, uint8, int16, uint16,
int32, uint32, double, single, or boolean based on the selected **Data
type** parameter value on the block. The default data type is int32.

The **Status** block output emits int values. You can use the Status
block output to determine whether a value of `0` emitted by the
**Data** port is data, or an indication that no data was
received.

During simulation this block outputs `0`.

**Note**

Only one Serial Transmit and one Serial Receive
blocks are allowed in a model.
