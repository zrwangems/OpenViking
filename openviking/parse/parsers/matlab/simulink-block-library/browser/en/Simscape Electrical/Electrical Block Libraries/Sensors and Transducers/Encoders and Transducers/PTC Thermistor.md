---
type: simulink-block
title: 'PTC Thermistor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Encoders and Transducers'
documentation_page: 'ptcthermistor'
documentation_source_path: 'ref/ptcthermistor.html'
language: en
---

# PTC Thermistor

## Ports

### Conserving

### **A** — Thermal mass thermal

Thermal conserving port associated with the thermal mass.

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative
terminal.

## Parameters

### Electrical

### **Thermistor parameterization type** — Thermistor type `Switching Thermistor` (default) | `RTD (Callendar - Van Dusen coefficients)`

*Since R2024a*

Thermistor type. This parameter determines the equations that the
block uses to calculate the resistance as a function of temperature.
Choose one of these options:

- `Switching Thermistor` — Model a
  switching thermistor. Specify the temperature coefficient
  and electrical resistance at a nominal temperature and a
  reference temperature.
- `RTD (Callendar - Van Dusen
  coefficients)` — Model a resistance
  temperature detector. Specify the Callendar–Van Dusen
  coefficients and the nominal resistance at 0 degC.

### **Nominal resistance R0 at T0** — Resistance at nominal temperature `1000` `Ohm` (default) | positive scalar

Resistance at the nominal temperature. Datasheets often list the
nominal resistance at 25 degrees Celsius as R25.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `Switching
Thermistor`.

### **Temperature coefficient alpha0 at T0** — Temperature coefficient at nominal temperature `-0.01` `1/K` (default) | negative scalar

Temperature coefficient at the nominal temperature.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `Switching
Thermistor`.

### **Nominal temperature T0** — Nominal temperature `298.15` `K` (default) | positive scalar

Temperature at which you quote the nominal resistance.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `Switching
Thermistor`.

### **Reference resistance R1 at T1** — Resistance at reference temperature `10000` `Ohm` (default) | positive scalar

Resistance at the reference temperature.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `Switching
Thermistor`.

### **Temperature coefficient alpha1 at T1** — Temperature coefficient at reference temperature `1` `1/K` (default) | positive scalar

Temperature coefficient at the reference temperature.

### **Reference temperature T1** — Reference temperature `398.15` `K` (default) | scalar

Temperature at which you quote the reference resistance. This
temperature must be in the PTC regime.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `Switching
Thermistor`.

### **Nominal resistance R0 at 0 degC** — Resistance at nominal temperature `100` `Ohm` (default) | positive scalar

*Since R2024a*

Resistance at the nominal temperature of 0 degrees Celsius.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `RTD (Callendar
- Van Dusen coefficients)`.

### **A Coefficient [degC^-1]** — `A` coefficient `3.9083e-3` (default) | positive scalar

*Since R2024a*

`A` coefficient in the Callendar–Van Dusen equation.
The default value is typical for platinum RTDs.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `RTD (Callendar
- Van Dusen coefficients)`.

### **B Coefficient [degC^-2]** — `B` coefficient `-5.775e-7` (default) | scalar

*Since R2024a*

`B` coefficient in the Callendar–Van Dusen equation.
The default value is typical for platinum RTDs.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `RTD (Callendar
- Van Dusen coefficients)`.

### **C Coefficient [degC^-4]** — `C` coefficient `-4.183e-12` (default) | scalar

*Since R2024a*

`C` coefficient in the Callendar–Van Dusen equation.
The default value is typical for platinum RTDs.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `RTD (Callendar
- Van Dusen coefficients)`.

### Temperature Operating Limits

### **Enable temperature operating limits** — Option to specify temperature operating limits `No` (default) | `Yes`

*Since R2024a*

Option to specify the operating limits for the temperature.

#### Dependencies

To enable this parameter, set **Thermistor
parameterization type** to `Switching
Thermistor`.

### **Reporting if operating limits exceeded** — Reporting if temperature falls outside operating range `Warn` (default) | `Error`

*Since R2024a*

Reporting if the temperature falls outside of the operating limits.
Choose one of these options:

- `Warn` — Simulink displays a warning and the simulation
  continues.
- `Error` — Simulink displays an error and terminates the
  simulation.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Thermistor parameterization
  type** to `Switching
  Thermistor` and **Enable
  temperature operating limits** to
  `Yes`.
- Set **Thermistor parameterization
  type** to `RTD (Callendar - Van
  Dusen coefficients)`.

### **Minimum operating temperature** — Lower limit of operating temperature range `223.15` `K` (default) | scalar

*Since R2024a*

Lower limit of the operating temperature range.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Thermistor parameterization
  type** to `Switching
  Thermistor` and **Enable
  temperature operating limits** to
  `Yes`.
- Set **Thermistor parameterization
  type** to `RTD (Callendar - Van
  Dusen coefficients)`.

### **Maximum operating temperature** — Upper limit of operating temperature range `428.15` `K` (default) | scalar

*Since R2024a*

Upper limit of the operating temperature range.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Thermistor parameterization
  type** to `Switching
  Thermistor` and **Enable
  temperature operating limits** to
  `Yes`.
- Set **Thermistor parameterization
  type** to `RTD (Callendar - Van
  Dusen coefficients)`.

### Thermal

### **Thermal time constant** — Thermal time constant `5.0` `s` (default) | positive scalar

Time it takes for the thermistor temperature to change by 63% of the
final temperature change when there is a step change in the ambient
temperature.

### **Dissipation factor** — Dissipation factor `0.75e-3` `W/K` (default) | positive scalar

Thermal power needed to raise the thermistor temperature by 1
K.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

### R2024a: Model resistance temperature detector

You can now model a resistance temperature detector (RTD). The block uses the
Callendar–Van Dusen equation to calculate the resistance as a function of
temperature. To enable this option, set the **Thermistor parameterization
type** parameter to `RTD (Callendar – Van Dusen
coefficients)`.

If you model an RTD, you must specify operating temperature limits. If you model a
switching-type thermistor, you can now choose to specify the operating temperature
limits.

### R2024a: Model self-heating

The PTC Thermistor block now models self-heating.
This equation describes the thermal behavior of the block:

Q=KdtcdTdt−I2R.

For a definition of each of the variables, see Description.

Before 2024a, the equation that the block uses does not include the
*IR*2 term. This change improves
modeling accuracy without slowing down the simulation.

As a result of this change, you must not connect the block to an ideal current
source because this arrangement creates a positive feedback loop that results in
thermal runaway.

## Description

Positive temperature coefficient (PTC) thermistor

The PTC thermistor block models a positive temperature
coefficient (PTC) thermistor. To model a switching PTC thermistor or a resistance
temperature detector (RTD), use this block. To model a non-switching linear PTC
thermistor, use the Thermal Resistor block.

The thermal behavior of the block uses the equation

Q=KdtcdTdt−I2R,

where:

- *Q* is the net heat flow into the **A** port.
- *K*d is the **Dissipation
  factor** parameter value.
- *t*c is the **Thermal time
  constant** parameter value.
- *dT/dt* is the rate of change of temperature with respect
  to time.
- *I* is the current.
- *R* is the resistance.

**Note**

You must not connect the PTC Thermistor block
to an ideal current source. This arrangement creates a positive feedback loop
that results in thermal runaway because:

- Increasing the temperature increases the resistance
- Increasing the resistance with an ideal current source increases the
  voltage
- Increasing the voltage increases the dissipated power
- Increasing the dissipated power increases the temperature, which
  closes the loop

### Temperature Operating Limits

*Since R2024a*

If you set the **Thermistor parameterization type** parameter to
`Switching Thermistor`, you can choose whether to
specify the range of operating temperatures by using the **Enable
temperature operating limits** parameter. If you set the
**Thermistor parameterization type** parameter to
`RTD (Callendar - Van Dusen coefficients)`, you must
specify the range of operating temperatures.

Specify the lower and upper temperature operating limits by setting the
**Minimum operating temperature** and **Maximum
operating temperature** parameters, respectively. Find these values on
a datasheet. If the temperature falls outside of the operating limits:

- If you set **Reporting if operating limits exceeded**
  to `Warn`, Simulink® displays a warning and the simulation continues.
- If you set **Reporting if operating limits exceeded**
  to `Error`, Simulink displays an error and terminates the simulation.

### Switching Thermistor

To model a switching PTC thermistor, set the **Thermistor parameterization
type** parameter to `Switching Thermistor`.
This type of thermistor has a decreasing resistance with increasing temperature up
to the Curie temperature *T*c. Above the
Curie temperature, the resistance increases rapidly with increasing temperature. The
region to the right of *T*c in this figure
is called the *PTC regime*.

This equation defines the resistance *R* at temperature
*T*,

R={R0eα0(T−T0)  ​​​​​​ for T≤TcR1eα1(T−T1)   ​ for T≥Tc

Tc=log(R1)−log(R0)+α0T0−α1T1α0−α1

where:

- *R*0 is the resistance at the
  nominal temperature.
- *R*1 is the resistance at the
  reference temperature.
- *α*0 is the temperature
  coefficient at the nominal temperature.
- *α*1 is the temperature
  coefficient at the reference temperature.
- *T*0 is the nominal temperature at
  which you quote the nominal resistance, usually room temperature.
  *T*0 must be less than the Curie
  temperature.
- *T*1 is the reference temperature
  at which you quote the reference resistance.
  *T*1 must be in the PTC
  regime.

### Resistance Temperature Detector

*Since R2024a*

To model an RTD, set the **Thermistor parameterization type** to
`RTD (Callendar - Van Dusen coefficients)`. The
Callendar–Van Dusen equation defines the resistance *R* at
temperature *T*. This equation uses *T* measured
in degC,

R={R0(1+AT+BT2+C(T−100)T3​)  ​ for T≤0R0(1+AT+BT2)                                     for T≥0

where:

- *R*0 is the resistance at the
  nominal temperature of 0 degC.
- *A*, *B*, and *C*
  are the Callendar–Van Dusen coefficients.

You can find these coefficients on a datasheet. The default parameter
values that the block uses are typical for platinum RTDs. The
*R*-*T* characteristic is approximately linear
within the range of operating temperatures so choose values of *B*
and *C* that are several orders of magnitude smaller than
*A*.

Simulink displays a warning if the resistance does not increase monotonically
over the range of operating temperatures. If you set the **Reporting if
operating limits exceeded** parameter to
`Warn` and the temperature falls outside of the
operating range, the block uses linear extrapolation to calculate the resistance
with respect to temperature.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
