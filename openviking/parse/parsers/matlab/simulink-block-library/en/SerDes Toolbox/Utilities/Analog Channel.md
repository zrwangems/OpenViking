---
type: simulink-block
title: 'Analog Channel'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'analogchannel'
documentation_source_path: 'ref/analogchannel.html'
language: en
---

# Analog Channel

## Ports

### Input

### **WaveIn** — Input signal scalar | vector

Input signal, specified as a waveform.

**Data Types:** `double`
### Output

### **WaveOut** — Modified output data scalar | vector

Modified output data that includes the effect of a lossy printed circuit board
transmission line model according to the method outlined in [1].

**Data Types:** `double`

## Parameters

### Channel Model

### **Channel model** — Source of channel model `Loss model` (default) | `Impulse response`

Source of channel model.

- Select `Loss model` to model the analog channel from
  a loss model.
- Select `Impulse response` to model the analog channel
  from an impulse response.

#### Programmatic Use

- Use `get_param(gcb,'ChannelType')` to view the current
  **Channel model**.
- Use `set_param(gcb,'ChannelType',value)` to set a
  specific **Channel model**.

### **Target frequency (Hz)** — Frequency for desired channel loss `20e9` (default) | positive real scalar

Frequency for the desired channel loss, specified as a positive real scalar in
hertz. It corresponds to the Nyquist frequency of the system.

#### Dependencies

This parameter is only available when `Loss model` is
selected as **Channel model**.

#### Programmatic Use

- Use `get_param(gcb,'TargetFrequency')` to view the
  current value of **Target frequency (Hz)**.
- Use `set_param(gcb,'TargetFrequency',value)` to set
  **Target frequency (Hz)** to a specific value.

**Data Types:** `double`

### **Loss (dB)** — Channel loss at target frequency `8` (default) | scalar

Channel loss at the target frequency, specified as a scalar in dB.

#### Dependencies

This parameter is only available when `Loss model` is
selected as **Channel model**.

#### Programmatic Use

- Use `get_param(gcb,'Loss')` to view the current value
  of **Loss (dB)**.
- Use `set_param(gcb,'Loss',value)` to set **Loss
  (dB)** to a specific value.

**Data Types:** `double`

### **Impedance (Ohms)** — Channel characteristic impedance positive real scalar

Characteristic impedance of the channel, specified as a positive real scalar in
ohms. **Impedance (Ohms)** depends on the setting of
**Signaling** in the **Configuration** tab in the
SerDes
Designer app or in the Configuration block.

- If **Signaling** is set to
  `Differential`, the default value of
  **Impedance (Ohms)** is `100`.
- If **Signaling** is set to
  `Single-ended`, the default value of
  **Impedance (Ohms)** is `50`.

#### Dependencies

This parameter is only available when `Loss model` is
selected as **Channel model**.

#### Programmatic Use

- Use `get_param(gcb,'Zc')` to view the current value of
  **Impedance**.
- Use `set_param(gcb,'Zc',value)` to set
  **Impedance** to a specific value.

**Data Types:** `double`

### **Impulse response** — User provided impulse response `[zeros(1,63),1/SampleInterval,zeros(1,192)]` (default) | matrix

User provided impulse response, specified as a unitless matrix. **Impulse
response** is used to construct a channel loss model from the user-defined
impulse response of the system.

You can use user specified impulse response to define your own crosstalk. If you
decide to include crosstalk from your custom impulse response, you can specify upto
six crosstalk stimuli as new columns in the impulse response.

#### Dependencies

This parameter is only available when `Impulse
response` is selected as **Channel model**

#### Programmatic Use

- Use `get_param(gcb,'ImpulseResponse')` to view the
  current value of **Impulse response**.
- Use `set_param(gcb,'ImpulseResponse',value)` to set
  **Impulse response** to a specific value.

**Data Types:** `double`

### **Impulse sample interval** — Sample interval of user provided impulse response `6.25e-12` (default) | positive real scalar

Sample interval of the user provided impulse response, specified as a positive
real scalar in seconds.

**Data Types:** `double`

#### Analog Model

### **Tx R (Ohms)** — Single-ended impedance of transmitter analog model `50` (default) | nonnegative real scalar

Single-ended impedance of the transmitter analog model, specified as a nonnegative
real scalar in ohms.

#### Programmatic Use

- Use `get_param(gcb,'TxR')` to view the current value of
  **Tx R (Ohms)**.
- Use `set_param(gcb,'TxR',value)` to set **Tx R
  (Ohms)** to a specific value.

**Data Types:** `double`

### **Tx C (F)** — Capacitance of transmitter analog model `100e-15` (default) | nonnegative real scalar

Capacitance of the transmitter analog model, specified as a nonnegative real
scalar in farads.

#### Programmatic Use

- Use `get_param(gcb,'TxC')` to view the current value of
  **Tx C (F)**.
- Use `set_param(gcb,'TxC',value)` to set **Tx C
  (F)** to a specific value.

**Data Types:** `double`

### **Rx R (Ohms)** — Single-ended impedance of receiver analog model `50` (default) | nonnegative real scalar

Single-ended impedance of the receiver analog model, specified as a nonnegative
real scalar in ohms.

#### Programmatic Use

- Use `get_param(gcb,'RxR')` to view the current value of
  **Rx R (Ohms)**.
- Use `set_param(gcb,'RxR',value)` to set **Rx R
  (Ohms)** to a specific value.

**Data Types:** `double`

### **Rx C (F)** — Capacitance of receiver analog model `200e-15` (default) | nonnegative real scalar

Capacitance of the receiver analog model, specified as a nonnegative real scalar
in farads.

#### Programmatic Use

- Use `get_param(gcb,'RxC')` to view the current value of
  **Rx C (F)**.
- Use `set_param(gcb,'RxC',value)` to set **Rx C
  (F)** to a specific value.

**Data Types:** `double`

### **Rise time (s)** — 20%−80% rise time of stimulus input `10e-12` (default) | positive real scalar

20%−80% rise time of the stimulus input to transmitter analog model, specified as
a positive real scalar in seconds.

#### Programmatic Use

- Use `get_param(gcb,'RiseTime')` to view the current
  value of **Rise time (s)**.
- Use `set_param(gcb,'RiseTime',value)` to set
  **Rise time (s)** to a specific value.

**Data Types:** `double`

### **Voltage (V)** — Peak-to-peak voltage at input of transmitter analog model `1` (default) | positive real scalar

Peak-to-peak voltage at the input of transmitter analog model, specified as a
positive real scalar in volts.

#### Programmatic Use

- Use `get_param(gcb,'VoltageSwingIdeal')` to view the
  current value of **Voltage (V)**.
- Use `set_param(gcb,'VoltageSwingIdeal',value)` to set
  **Voltage (V)** to a specific value.

**Data Types:** `double`

### Crosstalk

### **Include crosstalk** — Include crosstalk in simulation off (default) | on

Select to include crosstalk in the simulation. By default, this option is
deselected.

#### Magnitude

### **Specification** — Specify magnitude of near and far end aggressors `100GBASE-CR4` (default) | `CEI-25G-LR` | `CEI-28G-SR` | `CEI-28G-VSR` | `Custom`

Specify the magnitude of the near and far end aggressors. You can choose to
include maximum allowed crosstalk for specifications such as
`100GBASE-CR4`, `CEI-25G-LR`,
`CEI-28G-SR`, `CEI-28G-VSR`, or
you can specify your own custom crosstalk integrated crosstalk noise (ICN)
level.

#### Programmatic Use

- Use `get_param(gcb,'CrosstalkSpecification')` to view
  the current value of **Specification**.
- Use `set_param(gcb,'CrosstalkSpecification',value)` to
  set **Specification** to a specific value.

### **Far end crosstalk ICN (V)** — Desired integrated noise level of far end aggressor `15e-3` (default) | nonnegative real scalar

Desired integrated crosstalk noise (ICN) level of the far end aggressor, specified
as a nonnegative real scalar in volts. ICN specifies the strength of the
crosstalk.

#### Dependencies

This parameter is only available when you choose
`Custom` as crosstalk
**Specification**.

#### Programmatic Use

- Use `get_param(gcb,'FEXTICN')` to view the current
  value of **Far end crosstalk ICN (V)**.
- Use `set_param(gcb,'FEXTICN',value)` to set
  **Far end crosstalk ICN (V)** to a specific value.

**Data Types:** `double`

### **Near end crosstalk ICN (V)** — Desired integrated noise level of near end aggressor `10e-3` (default) | nonnegative real scalar

Desired integrated crosstalk noise (ICN) level of the near end aggressor,
specified as a nonnegative real scalar in volts. ICN specifies the strength of the
crosstalk.

#### Dependencies

This parameter is only available when you choose
`Custom` as crosstalk
**Specification**.

#### Programmatic Use

- Use `get_param(gcb,'NEXTICN')` to view the current
  value of **Near end crosstalk ICN (V)**.
- Use `set_param(gcb,'NEXTICN',value)` to set
  **Near end crosstalk ICN (V)** to a specific value.

**Data Types:** `double`

#### FEXT Stimulus

### **Symbol Time (s)** — Symbol time of far end crosstalk stimulus `100e-12` (default) | positive real scalar

Symbol time of the far end crosstalk (FEXT) stimulus, specified as a positive real
scalar in seconds.

#### Programmatic Use

- Use `get_param(gcb,'UIFEXT')` to view the current value
  of **Symbol Time (s)** in FEXT stimulus.
- Use `set_param(gcb,'UIFEXT',value)` to set
  **Symbol Time (s)** in FEXT stimulus to a specific
  value.

**Data Types:** `double`

### **Delay (s)** — Delay offset of far end crosstalk stimulus `0` (default) | nonnegative real scalar

Delay offset of the far end crosstalk (FEXT) stimulus, specified as a positive
real scalar in seconds.

#### Programmatic Use

- Use `get_param(gcb,'DelayFEXT')` to view the current
  value of **Delay (s)** in FEXT stimulus.
- Use `set_param(gcb,'DelayFEXT',value)` to set
  **Delay (s)** in FEXT stimulus to a specific value.

**Data Types:** `double`

### **Modulation** — Modulation levels of far end crosstalk stimulus `NRZ` (default) | `PAM3` | `PAM4` | `PAM5` | `PAM6` | `PAM7` | `PAM8` | `PAM9` | `PAM10` | `PAM11` | `PAM12` | `PAM13` | `PAM14` | `PAM15` | `PAM16`

Modulation levels of the far end crosstalk (FEXT) stimulus, specified between
`NRZ` (2-level) and `PAM16`
(16-level).

#### Programmatic Use

- Use `get_param(gcb,'ModulationFEXT')` to view the
  current value of **Modulation** in FEXT stimulus.
- Use `set_param(gcb,'ModulationFEXT',value)` to set
  **Modulation** in FEXT stimulus to a specific value.

### **PRBS Order** — PRBS order of far end crosstalk stimulus `7` (default) | `9` | `11` | `13` | `15` | `20` | `23` | `31` | `47`

Pseudorandom binary sequence (PRBS) order of the far end crosstalk (FEXT)
stimulus.

#### Programmatic Use

- Use `get_param(gcb,'OrderFEXT')` to view the current
  value of **PRBS Order** in FEXT stimulus.
- Use `set_param(gcb,'OrderFEXT',value)` to set
  **PRBS Order** in FEXT stimulus to a specific value.

**Data Types:** `double`

#### NEXT Stimulus

### **Symbol Time (s)** — Symbol time of near end crosstalk stimulus `100e-12` (default) | positive real scalar

Symbol time of the near end crosstalk (NEXT) stimulus, specified as a positive
real scalar in seconds.

#### Programmatic Use

- Use `get_param(gcb,'UINEXT')` to view the current value
  of **Symbol Time (s)** in NEXT stimulus.
- Use `set_param(gcb,'UINEXT',value)` to set
  **Symbol Time (s)** in NEXT stimulus to a specific
  value.

**Data Types:** `double`

### **Delay (s)** — Delay offset of near end crosstalk stimulus `0` (default) | nonnegative real scalar

Delay offset of the near end crosstalk (NEXT) stimulus, specified as a positive
real scalar in seconds.

#### Programmatic Use

- Use `get_param(gcb,'DelayNEXT')` to view the current
  value of **Delay (s)** in NEXT stimulus.
- Use `set_param(gcb,'DelaynEXT',value)` to set
  **Delay (s)** in NEXT stimulus to a specific value.

**Data Types:** `double`

### **Modulation** — Modulation levels of near end crosstalk stimulus `NRZ` (default) | `PAM3` | `PAM4` | `PAM5` | `PAM6` | `PAM7` | `PAM8` | `PAM9` | `PAM10` | `PAM11` | `PAM12` | `PAM13` | `PAM14` | `PAM15` | `PAM16`

Modulation levels of the near end crosstalk (NEXT) stimulus, specified between
`NRZ` (2-level) and `PAM16`
(16-level).

#### Programmatic Use

- Use `get_param(gcb,'ModulationNEXT')` to view the
  current value of **Modulation** in NEXT stimulus.
- Use `set_param(gcb,'ModulationNEXT',value)` to set
  **Modulation** in NEXT stimulus to a specific value.

### **PRBS Order** — PRBS order of near end crosstalk stimulus `9` (default) | `7` | `11` | `13` | `15` | `20` | `23` | `31` | `47`

Pseudorandom binary sequence (PRBS) order of the near end crosstalk (NEXT)
stimulus.

#### Programmatic Use

- Use `get_param(gcb,'OrderFEXT')` to view the current
  value of **PRBS Order** in FEXT stimulus.
- Use `set_param(gcb,'OrderFEXT',value)` to set
  **PRBS Order** in FEXT stimulus to a specific value.

**Data Types:** `double`

## Libraries

SerDes Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Construct loss model from channel loss metric or impulse response

The Analog Channel block constructs a loss model using a channel loss
metric or an impulse response from another source in a SerDes Toolbox™ model. Analog model inputs are only used for IBIS file construction when using
impulse response. For more information, see Analog Channel Loss in SerDes System.
