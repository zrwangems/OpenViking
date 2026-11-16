---
type: simulink-block
title: 'Modem Status'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232 / Mainboard'
documentation_page: 'modemstatus'
documentation_source_path: 'io_ref/modemstatus.html'
language: en
---

# Modem Status

## Ports

### Output

### **CTS** — Status of clear to send line `true` | `false`

If `true`, the modem is ready to receive data.

#### Dependency

To make this output visible, select the **CTS**
parameter.

### **DSR** — Status of data set ready line `true` | `false`

If `true`, the modem is ready to send and receive
data.

#### Dependency

To make this output visible, select the **DSR**
parameter.

### **DCD** — Status of data carrier detect line `true` | `false`

If `true`, the modem is receiving a carrier from a
remote device.

#### Dependency

To make this output visible, select the **DCD**
parameter.

## Parameters

### **CTS** — Enables clear to send status output `on` (default) | `off`

Select this check box to monitor the CTS line of the modem.

Selecting this parameter makes the `CTS` port
visible.

#### Programmatic Use

```
cts
```

### **DSR** — Enables data set ready status output `on` (default) | `off`

Select this check box to monitor the DSR line of the modem.

Selecting this parameter makes the `DSR` port
visible.

#### Programmatic Use

```
dsr
```

### **DCD** — Enables data carrier detect status output `on` (default) | `off`

Select this check box to monitor the DCD line of the modem.

Selecting this parameter makes the `DCD` port
visible.

#### Programmatic Use

```
dcd
```

### **Sample time** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample time. `-1` means
that sample time is inherited.

#### Programmatic Use

```
sampletime
```

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

## Libraries

Simulink Real-Time / RS232 / Mainboard

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Return state of modem control lines

The Modem Status block reads the state of the input modem control lines
on the Speedgoat® target computer.

This block has outputs of type `Boolean`. If the input voltage is
positive, the output is true. If the input voltage is negative, the output is
false.
