---
type: simulink-block
title: 'Receiver'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Phased Array Design and Analysis / Transmitters and Receivers'
documentation_page: 'receiverblock'
documentation_source_path: 'ref/receiverblock.html'
language: en
---

# Receiver

## Ports

### Input

### **X** — Received signal complex-valued vector | complex-valued matrix

Received signal voltage, input as a complex-valued vector or complex-valued
matrix. The number of rows is equal to the number of samples.

If **X** is a vector, the number of rows in **Y** equals the
number of rows in `X`.The number of columns in **Y**
equals the number of channels in the receiver.

In the case where **X** is a vector, the number of channels is determined
by the active parameters that indicate a channel number, such as **Noise
figure (dB)**, **Reference temperature (K)**,
**Gain (dB)** and **Phase offset
(degrees)**.

Receiver effects are applied to the signal in a fixed order although some effects
can be omitted. The order in which effects are applied to the input signal:

- Input noise is when the **Add noise to input signal**
  check box is selected.
- System noise is added according to the method specified in **Noise
  method** parameter.
- Signal gain is applied according to the method specified in the
  **Gain method** parameter.
- Phase offset is added to the signal according to **Phase offset
  (degrees)** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **EN** — Enabling signal real-valued vector (default) | real-valued matrix | logical-valued vector | logical-valued matrix

Enabling signal, input as a real-valued vector or matrix or logical-valued vector
or matrix.

- If **EN** is a vector, it must have the same number of rows as the
  input signal matrix in the port **X**. Then, the value in each row of
  **EN** is applied to all the columns of **X**.
- If **EN** is a matrix, **EN** must be the same size as
  **X**, and each element in **EN** is applied to the
  corresponding element in **X**.

If **EN** is of type single or double, when an element of **EN**
is zero,the receiver is turned off, and the input signal is set to zero. When element
of **EN** is nonzero, the receiver is turned on, and the input passes through
the receiver.

If **EN** is logical, the receiver is enabled whenever an element of
**EN** is `true` and disabled whenever an element of
**EN** is `false`.

#### Dependencies

To enable this argument, set the select the **Enable signal enabling
input** check box.

**Data Types:** `double` | `single` | `Boolean`
### Output

### **Y** — Amplified signal complex-valued vector | complex-valued matrix

Amplified received signal voltage, returned as a complex-valued vector or
complex-valued matrix. If **X** is a matrix, the size of **y** is
equal to the size of **X**. The transformation is based on receiver
characteristics, such as the gain, nonlinearity, and noise Power is calculated from
signal voltage assuming a reference impedance of 1 Ohm.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Input Signal

### **Enable signal enabling input** — Enablng signal input `false`0 (default) | `true`1

Select this check box to allow the receiver to accept input though the
**EN** port.

**Example:**

**Data Types:** `Boolean`

### **Add noise to input signal** — Add noise to input signal `off` (default) | `on`

Selected this check box to add noise it the input signal prior to applying receiver
effects. The **Input noise temperature (K)** parameter determines the
power of the added noise. The **Sample rate (Hz)** parameter
determines the noise bandwidth.

**Example:**
`true`

**Data Types:** `Boolean`

### **Input noise temperature (K)** — Input noise temperature `290` (default) | positive scalar | length-*N* vector of positive values

Input noise temperature, specified as a positive scalar or
length-*N* vector of positive values where *N* is
the number of receiver channels. If the **Input noise temperature
(K)** parameter is a scalar, the same value is applied to all channels.
Units are in Kelvin degrees.

**Example:** `300`

#### Dependencies

To enable this parameter, select the **Input noise temperature
(K)** check box.

**Data Types:** `single` | `double`

### **Sample rate (Hz)** — Sample rate `1e6` (default) | positive scalar

Sample rate of the input signal, specified as a positive scalar. Use this parameter
to add noise to the signal. The **Sample rate (Hz)** parameter is
only used to derive the noise bandwidth of the signal.

#### Dependencies

To enable this property, select the **Add noise to input
signal** check box or set the **Noise method**
parameter to `Noise figure`, `Noise
factor`, or `Noise temperature`.

**Data Types:** `single` | `double`

### **Inherit sample rate** — Inherit sample rate from upstream blocks on (default) | off

Select this parameter to inherit the sample rate from upstream blocks. Otherwise,
specify the sample rate using the **Sample rate (Hz)**
parameter.

**Data Types:** `Boolean`

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

When the Simulink model is in `Accelerator` mode, the block mode specified
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

#### System Noise

### **Noise method** — Noise method `None` | `Noise figure` | `Noise factor` | `Noise temperature`

Method for defining the system noise, specified as `None`,
`Noise figure`, `Noise factor` or
`Noise temperature`.

- When set to `None`, no noise is applied.
- When set to `Noise figure`, the **Noise
  figure (dB)** parameter determines the noise level.
- When set to `Noise temperature`, the **Input
  noise temperature (K)** parameter determines the noise level.
- When set to `Noise factor`, the **Noise
  factor** parameter determines the noise level.

The noise bandwidth is derived from the input signal sample rate.

**Example:** `Noise figure`

**Data Types:** `char` | `string`

### **Noise figure (dB)** — Noise figure `3` (default) | real scalar | length-*N* vector or real values

Receiver noise figure, specified as a real scalar or length-*N*
vector of real values. *N* is the number of channels. If
**Noise figure (dB)** is a scalar, the same value is applied to all
channels. Noise is generated with respect to the temperature defined by the
**Reference temperature (K)** parameter.

#### Dependencies

To enable this property, set the **Noise method** parameter to
`Noise figure`.

**Data Types:** `single` | `double`

### **Noise factor** — Noise factor `2` (default) | positive scalar | length-*N* vector of positive values

Receiver noise factor, specified as a positive scalar or length-*N*
vector of positive values. *N* is the number of channels. If the
**Noise factor** parameters is a scalar, the same value is applied
to all channels. Noise is generated with respect to the temperature defined by the
**Reference temperature (K)** parameter.

#### Dependencies

To enable this property, set the **Noise method** parameter to
`Noise factor`.

**Data Types:** `single` | `double`

### **Reference temperature (K)** — Reference temperature `290` (default) | positive scalar | length-*N* vector of positive values

Reference temperature, specified as a positive scalar or a
length-*N* vector of positive values. *N* is the
number of channels. If the **Reference temperature (K)** parameter is
a scalar, the same value is applied to all channels.

#### Dependencies

To enable this property, set the **Noise method** parameter to
`Noise figure` or `Noise
factor`.

**Data Types:** `single` | `double`

#### Gain

### **Gain method** — Gain method `Linear` (default) | `Cubic polynomial` | `Lookup table`

Method for applying gain to the received signal, specified as
`Linear`, `Cubic polynomial` or
`Lookup table`.

- When set to `Linear`, linear gain is applied.
- When set to `Cubic polynomial`, a cubic polynomial
  model is used to apply non-linear gain.
- When set to `Lookup table`, a lookup table is defined
  to directly specify output power and phase shift as a function of input
  power.

**Data Types:** `char` | `string`

### **Gain (dB)** — Linear receiver gain `20` (default) | real scalar | length-*N* vector of real values

Linear receiver gain, specified as a real scalar or length-*N*
vector of real values. *N* is the number of channels. If the
**Gain (dB)** parameter is a scalar, the same value is applied to
all channels. Units are in dB.

#### Dependencies

To enable this property, set the **Gain method** parameter to
`Linear` or `Cubic
polynomial`.

**Data Types:** `single` | `double`

### **Output IP3 (dBm)** — Output IP3 `Inf` (default) | scalar | length-*N* vector of real values

Output IP3 specified as a scalar or length-*N* vector of real
values. *N* is the number of channels. OIP3 expresses the non-linearity
of the transmitter or receiver. OIP is also called the third-order intercept point. If
OIP3 is a scalar, the same value is applied to all channels. See Nonlinearities and Noise in Idealized Baseband Amplifier Block (RF Blockset) for a detailed
discussion of OIP3. Units are in dBm.

#### Dependencies

To enable this property, set the **Gain method** parameter to
`Cubic polynomial`.

**Data Types:** `single` | `double`

### **Lookup table** — Lookup table `[-25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12]` (default) | *M*-by-*N* real-valued matrix | *M*-by-*N* real-valued matrix

Lookup table, specified as a 3-by-*M*-by-*N*
real-valued array. Specify AM/AM (in dB/dB) and AM/PM (in deg/dB) characteristics in a
[Pin(dBm),Pout(dBm),Phase shift(degrees)]-by-*M* or
[Pin(dBm),Pout(dBm),Phase
shift(degrees)]-by-*M*-by-*N* matrix.
*M* is the number of table entries and *N* is the
number of channels. The matrix elements must be real. The column 1 input power must
increase monotonically. There must be at least 3 rows in the table.

#### Dependencies

To enable this property, set the **Gain method** parameter to
`Lookup table`.

**Data Types:** `single` | `double`

#### PhaseOffset

### **Phased offset (degrees)** — Phase offset `0` (default) | scalar | length-*N* vector of real values

Phase offset, specified as a real scalar or length-*N* vector of
real values. *N* is the number of channels. If **Phase offset
(degrees)** is a scalar, the same value is applied to all channels. Units
are in degrees.

**Data Types:** `single` | `double`

#### Randomization

### **Source of seed for random number generator** — Source of seed for random number generator `Auto` (default) | `Property`

Source of seed for random number generator, specified as
`Auto` or `Property`. When source is
`Auto`, the seed if generated automatically. When the source
is `Property`, seed is set using the **Seed for random
number generator** parameter.

**Example:** `Property`

**Data Types:** `char` | `string`

### **Seed for random number generator** — Seed for random number generator 0 (default) | positive integer

Seed for random generator, specified as a positive integer.

**Data Types:** `single` | `double`

## Libraries

Phased Array System Toolbox / Transmitters and Receivers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Receiver

Amplify an input signal with non-linear distortions and added noise.
