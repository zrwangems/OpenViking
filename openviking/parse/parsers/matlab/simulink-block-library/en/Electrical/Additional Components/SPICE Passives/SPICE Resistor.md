---
type: simulink-block
title: 'SPICE Resistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Passives'
documentation_page: 'spiceresistor'
documentation_source_path: 'ref/spiceresistor.html'
language: en
---

# SPICE Resistor

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the SPICE resistor positive
voltage terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the SPICE resistor negative
voltage terminal.

## Parameters

### Resistance

### **Device scale factor, SCALE** — Device scale factor `1.0` (default)

Number of parallel resistors that the block represents. This value
multiplies the output current.

### **Resistor parameterization** — Parameterization options `Use specified resistance` (default) | `Calculate from process information`

Select one of the following options for specifying the resistor value:

- `Use specified resistance`
  — Provide the resistance value directly.
- `Calculate from process
  information` — Provide process
  parameters that the block uses to calculate the resistance
  value.

  When you select this option, the block calculates the
  resistance using the following equation:

  R=RSH\*(LENGTH−NARROW)(WIDTH−NARROW)

  where:

  - *RSH* is the **Sheet
    resistance, RSH** parameter value.
  - *LENGTH* is the
    **Resistor length, LENGTH**
    parameter value.
  - *WIDTH* is the
    **Resistor width, WIDTH**
    parameter value.
  - *NARROW* is the
    **Etch narrowing, NARROW**
    parameter value.

### **Resistance, R** — Resistance `0` `Ohm` (default)

Resistance value.

#### Dependencies

This parameter is visible only when you select `Use
specified resistance` for the **Resistor
parameterization** parameter.

### **Sheet resistance, RSH** — Resistance per square `0` `Ohm` (default)

Resistance per square of the resistor.

#### Dependencies

This parameter is visible only when you select
`Calculate from process information`
for the **Resistor parameterization**
parameter.

### **Resistor length, LENGTH** — Resistor length `1e-6` `m` (default)

Length dimension of the resistor.

#### Dependencies

This parameter is visible only when you select
`Calculate from process information`
for the **Resistor parameterization**
parameter.

### **Resistor width, WIDTH** — Resistor width `1e-6` `m` (default)

Width dimension of the resistor.

#### Dependencies

This parameter is visible only when you select
`Calculate from process information`
for the **Resistor parameterization**
parameter.

### **Etch narrowing, NARROW** — Etch narrowing `0` `m` (default)

Amount by which the resistor length and width are reduced due to side
etching.

#### Dependencies

This parameter is visible only when you select
`Calculate from process information`
for the **Resistor parameterization**
parameter.

### Temperature

### **Model temperature dependence using** — Temperature dependence parameterization `Device temperature` (default) | `Fixed temperature`

Select one of the following options for modeling the resistor
temperature dependence:

- `Device temperature` — Use
  the device temperature, which is the
  **Temperature** parameter value (from
  the Environment Parameters
  block, if one exists in the circuit, or the default value
  for this block otherwise) plus the **Offset local
  circuit temperature, TOFFSET** parameter
  value.
- `Fixed temperature` — Use
  a temperature that is independent of the circuit temperature
  to model temperature dependence.

### **First order temperature coefficient, TC1** — First order temperature coefficient `0` `1/K` (default)

Coefficient for the linear term in the equation that the block uses to
adjust the specified or calculated resistance value for
temperature.

### **Second order temperature coefficient, TC2** — Second order temperature coefficient `0` `1/K^2` (default)

Coefficient for the quadratic term in the equation the block uses to
adjust the specified or calculated resistance value for
temperature.

### **Offset local circuit temperature, TOFFSET** — Offset local circuit temperature `0` `K` (default)

The amount by which the resistor temperature differs from the circuit
temperature.

#### Dependencies

This parameter is visible only when you select `Device
temperature` for the **Model temperature
dependence using** parameter.

### **Fixed circuit temperature, TFIXED** — Fixed circuit temperature `300.15` `K` (default)

The temperature at which to simulate the resistor.

#### Dependencies

This parameter is visible only when you select `Fixed
temperature` for the **Model temperature
dependence using** parameter.

### **Parameter extraction temperature, TMEAS** — Parameter extraction temperature `300.15` `K` (default)

The temperature at which the resistor parameters were measured.

## Libraries

Simscape / Electrical / Additional Components / SPICE Passives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Model SPICE-compatible resistor

The SPICE Resistor block represents a SPICE-compatible
resistor. You can specify the resistance in one of the following ways:

- As a resistance value
- As process information that the block uses to calculate a resistance
  value

The block models temperature dependence. There are two ways to specify the resistor temperature:

- When you select `Device temperature` for the
  **Model temperature dependence using** parameter, the
  resistor temperature is

  T=TC+TO

  where:

  - *TC* is the
    **Temperature** parameter value from the
    Environment Parameters block.
    If this block doesn't exist in the circuit,
    *TC* is the
    default value of this parameter.
  - *TO* is the
    **Offset local circuit temperature,
    TOFFSET** parameter value.
- When you select `Fixed temperature` for the
  **Model temperature dependence using** parameter, the
  resistor temperature is the **Fixed circuit temperature,
  TFIXED** parameter value.

The block adjusts the specified or calculated resistance value for
temperature using the following equation:

*R* =
*R0*(1+*TC1*(*T*–*Tnom*)+*TC2*(*T*–*Tnom*)2)

Where

- *R0* is the specified or
  calculated resistance value.
- *TC1* is the **First order temperature
  coefficient, TC1** parameter value.
- *TC2* is the **Second order temperature
  coefficient, TC2** parameter value.
- *Tnom* is the **Parameter
  extraction temperature, TMEAS** parameter value.
