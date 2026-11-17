---
type: simulink-block
title: 'Operational Amplifier'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'operationalamplifier'
documentation_source_path: 'ref/operationalamplifier.html'
language: en
---

# Operational Amplifier

## Ports
```yaml
ports:
- name: InP
  summary: Positive input terminal scalar
  direction: input
  data_types: single | double
- name: InN
  summary: Negative input terminal scalar
  direction: input
  data_types: single | double
- name: OutP
  summary: Positive output terminal scalar
  direction: output
  data_types: single | double
- name: OutN
  summary: Negative output terminal scalar
  direction: output
  data_types: single | double
```

### Input

### **InP** — Positive input terminal scalar

Positive input terminal of the operational amplifier.

**Data Types:** `single` | `double`

### **InN** — Negative input terminal scalar

Negative input terminal of the operational amplifier.

**Data Types:** `single` | `double`
### Output

### **OutP** — Positive output terminal scalar

Positive output terminal of the operational amplifier.

**Data Types:** `single` | `double`

### **OutN** — Negative output terminal scalar

Negative output terminal of the operational amplifier.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Operational Amplifier Circuit
  summary: Type of operational amplifier circuit Double-pole Circuit (default) | Multipole Circuit
  group: ''
  block_parameter: OpampType
  type: character vector
  values: Double-pole Circuit| Multipole Circuit
  default: Double-pole Circuit
- name: Inherit sample interval from input
  summary: Inherit sample interval from input off (default) | on
  group: ''
- name: Sample interval (s)
  summary: Sample interval value used in MATLAB analyses 1e-8 (default) | scalar
  group: ''
  block_parameter: SampleInterval
  type: character vector
  values: scalar
  default: 1e-8
- name: Simulate using
  summary: Select simulation mode Code generation (default) | Interpreted execution
  group: ''
  block_parameter: SimulateUsing
  type: character vector
  values: Code generation| Interpreted execution
  default: Code generation
- name: Supply rail high (V)
  summary: Maximum supply voltage 5 (default) | real scalar
  group: Signal Parameters
  block_parameter: VoltageSupplyPlus
  type: character vector
  values: real scalar
  default: '5'
- name: Supply rail low (V)
  summary: Minimum supply voltage -5 (default) | real scalar
  group: Signal Parameters
  block_parameter: VoltageSupplyMinus
  type: character vector
  values: real scalar
  default: '-5'
- name: Input offset voltage (V)
  summary: Offset voltage at input terminals 0 (default) | scalar
  group: Signal Parameters
  block_parameter: InputOffsetVoltage
  type: character vector
  values: scalar
  default: '0'
- name: Open loop gain (V/V)
  summary: Operational amplifier gain without feedback 3e3 (default) | positive real scalar
  group: Advanced Parameters
  block_parameter: Gain
  type: character vector
  values: positive real scalar
  default: 3e3
- name: Unity gain bandwidth (Hz)
  summary: Frequency at which operational amplifier gain equals unity 10e6 (default) | positive real scalar
  group: Advanced Parameters
  block_parameter: FrequencyUnityGain
  type: character vector
  values: positive real scalar
  default: 10e6
- name: Maximum tail current (A)
  summary: Maximum current passing through tail MOSFET in operational amplifier circuit 100e-6 (default) | positive real scalar
  group: Advanced Parameters
  block_parameter: InputCurrentMax
  type: character vector
  values: positive real scalar
  default: 100e-6
- name: Slew rate (V/s)
  summary: Rate of change of operational amplifier output voltage 10e6 (default) | positive real scalar
  group: Advanced Parameters
  block_parameter: SlewRate
  type: character vector
  values: positive real scalar
  default: 10e6
- name: Output resistance (Ohms)
  summary: Resistance at output terminals 10e3 (default) | positive real scalar
  group: Advanced Parameters
  block_parameter: OutputResistance
  type: character vector
  values: positive real scalar
  default: 10e3
- name: Output Capacitance (F)
  summary: Capacitance at output terminals 50e-12 (default) | positive real scalar
  group: Advanced Parameters
  block_parameter: OutputCapacitance
  type: character vector
  values: positive real scalar
  default: 50e-12
- name: Transfer function poles
  summary: Poles in transfer function in Laplace domain [-2.09e+04 -8.62e+07] (default) | column vector
  group: Advanced Parameters
  block_parameter: Poles
  type: character vector
  values: column vector
  default: '[-2.09e+04 -8.62e+07]'
- name: Transfer function zeroes
  summary: Zeros in transfer function in Laplace domain [-9.14e+07] (default) | column vector
  group: Advanced Parameters
  block_parameter: Zeros
  type: character vector
  values: column vector
  default: '[-9.14e+07]'
- name: Include Z-domain approximation
  summary: Include *z*-domain approximation while plotting open loop response off (default) | on
  group: Analysis
- name: Plot open loop response
  summary: Plot open loop response of op-amp button
  group: Analysis
```

### **Operational Amplifier Circuit** — Type of operational amplifier circuit `Double-pole Circuit` (default) | `Multipole Circuit`

Type of the operational amplifier circuit.

- `Double-pole Circuit` — Use circuit parameters such as
  open-loop gain, unity gain bandwidth, maximum tail current, and slew rate to define
  a simple double-pole circuit.
- `Multipole Circuit` — Use transfer function poles and
  zeros to define a multiple-pole circuit.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OpampType` |
| **Type:** character vector |
| **Values:** `Double-pole Circuit`| `Multipole Circuit` |
| **Default:** `Double-pole Circuit` |

### **Inherit sample interval from input** — Inherit sample interval from input off (default) | on

Inherit the sample interval value from the input. By default, this option is
deselected.

### **Sample interval (s)** — Sample interval value used in MATLAB analyses `1e-8` (default) | scalar

Sample interval value the block uses in MATLAB® analyses, specified as a scalar in seconds.

#### Dependencies

To enable this parameter, deselect the **Inherit sample interval from
input** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SampleInterval` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `1e-8` |

### **Simulate using** — Select simulation mode `Code generation` (default) | `Interpreted execution`

Select the simulation mode. This option you choose affects simulation
performance.

Simulating the model using the `Code generation` method
requires additional startup time, but the subsequent simulations run faster. Simulating
the model using the `Interpreted execution` method may reduce
the startup time, but the subsequent simulations run slower. For more information, see
Interpreted Execution vs. Code Generation.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SimulateUsing` |
| **Type:** character vector |
| **Values:** `Code generation`| `Interpreted execution` |
| **Default:** `Code generation` |

### Signal Parameters

### **Supply rail high (V)** — Maximum supply voltage `5` (default) | real scalar

Maximum supply voltage provided to the Operational Amplifier block,
specified as a real scalar in volts.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `VoltageSupplyPlus` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `5` |

### **Supply rail low (V)** — Minimum supply voltage `-5` (default) | real scalar

Minimum supply voltage provided to the Operational Amplifier block,
specified as a real scalar in volts.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `VoltageSupplyMinus` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `-5` |

### **Input offset voltage (V)** — Offset voltage at input terminals `0` (default) | scalar

Offset voltage at the input terminals of the operational amplifier, specified as a
scalar in volts. The block uses this value to obtain a zero voltage at the output
terminals of the operational amplifier.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `InputOffsetVoltage` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `0` |

### Advanced Parameters

### **Open loop gain (V/V)** — Operational amplifier gain without feedback `3e3` (default) | positive real scalar

The gain of the operational amplifier without any positive or negative feedback,
specified as a unitless positive real scalar.

#### Dependencies

To enable this parameter, set **Operational Amplifier
Circuit** to `Double Pole Circuit`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Gain` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `3e3` |

### **Unity gain bandwidth (Hz)** — Frequency at which operational amplifier gain equals unity `10e6` (default) | positive real scalar

The frequency at which the open-loop gain of the operational amplifier becomes
unity, specified as a positive real scalar in hertz.

#### Dependencies

To enable this parameter, set **Operational Amplifier
Circuit** to `Double Pole Circuit`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FrequencyUnityGain` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `10e6` |

### **Maximum tail current (A)** — Maximum current passing through tail MOSFET in operational amplifier circuit `100e-6` (default) | positive real scalar

Maximum value of the current passing through the tail MOSFET (metal oxide
semiconductor field effect transistor) in the operational amplifier circuit, specified
as a positive real scalar in amperes.

#### Dependencies

To enable this parameter, set **Operational Amplifier
Circuit** to `Double Pole Circuit`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `InputCurrentMax` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `100e-6` |

### **Slew rate (V/s)** — Rate of change of operational amplifier output voltage `10e6` (default) | positive real scalar

The rate of the change of the output voltage of the operational amplifier with
respect to time, specified as a positive real scalar.

#### Dependencies

To enable this parameter, set **Operational Amplifier
Circuit** to `Double Pole Circuit`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SlewRate` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `10e6` |

### **Output resistance (Ohms)** — Resistance at output terminals `10e3` (default) | positive real scalar

Resistance at the output terminals of the operational amplifier, specified as a
positive real scalar in ohms.

#### Dependencies

To enable this parameter, set **Operational Amplifier
Circuit** to `Double Pole Circuit`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputResistance` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `10e3` |

### **Output Capacitance (F)** — Capacitance at output terminals `50e-12` (default) | positive real scalar

Capacitance at the output terminals of the operational amplifier, specified as a
positive real scalar in farads.

#### Dependencies

To enable this parameter, set **Operational Amplifier
Circuit** to `Double Pole Circuit`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputCapacitance` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `50e-12` |

### **Transfer function poles** — Poles in transfer function in Laplace domain `[-2.09e+04 -8.62e+07]` (default) | column vector

Poles in the transfer function of the operational amplifier in the Laplace domain,
specified as a column vector in rad/s.

If you set **Operational Amplifier Circuit** to
`Double-pole Circuit`, the block automatically calculates
the poles for you from the circuit parameters. If you set **Operational
Amplifier Circuit** to `Multipole Circuit`, you
can specify the poles.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Poles` |
| **Type:** character vector |
| **Values:** column vector |
| **Default:** `[-2.09e+04 -8.62e+07]` |

### **Transfer function zeroes** — Zeros in transfer function in Laplace domain `[-9.14e+07]` (default) | column vector

Zeros in the transfer function of the operational amplifier in the Laplace domain,
specified as a column vector in rad/s.

If you set **Operational Amplifier Circuit** to
`Double-pole Circuit`, the block automatically calculates
the zeros for you from the circuit parameters. If you set **Operational
Amplifier Circuit** to `Multipole Circuit`, you
can specify the zeros.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Zeros` |
| **Type:** character vector |
| **Values:** column vector |
| **Default:** `[-9.14e+07]` |

### Analysis

### **Include Z-domain approximation** — Include *z*-domain approximation while plotting open loop response off (default) | on

When plotting the open-loop response of the operational amplifier, include the
*z*-domain (discrete time) approximation in addition to
*s*-domain transfer function.

### **Plot open loop response** — Plot open loop response of op-amp button

Plot the *s*-domain transfer function of the open loop response
of the operational amplifier. The plot also reports the unity gain bandwidth and phase
margin. You can choose to include the *z*-domain
approximation.
## Libraries

Mixed-Signal Blockset / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2024a: Plot Open Loop Response

You can now plot the open loop response of the operational amplifier, along with the
*z*-domain approximation.

## Description

Model operational amplifier with two or more poles

Use the Operational Amplifier block to model an operational amplifier with
two or more poles. You can create a double-pole amplifier from the important circuit
parameters or a multiple-pole amplifier from a transfer function. Use the block to
characterize the performance of an operational amplifier as part of a larger circuit
system.
