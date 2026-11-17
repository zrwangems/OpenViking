---
type: simulink-block
title: 'Hall Speed and Position'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'hallspeedandposition'
documentation_source_path: 'ref/hallspeedandposition.html'
language: en
---

# Hall Speed and Position

## Ports
```yaml
ports:
- name: HallVal
  summary: Current Hall sensor output state scalar
  direction: input
  data_types: uint8 | uint16 | uint32
- name: Cnt
  summary: External counter value scalar
  direction: input
  data_types: uint8 | uint16 | uint32
- name: SpdCnt
  summary: Count at Hall state change scalar
  direction: input
  data_types: uint8 | uint16 | uint32
- name: Dir
  summary: Rotor spin direction during current Hall state scalar
  direction: input
  data_types: int8 | int16 | int32
- name: SpdVal
  summary: Validity of current and previous Hall states and speed calculation scalar
  direction: input
  data_types: uint8 | uint16 | uint32
- name: HallChng
  summary: Value of Hall state change flag scalar
  direction: input
  data_types: uint8 | uint16 | uint32
- name: θe
  summary: Electrical position of rotor scalar
  direction: output
  data_types: single | double | fixed point
- name: ⍵m
  summary: Mechanical speed of rotor scalar
  direction: output
  data_types: single | double | fixed point
- name: HallChngRst
  summary: Resets Hall state change flag to zero scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **HallVal** — Current Hall sensor output state scalar

The Hall state at current time. For example, these are the possible valid Hall
states (where the MSB represents the output of the first Hall sensor
connected):

- 5 - (101)
- 4 - (100)
- 6 - (110)
- 2 - (010)
- 3 - (011)
- 1 - (001)

**Data Types:** `uint8` | `uint16` | `uint32`

### **Cnt** — External counter value scalar

The external counter value that the block uses to determine the time elapsed
between the Hall state change and block execution.

**Data Types:** `uint8` | `uint16` | `uint32`

### **SpdCnt** — Count at Hall state change scalar

This value indicates the clock cycles (time) elapsed between two consecutive
changes in the Hall state.

**Data Types:** `uint8` | `uint16` | `uint32`

### **Dir** — Rotor spin direction during current Hall state scalar

The direction of the rotor spin (either +1 or –1 indicating positive or negative
direction of rotation, respectively) during the current Hall state.

**Data Types:** `int8` | `int16` | `int32`

### **SpdVal** — Validity of current and previous Hall states and speed calculation scalar

The port value indicates Hall state validity. The value zero indicates that the
current or previous Hall state is invalid and that the block cannot calculate speed
and position.

The value one indicates that both the current and previous Hall states are valid
and that the block can calculate speed and position.

**Data Types:** `uint8` | `uint16` | `uint32`

### **HallChng** — Value of Hall state change flag scalar

The port value indicates Hall state change and block execution status. The value
one indicates that the Hall state changed, but that the block execution is pending.
The value zero indicates that the block has completed executing the last Hall state
change.

**Data Types:** `uint8` | `uint16` | `uint32`
### Output

### **θe** — Electrical position of rotor scalar

The estimated electrical position of the rotor based on the **Expected
hall sequence in positive direction** parameter and the
`Direction`, `HallVal`, and
`CounterValue` inputs.

#### Dependencies

To enable this port, set **Block output** to either
`Position` or `Speed and
position`.

**Data Types:** `single` | `double` | `fixed point`

### **⍵m** — Mechanical speed of rotor scalar

The mechanical speed of the rotor in revolutions per minute. The block calculates
this value by tracking the Hall state changes.

The port returns zero if the `SpdVal` input is zero.

#### Dependencies

To enable this port, set **Block output** to either
`Speed` or `Speed and
position`.

**Data Types:** `single` | `double` | `fixed point`

### **HallChngRst** — Resets Hall state change flag to zero scalar

The port outputs a value of zero (sets the Hall state change flag to zero)
indicating that the block has successfully executed speed and position computations
for the last Hall state change.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Block output
  summary: Select output ports Speed and position (default) | Speed | Position
  group: General
- name: Counter size
  summary: Size of external counter register 32 bits (default) | 8 bits | 16 bits
  group: General
- name: Counter clock frequency (Hz)
  summary: Clock frequency of external counter 90e6 (default) | scalar
  group: General
- name: Discrete step size (s)
  summary: Sample time after which block executes again 50e-6 (default) | scalar
  group: General
- name: Number of pole pairs
  summary: Number of pole pairs available in motor 8 (default) | scalar
  group: General
- name: Minimum detectable speed (RPM)
  summary: Minimum speed that block can detect 20 (default) | scalar
  group: General
- name: Speed measurement interval
  summary: Interval over which block measures speed Every 180 Degrees (default) | Every 60 Degrees
  group: General
- name: Speed unit
  summary: Unit of rotor angular speed output Radians/sec (default) | Degrees/sec | RPM | Per unit
  group: General
- name: Speed datatype
  summary: Data type of rotor angular speed output single (default) | double | fixed point
  group: General
- name: Expected hall sequence in positive direction
  summary: Sequence indicating positive direction ABC (default) | CBA | Custom sequence
  group: Position
- name: Sequence
  summary: Custom sequence indicating positive direction [5,4,6,2,3,1] (default) | scalar
  group: Position
- name: Order of extrapolation of position
  summary: Indicates precision in position computation 1st Order (default) | 2nd Order
  group: Position
- name: Position unit
  summary: Unit of angular position output Radians (default) | Degrees | Per unit
  group: Position
- name: Position datatype
  summary: Data type of angular position output single (default) | double | fixed point
  group: Position
```

### General

### **Block output** — Select output ports `Speed and position` (default) | `Speed` | `Position`

Select the available block output ports as one of the following values:

- Speed and position
- Speed
- Position

### **Counter size** — Size of external counter register `32 bits` (default) | `8 bits` | `16 bits`

The register size of the external counter. The maximum counter value is 2n-1, where n = counter size.

### **Counter clock frequency (Hz)** — Clock frequency of external counter `90e6` (default) | scalar

The clock frequency of the external counter.

### **Discrete step size (s)** — Sample time after which block executes again `50e-6` (default) | scalar

The time between two consecutive instances of block execution.

### **Number of pole pairs** — Number of pole pairs available in motor `8` (default) | scalar

Number of pole pairs available in the motor.

### **Minimum detectable speed (RPM)** — Minimum speed that block can detect `20` (default) | scalar

The block does not calculate position for speed below this value.

### **Speed measurement interval** — Interval over which block measures speed `Every 180 Degrees` (default) | `Every 60 Degrees`

Rotor angular displacement that represents the interval at which the
`SpdCnt` port value was calculated.

### **Speed unit** — Unit of rotor angular speed output `Radians/sec` (default) | `Degrees/sec` | `RPM` | `Per unit`

Unit of the angular velocity or mechanical speed
(`⍵m`) output.

#### Dependencies

To enable this parameter, set **Block output** to either
`Speed` or `Speed and
position`.

### **Speed datatype** — Data type of rotor angular speed output `single` (default) | `double` | `fixed point`

Data type of the rotor angular speed output.

#### Dependencies

To enable this parameter, set **Block output** to either
`Speed` or `Speed and
position`.

### Position

### **Expected hall sequence in positive direction** — Sequence indicating positive direction `ABC` (default) | `CBA` | `Custom sequence`

The Hall sensor sequence that represents the positive direction of rotor
spin.

#### Dependencies

To enable this parameter, set **Block output** to either
`Position` or `Speed and
position`.

### **Sequence** — Custom sequence indicating positive direction `[5,4,6,2,3,1]` (default) | scalar

The custom sequence that you can enter to represent rotor spin in the positive
direction.

#### Dependencies

To enable this parameter:

- Set **Block output** to either
  `Position` or `Speed and
  position`.
- Set **Expected hall sequence in positive direction** to
  `Custom sequence`.

### **Order of extrapolation of position** — Indicates precision in position computation `1st Order` (default) | `2nd Order`

The `1st Order` option is less accurate in computing
position, but quick. The `2nd Order` option is more accurate,
but needs more computation time. These equations describe the options:

θ1st Order=θsector+ωt

θ2nd Order=θsector+ωt+12αt2

where:

θ1st Order = Position computed by using 1st order extrapolation.

θ2nd Order = Position computed by using 2nd order extrapolation.

θsector = Sector angle defined by the Hall sensor output.

ω = Angular velocity of the rotor.

α = Angular acceleration of the rotor.

t = Time spent in a sector.

#### Dependencies

To enable this parameter, set **Block output** to either
`Position` or `Speed and
position`.

### **Position unit** — Unit of angular position output `Radians` (default) | `Degrees` | `Per unit`

Unit of the angular position output.

#### Dependencies

To enable this parameter, set **Block output** to either
`Position` or `Speed and
position`.

### **Position datatype** — Data type of angular position output `single` (default) | `double` | `fixed point`

The data type for the angular position output.

#### Dependencies

To enable this parameter, set **Block output** to either
`Position` or `Speed and
position`.
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

Compute speed and estimate position of rotor by using Hall sensors

The Hall Speed and Position block computes the mechanical speed of the
rotor by tracking changes in the Hall state. The block also estimates the electric position of
the rotor by using the direction, Hall state, and external counter value inputs.

The block executes periodically after a fixed time interval that the controller algorithm
defines.
