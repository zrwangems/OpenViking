---
type: simulink-block
title: 'Sinestream Signal Generator'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Frequency Response Estimation / Standalone Perturbation Signal Generation'
documentation_page: 'sinestreamsignalgenerator'
documentation_source_path: 'ug/sinestreamsignalgenerator.html'
language: en
---

# Sinestream Signal Generator

## Ports

### Input

### **start/stop** — Start and stop the signal generation scalar

To start and stop the signal generation process, provide a signal at the
**start/stop** port. When the value of the signal changes
from:

- Negative or zero to positive, the signal generation starts
- Positive to negative or zero, the signal generation stops

Typically, you can use a signal that changes from 0 to 1 to start the experiment,
and from 1 to 0 to stop it. When the experiment is not running, the block does not
generate a perturbation at the output port.

Generate a perturbation signal which is long enough for the algorithm to collect
sufficient data for a good estimate at all frequencies it probes. The block displays a
recommended experiment length in the **Signal Length** section of the
block parameters. This value is based on the experiment mode and the frequencies you
specify for the experiment.

The recommended experiment length is:

∑i2πωiNp,i+2TsNfreq,

where:

- *ωi* is the *i*th
  frequency specified in the **Frequencies** parameter (in
  rad/s).
- *Nfreq* is the number of frequencies
  in **Frequencies**.
- *N**p*,*i*
  is the corresponding value of the **Number of signal periods**
  parameter.
- *Ts* is the experiment sampling
  time, specified by the **Sample time (Ts)** parameter.

Avoid any load disturbance to the plant during the experiment. Load disturbance
can distort the plant output and reduce the accuracy of the frequency-response
estimation.

**Data Types:** `single` | `double`

### **w** — Frequencies for estimation experiment vector

Supply a value for the **Frequencies** parameter. See the
**Frequencies** parameter for information about how to choose
frequencies.

When you supply frequencies via this port, specify the number of frequencies with
the **Number of frequencies in the excitation signal**
parameter.

#### Dependencies

To enable this port, in **Excitation Signal Source**, select
**External ports**.

**Data Types:** `single` | `double`

### **amp** — Perturbation amplitudes scalar | vector

Supply a value for the **Amplitudes** parameter. See the
**Amplitudes** parameter for details.

#### Dependencies

To enable this port, in **Excitation Signal Source**, select
**External Ports**.

**Data Types:** `single` | `double`
### Output

### **sin**, **cos**, **sincos** — Sinestream perturbation signal scalar | vector

Sinestream perturbation signal.

**Data Types:** `single` | `double`

### **3ϕ-sin**, **3ϕ-cos**, **3ϕ-sincos** — Three-phase sinestream perturbation signal vector

Three-phase sinestream perturbation signal.

To extract each phase in the output signal, use a Demux
block.

#### Dependencies

To enable this port, select **Generate three-phase perturbation
signal**.

**Data Types:** `single` | `double`

### **idx w** — Output frequency indices scalar | vector

The signal at this port outputs the corresponding index of the generated frequency
component.

#### Dependencies

**Data Types:** `single` | `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Sample time (Ts)** — Sample time 0.1 (default) | positive scalar | –1

The block is a discrete-time block that runs at a fixed sample time, specified with
this parameter. The largest frequency that you can estimate is the Nyquist frequency,
*π*/*Ts* rad/s. Best practice
is to use a sample time at least five times faster than the Nyquist frequency.

*Ts* =
*π*/(5*ωmax*) ≅
0.6/*ωmax* or
0.1/*fmax*,

Here, *ωmax* is the highest frequency in the
**Frequencies** parameter in rad/s, and
*fmax* is the highest frequency in Hz. The
sample time must be small enough to estimate the fastest desired frequency, but not so
small as to introduce unnecessary computational burden.

If you set the sample time to –1, then the software determines the sample time on
compilation, based on the sources outside the block. Setting sample time to –1 disables
the internal checks in the block that ensure your estimation frequencies are below the
Nyquist frequency.

#### Tip

If you want to run the deployed block with different sample times in your
application, set this parameter to –1 and put the block in a Triggered Subsystem. Then, trigger the subsystem at the desired sample
time. If you do not plan to change the sample time after deployment, specify a fixed
and finite sample time.

### **Data Type** — Floating point precision `double` (default) | `single`

Specify the floating-point precision based on simulation environment or hardware
requirements.

### **Excitation signal source** — Excitation signal source **Block parameters** (default) | **External ports**

Specify whether to supply the frequencies and amplitudes of the experiment
perturbation signal via block parameters or via external ports.

- **Block parameters** — Select to enable the
  **Frequencies** and **Amplitudes**
  parameters.
- **External ports** — Select to enable the
  **w** and **amp** input ports. Use this option
  if you want to change the frequencies and amplitudes of the perturbation signal
  after deployment.

### **Frequencies** — Frequencies for estimation [0.5 1 2] (default) | vector

Frequencies at which to estimate the frequency response of the plant. The block
injects a perturbation at each of these frequencies. The highest frequency you can
estimate is limited by the Nyquist frequency,
*π*/*Ts* rad/s, where
*Ts* is the value you set for the
**Sample time (Ts)** parameter.

There is no recommended limit on the number or range of frequencies. However, due to
the sequential nature of the sinestream perturbation, each frequency point you add
increases the required experiment time (see the **start/stop** input
port for details). Further, a too-wide range of frequencies requires you to use a fast
sample time for high frequencies that is inefficient for the lower frequencies.

#### Tips

This parameter is not tunable. To provide frequencies after deployment, set
**Excitation Signal Source** to **External ports**
and use the **w** input port.

#### Dependencies

To enable this parameter, set **Excitation Signal Source** to
**Block parameters**.

### **Amplitudes** — Amplitudes of injected perturbations 1 (default) | scalar | vector

Specify the amplitudes of the perturbation signals injected into the plant. To use
the same amplitude for all frequencies, specify a scalar value. If you know that the
response changes significantly over range of frequencies to estimate, then you can use a
vector to specify a different amplitude for each frequency. For instance, you can use a
smaller value around known resonant frequencies and a larger value above the rolloff
frequency. The vector must be the same length as the vector you provide for
**Frequencies**.

The amplitudes must be:

- Large enough that the perturbation overcomes any deadband in the plant actuator
  and generates a response above the noise level
- Small enough to keep the plant running within the approximately linear region
  near the nominal operating point, and to avoid saturating the plant input or output

#### Tip

This parameter is not tunable. To provide amplitudes after deployment, set
**Excitation Signal Source** to **External ports**
and use the **amp** input port.

#### Dependencies

To enable this parameter, set **Excitation Signal Source** to
**Block parameters**.

### **Number of frequencies** — Number of externally supplied frequencies 3 (default) | positive integer

When you provide the experiment frequencies via the external port
**w**, specify the number of frequencies (the length of the vector
signal at **w**) with this parameter.

#### Dependencies

To enable this parameter, set **Excitation Signal Source** to
**External ports**.

### **Number of signal periods** — Number of periods each sine wave is at maximum amplitude 6 (default) | scalar | vector

Number of periods each sine wave is at maximum amplitude, specified as one of the
following:

- Scalar — Use the same number of periods for all frequencies.
- Vector with length equal to the length of **Frequency** — Use a
  different number of periods for each frequency.

### Advanced Settings

### **Waveform Type** — Waveform type **sine** (default) | **cosine** | **both**

Specify the waveform type of the perturbation signal as either sine, cosine, or
both (sincos) at the same time.

### **Phase Shift** — Phase shift of the wave 0 (default) | scalar | vector

Specify the phase shift in the waveform.

### **Generate three-phase perturbation signal** — Generate three-phase perturbation signal `off` (default) | `on`

Generate a three-phase perturbation signal with a phase difference of 120° between
waves. Three-phase signals are helpful when you want to identify frequency response
of three-phase AC power systems.

### **Show frequency index port** — Enable frequency index port `off` (default) | `on`

Select this option to enable **idx w** port.

## Libraries

Simulink Control Design / Signal Generation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Generate sinestream input signal for plant frequency response estimation

Use this block to generate sinestream input perturbation signals. This block allows you to
generate scalar or vector signals including three-phase sin, cos, or both (sincos) signals.
Three-phase signals are helpful when you want to identify frequency response of three-phase AC
power systems. For example, you can use the generated signal to measure impedance of a power
inverter which connects renewable energy resources to three-phase AC power grids. For more
information about sinestream input signals, see Sinestream Input Signals.

This block is helpful when you want to generate perturbation signals to inject in your
plant models in desktop simulation or on hardware through code generation. You can then
collect the plant response data to the perturbation signal and perform custom processing to
identify plant characteristics.
