---
type: simulink-block
title: 'Integer N PLL with Single Modulus Prescaler'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Phase-Locked Loops / Reference Architectures'
documentation_page: 'integernpllwithsinglemodulusprescaler'
documentation_source_path: 'ref/integernpllwithsinglemodulusprescaler.html'
language: en
---

# Integer N PLL with Single Modulus Prescaler

## Ports

### Input

### **clk in** — Input clock signal scalar

Input clock signal, specified as a scalar. The signal at the **clk
in** port is used as the reference signal for the PFD block in
a PLL system.

**Data Types:** `double`
### Output

### **clk out** — Output clock signal scalar

Output clock signal, specified as a scalar. The signal at the **clk
out** port is the output of the VCO block in
a PLL system.

**Data Types:** `double`

## Parameters

### **Edit System** — Break library block links and replace internal variables by appropriate values button

Click to break the block links to the library. The internal variables are replaced
by their values and the block becomes a simple subsystem.

### **Enable increased buffer size** — Enable increased buffer size button

Select to enable increased buffer size during the simulation. This increases the
buffer size of all the building blocks in the PLL model that belong to the Mixed-Signal Blockset™/PLL/Building Blocks Simulink® library. The building blocks are PFD, Charge Pump,
Loop Filter,
VCO, and
Single Modulus
Prescaler. By default, this option is deselected.

### **Buffer size for loop filter** — Buffer size for loop filter `1000` (default) | positive integer scalar

Buffer size for the loop filter, specified as a positive integer scalar. This sets
the number of extra buffer samples available during the simulation to the Convert Sample
Time subsystem inside the loop filter.

Selecting different simulation solver or sampling strategies can change the number
of input samples needed to produce an accurate output sample. Set the **Buffer
size for loop filter** to a large enough value so that the input buffer
contains all the input samples required.

#### Dependencies

This parameter is only available when the **Enable increased buffer
size** option is selected.

#### Programmatic Use

- Use `get_param(gcb,'NBufferFilter')` to view the current
  value of **Buffer size for loop filter**.
- Use `set_param(gcb,'NBufferFilter',value)` to set
  **Buffer size for loop filter** to a specific value.

### **Buffer size for PFD, charge pump, VCO, prescaler** — Buffer size for PFD, charge pump, VCO, and prescaler `10` (default) | positive integer scalar

Buffer size for the PFD, charge pump, VCO, and prescaler, specified as a positive
integer scalar. This sets the buffer size of the PFD, Charge Pump,
VCO, and
Single Modulus
Prescaler blocks inside the PLL model.

Selecting different simulation solver or sampling strategies can change the number
of input samples needed to produce an accurate output sample. Set the **Buffer
size for PFD, charge pump, VCO, prescaler** to a large enough value so that
the input buffer contains all the input samples required.

#### Dependencies

This parameter is only available when the **Enable increased buffer
size** option is selected.

#### Programmatic Use

- Use `get_param(gcb,'NBuffer')` to view the current value of
  **Buffer size for PFD, charge pump, VCO, prescaler**.
- Use `set_param(gcb,'NBuffer',value)` to set
  **Buffer size for PFD, charge pump, VCO, prescaler** to a
  specific value.

### PFD

#### Configuration

### **Deadband compensation (s)** — Delay added for active output near zero phase offset `30e-12` (default) | positive real scalar

Delay added for active output near zero phase offset, specified as a positive real
scalar in seconds. Deadband is the phase offset band near zero phase offset for which
the PFD output is negligible.

#### Programmatic Use

- Use `get_param(gcb,'DeadbandCompensation')` to view the
  current value of **Deadband compensation (s)**.
- Use `set_param(gcb,'DeadbandCompensation',value)` to set
  **Deadband compensation (s)** to a specific value.

**Data Types:** `double`

#### Impairments

### **Enable impairments** — Add circuit impairments to simulation off (default) | on

Select to add circuit impairments such as rise/fall time and propagation delay to
simulation. By default, this option is deselected.

### **Output step size calculation** — Determine how output step size is calculated `Default` (default) | `Advanced`

Determine how output step size is calculated:

- Select `Default` to calculate output step size from rise/fall
  time. Output step size (ΔT) is given by ΔT=(Rise/fall time)26 · 0.22.
- Select `Advanced` to calculate output step size from maximum
  frequency of interest. Output step size (ΔT) is given by ΔT=Rise/fall time6 · Maximum frequency of interest.

#### Dependencies

To enable this parameter, select **Enable Impairments** in the
**PFD** tab.

### **Maximum frequency of interest (Hz)** — Maximum frequency of interest at output `10e9` (default) | positive real scalar

Maximum frequency of interest at the output, specified as a positive real scalar in
Hz.

#### Dependencies

To enable this parameter, select **Enable Impairments** in the
**PFD** tab and choose **Advanced** for
**Output step size calculation**.

#### Programmatic Use

- Use `get_param(gcb,'MaxFreqInterest')` to view the
  current value of **Maximum frequency of interest
  (Hz)**.
- Use `set_param(gcb,'MaxFreqInterest',value)` to set
  **Maximum frequency of interest (Hz)** to a specific
  value.

**Data Types:** `double`

### **Rise/fall time (s)** — 20% – 80% rise/fall time for up output port of PFD `30e-12` (default) | positive real scalar

20% – 80% rise/fall time for the up output port of the PFD, specified as a real
positive scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable Impairments** in the
**PFD** tab.

#### Programmatic Use

- Use `get_param(gcb,'RiseFallTime')` to view the current
  value of **Rise/fall time (s)**.
- Use `set_param(gcb,'RiseFallTime',value)` to set
  **Rise/fall time (s)** to a specific value.

### **Propagation Delay (s)** — Delay from input port to output port of PFD `50e-12` (default) | positive real scalar

Delay from the input port to output port of the PFD, specified as a positive real
scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable Impairments** in the
**PFD** tab.

#### Programmatic Use

- Use `get_param(gcb,'PropDelay')` to view the current
  value of **Propagation Delay (s)**.
- Use `set_param(gcb,'PropDelay',value)` to set
  **Propagation Delay (s)** to a specific value.

**Data Types:** `double`

### Charge pump

#### Configuration

### **Output current (A)** — Design output current `1e-3` (default) | positive real scalar

Full scale magnitude of design output current, specified as a positive real scalar in
amperes. This parameter is also reported as **Charge pump current** in
the **Loop Filter** tab and is used to automatically calculate the
filter component values of the loop filter. This parameter is tunable.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputCurrent` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e-3` |

**Data Types:** `double`

### **Input threshold (V)** — Logic switching threshold at input ports `0.5` (default) | real scalar

Logic switching threshold at input ports, specified as a real scalar in volts.

#### Programmatic Use

- Use `get_param(gcb,'InputThreshold')` to view the
  current value of **Input threshold (V)**.
- Use `set_param(gcb,'InputThreshold',value)` to set
  **Input threshold (V)** to a specific value.

**Data Types:** `double`

#### Impairments

### **Enable current impairments** — Add current impairments to simulation off (default) | on

Select to add current impairments such as current imbalance and leakage current to
simulation. By default, this option is deselected.

### **Current imbalance (A)** — Difference between full scale positive and negative current `1e-7` (default) | positive real scalar

Difference between full scale positive and negative current, specified as a positive
real scalar in amperes.

#### Dependencies

To enable this parameter, select **Enable current impairments**
in the **Charge pump** tab.

#### Programmatic Use

- Use `get_param(gcb,'CurrentImbalance')` to view the
  current value of **Current imbalance (A)**.
- Use `set_param(gcb,'CurrentImbalance',value)` to set
  **Current imbalance (A)** to a specific value.

**Data Types:** `double`

### **Leakage current (A)** — Output current without any input `1e-8` (default) | nonnegative real scalar

Output current when both inputs are at logic zero, specified as a nonnegative real
scalar in amperes.

#### Dependencies

To enable this parameter, select **Enable current impairments**
in the **Charge pump** tab.

#### Programmatic Use

- Use `get_param(gcb,'LeakageCurrent')` to view the
  current value of **Leakage current (A)**.
- Use `set_param(gcb,'LeakageCurrent',value)` to set
  **Leakage current (A)** to a specific value.

**Data Types:** `double`

### **Enable timing impairments** — Add timing impairments to simulation off (default) | on

Select to add timing impairments such as rise/fall time and propagation delay to
simulation. By default, this option is deselected.

### **Output step size calculation** — Determine how output step size is calculated `Default` (default) | `Advanced`

Determine how output step size is calculated:

- Select `Default` to calculate output step size from rise/fall
  time. Output step size (ΔT) is given by ΔT=(Rise/fall time)26 · 0.22.
- Select `Advanced` to calculate output step size from maximum
  frequency of interest. Output step size (ΔT) is given by ΔT=Rise/fall time6 · Maximum frequency of interest.

#### Dependencies

To enable this parameter, select **Enable timing impairments** in
the **Charge Pump** tab.

### **Maximum frequency of interest (Hz)** — Maximum frequency of interest at output `10e9` (default) | positive real scalar

Maximum frequency of interest at the output, specified as a positive real scalar in
Hz.

#### Dependencies

To enable this parameter, select **Enable timing impairments** in
the **Charge Pump** tab and choose **Advanced**
for **Output step size calculation**.

#### Programmatic Use

- Use `get_param(gcb,'MaxFreqInterestCp')` to view the
  current value of **Maximum frequency of interest
  (Hz)**.
- Use `set_param(gcb,'MaxFreqInterestCp',value)` to set
  **Maximum frequency of interest (Hz)** to a specific
  value.

**Data Types:** `double`

#### Up

### **Rise/fall time (s)** — 20% – 80% rise/fall time for up input port `5e-9` (default) | positive real scalar

20% – 80% rise/fall time for the up input port of the charge pump, specified as a
positive real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable timing impairments** in
the **Charge pump** tab.

#### Programmatic Use

- Use `get_param(gcb,'RiseFallUp')` to view the current
  value of **Up Rise/fall time (s)**.
- Use `set_param(gcb,'RiseFallUp',value)` to set
  **Up Rise/fall time (s)** to a specific value.

**Data Types:** `double`

### **Propagation delay (s)** — Total propagation delay from up input port to output port of charge pump `6e-9` (default) | positive real scalar

Total propagation delay from the up input port to output port of the charge pump,
specified as a positive real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable timing impairments** in
the **Charge pump** tab.

#### Programmatic Use

- Use `get_param(gcb,'PropDelayUp')` to view the current
  value of **Up Propagation delay (s)**.
- Use `set_param(gcb,'PropDelayUp',value)` to set
  **Up Propagation delay (s)** to a specific
  value.

**Data Types:** `double`

#### Down

### **Rise/fall time** — 20% – 80% rise/fall time for down input port `2e-9` (default) | scalar

20% – 80% rise/fall time for down input port of charge pump.

#### Dependencies

To enable this parameter, select **Enable timing impairments** in
the **Charge pump** tab.

#### Programmatic Use

- Use `get_param(gcb,'RiseFallDown')` to view the current
  value of **Down Rise/fall time (s)**.
- Use `set_param(gcb,'RiseFallDown',value)` to set
  **Down Rise/fall time (s)** to a specific value.

**Data Types:** `double`

### **Propagation delay (s)** — Total propagation delay from up input port to output port of charge pump `4e-9` (default) | positive real scalar

Total propagation delay from the up input port to output port of the charge pump,
specified as a positive real scalar in seconds.

#### Dependencies

To enable this parameter, select **Enable timing impairments** in
the **Charge pump** tab.

#### Programmatic Use

- Use `get_param(gcb,'PropDelayUp')` to view the current
  value of **Down Propagation delay (s)**.
- Use `set_param(gcb,'PropDelayUp',value)` to set
  **Down Propagation delay (s)** to a specific
  value.

**Data Types:** `double`

### VCO

### **Specify using** — Define how VCO output frequency is specified `Voltage sensitivity` (default) | `Output frequency vs. control voltage`

Define how VCO output frequency is specified:

- Select `Voltage sensitivity` to specify output
  frequency from **Voltage sensitivity (Hz/V)** and
  **Free running frequency (Hz)**.
- Select `Output frequency vs. control voltage` to
  interpolate output frequency from **Control voltage (V)**
  vector versus **Output frequency (Hz)** vector.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SpecifyUsing` |
| **Type:** character vector |
| **Values:** `Voltage sensitivity` | `Output frequency vs. control voltage` |
| **Default:** `Voltage sensitivity` |

### **Voltage sensitivity (Hz/V)** — Measure of change in output frequency of VCO `100e6` (default) | positive real scalar

Measure of change in output frequency for input voltage change, specified as a
positive real scalar with units in Hz/V. This parameter is also reported as
**VCO voltage sensitivity** in the **Loop Filter**
tab and is used to automatically calculate the filter component values of the loop
filter.

#### Dependencies

To enable this parameter, select `Voltage sensitivity` in
**Specify using** in the **VCO** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Kvco` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `100e6` |

**Data Types:** `double`

### **Free running frequency (Hz)** — VCO output frequency without control voltage `1.8e9` (default) | positive real scalar

Frequency of the VCO without any control voltage input (`0` V), or
the quiescent frequency, specified as a positive real scalar in Hz.

#### Dependencies

To enable this parameter, select `Voltage sensitivity` in
**Specify using** in the **VCO** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Fo` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1.8e9` |

**Data Types:** `double`

### **Control voltage (V)** — Control voltage values `[-5 0 5]` (default) | real valued vector

Control voltage values of the VCO, specified as a real valued vector in volts.

#### Dependencies

To enable this parameter, select `Output frequency vs. control
voltage` in **Specify using** in the
**VCO** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ControlVoltage` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[-5 0 5]` |

**Data Types:** `double`

### **Output frequency (Hz)** — VCO output frequency values `[2e9 2.5e9 3e9]` (default) | real valued vector

Output frequency of the values of the VCO, corresponding to the **Control
voltage (V)** vector, specified in Hz.

#### Dependencies

To enable this parameter, select `Output frequency vs. control
voltage` in **Specify using** in the
**VCO** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputFrequency` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[2e9 2.5e9 3e9]` |

**Data Types:** `double`

### **Output amplitude** — Maximum amplitude of VCO output voltage `1` (default) | positive real scalar

Maximum amplitude of the VCO output voltage, specified as a positive real
scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Amplitude` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1` |

**Data Types:** `double`

#### Impairment

### **Add phase noise** — Add phase noise as function of frequency off (default) | on

Select to introduce phase noise as a function of frequency to the VCO. By default,
this option is deselected.

### **Phase noise frequency offset (Hz)** — Frequency offsets of phase noise from carrier frequency `[10e3 100e3 1e6 3e6 10e6]` (default) | real valued vector

Frequency offsets of the phase noise from the carrier frequency, specified as a real
valued vector in Hz.

#### Dependencies

To enable this parameter, select **Add phase noise** in the
**VCO** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Foffset` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[10e3 100e3 1e6 3e6 10e6]` |

**Data Types:** `double`

### **Phase noise level (dBc/Hz)** — Phase noise power at specified frequency offsets relative to the carrier `[-77 -108 -134 -145 -154]` (default) | real valued vector

Real valued vector specifying the phase noise power in a 1 Hz bandwidth centered at
the specified frequency offsets relative to the carrier. The value is specified in
dBc/Hz.

#### Dependencies

To enable this parameter, select **Add phase noise** in the
**VCO** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseNoise` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[-77 -108 -134 -145 -154]` |

**Data Types:** `double`

### **Estimate phase noise parameters** — Automatically estimate phase noise parameters on (default) | off

Select to automatically estimate the phase noise parameters. By default, this option
is selected.

You can deselect this option to define custom period jitter and flicker corner
frequency.

#### Dependencies

To enable this parameter, select **Add phase noise** in the
**VCO** tab.

**Data Types:** `double`

### **Period jitter (S)** — Standard deviation of period jitter `2.6794e-15` (default) | positive real scalar

Standard deviation of the period jitter, specified as a positive real scalar in
seconds. Period jitter is the deviation in cycle time of a clock signal with respect to
the ideal period.

To enable this parameter, select **Add phase noise** and deselect
**Estimate phase noise parameters** in the **VCO**
tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PeriodJitter` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `2.6794e-15` |

**Data Types:** `double`

### **Flicker corner frequency (Hz)** — Corner frequency of flicker noise `517103.8168` (default) | scalar

Corner frequency of the flicker noise, specified as a scalar in hertz.
**Flicker corner frequency (Hz)** is defined as the frequency at
which the phase noise transitions from
1/*f*2 to
1/*f*3 due to flicker noise. At this
frequency, the spectral densities of period jitter and flicker noise are equal.

#### Dependencies

To enable this parameter, select **Add phase noise** and deselect
**Estimate phase noise parameters** in the
**VCO** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CornerFrequency` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `517103.8168` |

**Data Types:** `double`

### **Plot fit** — Plot specified and expected VCO output phase noise density button

Click to plot the specified phase noise density and realizable expected output phase
noise density of the VCO.

### Prescaler

### **Clock divider value** — Value by which the clock divider divides the input frequency `100` (default) | real positive scalar

Value by which the clock divider divides the input frequency, specified as a real
positive scalar. This parameter is tunable.

#### Programmatic Use

- Use `get_param(gcb,'N')` to view the current value of
  **Clock divider value**.
- Use `set_param(gcb,'N',value)` to set **Clock
  divider value** to a specific value.

**Data Types:** `double`

### **Min clock divider value** — Minimum value by which clock divider can divide input frequency `100` (default) | real positive scalar

Minimum value by which the clock divider can divide input frequency, specified as
a real positive scalar. This parameter is also reported in the **Loop
Filter** tab and is used to automatically calculate the filter component
values of the loop filter.

#### Programmatic Use

- Use `get_param(gcb,'Nmin')` to view the current value of
  **Min clock divider value**.
- Use `set_param(gcb,'Nmin',value)` to set **Min
  clock divider value** to a specific value.

**Data Types:** `double`

### Loop Filter

### **Filter component values** — Determines how filter components are computed `Automatic` (default) | `Manual`

Select how filter components for the loop filter are computed:

- Select `Automatic` to automatically compute filter
  components from system specifications. Resistance and capacitance edit boxes in
  the **Loop Filter** tab are not editable if this option is
  selected. Rather, the filter component values are calculated from **Loop
  bandwidth (Hz)**, **Phase margin (degrees)**,
  **VCO voltage sensitivity**, **Charge pump
  current**, and **Min clock divider value**. By
  default, this option is selected.
- Select `Manual` to manually enter the resistance and
  capacitance values to design a customized loop filter.

### **Loop bandwidth (Hz)** — Frequency at which magnitude of open loop transfer function becomes 1 `2e6` (default) | positive real scalar

Frequency at which the magnitude of the open loop transfer function becomes 1,
specified as a positive real scalar in Hz. Lower values of **Loop bandwidth
(Hz)** result in reduced phase noise and reference spurs at the expense of
longer lock time and less phase margin.

#### Dependencies

This parameter is only available when `Automatic` is
selected for the **Filter Component values** parameter in the
**Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'Fc')` to view the current value of
  **Loop bandwidth (Hz)**.
- Use `set_param(gcb,'Fc',value)` to set **Loop
  bandwidth (Hz)** to a specific value.

**Data Types:** `double`

### **Phase margin (degrees)** — Phase of open loop transfer function at loop bandwidth subtracted from 180° `45` (default) | positive real scalar

Phase of the open loop transfer function at the loop bandwidth subtracted from 180°,
specified as a positive real scalar in degrees. For optimum lock time, select a phase
margin between 40° and 55°.

#### Dependencies

This parameter is only available when `Automatic` is
selected for the **Filter Component values** parameter in the
**Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'Phi')` to view the current value of
  **Phase margin (degrees)**.
- Use `set_param(gcb,'Phi',value)` to set **Phase
  margin (degrees)** to a specific value.

**Data Types:** `double`

### **Loop filter type** — Order of the loop filter `3rd Order Passive` (default) | `2nd Order Passive` | `4th Order Passive`

Order of the loop filter. Applies a second-, third-, or fourth-order passive RC loop
filter in the PLL system.

### **C1 (F)** — Capacitance 1 `1.31e-12` (default) | positive real scalar

Capacitor value C1, specified as a positive real scalar in farad.

#### Dependencies

This parameter is only editable when `Manual` is
selected for the **Filter Component values** parameter in the
**Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'C1')` to view the current value of
  **C1 (F)**.
- Use `set_param(gcb,'C1',value)` to set **C1
  (F)** to a specific value.

**Data Types:** `double`

### **C2 (F)** — Capacitance 2 `1.44e-11` (default) | positive real scalar

Capacitor value C2, specified as a positive real scalar in farad.

#### Dependencies

This parameter is only editable when `Manual` is
selected for the **Filter Component values** parameter in the
**Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'C2')` to view the current value of
  **C2 (F)**.
- Use `set_param(gcb,'C2',value)` to set **C2
  (F)** to a specific value.

**Data Types:** `double`

### **C3 (F)** — Capacitance 3 `9.41e-14` (default) | positive real scalar

Capacitor value C3, specified as a positive real scalar in farad.

#### Dependencies

- To enable this parameter, select `3rd Order
  Passive` or `4th Order Passive` in
  **Loop filter type**.
- This parameter is only editable when `Manual` is
  selected for the **Filter Component values** parameter in the
  **Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'C3')` to view the current value of
  **C3 (F)**.
- Use `set_param(gcb,'C3',value)` to set **C3
  (F)** to a specific value.

**Data Types:** `double`

### **C4 (F)** — Capacitance 4 `331.5752` (default) | positive real scalar

Capacitor value C4, specified as a positive real scalar in farad.

#### Dependencies

- To enable this parameter, select `4th Order
  Passive` in **Loop filter type**.
- This parameter is only editable when `Manual` is
  selected for the **Filter Component values** parameter in the
  **Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'C4')` to view the current value of
  **C4 (F)**.
- Use `set_param(gcb,'C4',value)` to set **C4
  (F)** to a specific value.

**Data Types:** `double`

### **R2 (ohms)** — Resistance 2 `1.33e+04` (default) | positive real scalar

Resistor value R2, specified as a positive real scalar in ohms.

#### Dependencies

This parameter is only editable when `Manual` is
selected for the **Filter Component values** parameter in the
**Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'R2')` to view the current value of
  **R2 (ohms)**.
- Use `set_param(gcb,'R2',value)` to set **R2
  (ohms)** to a specific value.

**Data Types:** `double`

### **R3 (ohms)** — Resistance 3 `1.7e+05` (default) | positive real scalar

Resistor value R3, specified as a positive real scalar in ohms.

#### Dependencies

- To enable this parameter, select `3rd Order
  Passive` or `4th Order Passive` in
  **Loop filter type**.
- This parameter is only editable when `Manual` is
  selected for the **Filter Component values** parameter in the
  **Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'R3')` to view the current value of
  **R3 (ohms)**.
- Use `set_param(gcb,'R3',value)` to set **R3
  (ohms)** to a specific value.

**Data Types:** `double`

### **R4 (ohms)** — Resistance 4 `28.1695` (default) | positive real scalar

Resistor value R4, specified as a positive real scalar in ohms.

#### Dependencies

- To enable this parameter, select `4th Order
  Passive` in **Loop filter type**.
- This parameter is only editable when `Manual` is
  selected for the **Filter Component values** parameter in the
  **Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'R4')` to view the current value of
  **R4 (ohms)**.
- Use `set_param(gcb,'R4',value)` to set **R4
  (ohms)** to a specific value.

**Data Types:** `double`

### **Enable impairments** — Add circuit impairments to simulation off (default) | on

Select to add circuit impairments such as operating temperature to determine thermal
noise to simulation. By default, this option is deselected.

### **Operating temperature (℃)** — Temperature to determine the level of thermal noise `30` (default) | real scalar

Temperature of the resistor, specified as a real scalar in ℃. **Operating
temperature** determines the level of thermal (Johnson) noise.

#### Dependencies

To enable this parameter, select **Enable impairments** in the
**Loop Filter** tab.

#### Programmatic Use

- Use `get_param(gcb,'Temperature')` to view the current
  value of **Operating temperature**.
- Use `set_param(gcb,'Temperature',value)` to set
  **Operating temperature** to a specific value.

**Data Types:** `double`

### **Export Loop Filter Component Values** — Export loop filter component values button

Click to export loop filter component values to a spreadsheet (XLS file) or as
comma-separated values (CSV file).

### Probe

### **PFD up and PFD down (pfd\_up and pfd\_down)** — Select to probe PFD outputs off (default) | on

Select to probe the PFD output wires (pfd\_up and pfd\_down) to view the response of
the PFD.

### **Charge pump output (cp\_out)** — Select to probe charge pump output off (default) | on

Select to probe the charge pump output wire (cp\_out) to view the response of the
Charge
Pump.

### **Loop filter output (lf\_out)** — Select to probe loop filter output off (default) | on

Select to probe loop filter output wire (lf\_out) to view the response of the
Loop Filter.
The loop filter output provides the control voltage to the VCO.

### **Prescaler output (ps\_out)** — Select to probe prescaler output off (default) | on

Select to probe the prescaler output wire (ps\_out) to view the response of the
Fractional Clock
Divider with Accumulator.

### Analysis

### **Open Loop Analysis** — Plot the presimulation open loop analysis on (default) | off

Select to plot the gain margin and phase margin of the PLL system before
simulation. By default, this option is selected.

### **Closed Loop Analysis** — Plot the presimulation closed loop analysis off (default) | on

Select to plot the pole-zero map, loop bandwidth, step response, and impulse
response of the PLL system before simulation. You must have a license to Control System Toolbox™ to plot the step response and impulse response of the PLL system. By
default, this option is deselected.

### **Plot Loop Dynamics** — Plot loop dynamics of PLL system button

Click to plot the presimulation loop dynamics of the PLL system.

### **Estimate phase noise** — Estimate phase noise from input clock off (default) | on

Select to estimate the phase noise from the input clock. By default, this option is
deselected.

### **Reference frequency (Hz)** — Reference frequency of input clock `10e6` (default) | positive real scalar

Reference frequency of input clock, specified as a positive real scalar.

#### Dependencies

To enable this parameter, select **Estimate Phase Noise** in the
**Analysis** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `RefFreq` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `10e6` |

### **Resolution bandwidth (Hz)** — Smallest positive frequency that can be resolved `10e3` (default) | positive real scalar

Smallest positive frequency that can be
resolved, specified as a real positive scalar. The **Resolution bandwidth
(Hz)** is used to determine window length for spectral analysis using the
Welch method. For more information, see Welch's Method of Averaged Modified Periodograms.

In general, **Resolution bandwidth
(Hz)** should be less than the lowest offset frequency value.

#### Dependencies

To enable this parameter, select **Estimate Phase Noise** in the
**Analysis** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Rbw` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `10e3` |

### **Frequency offset vector (Hz)** — Frequency points relative to fundamental frequency where phase noise is calculated `[10e3 100e3 1e6 3e6 10e6]` (default) | real valued vector

Frequency points relative to fundamental frequency where phase noise is calculated,
specified as a real valued vector in Hz.

#### Dependencies

To enable this parameter, select **Estimate Phase Noise** in the
**Analysis** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FrOffset` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[10e3 100e3 1e6 3e6 10e6]` |

### **Target phase-noise levels (dBc/Hz)** — Target phase noise profile for given frequency offset vector `-inf` (default) | vector | scalar

Target phase noise profile for given frequency offset vector, specified in dBc/Hz.
**Target phase noise levels (dBc/Hz)** is the phase noise power in
a 1 Hz bandwidth centered at the specified frequency offsets relative to the
carrier.

#### Dependencies

To enable this parameter, select **Estimate Phase Noise** in the
**Analysis** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `TargetPn` |
| **Type:** character vector |
| **Values:** vector | scalar |
| **Default:** `-inf` |

### **Plot estimated phase noise** — Plot estimated input clock phase noise button

Click to plot the estimated input clock phase noise.

## Libraries

Mixed-Signal Blockset / PLL / Architectures

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

### R2023b: Estimate VCO Phase Noise Parameters

You can either estimate the phase noise parameters of the VCO, or manually define the
custom period jitter and flicker corner frequency. You can also plot the specified and
expected output phase noise density of the VCO.

## Description

Frequency synthesizer with single modulus prescaler based integer N PLL architecture

The Integer N PLL with Single Modulus Prescaler reference architecture uses
a Single Modulus
Prescaler block as the frequency divider in a PLL system. The frequency divider
divides the frequency of the VCO output signal by
an integer value to make it comparable to a PFD reference signal
frequency.
