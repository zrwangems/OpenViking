---
type: simulink-block
title: 'Battery Equivalent Circuit'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cells'
documentation_page: 'batteryequivalentcircuit'
documentation_source_path: 'ref/batteryequivalentcircuit.html'
language: en
---

# Battery Equivalent Circuit

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
- name: H
  summary: Battery thermal mass thermal
  direction: conserving
- name: HDist
  summary: Discretized battery thermal mass thermal array-of-nodes
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the battery positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the battery negative
terminal.

### **H** — Battery thermal mass thermal

Thermal conserving port associated with the battery thermal
mass.

#### Dependencies

To enable this port, in the **Main** section, set
the **Thermal model** parameter to
`Lumped thermal mass`.

### **HDist** — Discretized battery thermal mass thermal array-of-nodes

*Since R2024b*

Thermal conserving port associated with the discretized battery thermal mass. Each
element of this column array of nodes represents one discretized element
in the thermal model along the height of the cell. The size of this
column vector depends on the value of the **Number of thermal
models** parameter.

This table shows the relationship between the elements of the array of nodes at this
port and the thermal option you choose for your battery
model:

| Thermal Option | Connection of Thermal Node |
| --- | --- |
| Cooling plate | The first element of the thermal array of nodes connects to the top cooling plate. The last element of the thermal array of nodes connects to the bottom cooling plate. |
| Ambient thermal path | Each element in the thermal array of nodes connects to an individual thermal resistance. All elements in the array also connect to a single top-level node. |
| Coolant thermal path |
| Inter-cell thermal path | Each element of the thermal array of nodes connects to the corresponding element of the cell next to it. |
| Inter-cell radiative path |
| Serpentine cooling plate | This option provides an interface to the thermal nodes of the cell at a specific cell boundary. Even for thermally discretized cells, the interface only provides one thermal node element at the interface. |
| Boundary connections |

#### Dependencies

To enable this port, in the **Main** section, set
the **Thermal model** parameter to
`Height distributed thermal
mass`.
## Parameters
```yaml
parameters:
- name: Selected part
  summary: Predefined parameterization option <click to select> (default)
  group: ''
- name: Battery capacity
  summary: Battery capacity at full charge 27 A*hr (default) | nonnegative scalar
  group: Main
- name: Thermal model
  summary: Option to define battery thermal model Constant temperature (default) | No temperature dependence | Lumped thermal
    mass | Height distributed thermal mass
  group: Main
  block_parameter: ThermalModel
  values: '"simscape.battery.enum.cells.BatteryThermalModel.ConstantTemperature" (default) | "simscape.battery.enum.cells.BatteryThermalModel.LumpedThermalMass"
    | "simscape.battery.enum.cells.BatteryThermalModel.TemperatureIndependent" | "simscape.battery.enum.cells.BatteryThermalModel.HeightDistributedMass"'
- name: Extrapolation method for all tables
  summary: Method of extrapolation for tables Nearest (default) | Linear | Error
  group: Main
  block_parameter: ExtrapolationMethod
  values: '"simscape.enum.extrapolation.nearest" (default) | "simscape.enum.extrapolation.linear" | "simscape.enum.extrapolation.error"'
- name: State of charge breakpoints, SOC
  summary: SOC breakpoints [0, .1, .25, .5, .75, .9, 1] (default) | vector of values in the range [0, 1]
  group: Open Circuit Voltage
- name: Temperature breakpoints, T
  summary: Temperature breakpoints [278, 293, 313] K (default) | vector of positive values
  group: Open Circuit Voltage
- name: Open-circuit voltage, OCV(SOC)
  summary: Lookup data for open-circuit voltages at specified SOC [3.5057, 3.566, 3.6337, 3.7127, 3.9259, 4.0777, 4.1928]
    V (default) | vector of nonnegative values
  group: Open Circuit Voltage
- name: Open-circuit voltage, OCV(SOC,T)
  summary: Lookup data for open-circuit voltages at specified SOC and temperature [3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62,
    3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19] V (default) | matrix of nonnegative
    values
  group: Open Circuit Voltage
- name: Terminal voltage operating range, [Min Max]
  summary: Terminal voltage operating range [0, inf] V (default) | vector of nonnegative values
  group: Open Circuit Voltage
- name: Hysteresis model
  summary: Option to model hysteresis None (default) | One-state model
  group: Open Circuit Voltage
  block_parameter: HysteresisModel
  values: '"simscape.battery.enum.cells.HysteresisModel.none" (default) | "simscape.battery.enum.cells.HysteresisModel.oneStateModel"'
- name: Maximum dynamic hysteresis voltage, MaximumHysteresisVoltage(SOC)
  summary: Maximum dynamic hysteresis voltage at specified SOC [0, 0, 0, 0, 0, 0, 0] V (default) | vector of nonnegative values
  group: Open Circuit Voltage
- name: Instantaneous hysteresis voltage, InstantaneousHysteresisVoltage(SOC)
  summary: Instantaneous hysteresis voltage at specified SOC [0, 0, 0, 0, 0, 0, 0] V (default) | vector of nonnegative values
  group: Open Circuit Voltage
- name: Hysteresis rate, HysteresisRate(SOC)
  summary: Hysteresis rate at specified SOC 0.1 (default) | nonnegative scalar | vector of nonnegative values
  group: Open Circuit Voltage
- name: Maximum dynamic hysteresis voltage, MaximumHysteresisVoltageThermal(SOC,T)
  summary: Maximum dynamic hysteresis voltage at specified SOC and temperature [0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0,
    0; 0, 0, 0; 0, 0, 0] V (default) | matrix of nonnegative values
  group: Open Circuit Voltage
- name: Instantaneous hysteresis voltage, InstantaneousHysteresisVoltageThermal(SOC,T)
  summary: Instantaneous hysteresis voltage at specified SOC and temperature [0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0;
    0, 0, 0; 0, 0, 0] V (default) | matrix of nonnegative values
  group: Open Circuit Voltage
- name: Hysteresis rate, HysteresisRateThermal(SOC,T)
  summary: Hysteresis rate at specified SOC and temperature 0.1 (default) | nonnegative scalar | matrix of nonnegative values
  group: Open Circuit Voltage
- name: State of charge breakpoints for resistance, SOC
  summary: SOC breakpoints for resistance parameters [0, .1, .25, .5, .75, .9, 1] (default) | vector of values in the range
    [0, 1]
  group: Overpotential
- name: Temperature breakpoints for resistance, T
  summary: Temperature breakpoints for resistance parameters [278, 293, 313] K (default) | vector of positive values
  group: Overpotential
- name: Current breakpoints for resistance, I
  summary: Current breakpoints for resistance parameters [-1, 0, 1] A (default) | vector of scalars
  group: Overpotential
- name: Current dependence for resistance parameters
  summary: Option to enable current dependency for resistance parameters Disabled (default) | Lookup tables (current directionality
    dependent) | Lookup tables (current dependent)
  group: Overpotential
  block_parameter: CurrentDependence
  values: '"simscape.battery.enum.cells.CurrentDependence.Disabled" (default) | "simscape.battery.enum.cells.CurrentDependence.CurrentDirectionalityDependent"
    | "simscape.battery.enum.cells.CurrentDependence.CurrentDependent"'
- name: Instantaneous resistance, R0(SOC)
  summary: Instantaneous resistance of battery at specified SOC [.0085, .0085, .0087, .0082, .0083, .0085, .0085] Ohm (default)
    | vector of nonnegative values
  group: Overpotential
- name: Instantaneous resistance, R0(SOC,T)
  summary: Instantaneous resistance of battery at specified SOC and temperature [.0117, .0085, .009; .011, .0085, .009; .0114,
    .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089] Ohm (default) | matrix
    of nonnegative values
  group: Overpotential
- name: Instantaneous resistance during discharging, R0(SOC)
  summary: Instantaneous resistance of battery during discharging phase at specified SOC [.0085, .0085, .0087, .0082, .0083,
    .0085, .0085] Ohm (default) | vector of nonnegative values
  group: Overpotential
- name: Instantaneous resistance during charging, R0(SOC)
  summary: Instantaneous resistance of battery during charging phase at specified SOC [.0085, .0085, .0087, .0082, .0083,
    .0085, .0085] Ohm (default) | vector of nonnegative values
  group: Overpotential
- name: Instantaneous resistance during charging, R0(SOC,T)
  summary: Instantaneous resistance of battery during charging phase at specified SOC and temperature [.0117, .0085, .009;
    .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]
    Ohm (default) | matrix of nonnegative values
  group: Overpotential
- name: Instantaneous resistance during discharging, R0(SOC,T)
  summary: Instantaneous resistance of battery during discharging phase at specified SOC and temperature [.0117, .0085, .009;
    .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]
    Ohm (default) | matrix of nonnegative values
  group: Overpotential
- name: Instantaneous resistance, R0(SOC,I)
  summary: Instantaneous resistance of battery at specified SOC and current [.0117, .0085, .009; .011, .0085, .009; .0114,
    .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089] Ohm (default) | matrix
    of nonnegative values
  group: Overpotential
- name: Instantaneous resistance, R0(SOC,T,I)
  summary: Instantaneous resistance of battery at specified SOC, temperature, and current repmat([.0117, .0085, .009; .011,
    .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089],
    1, 1, 3) Ohm (default) | 3-D array of nonnegative values
  group: Overpotential
- name: Parallel resistor capacitor pairs
  summary: Option to model battery charge dynamics No dynamics (default) | One time-constant dynamics | Two time-constant
    dynamics | Three time-constant dynamics
  group: Overpotential
  block_parameter: RCPairs
  values: '"simscape.battery.enum.cells.RCPairs.noDynamics" (default) | "simscape.battery.enum.cells.RCPairs.rc1" | "simscape.battery.enum.cells.RCPairs.rc2"
    | "simscape.battery.enum.cells.RCPairs.rc3"'
- name: First polarization resistance, R1(SOC)
  summary: First parallel RC resistance at specified SOC [.0029, .0024, .0026, .0016, .0023, .0018, .0017] Ohm (default) |
    vector of positive values
  group: Overpotential
- name: First time constant, Tau1(SOC)
  summary: First parallel RC time constant at specified SOC [36, 45, 105, 29, 77, 33, 39] s (default) | vector of positive
    values
  group: Overpotential
- name: Second polarization resistance, R2(SOC)
  summary: Second parallel RC resistance at specified SOC [.0029, .0024, .0026, .0016, .0023, .0018, .0017] Ohm (default)
    | vector of positive values
  group: Overpotential
- name: Second time constant, Tau2(SOC)
  summary: Second parallel RC time constant at specified SOC [36, 45, 105, 29, 77, 33, 39] s (default) | vector of positive
    values
  group: Overpotential
- name: Third polarization resistance, R3(SOC)
  summary: Third parallel RC resistance at specified SOC [.0029, .0024, .0026, .0016, .0023, .0018, .0017] Ohm (default) |
    vector of positive values
  group: Overpotential
- name: Third time constant, Tau3(SOC)
  summary: Third parallel RC time constant at specified SOC [36, 45, 105, 29, 77, 33, 39] s (default) | vector of positive
    values
  group: Overpotential
- name: First polarization resistance during discharging, R1(SOC)
  summary: First parallel RC resistance during discharging phase at specified SOC [.0029, .0024, .0026, .0016, .0023, .0018,
    .0017] Ohm (default) | vector of positive values
  group: Overpotential
- name: First time constant during discharging, Tau1(SOC)
  summary: First parallel RC time constant during discharging phase at specified SOC [36, 45, 105, 29, 77, 33, 39] s (default)
    | vector of positive values
  group: Overpotential
- name: First polarization resistance during charging, R1(SOC)
  summary: First parallel RC resistance during charging phase at specified SOC [.0029, .0024, .0026, .0016, .0023, .0018,
    .0017] Ohm (default) | vector of positive values
  group: Overpotential
- name: First time constant during charging, Tau1(SOC)
  summary: First parallel RC time constant during charging phase at specified SOC [36, 45, 105, 29, 77, 33, 39] Ohm (default)
    | vector of positive values
  group: Overpotential
- name: Second polarization resistance during discharging, R2(SOC)
  summary: Second parallel RC resistance during discharging phase at specified SOC [.0029, .0024, .0026, .0016, .0023, .0018,
    .0017] Ohm (default) | vector of positive values
  group: Overpotential
- name: Second time constant during discharging, Tau2(SOC)
  summary: Second parallel RC time constant during discharging phase at specified SOC [36, 45, 105, 29, 77, 33, 39] s (default)
    | vector of positive values
  group: Overpotential
- name: Second polarization resistance during charging, R2(SOC)
  summary: Second parallel RC resistance during charging phase at specified SOC [.0029, .0024, .0026, .0016, .0023, .0018,
    .0017] Ohm (default) | vector of positive values
  group: Overpotential
- name: Second time constant during charging, Tau2(SOC)
  summary: Second parallel RC time constant during charging phase at specified SOC [36, 45, 105, 29, 77, 33, 39] s (default)
    | vector of positive values
  group: Overpotential
- name: Third polarization resistance during discharging, R3(SOC)
  summary: Third parallel RC resistance during discharging phase at specified SOC [.0029, .0024, .0026, .0016, .0023, .0018,
    .0017] Ohm (default) | vector of positive values
  group: Overpotential
- name: Third time constant during discharging, Tau3(SOC)
  summary: Third parallel RC time constant during discharging phase at specified SOC [36, 45, 105, 29, 77, 33, 39] s (default)
    | vector of positive values
  group: Overpotential
- name: Third polarization resistance during charging, R3(SOC)
  summary: Third parallel RC resistance during charging phase at specified SOC [.0029, .0024, .0026, .0016, .0023, .0018,
    .0017] Ohm (default) | vector of positive values
  group: Overpotential
- name: Third time constant during charging, Tau3(SOC)
  summary: Third parallel RC time constant during charging phase at specified SOC [36, 45, 105, 29, 77, 33, 39] s (default)
    | vector of positive values
  group: Overpotential
- name: First polarization resistance, R1(SOC,T)
  summary: First parallel RC resistance at specified SOC and temperature [.0109, .0029, .0013; .0069, .0024, .0012; .0047,
    .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011] Ohm (default) | matrix
    of positive values
  group: Overpotential
- name: First time constant, Tau1(SOC,T)
  summary: First parallel RC time constant at specified SOC and temperature [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29,
    26; 59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: Second polarization resistance, R2(SOC,T)
  summary: Second parallel RC resistance at specified SOC and temperature [.0109, .0029, .0013; .0069, .0024, .0012; .0047,
    .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011] Ohm (default) | matrix
    of positive values
  group: Overpotential
- name: Second time constant, Tau2(SOC,T)
  summary: Second parallel RC time constant at specified SOC and temperature [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29,
    26; 59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: Third polarization resistance, R3(SOC,T)
  summary: Third parallel RC resistance at the specified SOC and temperature [.0109, .0029, .0013; .0069, .0024, .0012; .0047,
    .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011] Ohm (default) | matrix
    of positive values
  group: Overpotential
- name: Third time constant, Tau3(SOC,T)
  summary: Third parallel RC time constant at specified SOC and temperature [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29,
    26; 59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: First polarization resistance during discharging, R1(SOC,T)
  summary: First parallel RC resistance during discharging phase at specified SOC and temperature [.0109, .0029, .0013; .0069,
    .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]
    Ohm (default) | matrix of positive values
  group: Overpotential
- name: First time constant during discharging, Tau1(SOC,T)
  summary: First parallel RC time constant during discharging phase at specified SOC and temperature [20, 36, 39; 31, 45,
    39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: First polarization resistance during charging, R1(SOC,T)
  summary: First parallel RC resistance during charging phase at specified SOC and temperature [.0109, .0029, .0013; .0069,
    .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]
    Ohm (default) | matrix of positive values
  group: Overpotential
- name: First time constant during charging, Tau1(SOC,T)
  summary: First parallel RC time constant during charging phase at specified SOC and temperature [20, 36, 39; 31, 45, 39;
    109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: Second polarization resistance during discharging, R2(SOC,T)
  summary: Second parallel RC resistance during discharging phase at specified SOC and temperature [.0109, .0029, .0013; .0069,
    .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]
    Ohm (default) | matrix of positive values
  group: Overpotential
- name: Second time constant during discharging, Tau2(SOC,T)
  summary: Second parallel RC time constant during discharging phase at specified SOC and temperature [20, 36, 39; 31, 45,
    39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: Second polarization resistance during charging, R2(SOC,T)
  summary: Second parallel RC resistance during charging phase at specified SOC and temperature [.0109, .0029, .0013; .0069,
    .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]
    Ohm (default) | matrix of positive values
  group: Overpotential
- name: Second time constant during charging, Tau2(SOC,T)
  summary: Second parallel RC time constant during charging phase at specified SOC and temperature [20, 36, 39; 31, 45, 39;
    109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: Third polarization resistance during discharging, R3(SOC,T)
  summary: Third parallel RC resistance during discharging phase at specified SOC and temperature breakpoints [.0109, .0029,
    .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028,
    .0017, .0011] Ohm (default) | matrix of positive values
  group: Overpotential
- name: Third time constant during discharging, Tau3(SOC,T)
  summary: Third parallel RC time constant during discharging phase at specified SOC and temperature breakpoints [20, 36,
    39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: Third polarization resistance during charging, R3(SOC,T)
  summary: Third parallel RC resistance during charging phase at specified SOC and temperature breakpoints [.0109, .0029,
    .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028,
    .0017, .0011] Ohm (default) | matrix of positive values
  group: Overpotential
- name: Third time constant during charging, Tau3(SOC,T)
  summary: Third parallel RC time constant during charging phase at specified SOC and temperature breakpoints [20, 36, 39;
    31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: First polarization resistance, R1(SOC,I)
  summary: First parallel RC resistance at specified SOC and current [.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026,
    .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011] Ohm (default) | matrix of positive
    values
  group: Overpotential
- name: First time constant, Tau1(SOC,I)
  summary: First parallel RC time constant at specified SOC and current [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26;
    59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: Second polarization resistance, R2(SOC,I)
  summary: Second parallel RC resistance at specified SOC and current [.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026,
    .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011] Ohm (default) | matrix of positive
    values
  group: Overpotential
- name: Second time constant, Tau2(SOC,I)
  summary: Second parallel RC time constant at specified SOC and current [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26;
    59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: Third polarization resistance, R3(SOC,I)
  summary: Third parallel RC resistance at the specified SOC and current [.0109, .0029, .0013; .0069, .0024, .0012; .0047,
    .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011] Ohm (default) | matrix
    of positive values
  group: Overpotential
- name: Third time constant, Tau3(SOC,I)
  summary: Third parallel RC time constant at specified SOC and current [20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26;
    59, 77, 67; 40, 33, 29; 25, 39, 33] s (default) | matrix of positive values
  group: Overpotential
- name: First polarization resistance, R1(SOC,T,I)
  summary: First parallel RC resistance at specified SOC, temperature, and current repmat([.0109, .0029, .0013; .0069, .0024,
    .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011], 1, 1,
    3) Ohm (default) | 3-D array of positive values
  group: Overpotential
- name: First time constant, Tau1(SOC,T,I)
  summary: First parallel RC time constant at specified SOC, temperature, and current repmat([20, 36, 39; 31, 45, 39; 109,
    105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33], 1, 1, 3) s (default) | 3-D array of positive values
  group: Overpotential
- name: Second polarization resistance, R2(SOC,T,I)
  summary: Second parallel RC resistance at specified SOC, temperature, and current repmat([.0109, .0029, .0013; .0069, .0024,
    .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011], 1, 1,
    3) Ohm (default) | 3-D array of positive values
  group: Overpotential
- name: Second time constant, Tau2(SOC,T,I)
  summary: Second parallel RC time constant at specified SOC, temperature, and current [repmat([20, 36, 39; 31, 45, 39; 109,
    105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33], 1, 1, 3) s (default) | 3-D array of positive values
  group: Overpotential
- name: Third polarization resistance, R3(SOC,T,I)
  summary: Third parallel RC resistance at the specified SOC. temperature, and current [repmat([.0109, .0029, .0013; .0069,
    .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011],
    1, 1, 3) Ohm (default) | 3-D array of positive values
  group: Overpotential
- name: Third time constant, Tau3(SOC,T,I)
  summary: Third parallel RC time constant at specified SOC, temperature, and current repmat([20, 36, 39; 31, 45, 39; 109,
    105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33], 1, 1, 3) s (default) | matrix of positive values
  group: Overpotential
- name: Self discharge
  summary: Option to model battery self-discharge resistance Disabled (default) | Enabled
  group: Overpotential
  block_parameter: SelfDischargeResistor
  values: '"simscape.battery.enum.cells.BatteryEnable.Disabled" (default) | "simscape.battery.enum.cells.BatteryEnable.Enabled"'
- name: Self-discharge resistance, SelfDischargeR
  summary: Self-discharge resistance of battery 7e3 Ohm (default) | positive scalar
  group: Overpotential
- name: Self-discharge resistance, SelfDischargeR(T)
  summary: Self-discharge resistance of battery at specified temperature [8000, 7000, 6000] Ohm (default) | vector of positive
    values
  group: Overpotential
- name: Cycling aging model
  summary: Option to define fading characteristic Disabled (default) | Equations | Lookup tables (temperature independent)
    | Lookup tables (constant temperature dependent) | Lookup tables (temperature dependent) | Lookup tables (temperature
    and current dependent)
  group: Cycling Aging
  block_parameter: CyclingAgingMethod
  values: '"simscape.battery.enum.cells.CyclingAgingMethod.disabled" (default) | "simscape.battery.enum.cells.CyclingAgingMethod.equations"
    | "simscape.battery.enum.cells.CyclingAgingMethod.tableN" | "simscape.battery.enum.cells.CyclingAgingMethod.tableNandT"
    | "simscape.battery.enum.cells.CyclingAgingMethod.tableNandVariableT" | "simscape.battery.enum.cells.CyclingAgingMethod.tableNandVariableTandI"'
- name: Cycle calculation method
  summary: Option to choose how block calculates number of discharge cycles Equivalent cycles (default) | Equivalent full
    cycles
  group: Cycling Aging
- name: Number of discharge cycles, NumDisCycles
  summary: Number of cycles for percentage change calculations 100 (default) | scalar in the range [1, inf)
  group: Cycling Aging
- name: Change in open-circuit voltage after NumDisCycles discharge cycles (%)
  summary: Percentage change in open-circuit voltage after *NumDisCycles* cycles 0 (default) | scalar
  group: Cycling Aging
- name: Change in terminal resistance after NumDisCycles discharge cycles (%)
  summary: Percentage change in terminal resistance after *NumDisCycles* cycles 0 (default) | scalar
  group: Cycling Aging
- name: Change in cell capacity after NumDisCycles discharge cycles (%)
  summary: Percentage change in cell capacity after *NumDisCycles* cycles 0 (default) | scalar
  group: Cycling Aging
- name: Change in self-discharge resistance after NumDisCycles discharge cycles (%)
  summary: Percentage change in self-discharge resistance after *NumDisCycles* cycles 0 (default) | scalar
  group: Cycling Aging
- name: Change in first polarization resistance after NumDisCycles discharge cycles (%)
  summary: Percentage change in first RC resistance after *NumDisCycles* cycles 0 (default) | scalar
  group: Cycling Aging
- name: Change in second polarization resistance after NumDisCycles discharge cycles (%)
  summary: Percentage change in second RC resistance after *NumDisCycles* cycles 0 (default) | scalar
  group: Cycling Aging
- name: Change in third polarization resistance after NumDisCycles discharge cycles (%)
  summary: Percentage change in third RC resistance after *NumDisCycles* cycles 0 (default) | scalar
  group: Cycling Aging
- name: Number of discharge cycles breakpoints, NumDisCyclesBreakpoints
  summary: Reference vector or numbers of cycles for percentage change calculations [0, 100, 200, 300] (default) | vector
    of nonnegative values
  group: Cycling Aging
- name: Temperatures breakpoints for cycling aging data, T
  summary: Temperature breakpoints at which block extracts fading lookup tables [298.15, 323.15] K (default) | vector of entries
    in the range [1, inf)
  group: Cycling Aging
- name: Current breakpoints for cycling aging data, I
  summary: Current breakpoints at which block extracts fading lookup tables [-.1, -.5, -5] A (default) | vector of negative
    scalars
  group: Cycling Aging
- name: Percentage change in open-circuit voltage, OCVChange(N)
  summary: Percentage change in open-circuit voltage after *N* cycles [0, 0, 0, 0] (default) | vector of scalars
  group: Cycling Aging
- name: Percentage change in terminal resistance, R0Change(N)
  summary: Percentage change in terminal resistance after *N* cycles [0, 0, 0, 0] (default) | vector of scalars
  group: Cycling Aging
- name: Percentage change in cell capacity, CapacityChange(N)
  summary: Percentage change in cell capacity after *N* cycles [0, 0, 0, 0] (default) | vector of scalars
  group: Cycling Aging
- name: Percentage change in self-discharge resistance, SelfDischargeRChange(N)
  summary: Percentage change in self-discharge resistance after *N* cycles [0, 0, 0, 0] (default) | vector of scalars
  group: Cycling Aging
- name: Percentage change in first polarization resistance, R1Change(N)
  summary: Percentage change in first parallel RC resistance after *N* cycles [0, 0, 0, 0] (default) | vector of scalars
  group: Cycling Aging
- name: Percentage change in second polarization resistance, R2Change(N)
  summary: Percentage change in second parallel RC resistance after *N* cycles [0, 0, 0, 0] (default) | vector of scalars
  group: Cycling Aging
- name: Percentage change in third polarization resistance, R3Change(N)
  summary: Percentage change in third parallel RC resistance after *N* cycles [0, 0, 0, 0] (default) | vector of scalars
  group: Cycling Aging
- name: Percentage change in open-circuit voltage, OCVChange(N,T)
  summary: Percentage change in open-circuit voltage after *N* cycles at specified temperature [0, 0; 0, 0; 0, 0; 0, 0] (default)
    | matrix of scalars
  group: Cycling Aging
- name: Percentage change in terminal resistance, R0Change(N,T)
  summary: Percentage change in terminal resistance after *N* cycles at specified temperature [0, 0; 0, 0; 0, 0; 0, 0] (default)
    | matrix of scalars
  group: Cycling Aging
- name: Initial target for percentage change in internal resistance due to cycling aging
  summary: Initial target value for percentage change in internal resistance due to cycling aging 0 (default) | scalar
  group: Cycling Aging
- name: Percentage change in cell capacity, CapacityChange(N,T)
  summary: Percentage change in cell capacity after *N* cycles at specified temperature [0, 0; 0, 0; 0, 0; 0, 0] (default)
    | matrix of scalars
  group: Cycling Aging
- name: Initial target for percentage change in capacity due to cycling aging
  summary: Initial target value for percentage change in capacity due to cycling aging 0 (default) | scalar
  group: Cycling Aging
- name: Percentage change in self-discharge resistance, SelfDischargeRChange(N,T)
  summary: Percentage change in self-discharge resistance after *N* cycles at specified temperature [0, 0; 0, 0; 0, 0; 0,
    0] (default) | matrix of scalars
  group: Cycling Aging
- name: Initial target for percentage change in self-discharge resistance due to cycling aging
  summary: Initial target value for percentage change in self-discharge resistance due to cycling aging 0 (default) | scalar
  group: Cycling Aging
- name: Percentage change in first polarization resistance, R1Change(N,T)
  summary: Percentage change in first parallel RC resistance after *N* cycles at specified temperature [0, 0; 0, 0; 0, 0;
    0, 0] (default) | matrix of scalars
  group: Cycling Aging
- name: Initial target for percentage change in first polarization resistance due to cycling aging
  summary: Initial target value for percentage change in first polarization resistance due to cycling aging 0 (default) |
    scalar
  group: Cycling Aging
- name: Percentage change in second polarization resistance, R2Change(N,T)
  summary: Percentage change in second parallel RC resistance after *N* cycles at specified temperature [0, 0; 0, 0; 0, 0;
    0, 0] (default) | matrix of scalars
  group: Cycling Aging
- name: Initial target for percentage change in second polarization resistance due to cycling aging
  summary: Initial target value for percentage change in second polarization resistance due to cycling aging 0 (default) |
    scalar
  group: Cycling Aging
- name: Percentage change in third polarization resistance, R3Change(N,T)
  summary: Percentage change in third parallel RC resistance after *N* cycles at specified temperature [0, 0; 0, 0; 0, 0;
    0, 0] (default) | matrix of scalars
  group: Cycling Aging
- name: Initial target for percentage change in third polarization resistance due to cycling aging
  summary: Initial target value for percentage change in third polarization resistance due to cycling aging 0 (default) |
    scalar
  group: Cycling Aging
- name: Percentage change in terminal resistance, R0Change(N,T,I)
  summary: Percentage change in terminal resistance after *N* cycles at specified temperature and current repmat(0, 4, 2,
    3) (default) | 3-D array of scalars
  group: Cycling Aging
- name: Percentage change in cell capacity, CapacityChange(N,T,I)
  summary: Percentage change in cell capacity after *N* cycles at specified temperature and current repmat(0, 4, 2, 3) (default)
    | 3-D array of scalars
  group: Cycling Aging
- name: Percentage change in self-discharge resistance, SelfDischargeRChange(N,T,I)
  summary: Percentage change in self-discharge resistance after *N* cycles at specified temperature and current repmat(0,
    4, 2, 3) (default) | 3-D array of scalars
  group: Cycling Aging
- name: Percentage change in first polarization resistance, R1Change(N,T,I)
  summary: Percentage change in first polarization resistance after *N* cycles at specified temperature and current repmat(0,
    4, 2, 3) (default) | 3-D array of scalars
  group: Cycling Aging
- name: Percentage change in second polarization resistance, R2Change(N,T,I)
  summary: Percentage change in second polarization resistance after *N* cycles at specified temperature and current repmat(0,
    4, 2, 3) (default) | 3-D array of scalars
  group: Cycling Aging
- name: Percentage change in third polarization resistance, R2Change(N,T,I)
  summary: Percentage change in third polarization resistance after *N* cycles at specified temperature and current repmat(0,
    4, 2, 3) (default) | 3-D array of scalars
  group: Cycling Aging
- name: Resistance calendar aging
  summary: Option to enable calendar aging for resistance Disabled (default) | Enabled
  group: Calendar Aging
  block_parameter: CalendarAgeResistance
  values: '"simscape.battery.enum.cells.BatteryEnable.Disabled" (default) | "simscape.battery.enum.cells.BatteryEnable.Enabled"'
- name: Capacity calendar aging
  summary: Option to enable calendar aging for capacity Disabled (default) | Enabled
  group: Calendar Aging
  block_parameter: CalendarAgeCapacity
  values: '"simscape.battery.enum.cells.BatteryEnable.Disabled" (default) | "simscape.battery.enum.cells.BatteryEnable.Enabled"'
- name: Modeling option
  summary: 'Modeling option for calendar aging Equation-based (default) | Tabulated: temperature | Tabulated: time and temperature'
  group: Calendar Aging
  block_parameter: CalendarAgingMethod
  values: '"simscape.battery.enum.cells.CalendarAgingMethod.equation" (default) | "simscape.battery.enum.cells.CalendarAgingMethod.tableT"
    | "simscape.battery.enum.cells.CalendarAgingMethod.tableTandTime"'
- name: Storage condition
  summary: Storage condition Specify open-circuit voltage during storage (default) | Specify state-of-charge during storage
  group: Calendar Aging
  block_parameter: StorageVariable
  values: '"simscape.battery.enum.cells.StorageVariable.OCV" (default) | "simscape.battery.enum.cells.StorageVariable.SOC"'
- name: Normalized open-circuit voltage during storage, V/Vnom
  summary: Normalized open-circuit voltage during storage 0.9 (default) | scalar
  group: Calendar Aging
- name: State of charge during storage
  summary: Percentage SOC during storage 0.6 (default) | scalar in the range [0, 1]
  group: Calendar Aging
- name: Vector of time intervals
  summary: Time intervals [0] d (default) | vector of scalars
  group: Calendar Aging
- name: Vector of storage temperatures
  summary: Storage temperatures [273] K (default) | vector of nonnegative values
  group: Calendar Aging
- name: Terminal resistance linear scaling for voltage, b
  summary: Voltage linear scaling coefficient of terminal resistance 2.2134e6 (default) | scalar
  group: Calendar Aging
- name: Terminal resistance constant offset for voltage, c
  summary: Voltage constant offset of terminal resistance 1.632e6 (default) | scalar
  group: Calendar Aging
- name: Terminal resistance temperature-dependent exponential increase, d
  summary: Temperature-dependent exponential increase in terminal resistance 0.515833569 V (default) | scalar
  group: Calendar Aging
- name: Terminal resistance time exponent, a
  summary: Time exponent in terminal resistance 0.75 (default) | scalar
  group: Calendar Aging
- name: Vector of sampled temperatures for terminal resistance calendar aging, T_ar
  summary: Sampled temperatures for terminal resistance calendar aging [273.15, 298.15, 323.15] K (default) | vector of positive
    values
  group: Calendar Aging
- name: Vector of sampled storage time intervals for terminal resistance calendar aging, t_ar
  summary: Sampled storage time intervals for terminal resistance calendar aging [90, 180, 270, 360] d (default) | vector
    of positive values
  group: Calendar Aging
- name: Percentage change in terminal resistance due to calendar aging, dR0(T_ar)
  summary: Percentage change in terminal resistance due to calendar aging [0,0,0] (default) | vector of scalars
  group: Calendar Aging
- name: Time between terminal resistance beginning of life and dR(T_ar) measurement
  summary: Time between terminal resistance at beginning of life and *dR(Tar)* measurement 100 d (default) | nonnegative scalar
  group: Calendar Aging
- name: Percentage change in terminal resistance due to calendar aging, dR0(t_ar,T_ar)
  summary: Percentage change in terminal resistance due to calendar aging [0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0] (default) |
    matrix of scalars
  group: Calendar Aging
- name: Capacity linear scaling for voltage, b
  summary: Voltage linear scaling of capacity 1.5097e07 (default) | scalar
  group: Calendar Aging
- name: Capacity constant offset for voltage, c
  summary: Voltage constant offset of capacity 8.3625e06 (default) | scalar
  group: Calendar Aging
- name: Capacity temperature-dependent exponential decrease, d
  summary: Temperature-dependent exponential decrease in capacity 0.6011 V (default) | scalar
  group: Calendar Aging
- name: Capacity time exponent, a
  summary: Time exponent in capacity 0.75 (default) | scalar
  group: Calendar Aging
- name: Vector of sampled temperatures for capacity calendar aging, T_ac
  summary: Sampled temperatures for capacity calendar aging [273.15, 298.15, 323.15] K (default) | vector of positive values
  group: Calendar Aging
- name: Vector of sampled storage time intervals for capacity calendar aging, t_ac
  summary: Sampled storage time intervals for capacity calendar aging [90, 180, 270, 360] d (default) | vector of positive
    values
  group: Calendar Aging
- name: Percentage change in capacity due to calendar aging, dAH(T_ac)
  summary: Percentage change in capacity due to calendar aging [0, 0, 0] (default) | vector of scalars
  group: Calendar Aging
- name: Time between capacity beginning of life and dAH(T_ac) measurement
  summary: Time between capacity at beginning of life and *dAH(Tac)* measurement 100 d (default) | positive scalar
  group: Calendar Aging
- name: Percentage change in capacity due to calendar aging, dAH(t_ac,T_ac)
  summary: Percentage change in capacity due to calendar aging [0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0] (default) | matrix of
    scalars
  group: Calendar Aging
- name: Simulation temperature
  summary: Battery temperature 298.15 K (default) | positive scalar
  group: Thermal
- name: Battery thermal mass
  summary: Battery thermal mass associated with thermal port 100 J/K (default) | positive scalar
  group: Thermal
- name: Number of thermal models
  summary: Number of discretized elements in thermal model 6 (default) | positive scalar
  group: Thermal
- name: Thermal conductivity in Z dimension
  summary: Thermal conductivity of cell in *Z* dimension 18 W/(K*m) (default) | positive scalar
  group: Thermal
- name: Cross-sectional area in XY dimension
  summary: Cross-sectional area of cell in *XY* dimension 3.5e-4 m^2 (default) | positive scalar
  group: Thermal
- name: Cell height
  summary: Height of cell 0.07 m (default) | positive scalar
  group: Thermal
- name: Reversible heat model
  summary: Option to model reversible heat Disabled (default) | Entropic coefficient
  group: Thermal
  block_parameter: ReversibleHeatModel
  values: '"simscape.battery.enum.cells.ReversibleHeatModel.Disabled" (default) | "simscape.battery.enum.cells.ReversibleHeatModel.EntropicCoefficient"'
- name: Entropic coefficient
  summary: Entropic coefficient of reversible heat [0, 0, 0, 0, 0, 0, 0] mV/K (default) | vector of scalars
  group: Thermal
- name: Additional resistance fault
  summary: Option to fault series-connected resistance Add fault (default)
  group: Faults
- name: Exothermic reactions fault
  summary: Option to model self-heating and thermal runaway events Add fault (default)
  group: Faults
- name: Internal short fault
  summary: Option to fault parallel-connected resistance Add fault (default)
  group: Faults
- name: Additional resistance when faulted
  summary: Additional resistance when block is faulted 1e5 Ohm (default)
  group: Faults
- name: Trigger type
  summary: Type of fault trigger for additional resistance fault Always On (default) | Timed | Additional triggers | Conditional
    | Manual
  group: Faults
- name: Trigger fault at time
  summary: Time before entering faulted state for additional resistance fault 0 s (default) | nonnegative scalar
  group: Faults
- name: Trigger Configuration
  summary: Option to enable additional trigger types for additional resistance fault Open fault properties
  group: Faults
- name: Short parallel resistance when faulted
  summary: Short parallel resistance when block is faulted 1e-6 (default)
  group: Faults
- name: Trigger type
  summary: Type of fault trigger for internal short fault Always On (default) | Timed | Additional triggers | Conditional
    | Manual
  group: Faults
- name: Trigger fault at time
  summary: Time before entering faulted state for internal short fault 0 s (default) | nonnegative scalar
  group: Faults
- name: Trigger Configuration
  summary: Option to enable additional trigger types for internal short fault Open fault properties
  group: Faults
- name: Modeling fidelity
  summary: Fidelity option for modeling exothermic reactions Analytical (default) | Tabulated accelerated rate calorimetry
    test temperature rate
  group: Faults
  block_parameter: ExothermModel
  values: '"simscape.battery.enum.cells.ExothermModel.analytical" (default) | "simscape.battery.enum.cells.ExothermModel.acceleratedRateCalorimetryTemperature"'
- name: Tabulate with state of charge
  summary: Option to tabulate exothermic reactions parameters as functions of SOC off (default) | on
  group: Faults
  block_parameter: TabulateWithSOC
  values: false (default) | true
- name: Current interruption temperature
  summary: Temperature over which current stops flowing 420 K (default) | positive scalar
  group: Faults
- name: Total heat of reaction
  summary: Total heat of reaction 23e3 J (default) | positive scalar
  group: Faults
- name: Exotherm onset temperature
  summary: Exotherm onset temperature 350 K (default) | positive scalar
  group: Faults
- name: Exotherm onset temperature rate
  summary: Exothermic onset temperature rate 0.02 K/min (default) | positive scalar
  group: Faults
- name: Activation energy
  summary: Activation energy 160e3 J/mol (default) | positive scalar
  group: Faults
- name: Order of reaction
  summary: Order of exothermic reaction 1 (default) | positive scalar
  group: Faults
- name: Percent of thermal mass vented
  summary: Percentage of thermal mass battery vents to environment 40 (default) | positive scalar
  group: Faults
- name: Vector of state of charge values for exothermic parameters, SOC
  summary: SOC values for lookup data of exothermic parameters [0,.5,1] (default) | vector of nonnegative values
  group: Faults
- name: Corresponding current interruption temperature, Tci(SOC)
  summary: Corresponding current interruption temperature at specified SOC breakpoints [420, 420, 420] (default) | vector
    of nonnegative values
  group: Faults
- name: Corresponding total heat of reaction, heat(SOC)
  summary: Corresponding total heat of reaction at specified SOC breakpoints [23000, 23000, 23000] (default) | vector of nonnegative
    values
  group: Faults
- name: Corresponding exotherm onset temperature, Tex(SOC)
  summary: Corresponding exothermic onset temperature at specified SOC breakpoints [350, 350, 350] (default) | vector of nonnegative
    values
  group: Faults
- name: Corresponding activation energy, Ea(SOC)
  summary: Corresponding activation energy at specified SOC breakpoints [160000, 160000, 160000] (default) | vector of nonnegative
    values
  group: Faults
- name: Corresponding order of reaction, Or(SOC)
  summary: Corresponding order of reaction at specified SOC breakpoints [1, 1, 1] (default) | vector of nonnegative values
  group: Faults
- name: Vector of ARC test temperatures, T
  summary: ARC test temperatures for lookup data [323, 373, 423, 438, 463, 483, 513, 543, 545, 547, 549, 551, 553, 573, 623,
    773, 923, 943, 1003, 1063, 1113, 1123, 1133, 1153, 1173] (default) | vector of nonnegative values
  group: Faults
- name: Corresponding ARC test temperature rates, dT/dt(T)
  summary: Corresponding ARC test temperature rates at specified T breakpoints [.0001, .001, .025, .2, .4, .6, 1.1, 1.3, 1.9,
    3, 5, 11.6, 183.3, 191.6, 200, 208.3, 200, 175, 8.33, 1.33, .33, .2, .13, .0017, .00017] (default) | vector of nonnegative
    values
  group: Faults
- name: Corresponding ARC test temperature rates, dT/dt(T,SOC)
  summary: Corresponding ARC test temperature rates at specified temperature and SOC breakpoints repmat([.0001, .001, .025,
    .2, .4, .6, 1.1, 1.3, 1.9, 3, 5, 11.6, 183.3, 191.6, 200, 208.3, 200, 175, 8.33, 1.33, .33, .2, .13, .0017, .00017]',
    1, 3) (default) | matrix of nonnegative values
  group: Faults
- name: Corresponding percent of thermal mass vented, Mvent(SOC)
  summary: Corresponding vented thermal mass percentage at specified SOC breakpoints [40, 40, 40] (default) | vector of values
    in the range [0, 100]
  group: Faults
- name: Trigger type
  summary: Type of fault trigger for exothermic reactions fault Always On (default) | Timed | Behavioral | Additional triggers
    | Conditional | Manual
  group: Faults
- name: Trigger fault at time
  summary: Time before entering faulted state for exothermic reactions fault 0 s (default) | nonnegative scalar
  group: Faults
- name: Trigger temperature
  summary: Temperature to trigger fault 350 K (default) | nonnegative scalar
  group: Faults
- name: Trigger Configuration
  summary: Option to enable additional trigger types for exothermic reactions fault Open fault properties
  group: Faults
```

### **Selected part** — Predefined parameterization option `<click to select>` (default)

Option to parameterize the block to represent components by specific suppliers. Click the
**<click to select>** hyperlink to open the Block
Parameterization Manager window. For more information about the Block Parameterization
Manager, see Load Predefined Parameterizations (Simscape Electrical).

### Main

### **Battery capacity** — Battery capacity at full charge `27` `A*hr` (default) | nonnegative scalar

Capacity of the battery when it is fully charged. The block calculates
the SOC by dividing the accumulated charge by this value. The block
calculates accumulated charge by integrating the battery current.

### **Thermal model** — Option to define battery thermal model `Constant temperature` (default) | `No temperature dependence` | `Lumped thermal mass` | `Height distributed thermal mass`

Option to define the thermal model of the battery.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ThermalModel` |
| **Values:** | `"simscape.battery.enum.cells.BatteryThermalModel.ConstantTemperature"` (default) | `"simscape.battery.enum.cells.BatteryThermalModel.LumpedThermalMass"` | `"simscape.battery.enum.cells.BatteryThermalModel.TemperatureIndependent"` | `"simscape.battery.enum.cells.BatteryThermalModel.HeightDistributedMass"` |

### **Extrapolation method for all tables** — Method of extrapolation for tables `Nearest` (default) | `Linear` | `Error`

Extrapolation method for all the table-based parameters:

- `Linear` — Estimate values beyond the
  data by creating a tangent line at the end of the known data and
  extending it beyond that limit.
- `Nearest` — Extrapolate a value at a
  query point that is the value at the nearest sample grid point.
- `Error` — Return an error if the
  value goes beyond the known data. If you select this option, the
  block does not use extrapolation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationMethod` |
| **Values:** | `"simscape.enum.extrapolation.nearest"` (default) | `"simscape.enum.extrapolation.linear"` | `"simscape.enum.extrapolation.error"` |

### Open Circuit Voltage

### **State of charge breakpoints, SOC** — SOC breakpoints `[0, .1, .25, .5, .75, .9, 1]` (default) | vector of values in the range [0, 1]

SOC breakpoints at which you specify lookup data. This vector must be
strictly ascending. The block calculates the SOC value with respect to
the nominal battery capacity specified in the **Battery
capacity** parameter. The SOC is the ratio of the available
battery charge, *q*battery and
the nominal battery capacity,
*q*nom*(T,n)*.
You must make sure that, for each temperature, an SOC value of 1
represents the respective battery charge capacity specified in the
**Battery capacity** parameter, assuming a fresh
battery with a number of cycles *N* equal to 1 and
*δAH(n = 1,
Tfade) = 0*.

SOC=qbatteryqnom(T,n)  for N=1 and δAH(n,Tfade)=0,  qnom(T,n)=AH

### **Temperature breakpoints, T** — Temperature breakpoints `[278, 293, 313]` `K` (default) | vector of positive values

Temperature breakpoints at which you specify lookup data. This vector
must be strictly ascending and each element must be greater than
`0`
`K`.

#### Dependencies

To enable this parameter, set **Thermal model** to `Constant
temperature`, `Lumped thermal mass`, or
`Height distributed thermal mass`.

### **Open-circuit voltage, OCV(SOC)** — Lookup data for open-circuit voltages at specified SOC `[3.5057, 3.566, 3.6337, 3.7127, 3.9259, 4.0777, 4.1928]` `V` (default) | vector of nonnegative values

Lookup data for the open-circuit voltages across the fundamental
battery model at the specified SOC.

#### Dependencies

To enable this parameter, set **Thermal model** to `No temperature dependence`.

### **Open-circuit voltage, OCV(SOC,T)** — Lookup data for open-circuit voltages at specified SOC and temperature `[3.49, 3.5, 3.51; 3.55, 3.57, 3.56; 3.62, 3.63, 3.64; 3.71, 3.71, 3.72; 3.91, 3.93, 3.94; 4.07, 4.08, 4.08; 4.19, 4.19, 4.19]` `V` (default) | matrix of nonnegative values

Lookup data for the open-circuit voltages across the fundamental
battery model at the specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set **Thermal model** to `Constant
temperature`, `Lumped thermal mass`, or
`Height distributed thermal mass`.

### **Terminal voltage operating range, [Min Max]** — Terminal voltage operating range `[0, inf]` `V` (default) | vector of nonnegative values

Operating range of the terminal voltage. This parameter must be a
1-by-2 vector that defines the minimum and maximum values of the
terminal voltage.

### **Hysteresis model** — Option to model hysteresis `None` (default) | `One-state model`

Option to model the hysteresis of the battery.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `HysteresisModel` |
| **Values:** | `"simscape.battery.enum.cells.HysteresisModel.none"` (default) | `"simscape.battery.enum.cells.HysteresisModel.oneStateModel"` |

### **Maximum dynamic hysteresis voltage, MaximumHysteresisVoltage(SOC)** — Maximum dynamic hysteresis voltage at specified SOC `[0, 0, 0, 0, 0, 0, 0]` `V` (default) | vector of nonnegative values

Maximum dynamic hysteresis voltage at the specified SOC breakpoints.
This parameter only affects the dynamic portion of the hysteresis
modeling. The instantaneous hysteresis voltage is independent of this
parameter.

The value of this parameter must be a vector of the same size as the
**State of charge breakpoints, SOC**
parameter.

#### Dependencies

To enable this parameter, set **Thermal model**
to `No temperature dependence` and
**Hysteresis model** to `One-state
model`.

### **Instantaneous hysteresis voltage, InstantaneousHysteresisVoltage(SOC)** — Instantaneous hysteresis voltage at specified SOC `[0, 0, 0, 0, 0, 0, 0]` `V` (default) | vector of nonnegative values

Instantaneous hysteresis voltage at the specified SOC breakpoints. The
value of this parameter must be a vector of the same size as the
**State of charge breakpoints, SOC**
parameter.

#### Dependencies

To enable this parameter, set **Thermal model**
to `No temperature dependence` and
**Hysteresis model** to `One-state
model`.

### **Hysteresis rate, HysteresisRate(SOC)** — Hysteresis rate at specified SOC `0.1` (default) | nonnegative scalar | vector of nonnegative values

Hysteresis rate at the specified SOC breakpoints. The value of this
parameter must be a scalar or a vector of the same size as the
**State of charge breakpoints, SOC**
parameter.

#### Dependencies

To enable this parameter, set **Thermal model**
to `No temperature dependence` and
**Hysteresis model** to `One-state
model`.

### **Maximum dynamic hysteresis voltage, MaximumHysteresisVoltageThermal(SOC,T)** — Maximum dynamic hysteresis voltage at specified SOC and temperature `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]` `V` (default) | matrix of nonnegative values

Maximum dynamic hysteresis voltage at the specified SOC and
temperature breakpoints. This parameter only affects the dynamic portion
of the hysteresis modeling. The instantaneous hysteresis voltage is
independent of this parameter.

The value of this parameter must be a matrix with a number of rows and
columns equal to the size of the **State of charge breakpoints,
SOC** and **Temperature breakpoints, T**
parameters, respectively.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Constant temperature`,
`Lumped thermal mass`, or
`Height distributed thermal mass` and
**Hysteresis model** to `One-state
model`.

### **Instantaneous hysteresis voltage, InstantaneousHysteresisVoltageThermal(SOC,T)** — Instantaneous hysteresis voltage at specified SOC and temperature `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]` `V` (default) | matrix of nonnegative values

Instantaneous hysteresis voltage at the specified SOC and temperature
breakpoints. The value of this parameter must be a matrix with a number
of rows and columns equal to the size of the **State of charge
breakpoints, SOC** and **Temperature breakpoints,
T** parameters, respectively.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Constant temperature`,
`Lumped thermal mass`, or
`Height distributed thermal mass` and
**Hysteresis model** to `One-state
model`.

### **Hysteresis rate, HysteresisRateThermal(SOC,T)** — Hysteresis rate at specified SOC and temperature `0.1` (default) | nonnegative scalar | matrix of nonnegative values

Hysteresis rate at the specified SOC and temperature breakpoints. The
value of this parameter must be a scalar or a matrix with a number of
rows and columns equal to the size of the **State of charge
breakpoints, SOC** and **Temperature breakpoints,
T** parameters, respectively.

#### Dependencies

To enable this parameter, set **Thermal model** to
`Constant temperature`,
`Lumped thermal mass`, or
`Height distributed thermal mass` and
**Hysteresis model** to `One-state
model`.

### Overpotential

### **State of charge breakpoints for resistance, SOC** — SOC breakpoints for resistance parameters `[0, .1, .25, .5, .75, .9, 1]` (default) | vector of values in the range [0, 1]

SOC breakpoints at which you specify lookup data for the resistance
parameters. This vector must be strictly ascending. The block calculates
the SOC value with respect to the nominal battery capacity specified in
the **Battery capacity** parameter.

### **Temperature breakpoints for resistance, T** — Temperature breakpoints for resistance parameters `[278, 293, 313]` `K` (default) | vector of positive values

Temperature breakpoints at which you specify lookup data for the
resistance parameters. This vector must be strictly ascending and its
entries must be greater than `0`
`K`.

#### Dependencies

To enable this parameter, set **Thermal model** to `Constant
temperature`, `Lumped thermal mass`, or
`Height distributed thermal mass`.

### **Current breakpoints for resistance, I** — Current breakpoints for resistance parameters `[-1, 0, 1]` `A` (default) | vector of scalars

*Since R2025a*

Current breakpoints at which you specify lookup data for the
resistance parameters.

#### Dependencies

To enable this parameter, set **Current dependence for
resistance parameters** to `Lookup tables
(current dependent)`.

### **Current dependence for resistance parameters** — Option to enable current dependency for resistance parameters `Disabled` (default) | `Lookup tables (current directionality dependent)` | `Lookup tables (current dependent)`

*Since R2025a*

Option to enable current dependency for resistance parameters. If you
set this parameter to `Lookup tables (current directionality
dependent)`, the instantaneous and polarization
resistances depend on the direction of the current. If you set this
parameter to `Lookup tables (current
dependent)`, the instantaneous and polarization
resistances depend on the current.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CurrentDependence` |
| **Values:** | `"simscape.battery.enum.cells.CurrentDependence.Disabled"` (default) | `"simscape.battery.enum.cells.CurrentDependence.CurrentDirectionalityDependent"` | `"simscape.battery.enum.cells.CurrentDependence.CurrentDependent"` |

### **Instantaneous resistance, R0(SOC)** — Instantaneous resistance of battery at specified SOC `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm` (default) | vector of nonnegative values

Instantaneous resistance of the battery at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter, set **Thermal model** to `No
temperature dependence` and **Current
dependence for resistance parameters** to
`Disabled`.

### **Instantaneous resistance, R0(SOC,T)** — Instantaneous resistance of battery at specified SOC and temperature `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm` (default) | matrix of nonnegative values

Instantaneous resistance of the battery at the specified SOC and
temperature breakpoints.

#### Dependencies

To enable this parameter, set **Thermal model** to
`Constant temperature`,
`Lumped thermal mass`, or
`Height distributed thermal mass` and
**Current dependence for resistance
parameters** to
`Disabled`.

### **Instantaneous resistance during discharging, R0(SOC)** — Instantaneous resistance of battery during discharging phase at specified SOC `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm` (default) | vector of nonnegative values

Instantaneous resistance of the battery during discharging phase at
the specified SOC breakpoints.

#### Dependencies

To enable this parameter, set **Thermal model** to `No
temperature dependence` and **Current
dependence for resistance parameters** to
`Lookup tables (current directionality
dependent)`.

### **Instantaneous resistance during charging, R0(SOC)** — Instantaneous resistance of battery during charging phase at specified SOC `[.0085, .0085, .0087, .0082, .0083, .0085, .0085]` `Ohm` (default) | vector of nonnegative values

Instantaneous resistance of the battery during charging phase at the
specified SOC breakpoints.

#### Dependencies

To enable this parameter, set **Thermal model** to `No
temperature dependence` and **Current
dependence for resistance parameters** to
`Lookup tables (current directionality
dependent)`.

### **Instantaneous resistance during charging, R0(SOC,T)** — Instantaneous resistance of battery during charging phase at specified SOC and temperature `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm` (default) | matrix of nonnegative values

Instantaneous resistance of the battery during charging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set **Thermal model** to
`Constant temperature`,
`Lumped thermal mass`, or
`Height distributed thermal mass` and
**Current dependence for resistance
parameters** to `Lookup tables (current
directionality dependent)`.

### **Instantaneous resistance during discharging, R0(SOC,T)** — Instantaneous resistance of battery during discharging phase at specified SOC and temperature `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm` (default) | matrix of nonnegative values

Instantaneous resistance of the battery during discharging phase at
the specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set **Thermal model** to
`Constant temperature`,
`Lumped thermal mass`, or
`Height distributed thermal mass` and
**Current dependence for resistance
parameters** to `Lookup tables (current
directionality dependent)`.

### **Instantaneous resistance, R0(SOC,I)** — Instantaneous resistance of battery at specified SOC and current `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` `Ohm` (default) | matrix of nonnegative values

*Since R2025a*

Instantaneous resistance of the battery at the specified SOC and
current breakpoints.

#### Dependencies

To enable this parameter, set **Thermal model**
to `No temperature dependence` and
**Current dependence for resistance
parameters** to `Lookup tables (current
dependent)`.

### **Instantaneous resistance, R0(SOC,T,I)** — Instantaneous resistance of battery at specified SOC, temperature, and current `repmat([.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089], 1, 1, 3)` `Ohm` (default) | 3-D array of nonnegative values

*Since R2025a*

Instantaneous resistance of the battery at the specified SOC,
temperature, and current breakpoints.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Constant temperature`,
`Lumped thermal mass`, or
`Height distributed thermal mass` and
**Current dependence for resistance
parameters** to `Lookup tables (current
dependent)`.

### **Parallel resistor capacitor pairs** — Option to model battery charge dynamics `No dynamics` (default) | `One time-constant dynamics` | `Two time-constant dynamics` | `Three time-constant dynamics`

Option to model the battery charge dynamics. This parameter determines
the number of parallel RC sections in the equivalent circuit.

- `No dynamics` — The equivalent
  circuit contains no parallel RC sections. The battery
  exhibits no delay between terminal voltage and internal
  charging voltage.
- `One time-constant dynamics` —
  The equivalent circuit contains one parallel RC section.
- `Two time-constant dynamics` —
  The equivalent circuit contains two parallel RC
  sections.
- `Three time-constant dynamics` —
  The equivalent circuit contains three parallel RC
  sections.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RCPairs` |
| **Values:** | `"simscape.battery.enum.cells.RCPairs.noDynamics"` (default) | `"simscape.battery.enum.cells.RCPairs.rc1"` | `"simscape.battery.enum.cells.RCPairs.rc2"` | `"simscape.battery.enum.cells.RCPairs.rc3"` |

### **First polarization resistance, R1(SOC)** — First parallel RC resistance at specified SOC `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | vector of positive values

First parallel RC resistance at the specified SOC breakpoints. This
parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First time constant, Tau1(SOC)** — First parallel RC time constant at specified SOC `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | vector of positive values

First parallel RC time constant at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `One time-constant dynamics`
  , `Two time-constant dynamics`,
  or `Three time-constant
  dynamics`.

### **Second polarization resistance, R2(SOC)** — Second parallel RC resistance at specified SOC `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | vector of positive values

Second parallel RC resistance at the specified SOC breakpoints. This
parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second time constant, Tau2(SOC)** — Second parallel RC time constant at specified SOC `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | vector of positive values

Second parallel RC time constant at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Third polarization resistance, R3(SOC)** — Third parallel RC resistance at specified SOC `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | vector of positive values

Third parallel RC resistance at the specified SOC breakpoints. This
parameter primarily affects the ohmic losses of the RC section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third time constant, Tau3(SOC)** — Third parallel RC time constant at specified SOC `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | vector of positive values

Third parallel RC time constant at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **First polarization resistance during discharging, R1(SOC)** — First parallel RC resistance during discharging phase at specified SOC `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | vector of positive values

First parallel RC resistance during discharging phase at the specified
SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First time constant during discharging, Tau1(SOC)** — First parallel RC time constant during discharging phase at specified SOC `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | vector of positive values

First parallel RC time constant during discharging phase at the
specified SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First polarization resistance during charging, R1(SOC)** — First parallel RC resistance during charging phase at specified SOC `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | vector of positive values

First parallel RC resistance during charging phase at the specified
SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First time constant during charging, Tau1(SOC)** — First parallel RC time constant during charging phase at specified SOC `[36, 45, 105, 29, 77, 33, 39]` `Ohm` (default) | vector of positive values

First parallel RC time constant during charging phase at the specified
SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **Second polarization resistance during discharging, R2(SOC)** — Second parallel RC resistance during discharging phase at specified SOC `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | vector of positive values

Second parallel RC resistance during discharging phase at the
specified SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second time constant during discharging, Tau2(SOC)** — Second parallel RC time constant during discharging phase at specified SOC `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | vector of positive values

Second parallel RC time constant during discharging phase at the
specified SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second polarization resistance during charging, R2(SOC)** — Second parallel RC resistance during charging phase at specified SOC `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | vector of positive values

Second parallel RC resistance during charging phase at the specified
SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second time constant during charging, Tau2(SOC)** — Second parallel RC time constant during charging phase at specified SOC `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | vector of positive values

Second parallel RC time constant during charging phase at the
specified SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Third polarization resistance during discharging, R3(SOC)** — Third parallel RC resistance during discharging phase at specified SOC `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | vector of positive values

Third parallel RC resistance during discharging phase at the specified
SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third time constant during discharging, Tau3(SOC)** — Third parallel RC time constant during discharging phase at specified SOC `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | vector of positive values

Third parallel RC time constant during discharging phase at the
specified SOC breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third polarization resistance during charging, R3(SOC)** — Third parallel RC resistance during charging phase at specified SOC `[.0029, .0024, .0026, .0016, .0023, .0018, .0017]` `Ohm` (default) | vector of positive values

Third parallel RC resistance during the charging phase at the
specified SOC.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third time constant during charging, Tau3(SOC)** — Third parallel RC time constant during charging phase at specified SOC `[36, 45, 105, 29, 77, 33, 39]` `s` (default) | vector of positive values

Third parallel RC time constant during charging phase at the specified
SOC.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **First polarization resistance, R1(SOC,T)** — First parallel RC resistance at specified SOC and temperature `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

First parallel RC resistance at the specified SOC and temperature
breakpoints. This parameter primarily affects the ohmic losses of the RC
section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First time constant, Tau1(SOC,T)** — First parallel RC time constant at specified SOC and temperature `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

First parallel RC time constant at the specified SOC and temperature
breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **Second polarization resistance, R2(SOC,T)** — Second parallel RC resistance at specified SOC and temperature `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

Second parallel RC resistance at the specified SOC and temperature
breakpoints. This parameter primarily affects the ohmic losses of the RC
section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second time constant, Tau2(SOC,T)** — Second parallel RC time constant at specified SOC and temperature `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

Second parallel RC time constant at the specified SOC and temperature
breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Third polarization resistance, R3(SOC,T)** — Third parallel RC resistance at the specified SOC and temperature `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

Third parallel RC resistance at the specified SOC and temperature
breakpoints. This parameter primarily affects the ohmic losses of the RC
section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third time constant, Tau3(SOC,T)** — Third parallel RC time constant at specified SOC and temperature `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

Third parallel RC time constant at the specified SOC and temperature
breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to
  `Disabled`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **First polarization resistance during discharging, R1(SOC,T)** — First parallel RC resistance during discharging phase at specified SOC and temperature `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

First parallel RC resistance during the discharging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First time constant during discharging, Tau1(SOC,T)** — First parallel RC time constant during discharging phase at specified SOC and temperature `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

First parallel RC time constant during the discharging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First polarization resistance during charging, R1(SOC,T)** — First parallel RC resistance during charging phase at specified SOC and temperature `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

First parallel RC resistance during the charging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First time constant during charging, Tau1(SOC,T)** — First parallel RC time constant during charging phase at specified SOC and temperature `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

First parallel RC time constant during the charging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **Second polarization resistance during discharging, R2(SOC,T)** — Second parallel RC resistance during discharging phase at specified SOC and temperature `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

Second parallel RC resistance during the discharging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second time constant during discharging, Tau2(SOC,T)** — Second parallel RC time constant during discharging phase at specified SOC and temperature `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

Second parallel RC time constant during the discharging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second polarization resistance during charging, R2(SOC,T)** — Second parallel RC resistance during charging phase at specified SOC and temperature `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

Second parallel RC resistance during the charging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second time constant during charging, Tau2(SOC,T)** — Second parallel RC time constant during charging phase at specified SOC and temperature `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

Second parallel RC time constant during the charging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Third polarization resistance during discharging, R3(SOC,T)** — Third parallel RC resistance during discharging phase at specified SOC and temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

Third parallel RC resistance during the discharging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third time constant during discharging, Tau3(SOC,T)** — Third parallel RC time constant during discharging phase at specified SOC and temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

Third parallel RC time constant during the discharging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third polarization resistance during charging, R3(SOC,T)** — Third parallel RC resistance during charging phase at specified SOC and temperature breakpoints `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

Third parallel RC resistance during the charging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third time constant during charging, Tau3(SOC,T)** — Third parallel RC time constant during charging phase at specified SOC and temperature breakpoints `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

Third parallel RC resistance during the charging phase at the
specified SOC and temperature breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current directionality
  dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **First polarization resistance, R1(SOC,I)** — First parallel RC resistance at specified SOC and current `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

*Since R2025a*

First parallel RC resistance at the specified SOC and current
breakpoints. This parameter primarily affects the ohmic losses of the RC
section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First time constant, Tau1(SOC,I)** — First parallel RC time constant at specified SOC and current `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

*Since R2025a*

First parallel RC time constant at the specified SOC and current
breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **Second polarization resistance, R2(SOC,I)** — Second parallel RC resistance at specified SOC and current `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

*Since R2025a*

Second parallel RC resistance at the specified SOC and current
breakpoints. This parameter primarily affects the ohmic losses of the RC
section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second time constant, Tau2(SOC,I)** — Second parallel RC time constant at specified SOC and current `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

*Since R2025a*

Second parallel RC time constant at the specified SOC and current
breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Third polarization resistance, R3(SOC,I)** — Third parallel RC resistance at the specified SOC and current `[.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011]` `Ohm` (default) | matrix of positive values

*Since R2025a*

Third parallel RC resistance at the specified SOC and current
breakpoints. This parameter primarily affects the ohmic losses of the RC
section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third time constant, Tau3(SOC,I)** — Third parallel RC time constant at specified SOC and current `[20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33]` `s` (default) | matrix of positive values

*Since R2025a*

Third parallel RC time constant at the specified SOC and current
breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to `No
  temperature dependence`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **First polarization resistance, R1(SOC,T,I)** — First parallel RC resistance at specified SOC, temperature, and current `repmat([.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011], 1, 1, 3)` `Ohm` (default) | 3-D array of positive values

*Since R2025a*

First parallel RC resistance at the specified SOC, temperature, and
current breakpoints. This parameter primarily affects the ohmic losses
of the RC section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **First time constant, Tau1(SOC,T,I)** — First parallel RC time constant at specified SOC, temperature, and current `repmat([20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33], 1, 1, 3)` `s` (default) | 3-D array of positive values

*Since R2025a*

First parallel RC time constant at the specified SOC, temperature, and
current breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `One time-constant
  dynamics`, `Two time-constant
  dynamics`, or `Three
  time-constant dynamics`.

### **Second polarization resistance, R2(SOC,T,I)** — Second parallel RC resistance at specified SOC, temperature, and current `repmat([.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011], 1, 1, 3)` `Ohm` (default) | 3-D array of positive values

*Since R2025a*

Second parallel RC resistance at the specified SOC, temperature, and
current breakpoints. This parameter primarily affects the ohmic losses
of the RC section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Second time constant, Tau2(SOC,T,I)** — Second parallel RC time constant at specified SOC, temperature, and current `[repmat([20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33], 1, 1, 3)` `s` (default) | 3-D array of positive values

*Since R2025a*

Second parallel RC time constant at the specified SOC, temperature,
and current breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `Two time-constant dynamics`
  or `Three time-constant
  dynamics`.

### **Third polarization resistance, R3(SOC,T,I)** — Third parallel RC resistance at the specified SOC. temperature, and current `[repmat([.0109, .0029, .0013; .0069, .0024, .0012; .0047, .0026, .0013; .0034, .0016, .001; .0033, .0023, .0014; .0033, .0018, .0011; .0028, .0017, .0011], 1, 1, 3)` `Ohm` (default) | 3-D array of positive values

*Since R2025a*

Third parallel RC resistance at the specified SOC, temperature, and
current breakpoints. This parameter primarily affects the ohmic losses
of the RC section.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Third time constant, Tau3(SOC,T,I)** — Third parallel RC time constant at specified SOC, temperature, and current `repmat([20, 36, 39; 31, 45, 39; 109, 105, 61; 36, 29, 26; 59, 77, 67; 40, 33, 29; 25, 39, 33], 1, 1, 3)` `s` (default) | matrix of positive values

*Since R2025a*

Third parallel RC time constant at the specified SOC, temperature, and
current breakpoints.

#### Dependencies

To enable this parameter, set:

- **Thermal model** to
  `Constant temperature`,
  `Lumped thermal mass`, or
  `Height distributed thermal
  mass`.
- **Current dependence for resistance
  parameters** to `Lookup tables
  (current dependent)`.
- **Parallel resistor capacitor pairs**
  to `Three time-constant
  dynamics`.

### **Self discharge** — Option to model battery self-discharge resistance `Disabled` (default) | `Enabled`

Option to model the self-discharge resistance of the battery. The
block models this effect as a resistor across the terminals of the
fundamental battery model.

As the temperature increases, the self-discharge resistance decreases.
If the decrease in resistance is too fast, the battery might experience
thermal runaway and numerical instability. To resolve this instability,
perform these steps:

- Decrease the thermal resistance.
- Decrease the gradient of the self-discharge resistance with
  respect to temperature.
- Increase the self-discharge resistance.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SelfDischargeResistor` |
| **Values:** | `"simscape.battery.enum.cells.BatteryEnable.Disabled"` (default) | `"simscape.battery.enum.cells.BatteryEnable.Enabled"` |

### **Self-discharge resistance, SelfDischargeR** — Self-discharge resistance of battery `7e3` `Ohm` (default) | positive scalar

Self-discharge resistance of the battery. This resistance acts across
the terminals of the fundamental battery model.

#### Dependencies

To enable this parameter, set **Thermal model**
to `No temperature dependence` and
**Self discharge** to
`Enabled`.

### **Self-discharge resistance, SelfDischargeR(T)** — Self-discharge resistance of battery at specified temperature `[8000, 7000, 6000]` `Ohm` (default) | vector of positive values

Self-discharge resistance of the battery at the specified temperature
breakpoints. This resistance acts across the terminals of the
fundamental battery model.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Constant temperature` or
`Lumped thermal mass` and
**Self discharge** to
`Enabled`.

### Cycling Aging

### **Cycling aging model** — Option to define fading characteristic `Disabled` (default) | `Equations` | `Lookup tables (temperature independent)` | `Lookup tables (constant temperature dependent)` | `Lookup tables (temperature dependent)` | `Lookup tables (temperature and current dependent)`

Option to define the fading characteristic:

- `Disabled` — Do not model fading
  characteristic.
- `Equations` — The cell capacity
  and terminal resistance are proportional to N. The open-circuit voltage is proportional
  to *N*. If you enable the self-discharge
  resistance or any of the time constants, their values are
  proportional to N.
- `Lookup tables (temperature
  independent)` — Set tabulated data for the
  percentage change in parameters as a function of
  *N*.
- `Lookup tables (constant temperature
  dependent)` — Set tabulated data for the
  percentage change in parameters as a function of
  *N* and constant temperature.
- `Lookup
  tables (temperature dependent)` — Set
  tabulated data for the percentage change in parameters as a
  function of *N* and variable temperature.
  This tabulated data must be strictly monotonically
  increasing or decreasing with respect to the number of
  discharge cycles. *(since R2025a)*
- `Lookup
  tables (temperature and current dependent)`
  — Set tabulated data for the percentage change in parameters
  as a function of *N*, variable temperature,
  and variable current. This tabulated data must be strictly
  monotonically increasing or decreasing with respect to the
  number of discharge cycles. *(since R2025a)*

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CyclingAgingMethod` |
| **Values:** | `"simscape.battery.enum.cells.CyclingAgingMethod.disabled"` (default) | `"simscape.battery.enum.cells.CyclingAgingMethod.equations"` | `"simscape.battery.enum.cells.CyclingAgingMethod.tableN"` | `"simscape.battery.enum.cells.CyclingAgingMethod.tableNandT"` | `"simscape.battery.enum.cells.CyclingAgingMethod.tableNandVariableT"` | `"simscape.battery.enum.cells.CyclingAgingMethod.tableNandVariableTandI"` |

### **Cycle calculation method** — Option to choose how block calculates number of discharge cycles `Equivalent cycles` (default) | `Equivalent full cycles`

*Since R2025a*

Option to choose how the block calculates the change in number of
discharge cycles:

- `Equivalent cycles` — The block
  uses the aged capacity to calculate the number of discharge
  cycles.
- `Equivalent full cycles` — The
  block uses the nominal capacity to calculate the number of
  discharge cycles.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Equations`,
`Lookup tables (temperature
independent)`, `Lookup tables (constant
temperature dependent)`, `Lookup tables
(temperature dependent)`, or `Lookup
tables (temperature and current dependent)`.

### **Number of discharge cycles, NumDisCycles** — Number of cycles for percentage change calculations `100` (default) | scalar in the range [1, `inf`)

Number of charge-discharge cycles over which the specified percentage
changes occur.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Equations`.

### **Change in open-circuit voltage after NumDisCycles discharge cycles (%)** — Percentage change in open-circuit voltage after *NumDisCycles* cycles `0` (default) | scalar

Percentage change in the open-circuit voltage after the battery
undergoes *NumDisCycles* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the open-circuit voltage increases. If you specify a negative value
for this parameter, the value of the open-circuit voltage decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Equations`.

### **Change in terminal resistance after NumDisCycles discharge cycles (%)** — Percentage change in terminal resistance after *NumDisCycles* cycles `0` (default) | scalar

Percentage change in the terminal resistance after the battery
undergoes *NumDisCycles* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the terminal resistance increases. If you specify a negative value
for this parameter, the value of the terminal resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Equations`.

### **Change in cell capacity after NumDisCycles discharge cycles (%)** — Percentage change in cell capacity after *NumDisCycles* cycles `0` (default) | scalar

Percentage change in the cell capacity after the battery undergoes
*NumDisCycles* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the cell capacity increases. If you specify a negative value for
this parameter, the value of the cell capacity decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Equations`.

### **Change in self-discharge resistance after NumDisCycles discharge cycles (%)** — Percentage change in self-discharge resistance after *NumDisCycles* cycles `0` (default) | scalar

Percentage change in the self-discharge resistance after the battery
undergoes *NumDisCycles* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the self-discharge resistance increases. If you specify a negative
value for this parameter, the value of the self-discharge resistance
decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Equations` and
**Self discharge** to
`Enabled`.

### **Change in first polarization resistance after NumDisCycles discharge cycles (%)** — Percentage change in first RC resistance after *NumDisCycles* cycles `0` (default) | scalar

Percentage change in the first RC resistance after the battery
undergoes *NumDisCycles* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the first RC resistance increases. If you specify a negative value
for this parameter, the value of the first RC resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Equations` and
**Parallel resistor capacitor pairs** to
`One time-constant dynamics`,
`Two time-constant dynamics`, or
`Three time-constant dynamics`.

### **Change in second polarization resistance after NumDisCycles discharge cycles (%)** — Percentage change in second RC resistance after *NumDisCycles* cycles `0` (default) | scalar

Percentage change in the second RC resistance after the battery
undergoes *NumDisCycles* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the second RC resistance increases. If you specify a negative value
for this parameter, the value of the second RC resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Equations` and
**Parallel resistor capacitor pairs** to
`Two time-constant dynamics`, or
`Three time-constant dynamics`.

### **Change in third polarization resistance after NumDisCycles discharge cycles (%)** — Percentage change in third RC resistance after *NumDisCycles* cycles `0` (default) | scalar

Percentage change in the third RC resistance after the battery
undergoes *NumDisCycles* discharge cycles.

**Note**

If you specify a positive value for this parameter, the value of
the third RC resistance increases. If you specify a negative value
for this parameter, the value of the third RC resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Equations` and
**Parallel resistor capacitor pairs** to
`Three time-constant dynamics`.

### **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** — Reference vector or numbers of cycles for percentage change calculations `[0, 100, 200, 300]` (default) | vector of nonnegative values

Numbers of charge-discharge cycles over which the specified percentage
changes occur.

#### Dependencies

To enable this parameter, set **Cycling aging model** to
`Lookup tables (temperature
independent)`, `Lookup tables (constant
temperature dependent)`, `Lookup tables
(temperature dependent)`, or `Lookup
tables (temperature and current dependent)`.

### **Temperatures breakpoints for cycling aging data, T** — Temperature breakpoints at which block extracts fading lookup tables `[298.15, 323.15]` `K` (default) | vector of entries in the range [1, `inf`)

Temperature breakpoints at which the block extracts the fading lookup
tables. These temperatures are completely independent of the
**Temperature breakpoints, T** parameter from the
**Main** section.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (constant
temperature dependent)`, `Lookup tables
(temperature dependent)`, or `Lookup
tables (temperature and current dependent)`.

### **Current breakpoints for cycling aging data, I** — Current breakpoints at which block extracts fading lookup tables `[-.1, -.5, -5]` `A` (default) | vector of negative scalars

*Since R2025a*

Current breakpoints at which the block extracts the fading lookup
tables.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature and
current dependent)`.

### **Percentage change in open-circuit voltage, OCVChange(N)** — Percentage change in open-circuit voltage after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Percentage change in the open-circuit voltage after the battery undergoes
*N* discharge cycles.

The size of this parameter must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the open-circuit voltage increases. If you specify a negative value
for this parameter, the value of the open-circuit voltage decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
independent)`.

### **Percentage change in terminal resistance, R0Change(N)** — Percentage change in terminal resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Percentage change in the terminal resistance after the battery
undergoes *N* discharge cycles.

The size of this parameter must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the terminal resistance increases. If you specify a negative value
for this parameter, the value of the terminal resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
independent)`.

### **Percentage change in cell capacity, CapacityChange(N)** — Percentage change in cell capacity after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Percentage change in the cell capacity after the battery undergoes
*N* discharge cycles.

The size of this parameter must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the cell capacity increases. If you specify a negative value for
this parameter, the value of the cell capacity decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
independent)`.

### **Percentage change in self-discharge resistance, SelfDischargeRChange(N)** — Percentage change in self-discharge resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Percentage change in the self-discharge resistance after the battery
undergoes *N* discharge cycles.

The size of this parameter must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the self-discharge resistance increases. If you specify a negative
value for this parameter, the value of the self-discharge resistance
decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
independent)` and **Self
discharge** to
`Enabled`.

### **Percentage change in first polarization resistance, R1Change(N)** — Percentage change in first parallel RC resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Percentage change in the first parallel RC resistance after the
battery undergoes *N* discharge cycles.

The size of this parameter must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the first parallel RC resistance increases. If you specify a
negative value for this parameter, the value of the first parallel
RC resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
independent)` and **Parallel resistor
capacitor pairs** to `One time-constant
dynamics`, `Two time-constant
dynamics`, or `Three time-constant
dynamics`.

### **Percentage change in second polarization resistance, R2Change(N)** — Percentage change in second parallel RC resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Percentage change in the second parallel RC resistance after the
battery undergoes *N* discharge cycles.

The size of this parameter must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the second parallel RC resistance increases. If you specify a
negative value for this parameter, the value of the second parallel
RC resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
independent)` and **Parallel resistor
capacitor pairs** to `Two time-constant
dynamics` or `Three time-constant
dynamics`.

### **Percentage change in third polarization resistance, R3Change(N)** — Percentage change in third parallel RC resistance after *N* cycles `[0, 0, 0, 0]` (default) | vector of scalars

Percentage change in the third parallel RC resistance after the
battery undergoes *N* discharge cycles.

The size of this parameter must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the third parallel RC resistance increases. If you specify a
negative value for this parameter, the value of the third parallel
RC resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
independent)` and **Parallel resistor
capacitor pairs** to `Three time-constant
dynamics`.

### **Percentage change in open-circuit voltage, OCVChange(N,T)** — Percentage change in open-circuit voltage after *N* cycles at specified temperature `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Percentage changes in the open-circuit voltage after the battery
undergoes *N* discharge cycles at the specified
temperature.

The number of rows of this matrix must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The number of columns of this matrix must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the open-circuit voltage increases. If you specify a negative value
for this parameter, the value of the open-circuit voltage decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (constant
temperature dependent)`.

### **Percentage change in terminal resistance, R0Change(N,T)** — Percentage change in terminal resistance after *N* cycles at specified temperature `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Percentage changes in the terminal resistance after the battery
undergoes *N* discharge cycles at the specified
temperature.

The number of rows of this matrix must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The number of columns of this matrix must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the terminal resistance increases. If you specify a negative value
for this parameter, the value of the terminal resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (constant
temperature dependent)` or `Lookup
tables (temperature dependent)`.

### **Initial target for percentage change in internal resistance due to cycling aging** — Initial target value for percentage change in internal resistance due to cycling aging `0` (default) | scalar

*Since R2025a*

Initial target value for the percentage change in internal resistance
due to cycling aging.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
dependent)` or `Lookup tables
(temperature and current dependent)`.

### **Percentage change in cell capacity, CapacityChange(N,T)** — Percentage change in cell capacity after *N* cycles at specified temperature `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Percentage changes in cell capacity after the battery undergoes
*N* discharge cycles at the specified
temperature.

The number of rows of this matrix must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The number of columns of this matrix must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the cell capacity increases. If you specify a negative value for
this parameter, the value of the cell capacity decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (constant
temperature dependent)` or `Lookup
tables (temperature dependent)`.

### **Initial target for percentage change in capacity due to cycling aging** — Initial target value for percentage change in capacity due to cycling aging `0` (default) | scalar

*Since R2025a*

Initial target value for the percentage change in capacity due to
cycling aging.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
dependent)` or `Lookup tables
(temperature and current dependent)`.

### **Percentage change in self-discharge resistance, SelfDischargeRChange(N,T)** — Percentage change in self-discharge resistance after *N* cycles at specified temperature `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Percentage changes in the self-discharge resistance after the battery
undergoes *N* discharge cycles at the specified
temperature.

The number of rows of this matrix must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The number of columns of this matrix must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the self-discharge resistance increases. If you specify a negative
value for this parameter, the value of the self-discharge resistance
decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (constant
temperature dependent)` or `Lookup
tables (temperature dependent)`.

### **Initial target for percentage change in self-discharge resistance due to cycling aging** — Initial target value for percentage change in self-discharge resistance due to cycling aging `0` (default) | scalar

*Since R2025a*

Initial target value for the percentage change in self-discharge
resistance due to cycling aging.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
dependent)` or `Lookup tables
(temperature and current dependent)` and
**Self discharge** to
`Enabled`.

### **Percentage change in first polarization resistance, R1Change(N,T)** — Percentage change in first parallel RC resistance after *N* cycles at specified temperature `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Percentage changes in the first parallel RC resistance after the
battery undergoes *N* discharge cycles at the specified
temperature.

The number of rows of this matrix must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The number of columns of this matrix must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the first parallel RC resistance increases. If you specify a
negative value for this parameter, the value of the first parallel
RC resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (constant
temperature dependent)` or `Lookup
tables (temperature dependent)` and
**Parallel resistor capacitor pairs** to
`One time-constant dynamics`,
`Two time-constant dynamics`, or
`Three time-constant dynamics`.

### **Initial target for percentage change in first polarization resistance due to cycling aging** — Initial target value for percentage change in first polarization resistance due to cycling aging `0` (default) | scalar

*Since R2025a*

Initial target value for the percentage change in first polarization
resistance due to cycling aging.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
dependent)` or `Lookup tables
(temperature and current dependent)` and
**Parallel resistor capacitor pairs** to
`One time-constant dynamics`,
`Two time-constant dynamics`, or
`Three time-constant dynamics`.

### **Percentage change in second polarization resistance, R2Change(N,T)** — Percentage change in second parallel RC resistance after *N* cycles at specified temperature `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Percentage changes in the second parallel RC resistance after the
battery undergoes *N* discharge cycles at the specified
temperature.

The number of rows of this matrix must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The number of columns of this matrix must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the second parallel RC resistance increases. If you specify a
negative value for this parameter, the value of the second parallel
RC resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (constant
temperature dependent)` or `Lookup
tables (temperature dependent)` and
**Parallel resistor capacitor pairs** to
`Two time-constant dynamics` or
`Three time-constant dynamics`.

### **Initial target for percentage change in second polarization resistance due to cycling aging** — Initial target value for percentage change in second polarization resistance due to cycling aging `0` (default) | scalar

*Since R2025a*

Initial target value for the percentage change in second polarization
resistance due to cycling aging.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
dependent)` or `Lookup tables
(temperature and current dependent)` and
**Parallel resistor capacitor pairs** to
`Two time-constant dynamics` or
`Three time-constant dynamics`.

### **Percentage change in third polarization resistance, R3Change(N,T)** — Percentage change in third parallel RC resistance after *N* cycles at specified temperature `[0, 0; 0, 0; 0, 0; 0, 0]` (default) | matrix of scalars

Percentage changes in the third parallel RC resistance after the
battery undergoes *N* discharge cycles at the specified
temperature.

The number of rows of this matrix must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The number of columns of this matrix must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the third parallel RC resistance increases. If you specify a
negative value for this parameter, the value of the third parallel
RC resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (constant
temperature dependent)` or `Lookup
tables (temperature dependent)` and
**Parallel resistor capacitor pairs** to
`Three time-constant dynamics`.

### **Initial target for percentage change in third polarization resistance due to cycling aging** — Initial target value for percentage change in third polarization resistance due to cycling aging `0` (default) | scalar

*Since R2025a*

Initial target value for the percentage change in third polarization
resistance due to cycling aging.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature
dependent)` or `Lookup tables
(temperature and current dependent)` and
**Parallel resistor capacitor pairs** to
`Three time-constant dynamics`.

### **Percentage change in terminal resistance, R0Change(N,T,I)** — Percentage change in terminal resistance after *N* cycles at specified temperature and current `repmat(0, 4, 2, 3)` (default) | 3-D array of scalars

*Since R2025a*

Percentage changes in the terminal resistance after the battery
undergoes *N* discharge cycles at the specified
temperature and current.

The size of the first dimension of this 3-D array must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The size of the second dimension of this 3-D array must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter. The size of the third dimension of this 3-D array must be equal to the size of the **Current breakpoints for cycling aging data, I** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the terminal resistance increases. If you specify a negative value
for this parameter, the value of the terminal resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature and
current dependent)`.

### **Percentage change in cell capacity, CapacityChange(N,T,I)** — Percentage change in cell capacity after *N* cycles at specified temperature and current `repmat(0, 4, 2, 3)` (default) | 3-D array of scalars

*Since R2025a*

Percentage changes in the cell capacity after the battery undergoes
*N* discharge cycles at the specified temperature
and current.

The size of the first dimension of this 3-D array must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The size of the second dimension of this 3-D array must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter. The size of the third dimension of this 3-D array must be equal to the size of the **Current breakpoints for cycling aging data, I** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the cell capacity increases. If you specify a negative value for
this parameter, the value of the cell capacity decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature and
current dependent)`.

### **Percentage change in self-discharge resistance, SelfDischargeRChange(N,T,I)** — Percentage change in self-discharge resistance after *N* cycles at specified temperature and current `repmat(0, 4, 2, 3)` (default) | 3-D array of scalars

*Since R2025a*

Percentage changes in the self-discharge resistance after the battery
undergoes *N* discharge cycles at the specified
temperature and current.

The size of the first dimension of this 3-D array must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The size of the second dimension of this 3-D array must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter. The size of the third dimension of this 3-D array must be equal to the size of the **Current breakpoints for cycling aging data, I** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the self-discharge resistance increases. If you specify a negative
value for this parameter, the value of the self-discharge resistance
decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature and
current dependent)` and **Self
discharge**to
`Enabled`.

### **Percentage change in first polarization resistance, R1Change(N,T,I)** — Percentage change in first polarization resistance after *N* cycles at specified temperature and current `repmat(0, 4, 2, 3)` (default) | 3-D array of scalars

*Since R2025a*

Percentage changes in the first polarization resistance after the
battery undergoes *N* discharge cycles at the specified
temperature and current.

The size of the first dimension of this 3-D array must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The size of the second dimension of this 3-D array must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter. The size of the third dimension of this 3-D array must be equal to the size of the **Current breakpoints for cycling aging data, I** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the first polarization resistance increases. If you specify a
negative value for this parameter, the value of the first
polarization resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature and
current dependent)`and **Parallel resistor
capacitor pairs** to `One time-constant
dynamics`, `Two time-constant
dynamics`, or `Three time-constant
dynamics`.

### **Percentage change in second polarization resistance, R2Change(N,T,I)** — Percentage change in second polarization resistance after *N* cycles at specified temperature and current `repmat(0, 4, 2, 3)` (default) | 3-D array of scalars

*Since R2025a*

Percentage changes in the second polarization resistance after the
battery undergoes *N* discharge cycles at the specified
temperature and current.

The size of the first dimension of this 3-D array must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The size of the second dimension of this 3-D array must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter. The size of the third dimension of this 3-D array must be equal to the size of the **Current breakpoints for cycling aging data, I** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the second polarization resistance increases. If you specify a
negative value for this parameter, the value of the second
polarization resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature and
current dependent)`and **Parallel resistor
capacitor pairs** to `Two time-constant
dynamics` or `Three time-constant
dynamics`.

### **Percentage change in third polarization resistance, R2Change(N,T,I)** — Percentage change in third polarization resistance after *N* cycles at specified temperature and current `repmat(0, 4, 2, 3)` (default) | 3-D array of scalars

*Since R2025a*

Percentage changes in the third polarization resistance after the
battery undergoes *N* discharge cycles at the specified
temperature and current.

The size of the first dimension of this 3-D array must be equal to the size of the **Number of discharge cycles breakpoints, NumDisCyclesBreakpoints** parameter. The size of the second dimension of this 3-D array must be equal to the size of the **Temperatures breakpoints for cycling aging data, T** parameter. The size of the third dimension of this 3-D array must be equal to the size of the **Current breakpoints for cycling aging data, I** parameter.

This parameter accepts a percentage value. For example, if the capacity of your battery decreases by 2% after 100 cycles, 4% after 200 cycles, and 8% after 300 cycles, set the corresponding percentage change parameter to `[0,-2,-4,-8]`.

**Note**

If you specify a positive value for this parameter, the value of
the third polarization resistance increases. If you specify a
negative value for this parameter, the value of the third
polarization resistance decreases.

#### Dependencies

To enable this parameter, set **Cycling aging
model** to `Lookup tables (temperature and
current dependent)`and **Parallel resistor
capacitor pairs** to `Three time-constant
dynamics`.

### Calendar Aging

### **Resistance calendar aging** — Option to enable calendar aging for resistance `Disabled` (default) | `Enabled`

Option to enable calendar aging for the resistance of the
battery.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CalendarAgeResistance` |
| **Values:** | `"simscape.battery.enum.cells.BatteryEnable.Disabled"` (default) | `"simscape.battery.enum.cells.BatteryEnable.Enabled"` |

### **Capacity calendar aging** — Option to enable calendar aging for capacity `Disabled` (default) | `Enabled`

Option to enable calendar aging for the capacity of the
battery.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CalendarAgeCapacity` |
| **Values:** | `"simscape.battery.enum.cells.BatteryEnable.Disabled"` (default) | `"simscape.battery.enum.cells.BatteryEnable.Enabled"` |

### **Modeling option** — Modeling option for calendar aging `Equation-based` (default) | `Tabulated: temperature` | `Tabulated: time and temperature`

Modeling option for resistance and capacity calendar aging.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** or **Capacity calendar aging**
to `Enabled`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CalendarAgingMethod` |
| **Values:** | `"simscape.battery.enum.cells.CalendarAgingMethod.equation"` (default) | `"simscape.battery.enum.cells.CalendarAgingMethod.tableT"` | `"simscape.battery.enum.cells.CalendarAgingMethod.tableTandTime"` |

### **Storage condition** — Storage condition `Specify open-circuit voltage during storage` (default) | `Specify state-of-charge during storage`

Option to specify the open-circuit voltage or the SOC during
storage.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Equation-based`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StorageVariable` |
| **Values:** | `"simscape.battery.enum.cells.StorageVariable.OCV"` (default) | `"simscape.battery.enum.cells.StorageVariable.SOC"` |

### **Normalized open-circuit voltage during storage, V/Vnom** — Normalized open-circuit voltage during storage `0.9` (default) | scalar

Normalized open-circuit voltage during storage.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Equation-based` and **Storage
condition** to `Specify open-circuit
voltage during storage`.

### **State of charge during storage** — Percentage SOC during storage `0.6` (default) | scalar in the range [0, 1]

Percentage SOC during storage.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Equation-based` and **Storage
condition** to `Specify state-of-charge
during storage`.

### **Vector of time intervals** — Time intervals `[0]` `d` (default) | vector of scalars

Time intervals. The size of this parameter must be equal to the size
of the **Vector of storage temperatures**
parameter.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Equation-based`,
`Tabulated: temperature`, or
`Tabulated: time and
temperature`.

### **Vector of storage temperatures** — Storage temperatures `[273]` `K` (default) | vector of nonnegative values

Storage temperatures. The size of this parameter must be equal to the
size of the **Vector of time intervals**
parameter.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Equation-based`,
`Tabulated: temperature`, or
`Tabulated: time and
temperature`.

### **Terminal resistance linear scaling for voltage, b** — Voltage linear scaling coefficient of terminal resistance `2.2134e6` (default) | scalar

Linear scaling coefficient of the terminal resistance for the
open-circuit voltage.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** to `Enabled` and
**Modeling option** to
`Equation-based`.

### **Terminal resistance constant offset for voltage, c** — Voltage constant offset of terminal resistance `1.632e6` (default) | scalar

Constant offset of the terminal resistance for the open-circuit
voltage.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** to `Enabled` and
**Modeling option** to
`Equation-based`.

### **Terminal resistance temperature-dependent exponential increase, d** — Temperature-dependent exponential increase in terminal resistance `0.515833569` `V` (default) | scalar

Temperature-dependent exponential increase in terminal
resistance.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** to `Enabled` and
**Modeling option** to
`Equation-based`.

### **Terminal resistance time exponent, a** — Time exponent in terminal resistance `0.75` (default) | scalar

Time exponent in the terminal resistance.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** to `Enabled` and
**Modeling option** to
`Equation-based` or
`Tabulated: temperature`.

### **Vector of sampled temperatures for terminal resistance calendar aging, T\_ar** — Sampled temperatures for terminal resistance calendar aging `[273.15, 298.15, 323.15]` `K` (default) | vector of positive values

Sampled temperatures for the calendar aging of the terminal
resistance.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
temperature` or `Tabulated: time and
temperature`.

### **Vector of sampled storage time intervals for terminal resistance calendar aging, t\_ar** — Sampled storage time intervals for terminal resistance calendar aging `[90, 180, 270, 360]` `d` (default) | vector of positive values

Sampled storage time intervals for the calendar aging of the terminal
resistance.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
time and temperature`.

### **Percentage change in terminal resistance due to calendar aging, dR0(T\_ar)** — Percentage change in terminal resistance due to calendar aging `[0,0,0]` (default) | vector of scalars

Percentage change in the terminal resistance due to the calendar
aging.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
temperature`.

### **Time between terminal resistance beginning of life and dR(T\_ar) measurement** — Time between terminal resistance at beginning of life and *dR(Tar)* measurement `100` `d` (default) | nonnegative scalar

Time between the battery terminal resistance at the beginning of life
and the *dR(Tar)*
measurement.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
temperature`.

### **Percentage change in terminal resistance due to calendar aging, dR0(t\_ar,T\_ar)** — Percentage change in terminal resistance due to calendar aging `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]` (default) | matrix of scalars

Percentage change in the terminal resistance due to the calendar
aging.

#### Dependencies

To enable this parameter, set **Resistance calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
time and temperature`.

### **Capacity linear scaling for voltage, b** — Voltage linear scaling of capacity `1.5097e07` (default) | scalar

Linear scaling coefficient of capacity for the open-circuit
voltage.

#### Dependencies

To enable this parameter, set **Capacity calendar
aging** to `Enabled` and
**Modeling option** to
`Equation-based`.

### **Capacity constant offset for voltage, c** — Voltage constant offset of capacity `8.3625e06` (default) | scalar

Constant offset of capacity for the open-circuit voltage.

#### Dependencies

To enable this parameter, set **Capacity calendar
aging** to `Enabled` and
**Modeling option** to
`Equation-based`.

### **Capacity temperature-dependent exponential decrease, d** — Temperature-dependent exponential decrease in capacity `0.6011` `V` (default) | scalar

Temperature-dependent exponential decrease in capacity.

#### Dependencies

To enable this parameter, set **Capacity calendar
aging** to `Enabled` and
**Modeling option** to
`Equation-based`.

### **Capacity time exponent, a** — Time exponent in capacity `0.75` (default) | scalar

Time exponent in capacity.

#### Dependencies

To enable this parameter, set **Capacity calendar
aging** to `Enabled` and
**Modeling option** to
`Equation-based` or
`Tabulated: temperature`.

### **Vector of sampled temperatures for capacity calendar aging, T\_ac** — Sampled temperatures for capacity calendar aging `[273.15, 298.15, 323.15]` `K` (default) | vector of positive values

Sampled temperatures for the calendar aging of the capacity.

#### Dependencies

To enable this parameter, set **Capacity calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
temperature` or `Tabulated: time and
temperature`.

### **Vector of sampled storage time intervals for capacity calendar aging, t\_ac** — Sampled storage time intervals for capacity calendar aging `[90, 180, 270, 360]` `d` (default) | vector of positive values

Sampled storage time intervals for the calendar aging of the
capacity.

#### Dependencies

To enable this parameter, set **Capacity calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
time and temperature`.

### **Percentage change in capacity due to calendar aging, dAH(T\_ac)** — Percentage change in capacity due to calendar aging `[0, 0, 0]` (default) | vector of scalars

Percentage change in the capacity due to the calendar aging.

#### Dependencies

To enable this parameter, set **Capacity calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
temperature`.

### **Time between capacity beginning of life and dAH(T\_ac) measurement** — Time between capacity at beginning of life and *dAH(Tac)* measurement `100` `d` (default) | positive scalar

Time between the battery capacity at the beginning of life and the
*dAH(Tac)*
measurement.

#### Dependencies

To enable this parameter, set **Capacity calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
temperature`.

### **Percentage change in capacity due to calendar aging, dAH(t\_ac,T\_ac)** — Percentage change in capacity due to calendar aging `[0, 0, 0; 0, 0, 0; 0, 0, 0; 0, 0, 0]` (default) | matrix of scalars

Percentage change in the capacity due to the calendar aging.

#### Dependencies

To enable this parameter, set **Capacity calendar
aging** to `Enabled` and
**Modeling option** to `Tabulated:
time and temperature`.

### Thermal

### **Simulation temperature** — Battery temperature `298.15` `K` (default) | positive scalar

Battery temperature that the block uses in lookup tables throughout
simulation.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Constant temperature`.

### **Battery thermal mass** — Battery thermal mass associated with thermal port `100` `J/K` (default) | positive scalar

Thermal mass of the battery associated with the thermal port **H** or
**HDist**. This parameter represents the energy
required to raise the temperature of the thermal port by one kelvin.

#### Dependencies

To enable this parameter, set **Thermal model** to `Lumped
thermal mass` or `Height distributed
thermal mass`.

### **Number of thermal models** — Number of discretized elements in thermal model `6` (default) | positive scalar

*Since R2024b*

Number of discretized elements in the thermal model. The value of this
parameter affects the size of the array of thermal nodes at port
**HDist**.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Height distributed thermal
mass`.

### **Thermal conductivity in Z dimension** — Thermal conductivity of cell in *Z* dimension `18` `W/(K*m)` (default) | positive scalar

*Since R2024b*

Thermal conductivity of the cell in the *Z*
dimension. This parameter affects the heat exchange between the nodes of
the array of thermal nodes, **HDist**.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Height distributed thermal
mass`.

### **Cross-sectional area in XY dimension** — Cross-sectional area of cell in *XY* dimension `3.5e-4` `m^2` (default) | positive scalar

*Since R2024b*

Cross-sectional area of the cell in the *XY*
dimension. This parameter affects the heat exchange between the nodes of
the array of thermal nodes, **HDist**.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Height distributed thermal
mass`.

### **Cell height** — Height of cell `0.07` `m` (default) | positive scalar

*Since R2024b*

Height of the battery cell.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Height distributed thermal
mass`.

### **Reversible heat model** — Option to model reversible heat `Disabled` (default) | `Entropic coefficient`

Option to model the reversible heat or entropic heat in the battery.
Entropy change causes the reversible heat inside a battery. The
reversible heat can have a heating or cooling effect.

The block uses this equation to calculate the value of the reversible heat

Qrev=I TdOCVdT,

where dOCVdT is the value of the **Entropic
coefficient** parameter.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Lumped thermal mass` or
`Height distributed thermal
mass`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ReversibleHeatModel` |
| **Values:** | `"simscape.battery.enum.cells.ReversibleHeatModel.Disabled"` (default) | `"simscape.battery.enum.cells.ReversibleHeatModel.EntropicCoefficient"` |

### **Entropic coefficient** — Entropic coefficient of reversible heat `[0, 0, 0, 0, 0, 0, 0]` `mV/K` (default) | vector of scalars

Entropic coefficient of the reversible heat model. The size of this
vector must be equal to the size of the **State of charge
breakpoints, SOC** parameter.

#### Dependencies

To enable this parameter, set **Reversible heat
model** to `Entropic
coefficient`.

### Faults

### **Additional resistance fault** — Option to fault series-connected resistance `Add fault` (default)

Option to fault a series-connected resistance. Use this fault to model
an open-circuit cell if the additional resistance is greater than 1000
ohm, or an abnormal internal resistance.

To add a fault, click the **Add fault**
hyperlink.

### **Exothermic reactions fault** — Option to model self-heating and thermal runaway events `Add fault` (default)

Option to model exothermic reactions that can cause a thermal runaway
event.

When exothermic reactions happen in the cell, a thermal runaway event
can occur, releasing large amounts of heat and destroying the battery.
The battery electrically acts as an open circuit when the temperature of
the cell exceeds the value of the **Current interruption
temperature** parameter.

To add a fault, click the **Add fault**
hyperlink.

#### Dependencies

To enable this parameter, set **Thermal model**
to `Lumped thermal mass`.

### **Internal short fault** — Option to fault parallel-connected resistance `Add fault` (default)

Option to fault a parallel-connected resistance. The
parallel-connected resistance ranges from an infinite value to a value
that you specify.

To add a fault, click the **Add fault**
hyperlink.

### **Additional resistance when faulted** — Additional resistance when block is faulted `1e5` `Ohm` (default)

Value of the additional resistance when the block is in a faulted
state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Additional resistance fault**
parameter.

### **Trigger type** — Type of fault trigger for additional resistance fault `Always On` (default) | `Timed` | `Additional triggers` | `Conditional` | `Manual`

Trigger type. Choose one of these options:

- `Always On` — The fault injects at the start of simulation.
- `Timed` — The fault injects when the simulation time reaches the value you specify for the **Trigger fault at time** parameter.
- `Additional triggers` — The fault injects as result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To model
    irreversible faults, select the **Trigger stays on once
    activated** parameter in the Property Inspector. The block
    enters the faulted state when the trigger condition becomes true for the
    first time and remains in the faulted state for the rest of the
    simulation. To model reversible faults, clear the **Trigger
    stays on once activated** parameter. The block enters the
    faulted state when the trigger condition is true and enters the
    unfaulted state when the trigger condition is false. To learn more, see
    Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Additional resistance fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state for additional resistance fault `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Additional resistance fault**
parameter and set **Trigger type** to
`Timed`.

### **Trigger Configuration** — Option to enable additional trigger types for additional resistance fault `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Additional resistance fault**
parameter and set **Trigger type** to
`Additional triggers`.

### **Short parallel resistance when faulted** — Short parallel resistance when block is faulted `1e-6` (default)

Value of the short parallel resistance when the block is in a faulted
state.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Internal short fault**
parameter.

### **Trigger type** — Type of fault trigger for internal short fault `Always On` (default) | `Timed` | `Additional triggers` | `Conditional` | `Manual`

Trigger type. Choose one of these options:

- `Always On` — The fault injects at the start of simulation.
- `Timed` — The fault injects when the simulation time reaches the value you specify for the **Trigger fault at time** parameter.
- `Additional triggers` — The fault injects as result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To learn
    more, see Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Internal short fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state for internal short fault `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Internal short fault**
parameter and set **Trigger type** to
`Timed`.

### **Trigger Configuration** — Option to enable additional trigger types for internal short fault `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Internal short fault**
parameter and set **Trigger type** to
`Additional triggers`.

### **Modeling fidelity** — Fidelity option for modeling exothermic reactions `Analytical` (default) | `Tabulated accelerated rate calorimetry test temperature rate`

Fidelity option for modeling the exothermic reactions.

#### Dependencies

To enable this parameter, set the **Thermal model** parameter to
`Lumped thermal mass` and click the
**Add fault** hyperlink for the
**Exothermic reactions fault**
parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ExothermModel` |
| **Values:** | `"simscape.battery.enum.cells.ExothermModel.analytical"` (default) | `"simscape.battery.enum.cells.ExothermModel.acceleratedRateCalorimetryTemperature"` |

### **Tabulate with state of charge** — Option to tabulate exothermic reactions parameters as functions of SOC `off` (default) | `on`

Option to tabulate the exothermic reactions parameters as functions of
the battery SOC.

#### Dependencies

To enable this parameter, set the **Thermal
model** parameter to `Lumped thermal
mass` and click the **Add fault**
hyperlink for the **Exothermic reactions fault**
parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TabulateWithSOC` |
| **Values:** | `false` (default) | `true` |

### **Current interruption temperature** — Temperature over which current stops flowing `420` `K` (default) | positive scalar

Temperature over which the battery is electrically disconnected due to
thermal runaway and the current stops flowing through the
battery.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Clear the **Tabulate with state of
  charge** parameter.

### **Total heat of reaction** — Total heat of reaction `23e3` `J` (default) | positive scalar

Total heat of the reaction.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Clear the **Tabulate with state of
  charge** parameter.

### **Exotherm onset temperature** — Exotherm onset temperature `350` `K` (default) | positive scalar

Temperature in an accelerating rate calorimetry (ARC) test at which
the self-heating rate exceeds the threshold of 0.02 celsius per minute
at which the reaction heat rate slowly increases the cell temperature.
If the temperature exceeds this value, the reaction become
self-sustaining and eventually produces a thermal runaway.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Analytical`.
- Clear the **Tabulate with state of
  charge** parameter.

### **Exotherm onset temperature rate** — Exothermic onset temperature rate `0.02` `K/min` (default) | positive scalar

Exothermic onset temperature rate.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Analytical`.

### **Activation energy** — Activation energy `160e3` `J/mol` (default) | positive scalar

Activation energy.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Analytical`.
- Clear the **Tabulate with state of
  charge** parameter.

### **Order of reaction** — Order of exothermic reaction `1` (default) | positive scalar

Order of the exothermic reaction.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Analytical`.
- Clear the **Tabulate with state of
  charge** parameter.

### **Percent of thermal mass vented** — Percentage of thermal mass battery vents to environment `40` (default) | positive scalar

Percentage of thermal mass that the battery vents to the environment.
As the reaction advances, part of the material in the battery decomposes
into gases. The battery vents these gases to the environment. The loss
of these materials decreases the thermal mass of the battery. To model
this loss of thermal mass, the thermal mass decreases linearly with the
reaction extent. To control the rate of decrease of thermal mass with
reaction extent, specify the **Percent of thermal mass
vented** parameter accordingly.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Clear the **Tabulate with state of
  charge** parameter.

### **Vector of state of charge values for exothermic parameters, SOC** — SOC values for lookup data of exothermic parameters `[0,.5,1]` (default) | vector of nonnegative values

SOC values at which you specify lookup data for the exothermic
parameters.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Select the **Tabulate with state of
  charge** parameter.

### **Corresponding current interruption temperature, Tci(SOC)** — Corresponding current interruption temperature at specified SOC breakpoints `[420, 420, 420]` (default) | vector of nonnegative values

Corresponding current interruption temperature at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Select the **Tabulate with state of
  charge** parameter.

### **Corresponding total heat of reaction, heat(SOC)** — Corresponding total heat of reaction at specified SOC breakpoints `[23000, 23000, 23000]` (default) | vector of nonnegative values

Corresponding total heat of reaction at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Select the **Tabulate with state of
  charge** parameter.

### **Corresponding exotherm onset temperature, Tex(SOC)** — Corresponding exothermic onset temperature at specified SOC breakpoints `[350, 350, 350]` (default) | vector of nonnegative values

Corresponding exothermic onset temperature at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Analytical`.
- Select the **Tabulate with state of
  charge** parameter.

### **Corresponding activation energy, Ea(SOC)** — Corresponding activation energy at specified SOC breakpoints `[160000, 160000, 160000]` (default) | vector of nonnegative values

Corresponding activation energy at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Analytical`.
- Select the **Tabulate with state of
  charge** parameter.

### **Corresponding order of reaction, Or(SOC)** — Corresponding order of reaction at specified SOC breakpoints `[1, 1, 1]` (default) | vector of nonnegative values

Corresponding order of the reaction at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Analytical`.
- Select the **Tabulate with state of
  charge** parameter.

### **Vector of ARC test temperatures, T** — ARC test temperatures for lookup data `[323, 373, 423, 438, 463, 483, 513, 543, 545, 547, 549, 551, 553, 573, 623, 773, 923, 943, 1003, 1063, 1113, 1123, 1133, 1153, 1173]` (default) | vector of nonnegative values

ARC test temperatures at which you specify lookup data.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Tabulated accelerated rate calorimetry
  test temperature rate`.

### **Corresponding ARC test temperature rates, dT/dt(T)** — Corresponding ARC test temperature rates at specified T breakpoints `[.0001, .001, .025, .2, .4, .6, 1.1, 1.3, 1.9, 3, 5, 11.6, 183.3, 191.6, 200, 208.3, 200, 175, 8.33, 1.33, .33, .2, .13, .0017, .00017]` (default) | vector of nonnegative values

Corresponding ARC test temperature rates at the specified temperature
breakpoints.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Tabulated accelerated rate calorimetry
  test temperature rate`.
- Clear the **Tabulate with state of
  charge** parameter.

### **Corresponding ARC test temperature rates, dT/dt(T,SOC)** — Corresponding ARC test temperature rates at specified temperature and SOC breakpoints `repmat([.0001, .001, .025, .2, .4, .6, 1.1, 1.3, 1.9, 3, 5, 11.6, 183.3, 191.6, 200, 208.3, 200, 175, 8.33, 1.33, .33, .2, .13, .0017, .00017]', 1, 3)` (default) | matrix of nonnegative values

Corresponding ARC test temperature rates at the specified temperature
and SOC breakpoints.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Modeling fidelity** to
  `Tabulated accelerated rate calorimetry
  test temperature rate`.
- Select the **Tabulate with state of
  charge** parameter.

### **Corresponding percent of thermal mass vented, Mvent(SOC)** — Corresponding vented thermal mass percentage at specified SOC breakpoints `[40, 40, 40]` (default) | vector of values in the range [0, 100]

Corresponding vented thermal mass percentage at the specified SOC
breakpoints.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Select the **Tabulate with state of
  charge** parameter.

### **Trigger type** — Type of fault trigger for exothermic reactions fault `Always On` (default) | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

Trigger type. Choose one of these options:

- `Always On` — The fault injects at the start of simulation.
- `Timed` — The fault injects when the simulation time reaches the value you specify for the **Trigger fault at time** parameter.
- `Behavioral` — The fault injects as a result of fault parameter values during simulation. Setting **Trigger type** to `Behavioral` enables block parameters that define the failure conditions.
- `Additional triggers` — The fault injects as result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To learn
    more, see Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, set the **Thermal
model** parameter to `Lumped thermal
mass` and click the **Add fault**
hyperlink for the **Exothermic reactions fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state for exothermic reactions fault `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Trigger type** to
  `Timed`.

### **Trigger temperature** — Temperature to trigger fault `350` `K` (default) | nonnegative scalar

Trigger temperature. The block enters the faulted state if the
temperature exceeds this value.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Trigger Configuration** — Option to enable additional trigger types for exothermic reactions fault `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter:

- Set the **Thermal model** parameter
  to `Lumped thermal
  mass`.
- Click the **Add fault** hyperlink for
  the **Exothermic reactions fault**
  parameter.
- Set **Trigger type** to
  `Additional
  triggers`.
## Libraries

Simscape / Battery / Cells

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

### R2025a: Generate Digital Datasheet

You can now generate a digital datasheet for the Battery Equivalent
Circuit block, including charging, discharging, cycle life, and
shelf life characteristics, using a MATLAB live script. The script imports the parameters from the
Battery Equivalent Circuit block you select in
the model.

### R2025a: Parameterize overpotential parameters with respect to SOC, temperature, and current

You can now parameterize the overpotential parameters of the Battery
Equivalent Circuit block with 2-D lookup tables depending on SOC
and current or 3-D lookup tables depending on SOC, temperature, and current. You can
continue to parameterize the existing dependencies on SOC, temperature, and current
directionality.

To enable the current dependency of the overpotential parameters, set the new
**Current dependence for resistance parameters** parameter to
`Lookup tables (current dependent)`.

As a result of this change, the **Current directionality for resistance
parameters** parameter has been replaced with the **Current
dependence for resistance parameters** parameter. For more information
about the compatibility considerations of this change, see Battery Equivalent Circuit block supports current dependency for overpotential parameters.

### R2025a: Support calculation of number of discharge cycles with nominal capacity

The Battery Equivalent Circuit block now supports
the calculation of the number of discharge cycles for cycling aging by using the
nominal capacity. Set the **Cycle calculation method** parameter to:

- `Equivalent cycles` — The block uses the aged
  capacity to calculate the number of discharge cycles.
- `Equivalent full cycles` — The block uses the
  nominal capacity to calculate the number of discharge cycles.

### R2025a: Model cycling aging data with respect to the number of discharge cycles, temperature, and current

You can now model the cycling aging data for the Battery Equivalent
Circuit block with respect to the number of discharge cycles,
temperature, and current by specifying these parameters:

- **Current breakpoints for cycling aging data,
  I**
- **Percentage change in terminal resistance,
  R0Change(N,T,I)**
- **Initial target for percentage change in internal resistance
  due to cycling aging**
- **Percentage change in cell capacity,
  CapacityChange(N,T,I)**
- **Initial target for percentage change in capacity due to
  cycling aging**
- **Percentage change in self-discharge resistance,
  SelfDischargeRChange(N,T,I)**
- **Initial target for percentage change in self-discharge
  resistance due to cycling aging**
- **Percentage change in first polarization resistance,
  R1Change(N,T,I)**
- **Initial target for percentage change in first polarization
  resistance due to cycling aging**
- **Percentage change in second polarization resistance,
  R2Change(N,T,I)**
- **Initial target for percentage change in second polarization
  resistance due to cycling aging**
- **Percentage change in third polarization resistance,
  R3Change(N,T,I)**
- **Initial target for percentage change in third polarization
  resistance due to cycling aging**

As a result of this change:

- The `Lookup tables (temperature dependent)`
  value of the **Cycling aging model** parameter has been
  renamed to `Lookup tables (constant temperature
  dependent)`. This option is valid only if you simulate
  the battery with a constant temperature value.
- The **Cycling aging model** parameter now comprises
  two more values:

  - `Lookup tables (temperature
    dependent)` — Set tabulated data for the
    percentage change in parameters as a function of
    *N* and variable temperature. This
    tabulated data must be strictly monotonically increasing or
    decreasing with respect to the number of discharge
    cycles.
  - `Lookup tables (temperature and current
    dependent)` — Set tabulated data for the
    percentage change in parameters as a function of
    *N*, variable temperature, and variable
    current. This tabulated data must be strictly monotonically
    increasing or decreasing with respect to the number of
    discharge cycles.

### R2024b: Additional built-in parameterizations

The block now supports these additional built-in parameterizations that represent
components from specific suppliers:

- CSB Battery/EVX12300
- CSB Battery/EVX12340
- CSB Battery/EVX12520
- CSB Battery/GP12340
- CSB Battery/GP1245
- CSB Battery/GPL12260
- CSB Battery/GPL12520
- CSB Battery/GPL1272
- Exide/EP10012
- Exide/EP1212
- Exide/EP16012
- Exide/EP1712
- Exide/EP3212
- Exide/EP6512
- Exide/EP912
- Panasonic/BK\_10V1S
- Panasonic/BK\_110AAO
- Panasonic/BK\_130AA
- Panasonic/BK\_200A
- Panasonic/BK\_200AAB
- Panasonic/BK\_210A
- Panasonic/BK\_250A
- Panasonic/BK\_260SCP
- Panasonic/BK\_300SCP
- Panasonic/BK\_310CH
- Panasonic/BK\_380A
- Panasonic/BK\_450A
- Panasonic/BK\_60AAAH
- Panasonic/BK\_65AAAK
- Panasonic/BK\_70AAAJ
- Panasonic/BK\_70AAH
- Panasonic/BK\_80AAAB

### R2024b: Discretize thermal model into multiple elements along the cell height

To increase the fidelity of the thermal modeling, you can now discretize the
thermal model of the block along the cell height. To discretize the thermal model
along the cell height, set the **Thermal model** parameter to
`Height distributed thermal mass`. The block then
exposes the **HDist** thermal port, which is an array of thermal
nodes that represents the nodes along the height of the cell.

## Description

Battery model with electro-thermal dynamics and optional faults

The Battery Equivalent Circuit block models the electro-thermal dynamics of a battery by
using electrical circuit elements with variable characteristics and a zero-dimensional
lumped-mass thermal heat equation. You can also use this block to simulate the faulted
dynamics of a battery in shorted, open-circuit, and thermal runaway conditions. To model
cycling aging and calendar aging of the battery, you can use lookup tables or empirical
relationships. The block tabulates the variable characteristics of the electrical
circuit elements as functions of the battery state of charge (SOC) and, optionally,
current directionality, current, and temperature. This block comprises these constituent
model files:

- Electrical model

  - Open-circuit voltage and hysteresis model
  - Instantaneous overpotential model
  - Dynamic overpotential model
- Thermal model

  - Constant temperature
  - Lumped thermal mass model
- Cycling aging model

  - Equations
  - Temperature-independent table lookup
  - Temperature-dependent table lookup
- Calendar aging model

  - Resistance aging model
  - Capacity aging model
- Faults model

  - Short model
  - Open-circuit model
  - Exothermic reactions model

### Electrical Model

The Battery Equivalent Circuit block models the battery terminal voltage by using
a combination of electrical circuit elements arranged in a specific circuit
topology. This figure shows the equivalent circuit topology, which relies on
variable resistances, variable capacitances, and a variable voltage source. However,
the implementation of the Battery Equivalent Circuit block is completely in the
Simscape language.

All the circuit elements have variable characteristics that are functions of other
battery states:

- **OpenCircuitVoltage** — The block tabulates this
  circuit element as a function of the SOC.

  - If you set the **Thermal model**
    parameter to `Constant
    temperature`, `Lumped thermal
    mass`, or `Height distributed
    thermal mass`, this circuit element also
    depends on the 2-D lookup temperature.
  - If you set the **Hysteresis model**
    parameter to `One-state model`,
    then the voltage source value is a function of the previous
    charge or discharge history of the battery.
- **R0, R1, R2, R3, Tau1, Tau2, Tau3** — The block
  tabulates this circuit element as a function of the SOC.

  - If you set the **Thermal model**
    parameter to `Constant
    temperature`, `Lumped thermal
    mass`, or `Height distributed
    thermal mass`, this circuit element also
    depends on the 2-D lookup temperature.
  - If you set the **Current dependence for resistance
    parameters** parameter to `Lookup
    tables (current directionality dependent)`,
    then the resistance and capacitance values are also
    functions of the instantaneous current charge or discharge
    direction. Therefore, you can use charge and discharge
    parameter tables if they are available. If the current
    flowing through the battery is positive, then the block uses
    the charge lookup table parameters. If the current flowing
    through the battery is negative, then the block uses the
    discharge lookup table parameters.
  - If you set the
    **Current dependence for resistance
    parameters** parameter to `Lookup
    tables (current dependent)`, then the
    resistance and capacitance values are also functions of the
    current. Therefore, you can use current parameter tables if
    they are available. *(since R2025a)*
- **SelfDischargeResistor** — If you set the
  **Thermal model** parameter to
  `Constant temperature`, `Lumped
  thermal mass`, or `Height distributed
  thermal mass`, this circuit element also depends on the
  2-D lookup temperature.

**Note**

For all the table-based parameters, the Battery Equivalent
Circuit block supports linear interpolation only. For
extrapolation, set the **Extrapolation method for all tables**
parameter to `Nearest`,
`Linear`, or `Error`.

For rows and columns, the extrapolation follows the row-column convention, in
which rows are indexed before columns.

**Terminal Voltage**

The Battery Equivalent Circuit calculates the terminal voltage of the battery
at every time step by solving the Kirchhoff's voltage law

U = OCVhyst + ηinst + ηdyn,

where:

- *U* is the battery terminal voltage.
- OCVhyst = OCV(SOC,T)+Uhyst(SOC,T) is the hysteresis-adjusted open-circuit voltage.
  The software updates the battery state of charge
  *SOC*, the temperature *T*,
  and the corresponding variables that depend on them at every time
  step during the simulation.

  - *OCV(SOC,T)* is the open-circuit
    voltage.
  - *U*hyst*(SOC,T)*
    is the hysteresis voltage.
- ηinst=​ I R0(SOC,T,CurDir) is the instantaneous overpotential. The software
  updates the battery SOC, the temperature, and the current
  directionality *CurDir*, as well as the
  corresponding variables that depend on them, at every time step
  during the simulation.

  - *I* is the battery current. If the
    value of *I* is positive, the block
    uses the charge lookup table parameters. If the value of
    *I* is negative, the block uses the
    discharge lookup table parameters.
- ηdyn = ∑i=13ΔURCi(SOC,T,CurDir) is the dynamic overpotential. This optional term
  depends on the number of parallel resistor-capacitor pairs. This
  number can vary between 1 and 3. The software updates the battery
  SOC, temperature, and current directionality, as well as the
  corresponding variables that depend on them, at every time step
  during the simulation.

  - *ΔU*RC*i*
    is the voltage drop for parallel resistor-capacitor pair
    *i*. The block calculates the voltage
    drop using this ordinary differential equation:

    (τi(SOC,T,CurDir)d ΔURCidt+ΔURCi)1Ri(SOC,T,CurDir)=I

For the Battery Equivalent Circuit block, *I* has a negative
sign during discharge and a positive sign during charge. During discharge, the
block subtracts the battery overpotentials from the open-circuit voltage value,
lowering the terminal voltage of the battery. In the discharge and charge cases,
the overpotentials dissipate energy as heat. This figure shows the evolution of
the battery overpotentials during a battery pulse discharge. The dynamic
overpotential from the resistor-capacitor pairs increases slowly over the pulse,
as opposed to the instantaneous overpotential, which increases during the first
few milliseconds.

**Dynamic Overpotential**

Batteries do not respond instantaneously to load changes. They require some
time to achieve a steady state. This time-varying property is a result of the
battery charge dynamics. The block models the charge dynamics by using parallel
RC sections in the equivalent circuit.

To model the battery charge dynamics, set the **Parallel resistor
capacitor pairs** parameter to one of these values:

- `No dynamics` — The equivalent circuit
  contains no parallel RC sections. The battery exhibits no delay
  between terminal voltage and internal charging voltage.
- `One time-constant dynamics` — The
  equivalent circuit contains one parallel RC section.
- `Two time-constant dynamics` — The
  equivalent circuit contains two parallel RC sections.
- `Three time-constant dynamics` — The
  equivalent circuit contains three parallel RC sections.

This diagram shows the battery equivalent circuit for the block
circuit topology with only two time-constant dynamics and no self-discharge resistance.

In this figure:

- *R*1 and
  *R*2 are the parallel RC
  resistances. Specify these values by setting the **First
  polarization resistance, R1(SOC,T)** and
  **Second polarization resistance, R2(SOC,T)**
  parameters, respectively, if you tabulate parameters over
  temperature. Otherwise, specify these values by setting the
  **First polarization resistance, R1(SOC)** and
  **Second polarization resistance, R2(SOC)**
  parameters, respectively. The voltage drop of the first RC pair is
  directly related to the activation overpotential from the chemical
  reaction at the interface of the electrodes. The time constant
  *τ*1 for this dynamic is
  typically lower than *τ*2,
  which indicates a faster response or faster dynamics. The voltage
  drop of the second RC pair is related to concentration
  overpotentials and typically evolves more slowly than the activation
  overpotential.
- *C*1 and
  *C*2 are the parallel RC
  capacitances. The time constant *τ* for each
  parallel section relates the *R* and
  *C* values through the relationship C=τ/R. Specify *τ* for each section by
  using the **First time constant, tau1(SOC,T)** and
  **Second time constant, tau2(SOC,T)**
  parameters if you tabulate parameters over temperature or
  **First time constant, tau1(SOC)** and
  **Second time constant, tau2(SOC)**
  otherwise.
- *R*0 is the instantaneous
  resistance. Specify this value with the **Instantaneous
  resistance, R0(SOC,T)** parameter if you tabulate
  parameters over temperature or **Instantaneous resistance,
  R0(SOC)** otherwise.

**Note**

The charge dynamics parameters can also depend on the current
directionality and on the current. If you set the **Current
dependence for resistance parameters** to `Lookup
tables (current directionality dependent` or
`Lookup tables (current dependent)`, the
parameters in the **Overpotential** section change
accordingly.

**State of Charge**

The Battery Equivalent Circuit block calculates the SOC of the battery with
the Coulomb counting method:

SOC=1Cageddchargedt,

where:

- *C*aged is the aged
  capacity of the cell.
- dchargedt=I−ID,SD(T)

  - *I*D,SD is the
    self-discharge current drain. This equation gives the
    current drain from the self-discharge resistor, which you
    can tabulate as a function of temperature
    *T*:

    ID,SD(T)=1RSD(T)OCVinternal.
  - *R*SD*(T)*
    is the self-discharge resistance.
  - *OCV*internal is
    the internal open-circuit voltage.

**Heat Generation Rate**

The Battery Equivalent Circuit block calculates the battery heat generation
rate by adding these quantities:

- Power dissipation terms from all the resistors in the equivalent
  circuit topology. This term is also called the irreversible heat
  generation. This quantity contains ohmic and activation
  overpotential heat terms.
- Reversible heat generation from entropy
- Heat generation terms from the faulted cell behaviour:

  - Short resistance (or parallel-added resistance)
  - Open-circuit resistance (or series-added
    resistance)
  - Thermal runaway reaction heat

This equation shows this summation:

Q˙gen=Pdiss+Q˙rev+Qflow,exr,

where:

- Q˙gen is the heat generation rate.
- Pdiss=I2 R0(SOC,T,CurDir)+(∑i=13ΔURCi(SOC,T,CurDir))I+OCVinternal2RSD(T) +Qflow,series+Qflow,parallel is the dissipated power.

  - *Q*flow,series is
    the series resistor heat flow.
  - *Q*flow,parallel
    is the parallel resistor heat flow.
- Q˙rev=I T dOCVdt(SOC) is the reversible heat.
- *Q*flow,exr is the
  exothermic reaction heat flow. For more information, see Model Faults.

**Hysteresis**

The hysteresis of a battery describes the dependency of the open-circuit
voltage (OCV) on the charge or discharge history. Hysteresis is only indirectly
dependent on the OCV.

The data obtained from measuring the OCV during a complete charging or
discharging cycle is called a *major loop*. If the battery
is only partially charged or discharged, the measured OCV forms a
*minor loop*. The minor loops approach the major loops
after a delay in charge. This effect is prominent in Li-ion batteries and it has
a significant effect on the SOC estimation.

The Battery Equivalent Circuit block models the
hysteresis by using a one-state model

Uhyst=M H+sgn(I)M0

where:

- *U*hyst is the hysteresis
  voltage.
- *H* defines the hysteresis state. The block uses
  this ordinary differential equation to calculate the hysteresis state:

  dHdt=γCaged[I−|I| H]
- *γ* is the hysteresis rate.
- *C*aged is the aged
  capacity of the cell.
- *M* is the value of the **Maximum dynamic
  hysteresis voltage,
  MaximumHysteresisVoltageThermal(SOC,T)** parameter if
  you tabulate the parameters over temperature, or **Maximum
  dynamic hysteresis voltage,
  MaximumHysteresisVoltage(SOC)** otherwise.
- *M*0 is the value of the
  **Instantaneous hysteresis voltage,
  InstantaneousHysteresisVoltageThermal(SOC,T)**
  parameter if you tabulate the parameters over temperature, or
  **Instantaneous hysteresis voltage,
  InstantaneousHysteresisVoltage(SOC)** otherwise.

For more information on hysteresis and on how to model it, see the Model Voltage Hysteresis in Battery example.

**Self-Discharge**

When the battery terminals are open-circuit, internal currents can still
discharge the battery. This behavior is called self-discharge. To enable and
model this effect, set the **Self discharge** parameter to
`Enabled`.

The block models these internal currents with a temperature-dependent
resistance *R*SD*(T)*
across the terminals of the fundamental battery model. Specify the lookup values
for this resistance by using the **Self-discharge resistance,
SelfDischargeR(T)** parameter if you tabulate the parameters over
temperature, or **Self-discharge resistance, SelfDischargeR**
otherwise.

### Thermal Model

Setting the **Thermal model** parameter to `Lumped
thermal mass` adds a thermal model to the Battery
Equivalent Circuit block. This model computes the battery
temperature at every time step. The block uses this temperature for all
temperature-dependent lookup tables. The lumped thermal mass adds this ordinary
differential equation:

Mthd Tdt=Q˙gen−Q˙diss,

where:

- *M*th is the battery thermal
  mass.
- Q˙gen=Pdiss+Q˙rev+Q˙flow,exr.
- Q˙dissis the heat across the **H** thermal
  port.

To increase the fidelity of the thermal
modeling and to model the thermal gradient inside the block, you can discretize the
thermal model along the cell height. To height-discretize the thermal model, set the
**Thermal model** parameter to `Height distributed
thermal mass`. The block then exposes the
**HDist** thermal port, which is an array of thermal nodes that
represents the nodes along the height of the cell. To compute the electrical
behavior of the cell, the block uses the mean of the discretized thermal
nodes. *(since R2024b)*

### Cycling Aging Model

Battery aging is the deterioration of the battery performance over repeated charge
and discharge cycles.

This block allows you to model the battery aging by setting the **Cycling
aging model** parameter to one of these options:

- `Disabled` — Do not model fading
  characteristic.
- `Equations` — The cell capacity and terminal
  resistance are proportional to N. The open-circuit voltage is proportional to
  *N*. If you enable the self-discharge resistance or
  any of the time constants, their values are proportional to N.
- `Lookup tables (temperature independent)` —
  Lookup table of the percent change of the underlying parameter, as a
  function of the number of discharge cycles, *N*.
- `Lookup tables (constant temperature
  dependent)` — Lookup table of percent change of the
  underlying parameter, as a function of the number of discharge cycles
  and the present battery temperature. Use this option only if your
  battery operates at a near-constant temperature. For batteries with
  varying temperatures, use `Lookup tables (temperature
  dependent)` or `Lookup tables (temperature
  and current dependent)`.
- `Lookup tables
  (temperature dependent)` — Lookup table of the percent
  change of the underlying parameter, as a function of the number of
  discharge cycles and the present battery temperature. Due to how the
  block internally calculates the value of the underlying parameter at the
  next timestep, this tabulated data must be strictly monotonically
  increasing or decreasing with respect to the number of discharge cycles.
  Use this option if your battery operates at variable temperatures. For
  batteries at near-constant temperatures, use `Lookup tables
  (constant temperature dependent)` to achieve better
  simulation performance. *(since R2025a)*
- `Lookup tables
  (temperature and current dependent)` — Lookup table of
  the percent change of the underlying parameter, as a function of the
  number of discharge cycles, the present battery temperature, and the
  present cell current. Due to how the block internally calculates the
  value of the underlying parameter at the next timestep, this tabulated
  data must be strictly monotonically increasing or decreasing with
  respect to the number of discharge cycles. Use this option if your
  battery operates at variable temperatures. *(since R2025a)*

When you set the **Cycling aging model** parameter to
`Equations`, the open-circuit voltage across the
fundamental battery model fades proportionally with the number of discharge cycles
*n*:

OCVfaded=OCV(1+δOCV(N,T)100nN),

where *δOCV(N,T)* is the percentage change in
open-circuit voltage after *N* discharge cycles. Specify
*δOCV(N,T)* by using the  **Change in open-circuit
voltage after NumDisCycles discharge cycles (%)** parameter.

**Note**

The Battery Equivalent Circuit block tracks the
current and integrates it over time. The number of discharge cycles
*n* depends on the value of the **Cycle calculation
method** parameter:

- `Equivalent cycles` — The block uses the
  aged capacity to calculate the number of discharge cycles.
- `Equivalent full cycles` — The block uses
  the value of the **Battery capacity** parameter to
  calculate the number of discharge cycles

The nominal charge, from which the block calculates the SOC, fades with the square
root of the number of discharge cycles:

Cfaded=C(1+δC(N,T)100nN),

where *C* is the initial capacity and
*δC(N,T)* is the percentage change in capacity after
*N* discharge cycles. Specify *δC(N,T)* by
using the  **Change in capacity after NumDisCycles discharge cycles
(%)** parameter.

All resistances in the battery model also fade with the square root of the number
of discharge cycles:

Ri,faded=Ri(1+δRi(N,T)100nN),

where *δRi(N,T)* is the
percentage change in the *i*th resistance after
*N* discharge cycles. Specify
*δRi(N,T)* by using the **Change in resistance after NumDisCycles discharge cycles (%)**
parameter.

Depending on how you configure the block, the resistances include these values:

- Instantaneous resistance — Specify the percentage change over
  *NumDisCycles* cycles using the **Change in
  instantaneous resistance after NumDisCycles discharge cycles
  (%)** parameter.
- Self-discharge resistance — Specify the percentage change over
  *NumDisCycles* cycles using the **Change in
  self-discharge resistance after NumDisCycles discharge cycles
  (%)** parameter.
- First charge dynamics resistance — Specify the percentage change over
  *NumDisCycles* cycles using the **Change in
  first polarization resistance after NumDisCycles discharge cycles
  (%)** parameter.
- Second charge dynamics resistance — Specify the percentage change over
  *NumDisCycles* cycles using the **Change in
  second polarization resistance after NumDisCycles discharge cycles
  (%)** parameter.
- Third charge dynamics resistance — Specify the percentage change over
  *NumDisCycles* cycles using the **Change in
  third polarization resistance after NumDisCycles discharge cycles
  (%)** parameter.

**Note**

You can also model the battery cycling aging characteristic by using the
temperature-dependent, temperature-independent, or
temperature-and-current-dependent lookup tables. Choosing one of these options
changes the block parameters accordingly.

### Calendar Aging Model

You can model the battery performance deterioration that occurs when the battery
is not in use. Calendar aging affects the internal resistance and the capacity. In
particular, the resistance increase varies by mechanisms such as the creation of a
solid-electrolyte interface (SEI) at the anode and cathode and the corrosion of the
current collector. These processes mainly depend on the storage temperature, the
storage SOC, and storage time.

To model calendar aging in the Battery Equivalent Circuit block,
set one of the **Resistance calendar aging** or **Capacity
calendar aging** parameters to `Enabled` and
then set the **Modeling option** parameter to one of these values:

- `Equation-based`
- `Tabulated: temperature`
- `Tabulated: time and temperature`

**Note**

The Battery Equivalent Circuit block applies the calendar aging
only during initialization. When you set the **Resistance calendar
aging** or **Capacity calendar aging** parameter
to `Enabled`, the block exposes the **Vector of
time intervals** parameter, which represents the time over which
the battery ages before the start of the simulation. This option does not
include calendar aging during the simulation.

**Equation-based**

These equations define the terminal resistance increase of the battery due to
calendar aging:

αR(T,Voc)=(bR Voc−cR)e−q dRk TRcalendar-aged=R0(1+∑i=1i=nαR(Ti,Voc)(tiaR−ti−1aR))

where:

- *V*oc is the
  **Normalized open-circuit voltage during storage,
  V/Vnom** parameter.
- *R*0 is the
  **Internal resistance** parameter.
- *ti* is the time sample
  derived from the **Vector of time intervals**
  parameter.
- *Ti* is derived from the
  **Temperature breakpoints, T**
  parameter.
- *b*R is the
  **Terminal resistance linear scaling for voltage,
  b** parameter.
- *c*R is the
  **Terminal resistance constant offset for voltage,
  c** parameter.
- *d*R is the
  **Terminal resistance temperature-dependent exponential
  increase, d** parameter.
- *a*R is the
  **Terminal resistance time exponent, a**
  parameter.
- *q* is the electron elementary charge, in
  C.
- *k* is the Boltzmann constant, in J/K.

These equations define the capacity decrease of the battery due to calendar aging:

αC(T,Voc)=(bC Voc−cC)e−q dCk TCcalendar-aged=C(1+∑i=1i=nαC(Ti,Voc)(tiaC−ti−1aC))

where:

- *C* is the initial capacity.
- *b*C is the
  **Capacity linear scaling for voltage, b**
  parameter.
- *c*C is the
  **Capacity constant offset for voltage, c**
  parameter.
- *d*C is the
  **Capacity temperature-dependent exponential increase,
  d** parameter.
- *a*C is the
  **Capacity time constant, a** parameter.

If you set the **Storage condition** parameter to
`Specify state-of-charge during storage`, the block
converts the SOC during storage into the normalized open-circuit voltage by
using the tabulated voltage **V0**
against the SOC and the temperature during storage.

**Tabulated: Temperature**

The aged terminal resistance is the product of the terminal resistance,
*R*0*(SOC,T)*, the
percentage resistance increase, *dR*0,
and the power law that describes the time dependence of the calendar aging:

R0(SOC,T;tst,Tst)=R0(SOC,T)(1+∑i=1ndR0(Tst,i)100(tast,i−tast,i−1tast,m)),

where:

- *T* is the battery temperature. Specify the
  *T* breakpoints using the **Temperature
  breakpoints, T** parameter if you tabulate the
  parameters over temperature.
- *T*st is the
  **Vector of storage temperatures**
  parameter.
- *t*st,*i*
  and
  *t*st,*i*-1
  are the time samples derived from the **Vector of time
  intervals** parameter.
- *t*0 is 0.
- *t*st,m is the moment at
  which the software measures the resistance increase,
  *dR*0.

The same equation applies to the calculation of the aged battery
capacity.

**Tabulated: Time and Temperature**

The aged terminal resistance is the product of the terminal resistance,
*R*0*(SOC,T)* and
*dR*0:

R0(SOC,T;Δtst,Tst)=R0(SOC,T)(1+∑i=1ndR0(Δtst,i,Tst,i)100).

The same equation applies to the calculation of the aged battery
capacity.

### Model Faults

To model a fault in the Battery Equivalent Circuit block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Battery Equivalent Circuit block supports three
different types of fault:

- Additional resistance fault — The resistance of a series-connected
  resistor ranges from a value of 0 ohm to a value that you specify. You
  can use this fault to model an open-circuit cell when the additional
  series-connected resistance is high (greater than 1000 ohm), or an
  abnormal internal resistance.
- Internal short fault — The resistance of a parallel-connected resistor
  ranges from an infinite value to a value that you specify.
- Exothermic reactions — Use this fault to simulate a thermal runaway
  event. Heat-releasing chemical reactions occur at the cell level. At low
  temperatures, the rate of reaction is low and the self-heating rate is
  not significant. At higher temperatures, the rate of exothermic
  reactions increases exponentially. The battery generates more heat than
  the amount it can dissipate. The temperature starts to rise
  exponentially, reaches a thermal runaway event, and the cell starts to
  burn. During the burn, the cell electrical behavior is equivalent to an
  open circuit.

  The released heat rate is a function of the extent of
  the reaction and the cell temperature:

  Qreaction(ξ,T)=Kscale(1−ξ)ρ e−EaRT,

  where:

  - *K*scale is a
    constant that scales the equation to define how fast the
    reaction advances.
  - *ξ* is the reaction extent. If the
    reaction extent is 0, the reaction has not started. If the
    reaction extent is 1, the reaction has consumed all possible
    reactants and is completed.
  - *ρ* is the value of the **Order
    of reaction** parameter and defines the
    polynomial dependency of the reaction rate with respect to
    the extent of reaction.
  - e−EaRT is the Arrhenius equation and defines the
    temperature dependency. *Ea* is the
    activation energy, in kJ/mol, and *R* is
    equal to 8.314 J/k/mol.

  The block computes *K*scale by
  using the **Exotherm onset temperature** parameter. The
  exotherm onset temperature is the temperature in an accelerating rate
  calorimetry (ARC) test at which the self-heating rate exceeds a
  threshold of 0.02 celsius per minute at which the reaction heat rate
  slowly increases the cell temperature. If the temperature exceeds this
  value, the reaction becomes self-sustaining and eventually produces the
  runaway event.

  In an ARC test, the released heat rate at the exothermic onset is
  equal to:

  Qreaction(ξ=0,  T=TEO)=Mth,cell dTdtEO=Kscale e−EaRTEO

  where:

  - *T*EO is the
    exothermic onset temperature in Kelvin.
  - *M*th,cell is the
    thermal mass of the cell.
  - *dTdt*EO is the
    rate of change of the cell temperature when the cell is at
    the exothermic onset temperature. The typical value is 0.02
    celsius per minute.

  You can then compute
  *K*scale as a function of
  *dTdt*EO,
  *T*EO, the thermal mass of
  the cell, and the activation energy:

  Kscale=Mth,cell∗dTdtEOe−EaRTEO.

  As the reaction advances, some of the materials in the battery
  decompose into gases. These gases dissipate into the environment. The
  loss of these materials decreases the thermal mass of the battery. To
  model this loss of thermal mass, the thermal mass decreases linearly
  with the reaction extent. To control the rate of thermal mass decrease
  with reaction extent, specify the **Percent of thermal mass
  vented** parameter accordingly.

**Fault Triggers**

You specify how and when faults occur by using the **Trigger
Type** parameter.

If you set the **Trigger Type** parameter to
`Timed`, the Battery Equivalent Circuit block triggers fault
events when the simulation time reaches the value you specify for the
**Trigger fault at time** parameter.

For the exothermic reactions fault, if you set the **Trigger
Type** to `Behavioral`, the Battery Equivalent Circuit
block triggers fault events when the temperature exceeds the value of the
**Trigger temperature** parameter.

If you set the **Trigger
Type** to `Conditional`, you can choose whether faults
in the Battery Equivalent Circuit block are reversible *(since R2025a)*. To model irreversible faults, click
**Open fault properties** to open the Property Inspector and select the
**Trigger stays on once activated** parameter. The block enters the faulted
state when the trigger condition becomes true for the first time and remains in the faulted
state for the rest of the simulation. To model reversible faults, clear the **Trigger
stays on once activated** parameter. The block enters the faulted state when the
trigger condition is true and enters the unfaulted state when the trigger condition is
false.

**Note**

Exothermic reactions fault and internal short fault do not support
reversible faults.

For more information about adding faults to blocks and
specifying fault triggers, see Introduction to Simscape Faults.

### Predefined Parameterization

You can parameterize the Battery Equivalent Circuit
block by using built-in parameterizations that represent components from specific
suppliers.

These parameterizations model the steady-state electrical parameters of a battery. The
software parameterizes the **Open-circuit voltage (SOC)**,
**Instantaneous resistance, R0(SOC, T)**, **Battery
capacity**, **Percentage change in cell capacity,
CapacityChange(N)**, and **Percentage change in open-circuit
voltage, OCVChangeVec(N)** parameters from characteristic curves in the
manufacturer datasheets. The software does not parameterize the change in series
resistance with the battery cycle life and the dynamic RC network parameters.
Instead, the software sums the net resistance of the RC network resistors to the
series resistance of the specific parameterized data. To populate the RC parameter
data, subtract the net RC network resistance from the series resistance data. The
software estimates the battery thermal mass by assuming a value of 900 J/kg K for
the specific heat of the battery. The thermal mass is then equal to 900 times the
weight of the battery in the manufacturer datasheet.

The available data corresponds to a 1 C discharge current for different
temperatures up to the minimum terminal voltage in the datasheet. The software
extrapolates the data below the minimum terminal voltage. The **Open-circuit voltage, OCV(SOC)** parameter is temperature-independent.
At lower temperatures, in the low-SOC region, the terminal resistances are constant
and equal to the value of the resistance at the minimum terminal voltage. In this
regime, batteries often experience higher thermal losses.

To load a predefined parameterization, double-click the Battery Equivalent Circuit
block, click the **<click to select>** hyperlink
of the **Selected part** parameter, and, in the Block
Parameterization Manager window, select the part you want to use from the list of
available components.

**Note**

The predefined parameterizations of Simscape™ components use available data sources for the parameter values. Engineering
judgment and simplifying assumptions are used to fill in for missing data. As a result,
expect deviations between simulated and actual physical behavior. To ensure accuracy,
validate the simulated behavior against experimental data and refine component models as
necessary.

For more information about predefined parameterization and for a list of the
available components, see List of Pre-Parameterized Components (Simscape Electrical).

### Generate Digital Data Sheet

*Since R2025a*

Generate a digital data sheet for the Battery Equivalent
Circuit block, including charging, discharging, cycle life,
shelf life, and hysteresis characteristics, using a MATLAB® live script. The script imports the parameters from the
Battery Equivalent Circuit block you select in
the model. To open the MATLAB live script:

1. Double-click the block to open the **Block
   Parameters** window.
2. Open the **Description** tab.
3. Click the `Generate datasheet` hyperlink.

To generate the data sheet, in the live script, click the `Generate
Datasheet` button.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

### Public Variables (Visible with Probe Block)

The Battery Equivalent Circuit block comprises
these public variables that you can probe using the Probe block:

- `batteryCurrent` — Total current measured through
  the battery terminals. By default, this variable has units of
  Amperes.
- `batteryTemperature` — Battery average temperature
  that the block uses for the table look-up of resistances and
  open-circuit voltage. If you set the **Thermal model**
  parameter to `Constant temperature`, then the
  `batteryTemperature` variable is equal to the
  specified temperature value. If you set the **Thermal
  model** parameter to `Lumped thermal
  mass`, then the `batteryTemperature`
  variable is a differential state that varies during the
  simulation.
- `batteryVoltage` — Battery terminal voltage, or the
  voltage difference between the positive and the negative terminals. By
  default, this variable has units of Volts.
- `capacityCyclingChange` — Percentage change of the
  battery capacity after the specified discharge cycles. By default, this
  variable is unitless.
- `charge` — Electrical charge drawn from or added to
  the battery. By default, this variable has units of A\*h.
- `heatGenerationRate` — Total battery heat
  generation rate. The block calculates the heat generation rate by adding
  up all resistive losses, reversible heating contribution, and the
  exothermic reaction heat if you enabled an exothermic fault. By default,
  this variable has units of Watts.
- `hysteresisState` — Hysteresis state in the range
  [-1,1]. A value of 1 indicates that the block is using the charge
  open-circuit voltage curve at that time step. A value of -1 indicates
  that the block is using the discharge open-circuit voltage curve at that
  time step. By default, this variable is unitless.
- `isCurrentInterruptionTempExceeded` — Boolean that
  indicates whether the battery has exceeded its current interruption
  temperature during a thermal runaway event. This variable is relevant
  only when modeling faults.
- `isExothermFaulted` — Boolean that indicates
  whether the battery model has transitioned into a thermal runaway or
  exothermic mode. This mode can be triggered by high temperature or timed
  based on the fault model specification. This variable is relevant only
  when modeling faults.
- `numCycles` — Equivalent number of discharge cycles
  of the battery. The counter starts at zero and increases by one every
  time an equivalent discharge charge has been drawn from the battery. By
  default, this variable is unitless.
- `ocv` — Open-circuit voltage of the battery
  adjusted for temperature, ageing, and state of charge. By default, this
  variable has units of Volts.
- `power_dissipated` — Resistive heat generation rate
  or dissipated power. By default, this variable has units of
  Watts.
- `r0CyclingChange` — Percentage change of the
  battery instantaneous resistance after the specified discharge cycles.
  By default, this variable is unitless.
- `r1CyclingChange` — Percentage change of the first
  polarization resistance of the battery after the specified discharge
  cycles. By default, this variable is unitless.
- `r2CyclingChange` — Percentage change of the second
  polarization resistance of the battery after the specified discharge
  cycles. By default, this variable is unitless.
- `r3CyclingChange` — Percentage change of the third
  polarization resistance of the battery after the specified discharge
  cycles. By default, this variable is unitless.
- `reactionExtent` — Exothermic reaction progression
  in the range [0,1]. Initially, the value of this variable is 0. This
  variable is relevant only when modeling faults.
- `reactionHeatRate` — Exothermic reaction heat, if
  you enabled an exothermic fault. By default, this variable has units of
  Watts.
- `reversibleHeat` — Reversible heating contribution
  from entropy changes. By default, this variable has units of
  Watts.
- `selfDischargeRCyclingChange` — Percentage change
  of the self-discharge resistance of the battery after the specified
  discharge cycles. By default, this variable is unitless.
- `stateOfCharge` — Battery state of charge obtained
  from coulomb counting. By default, this variable is unitless.
- `voltageDropRC1` — Voltage drop that the first RC
  branch of the equivalent circuit model causes. By default, this variable
  has units of Volts.
- `voltageDropRC2` — Voltage drop that the second RC
  branch of the equivalent circuit model causes. By default, this variable
  has units of Volts.
- `voltageDropRC3` — Voltage drop that the third RC
  branch of the equivalent circuit model causes. By default, this variable
  has units of Volts.
