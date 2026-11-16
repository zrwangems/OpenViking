---
type: simulink-block
title: 'Operational Transconductance Amplifier'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'operationaltransconductanceamplifier'
documentation_source_path: 'ref/operationaltransconductanceamplifier.html'
language: en
---

# Operational Transconductance Amplifier

## Ports

### Conserving

### **+** — Non-inverting input electrical

Electrical conserving port associated with the op-amp non-inverting
input.

### **-** — Negative voltage electrical

Electrical conserving port associated with the op-amp inverting
input.

### **C** — Control current electrical

Electrical conserving port associated with the op-amp control
current.

### **OUT** — Output current electrical

Electrical conserving port associated with the op-amp output. The port
name is hidden on the block icon, but you can see it in simulation data
logs.

## Parameters

### Nominal Measurements

### **Transconductance** — Transconductance `9600` `uS` (default)

The transconductance, *g*m,
when the control current is equal to the **Reference control
current**. This is the ratio of the transconductance
current, *i*gm, to the voltage
difference, *v*, across the `+` and
`-` pins.

### **Input resistance** — Input resistance `25` `kOhm` (default)

The input resistance, *R*in,
when the control current is equal to the **Reference control
current**. The input resistance is the ratio of the voltage
difference, *v*, across the `+` and
`-` pins to the current flowing from the
`+` to the `-` pin.

### **Output resistance** — Output resistance `3` `MOhm` (default)

The output resistance, *R*out,
when the control current is equal to the **Reference control
current**. See above for the equation defining output
resistance.

### **Reference control current** — Reference control current `500` `uA` (default)

The control current at which the
**Transconductance**, **Input
resistance**, and **Output resistance**
are quoted.

### Dynamics

### **Dynamics** — Dynamics `No lag` (default) | `Finite bandwidth with slew rate limiting`

Select one of the following options:

- `No lag` — Do not model
  the dynamics of the relationship between output current and
  input voltage. This is the default.
- `Finite bandwidth with slew rate
  limiting` — Model the dynamics of
  the relationship between output current and input voltage
  using a first-order lag. If you select this option, the
  **Bandwidth**, **Maximum
  current slew rate**, and **Initial
  current** parameters appear on the
  **Dynamics** tab.

### **Bandwidth** — Bandwidth of the first-order lag `2` `MHz` (default)

The bandwidth of the first-order lag used to model the dynamics of the
relationship between output current and input voltage.

#### Dependencies

This parameter is visible only when the
**Dynamics** parameter is set to
`Finite bandwidth with slew rate
limiting`.

### **Maximum current slew rate** — Maximum rate-of-charge of transconductance current `2` `A/us` (default)

The maximum rate-of-change of transconductance current when there is
no feedback around the device. Note that datasheets sometimes quote slew
rate as a maximum rate of change of voltage. In this case, the value
depends on the particular test circuit. To get an accurate value for
**Maximum current slew rate**, reproduce the test
circuit in a Simscape™
Electrical™ model, and tune the parameter value to match the datasheet
value. If the test circuit is open-loop, and the load resistance is
quoted, you can obtain an approximate value for the **Maximum
current slew rate** by dividing the voltage slew rate by
the load resistance.

#### Dependencies

This parameter is visible only when the
**Dynamics** parameter is set to
`Finite bandwidth with slew rate
limiting`.

### **Initial current** — Initial transconductance current `0` `A` (default)

The initial transconductance current (note, not the initial output
current). This is the transconductance current sinking to both the
internal output resistance,
*R*out, and the output
pin.

#### Dependencies

This parameter is visible only when the
**Dynamics** parameter is set to
`Finite bandwidth with slew rate
limiting`.

### Limits

### **Minimum output voltage** — Minimum output voltage `-15` `V` (default)

The output voltage is limited to be greater than the value of this
parameter.

### **Maximum output voltage** — Maximum output voltage `15` `V` (default)

The output voltage is limited to be less than the value of this
parameter.

### **Additional output resistance at voltage swing limits** — Additional output resistance at voltage swing limits `1` `Ohm` (default)

To limit the output voltage swing, an additional output resistance is
applied between output and the power rail when the output voltage
exceeds the limit. The value of this resistance should be low compared
to the output resistance and circuit load resistance.

### **Minimum control current for simulation** — Minimum control current for simulation `0.001` `uA` (default)

The control current measured at the control current pin
`C` is limited to be greater than the value of this
parameter. This prevents a potential divide-by-zero when calculating
input and output resistance values based on the value of the control
current.

## Libraries

Simscape / Electrical / Integrated Circuits

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011b**

## Description

Behavioral representation of operational transconductance amplifier

The Operational Transconductance Amplifier block
provides a behavioral representation of an operational transconductance amplifier. A
transconductance amplifier converts an input voltage into an output current.
Applications include variable frequency oscillators, variable gain amplifiers and
current-controlled filters. These applications exploit the fact that the
transconductance gain is a function of current flowing into the control current
pin.

To support faster simulation, the behavioral representation does not model the
detailed transistor implementation. Therefore, the model is only valid when operating in
the linear region, that is, where the device input resistance, output resistance, and
transconductance gain all depend linearly on the control current, and are independent of
input signal amplitude. The dynamics are approximated by a first-order lag, based on the
value you specify for the block parameter **Bandwidth**.

### Control Current

The control current pin `C` is maintained at the voltage that you
specify for the **Minimum output voltage**. In practice, the
**Minimum output voltage** equals the negative supply
voltage plus the transistor collector-emitter voltage drop. For example, if the
**Minimum output voltage** for a supply voltage of +-15V
is -14.5, then to achieve a control current of 500μA, a resistor connected between
the +15V rail and the control current pin must have a value of (15 - (-14.5)) /
500e-6 = 59kOhm.

### Transconductance

The relationship between input voltage, *v*, and transconductance
current, *i*gm, is:

v=v+−v−igm=gm⋅vgm=gm0⋅icic0

where:

- *v*+ is the voltage presented
  at the block `+` pin.
- *v*– is the voltage presented
  at the block `-` pin.
- *g*m is the
  transconductance.
- *i*c is the control current
  flowing into the control current pin `C`.
- *i*c0 is the reference control
  current, that is, the control current at which transconductance is
  quoted on the datasheet.
- *g*m0 is the transconductance
  measured at the reference control current
  *i*c0.

Therefore, increasing control current increases the transconductance.

### Output Resistance and Determining Output Current

The output resistance, *R*out, is defined
by:

igm+io=voRoutRout=Rout0⋅ic0ic

where:

- *i*gm is the transconductance
  current.
- *i*o is the output current,
  defined as positive if flowing into the transconductance amplifier
  output pin.
- *i*c is the control current
  flowing into the control current pin `C`.
- *i*c0 is the reference control
  current, that is, the control current at which output resistance is
  quoted on the datasheet.
- *R*out0 is the output
  resistance measured at the reference control current
  *i*c0.

Therefore, increasing control current reduces output resistance.

### Input Resistance

The relationship between input voltage, *v*, across the
`+` and `-` pins and the current flowing,
*i*, is:

vi=RinRin=Rin0⋅ic0ic

where:

- *i*c is the control current
  flowing into the control current pin `C`.
- *R*in is the input resistance
  for the current control current value,
  *i*c.
- *i*c0 is the reference control
  current, that is, the control current at which input resistance is
  quoted on the datasheet.
- *R*in0 is the input resistance
  measured at the reference control current
  *i*c0.

Therefore, increasing control current reduces input resistance.

### Limits

Because of the physical construction of an operational transconductance amplifier
based on current mirrors, the transconductance current
*i*gm cannot exceed the control current.
Hence the value of *i*gm is limited
by:

|  |  |
| --- | --- |
| –*i*c ≤ *i*gm ≤ *i*c | **(1)** |

The output voltage is also limited by the supply voltage:

|  |  |
| --- | --- |
| *V*min ≤ *v*o ≤ *V*max | **(2)** |

where *V*min is the **Minimum
output voltage**, and *V*max is
the **Maximum output voltage**. Output voltage limiting is
implemented by adding a low resistance to the output when the voltage limit is
exceeded. The value of this resistance is set by the **Additional output
resistance at voltage swing limits** parameter.

The transconductance current is also slew-rate limited, a value for slew rate
limiting typically being given on datasheets:

−μ≤digmdt≤μ

where *μ* is the **Maximum current slew
rate**.
