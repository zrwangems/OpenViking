---
type: simulink-block
title: 'Solar Cell'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'solarcell'
documentation_source_path: 'ref/solarcell.html'
language: en
---

# Solar Cell

## Ports
```yaml
ports:
- name: Ir
  summary: Incident irradiance physical signal
  direction: input
- name: +
  summary: Positive voltage electrical
  direction: conserving
- name: '-'
  summary: Negative voltage electrical
  direction: conserving
- name: H
  summary: Thermal port thermal
  direction: conserving
```

### Input

### **Ir** — Incident irradiance physical signal

Physical signal associated with the solar cell incident
irradiance.
### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the solar cell positive
voltage.

### **-** — Negative voltage electrical

Electrical conserving port associated with the solar cell negative
voltage.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Selected part
  summary: Predefined parameterization option <click to select> (default)
  group: ''
- name: Modeling option
  summary: Whether to enable thermal port No thermal port (default) | Show thermal port
  group: ''
- name: Parameterize by
  summary: Block parameterization By s/c current and o/c voltage, 5 parameter (default) | By equivalent circuit parameters,
    5 parameter | By equivalent circuit parameters, 8 parameter
  group: Cell Characteristics
- name: Short-circuit current, Isc
  summary: Short-circuit current 7.34 A (default)
  group: Cell Characteristics
- name: Open-circuit voltage, Voc
  summary: Open-circuit voltage 0.6 V (default)
  group: Cell Characteristics
- name: Diode saturation current, Is
  summary: First diode saturation current 1e-6 A (default)
  group: Cell Characteristics
- name: Diode saturation current, Is2
  summary: Second diode saturation current 0 A (default)
  group: Cell Characteristics
- name: Solar-generated current for measurements, Iph0
  summary: Solar-generated current for measurements 7.34 A (default)
  group: Cell Characteristics
- name: Irradiance used for measurements, Ir0
  summary: Irradiance used for measurements 1000 W/m2 (default)
  group: Cell Characteristics
- name: Quality factor, N
  summary: First diode emission coefficient 1.5 (default)
  group: Cell Characteristics
- name: Quality factor, N2
  summary: Second diode emission coefficient 2 (default)
  group: Cell Characteristics
- name: Series resistance, Rs
  summary: Series resistance 0 Ohm (default)
  group: Cell Characteristics
- name: Parallel resistance, Rp
  summary: Parallel resistance inf Ohm (default)
  group: Cell Characteristics
- name: Number of series-connected cells per string
  summary: Series-connected solar cells per string 1 (default) | positive scalar
  group: Panel Configuration
- name: Number of parallel-connected strings
  summary: Number of parallel-connected strings 1 (default) | positive scalar
  group: Panel Configuration
- name: First order temperature coefficient for Iph, TIPH1
  summary: First order temperature coefficient for Iph 0 1/K (default) | nonnegative scalar
  group: Temperature Dependence
- name: Energy gap, EG
  summary: Energy gap 1.11 eV (default)
  group: Temperature Dependence
- name: Temperature exponent for Is, TXIS1
  summary: Temperature exponent for Is 3 (default) | positive scalar
  group: Temperature Dependence
- name: Temperature exponent for Is2, TXIS2
  summary: Temperature exponent for Is2 3 (default) | nonnegative scalar
  group: Temperature Dependence
- name: Temperature exponent for Rs, TRS1
  summary: Temperature exponent for Rs 0 (default)
  group: Temperature Dependence
- name: Temperature exponent for Rp, TRP1
  summary: Temperature exponent for Rp 0 (default) | nonnegative scalar
  group: Temperature Dependence
- name: Measurement temperature
  summary: Measurement temperature 25 degC (default) | positive scalar
  group: Temperature Dependence
- name: Device simulation temperature
  summary: Device simulation temperature 25 degC (default) | positive scalar
  group: Temperature Dependence
- name: Thermal mass per cell
  summary: Thermal mass per cell 100 J/K (default)
  group: Thermal port
- name: Initial temperature
  summary: Initial temperature 25 degC (default)
  group: Thermal port
```

### **Selected part** — Predefined parameterization option `<click to select>` (default)

Option to parameterize the block to represent components by specific suppliers. Click the
**<click to select>** hyperlink to open the Block
Parameterization Manager window. For more information about the Block Parameterization
Manager, see Load Predefined Parameterizations.

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of generated heat and device temperature.

### Cell Characteristics

All quantities in this setting are for a single cell.

### **Parameterize by** — Block parameterization `By s/c current and o/c voltage, 5 parameter` (default) | `By equivalent circuit parameters, 5 parameter` | `By equivalent circuit parameters, 8 parameter`

Select one of the following methods for block parameterization:

- `By s/c current and o/c voltage, 5
  parameter` — Provide short-circuit
  current and open-circuit voltage that the block converts to
  an equivalent circuit model of the solar cell.
- `By equivalent circuit parameters, 5
  parameter` — Provide electrical
  parameters for an equivalent circuit model of the solar cell
  using the 5-parameter solar cell model that makes the
  following assumptions:

  - The saturation current of the second diode is
    zero.
  - The parallel resistor has infinite
    impedance.
- `By equivalent circuit parameters, 8
  parameter` — Provide electrical
  parameters for an equivalent circuit model of the solar cell
  using the 8-parameter solar cell model.

### **Short-circuit current, Isc** — Short-circuit current `7.34` `A` (default)

Current that flows when you short-circuit the solar cell.

#### Dependencies

This parameter is visible only when you select `By s/c
current and o/c voltage, 5 parameter` for the
**Parameterize by** parameter.

### **Open-circuit voltage, Voc** — Open-circuit voltage `0.6` `V` (default)

Voltage across the solar cell when it is not connected.

#### Dependencies

This parameter is visible only when you select `By s/c
current and o/c voltage, 5 parameter` for the
**Parameterize by** parameter.

### **Diode saturation current, Is** — First diode saturation current `1e-6` `A` (default)

Asymptotic reverse current of the first diode for increasing reverse
bias in the absence of any incident light.

#### Dependencies

This parameter is visible only when you select `By
equivalent circuit parameters, 5 parameter` or
`By equivalent circuit parameters, 8
parameter` for the **Parameterize
by** parameter.

### **Diode saturation current, Is2** — Second diode saturation current `0` `A` (default)

Asymptotic reverse current of the second diode for increasing reverse
bias in the absence of any incident light.

#### Dependencies

This parameter is visible only when you select `By
equivalent circuit parameters, 8 parameter` for the
**Parameterize by** parameter.

### **Solar-generated current for measurements, Iph0** — Solar-generated current for measurements `7.34` `A` (default)

Solar-induced current when the irradiance is
*Ir0*.

#### Dependencies

This parameter is visible only when you select `By
equivalent circuit parameters, 5 parameter` or
`By equivalent circuit parameters, 8
parameter` for the **Parameterize
by** parameter.

### **Irradiance used for measurements, Ir0** — Irradiance used for measurements `1000` `W/m2` (default)

Irradiance that produces a current of
*Iph0* in the solar
cell.

### **Quality factor, N** — First diode emission coefficient `1.5` (default)

Emission coefficient of the first diode.

### **Quality factor, N2** — Second diode emission coefficient `2` (default)

Emission coefficient of the second diode.

#### Dependencies

This parameter is visible only when you select `By
equivalent circuit parameters, 8 parameter` for the
**Parameterize by** parameter.

### **Series resistance, Rs** — Series resistance `0` `Ohm` (default)

Internal series resistance.

### **Parallel resistance, Rp** — Parallel resistance `inf` `Ohm` (default)

Internal parallel resistance.

#### Dependencies

This parameter is visible only when you select `By
equivalent circuit parameters, 8 parameter` for the
**Parameterize by** parameter.

### Panel Configuration

### **Number of series-connected cells per string** — Series-connected solar cells per string `1` (default) | positive scalar

Number of series-connected solar cells per string modeled by the
block. The value must be greater than `0`.

### **Number of parallel-connected strings** — Number of parallel-connected strings `1` (default) | positive scalar

Number of strings connected in parallel. The value must be greater
than `0`.

### Temperature Dependence

### **First order temperature coefficient for Iph, TIPH1** — First order temperature coefficient for Iph `0` `1/K` (default) | nonnegative scalar

Order of the linear increase in the solar-generated current as
temperature increases. The value must be greater than or equal to
`0`.

### **Energy gap, EG** — Energy gap `1.11` `eV` (default)

Solar cell activation energy. The value must be greater than or equal
to 0.1.

### **Temperature exponent for Is, TXIS1** — Temperature exponent for Is `3` (default) | positive scalar

Order of the exponential increase in the current from the first diode
as temperature increases. The value must be greater than
`0`.

### **Temperature exponent for Is2, TXIS2** — Temperature exponent for Is2 `3` (default) | nonnegative scalar

Order of the exponential increase in the current from the second diode
as temperature increases. The value must be greater than or equal to
`0`.

#### Dependencies

This parameter is visible only when you select `By
equivalent circuit parameters, 8 parameter` for the
**Parameterize by** parameter.

### **Temperature exponent for Rs, TRS1** — Temperature exponent for Rs `0` (default)

Order of the exponential increase in the series resistance as
temperature increases. The value must be greater than or equal to
`0`.

### **Temperature exponent for Rp, TRP1** — Temperature exponent for Rp `0` (default) | nonnegative scalar

Order of the exponential increase in the parallel resistance as
temperature increases. The value must be greater than or equal to
`0`.

#### Dependencies

This parameter is visible only when you select `By
equivalent circuit parameters, 8 parameter` for the
**Parameterize by** parameter.

### **Measurement temperature** — Measurement temperature `25` `degC` (default) | positive scalar

Temperature at which the solar cell parameters were measured. The
value must be greater than `0`.

### **Device simulation temperature** — Device simulation temperature `25` `degC` (default) | positive scalar

Temperature at which the solar cell is simulated. The value must be
greater than `0`.

### Thermal port

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Thermal mass per cell** — Thermal mass per cell `100` `J/K` (default)

The heat energy required to raise the temperature of one solar cell by
one degree. When modeling more than one cell in series, specify the
thermal mass for a single cell. This value gets multiplied internally by
the number of cells to determine the total thermal mass.

### **Initial temperature** — Initial temperature `25` `degC` (default)

The temperature of the solar cell at the start of simulation.
## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

### R2024b: Generate Digital Datasheet

You can now generate a digital datasheet for the Solar Cell block, including
current-voltage (I-V) and power-voltage (P-V) curves, using a MATLAB live script. The script imports the parameters from the Solar Cell
block you select in the model. You can use these characteristic curves to evaluate
the maximum power point tracking (MPPT) output, because the curves help to identify
the peak power at various irradiance levels and cell temperatures.

## Description

Photovoltaic solar cell

The Solar Cell block represents a solar cell current
source.

The solar cell model includes the following components:

- Solar-Induced Current
- Temperature Dependence
- Predefined Parameterization
- Thermal Port
- Generate Digital Datasheet

### Solar-Induced Current

The block represents a single solar cell as a resistance
*Rs* that is connected in series
with a parallel combination of the following elements:

- Current source
- Two exponential diodes
- Parallel resistor *Rp*

The following illustration shows the equivalent circuit diagram:

The output current *I* is

I=Iph−Is\*(e(V+I\*Rs)/(N\*Vt)−1)−Is2\*(e(V+I\*Rs)/(N2\*Vt)−1)−(V+I\*Rs)/Rp

where:

- *Iph* is the solar-induced
  current:

  Iph=Iph0×IrIr0

  where:

  - *Ir* is the
    irradiance (light intensity), in
    W/m2, falling on the
    cell.
  - *Iph0* is the
    measured solar-generated current for the irradiance
    *Ir0*.
- *Is* is the saturation current
  of the first diode.
- *Is2* is the saturation
  current of the second diode.
- *Vt* is the thermal voltage,
  *kT/q*, where:

  - *k* is the Boltzmann constant.
  - *T* is the **Device simulation
    temperature** parameter value.
  - *q* is the elementary charge on an
    electron.
- *N* is the quality factor (diode emission
  coefficient) of the first diode.
- *N2* is the quality factor
  (diode emission coefficient) of the second diode.
- *V* is the voltage across the solar cell electrical
  ports.

The quality factor varies for amorphous cells, and is typically
`2` for polycrystalline cells.

The block lets you choose between two models:

- An 8-parameter model where the preceding equation describes the output
  current
- A 5-parameter model that applies the following simplifying assumptions
  to the preceding equation:

  - The saturation current of the second diode is zero.
  - The impedance of the parallel resistor is infinite.

If you choose the 5-parameter model, you can parameterize this block
in terms of the preceding equivalent circuit model parameters or in terms of the
short-circuit current and open-circuit voltage the block uses to derive these
parameters.

All models adjust the block resistance and current parameters as a function of
temperature.

You can model any number of solar cells connected in series using a single
Solar Cell block by setting the parameter
**Number of series-connected cells per string** to a value
larger than 1. Internally the block still simulates only the equations for a single
solar cell, but scales up the output voltage according to the number of cells. This
results in a more efficient simulation than if equations for each cell were
simulated individually.

### Temperature Dependence

Several solar cell parameters depend on temperature. The solar cell temperature is
specified by the **Device simulation temperature** parameter
value.

The block provides the following relationship between the solar-induced current
*Iph* and the solar cell temperature
*T*:

Iph(T)=Iph\*(1+TIPH1\*(T−Tmeas))

where:

- *TIPH1* is the **First order temperature
  coefficient for Iph, TIPH1** parameter value.
- *Tmeas* is the
  **Measurement temperature** parameter value.

The block provides the following relationship between the saturation current of
the first diode *Is* and the solar cell
temperature *T*:

Is(T)=Is\*(TTmeas)(TXIS1N)\*e(EG\*(TTmeas−1)/(N\*Vt))

where *TXIS1* is the **Temperature
exponent for Is, TXIS1** parameter value.

The block provides the following relationship between the saturation current of
the second diode *Is2* and the solar cell
temperature *T*:

Is2(T)=Is2\*(TTmeas)(TXIS2N2)\*e(EG\*(TTmeas−1)/(N2\*Vt))

where *TXIS2* is the **Temperature
exponent for Is2, TXIS2** parameter value.

The block provides the following relationship between the series resistance
*Rs* and the solar cell temperature
*T*:

Rs(T)=Rs\*(TTmeas)TRS1

where *TRS1* is the **Temperature
exponent for Rs, TRS1** parameter value.

The block provides the following relationship between the parallel resistance
*Rp* and the solar cell temperature
*T*:

Rp(T)=Rp\*(TTmeas)TRP1

where *TRP1* is the **Temperature
exponent for Rp, TRP1** parameter value.

### Predefined Parameterization

There are multiple available built-in parameterizations for the Solar Cell
block.

This pre-parameterization data allows you to set up the block to represent
components by specific suppliers. The parameterizations of these solar cell modules
match the manufacturer data sheets. To load a predefined parameterization,
double-click the Solar Cell block, click the **<click to
select>** hyperlink of the **Selected part** parameter
and, in the Block Parameterization Manager window, select the part you want to use
from the list of available components.

**Note**

The predefined parameterizations of Simscape™ components use available data sources for the parameter values. Engineering
judgment and simplifying assumptions are used to fill in for missing data. As a result,
expect deviations between simulated and actual physical behavior. To ensure accuracy,
validate the simulated behavior against experimental data and refine component models as
necessary.

For more information about pre-parameterization and for a list of the available
components, see List of Pre-Parameterized Components.

### Thermal Port

You can expose the thermal port to model the effects of generated heat and device
temperature. To expose the thermal port, set the **Modeling option**
parameter to either:

- `No thermal port` — The block does not contain a
  thermal port and does not simulate heat generation in the device.
- `Show thermal port` — The block contains a thermal
  port that allows you to model the heat that conduction losses generate. For
  numerical efficiency, the thermal state does not affect the electrical behavior
  of the block.

For more information on using thermal ports and on the **Thermal Port**
parameters, see Simulating Thermal Effects in Semiconductors.

The thermal port model, shown in the following illustration, represents just the
thermal mass of the device. The thermal mass is directly connected to the component
thermal port **H**. An internal Ideal Heat Flow
Source block supplies a heat flow to the port and thermal mass.
This heat flow represents the internally generated heat.

The internally generated heat in the solar cell is calculated according to the
equivalent circuit diagram, shown at the beginning of the reference page, in the
Solar-Induced Current section. It is the
sum of the *i*2 ·
*R* losses for each of the resistors plus the losses in each of
the diodes.

The internally generated heat due to electrical losses is a separate heating
effect to that of the solar irradiation. To model thermal heating due to solar
irradiation, you must account for it separately in your model and add the heat flow
to the physical node connected to the solar cell thermal port.

### Generate Digital Datasheet

*Since R2024b*

Generate a digital datasheet for the Solar Cell block, including current-voltage
(I-V) and power-voltage (P-V) curves, using a MATLAB® live script. The script imports the parameters from the Solar Cell
block you select in the model. You can use these characteristic curves to evaluate
the maximum power point tracking (MPPT) output, because the curves help to identify
the peak power at various irradiance levels and cell temperatures. To open the
MATLAB live script:

1. Double-click the block to open the **Block
   Parameters** window.
2. Open the **Description** tab.
3. Click the `Generate datasheet` hyperlink.

To generate the datasheet, in the live script, click the `Generate
Datasheet` button.
