---
type: simulink-block
title: 'Software Watchdog Timer'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'softwarewatchdogtimer'
documentation_source_path: 'ref/softwarewatchdogtimer.html'
language: en
---

# Software Watchdog Timer

## Ports
```yaml
ports:
- name: Restart
  summary: Pulse to restart watchdog timer counter scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Status
  summary: Watchdog timer status scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **Restart** — Pulse to restart watchdog timer counter scalar

The pulse (true value) that restarts the watchdog timer counter. The counter
resumes counting when the pulse falls (false value).

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Status** — Watchdog timer status scalar

The watchdog timer status indicated as one of the following:

- True indicates that the counter value is less than the value of the
  **Maximum count** parameter.
- False indicates that the counter value is equal to the value of the
  **Maximum count** parameter and the block has stopped the
  counter.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Maximum count
  summary: Maximum limit of watchdog timer value 10 (default) | scalar
  group: ''
- name: Counter data type
  summary: Data type of Status output uint8 (default) | uint16 | uint32
  group: ''
```

### **Maximum count** — Maximum limit of watchdog timer value `10` (default) | scalar

The maximum limit of the watchdog timer counter value that causes the block to stop
the counter and turn the watchdog timer status to false.

### **Counter data type** — Data type of `Status` output `uint8` (default) | `uint16` | `uint32`

The data type of the watchdog timer status output.
## Libraries

Motor Control Blockset / Sensor Decoders

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Output true until counter reaches maximum count limit

The Software Watchdog Timer block increments the counter value until either
the block receives a `Restart` input pulse, or the count reaches the value of
the **Maximum count** parameter.

On receiving the `Restart` pulse, the block restarts the counter and
starts incrementing the counter value again when the `Restart` pulse
falls.

The block maintains the true `Status` output until the counter value
remains less than the value of **Maximum count** parameter. When the counter
reaches **Maximum count**, the block stops the counter and turns the
`Status` false.
