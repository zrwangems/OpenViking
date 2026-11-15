---
type: simulink-block
title: 'Legacy Serial Setup'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'legacyserialsetup'
documentation_source_path: 'io_ref/legacyserialsetup.html'
language: en
---

# Legacy Serial Setup

## Ports

Not documented in R2025b.

## Parameters

### **Serial port** — Port that is being accessed `Legacy Serial Port 1` (default) | .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

Specify the serial port for communications.

If using USB-to-serial adapters, the target computer
detects these adapters as `serusb1`, `serusb2`, and so
on in the order that the adapters are connected to the serial devices.

The order of port assignment is retained through the power cycle of the target
computer or serial device if there is no change in the connections to the ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `port` |

### **Baud rate** — Select serial port baud rate `115200` (default) | `57600` | `38400` | `19200` | `9600` | `4800` | `2400` | `1200` | `600` | `300` | `110`

Use this value to select the serial port baud rate.

#### Programmatic Use

```
baud
```

### **Number of data bits** — Select serial port data bits `8` (default) | `7` | `6` | `5`

Use this value to select the number of serial port data bits.

#### Programmatic Use

```
width
```

### **Number of stop bits** — Select serial port stop bits `1` (default) | `2`

Use this value to select the number of serial port stop bits.

#### Programmatic Use

```
nstop
```

### **Parity** — Select serial port parity `None` (default) | `Even` | `Odd` | `Mark` | `Space`

Use this value to select serial port parity.

#### Programmatic Use

```
parity
```

### **Enable auto RTX/CTS** — Select serial port RTX/CTS mode `off` (default) | `on`

Use this value to select the serial port RTX/CTS mode.

#### Programmatic Use

```
ctsmode
```

## Libraries

Simulink Real-Time / RS232 / Mainboard

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

### R2021b: USB to Serial for RS232 Blocks

The RS232 mainboard blocks support connecting USB serial adapter ports. The
`Serial port` parameter of the Legacy Serial Read
block, Legacy Serial Write block, Legacy Serial Setup block,
Legacy Serial Port block, and Legacy Serial Port F block
means that you can select a `USB Serial Port` or a
`Legacy Serial Port`.

## Description

Set up baseboard serial communications

The Legacy Serial Setup block sets up baseboard serial communications on
the Speedgoat® target computer.

For more information, see RS-232 Serial Communication and RS-232 Legacy Drivers.
