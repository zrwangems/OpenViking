---
type: simulink-block
title: 'Speed Measurement'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'speedmeasurement'
documentation_source_path: 'ref/speedmeasurement.html'
language: en
---

# Speed Measurement

## Ports

### Input

### **θ** — Angular position of rotor scalar

Angular position of the rotor specified in either radians, degrees, or
per-unit.

**Data Types:** `single` | `double` | `fixed point`

### **Ts** — Sample time after which block executes again scalar

The fixed time interval (in seconds) between every two consecutive instances of
block execution.

#### Dependencies

To enable this port, select the **Advanced Options** >
**Use input port for Discrete step size** parameter.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **⍵** — Angular speed of rotor scalar

Angular speed that the block computes based on the angular position input.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Position unit** — Unit of angular position `Radians` (default) | `Degrees` | `Per unit`

The unit of the angular position `θ`.

### **Position scaling datatype** — Range for mapping input position `uint32` (default) | `uint16` | `uint64`

Range used to map input position internally to fit in the unsigned integer datatype.
For example, the block scales an input in the range `(0 - 2π)` to
`(0 - (232-1))` for uint32
datatype.

### **Speed calculation criteria** — Method of speed calculation `Maximum application speed` (default) | `Speed resolution` | `Time interval for speed calculation`

The speed calculation method used in the block. The selected method determines the
range of the rotor speed that the block can measure.

These parameters change values according to the **Speed calculation
criteria** parameter:

| Parameter name | Maximum application speed | Speed Resolution | Time interval for speed calculation |
| --- | --- | --- | --- |
| **Delays for speed calculation (number of samples)** | `299` | `28` | `28` |
| **Maximum measurable speed (RPM)** | `1000` | `10344.8276` | `10713.2857` |
| **Measurable speed resolution (RPM)** | `4.6566e-07` | `4.9892e-06` | `4.9892e-06` |

### **Discrete step size (s)** — Sample time after which block executes again `100e-6` (default) | scalar

The fixed time interval (in seconds) between every two consecutive instances of
block execution.

These parameters change values according to the **Discrete step size
(s)** parameter value:

- **Delays for speed calculation (number of samples)**
- **Maximum measurable speed (RPM)**
- **Measurable speed resolution (RPM)**

#### Dependencies

To enable this parameter, clear the **Advanced Options** >
**Use input port for Discrete step size** parameter.

### **Maximum application speed (RPM)** — Maximum measurable rotor speed `1000` (default) | scalar

The maximum rotor speed (in rotations per minute) that the block can measure.

These parameters change values according to the **Maximum application speed
(RPM)** parameter value:

- **Delays for speed calculation (number of samples)**
- **Maximum measurable speed (RPM)**
- **Measurable speed resolution (RPM)**

#### Dependencies

To enable this parameter, set **Speed calculation criteria** to
`Maximum application speed`.

### **Speed Resolution (RPM)** — Minimum detectable speed `5e-6` (default) | scalar

The minimum value of change in the `θ` input per unit time that the
block can detect.

These parameters change values according to the **Speed Resolution
(RPM)** parameter value:

- **Delays for speed calculation (number of samples)**
- **Maximum measurable speed (RPM)**
- **Measurable speed resolution (RPM)**

#### Dependencies

To enable this parameter, set **Speed calculation criteria** to
`Speed resolution`.

### **Delays for speed calculation (number of samples)** — Number of angular position samples measured `299` or `28` (default) | scalar

The number of samples of the angular position input that the block measures to
compute the average position value.

These parameters change values according to the **Delays for speed
calculation (number of samples)** parameter value:

- **Maximum measurable speed (RPM)**
- **Measurable speed resolution (RPM)**

**Note**

The maximum limit for **Delays for speed calculation (number of
samples)** parameter is set at 2^30 (or 1073741824). This limit affects the
values of **Maximum measurable speed (RPM)** and **Measurable
speed resolution (RPM)** parameters, and they may not always match the
desired values.

#### Dependencies

To enable this parameter, set **Speed calculation criteria** to
`Time interval for speed calculation`.

### **Maximum measurable speed (RPM)** — Maximum measurable speed `1000` or `10344.8276` or `10713.2857` (default) | scalar

The absolute maximum speed that the block can measure.

This parameter is not configurable and uses a value that is internally computed
using other parameters.

### **Measurable speed resolution (RPM)** — Minimum speed resolution used for speed computation `4.6566e-07` or `4.9892e-06` (default) | scalar

The minimum speed resolution that the block uses for speed computation. It is always
less than or equal to **Speed Resolution (RPM)**.

This parameter is not configurable and uses a value that is internally computed
using other parameters.

### **Speed unit** — Unit of angular speed output `RPM` (default) | `Degrees/Sec` | `Radians/Sec` | `Per unit based on maximum measurable speed` | `Per unit based on dialog`

Unit of the angular speed output.

### **Per unit speed (RPM)** — Speed (in RPM) for per-unit calculation `1000` (default)

Specify the speed in RPM for per-unit calculation.

#### Dependencies

This parameter appears only if `Per unit based on dialog`
is selected for **Speed unit**.

### **Speed data type** — Data type of angular speed output `single` (default) | `double` | `fixed point`

The data type of the angular speed output `⍵`.

**Note**

The Speed Measurement block may occasionally display the warning message
`'Wrap on overflow detected`.`'`

### **Use input port for Discrete step size** — Specify sample step size with input port `off` (default) | `on`

Select this parameter if you want to specify the sample step size using an input
port.

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

This block has a single, default HDL
architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

### R2025a: New input port and block parameters added

The Block Parameters dialog box now includes the **Use input port for Discrete
step size** parameter for you to specify a discrete step size from a separate
input port **Ts**.

## Description

Compute speed from rotor angular position

The Speed Measurement block calculates the angular speed from the angular
position of the rotor by calculating the change in the angular position with respect to
time.
