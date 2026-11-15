---
type: simulink-block
title: 'Position Compensation'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Signal Management'
documentation_page: 'positioncompensation'
documentation_source_path: 'ref/positioncompensation.html'
language: en
---

# Position Compensation

## Ports

### Input

### **θin** — Position input value scalar

Position input value that needs offset correction. This port supports the
following range of values:

- -2π to +2π radians
- 0 to 1 per-unit
- -360 to +360 degrees

**Data Types:** `single` | `double` | `fixed point`

### **ϕ** — Position offset scalar

Externally computed position offset value. This value must have same unit as that
of *θin* input. This port supports the
following range of values:

- -2π to +2π radians
- 0 to 1 per-unit
- -360 to +360 degrees

#### Dependencies

To enable this port, set **Nature of offset** parameter to
`External delay`.

**Data Types:** `single` | `double` | `fixed point`

### **ω** — Angular velocity scalar

Externally computed angular velocity. This value represents the change in the
*θin* input.

#### Dependencies

To enable this port, set **Nature of offset** parameter to
`Sample delay`, `High-pass filter
delay`, or `Low-pass filter delay`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **θout** — Position output value scalar

Position output value that is corrected for offset.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Nature of offset** — Type of offset `Sample delay` (default) | `Constant delay` | `External delay` | `High-pass filter delay` | `Low-pass filter delay`

Type of delay or offset in the system that you want to compensate for. Select one of
the following values:

- Constant delay — Compensate for a fixed delay or offset.
- External delay — Compensate for a constant delay using an externally computed
  position offset value.
- Sample delay — Compensate for the delay based on a discrete step size or block
  execution time.
- High-pass filter delay — Compensate for delay from first-order Butterworth
  highpass filter using a cutoff frequency value.
- Low-pass filter delay — Compensate for delay from first-order Butterworth
  lowpass filter using a cutoff frequency value.

### **Offset value** — Position offset value `0.1` (default) | scalar

Position offset for constant delay in a system.

#### Dependencies

To enable this parameter, set **Nature of offset** to
`Constant delay`.

### **Number of sample delay** — Number of block execution time samples `1` (default) | scalar

Number of block execution time samples that the block uses for position offset
compensation.

#### Dependencies

To enable this parameter, set **Nature of offset** to
`Sample delay`.

### **Discrete step size (s)** — Sample time after which block executes again `50e-6` (default) | scalar

The fixed time interval (in seconds) between consecutive instances of block
execution.

#### Dependencies

To enable this parameter, set **Nature of offset** to
`Sample delay`.

### **Cut-off frequency (Hz)** — Filter cutoff frequency `9.578` (default) | scalar

Cutoff frequency of the first-order Butterworth highpass or lowpass filter.

#### Dependencies

To enable this parameter, set **Nature of offset** to
`High-pass filter delay` or `Low-pass filter
delay`.

### **Position unit** — Unit of position input `Radians` (default) | `Degrees` | `Per unit`

Unit of the position input *θin*.

### **Speed unit** — Unit of angular velocity input `RPM` (default) | `Degrees/Sec` | `Radians/Sec` | `Per unit`

Unit of the angular velocity input *ω*.

#### Dependencies

To enable this parameter, set **Nature of offset** to
`Sample delay`, `High-pass filter
delay`, or `Low-pass filter delay`.

### **Maximum application speed (RPM)** — Upper limit of angular velocity `4000` (default) | scalar

Upper limit or the maximum possible value for the angular velocity input
*ω*, in RPM.

#### Dependencies

To enable this parameter, set **Nature of offset** to
`Sample delay`, `High-pass filter
delay`, or `Low-pass filter delay`.

## Libraries

Motor Control Blockset / Signal Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2022b**

## Description

Compensate for position offset due to different types of delays

The Position Compensation block compensates for position offset due to different types of
delays in a system.

Motor control algorithms can introduce offsets in the computed position because of
different algorithmic entities such as delays and filters. These offsets affect accuracy in
motor control algorithms such as the field-oriented control (FOC) and direct-torque control
(DTC). You can use this block to compensate for the offsets in the motor control
algorithms.

The block uses the following computations for a sample delay compensation.

Offset introduced by delay = Applied compensation =(− Sample time) × (Number of delay) × (angular velocity) radians

The block uses the following computations for a first-order Butterworth highpass and
lowpass filter compensation.

- For a highpass filter:

  Phase offset=π2−arctan(ωspeedωcutoff)=arctan(ωcutoffωspeed)

  Phase compensation=−arctan(ωcutoffωspeed)
- For lowpass filter:

  Phase offset=−arctan(ωspeedωcutoff)

  Phase compensation=arctan(ωspeedωcutoff)
