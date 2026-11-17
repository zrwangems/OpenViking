---
type: simulink-block
title: 'Bidirectional DC-DC Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'bidirectionaldcdcconverter'
documentation_source_path: 'ref/bidirectionaldcdcconverter.html'
language: en
---

# Bidirectional DC-DC Converter

## Ports
```yaml
ports:
- name: G
  summary: Switching device gate control electrical | vector
  direction: conserving
  data_types: double
- name: 1+
  summary: Positive DC voltage 1 electrical | scalar
  direction: conserving
  data_types: double
- name: 1-
  summary: Negative DC voltage 1 electrical | scalar
  direction: conserving
  data_types: double
- name: 2+
  summary: Positive DC voltage 2 electrical | scalar
  direction: conserving
  data_types: double
- name: 2-
  summary: Negative DC voltage 2 electrical | scalar
  direction: conserving
  data_types: double
```

### Conserving

### **G** — Switching device gate control electrical | vector

Electrical conserving port associated with the gate terminals of the
switching devices.

**Data Types:** `double`

### **1+** — Positive DC voltage 1 electrical | scalar

Electrical conserving port associated with the positive terminal of
the first DC voltage.

**Data Types:** `double`

### **1-** — Negative DC voltage 1 electrical | scalar

Electrical conserving port associated with the negative terminal of
the first DC voltage.

**Data Types:** `double`

### **2+** — Positive DC voltage 2 electrical | scalar

Electrical conserving port associated with the positive terminal of
the second DC voltage.

**Data Types:** `double`

### **2-** — Negative DC voltage 2 electrical | scalar

Electrical conserving port associated with the negative terminal of
the second DC voltage.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Converter model Nonisolated converter (default) | Isolated converter | Dual Active Bridge converter
  group: ''
- name: Fidelity level
  summary: Fidelity level Detailed model - switching devices (default) | Equivalent model - PWM-controlled
  group: Main
- name: Switching device
  summary: Switch type Ideal Semiconductor Switch (default) | GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: Switching Devices
- name: Forward voltage
  summary: Voltage 0.8 V (default) | scalar
  group: Switching Devices
- name: On-state resistance
  summary: Resistance 0.001 Ohm (default) | scalar
  group: Switching Devices
- name: Drain-source on resistance
  summary: Resistance 0.001 Ohm (default) | scalar
  group: Switching Devices
- name: Off-state conductance
  summary: Conductance 1e-5 1/Ohm (default) | scalar
  group: Switching Devices
- name: Threshold voltage
  summary: Voltage threshold 6 V (default) | scalar
  group: Switching Devices
- name: Gate trigger voltage, Vgt
  summary: Voltage threshold 1 V (default) | scalar
  group: Switching Devices
- name: Gate turn-off voltage, Vgt_off
  summary: Voltage threshold -1 V (default) | scalar
  group: Switching Devices
- name: Holding current
  summary: Current threshold 1 A (default) | scalar
  group: Switching Devices
- name: Switching device HV
  summary: Switch Ideal Semiconductor Switch (default) | GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: Switching Devices
- name: Forward voltage HV
  summary: Voltage 0.8 Ohm (default) | scalar
  group: Switching Devices
- name: Drain-source on resistance HV
  summary: Resistance 0.001 Ohm (default) | scalar
  group: Switching Devices
- name: On-state resistance HV
  summary: Resistance 0.001 Ohm (default) | scalar
  group: Switching Devices
- name: Off-state conductance HV
  summary: Conductance 1e-5 1/Ohm (default) | scalar
  group: Switching Devices
- name: Threshold voltage HV
  summary: Voltage threshold 6 V (default) | scalar
  group: Switching Devices
- name: Gate trigger voltage HV, Vgt_hv
  summary: Voltage threshold 1 V (default) | scalar
  group: Switching Devices
- name: Gate turn-off voltage HV, Vgt_off_hv
  summary: Voltage threshold -1 V (default) | scalar
  group: Switching Devices
- name: Holding current HV
  summary: Current threshold 1 A (default) | scalar
  group: Switching Devices
- name: Switching device LV
  summary: Switch Ideal Semiconductor Switch (default) | GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: Switching Devices
- name: Forward voltage LV
  summary: Voltage 0.8 Ohm (default) | scalar
  group: Switching Devices
- name: Drain-source on resistance LV
  summary: Resistance 0.001 Ohm (default) | scalar
  group: Switching Devices
- name: On-state resistance LV
  summary: Resistance 0.001 Ohm (default) | scalar
  group: Switching Devices
- name: Off-state conductance LV
  summary: Conductance 1e-5 1/Ohm (default) | scalar
  group: Switching Devices
- name: Threshold voltage LV
  summary: Voltage threshold 6 V (default) | scalar
  group: Switching Devices
- name: Gate trigger voltage LV, Vgt_lv
  summary: Voltage threshold 1 V (default) | scalar
  group: Switching Devices
- name: Gate turn-off voltage LV, Vgt_off_lv
  summary: Voltage threshold -1 V (default) | scalar
  group: Switching Devices
- name: Holding current LV
  summary: Current threshold 1 A (default) | scalar
  group: Switching Devices
- name: Integer for piecewise constant approximation of gate input (0 for disabled)
  summary: Integer mode for FPGA deployment 0 (default) | nonnegative scalar
  group: Switching Devices
- name: Model dynamics
  summary: Diode model Diode with no dynamics (default) | Diode with charge dynamics
  group: Protection Diode
- name: Forward voltage
  summary: Voltage 0.8 V (default) | scalar
  group: Protection Diode
- name: On resistance
  summary: On resistance 0.001 Ohm (default) | scalar
  group: Protection Diode
- name: Off conductance
  summary: Conductance 1e-5 1/Ohm (default) | scalar
  group: Protection Diode
- name: Junction capacitance
  summary: Junction capacitance 50 nF (default) | scalar
  group: Protection Diode
- name: Peak reverse current, iRM
  summary: Peak reverse current -235 A (default) | negative scalar
  group: Protection Diode
- name: Initial forward current when measuring iRM
  summary: Initial forward current when measuring iRM 300 A (default) | positive scalar
  group: Protection Diode
- name: Rate of change of current when measuring iRM
  summary: Current change rate -50 A/us (default) | scalar
  group: Protection Diode
- name: Reverse recovery time parameterization
  summary: Recovery-time model Specify stretch factor (default) | Specify reverse recovery time directly | Specify reverse
    recovery charge
  group: Protection Diode
- name: Reverse recovery time stretch factor
  summary: Reverse recovery time stretch factor 3 (default) | scalar greater than 1
  group: Protection Diode
- name: Reverse recovery time, trr
  summary: Reverse recovery time 15 us (default) | scalar
  group: Protection Diode
- name: Reverse recovery charge, Qrr
  summary: Reverse recovery charge 1500 s*uA (default) | scalar
  group: Protection Diode
- name: Self inductance of transformer primary winding, L1
  summary: Self-inductance of transformer primary winding 0.03 H (default) | positive scalar
  group: Transformer
- name: Self inductance of transformer secondary winding, L2
  summary: Self-inductance of transformer secondary winding 0.03 H (default) | positive scalar
  group: Transformer
- name: Transformer coefficient of coupling
  summary: Coupling coefficient 0.9 (default) | positive scalar greater than zero and less than 1
  group: Transformer
- name: Inductance, L
  summary: Inductance 1e-6 H (default) | positive scalar
  group: LC Parameters
- name: Inductor series resistance
  summary: Inductor series resistance 0 Ohm (default) | zero or positive scalar
  group: LC Parameters
- name: Capacitance, C1
  summary: Capacitance 1e-7 F (default) | positive scalar
  group: LC Parameters
- name: Capacitance, C2
  summary: Capacitance 1e-7 F (default) | positive scalar
  group: LC Parameters
- name: C1 effective series resistance
  summary: Resistance 1e-6 Ohm (default) | zero or positive scalar
  group: LC Parameters
- name: C2 effective series resistance
  summary: Resistance 1e-6 Ohm (default) | zero or positive scalar
  group: LC Parameters
- name: Snubber
  summary: Snubber model None (default) | RC snubber
  group: Snubbers
- name: Snubber resistance
  summary: Resistance 0.1 Ohm (default) | scalar
  group: Snubbers
- name: Snubber capacitance
  summary: Capacitance 1e-7 F (default) | scalar
  group: Snubbers
- name: Snubber HV
  summary: Snubber model None (default) | RC snubber
  group: Snubbers
- name: Snubber resistance HV
  summary: Resistance 0.1 Ohm (default) | scalar
  group: Snubbers
- name: Snubber capacitance HV
  summary: Capacitance 1e-7 F (default) | scalar
  group: Snubbers
- name: Snubber LV
  summary: Snubber model None (default) | RC snubber
  group: Snubbers
- name: Snubber resistance LV
  summary: Resistance 0.1 Ohm (default) | scalar
  group: Snubbers
- name: Snubber capacitance LV
  summary: Capacitance 1e-7 F (default) | scalar
  group: Snubbers
```

### **Modeling option** — Converter model `Nonisolated converter` (default) | `Isolated converter` | `Dual Active Bridge converter`

Whether to model a nonisolated converter with two switching devices, an isolated converter with six switching devices, or a dual active bridge converter with eight switching devices.

### Main

### **Fidelity level** — Fidelity level `Detailed model - switching devices` (default) | `Equivalent model - PWM-controlled`

*Since R2024a*

Level of fidelity of the model.

To prioritize simulation accuracy, or to obtain results for the
individual switching devices, set this parameter to
`Detailed model - switching
devices`.

To prioritize simulation speed, set this parameter to
`Equivalent model - PWM-controlled`.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Nonisolated converter` or
`Dual Active Bridge converter`.

### Switching Devices

These tables show how the visibility of **Switching Devices**
parameters depends on the converter model and switching devices that you select when
you use the detailed model option. To learn how to read the table, see Parameter Dependencies.

**Nonisolated Converter Switching Devices Parameter Dependencies**

| Parameters and Options | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| On-state resistance | Forward voltage | Forward voltage | Drain-source on resistance | Forward voltage | On-state resistance |
| Off-state conductance | On-state resistance | On-state resistance | Off-state conductance | On-state resistance |
| Threshold voltage | Off-state conductance | Off-state conductance | Threshold voltage | Off-state conductance |
| Gate trigger voltage, Vgt | Threshold voltage | Gate trigger voltage, Vgt | Integer for piecewise constant approximation of gate input (0 for disabled) |
| Gate turn-off voltage, Vgt\_off | Gate turn-off voltage, Vgt\_off |
| Holding current | Holding current |

**Note**

To enable these parameters, set **Modeling option** to
`Nonisolated converter` and **Fidelity
level** to `Detailed model - switching
devices`.

**Isolated Converter and Dual Active Bridge Converter Switching Devices
Parameter Dependencies**

| Parameters and Options | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device HV** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| On-state resistance HV | Forward voltage HV | Forward voltage HV | Drain-source on resistance HV | Forward voltage HV | On-state resistance HV |
| Off-state conductance HV | On-state resistance HV | On-state resistance HV | Off-state conductance HV | On-state resistance HV |
| Threshold voltage HV | Off-state conductance HV | Off-state conductance HV | Threshold voltage HV | Off-state conductance HV |
| Gate trigger voltage HV, Vgt\_hv | Threshold voltage HV | Gate trigger voltage HV, Vgt\_hv | Integer for piecewise constant approximation of gate input (0 for disabled) |
| Gate turn-off voltage HV, Vgt\_off\_hv | Gate turn-off voltage HV, Vgt\_off\_hv |
| Holding current HV | Holding current HV |
| **Switching device LV** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| On-state resistance LV | Forward voltage LV | Forward voltage LV | Drain-source on resistance LV | Forward voltage LV | On-state resistance LV |
| Off-state conductance LV | On-state resistance LV | On-state resistance LV | Off-state conductance LV | On-state resistance LV |
| Threshold voltage LV | Off-state conductance LV | Off-state conductance LV | Threshold voltage LV | Off-state conductance LV |
| Gate trigger voltage LV, Vgt | Threshold voltage LV | Gate trigger voltage LV, Vgt | Integer for piecewise constant approximation of gate input (0 for disabled) |
| Gate turn-off voltage LV, Vgt\_off\_lv | Gate turn-off voltage LV, Vgt\_off\_lv |
| Holding current LV | Holding current LV |

**Note**

To enable these parameters, choose one of these options:

- Set **Modeling option** to `Isolated
  converter`.
- Set **Modeling option** to `Dual
  Active Bridge converter` and **Fidelity
  level** to `Detailed model - switching
  devices`.

### **Switching device** — Switch type `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Switching device type for the nonisolated converter model.

#### Dependencies

See the Nonisolated Converter Switching Devices Parameter Dependencies table.

### **Forward voltage** — Voltage `0.8` `V` (default) | scalar

For the different switching device types, the **Forward
voltage** is taken as:

- GTO — Minimum voltage required across the anode and
  cathode block ports for the gradient of the device I-V
  characteristic to be
  1/*Ron*, where
  *Ron* is the
  value of **On-state resistance**
- IGBT — Minimum voltage required across the collector and
  emitter block ports for the gradient of the diode i-v
  characteristic to be
  1/*Ron*, where
  *Ron* is the
  value of **On-state resistance**
- Thyristor — Minimum voltage required for the device to
  turn on

#### Dependencies

See the Nonisolated Converter Switching Devices Parameter Dependencies table.

### **On-state resistance** — Resistance `0.001` `Ohm` (default) | scalar

For the different switching device types, the **On-state
resistance** is taken as:

- GTO — Rate of change of voltage versus current above the
  forward voltage
- Ideal semiconductor switch — Anode-cathode resistance when
  the device is on
- IGBT — Collector-emitter resistance when the device is
  on
- Thyristor — Anode-cathode resistance when the device is
  on
- Averaged switch — Anode-cathode resistance when the device
  is on

#### Dependencies

See the Nonisolated Converter Switching Devices Parameter Dependencies table.

### **Drain-source on resistance** — Resistance `0.001` `Ohm` (default) | scalar

Resistance between the drain and the source, which also depends on the
gate-to-source voltage.

#### Dependencies

See the Nonisolated Converter Switching Devices Parameter Dependencies table.

### **Off-state conductance** — Conductance `1e-5` `1/Ohm` (default) | scalar

Conductance when the device is off. The value must be less than
1/*R*, where *R* is the value of
**On-state resistance**.

For the different switching device types, the **On-state
resistance** is taken as:

- GTO — Anode-cathode conductance
- Ideal semiconductor switch — Anode-cathode
  conductance
- IGBT — Collector-emitter conductance
- MOSFET — Drain-source conductance
- Thyristor — Anode-cathode conductance

#### Dependencies

See the Nonisolated Converter Switching Devices Parameter Dependencies table.

### **Threshold voltage** — Voltage threshold `6` `V` (default) | scalar

Gate voltage threshold. The device turns on when the gate voltage is
above this value. For the different switching device types, the device
voltage of interest is:

- Ideal semiconductor switch — Gate-cathode voltage
- IGBT — Gate-emitter voltage
- MOSFET — Gate-source voltage

#### Dependencies

See the Nonisolated Converter Switching Devices Parameter Dependencies table.

### **Gate trigger voltage, Vgt** — Voltage threshold `1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

#### Dependencies

See the Nonisolated Converter Switching Devices Parameter Dependencies table.

### **Gate turn-off voltage, Vgt\_off** — Voltage threshold `-1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns off when the
gate-cathode voltage is below this value.

#### Dependencies

See the Nonisolated Converter Switching Devices Parameter Dependencies table.

### **Holding current** — Current threshold `1` `A` (default) | scalar

Gate current threshold. The device stays on when the current is above
this value, even when the gate-cathode voltage falls below the gate
trigger voltage.

#### Dependencies

See the Nonisolated Converter Switching Devices Parameter Dependencies table.

### **Switching device HV** — Switch `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Switching device type for the high-voltage side of the isolated
converter model.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Forward voltage HV** — Voltage `0.8` `Ohm` (default) | scalar

For the different switching device types, the **Forward
voltage HV** is taken as:

- GTO — Minimum voltage required across the anode and
  cathode block ports for the gradient of the device I-V
  characteristic to be
  1/*Ron*, where
  *Ron* is the
  value of **On-state resistance**
- IGBT — Minimum voltage required across the collector and
  emitter block ports for the gradient of the diode i-v
  characteristic to be
  1/*Ron*, where
  *Ron* is the
  value of **On-state resistance**
- Thyristor — Minimum voltage required for the device to
  turn on

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Drain-source on resistance HV** — Resistance `0.001` `Ohm` (default) | scalar

Resistance between the drain and the source, which also depends on the
gate-to-source voltage.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **On-state resistance HV** — Resistance `0.001` `Ohm` (default) | scalar

For the different switching device types, the **On-state
resistance HV** is taken as:

- GTO — Rate of change of voltage versus current above the
  forward voltage
- Ideal semiconductor switch — Anode-cathode resistance when
  the device is on
- IGBT — Collector-emitter resistance when the device is
  on
- Thyristor — Anode-cathode resistance when the device is
  on
- Averaged switch — Anode-cathode resistance when the device
  is on

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Off-state conductance HV** — Conductance `1e-5` `1/Ohm` (default) | scalar

Conductance when the device is off. The value must be less than
1/*R*, where *R* is the value of
**On-state resistance HV**.

For the different switching device types, the **On-state
resistance HV** is taken as:

- GTO — Anode-cathode conductance
- Ideal semiconductor switch — Anode-cathode
  conductance
- IGBT — Collector-emitter conductance
- MOSFET — Drain-source conductance
- Thyristor — Anode-cathode conductance

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Threshold voltage HV** — Voltage threshold `6` `V` (default) | scalar

Gate voltage threshold. The device turns on when the gate voltage is
above this value. For the different switching device types, the device
voltage of interest is:

- Ideal semiconductor switch — Gate-cathode voltage
- IGBT — Gate-emitter voltage
- MOSFET — Gate-source voltage

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Gate trigger voltage HV, Vgt\_hv** — Voltage threshold `1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Gate turn-off voltage HV, Vgt\_off\_hv** — Voltage threshold `-1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns off when the
gate-cathode voltage is below this value.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Holding current HV** — Current threshold `1` `A` (default) | scalar

Gate current threshold. The device stays on when the current is above
this value, even when the gate-cathode voltage falls below the gate
trigger voltage.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Switching device LV** — Switch `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Switching device type for the low-voltage side of the isolated
converter model.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Forward voltage LV** — Voltage `0.8` `Ohm` (default) | scalar

For the different switching device types, the **Forward
voltage LV** is taken as:

- GTO — Minimum voltage required across the anode and
  cathode block ports for the gradient of the device I-V
  characteristic to be
  1/*Ron*, where
  *Ron* is the
  value of **On-state resistance**
- IGBT — Minimum voltage required across the collector and
  emitter block ports for the gradient of the diode i-v
  characteristic to be
  1/*Ron*, where
  *Ron* is the
  value of **On-state resistance**
- Thyristor — Minimum voltage required for the device to
  turn on

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Drain-source on resistance LV** — Resistance `0.001` `Ohm` (default) | scalar

Resistance between the drain and the source, which also depends on the
gate-to-source voltage.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **On-state resistance LV** — Resistance `0.001` `Ohm` (default) | scalar

For the different switching device types, the **On-state
resistance LV** is taken as:

- GTO — Rate of change of voltage versus current above the
  forward voltage
- Ideal semiconductor switch — Anode-cathode resistance when
  the device is on
- IGBT — Collector-emitter resistance when the device is
  on
- Thyristor — Anode-cathode resistance when the device is
  on
- Averaged switch — Anode-cathode resistance when the device
  is on

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Off-state conductance LV** — Conductance `1e-5` `1/Ohm` (default) | scalar

Conductance when the device is off. The value must be less than
1/*R*, where *R* is the value of
**On-state resistance LV**.

For the different switching device types, the **On-state
resistance LV** is taken as:

- GTO — Anode-cathode conductance
- Ideal semiconductor switch — Anode-cathode
  conductance
- IGBT — Collector-emitter conductance
- MOSFET — Drain-source conductance
- Thyristor — Anode-cathode conductance

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Threshold voltage LV** — Voltage threshold `6` `V` (default) | scalar

Gate voltage threshold. The device turns on when the gate voltage is
above this value. For the different switching device types, the device
voltage of interest is:

- Ideal semiconductor switch — Gate-cathode voltage
- IGBT — Gate-emitter voltage
- MOSFET — Gate-source voltage

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Gate trigger voltage LV, Vgt\_lv** — Voltage threshold `1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Gate turn-off voltage LV, Vgt\_off\_lv** — Voltage threshold `-1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns off when the
gate-cathode voltage is below this value.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Holding current LV** — Current threshold `1` `A` (default) | scalar

Gate current threshold. The device stays on when the current is above
this value, even when the gate-cathode voltage falls below the gate
trigger voltage.

#### Dependencies

See the Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies table.

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — Integer mode for FPGA deployment `0` (default) | nonnegative scalar

Integer used to perform piecewise constant approximation of the gate input for FPGA
deployment.

#### Dependencies

To enable this parameter, set **Switching device** to `Averaged Switch`.

### Protection Diode

To enable these parameters, choose one of these options:

- Set **Modeling Option** to `Nonisolated
  converter` or `Dual Active Bridge
  converter` and **Fidelity level** to
  `Detailed model - switching
  devices`.
- Set **Modeling Option** to `Isolated
  converter`.

The visibility of the **Protection Diode**
parameters depends on how you configure the **Model dynamics** and
**Reverse recovery time parameterization** parameters. To learn
how to read this table, see Parameter Dependencies.

**Protection Diode Parameter Dependencies**

| Parameters and Options | | | |
| --- | --- | --- | --- |
| **Model dynamics** | | | |
| *Diode with no dynamics* | *Diode with charge dynamics* | | |
| Forward voltage | Forward voltage | | |
| On resistance | On resistance | | |
| Off conductance | Off conductance | | |
| Junction capacitance | | |
| Peak reverse current, iRM | | |
| Initial forward current when measuring iRM | | |
| Rate of change of current when measuring iRM | | |
| **Reverse recovery time parameterization** | | |
| *`Specify stretch factor`* | *`Specify reverse recovery time directly`* | *`Specify reverse recovery charge`* |
| Reverse recovery time stretch factor | Reverse recovery time, trr | Reverse recovery charge, Qrr |

**Note**

If you set the **Switching device** parameter to
`Averaged Switch`, the block models protection
diodes with no dynamics and the **Model dynamics**
parameter is not visible.

### **Model dynamics** — Diode model `Diode with no dynamics` (default) | `Diode with charge dynamics`

Model that the Bidirectional DC-DC Converter block uses for the protection diode for
each switching device. Choose one of these options:

- `None` — The Bidirectional DC-DC Converter does not
  model protection diodes.
- `Diode with no dynamics` — The
  Bidirectional DC-DC Converter block models protection diodes using the same
  equations as the Diode
  block with no dynamics. Select this option to prioritize
  simulation speed.
- `Diode with charge dynamics` —
  The Bidirectional DC-DC Converter block models protection diodes using the
  same equations as the Diode
  block with charge dynamics. Select this option to prioritize
  detailed simulation results.

#### Dependencies

See the Protection Diode Parameter Dependencies table.

### **Forward voltage** — Voltage `0.8` `V` (default) | scalar

Minimum voltage required across the positive and negative block ports
for the gradient of the diode I-V characteristic to be
1/*Ron*, where
*Ron* is the value of
the **On resistance** parameter.

### **On resistance** — On resistance `0.001` `Ohm` (default) | scalar

Rate of change of voltage versus current above the **Forward
voltage** parameter value.

### **Off conductance** — Conductance `1e-5` `1/Ohm` (default) | scalar

Conductance of the reverse-biased diode.

### **Junction capacitance** — Junction capacitance `50` `nF` (default) | scalar

Diode junction capacitance.

#### Dependencies

See the Protection Diode Parameter Dependencies table.

### **Peak reverse current, iRM** — Peak reverse current `-235` `A` (default) | negative scalar

Peak reverse current measured by an external test circuit.

#### Dependencies

See the Protection Diode Parameter Dependencies table.

### **Initial forward current when measuring iRM** — Initial forward current when measuring iRM `300` `A` (default) | positive scalar

Initial forward current when measuring peak reverse current.

#### Dependencies

See the Protection Diode Parameter Dependencies table.

### **Rate of change of current when measuring iRM** — Current change rate `-50` `A/us` (default) | scalar

Rate of change of current when measuring peak reverse current.

#### Dependencies

See the Protection Diode Parameter Dependencies table.

### **Reverse recovery time parameterization** — Recovery-time model `Specify stretch factor` (default) | `Specify reverse recovery time directly` | `Specify reverse recovery charge`

Model for parameterizing the recovery time. When you select
`Specify stretch factor` or
`Specify reverse recovery charge`, you can
specify a value that the block uses to derive the reverse recovery time.
For more information on these options, see How the Block Calculates TM and Tau.

#### Dependencies

See the Protection Diode Parameter Dependencies table.

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default) | scalar greater than `1`

Stretch factor that the block uses to calculate the reverse recovery
time. Specifying the stretch factor is an easier way to parameterize the
reverse recovery time than specifying the reverse recovery charge. The
larger the value of the stretch factor, the longer it takes for the
reverse recovery current to dissipate.

#### Dependencies

See the Protection Diode Parameter Dependencies table.

### **Reverse recovery time, trr** — Reverse recovery time `15` `us` (default) | scalar

Interval between the time when the current initially goes to zero
(when the diode turns off) and the time when the current falls to less
than 10 percent of the peak reverse current.

The value of the **Reverse recovery time, trr**
parameter must be greater than the value of the **Peak reverse
current, iRM** parameter divided by the value of the
**Rate of change of current when measuring iRM**
parameter.

#### Dependencies

See the Protection Diode Parameter Dependencies table.

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `s*uA` (default) | scalar

Reverse recovery charge that the block uses to calculate the reverse
recovery time. Use this parameter if the data sheet for your diode
device specifies a value for the reverse recovery charge instead of a
value for the reverse recovery time.

The reverse recovery charge is the total charge that continues to
dissipate when the diode turns off. The value must be less than −i2RM2a,

where:

- *iRM* is the value
  specified for **Peak reverse current,
  iRM**.
- *a* is the value specified for **Rate
  of change of current when measuring iRM**.

#### Dependencies

See the Protection Diode Parameter Dependencies table.

### Transformer

### **Self inductance of transformer primary winding, L1** — Self-inductance of transformer primary winding `0.03` `H` (default) | positive scalar

Self-inductance of the primary winding of the transformer.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Isolated converter` or
`Dual Active Bridge converter`.

### **Self inductance of transformer secondary winding, L2** — Self-inductance of transformer secondary winding `0.03` `H` (default) | positive scalar

Self-inductance of the secondary winding of the transformer.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Isolated converter` or
`Dual Active Bridge converter`.

### **Transformer coefficient of coupling** — Coupling coefficient `0.9` (default) | positive scalar greater than zero and less than 1

Defines the mutual inductance of the transformer.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Isolated converter` or
`Dual Active Bridge converter`.

### LC Parameters

### **Inductance, L** — Inductance `1e-6` `H` (default) | positive scalar

Converter inductance. If you set the **Modeling
option** parameter to `Isolated
converter`, the two inductors are identical.

### **Inductor series resistance** — Inductor series resistance `0` `Ohm` (default) | zero or positive scalar

Series resistance of the inductor.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Modeling Option** to
  `Isolated
  converter`.
- Set **Modeling Option** to
  `Nonisolated converter` or
  `Dual Active Bridge
  converter` and **Fidelity
  level** to `Detailed model -
  switching devices`.

### **Capacitance, C1** — Capacitance `1e-7` `F` (default) | positive scalar

Capacitance of the first DC terminal.

### **Capacitance, C2** — Capacitance `1e-7` `F` (default) | positive scalar

Capacitance of the second DC terminal.

### **C1 effective series resistance** — Resistance `1e-6` `Ohm` (default) | zero or positive scalar

Series resistance of capacitor *C1*.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Modeling Option** to
  `Isolated
  converter`.
- Set **Modeling Option** to
  `Nonisolated converter` or
  `Dual Active Bridge
  converter` and **Fidelity
  level** to `Detailed model -
  switching devices`.

### **C2 effective series resistance** — Resistance `1e-6` `Ohm` (default) | zero or positive scalar

Series resistance of capacitor *C2*.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Modeling Option** to
  `Isolated
  converter`.
- Set **Modeling Option** to
  `Nonisolated converter` or
  `Dual Active Bridge
  converter` and **Fidelity
  level** to `Detailed model -
  switching devices`.

### Snubbers

To enable these parameters, set **Switching device** to one of
these options:

- `Ideal Semiconductor Switch`
- `GTO`
- `IGBT`
- `MOSFET`
- `Thyristor`

This table summarizes the **Snubbers** parameter dependencies. To
learn how to read the table, see Parameter Dependencies.

**Snubbers Parameter Dependencies**

| Snubbers Parameter Dependencies | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Modeling option** | | | | | |
| *`Nonisolated Converter`* | | *`Isolated Converter`* | | *`Dual Active Bridge converter`* | |
| **Snubber** | | **Snubber HV** | | **Snubber HV** | |
| *`None`* | *`RC Snubber`* | **`None`** | *`RC Snubber`* | **`None`** | *`RC Snubber`* |
| Snubber resistance | Snubber resistance HV | Snubber resistance HV |
| Snubber capacitance | Snubber capacitance HV | Snubber capacitance HV |
| **Snubber LV** | | **Snubber LV** | |
| *`None`* | *`RC Snubber`* | *`None`* | *`RC Snubber`* |
| Snubber resistance LV | Snubber resistance LV |
| Snubber capacitance LV | Snubber capacitance LV |

### **Snubber** — Snubber model `None` (default) | `RC snubber`

Snubber for each switching device.

#### Dependencies

See the Snubbers Parameter Dependencies table.

### **Snubber resistance** — Resistance `0.1` `Ohm` (default) | scalar

Resistance of the snubbers.

#### Dependencies

See the Snubbers Parameter Dependencies table.

### **Snubber capacitance** — Capacitance `1e-7` `F` (default) | scalar

Capacitance of the snubbers.

#### Dependencies

See the Snubbers Parameter Dependencies table.

### **Snubber HV** — Snubber model `None` (default) | `RC snubber`

HV snubber for each switching device.

#### Dependencies

See the Snubbers Parameter Dependencies table.

### **Snubber resistance HV** — Resistance `0.1` `Ohm` (default) | scalar

Resistance of the high-voltage snubbers.

#### Dependencies

See the Snubbers Parameter Dependencies table.

### **Snubber capacitance HV** — Capacitance `1e-7` `F` (default) | scalar

Capacitance of the high-voltage snubbers.

#### Dependencies

See the Snubbers Parameter Dependencies table.

### **Snubber LV** — Snubber model `None` (default) | `RC snubber`

LV snubber for each switching device.

#### Dependencies

See the Snubbers Parameter Dependencies table.

### **Snubber resistance LV** — Resistance `0.1` `Ohm` (default) | scalar

Resistance of the low-voltage snubbers.

#### Dependencies

See the Snubbers Parameter Dependencies table.

### **Snubber capacitance LV** — Capacitance `1e-7` `F` (default) | scalar

Capacitance of the low-voltage snubbers.

#### Dependencies

See the Snubbers Parameter Dependencies table.
## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024a: Increase simulation speed using an equivalent model

If you model a nonisolated converter or a dual active bridge converter, you can
now choose from two fidelity levels for the converter model. The equivalent model
option does not model the individual switching devices but returns equivalent
results. If you need detailed results for the switching device dynamics, use the
detailed model option. Otherwise, use the equivalent model for faster simulation. To
simulate in real time, use the equivalent model. To validate the results, use the
detailed model with a variable-step solver.

To use the detailed model, set the **Fidelity level** parameter
to `Detailed model - switching devices`. To use the
equivalent model, set the **Fidelity level** parameter to
`Equivalent model - PWM-controlled`.

Before R2024a, you can use the detailed model only.

## Description

Controller-driven bidirectional DC-DC step-up and step-down voltage regulator

The Bidirectional DC-DC Converter block represents a
converter that steps up or steps down DC voltage from either side of the converter to
the other as driven by an attached controller and gate-signal generator. Bidirectional
DC-DC converters are useful for switching between energy storage and use, for example,
in electric vehicles.

The Bidirectional DC-DC Converter block allows you to
model a nonisolated converter with two switching devices, an isolated converter with six
switching devices, or a dual active bridge converter with eight switching
devices.

If you model a nonisolated converter or a dual active bridge converter, you can choose
from two fidelity levels for the converter model. The equivalent model option does not
model the individual switching devices but returns equivalent results. If you need
detailed results for the switching device dynamics, use the detailed model option.
Otherwise, use the equivalent model for faster simulation. To simulate in real time, use
the equivalent model. To validate the results, use the detailed model with a
variable-step solver. To use the detailed model, set the **Fidelity
level** parameter to `Detailed model - switching
devices`. To use the equivalent model, set the **Fidelity
level** parameter to `Equivalent model -
PWM-controlled`.

If you model an isolated converter, you can only use the detailed model. The
**Fidelity level** parameter is not visible.

If you choose the detailed model, each component is the same switching device, which
you specify by setting the **Switching device** parameter. The
switching devices that you can specify are implementations of blocks in the **Simscape** > **Electrical** > **Semiconductors & Converters** library:

- GTO — Gate turn-off thyristor. For information about the I-V characteristic of the
  device, see GTO.
- Ideal semiconductor switch — For information about the I-V characteristic of the
  device, see Ideal Semiconductor Switch.
- IGBT — Insulated-gate bipolar transistor. For information about the I-V characteristic
  of the device, see IGBT (Ideal, Switching).
- MOSFET — N-channel metal-oxide-semiconductor field-effect transistor. For information
  about the I-V characteristic of the device, see MOSFET (Ideal, Switching).
- Thyristor — For information about the I-V characteristic of the device, see
  Thyristor (Piecewise Linear).
- Averaged Switch — Semiconductor switch with an antiparallel diode. The control signal
  port **G** accepts values in the interval [0,1]. When
  **G** is equal to `0` or `1`, the
  averaged switch is fully opened or fully closed respectively. The switch behaves
  similarly to the Ideal Semiconductor Switch block with
  an antiparallel diode. When **G** is between 0 and 1, the averaged
  switch is partly opened. You can average the pulse-width modulation (PWM) signal over a
  specified period. You can then undersample the model and use modulation waveforms
  instead of PWM signals.

**Note**

If you set the **Switching device** parameter to
`Averaged Switch`, the block automatically models
protection diodes with no dynamics and the **Model dynamics**
parameter is not visible.

### Model

You can model three different types of
bidirectional DC-DC converter. To access the different options, double-click the
block and set the **Modeling option** parameter to either:

- `Nonisolated converter` — Bidirectional DC-DC
  converter without an electrical barrier. This converter contains an
  inductor, two capacitors, and two switches that are of the same device type.
- `Isolated converter` — Bidirectional DC-DC
  converter with an electrical barrier. This converter contains four
  additional switches that form a full bridge. The full bridge is on the
  input or high-voltage (HV) side of the converter. The other two switches
  are on the output or low-voltage (LV) side of the converter. You can
  select different semiconductor types for the HV and LV switching
  devices. For example, you can use a GTO for the HV switching devices and
  an IGBT for the LV switching devices. To provide separation between the
  input and output voltages, the model uses a high-frequency transformer.
- `Dual Active Bridge converter` — This
  bidirectional DC-DC converter contains two full-bridges. The left bridge
  is the input or high-voltage (HV) side of the converter. The right
  bridge is the output or low-voltage (LV) side of the converter. You can
  select different semiconductor types for the HV and LV switching
  devices. For example, you can use a GTO for the HV switching devices and
  an IGBT for the LV switching devices. To provide separation between the
  input and output voltages, the model uses a high-frequency transformer.
  To use the equivalent model and use either of the two sides of the
  transformer as a rectifier, set the elements of the PWM signal
  corresponding to that side to zero. That side of the transformer behaves
  as a diode rectifier.

### Protection

The block contains an integral protection diode for each switching device. The
integral diode protects the semiconductor device by providing a conduction path for
reverse current. An inductive load can produce a high reverse-voltage spike when the
semiconductor device suddenly switches off the voltage supply to the load.

To configure the internal protection diode block, use the **Protection
Diode** parameters. This table shows how to set the **Model
dynamics** parameter based on your goals.

| Goals | Value to Select | Integral Protection Diode |
| --- | --- | --- |
| Prioritize simulation speed. | `Diode with no dynamics` | The Diode block |
| Prioritize model fidelity by precisely specifying reverse-mode charge dynamics. | `Diode with charge dynamics` | The dynamic model of the Diode block |

You can also include a snubber circuit for each switching device. Snubber circuits contain a series-connected resistor and capacitor. They protect switching devices against high voltages that inductive loads produce when the device turns off the voltage supply to the load. Snubber circuits also prevent excessive rates of current change when a switching device turns on.

To include and configure a snubber circuit for each switching device, use the
**Snubbers** parameters.

### Gate Control

To connect Simulink® gate-control voltage signals to the gate ports of the switching devices:

1. Convert each voltage signal using a Simulink-PS
   Converter block.
2. Multiplex the converted gate signals into a single vector.

   - For a nonisolated converter model, use a Two-Pulse Gate Multiplexer
     block.
   - For an isolated converter model, use a Six-Pulse Gate
     Multiplexer block.
   - For a dual active bridge converter model, use a
     Eight-Pulse Gate Multiplexer
     block.
3. Connect the vector signal to the **G** port.

### Piecewise Constant Approximation in Averaged Switch for FPGA Deployment

If you set the **Switching device** parameter to `Averaged switch` and your model uses a partitioning solver, this block produces nonlinear partitions because the average mode equations include modes, *Gsat* that are functions of the input **G**. To make these equations compatible with hardware description language (HDL) code generation, and therefore FPGA deployment, set the **Integer for piecewise constant approximation of gate input (0 for disabled)** parameter to a value greater than `0`. This block then treats the *Gsat* mode as a piecewise constant integer with a fixed range. This turns the previously nonlinear partitions to linear time varying partitions.

An integer value in the range `[0,K]`, where *K* is the value of the **Integer for piecewise constant approximation of gate input (0 for disabled)**, is now associated with each real value mode in the range `[0,1]`. The block computes the piecewise constant mode by dividing the original mode by K to normalize it back to the range `[0,1]`:

uI=(floor(u⋅K))u^=uIK

### Assumptions

A source impedance or a nonzero equivalent-series resistance (ESR) is connected to
the left side of the Bidirectional DC-DC Converter
block.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
