---
type: simulink-block
title: 'Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'amplifier'
documentation_source_path: 'ref/amplifier.html'
language: en
---

# Amplifier

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Source of amplifier gain
  summary: Amplifier gain source Available power gain (default) | Open circuit voltage gain | Data source | Polynomial coefficients
    | AM/AM-AM/PM table
  group: Main
- name: Available power gain
  summary: Available power gain 0 dB (default) | scalar
  group: Main
- name: Open circuit voltage gain
  summary: Open circuit voltage gain 0 dB (default) | scalar
  group: Main
- name: Data source
  summary: Data source Data File (default) | Network-parameters | Rational Model
  group: Main
- name: Polynomial coefficients
  summary: Polynomial coefficients [0 1] (default) | vector
  group: Main
- name: AM/AM-AM/PM table
  summary: Lookup table [ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ] (default) | *M*-by-3 real matrix
  group: Main
- name: Network-parameter object
  summary: Network parameter objects as data source off (default) | on
  group: Main
- name: Network parameter type
  summary: Network parameter type S-parameters (default) | Y-parameters | Z-parameters
  group: Main
- name: Input impedance (Ohm)
  summary: Input impedance 50 (default) | positive scalar
  group: Main
- name: Output impedance (Ohm)
  summary: Output impedance 50 (default) | positive scalar
  group: Main
- name: Data file
  summary: Name of network parameter data file unitygain.s2p (default) | character vector
  group: Main
- name: Frequency (dB)
  summary: Frequency of network parameters 1e9 Hz (default) | scalar | Hz | kHz | MHz | GHz
  group: Main
- name: Reference Impedance(Ohm)
  summary: Reference impedance of network parameters 50 (default) | positive scalar | vector of positive scalars
  group: Main
- name: Use rational object
  summary: Rational object as data source off (default) | on
  group: Main
- name: Residues
  summary: Residues in order of rational model 0 (default) | vector
  group: Main
- name: Poles
  summary: Residues in order of rational model 0 (default) | vector
  group: Main
- name: Direct feedthrough
  summary: Direct feedthrough {0 0:1 0} (default) | array of vectors
  group: Main
- name: Ground and hide negative terminals
  summary: Ground RF circuit terminals on (default) | off
  group: Main
- name: Nonlinear polynomial type
  summary: Type of nonlinearity Even and odd order (default) | Odd order
  group: Nonlinearity
- name: Intercept points convention
  summary: Intercept points convention Output (default) | Input
  group: Nonlinearity
- name: IP2
  summary: Second-order intercept point infdBm (default) | scalar | W | mW | dBW | dBm
  group: Nonlinearity
- name: IP3
  summary: Third-order intercept point infdBm (default) | scalar | W | mW | dBW | dBm
  group: Nonlinearity
- name: 1-dB gain compression power
  summary: 1-dB gain compression power inf dBm (default) | scalar | W | mW | dBW | dBm
  group: Nonlinearity
- name: Output saturation power
  summary: Output saturation power inf dBm (default) | scalar | W | mW | dBW | dBm
  group: Nonlinearity
- name: Gain compression at saturation
  summary: Gain compression at saturation inf dBm (default) | scalar | W | mW | dBW | dBm
  group: Nonlinearity
- name: Use operation frequency at maximum S21 magnitude
  summary: Specify operation frequency off (default) | on
  group: Nonlinearity
- name: Operation frequency
  summary: Operation frequency 1 GHz (default) | scalar | finite vector | Hz | KHz | MHz | GHz
  group: Nonlinearity
- name: Use constant S21 and nonlinearity
  summary: Operation frequency off (default) | on
  group: Nonlinearity
- name: Plot Power Characteristics
  summary: Amplifier nonlinear power curve visualization button (default)
  group: Nonlinearity
- name: Simulate noise
  summary: Simulate thermal noise on (default) | off
  group: Noise
- name: Noise type
  summary: Noise type Noise figure (default) | Spot noise data
  group: Noise
- name: Noise distribution
  summary: Noise distribution White (default) | Piece-wise linear | Colored
  group: Noise
- name: Noise figure (dB)
  summary: Noise figure 0 (default) | scalar
  group: Noise
- name: Frequencies
  summary: Frequency data 0 Hz (default) | real scalar | finite vector
  group: Noise
- name: Minimum noise figure (dB)
  summary: Minimum noise figure 0 (default) | scalar | finite vector
  group: Noise
- name: Optimal reflection coefficient
  summary: Optimal reflection coefficient 0 (default) | scalar | finite vector
  group: Noise
- name: Equivalent normalized noise resistance
  summary: Equivalent normalized noise resistance 0 (default) | scalar | finite vector
  group: Noise
- name: Automatically estimate impulse response duration
  summary: Automatically estimate impulse response duration on (default) | off
  group: Noise
- name: Impulse response duration
  summary: Impulse response duration 1e-10s (default) | scalar
  group: Noise
- name: Modeling options
  summary: Model S-parameters Time domain (default) | Frequency domain
  group: Modeling
- name: Fitting options
  summary: Rationalfit fitting options Fit individually (default) | Share poles by column | Share all poles
  group: Modeling
- name: Relative error desired (dB)
  summary: Relative error acceptable for the rational fit -40 (default) | scalar
  group: Modeling
- name: Automatically estimate impulse response duration
  summary: Automatically calculate impulse response on | off
  group: Modeling
- name: Impulse response duration
  summary: Impulse response duration 1e-10 (default) | scalar
  group: Modeling
- name: Use only S-parameter magnitude with appropriate delay
  summary: Use only S-parameter magnitude with appropriate delay off (default) | on
  group: Modeling
- name: Source of frequency data
  summary: Frequency data source Extracted from data source (default) | User-defined
  group: Visualization
- name: Frequency data
  summary: Frequency data range [1e9:1e6:3e9] (default) | finite vector | Hz | kHz | MHz | GHz
  group: Visualization
- name: Plot type
  summary: Type of data plot X-Y plane (default) | Polar plane | Z Smith chart | Y Smith chart | ZY Smith chart
  group: Visualization
- name: Parameter 1
  summary: Type of S-Parameters to plot S11 (default) | S12 | S21 | S22 | NF
  group: Visualization
- name: Parameter 2
  summary: Type of S-Parameters to plot None (default) | S11 | S12 | S21 | S22 | NF
  group: Visualization
- name: Format1
  summary: Plot format Magnitude (decibels) (default) | Magnitude (linear) | Angle(degrees) | Real | Imaginary
  group: Visualization
- name: Format2
  summary: Plot format Magnitude (decibels) (default) | Magnitude (linear) | Angle(degrees) | Real | Imaginary
  group: Visualization
- name: Y-axis scale
  summary: Y-axis scale Linear (default) | Logarithmic
  group: Visualization
- name: X-axis scale
  summary: X-axis scale Linear (default) | Logarithmic
  group: Visualization
- name: Plot
  summary: Plot specified data button
  group: Visualization
```

### Main

### **Source of amplifier gain** — Amplifier gain source `Available power gain` (default) | `Open circuit voltage gain` | `Data source` | `Polynomial coefficients` | `AM/AM-AM/PM table`

Source of the amplifier gain, specified as one of the following:

- `Available power gain` —
  The block uses the **Available power gain** parameter to
  calculate *a1*, the
  linear voltage gain term of the polynomial VCVS. This
  calculation assumes a matched load termination for the
  amplifier.
- `Open circuit voltage gain`
  — The block uses the **Open circuit voltage gain** parameter to
  calculate *a1*, the
  linear voltage gain term of the polynomial VCVS.
- `Data source` — The block
  uses the **Data
  source** parameter to calculate the linear
  voltage gain. When you use the data source option, the block
  uses *S*11 and
  *S*22 as the
  input and output impedances.
- `Polynomial coefficients`
  — The block uses the **Polynomial coefficients** parameter to
  calculate the nonlinear voltage gain.
- `AM/AM-AM/PM table` — The
  block uses the **AM/AM-AM/PM table** parameter to determine
  the power characteristics of the amplifier.

### **Available power gain** — Available power gain 0 `dB` (default) | scalar

Available power gain of amplifier, specified as a scalar in dB.
Specify the units from the corresponding drop-down list.

#### Dependencies

To enable this parameter, choose `Available power
gain` in the **Source of amplifier
gain** tab.

### **Open circuit voltage gain** — Open circuit voltage gain 0 `dB` (default) | scalar

Open circuit voltage of amplifier, specified as a scalar in dB.
Specify the units from the corresponding drop-down list.

#### Dependencies

To enable this parameter, choose `Open circuit voltage
gain` in the **Source of amplifier
gain** tab.

### **Data source** — Data source `Data File` (default) | `Network-parameters` | `Rational Model`

Data source, specified as one of the following:

- `Data file` — Name of a
  Touchstone file with the extension`.s2p`.
- `Network-parameters` —
  Provide **Network parameter** data such as
  `S-parameters`,
  `Y-parameters`, and
  `Z-parameters` with
  corresponding **Frequency** and
  **Reference impedance (ohms)** for the
  amplifier.
- `Rational model` — Provide
  values for **Residues**,
  **Poles**, and **Direct
  feedthrough** parameters which correspond to
  the equation for a rational model

  F(s)=(∑k=1nCks−Ak+D),s=j2πf

  In this rational model equation, each
  *Ck* is the
  residue of the pole
  *Ak*. If
  *Ck* is
  complex, a corresponding complex conjugate pole and residue
  must also be enumerated. This object has the properties
  `C`, `A`, and
  `D`. You can use these properties to
  specify the **Residues**,
  **Poles**, and **Direct
  feedthrough** parameters.

When the amplifier is nonlinear, the nonlinearity applies only to the
S21 term of the scattering parameters representing the 2-port element.
In this case, S21 is frequency-independent with its constant value being
either the maximal value of S21, or the S21 value at an Operation
frequency specified by the user. The other scattering parameters, S11,
S12, and S22 remain the same as in the linear case.

#### Dependencies

To enable this parameter, select `Data
source` in **Source of amplifier
gain** tab.

### **Polynomial coefficients** — Polynomial coefficients `[0 1]` (default) | vector

Order of polynomial, specified as a vector.

The order of the polynomial must be less than or equal to 9. The
coefficients are ordered in ascending powers. If a vector has 10
coefficients,
`[a0,a1,a2,
... a9]`,
the polynomial it represents is:

*Vout* = *a*0 + *a*1*Vin* + *a*2*Vin*2 + ...
 + *a*9*Vin*9

where
*a*1 represents the linear
gain term, and higher-order terms are modeled according to [1].

For example, the vector
`[a0,a1,a2,a3]`
specifies the relation *Vout* = *a*0 + *a*1*V1* + *a*2*V1*2 + *a*3*V1*3. Trailing zeroes are omitted. So,
`[a0,a1,a2]`
defines the same polynomial as
`[a0,a1,a2,
0]`. The default value of this parameter is [0,1],
corresponding to the linear relation
*Vout* =
*Vin*.

#### Dependencies

To enable this parameter, select `Polynomial
coefficients` in **Source of amplifier
gain** tab.

### **AM/AM-AM/PM table** — Lookup table `[ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ]` (default) | *M*-by-3 real matrix

Table lookup entries specified as a real *M*-by-3
matrix. The second column of the matrix represents the AM/AM–AM/PM model
output power in dBm. The third column represents the model phase change
in degrees. The second and third column values are related to the
absolute value of the power of the input signal represented in the first
column of matrix. The input power in the first column must increase
monotonically.

#### Dependencies

To enable this parameter, set **Source of amplifier
gain** to `AM/AM - AM/PM
table`.

### **Network-parameter object** — Network parameter objects as data source `off` (default) | `on`

Select this parameter to use a network parameter object as the source
of amplifier gain.

Once you select this parameter, in the text box that opens, specify
one of these:

- Network parameter object.
- MATLAB® base workspace variable or a Simulink® model workspace variable. The block evaluates
  if the specified variable is a network parameter
  object.

The network parameter objects that you can specify include:

- `sparameters`
- `yparameters`
- `zparameters`
- `gparameters`
- `hparameters`
- `abcdparameters`
- `tparameters`

#### Dependencies

To enable this parameter, first select `Data
source` in **Source of amplifier
gain**, and then select
`Network-parameters` in **Data
source**.

### **Network parameter type** — Network parameter type `S-parameters` (default) | `Y-parameters` | `Z-parameters`

Network parameter type, specified as `S-parameters`,
`Y-parameters`, or
`Z-parameters`.

#### Dependencies

To enable this parameter, first select `Data
source` in **Source of amplifier
gain** and then, select
`Network-parameters` in the
**Data source**.

### **Input impedance (Ohm)** — Input impedance `50` (default) | positive scalar

Input impedance of amplifier, specified as a positive scalar in ohms.

#### Dependencies

To enable this parameter, select `Available power
gain`, `Open circuit voltage
gain`, or `Polynomial
coefficients` in **Source of amplifier
gain**.

### **Output impedance (Ohm)** — Output impedance `50` (default) | positive scalar

Output impedance of amplifier, specified as a positive scalar in ohms.

#### Dependencies

To enable this parameter, select `Available power
gain`, `Open circuit voltage
gain`, or `Polynomial
coefficients` in **Source of amplifier
gain**.

### **Data file** — Name of network parameter data file `unitygain.s2p` (default) | character vector

Name of network parameter data file, specified as a character vector.

#### Dependencies

To enable this parameter, first select `Data
source` in **Source of amplifier
gain** and then, select `Data
file` in **Data source**.

### **Frequency (dB)** — Frequency of network parameters `1e9 Hz` (default) | scalar | `Hz` | `kHz` | `MHz` | `GHz`

Frequency of network parameters, specified as a scalar in Hz.

#### Dependencies

To enable this parameter, first select `Data
source` in **Source of amplifier
gain** and then, select
`Network-parameters` in **Data
source**.

### **Reference Impedance(Ohm)** — Reference impedance of network parameters `50` (default) | positive scalar | vector of positive scalars

Reference impedance of network parameters, specified as a positive
scalar or vector of positive scalars in ohms.

**Note**

The reference impedance of all the ports must be equal when
you specify it as a vector of positive scalars.

#### Dependencies

To enable this parameter, first select `Data
source` in **Source of amplifier
gain** and then, select
`Network-parameters` in **Data
source**.

### **Use rational object** — Rational object as data source `off` (default) | `on`

Select this parameter to use a `rational` object as the
data source to model amplifier gain.

Once you select this parameter, in the text box that opens, specify
one of these:

- `rational` object.
- MATLAB base workspace variable or a Simulink model workspace variable. The block evaluates
  if the specified variable is a rational object."

The `rational` objects that you can specify include:

- `rational`
- `rationalfit`
- `rfmodel.rational`

#### Dependencies

To enable this parameter, first select `Data
source` in **Source of amplifier
gain**, and then select `Rational
model` in **Data source**.

### **Residues** — Residues in order of rational model `0` (default) | vector

Residues in order of rational model, specified as a vector.

#### Dependencies

To enable this parameter, first select `Data
source` in **Source of amplifier
gain** and then, select `Rational
model` in **Data source**.

### **Poles** — Residues in order of rational model `0` (default) | vector

Poles in order of rational model, specified as a vector.

#### Dependencies

To enable this parameter, first select `Data
source` in **Source of amplifier
gain** and then, select `Rational
model` in **Data source**.

### **Direct feedthrough** — Direct feedthrough `{0 0:1 0}` (default) | array of vectors

Direct feedthrough, specified as an array vector.

#### Dependencies

To enable this parameter, first select `Data
source` in **Source of amplifier
gain** and then, select `Rational
model` in **Data source**.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select this option to ground and hide the negative terminals. Clear
this parameter to expose the negative terminals. By exposing these
terminals, you can connect them to other parts of your model.

By default, this option is selected.

### Nonlinearity

### **Nonlinear polynomial type** — Type of nonlinearity `Even and odd order` (default) | `Odd order`

Type of nonlinearity, specified as `Even and odd
order` or `Odd order`.

- When you select `Even and odd order`,
  the amplifier can produce second- and third-order
  intermodulation frequencies in addition to a linear term.
- When you select `Odd order`, the
  amplifier generates only odd order intermodulation
  frequencies.

  The linear gain determines the linear
  *a*1 term. The block
  calculates the remaining terms from the specified parameters.
  These parameters are **IP3**, **1-dB
  gain compression power**, **Output
  saturation power**, and **Gain compression
  at saturation**. The number of constraints you
  specify determines the order of the model. The figure shows the
  graphical definition of the nonlinear amplifier parameters.

  Po vs. Pi plot to represent nonlinear amplifier parameters.

### **Intercept points convention** — Intercept points convention `Output` (default) | `Input`

Intercept points convention, specified a
`Input`-referred, or
`Output`-referred convention. Use this
specification for the intercept points, 1-dB gain compression power, and
saturation power.

### **IP2** — Second-order intercept point `inf``dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

Second-order intercept point, specified as a scalar.

#### Dependencies

To set this parameter, select `Even and odd
order` in **Nonlinear polynomial
type**.

### **IP3** — Third-order intercept point `inf``dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

Third-order intercept point, specified as a scalar.

### **1-dB gain compression power** — 1-dB gain compression power `inf dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

1-dB gain compression power, specified as a scalar.

#### Dependencies

To set this parameter, select `Odd order`
in **Nonlinear polynomial type**.

### **Output saturation power** — Output saturation power `inf dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

Output saturation power, specified as scalar. The block uses this
value to calculate the voltage saturation point used in the nonlinear
model. In this case, the first derivative of the polynomial is zero, and
the second derivative is negative.

#### Dependencies

To set this parameter, select `Odd order`
in **Nonlinear polynomial type**.

### **Gain compression at saturation** — Gain compression at saturation `inf dBm` (default) | scalar | `W` | `mW` | `dBW` | `dBm`

Gain compression at saturation, specified as scalar.

When **Nonlinear polynomial type** is
`Odd order`, specify the gain compression
at saturation.

#### Dependencies

To set this parameter, first select `Odd
order` in **Nonlinear polynomial
type**. Then, change the default value of
**Output saturation power**.

### **Use operation frequency at maximum S21 magnitude** — Specify operation frequency `off` (default) | `on`

Select this parameter to specify operation frequency at the maximum
magnitude of S21.

#### Dependencies

To enable this parameter:

- First, choose `Data source`
  in the **Source of amplifier gain**
  parameter on the**Main** tab.
- Second, specify the nonlinearity in the
  **Nonlinearity** tab.
- And finally, click the **Apply**
  button.

### **Operation frequency** — Operation frequency `1 GHz` (default) | scalar | finite vector | `Hz` | `KHz` | `MHz` | `GHz`

Operation frequency, specified as a scalar or finite vector.

#### Dependencies

To enable this parameter:

- First, choose `Data source`
  in the **Source of amplifier gain**
  parameter on the**Main** tab.
- Second, specify the nonlinearity in the
  **Nonlinearity** tab.
- And finally, click the **Apply**
  button.

**Note**

If the **Use constant S21 and
nonlinearity** parameter is selected, clear
this parameter to enable the **Operation
frequency** parameter.

### **Use constant S21 and nonlinearity** — Operation frequency `off` (default) | `on`

Select this parameter to use the constant magnitude of S21 and
nonlinearity in your amplifier model.

#### Dependencies

To enable this parameter:

- First, choose `Data source`
  in the **Source of amplifier gain**
  parameter on the**Main** tab.
- Second, specify the nonlinearity in the
  **Nonlinearity** tab.
- And finally, click the **Apply**
  button.

### **Plot Power Characteristics** — Amplifier nonlinear power curve visualization button (default)

Use this button to plot the power characteristics of the amplifier
based on the nonlinearity parameters specified on the
**Nonlinearity** tab. When you clear the
**Use
constant S21 and nonlinearity** parameter, the power
curve reflects the amplifier power measured at the frequency specified
in the **Operation frequency** parameter.

#### Dependencies

To enable this parameter, set **Source of amplifier
gain** in the **Main** tab to
`Available power gain`,
`Open circuit voltage gain`, or
`Data source`.

### Noise

### **Simulate noise** — Simulate thermal noise `on` (default) | `off`

Select this parameter, to simulate noise as specified in block
parameters or on file.

If the noise is specified in an `.s2p` file, then it
is used for simulation.

### **Noise type** — Noise type `Noise figure` (default) | `Spot noise data`

Noise type, specified as `Noise figure` or
`Spot noise data`.

### **Noise distribution** — Noise distribution `White` (default) | `Piece-wise linear` | `Colored`

Noise distribution, specified as:

- `White`, spectral density is a
  single non-negative value. The power value of the noise
  depends on the bandwidth of the carrier and the bandwidth
  depends on the time step. This is an uncorrelated noise
  source.
- `Piece-wise linear`, spectral
  density is a vector of values [pi].
  For each carrier, the noise source behaves like a white
  uncorrelated noise. The power of the noise source is
  carrier-dependent.
- `Colored`, depends on both
  carrier and bandwidth. This is a correlated noise
  source.

### **Noise figure (dB)** — Noise figure 0 (default) | scalar

Noise figure, specified as a scalar in decibels.

### **Frequencies** — Frequency data `0 Hz` (default) | real scalar | finite vector

Frequency data, specified as a real scalar or finite vector in Hz,
kHz, MHz, or GHz.

#### Dependencies

To set this parameter, first select `Piece-wise
linear` or `Colored` in
**Noise distribution**.

### **Minimum noise figure (dB)** — Minimum noise figure `0` (default) | scalar | finite vector

Minimum noise figure, specified as a scalar or finite vector in
decibels.

#### Dependencies

To set this parameter, first select `Spot noise
data` in **Noise type**.

### **Optimal reflection coefficient** — Optimal reflection coefficient `0` (default) | scalar | finite vector

Optimal reflection coefficient, specified as a scalar or a finite
vector.

#### Dependencies

To set this parameter, first select `Spot noise
data` in **Noise type**.

### **Equivalent normalized noise resistance** — Equivalent normalized noise resistance `0` (default) | scalar | finite vector

Equivalent normalized noise resistance, specified as a scalar or
finite vector.

#### Dependencies

To set this parameter, first select `Spot noise
data` in **Noise type**.

### **Automatically estimate impulse response duration** — Automatically estimate impulse response duration `on` (default) | `off`

Select this parameter to automatically calculate impulse response for
frequency dependent noises. Clear this parameter to manually specify the
impulse response duration using **Impulse response
duration**. You cannot specify impulse response when
amplifier is nonlinear, as in this case noise is simulated as
white-noise.

#### Dependencies

To set this parameter, first select
`Colored` in **Noise
distribution**.

### **Impulse response duration** — Impulse response duration `1e-10``s` (default) | scalar

Impulse response duration used to simulate frequency dependent noise,
specified as a scalar in seconds. You cannot specify impulse response if
the amplifier is nonlinear.

#### Dependencies

To set this parameter, first clear **Automatically
estimate impulse response duration**.

### Modeling

### **Modeling options** — Model S-parameters `Time domain` (default) | `Frequency domain`

Model S-parameters, specified as:

- `Time domain` technique creates
  an analytical rational model that approximates the whole
  range of the data. When modeling using `Time
  domain`, the **Plot** in
  `Visualization` tab plots the data
  defined in `Data Source` and the values in
  the `rationalfit` function.
- `Frequency domain` computes the
  baseband impulse response for each carrier frequency
  independently. This technique is based on convolution. There
  is an option to specify the duration of the impulse
  response. For more information, see Compare Time and Frequency Domain Simulation Options for S-parameters.
- For the Amplifier, Antenna, and S-Parameters
  blocks, the default value is `Time
  domain`. For the Transmission Line block, the default value is
  `Frequency domain`.

#### Dependencies

To set this parameter, first select `Data
source` in **Source of amplifier
gain**. This selection activates the
**Modeling** Tab which contains
**Modeling options**

### **Fitting options** — Rationalfit fitting options `Fit individually` (default) | `Share poles by column` | `Share all poles`

Rationalfit fitting options, specified as `Fit
individually`, `Share poles by
column`, or `Share all
poles`.

**Rational fitting results** shows values of
**Number of independent fits**, **Number of
required poles**, and **Relative error achieved
(dB)**.

#### Dependencies

To set this parameter, select `Time
domain` in **Modeling options**.

### **Relative error desired (dB)** — Relative error acceptable for the rational fit `-40` (default) | scalar

Relative error acceptable for the rational fit, specified as a scalar
in decibels.

#### Dependencies

To set this parameter, select `Time
domain` in **Modeling options**.

### **Automatically estimate impulse response duration** — Automatically calculate impulse response `on` | `off`

Select this parameter to automatically calculate impulse response.
Clear this parameter to manually specify the impulse response duration
using **Impulse response duration**.

#### Dependencies

To set this parameter, select `Frequency
domain` in **Modeling options**.

### **Impulse response duration** — Impulse response duration `1e-10` (default) | scalar

Impulse response duration, specified as a scalar in seconds.

#### Dependencies

To set this parameter, first select `Frequency
domain` in **Modeling options**.
Then, clear `Automatically estimate impulse response
duration`.

### **Use only S-parameter magnitude with appropriate delay** — Use only S-parameter magnitude with appropriate delay `off` (default) | `on`

Select this parameter to S-parameter phase and delay the impulse
response by half its length. This parameter is applicable only for
S-parameter data modeled in time domain. You can use this parameter to
shape spectral content with filter effects by specifying only
magnitude.

**Note**

This parameter introduces an artificial delay to the
system.

### Visualization

### **Source of frequency data** — Frequency data source `Extracted from data source` (default) | `User-defined`

Frequency data source, specified as:

When **Source of frequency data** is
`Extracted from data source`, the
**Data source** must be set to `Data
file`. Verify that the specified **Data
file** contains frequency data.

When **Source of frequency data** is
`User-specified`, specify a vector of
frequencies in the **Frequency data** parameter. Also,
specify units from the corresponding drop-down list.

#### Dependencies

To set this parameter, first select `Data
source` in **Source of amplifier
gain**. This selection activates the
**Visualization** Tab which contains
**Source of frequency data**

### **Frequency data** — Frequency data range `[1e9:1e6:3e9]` (default) | finite vector | `Hz` | `kHz` | `MHz` | `GHz`

Frequency data range, specified as a finite vector.

#### Dependencies

To enable this parameter, set **Source of frequency
data** to
`User-specified`.

### **Plot type** — Type of data plot `X-Y plane` (default) | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

Type of data plot that you want to produce with your data specified as
one of the following:

- `X-Y plane` — Generate a
  Cartesian plot of your data versus frequency. To create linear,
  semilog, or log-log plots, set the **Y-axis
  scale** and **X-axis scale**
  accordingly.
- `Polar plane` — Generate a
  polar plot of your data. The block plots only the range of data
  corresponding to the specified frequencies.
- `Z smith chart`, `Y smith
  chart`, and `ZY smith
  chart` — Generate a Smith® chart. The block plots
  only the range of data corresponding to the specified
  frequencies.

### **Parameter 1** — Type of S-Parameters to plot `S11` (default) | `S12` | `S21` | `S22` | `NF`

Type of S-Parameters to plot, specified as `S11`,
`S12`, `S21`, or
`S22`. When noise is spectral `NF`
plotting is possible.

#### Dependencies

To enable `NF`, set **Noise
type** to `Noise figure` and
select **Apply**.

### **Parameter 2** — Type of S-Parameters to plot `None` (default) | `S11` | `S12` | `S21` | `S22` | `NF`

Type of S-Parameters to plot, specified as `S11`,
`S12`, `S21`, or
`S22`. When noise is spectral `NF`
plotting is possible.

#### Dependencies

To enable `NF`, set **Noise
distribution** to `Piece-wise
linear` or `Colored` and
select **Apply**.

### **Format1** — Plot format `Magnitude (decibels)` (default) | `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

Plot format, specified as `Magnitude (decibels)`,
`Angle(degrees)`, `Real`, or
`Imaginary`.

#### Dependencies

To enable this parameter, set **Plot type** to
`X-Y plane`.

### **Format2** — Plot format `Magnitude (decibels)` (default) | `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

Plot format, specified as `Magnitude (decibels)`,
`Angle(degrees)`, `Real`, or
`Imaginary`.

#### Dependencies

To enable this parameter, set **Plot type** to
`X-Y plane`.

### **Y-axis scale** — Y-axis scale `Linear` (default) | `Logarithmic`

Y-axis scale, specified as `Linear` or
`Logarithmic`.

#### Dependencies

To enable this parameter, set **Plot type** to
`X-Y plane`.

### **X-axis scale** — X-axis scale `Linear` (default) | `Logarithmic`

X-axis scale, specified as `Linear` or
`Logarithmic`.

#### Dependencies

To enable this parameter, set **Plot type** to
`X-Y plane`.

### **Plot** — Plot specified data button

Plot specified data using plot button.
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2010b**

### R2025a: Improved polynomial model to compute nonlinearity

The Amplifier block now supports the improved polynomial model to
compute nonlinearity that better adheres to user specification.

When you open a model created before R2025a containing the
Amplifier block, the software uses the improved polynomial model
to compute nonlinearity and numerical results may be different.

### R2024b: `Time domain (rationalfit)` parameter renamed

The `Time domain (rationalfit)` parameter value in the
**Modeling options** parameter has been renamed to
`Time domain` in the Amplifier
block.

When you open a model created before R2024b containing an Amplifier
block, the parameter name displays as `Time domain`.

### R2022b: Three new parameters added

The Amplifier block has three new parameters.

- **Network-parameter object** — Use this parameter to
  specify a network parameter object as the source of amplifier gain.
- **Use
  rational object** — Use this parameter to specify a
  `rational` object as the source of amplifier gain.
- **Plot
  power characteristics** — Use this button to plot the
  power characteristics of an amplifier based on the specified
  nonlinearities.

### R2022b: Two block parameters renamed

The **Pick operation frequency at maximum S21 magnitude** and
**Frequency data** parameters have been renamed to **Use operation
frequency at maximum S21 magnitude** and **Source of frequency
data**, respectively.

When you open a model created before R2022b containing the
Amplifier block, the software replaces the old parameter names
with the new names.

### R2022a: Modeling noise in nonlinear circuit envelope amplifier

The Amplifier block now enables you to model frequency-dependent
noise as colored noise when your amplifier operates in a nonlinear region.

When you open a model created before R2022a containing the
Amplifier block operating in a nonlinear region with
frequency-dependent noise, the software models the noise as specified in the
block.

### R2022a: Two new parameters added

The Amplifier block has two new parameters.

- **AM/AM-AM/PM table** — Use this parameter to specify
  amplifier power characteristics using AM/AM-AM/PM table.
- **Use
  constant S21 and nonlinearity** — Use this parameter to
  model frequency-dependent gain (S21) when operating in a nonlinear
  region.

### R2021b: Amplifier block icon updated

Starting in R2021b, the Amplifier block icon has updated. The block
icon is now dynamic and shows the current state of the noise parameter.

When you open a model created before R2021b containing an Amplifier
block, the software replaces the block icon with the R2021b version.

## Description

Model amplifier in RF systems

Use the Amplifier block to model a linear or
nonlinear amplifier, with or without noise. Defining the amplifier
gain using a data source also defines input data visualization and
modeling. Use the **Main** tab parameters to specify
amplifier gain and noise using data sheet values, standard `s2p` files,
S-parameters, or circuit envelope polynomial coefficients.

The amplifier is implemented as a polynomial, voltage-controlled voltage source (VCVS) except
when the amplifier gain is obtained from a `Data source`. The
VCVS includes nonlinearities that are described using parameters listed in the
**Nonlinearity** tab. To model linear amplification, the amplifier
implements the relation *V*out =
a1\**V*in between the input and output voltages. The input voltage is *V*i(*t*) =
*A*i(*t*)ejωt, and the output voltage is *V*o(*t*) =
*A*o(*t*)ejωt at each carrier *w* = 2π*f* in the RF Blockset™ environment.

In case the amplifier gain is obtained from a data source, amplifier implementation is
based on S-parameter data. Nonlinear amplification is modeled as a polynomial (with the
saturation power computed automatically). It also produces additional intermodulation
frequencies.

Amplifier block mask icons are dynamic and show the current state of
the applied noise parameter. This table shows you how the icons on this block vary based
on the state of the **Noise figure (dB)** parameter on the
block.

| Noise Figure (dB): `10` | Noise Figure (dB): `0` |
| --- | --- |
| Amplifier block icon with Noise figure (dB) is set to 10. | Amplifier block icon with Noise figure (dB) is set to 0. |
