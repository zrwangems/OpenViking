---
type: simulink-block
title: 'EDSADC'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'edsadc'
documentation_source_path: 'infineonaurixtc3x/ref/edsadc.html'
language: en
---

# EDSADC

## Ports

### Output

### **result** — Voltage of analog input pin `scalar` | `vector`

When you set the **Result type** parameter to
`Voltage`, the block outputs the measured voltage
as a single-precision floating-point number. When you set the **Result
type** parameter to `Counts`, the block
outputs the voltage as a 16-bit count formatted as an `N`-by-1
array, where `N` varies based on the parameter values, as
shown in this table.

| Read Mode | FIFO | Timestamp | Valid FIFO Level | Size of Result |
| --- | --- | --- | --- | --- |
| Number of 16-bit data to read: **1** | Disable | Disable | Stage 1 | 1-by-1 |
| Enable | Disable | Stage 1 | 1-by-1 |
| Stage 2 | 2-by-1 |
| Stage 3 | 3-by-1 |
| Stage 4 | 4-by-1 |
| Enable | Stage 2 | 1-by-1 |
| Stage 3 | 2-by-1 |
| Stage 4 | 3-by-1 |
| Number of 16-bit data to read: **2** | Enable | Disable | Stage 2 | 2-by-1 |
| Stage 4 | 4-by-1 |
| Enable | Stage 4 | 3-by-1 |

**Data Types:** `uint16` | `int16` | `single`

### **aux\_result** — Auxiliary result as signed or unsigned 16-bit value `scalar`

The block outputs the auxiliary result as a 16-bit signed value or a
single-precision floating-point number, depending on the choice of
**Result type** parameter. Use this port to obtain to
obtain immediate result of conversion, bypassing the offset and integrator
filter stages during conversion.

#### Dependencies

To enable this port, select the **Auxiliary result**
parameter.

**Data Types:** `int16` | `single`

### **timestamp** — Timestamp of 16-bit counter value `scalar`

The block outputs the current value of the 16-bit timestamp counter.

#### Dependencies

To enable this port, select the **Enable timestamp**
parameter.

**Data Types:** `uint16`

## Parameters

### **Enable timestamp** — Option to enable timestamp output `off` (default) | `on`

Select this parameter to enable the **timestamp** output
port..

Selecting this parameter also enables options in the
**Timestamp** tab and Timestamp event (under
**Events** tab) in the EDSADC Peripheral Configuration tool.

**Note**

Configure the trigger signal before selecting the **Enable
timestamp** parameter, since the timestamp is always associated
with a trigger signal.

### **Auxiliary result** — Enable auxiliary result output `off` (default) | `on`

Select this parameter to enable the **aux\_result** output
port. The block outputs the auxiliary result as a single-precision floating-point
number or a signed 16-bit value.

Selecting this parameter enables the related parameters in the EDSADC Peripheral Configuration tool.

### **Enable FIFO** — Option to enable FIFO register `off` (default) | `on`

Select this parameter to enable the FIFO register.

### **Number of 16 bit data to read** — Number of 16-bit output data to read `1` (default) | `2`

Specify the number of 16 bit output data to read.

Specify `2` to fetch the data faster from the FIFO
register.

#### Dependencies

To enable the **Number of 16 bit data to read** parameter,
select the **Enable FIFO** parameter.

### **FIFO level** — Level of FIFO register `4` (default) | `3` | `2` | `1`

Level of the FIFO register for data transfer.

The option `1` appears if you disable **Enable
Timestamp**

#### Dependencies

To enable the **FIFO level** parameter, select the
**Enable FIFO** parameter.

### **Result type** — Type of the conversion result `Counts` (default) | `Voltage`

Specify the type of the output at the **result** port.

### **Main result type** — Data type of the result `Signed` (default) | `Unsigned`

Specify the data type of the output at **result** port.

#### Dependencies

To enable this parameter, set the **Result type** parameter
to `Counts`.

### **Sample time** — Frequency at which block reads input analog pin(s) `-1` (default) | `scalar`

Specify in seconds how often the block should read the analog
pin(s).

When you specify this parameter as `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Measure voltage of analog input pin using delta-sigma conversion

The EDSADC block measures the voltage of an analog input pin using delta-sigma
conversion.

It outputs the voltage as a single-precision floating-point number, unsigned, or signed
16-bit count formatted as an N-by-1 array. The delta-sigma conversion process can utilize
either the on-chip modulator or the external modulator, which you select in the EDSADC
Peripheral Configuration tool. The block provides the conversion results
continuously based on the filter parameters that you specify when configuring the EDSADC
peripheral in the Hardware Mapping tool.
