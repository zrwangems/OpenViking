---
type: simulink-block
title: 'Radio Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Radio'
documentation_page: 'radioreceive'
documentation_source_path: 'microbit/ref/radioreceive.html'
language: en
---

# Radio Receive

## Ports

### Output

### **Data** — Received data vector

At each sample time, the port outputs received data as an N-by-1 array
of the type specified in the Data type
parameter and size specified in the **Data length (N)**
parameter.

### **Status** — Status of received data scalar

The status port outputs one of these values:

- `1`—Data is received.
- `0`—No data is received.
- `–1`—Data is corrupted during
  reception.

## Parameters

### **Channel number (1–100)** — Channel selected to receive data `1` (default) | any integer from 1 to 100, inclusive

The channel number at which you want to receive data.

**Note**

The transmitter and receiver must be set to the same channel
number.

### **Data type** — Type of data to be received `double` (default) | `string` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

The type of data the block receives. The size of each element depends on
its data type.

### **Data length (N)** — Number of data units to be received `10` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

The number of data units received at each sample time. The range of
permitted units is dependent on the data type, as summarized in the
table:

| Data type | Range |
| --- | --- |
| double | 1–31 |
| single | 1–63 |
| int8 | 1–254 |
| uint8 | 1–254 |
| int16 | 1–127 |
| uint16 | 1–127 |
| int32 | 1–63 |
| uint32 | 1–63 |
| boolean | 1–254 |

### **Sample time** — Interval at which the block reads data `0.2` (default) | `-1` | any nonnegative value

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

## Libraries

Simulink Coder Support Package for BBC micro:bit/Radio

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Receive data from micro:bit devices via radio

The Radio Receive block receives data from other micro:bit devices
through a wireless connection.
