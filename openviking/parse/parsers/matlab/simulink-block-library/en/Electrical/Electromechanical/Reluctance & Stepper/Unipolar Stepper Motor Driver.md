---
type: simulink-block
title: 'Unipolar Stepper Motor Driver'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'unipolarsteppermotordriver'
documentation_source_path: 'ref/unipolarsteppermotordriver.html'
language: en
---

# Unipolar Stepper Motor Driver

## Ports

### Conserving

### **A+** — Top A-phase electrical connection electrical

Electrical conserving port associated with the top A-phase electrical
connection.

### **A0** — A-phase center tap connection electrical

Electrical conserving port associated with the A-phase center tap
connection.

### **A-** — Lower A-phase electrical connection electrical

Electrical conserving port associated with the lower A-phase
electrical connection.

### **B+** — Top B-phase electrical connection electrical

Electrical conserving port associated with the top B-phase electrical
connection.

### **B0** — B-phase center tap connection electrical

Electrical conserving port associated with the B-phase center tap
connection.

### **B-** — Lower B-phase electrical connection electrical

Electrical conserving port associated with the lower B-phase
electrical connection.

### **ENA** — Triggering input step voltage electrical

Electrical conserving port associated with the triggering input step
voltage.

### **REF** — Rotor electrical

Electrical conserving port associated with the input floating
reference voltage.

### **REV** — Motor direction control voltage electrical

Electrical conserving port associated with the voltage that controls
motor direction.

## Parameters

### **Simulation mode** — Simulation mode `Stepping` (default) | `Averaged`

Select `Stepping` or
`Averaged`. Use
`Averaged` only if the block is connected
directly to a Unipolar Stepper Motor block
also running in **Averaged** mode.

### **Step rate sensitivity** — Step rate sensitivity `10` `Hz/V` (default)

This parameter converts the voltage presented across the
**ENA** and **REF** ports into a step
rate demand.

#### Dependencies

This parameter is visible only when you set the **Simulation
mode** parameter to
`Averaged`.

### **Enable threshold voltage** — Enable threshold voltage `2.5` `V` (default)

When the voltage at the **ENA** port rises above this
threshold, the Unipolar Stepper Motor Driver
block initiates a step.

#### Dependencies

This parameter is visible only when you set the **Simulation
mode** parameter to
`Stepping`.

### **Reverse threshold voltage** — Reverse threshold voltage `2.5` `V` (default)

When the voltage at the **REV** port rises above this
threshold, pulse *B* leads pulse *A* by 90
degrees, and the motor direction is reversed.

### **Output voltage amplitude** — Output voltage amplitude `10` `V` (default)

Amplitude of the output pulse trains.

### **Stepping mode** — Stepping mode `Full stepping` (default) | `Half stepping`

Select `Full stepping` or `Half
stepping`.

## Libraries

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014a**

## Description

Driver for unipolar stepper motor

The Unipolar Stepper Motor Driver block represents a
driver specifically configured for use with the Unipolar Stepper
Motor block. It connects the two winding center-tap connections A0
and B0 to the positive supply with a voltage equal to the value you provide for the
**Output voltage amplitude** parameter. The
**A+**, **A-**, **B+**, and
**B-** ports are grounded in the appropriate sequence to create the
stepping motion. The block initiates a step each time the voltage at the
**ENA** port rises above the **Enable threshold
voltage** parameter value.

If the voltage at the **REV** port is less than or equal to the
**Reverse threshold voltage** parameter value, pulse
*A* leads pulse *B* by 90 degrees. If the voltage
at the **REV** port is greater than the **Reverse threshold
voltage** value, pulse *B* leads pulse
*A* by 90 degrees and the motor direction is reversed.

At time zero, **A-** and **B+** are grounded.

If you set the **Stepping mode** parameter to `Half
stepping`, the Unipolar Stepper Motor
Driver block can produce the output waveforms required for half
stepping. In this mode, there is an intermediate state between the full steps, in which
just one of the *A* or the *B* half-windings is
powered. As a result, the step size is half of the stepper motor’s full step size. At
half steps, windings that are not powered are short-circuited. This approximates the
effect of a freewheeling diode connected across the windings.

### Averaged Mode

If you set the **Simulation mode** parameter to
`Averaged`, both for a Unipolar Stepper
Motor Driver block and for the Unipolar Stepper
Motor block connected to it, then the individual steps are not
simulated. This can be a good way to speed up simulation. The
`Averaged` mode assumes that the external controller
provides a step rate demand. This step rate demand is determined from the voltage
applied between the **ENA** and **REF** ports on
the Unipolar Stepper Motor Driver block, by
multiplying this voltage by the value of the **Step rate
sensitivity** parameter. The rotation direction is set by the
**REF** port in the same way as for the Stepping mode.

`Averaged` mode needs to communicate the step rate demand
and also output voltage amplitude information to the Unipolar Stepper
Motor block. To do this, the step rate demand is applied as an
equivalent voltage across the **A+** and **A-**
ports. Similarly the output voltage amplitude information is conveyed by applying a
steady-state voltage across the **B+** and **B-**
ports with value equal to the **Output voltage amplitude**
parameter.
