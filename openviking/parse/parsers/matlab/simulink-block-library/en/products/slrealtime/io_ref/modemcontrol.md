---
type: simulink-block
title: 'Modem Control'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'modemcontrol'
documentation_source_path: 'io_ref/modemcontrol.html'
language: en
---

# Modem Control

## Ports

### Input

### **RTS** — Level-sensitive signal for setting ready-to-send line `double`

The behavior of the block is:

- `RTS > 0.5` — The block asserts the RTS
  control bit to `true`. The output goes to a
  positive voltage.
- `RTS ≤ 0.5` — The block asserts the RTS
  control bit to `false`. The output goes to a
  negative voltage.

#### Dependency

If the **RTS** parameter is
`off`, this input has
no
effect.

### **DTR** — Level-sensitive signal for setting data-terminal-ready line `double`

The behavior of the block is:

- `DTR > 0.5` — The block asserts the DTR
  control bit to `true`. The output goes to a
  positive voltage.
- `DTR ≤ 0.5` — The block asserts the DTR
  control bit to `false`. The output goes to a
  negative voltage.

#### Dependency

If the **DTR** parameter is
`off`, this input has
no
effect.

## Parameters

### **RTS** — Enable control of RTS line for serial device `on` (default) | `off`

Select this check box to control the RTS line for this board.

#### Programmatic Use

```
rts
```

### **DTR** — Enable control of DTR line for serial device `on` (default) | `off`

Select this check box to control the DTR line for this board.

#### Programmatic Use

```
dtr
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

Control state of RTS and DTR output lines on serial port

The Modem Control block controls the state of either or both of the
Request To Send (RTS) and Data Terminal Ready (DTR) output lines of the serial port on
the Speedgoat® target computer. To choose which output lines to control, select the
**RTS** and **DTR** parameters.
