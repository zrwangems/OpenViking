---
type: simulink-block
title: 'Battery Power Estimator'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'batterypowerestimator'
documentation_source_path: 'ref/batterypowerestimator.html'
language: en
---

# Battery Power Estimator

## Ports

### Input

### **CellSOC** — Cell state of charge, unitless scalar | vector

State of charge of one or multiple cells, specified as a scalar or vector of
entries in the range [0,1]. The size of this input port must be equal to the size of
the **CellTemperature** input port and to the value of the
**Number of series modules, Ns** parameter.

### **CellTemperature** — Cell temperature, K scalar | vector

Cell temperature, specified as a scalar for a single cell or a vector for multiple
cells. The size of this input port must be equal to the size of the
**CellSOC** input port and to the value of the **Number of
series modules, Ns** parameter.
### Output

### **MaxPowerDischarging** — Maximum power for discharging battery, W scalar

Maximum power for discharging the battery over the prediction horizon.

### **MaxPowerCharging** — Maximum power for charging battery, W scalar

Maximum power for charging the battery over the prediction horizon.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Battery

### **Vector of state-of-charge values, SOC (-)** — SOC breakpoints `[0, .1, .25, .5, .75, .9, 1]` (default) | vector of scalars in the range [0, 1]

Vector of the state-of-charge breakpoints that defines the points at which you
specify lookup data. The entries of this vector must be in strictly ascending order.
The block calculates the state-of-charge value with respect to the nominal battery
capacity specified in the **Cell capacity, AH (A\*Hr)** parameter. The
SOC is the ratio of the available battery charge
*q*battery and the nominal battery capacity
*q*nom*(T,n)*. Make sure
that, for each temperature value, an SOC of 1 represents the battery charge capacity
for the corresponding element of the **Cell capacity, AH (A\*Hr)**
parameter when you model a fresh battery with a number of cycles *N*
equal to 1 and *δAH(n = 1,
Tfade)* equal to 0:

SOC=qbatteryqnom(T,n)  for N=1 and δAH(n,Tfade)=0,  qnom(T,n)=AH.

### **Vector of temperatures, T** — Temperature breakpoints `[278, 293, 313]` (default) | vector of positive scalars

Vector of temperature breakpoints that defines the points at which you specify
lookup data. This vector must be strictly ascending and greater than 0 K. The physical
unit of this parameter must be the same as the physical unit of the
**CellTemperature** input port.

### **No-load voltage, V0(SOC,T), (V)** — *V*0 lookup table `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]` (default) | matrix of nonnegative entries

Lookup data, in volt, for open-circuit voltages across the fundamental battery
model at the specified SOC. The number of rows of this matrix is equal to the size of
the **Vector of state-of-charge values, SOC (-)** parameter. The
number of columns of this matrix is equal to the size of the **Vector of
temperatures, T** parameter.

### **Charging pulse test resistance, R0Dt(SOC,T), (ohm)** — Charging resistances over pulse of `Δt` seconds `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` (default) | matrix of nonnegative entries

Charging resistances over a pulse of `Δt` seconds. The number of
rows of this matrix is equal to the size of the **Vector of state-of-charge
values, SOC (-)** parameter. The number of columns of this matrix is equal
to the size of the **Vector of temperatures, T** parameter.

### **Discharging pulse test resistance, R0Dt(SOC,T), (ohm)** — Discharging resistances over pulse of `Δt` seconds `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` (default) | matrix of nonnegative entries

Discharging resistances over a pulse of `Δt` seconds. The number
of rows of this matrix is equal to the size of the **Vector of state-of-charge
values, SOC (-)** parameter. The number of columns of this matrix is equal
to the size of the **Vector of temperatures, T** parameter.

### **Cell capacity, AH (A\*Hr)** — Battery capacity when fully charged `27` (default) | nonnegative scalar

Cell capacity of the battery, in ampere-hour. The block calculates the state of
charge by dividing the accumulated charge by this value. The block calculates the
accumulated charge by integrating the battery current.

### **Number of series modules, Ns** — Number of modules in series `10` (default) | positive scalar

Number of series-connected modules inside the battery pack.

### **Number of parallel modules, Np** — Number of modules in parallel `1` (default) | positive scalar

Number of parallel-connected modules inside the battery pack.

### **Charging efficiency ratio** — Ratio of charging efficiency `1` (default) | nonnegative scalar in the range (0,1]

Ratio of the charging efficiency.

### Limits

### **Minimum cell voltage (V)** — Minimum voltage of cell `2.5` (default) | positive scalar

Minimum voltage of the battery cell, in volt. The value of this parameter must be
less than the value of the **Maximum cell voltage (V)**
parameter.

### **Maximum cell voltage (V)** — Maximum voltage of cell `4.5` (default) | positive scalar

Maximum voltage of the battery cell, in volt. The value of this parameter must be
greater than the value of the **Minimum cell voltage (V)**
parameter.

### **Minimum state of charge, SOCmin(-)** — Minimum state of charge `0.1` (default) | nonnegative scalar in the range [0,1]

Minimum state of charge of the battery cell. The value of this parameter must be
less than the value of the **Maximum state of charge, SOCmin(-)**
parameter.

### **Maximum state of charge, SOCmax(-)** — Maximum state of charge `0.9` (default) | nonnegative scalar in the range [0,1]

Maximum state of charge of the battery cell. The value of this parameter must be
greater than the value of the **Minimum state of charge, SOCmax(-)**
parameter.

### **Minimum pack current (A)** — Minimum current of pack `-200` (default) | negative scalar

Minimum current of the battery pack, in ampere. The value of this parameter must
be less than the value of the **Maximum pack current (A)** parameter.
If you set this value to `-inf`, the block ignores this
parameter.

### **Maximum pack current (A)** — Maximum current of pack `200` (default) | positive scalar

Maximum current of the battery pack, in ampere. The value of this parameter must
be greater than the value of the **Minimum pack current (A)**
parameter. If you set this value to `inf`, the block ignores this
parameter.

### **Minimum cell power (W)** — Minimum power of battery cell `-inf` (default) | negative scalar

Minimum power of the battery cell, in watt. The value of this parameter must be
less than the value of the **Maximum cell power (W)** parameter. If
you set this value to `-inf`, the block ignores this
parameter.

### **Maximum cell power (W)** — Maximum power of battery cell `inf` (default) | positive scalar

Maximum power of the battery cell, in watt. The value of this parameter must be
greater than the value of the **Minimum cell power (W)** parameter.
If you set this value to `inf`, the block ignores this
parameter.

### **Time horizon (s)** — Time horizon `10` (default) | positive scalar

Time, in seconds, over which the block calculates the maximum charging and
discharging power capabilities of the battery pack.

### Signal Attributes

### **Algorithm data type** — Option to choose data type for block algorithm `Inherit: auto` (default) | `double` | `single` | `<data type expression>`

*Since R2025a*

Option to choose the data type for the block algorithm, specified as one of these values:

- `Inherit: auto` — You can simulate the block in
  both `single` and `double`
  precision. You must explicitly provide the inputs and parameters as either
  `single` or
  `double`.
- `double` — The block algorithm casts all inputs
  and parameters to `double` data type.
- `single` — The block algorithm casts all inputs
  and parameters to `single` data type.
- `<data type expression>` — The block
  algorithm casts all inputs and parameters to the data type object you
  specify.

Click the **Show data type assistant** button  to display the **Data Type Assistant**, which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant and Control Data Types of Signals.

## Libraries

Simscape / Battery / BMS / Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

## Description

Calculate maximum charging and discharging power of battery pack over time horizon

The Battery Power Estimator block calculates the maximum charging and
discharging power capabilities of a battery pack across a specified time horizon. This block
adheres to the sign convention where the current and power are positive values during the
battery charging process.

This diagram shows the structure of the block:

### Equations

To estimate the maximum charging and discharging power capabilities of a battery pack,
the Battery Power Estimator block uses the hybrid pulse power
characterization (HPPC) method [1].

Diagram of pulse test voltage, on the Y axis, versus time, on the X axis

To calculate the discharging and charging currents, the block uses these equations,

idischg,volt,n=−V0(SOC,T)−vminRdischgDtichg,volt,n=−V0(SOC,T)−vmaxRchgDt

where:

- `V0(SOC,T)` is the open-circuit
  voltage.
- `vmin` and
  `vmax` are the minimum and maximum cell
  voltages.
- `RdischgDt` and
  `RchgDt` are the discharging and charging
  resistances over a pulse of `Δt` seconds.
- `idischg,volt,n` and
  `ichg,volt,n` are the discharging and
  charging currents for the `n`th cell based on the voltage
  constraints.

For a constant current `in`, the state-of-charge
(SOC) relationship is

SOCn(t+Δt)=SOCn(t)−η Δt in 3600 Q,

where:

- *Q* is the capacity in ampere-hour.
- *SOCn* is the state of charge of the
  *n*th cell.
- *η* is the efficiency factor, with *η* =
  *1* for discharging and *η* ≤ `1`
  for charging.

Minimum and a maximum permissible values limit the state of charge for all cells in the
pack such that

SOCmin≤SOCn(t)≤SOCmax.

The block then computes the current limits based on the SOC:

idischg,SOC,n=−3600⋅Q⋅(SOCn−SOCmin)Δtichg,SOC,n=−3600⋅Q⋅(SOCn−SOCmax)ηΔt

To calculate the discharging and charging currents of the entire battery
pack, the block uses these equations:

idischg=max(imin,maxnidischg,SOC,n,maxnidischg,volt,n)ichg=min(imax,minnichg,SOC,n,minnichg,volt,n)

Finally, the block calculates the charging and discharging power limits
for a prediction horizon `Δt`:

Pmax,dischg=Npmax(NsPmin,∑n=1Nsidischg(V0(SOCn(t)−idischgΔt3600 Q,T)−idischgRdischgDt))Pmin,chg=Npmin(NsPmax,∑n=1Nsichg(V0(SOCn(t)−ichgηΔt3600 Q,T)−ichgRchgDt))

where *Np* is the number of
parallel modules and *Ns* is the number of series
modules.

### Assumptions and Limitations

During the battery charging process, the current and power are positive values.
