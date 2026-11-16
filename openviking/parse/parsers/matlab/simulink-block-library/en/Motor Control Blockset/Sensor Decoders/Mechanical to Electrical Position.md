---
type: simulink-block
title: 'Mechanical to Electrical Position'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'mechanicaltoelectricalposition'
documentation_source_path: '../mcb/ref/mechanicaltoelectricalposition.html'
language: en
---

# Mechanical to Electrical Position

## Ports

### Input

### **θm** — Mechanical position of rotor scalar

The mechanical position of rotor (as output by the rotor position sensor) in
either radians (0 to 2π), degrees (0 to 360), or per unit (0 to 1).

**Data Types:** `single` | `double` | `fixed point`

### **Npp** — Number of pole pairs available in motor scalar

Number of pole pairs available in the motor.

#### Dependencies

To enable this port, set the **Pole pairs input** parameter to
`Input port`.

**Data Types:** `single` | `double` | `fixed point`

### **Offset** — Mechanical position offset scalar

The amount by which the electrical zero of the rotor deviates from the mechanical
zero position. Unit of offset is identical to the unit of the mechanical position
input.

#### Dependencies

To enable this port, set **Specify offset via** to
`Input port`.

**Data Types:** `single` | `double` | `fixed point`

**Note**

The values that you specify at all the input ports should have the same data
type.
### Output

### **θe** — Electrical position of rotor scalar

The electrical position of the rotor with a range that is identical to that of the
mechanical position input. Data type of the electrical position is identical to that
of the input.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Pole pairs input** — Method to specify number of pole pairs available in motor `Specify via dialog` (default) | `Input port`

The method you want to use to specify the number of pole pairs available in the
motor. Select `Input port` to enable and use the input port
**Npp**. Select `Specify via
dialog` to provide the number of pole pairs using the dialog box.

### **Number of pole pairs** — Number of pole pairs available in motor `4` (default) | scalar

Number of pole pairs available in the motor.

#### Dependencies

To enable this parameter, set the **Pole pairs input** parameter
to `Specify via dialog`.

### **Input mechanical angle unit** — Unit of mechanical position of rotor `Per unit` (default) | `Radians` | `Degrees`

Unit of the mechanical position of the rotor.

### **Offset input type** — Method to specify offset `Input port` (default) | `Specify via dialog`

Method to specify the mechanical position offset.

- Select `Input port` to enable and use the input port
  **Offset**.
- Select `Specify via dialog` to enable the
  **Mechanical offset** parameter and provide the offset
  value.

### **Mechanical offset** — Value of mechanical position offset `0` (default) | scalar

Specify the mechanical position offset value in this parameter. The unit of the
offset must be identical to the unit of the mechanical position input.

#### Dependencies

To enable this parameter, set **Offset input type** to
`Specify via dialog`.

### **Input data type** — Data type of input ports `single` (default) | `double` | `fixed point`

The data type that you want to use for the input ports.

**Note**

If you select fixed point input data type and provide fixed point values to the
input ports, the block runs faster when deployed on hardware.

## Libraries

Motor Control Blockset / Sensor Decoders Motor Control Blockset HDL Support / Sensor Decoders

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Compute electrical position of rotor from mechanical position

The Mechanical to Electrical Position block computes the electrical
position of rotor by using its mechanical position, mechanical offset value, and the number of
pole-pairs.
