---
type: simulink-block
title: 'Cycler'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cyclers'
documentation_page: 'cycler'
documentation_source_path: 'ref/cycler.html'
language: en
---

# Cycler

## Ports

### Input

### **i** — Current, A physical signal

Physical signal input port associated with the current that passes
through the cycler.

#### Dependencies

To enable this port, set the **Configuration**
parameter to either `Galvanostat, specify
current` or `Cycler, specify current or
voltage`.

### **v** — Voltage, V physical signal

Physical signal input port associated with the voltage across the
cycler.

#### Dependencies

To enable this port, set the **Configuration**
parameter to either `Potentiostat, specify
voltage` or `Cycler, specify current or
voltage`.

### **c** — Control, unitless physical signal

Physical signal input port that controls the behavior of the
cycler.

#### Dependencies

To enable this port, set the **Configuration**
parameter to `Cycler, specify current or
voltage`.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal of
the cycler.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal of
the cycler.

## Parameters

### **Current sign convention** — Sign convention option for current `Positive for device discharge (IEC 62660)` (default) | `Positive for device charge`

Convention option for the sign of the current.

### **Configuration** — Block configuration `Cycler, specify current or voltage` (default) | `Galvanostat, specify current` | `Potentiostat, specify voltage`

Option to configure the behavior of the block.

## Libraries

Simscape / Battery / Cyclers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Ideal galvanostat, potentiostat, or cycler

The Cycler block implements an ideal galvanostat,
potentiostat, or a cycler.

To configure this block as a galvanostat, set the **Configuration**
parameter to `Galvanostat, specify current`. The
Cycler block then represents an ideal current source
or sink that is powerful enough to maintain the specified current through it regardless
of the voltage across it. The output current is the value at the physical signal port,
**i**.

To configure this block as a potentiostat, set the **Configuration**
parameter to `Potentiostat, specify voltage`. The
Cycler block then represents an ideal voltage source
that is powerful enough to maintain the specified voltage at its output regardless of
the current passing through it. The output voltage is the value at the physical signal
port, **v**.

To configure this block as a cycler, set the **Configuration**
parameter to `Cycler, specify current or voltage`. When the
value at the control physical signal port, **c**, is equal to
`0`, the cycler turns off. When the value at the control physical
signal port, **c**, is equal to `1`, this block
represents a galvanostat. When the value at the control physical signal port,
**c**, is equal to `2`, this block represents a
potentiostat.

This table shows the overall behavior of the Cycler
block:

| Configuration | | | | |
| --- | --- | --- | --- | --- |
| `Galvanostat, specify current` | `Potentiostat, specify voltage` | `Cycler, specify current or voltage` | | |
| Value at input port **c** | | |
| 0 | 1 | 2 |
| The Cycler block represents an ideal current source. | The Cycler block represents an ideal voltage source. | The Cycler block turns off. | The Cycler block represents a galvanostat. | The Cycler block represents a potentiostat. |
