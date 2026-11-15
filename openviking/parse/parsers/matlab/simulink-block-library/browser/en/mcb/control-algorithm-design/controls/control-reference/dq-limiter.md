---
type: simulink-block
title: 'DQ Limiter'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Control Reference'
documentation_page: 'dqlimiter'
documentation_source_path: 'ref/dqlimiter.html'
language: en
---

# DQ Limiter

## Ports

### Input

### **dref** — Reference *d*-axis voltage (or current) scalar

Reference voltage (or current) value along the *d*-axis of the
rotating *dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **qref** — Reference *q*-axis voltage (or current) scalar

Reference voltage (or current) value along the *q*-axis of the
rotating *dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **satMethod** — Saturation technique scalar

Saturation method that the block uses to initiate saturation. The port accepts one
of the following integer values:

- 1 – Prioritize D-axis
- 2 – Prioritize Q-axis
- Any other positive integer – D-Q equivalence method

#### Dependencies

To enable this port, select `Input port` for the
**Saturation method** parameter.

**Data Types:** `uint16`

### **satLim** — Saturation limit scalar

Saturation limit value that the block uses to initiate saturation. The port
accepts values greater than or equal to 0.

#### Dependencies

To enable this port, select `Input port` for the
**Saturation limit** parameter.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **dsat** — Saturated *d*-axis voltage (or current) scalar

Saturated voltage (or current) value along the *d*-axis of the
rotating *dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **qsat** — Saturated *q*-axis voltage (or current) scalar

Saturated voltage (or current) value along the *q*-axis of the
rotating *dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **magref** — Unsaturated peak value of block inputs scalar

Unsaturated peak value of the input voltages (or current).

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Saturation method** — Saturation method selection technique `Specify via dialog` (default) | `Input port`

Select whether the block should use dialog box or input port to specify the
saturated method.

#### Programmatic Use

```
satMethodInputType
```

### **Saturation method selected** — Saturation method used by block `D-Q equivalence` (default) | `Prioritize D axis` | `Prioritize Q axis`

Select the saturation method that the block should use.

#### Dependencies

To enable this parameter, set **Saturation method** to
`Specify via dialog`.

#### Programmatic Use

```
satMethodSelected
```

### **Saturation limit** — Saturation limit selection technique `Specify via dialog` (default) | `Input port`

Select whether the block should use dialog box or input port to specify the
saturated limit.

#### Programmatic Use

```
satLimitInputType
```

### **Saturation limit value** — Phase voltage (or current) peak limit `1` (default) | scalar

The maximum magnitude of voltage (or current) above which the block outputs are
limited.

D−Q saturation limit (current) is usually the rated current of the motor. When you work with the
Per-Unit system (PU), you should convert the rated current of the motor to Per-Unit
value with respect to the base current.

D−Q saturation limit (voltage) is usually the maximum phase voltage supplied by the inverter.
Generally it is Vdc3 for Space Vector PWM and Vdc2 for Sinusoidal PWM, where Vdc is the DC link
voltage of the inverter.

**Note**

You can enter either per unit or SI unit voltage (or current) value in this
parameter (unit of the entered value should be same as that of the
*dref* and
*qref* inputs). For optimum
performance, we recommend that you provide a per unit value.

#### Dependencies

To enable this parameter, set **Saturation limit** to
`Specify via dialog`.

#### Programmatic Use

```
Vmax
```

## Libraries

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**Supported Block Parameters**

For HDL code generation with the DQ Limiter block, set these
parameters:

- Set **Saturation method** to `Specify via
  dialog`
- Set **Saturation method selected** to `D-Q
  equivalence`
- Set **Saturation limit** to `Specify via
  dialog`

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **FlattenHierarchy** | Remove DQ Limiter block hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Saturate voltages (or current) in the dq reference frame

The DQ Limiter block generates saturated values of the input voltages (or
current) in the *dq* reference frame, depending on the specified saturation
limit and the selected method of saturation.

The block accepts reference values of *d* and *q* axis
voltages (or current) and outputs the corresponding saturated values. The block also provides
the unsaturated peak value of the reference *dq* voltages (or current), which
you can use to enable field weakening control.

**Note**

The block supports a fixed-point data type size up to 128 bits.

### Equations

These equations describe the computation of saturated *dq* voltage (or
current) values by the block.

**For DQ equivalence:**

magref=(dref)2+(qref)2

When magref>xmax.

- dsat=drefmagref×xmax
- qsat=qrefmagref×xmax

When magref≤xmax.

- dsat=dref
- qsat=qref

Where, *xmax* is the saturation limit.

**When D-axis is prioritized:**

magref=(dref)2+(qref)2

dsat=min(max(dref,−xmax),xmax)qsat=sign(qref)×min(|qref|,|xmax2−(dsat)2|)

Where, *xmax* is the saturation limit.

**When Q-axis is prioritized:**

magref=(dref)2+(qref)2

qsat=min(max(qref,−xmax),xmax)dsat=sign(dref)×min(|dref|,|xmax2−(qsat)2|)

Where, *xmax* is the saturation limit.
