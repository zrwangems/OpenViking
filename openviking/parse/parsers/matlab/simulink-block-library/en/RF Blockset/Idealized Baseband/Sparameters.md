---
type: simulink-block
title: 'S-Parameters'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'sparameters'
documentation_source_path: 'ref/sparameters.html'
language: en
---

# S-Parameters

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Data source
  summary: Data source Data file (default) | Network-parameters | Rational model
  group: ''
- name: Data file
  summary: Name of network parameter data file simrfV2_unitygain.s2p (default) | character vector
  group: ''
- name: Network-parameter object
  summary: Network parameter objects as data source off (default) | on
  group: ''
- name: Network parameter type
  summary: Network parameter type S-parameters (default) | Y-parameters | Z-parameters
  group: ''
- name: Network-parameters
  summary: Network parameter values [0 0;1 0] (default) | multidimensional array | scalar
  group: ''
- name: Frequency (dB)
  summary: Frequency of network parameters 1e9 Hz (default) | scalar | vector | Hz | kHz | MHz | GHz
  group: ''
- name: Reference Impedance(Ohm)
  summary: Reference impedance of network parameters 50 (default) | positive scalar | vector of positive scalars
  group: ''
- name: Use rational object
  summary: Rational object as data source off (default) | on
  group: ''
- name: Residues
  summary: Residues in order of rational model 0 (default) | vector
  group: ''
- name: Poles
  summary: Residues in order of rational model 0 (default) | vector
  group: ''
- name: Direct feedthrough
  summary: Direct feedthrough {0 0:1 0} (default) | array of vectors
  group: ''
- name: Simulate noise
  summary: Simulate thermal noise waves off (default) | on
  group: ''
- name: Ground and hide negative terminals
  summary: Ground RF circuit terminals on (default) | off
  group: ''
- name: Modeling options
  summary: Model S-parameters Time domain (default) | Frequency domain
  group: ''
- name: Fitting options
  summary: Rational fit fitting options Fit individually (default) | Share poles by column | Share all poles
  group: ''
- name: Relative error desired (dB)
  summary: Relative error acceptable for the rational fit -40 (default) | scalar
  group: ''
- name: Maximum number of poles
  summary: Maximum number of poles 48 (default) | positive scalar
  group: ''
- name: Automatically estimate impulse response duration
  summary: Automatically calculate impulse response on | off
  group: ''
- name: Impulse response duration
  summary: Impulse response duration 1e-10 (default) | scalar
  group: ''
- name: Use only S-parameter magnitude with appropriate delay
  summary: Use only S-parameter magnitude with appropriate delay off (default) | on
  group: ''
- name: Source of frequency data
  summary: Frequency data source Extracted from data source (default) | User-defined
  group: ''
- name: Frequency data
  summary: Frequency data range [1e9:1e6:3e9] Hz (default) | vector | scalar
  group: ''
- name: Plot type
  summary: Type of data plot X-Y plane (default) | Polar plane | Z Smith chart | Y Smith chart | ZY Smith chart
  group: ''
- name: Parameter 1
  summary: Type of S-Parameters to plot S11 (default) | SNN
  group: ''
- name: Parameter 2
  summary: Type of S-Parameters to plot None (default) | SNN
  group: ''
- name: Format1
  summary: Plot format Magnitude (decibels) (default) | Angle(degrees) | Real | Imaginary
  group: ''
- name: Format2
  summary: Plot format Magnitude (decibels) (default) | Angle(degrees) | Real | Imaginary
  group: ''
- name: Y-axis scale
  summary: Y-axis scale Linear (default) | Logarithmic
  group: ''
- name: X-axis scale
  summary: X-axis scale Linear (default) | Logarithmic
  group: ''
- name: Plot
  summary: Plot specified data button
  group: ''
```

#### Main

### **Data source** — Data source `Data file` (default) | `Network-parameters` | `Rational model`

Data source for S-parameters behavior, specified as one of the
following:

- `Data file` — Name
  of a Touchstone file with the extension`.s2p`. The
  block ignores noise and nonlinearity data in imported files.
- `Network-parameters` —
  Provide **Network parameter** data such as `S-parameters`, `Y-parameters`,
  and `Z-parameters` with corresponding **Frequency** and **Reference
  impedance (ohms)** for the s-parameters.
- `Rational model` —
  Provide values for **Residues**, **Poles**,
  and **Direct feedthrough** parameters which correspond
  to the equation for a rational model

  F(s)=(∑k=1nCks−Ak+D),s=j2πf

  .In this rational model
  equation, each *Ck* is the
  residue of the pole *Ak*.
  If *Ck* is complex, a corresponding
  complex conjugate pole and residue must also be enumerated. This object
  has the properties `C`, `A`, and `D`.
  You can use these properties to specify the **Residues**, **Poles**,
  and **Direct feedthrough** parameters.

### **Data file** — Name of network parameter data file `simrfV2_unitygain.s2p` (default) | character vector

Name of network parameter data file, specified as a character
vector.

#### Dependencies

To enable this parameter, select `Data file` in **Data
source** tab.

### **Network-parameter object** — Network parameter objects as data source `off` (default) | `on`

Select this parameter to use a network parameter object as the data source
to model the S-parameters.

Once you select this parameter, in the text box that opens, specify one of
these:

- Network parameter object.
- MATLAB® base workspace variable or a Simulink® model workspace variable. The block evaluates if
  the specified variable is a network parameter object.

`sparameters('default.s2p')` is the default network
parameter object when you select this parameter.

The network parameter objects that you can specify include:

- `sparameters`
- `yparameters`
- `zparameters`
- `gparameters`
- `hparameters`
- `abcdparameters`
- `tparameters`

#### Dependencies

To enable this parameter, set **Data source** to
`Network-parameters`.

### **Network parameter type** — Network parameter type `S-parameters` (default) | `Y-parameters` | `Z-parameters`

Network parameter type, specified as `S-parameters`, `Y-parameters`,
or `Z-parameters`.

#### Dependencies

To enable this parameter, set **Data source** to
`Network-parameters`.

### **Network-parameters** — Network parameter values `[0 0;1 0]` (default) | multidimensional array | scalar

Network parameter values specified as a multidimensional array or a scalar. When you specify
**Network parameters** as a multi-dimensional array,
the third dimension of the S-parameter array must be of the same length as
the frequencies vector specified in the **Frequency (dB)**
parameter.

#### Dependencies

To enable this parameter, set **Data source** to
`Network-parameters`.

### **Frequency (dB)** — Frequency of network parameters `1e9 Hz` (default) | scalar | vector | `Hz` | `kHz` | `MHz` | `GHz`

Frequency of network parameters, specified as a scalar or a vector in Hz.

#### Dependencies

To enable this parameter, set **Data source** to
`Network-parameters`.

### **Reference Impedance(Ohm)** — Reference impedance of network parameters `50` (default) | positive scalar | vector of positive scalars

Reference impedance of network parameters, specified as a positive scalar or vector of
positive scalars in ohms.

**Note**

The reference impedance of all ports must be equal when you
specify it as a vector of positive scalars.

#### Dependencies

To enable this parameter, set **Data source** to
`Network-parameters`.

### **Use rational object** — Rational object as data source `off` (default) | `on`

Select this parameter to use a `rational` object as the
data source to model S-parameter.

Once you select this parameter, in the text box that opens, specify one of these:

- `rational` object.
- MATLAB base workspace variable or a Simulink model workspace
  variable. The block evaluates if the specified variable is a
  rational object."

`rational('default.s2p')` is the default
`rational` object when you select this parameter.

The `rational` objects that you can specify include:

- `rational`
- `rationalfit`
- `rfmodel.rational`

#### Dependencies

To enable this parameter, set **Data source** to
`Rational model`.

### **Residues** — Residues in order of rational model `0` (default) | vector

Residues in order of rational model, specified as a vector.

#### Dependencies

To enable this parameter, set **Data source** to
`Rational model`.

### **Poles** — Residues in order of rational model `0` (default) | vector

Poles in order of rational model, specified as a vector.

#### Dependencies

To enable this parameter, set **Data source** to
`Rational model`.

### **Direct feedthrough** — Direct feedthrough `{0 0:1 0}` (default) | array of vectors

Direct feedthrough, specified as an array vector.

#### Dependencies

To enable this parameter, set **Data source** to
`Rational model`.

### **Simulate noise** — Simulate thermal noise waves `off` (default) | `on`

Select this parameter to simulate thermal noise waves [1]. For more
information see, Generate Thermal Noise.

The S-Parameter block
simulates thermal noise of an S-parameter network with up to 65
ports. *(since R2023b)*

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select this parameter to ground and hide the negative terminals.
Clear this parameter to expose the negative terminals. By exposing
these terminals, you can connect them to other parts of your model.

#### Modeling

### **Modeling options** — Model S-parameters `Time domain` (default) | `Frequency domain`

Model S-parameters, specified as:

- `Time domain` technique creates an
  analytical rational model that approximates the whole range of
  the data. When modeling using `Time domain`,
  the **Plot** in
  `Visualization` tab plots the data defined
  in `Data Source` and the values in the
  `rational` function.
- `Frequency domain`computes the
  baseband impulse response for each carrier frequency
  independently. This technique is based on convolution. There is
  an option to specify the duration of the impulse response. For
  more information, see Compare Time and Frequency Domain Simulation Options for S-parameters.
- For the Amplifier, Antenna, and S-parameters blocks,
  the default value is `Time domain`. For
  the Transmission Line block, the default value is
  `Frequency domain`.

#### Dependencies

To enable this parameter, set **Data source** to either `Data
file` or
`Network-parameters`.

### **Fitting options** — Rational fit fitting options `Fit individually` (default) | `Share poles by column` | `Share all poles`

Rational fit fitting options, specified as `Fit
individually`, `Share poles by
column`, or `Share all
poles`.

**Rational fitting results** shows values of
**Number of independent fits**, **Number of
required poles**, and **Relative error achieved
(dB)**.

#### Dependencies

To set this parameter, select `Time domain`
in **Modeling options**.

### **Relative error desired (dB)** — Relative error acceptable for the rational fit `-40` (default) | scalar

Relative error acceptable for the rational fit, specified as
a scalar.

#### Dependencies

To set this parameter, select `Time domain` in **Modeling
options**.

### **Maximum number of poles** — Maximum number of poles `48` (default) | positive scalar

Maximum number of poles to control over the fitting procedure, specified
as a positive scalar. You can specify up to `99`
poles.

#### Dependencies

To set this parameter, select `Time domain`
in **Modeling options**.

### **Automatically estimate impulse response duration** — Automatically calculate impulse response `on` | `off`

Select this parameter to automatically calculate impulse response.
Clear this parameter to manually specify the impulse response duration
using **Impulse response duration**.

#### Dependencies

To set this parameter, select `Frequency domain` in **Modeling
options**.

### **Impulse response duration** — Impulse response duration `1e-10` (default) | scalar

Impulse response duration, specified as a scalar.

#### Dependencies

To set this parameter, first select `Frequency domain` in **Modeling
options**. Then, clear `Automatically estimate impulse
response duration`.

### **Use only S-parameter magnitude with appropriate delay** — Use only S-parameter magnitude with appropriate delay `off` (default) | `on`

Select this parameter to ignore the S-parameter phase and to delay the
impulse response by half its length. You can use this parameter to shape
spectral content with filter effects by specifying only magnitude.

This parameter uses the magnitude of the original data to obtain the
impulse response of the block. This impulse response is centered about the
time sequence and adds an inherent delay of half the duration of the impulse
response. In the frequency domain, this translates to a linear monotonic
decrease in phase throughout the given spectrum.

**Note**

- This parameter is applicable only for S-parameter data modeled
  in the frequency domain and introduces an artificial delay to
  the system.
- Adding a time delay (or frequency phase variation) to the
  system can result in unexpected behaviors. For example, in an
  unmatched system, delayed signals are bounced back and added to
  the original signals.

#### Dependencies

To enable this parameter, set **Modeling options** to
`Frequency domain`.

#### Visualization

### **Source of frequency data** — Frequency data source `Extracted from data source` (default) | `User-defined`

Frequency data source, specified as:

When **Source of frequency data** is `Extracted
from data source`, the **Data source** must
be set to `Data file`. Verify that the specified **Data
file** contains frequency data.

When **Source of frequency data** is `User-specified`,
specify a vector of frequencies in the **Frequency data** parameter.
Also, specify units from the corresponding drop-down list.

### **Frequency data** — Frequency data range `[1e9:1e6:3e9]` Hz (default) | vector | scalar

Frequency data range, specified as a vector or a scalar in Hz, kHz, MHZ,
or GHz. Specify **Frequency data** as a scalar when you
want to visualize a singe frequency S-parameter data.

#### Dependencies

To enable this parameter, set **Source of frequency
data** to `User-specified`.

### **Plot type** — Type of data plot `X-Y plane` (default) | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

Type of data plot that you want to produce with your data specified
as one of the following:

- `X-Y plane` — Generate
  a Cartesian plot of your data versus frequency. To create linear,
  semilog, or log-log plots, set the **Y-axis scale** and **X-axis
  scale** accordingly.
- `Polar plane` — Generate
  a polar plot of your data. The block plots only the range of data
  corresponding to the specified frequencies.
- `Z smith chart`, `Y
  smith chart`, and `ZY smith chart` —
  Generate a Smith® chart.
  The block plots only the range of data corresponding to the specified
  frequencies.

### **Parameter 1** — Type of S-Parameters to plot `S11` (default) | `SNN`

Type of S-Parameters to plot, specified as `SNN`, where *N*
is the number of ports in the s-parameters block.

### **Parameter 2** — Type of S-Parameters to plot `None` (default) | `SNN`

Type of S-Parameters to plot, specified as `SNN`, where
*N* is the number of ports in the s-parameters
block.

### **Format1** — Plot format `Magnitude (decibels)` (default) | `Angle(degrees)` | `Real` | `Imaginary`

Plot format, specified as `Magnitude (decibels)`, `Angle(degrees)`, `Real`,
or `Imaginary`.

### **Format2** — Plot format `Magnitude (decibels)` (default) | `Angle(degrees)` | `Real` | `Imaginary`

Plot format, specified as `Magnitude (decibels)`, `Angle(degrees)`, `Real`,
or `Imaginary`.

### **Y-axis scale** — Y-axis scale `Linear` (default) | `Logarithmic`

Y-axis scale, specified as `Linear` or `Logarithmic`.

### **X-axis scale** — X-axis scale `Linear` (default) | `Logarithmic`

X-axis scale, specified as `Linear` or `Logarithmic`.

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

### R2024b: `Time domain (rationalfit)` parameter renamed

The `Time domain (rationalfit)` parameter value in the
**Modeling options** parameter has been renamed to
`Time domain` in the S-parameters
block.

When you open a model created before R2024b containing an
S-parameters block, the parameter name displays as
`Time domain`.

### R2023b: Simulate noise in S-parameters block

Starting this release, you can use the **Simulate noise**
parameter in the S-Parameters block to simulate the noise of an
S-parameter network with more than eight ports. In earlier releases, you could use
the block to simulate the noise of networks with up to eight ports.

### R2022b: Use Network parameter and rational objects to model S-parameters

Use network parameter and `rational` objects created at the MATLAB
command line as the data source to model S-parameters by setting **Data
Source** to `Network parameters` and
`Rational model`. For more information, see
**Network-parameter
object** and **Use rational
object**.

### R2022b: Visualize single-frequency S-parameter data

Visualize single-frequency S-parameter data by specifying single-frequency
S-parameter data in the **Frequency data**
parameter.

### R2022b: Block parameter renamed

The **Frequency data** parameter in the S-parameter
 block has been renamed to **Source of frequency
data**.

When you open a model created before R2022b containing the
S-parameter block, the software replaces the **Frequency
data** parameter with the **Source of frequency data**
parameter.

### R2021b: S-parameter network data construction in S-parameter block

Starting in R2021b, the Circuit Envelope library S-Parameters block uses the `rational`
function to perform rational fitting to complex frequency-dependent data. The
`rational` object provides improved fitting speed. The block
also has a new parameter, **Maximum number of poles**, to provide
additional control over the fitting procedure. You can specify up to 99
poles.

When you open a model created before R2021b containing the Circuit Envelope
library S-parameter block, the software updates the extraction method
to perform a rational fit with the new **Maximum number of poles**
parameter. The output of the model gets refitted and the refitted output might
differ from the output in previous releases.

### R2021b: S-parameter block icon updated

Starting in R2021b, the S-parametrs block icon has updated. The
block icons are now dynamic and show the current state of the noise
parameter.

When you open a model created before R2021b containing a
S-parametrs block, the software replaces the block icon with the
R2021b version.

## Description

Model S-parameter network

The S-parameters block models a network defined by S-parameters in the
RF Blockset™ circuit envelope simulation environment. The device can have up to 65
ports. For an introduction to RF simulation, see the example, Simulate High Frequency Components.

The block models S-parameter data in the RF Blockset environment by fitting a rational function to the specified data. For more
information about rational fitting of S-parameters, see the RF Toolbox™
`rational` function.

**Note**

During the fitting procedure, the block sets the
`TendsToZero` and `Qlimit` properties
of the `rational` object to `false` and
`inf`, respectively.

S-parameters block mask icons are dynamic and indicate the current
state of the applied noise parameter. This table shows you how the icons on this block
vary based on the state of the **Simulate noise** parameter on the
block.

| Simulate noise: `on` | Simulate noise: `off` |
| --- | --- |
| S-parameters block icon with Simulate noise is set to on. | S-parameters block icon with Simulate noise is set to off. |

To model RF complex baseband S-parameters in Simulink, use the Idealized Baseband
S-parameters
block.
