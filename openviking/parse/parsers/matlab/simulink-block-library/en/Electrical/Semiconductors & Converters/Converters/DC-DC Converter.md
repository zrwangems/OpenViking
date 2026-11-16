---
type: simulink-block
title: 'DC-DC Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'dcdcconverter'
documentation_source_path: 'ref/dcdcconverter.html'
language: en
---

# DC-DC Converter

## Ports

### Conserving

### **1+** — Input positive terminal electrical

Electrical conserving port associated with the positive terminal of
the input side.

### **1-** — Input negative terminal electrical

Electrical conserving port associated with the negative terminal of
the input side.

### **2+** — Output positive terminal electrical

Electrical conserving port associated with the positive terminal of
the output side.

### **2-** — Output negative terminal electrical

Electrical conserving port associated with the negative terminal of
the output side.

### **Vref** — Voltage reference physical

Physical signal input port that provides the external voltage
reference signal.

#### Dependencies

To enable this port, set the **Voltage Reference** parameter to
`External`.

### **H** — Thermal mass thermal

Thermal conserving port that represents the thermal mass. When you
expose this port, provide additional parameters to define battery
behavior at a second temperature. For more information, see the Thermal parameters.

#### Dependencies

To enable this port, set **Modeling option** to `Show
thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model thermal parameters.

### Main

### **Voltage reference** — Voltage reference `Internal` (default) | `External`

Whether to model the voltage reference internally or externally.

### **Output voltage reference demand** — Voltage set point `10` `V` (default)

Set point for the voltage regulator, and the output voltage value when there is no
output current.

#### Dependencies

This port is visible only when the **Voltage
Reference** parameter is set to
`Internal`.

### **Rated output power** — Rated power `10` `W` (default)

Output power for which the percentage efficiency value is given. This parameter is also
used to calculate droop, *D*, if droop is specified as
a percentage.

### **Enable droop** — Droop option `On` (default) | `Off`

Whether to enable voltage droop.

### **Droop parameterization** — Droop model `By voltage droop with output current` (default) | `By percent voltage droop at rated load`

Select one of the following methods for droop parameterization:

- `By voltage droop with output
  current` — Specify the absolute
  value of droop, *D*. This is the default
  option.
- `By percent voltage droop at rated
  load` — Specify droop,
  *D*, as a percentage at rated
  load.

#### Dependencies

To enable this parameter, select the **Enable
droop** parameter.

### **Output voltage droop with output current** — Voltage droop at 1 A `0.1` `V/A` (default)

Number of volts that the output voltage will drop from the set point for an output
current of 1 A.

#### Dependencies

To enable this parameter, select the **Enable droop** parameter and
set **Droop parameterization** to `By
voltage droop with output current`.

### **Voltage droop percent at rated load** — Voltage droop percent at rated load `2` (default)

Percentage by which the voltage drops compared to the nominal output
voltage when supplying the rated load. If you set the **Voltage
reference** parameter to
`Internal`, the block uses the
**Output voltage reference demand** parameter to
calculate the droop percent. If you set the **Voltage
reference** parameter to
`External`, the block uses the
**Voltage reference used to calculate droop
percent** parameter instead.

#### Dependencies

To enable this parameter, select the **Enable
droop** parameter and set **Droop
parameterization** to `By percent voltage
droop at rated load`.

### **Voltage reference used to calculate droop percent** — Voltage droop percent at rated load `10` `V` (default)

Voltage reference that the **Voltage droop percent at rated
load** parameter uses to calculate the voltage droop during
the simulation.

#### Dependencies

To enable this parameter:

- Set **Voltage reference** to
  `External`.
- Select the **Enable droop**
  parameter.
- Set **Droop parameterization** to
  `By percent voltage droop at rated
  load`.

### **Power direction** — Power flow direction `Unidirectional power flow from supply to regulated side` (default) | `Bidirectional power flow`

Select one of the following methods for the direction of power conversion:

- `Unidirectional power flow from supply to
  regulated side` — Most small power
  regulators are unidirectional. This is the default
  option.
- `Bidirectional power flow`
  — Larger power converters can be bidirectional, for
  example, converters used in electric vehicles to allow
  regenerative braking.

### **Diode off-state conductance** — Unidirectional diode `1e-8` `1/Ohm` (default)

Ideal diode incorporated on the output side to prevent current from
being forced into the converter in the unidirectional
configuration.

### Losses

### **Converter losses at zero output power** — Constant losses `1` `W` (default)

Power drawn by the Pfixed component in the
equivalent circuit diagram, which corresponds to converter losses that
are independent of load current.

### **Converter losses** — Converter losses `Assume proportional to square of output current` (default) | `Tabulate efficiency`

Converter losses parameterization.

### **Percentage efficiency at rated output power** — Rated efficiency `80` (default)

Efficiency as defined by 100 times the output load power divided by the input supply
power.

#### Dependencies

To enable this parameter, set **Converter
losses** to `Assume proportional to square
of output current`.

### **Variables for tabulation** — Tabulation variables `Output current` (default) | `Output current and input voltage` | `Output current and temperature` | `Output current, input voltage, and temperature`

Whether to tabulate efficiency on the output current, the input
voltage, and the temperature. To enable the temperature options, you
need to expose the thermal ports of the block.

### **Vector of output currents for tabulated efficiencies, I2** — Output currents for tabulated efficiencies `[-2, -1, 1, 2]` `A` (default) | vector of positive ascending scalars

Vector of output currents for tabulated efficiencies. The size of this
parameter must be equal to or greater than `3` and
equal to the size of **Percentage efficiency table,
eff(I)**.

#### Dependencies

To enable this parameter, set **Converter
losses** to `Tabulate
efficiency`.

### **Percentage efficiency table, eff(I2)** — Efficiency table in function of current `[66, 76, 80, 74]` (default) | vector of positive scalars

Efficiency table in function of the current, in percentage. The size
of this parameter must be equal to the size of **Vector of
output currents for tabulated efficiencies, I2**.

#### Dependencies

To enable this parameter, set **Converter
losses** to `Tabulate
efficiency` and **Variables for
tabulation** to `Output
current`.

### **Vector of input voltages for tabulated efficiencies, V1** — Input voltages for tabulated efficiencies `[15, 30, 45]` `V` (default) | vector of positive ascending scalars

Vector of input voltages for tabulated efficiencies. The size of this
parameter must be equal to or greater than `2`.

#### Dependencies

To enable this parameter, set **Converter
losses** to `Tabulate
efficiency` and **Variables for
tabulation** to `Output current and input
voltage` or `Output current, input
voltage, and temperature`.

### **Percentage efficiency table, eff(I2,V1)** — Efficiency table in function of current and voltage `[66, 66, 66; 76, 76, 76; 80, 80, 80; 74, 74, 74]` (default) | vector of positive scalars

Efficiency table in function of the current, in percentage.

#### Dependencies

To enable this parameter, set **Converter
losses** to `Tabulate
efficiency` and **Variables for
tabulation** to `Output
current`.

### **Vector of temperatures for tabulated efficiencies, T** — Temperatures for tabulated efficiencies `[280, 300, 320]` `K` (default) | vector of positive ascending scalars

Vector of temperatures for tabulated efficiencies. The size of this
parameter must be equal to or greater than `2`.

#### Dependencies

To enable this parameter, expose the thermal port of this block
and set **Converter losses** to
`Tabulate efficiency`.

### **Percentage efficiency table, eff(I2,T)** — Efficiency table in function of current and temperature `[66, 66, 66; 76, 76, 76; 80, 80, 80; 74, 74, 74]` (default) | vector of scalars

Efficiency table in function of current and temperature, in
percentage.

#### Dependencies

To enable this parameter, expose the thermal port of this block
and set **Converter losses** to
`Tabulate efficiency` and
**Variables for tabulation** to
`Output current and
temperature`.

### **Percentage efficiency table, eff(I2,V1,T)** — Efficiency table in function of current, voltage, and temperature `repmat([66; 76; 80; 74], 1, 3, 3)` (default) | vector of scalars

Efficiency table in function of current, voltage, and temperature, in
percentage.

#### Dependencies

To enable this parameter, expose the thermal port of this block
and set **Converter losses** to
`Tabulate efficiency` and
**Variables for tabulation** to
`Output current, input voltage, and
temperature`.

### Dynamics

### **Dynamics** — Dynamics model `No dynamics` (default) | `Specify voltage regulation time constant`

Specify whether to include voltage regulation dynamics:

- `No dynamics` — Do not
  consider the voltage regulation dynamics.
- `Specify voltage regulation time
  constant` — Add a first-order lag to
  the equation defining the voltage source value. With the
  dynamics enabled, a load step change results in a transient
  change in output voltage.

### **Voltage regulation time constant** — Dynamics time constant `0.02` `s` (default)

Time constant associated with voltage transients when the load current is
stepped.

#### Dependencies

To enable this parameter, set **Dynamics** to `Specify
voltage regulation time constant`.

### **Initial output voltage demand** — Initial demand voltage `10` `V` (default)

Value of *v*ref at time zero. Normally,
*v*ref is defined by the
**Output voltage reference demand** parameter.
However, if you want to initialize the model with no transients when
delivering a steady-state load current, you can set the initial
*v*ref value by using this
parameter, and increase it accordingly to take account of output
resistance and droop.

#### Dependencies

To enable this parameter, set **Dynamics** to
`Specify voltage regulation time
constant`.

### Off State

### **Minimum supply voltage to function** — Minimum supply voltage to operate `1` `V` (default)

Minimum supply voltage for the converter to operate and regulate the
output voltage to the set point. When the supply voltage drops below
`90`% of the value of this parameter, the input to
the DC-DC Converter block behaves like a
fixed resistance equal to the value of the **Input resistance
if not functioning** parameter. Similarly, the output of
the DC-DC Converter block behaves like a
fixed resistance equal to the value of the **Output resistance
if not functioning** parameter.

### **Input resistance if not functioning** — Input resistance if not functioning `1000` `Ohm` (default)

Input resistance when the supply voltage falls below
`90`% of the value of the **Minimum supply
voltage to function** parameter.

### **Output resistance if not functioning** — Output resistance if not functioning `1000` `Ohm` (default)

Output resistance when the supply voltage falls below
`90`% of the value of the **Minimum supply
voltage to function** parameter.

### Faults

### **Open circuit fault** — Option to add open circuit fault `Add fault` (default)

Option to add an output open-circuit fault.

To add a fault, click the **Add fault**
hyperlink.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Thermal mass** — Thermal mass associated with the thermal port `100` `J/K` (default)

Thermal mass associated with thermal port **H**. It represents the
energy required to raise the temperature of the thermal port by one
degree.

### **Initial temperature** — Initial temperature at the thermal port `298.15` `K` (default)

Initial temperature associated with thermal port **H**.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

### R2022b: Support series-connected supply switch

You can now connect a switch in series between the voltage supply and the
DC-DC Converter block and toggle this switch on
and off during the simulation.

To reflect this change, the **Maximum expected supply-side
current** parameter is now called **Minimum supply voltage to
function**. If the supply voltage drops below this value, both the
input and the output sides of the converter behave like constant impedances and the
converter ceases to convert.

If your model saved in an earlier release contains a DC-DC
Converter block with dynamics enabled, and you configure this
block to stop the power flowing form the load to the supply, the simulation results
might behave slightly different. The voltage regulation time constant no longer lags
the blocking diode that prevents reverse power flow and it is now
instantaneous.

## Description

Behavioral model of power converter

The DC-DC Converter block represents a behavioral model of a power converter.
This power converter regulates voltage on the load side. To balance input power, output
power, and losses, the required amount of power is drawn from the supply side.
Alternatively, the converter can support regenerative power flow from load to
supply.

This circuit illustrates the converter's behavior.

The *Pfixed* component draws a constant power and
corresponds to converter losses that are independent of load current. The power drawn is
set by the **Converter losses at zero output power** parameter value.
The resistor *Rout* corresponds to losses that
increase with load current, and is determined from the value you specify for the
**Percentage efficiency at rated output power** parameter.

The voltage source is defined by the following equation:

*v* = *vref* –
*i*
load
*D* + *iload*
*Rout*

Where:

- *vref* is the load side voltage set
  point, as defined by the value you specify for the **Output voltage
  reference demand** parameter. Alternatively, you can provide this
  value as input to the **Vref** port when the **Voltage
  reference** parameter is set to
  `External`.
- *D* is the value you specify for the **Output voltage
  droop with output current** parameter. For more information, see
  Voltage Droop.

The current source value *i* is calculated so that the power flowing
in to the converter equals the sum of the power flowing out plus the converter
losses.

To specify the converter behavior when the voltage presented by the load is higher than the
converter output voltage reference demand, use the **Power direction** parameter:

- `Unidirectional power flow from supply to regulated
  side` — Current is blocked by the off-state diode, and the
  current source current *i* is zero. Set the conductance of
  this diode using the **Diode off-state conductance**
  parameter.
- `Bidirectional power flow` — Power is transmitted
  to the supply side, and *i* becomes negative.

Optionally, the block can include voltage regulation dynamics. If you select
`Specify voltage regulation time constant` for the
**Dynamics** parameter, then a first-order lag is added to the
equation defining the voltage source value. With the dynamics enabled, a load step
change results in a transient change in output voltage, the time constant being defined
by the **Voltage regulation time constant** parameter.

### Voltage Droop

Voltage droop is the loss in output voltage for a device that drives a load. Droop
is important in voltage regulation circuits as it increases the tolerance of the
systems towards load transients.

A separate value for the droop allows you to control how the output voltage varies
with the load regardless of load-dependent losses. To enable droop, select the
**Enable droop** parameter. To specify the droop, set the
**Droop parameterization** parameter to:

- `By voltage droop with output current` — Set
  the voltage droop directly by specifying the value of the
  **Output voltage droop with output current**
  parameter.
- `By percent voltage droop at rated load` —
  This equation calculates the voltage droop as a percent of the
  **Output voltage reference demand** parameter,
  based on the value of the **Voltage droop percent at rated
  load** parameter:

  ΔV=Dpercent100Vref\_droopD=ΔV(Vref\_droop−ΔV)Prated

  where
  `Vref_droop` is the value of
  the **Output voltage reference demand** parameter. If
  you set the **Voltage reference** parameter to
  `External`, the block uses the constant
  value of the **Voltage reference used to calculate droop
  percent** parameter to calculate the droop instead.

  This plot shows how the block calculates the voltage droop:

  The voltage droop, *D*, is the slope of the line,
  where Irated=PratedVrated and Vrated=Vref\_droop−ΔV.

### Tabulated efficiency

You can tabulate the DC-DC Converter block efficiency
depending on the output current, input voltage, and temperature.

This equation defines the relationship between losses and efficiency:

loss(i2,v1,T)=[1−eff(i2,v1,T)100]abs(v1i1)if i2<0 (power flow 1→2)loss(i2,v1,T)=[1−eff(i2,v1,T)100]abs(v2i2)if i2>0 (power flow 2→1)

where

- *loss(i2,v1,T)*
  are the DC-DC converter losses.
- *v1* is the input
  voltage.
- *i1* is the input
  current.
- *i2* is the output
  current.
- *T* is the device temperature, if you expose the
  thermal port of this block.
- *eff(i2,v1,T)*
  is the efficiency of the DC-DC converter as a function of the output
  current, input voltage, and temperature, as specified in
  **Percentage efficiency table,
  eff(I2,V1,T)**.

If the output current is equal to `0`, the converter
losses are equal to **Converter losses at zero output power**.

These are the steps to compute the used power losses depending on the output current:

1. If the output current is less than the last negative current point or
   greater than the first positive current point in the **Vector of
   output currents for tabulated efficiencies, I2** parameter,
   the block uses the **Percentage efficiency table,
   eff(I2)** parameter to find the corresponding efficiency
   (with linear interpolation or nearest extrapolation) and then convert
   that efficiency to losses.
2. Else, the block blends the zero output current case to the last
   negative point or the first positive point in the table, as shown in
   this figure:

If you set the **Modeling option** parameter to `Show thermal
port`, the block tabulates the efficiency depending on the
temperature, in addition to the output current and input voltage. The losses
calculation remains the same as the option with hidden thermal ports.

### Simulating When the Supply Cannot Match the Load

The DC-DC Converter block uses the
**Minimum supply voltage to function** parameter to protect the
network when the voltage supply cannot deliver the load requirements. This happens
if you connect a switch in series with the supply and then turn it off, or if the
supply connection has a series resistance which drops too much voltage. During the
simulation, if the voltage falls below the value of the **Minimum supply
voltage to function** parameter, the block relaxes the regulation of
the output voltage. Once the voltage falls below `90`% of the
**Minimum supply voltage to function** parameter, the input of
the converter behaves like a fixed resistance equal to the value of the
**Input resistance if not functioning** parameter. Similarly,
the output of the DC-DC Converter block behaves like
a fixed resistance equal to the value of the **Output resistance if not
functioning** parameter.

### Simulating Faults

To model a fault in the DC-DC Converter block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The DC-DC Converter block allows you to model an open-circuit fault. When the fault is
triggered, the servomotor stops operating, zero current is taken from the supply
side, and zero current is supplied to the load side.

### Model thermal effects

This block has one optional thermal port. To control the
visibility of the thermal port, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain a thermal
  port.
- `Show thermal port` — The block contains one thermal
  conserving port.

The block transfers heat generated from electrical losses through a Controlled
Heat Flow Rate Source to a Thermal Mass block. The
electrical properties of the block do not change with temperature. Specify the
thermal properties for this block using the parameters **Thermal
mass** and **Initial temperature**.
