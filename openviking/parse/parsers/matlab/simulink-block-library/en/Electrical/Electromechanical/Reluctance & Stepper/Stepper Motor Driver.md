---
type: simulink-block
title: 'Stepper Motor Driver'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'steppermotordriver'
documentation_source_path: 'ref/steppermotordriver.html'
language: en
---

# Stepper Motor Driver

## Ports

### Conserving

### **A+** — *A*-phase positive terminal electrical

Electrical conserving port associated with the
*A*-phase positive terminal.

### **A-** — *A*-phase negative terminal electrical

Electrical conserving port associated with the
*A*-phase negative terminal.

### **B+** — *B*-phase positive terminal electrical

Electrical conserving port associated with the
*B*-phase positive terminal.

### **B-** — *B*-phase negative terminal electrical

Electrical conserving port associated with the
*B*-phase negative terminal.

### **ENA** — Triggering input step voltage electrical

Electrical conserving port associated with the step trigger
input.

### **REF** — Input floating reference voltage electrical

Electrical conserving port associated with the floating reference
voltage.

### **REV** — Input voltage that controls motor direction electrical

Electrical conserving port associated with the motor direction
input.

### **VM** — Supply voltage electrical

Electrical conserving port associated with the supply voltage.

#### Dependencies

To enable this port, set **Power supply** to
`External`.

### **GND** — Supply ground reference electrical

Electrical conserving port associated with the supply ground
reference.

In external power supply mode, the **A-** and
**B-** ports are internally connected to **GND**. You must provide positive supply
voltages and the supply must always be connected (for example, you
cannot put a series switch between supply and driver).

#### Dependencies

To enable this port, set **Power supply** to
`External`.

## Parameters

### **Simulation mode** — Simulation mode `Stepping` (default) | `Averaged`

Use `Averaged` only if the block is connected
directly to a Stepper Motor block also
running in Averaged mode.

### **Step rate sensitivity** — Step rate demand sensitivity `10` `Hz/V` (default) | positive number

This parameter converts the voltage presented across the
**ENA** and **REF** ports into a step
rate demand.

#### Dependencies

To enable this parameter, set **Simulation mode** to
`Averaged`.

### **Enable threshold voltage** — Step voltage threshold `2.5` `V` (default) | positive number

When the voltage at the **ENA** port rises above this
threshold, the Stepper Motor Driver block
initiates a step.

#### Dependencies

To enable this parameter, set **Simulation mode** to
`Stepping`.

### **Reverse threshold voltage** — Reversal voltage threshold `2.5` `V` (default) | positive number

When the voltage at the **REV** port rises above this
threshold, pulse *B* leads pulse *A* by 90
degrees, and the motor direction is reversed.

### **Output voltage amplitude** — Pulse output amplitude `10` `V` (default) | positive number

Amplitude of the output pulse trains.

#### Dependencies

To enable this parameter, either:

- Set **Simulation mode** to
  `Averaged`.
- Set **Simulation mode** to
  `Stepping` and **Power
  supply** to
  `Internal`.

### **Supply voltage** — Supply voltage `10` `V` (default) | positive number

Voltage from external power supply.

#### Dependencies

To enable this parameter, set **Stepping mode** to
`Microstepping` and **Power
supply** to `Internal`.

### **Stepping mode (averaged)** — Step size for averaged simulation `Full stepping` (default) | `Half stepping`

Whether to enable `Full stepping` or
`Half stepping` mode.

#### Dependencies

To enable this parameter, set **Simulation mode** to
`Averaged`.

### **Stepping mode** — Step size for stepping simulation `Full stepping` (default) | `Half stepping` | `Microstepping`

Whether to enable `Full stepping`,
`Half stepping`, or
`Microstepping` mode.

#### Dependencies

To enable this parameter, set **Simulation mode** to
`Stepping`.

### **Number of microsteps per step** — Number of microsteps per step `4` (default) | positive number

Number of microsteps per step. This value must be a positive power of
two.

#### Dependencies

To enable this parameter, set **Stepping mode** to
`Microstepping`.

### **Maximum continuous current per phase** — Maximum continuous current per phase `1.2` `A` (default)

Maximum continuous current per phase

#### Dependencies

To enable this parameter, set **Stepping mode** to
`Microstepping`.

## Libraries

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Driver for stepper motor

The Stepper Motor Driver block represents a driver for
a stepper motor. It creates the pulse trains, *A* and
*B*, required to control the motor. This block initiates a step
each time the voltage at the **ENA** port rises above the
**Enable threshold voltage** parameter value.

If the voltage at the **REV** port is less than or equal to the
**Reverse threshold voltage** parameter value, pulse
*A* leads pulse *B* by 90 degrees. If the voltage
at the **REV** port is greater than the **Reverse threshold
voltage** value, pulse *B* leads pulse
*A* by 90 degrees and the motor direction is reversed.

At time zero, pulse *A* is positive and pulse *B* is
negative.

If you set the **Stepping mode** parameter to `Half
stepping`, the Stepper Motor Driver
block can produce the output waveforms required for half stepping. In this mode, there
is an intermediate state between the full steps, in which just one of the
*A* or the *B* half-windings is powered. As a
result, the step size is half of the stepper motor’s full step size. At half steps,
windings that are not powered are short-circuited. This approximates the effect of a
freewheeling diode connected across the windings.

### Microstepping

To advance the rotor of a fraction of a step instead of a full or half step, set
the **Stepping mode** parameter
to `Microstepping`. This mode enables circular
current-controlled microstepping and increases the resolution in the position of the
rotor. To select the fractional stepping resolution, specify the value of the
**Number of microsteps per step** parameter.

The block initiates a micro-step each time the voltage at the **ENA** port rises above the value of the **Enable
threshold voltage** parameter.

In microstepping mode, the current in each motor winding follows a discretized
sinusoidal waveform. The amplitude of the current waveform is equal to the value of
the **Maximum continuous current per phase** parameter.

To increase or decrease the current in each microstep, the driver applies a
positive or negative over-voltage until the current matches the target value.

If you set the **Power supply** parameter to
`Internal`, the applied over-voltage is equal to the
value of the **Supply voltage** parameter. If you set the
**Power supply** parameter to
`External` the applied over-voltage is equal to the
voltage between the **VM** and **GND**  ports.

### Averaged Mode

If you set the **Simulation mode** parameter to
`Averaged`, both for a Stepper Motor
Driver block and for the Stepper
Motor block connected to it, then the individual steps are not
simulated. This can be a good way to speed up simulation. The
`Averaged` mode assumes that the external controller
provides a step rate demand. This step rate demand is determined from the voltage
applied between the **ENA** and **REF** ports on
the Stepper Motor Driver block, by multiplying this
voltage by the value of the **Step rate sensitivity** parameter.
The rotation direction is set by the **REF** port in the same way
as for the `Stepping` mode.

`Averaged` mode needs to communicate the step rate demand
and also output voltage amplitude information to the Stepper
Motor block. To do this, the step rate demand is applied as an
equivalent voltage across the **A+** and **A-**
ports. Similarly the output voltage amplitude information is conveyed by applying a
steady-state voltage across the **B+** and **B-**
ports with value equal to the **Output voltage amplitude**
parameter.
