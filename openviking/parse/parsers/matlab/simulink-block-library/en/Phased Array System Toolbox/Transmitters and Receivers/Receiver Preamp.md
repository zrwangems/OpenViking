---
type: simulink-block
title: 'Receiver Preamp'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'receiverpreamp'
documentation_source_path: 'ref/receiverpreamp.html'
language: en
---

# Receiver Preamp

## Ports

### Input

### **X** — Input signal complex-valued matrix

Input signal, specified as a complex-valued matrix.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`

### **TR** — Enable enabling signal logical-valued scalar | scalar

Enable enabling signal, specified as a column vector whose length
equals the number of rows in the input signal `X`.
Every element of `TR` that equals
`0` or `false` indicates that the
receiver is turned off, and no input signal passes through the receiver.
Every element of `TR` that is nonzero or
`true` indicates that the receiver is turned on,
and the input signal passes through.

#### Dependencies

To enable this port, select the **Enable enabling signal
input** check box.

**Data Types:** `double` | `Boolean`

### **Ph** — Input phase noise scalar

Phase noise for each input sample of `X`, specified
as a column vector whose length equals the number of rows in
`X`.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

#### Dependencies

To enable this port, select the **Enable phase noise
input** check box.

**Data Types:** `double`
### Output

### **Out 1** — Output complex-valued matrix

Output signal, returned as a complex-valued matrix.

**Data Types:** `double`

## Parameters

### **Gain (dB)** — Gain of receiver `20` (default)

Specify a scalar containing the gain in dB of the receiver
preamplifier.

### **Loss factor (dB)** — Loss factor of receiver `0` (default)

Specify a scalar containing the loss factor in dB of the receiver
preamplifier.

### **Noise specification method** — Noise specification method `Noise temperature` (default) | `Noise power`

Specify the receiver noise as `Noise power` or
`Noise temperature`.

### **Noise power (W)** — Noise power `0` (default)

Specify a scalar containing the noise power in watts at the receiver
preamplifier. If the receiver has multiple channels or sensors, the noise
bandwidth applies to each channel or sensor.

#### Dependencies

This parameter appears only when you set **Noise specification
method** to `Noise power`.

### **Noise figure (dB)** — Noise figure of receiver `0` (default)

Specify a scalar containing the noise figure of the receiver preamplifier.
Units are in dB. If the receiver has multiple channels or sensors, the noise
figure applies to each channel or sensor. This parameter appears only when
you set **Noise specification method** to
`Noise temperature`.

#### Dependencies

This parameter appears only when you set **Noise specification
method** to `Noise
temperature`.

### **Reference temperature (K)** — Reference temperature of receiver `290` (default)

A scalar containing the reference temperature in degrees kelvin of the
receiver preamplifier. If the receiver has multiple channels or sensors, the
reference temperature applies to each channel or sensor.

#### Dependencies

This parameter appears only when you set **Noise specification
method** to `Noise
temperature`.

### **Inherit sample rate** — Inherit sample rate on (default) | off

Select this check box to inherit the sample rate from upstream blocks.
Otherwise, specify the sample rate using the **Sample
rate** parameter.

#### Dependencies

This parameter appears only when you set **Noise specification
method** to `Noise
temperature`.

### **Sample rate (Hz)** — Sampling rate of signal `1e6` (default) | positive real-valued scalar

Specify the signal sampling rate as a positive scalar. Units are in Hz.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate** check
box.

**Data Types:** `double`

### **Enable enabling signal input** — Add input to specify enabling signal off (default) | on

Select this check box to allow input of the receiver-enabling signal via
the input port `TR`. T

#### Dependencies

This parameter appears only when you set **Noise specification
method** to `Noise
temperature`.

### **Enable phase noise input** — Add input to specify phase noise off (default) | on

Select this check box to allow input of phase noise for each incoming
sample using the input port `Ph`. You can use this
information to emulate coherent-on-receive systems.

#### Dependencies

This parameter appears only when you set **Noise specification
method** to `Noise
temperature`.

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The block
runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

When the Simulink® model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** enum |
| **Values:** `Interpreted Execution`, `Code Generation` |
| **Default:** `Interpreted Execution` |

## Libraries

Phased Array System Toolbox / Transmitters and Receivers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Receiver preamplifier

The Receiver Preamp block implements a receiver preamplifier that amplifies an input signal and adds thermal noise. In addition, you can add phase noise using an input port.
