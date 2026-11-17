---
type: simulink-block
title: 'Finite-Gain Op-Amp'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'finitegainopamp'
documentation_source_path: 'ref/finitegainopamp.html'
language: en
---

# Finite-Gain Op-Amp

## Ports
```yaml
ports:
- name: +
  summary: Positive electrical voltage electrical
  direction: conserving
- name: '-'
  summary: Negative electrical voltage electrical
  direction: conserving
- name: out
  summary: Output voltage electrical
  direction: conserving
```

### Conserving

### **+** — Positive electrical voltage electrical

Electrical conserving port associated with the op-amp noninverting
input.

### **-** — Negative electrical voltage electrical

Electrical conserving port associated with the op-amp inverting input.

### **out** — Output voltage electrical

Electrical conserving port associated with the op-amp output. The port
name is hidden on the block icon, but you can see it in simulation data
logs.
## Parameters
```yaml
parameters:
- name: Gain, A
  summary: Open-loop gain 1000 (default)
  group: Main
- name: Input resistance, Rin
  summary: Resistance at block input 1e6 Ohm (default)
  group: Main
- name: Output resistance, Rout
  summary: Resistance at block output 100 Ohm (default)
  group: Main
- name: Minimum output, Vmin
  summary: Output voltage lower limit -15 V (default)
  group: Main
- name: Maximum output, Vmax
  summary: Output voltage upper limit 15 V (default)
  group: Main
- name: Noise mode
  summary: Select whether op-amp generates thermal noise Disabled (default) | Enabled
  group: Noise
- name: Input noise voltage density
  summary: Density of voltage noise 30e-9 V/Hz^0.5 (default)
  group: Noise
- name: Noise current parameterization
  summary: Select whether noise current density is different or the same for both inputs Apply same density function to both
    inputs (default) | Apply different density function to each input
  group: Noise
- name: Input noise current density
  summary: Current noise at both inputs 0.5e-12 A/Hz^0.5 (default)
  group: Noise
- name: Noninverting input noise current density
  summary: Current noise at noninverting input 0.5e-12 A/Hz^0.5 (default)
  group: Noise
- name: Inverting input noise current density
  summary: Current noise at inverting input 0.5e-12 A/Hz^0.5 (default)
  group: Noise
- name: Sample time
  summary: Rate at which the noise source is sampled 1e-3 s (default)
  group: Noise
- name: Repeatability
  summary: Select the noise control option Not repeatable (default) | Repeatable | Specify seed
  group: Noise
- name: Input noise voltage auto-generated seed used for repeatable option
  summary: Auto-generated random number seed for voltage noise random real number
  group: Noise
- name: Noninverting input noise current auto-generated seed used for repeatable option
  summary: Auto-generated random number seed for current noise at noninverting input random real number
  group: Noise
- name: Inverting input noise current auto-generated seed used for repeatable option
  summary: Auto-generated random number seed for current noise at inverting input random real number
  group: Noise
- name: Input noise voltage seed
  summary: Random number seed for voltage noise 0 (default)
  group: Noise
- name: Noninverting input noise current seed
  summary: Random number seed for current noise at noninverting input 0 (default)
  group: Noise
- name: Inverting input noise current seed
  summary: Random number seed for current noise at inverting input 0 (default)
  group: Noise
```

### Main

### **Gain, A** — Open-loop gain 1000 (default)

The open-loop gain of the operational amplifier.

### **Input resistance, Rin** — Resistance at block input 1e6 Ohm (default)

The resistance at the input of the operational amplifier that the
block uses to calculate the input current.

### **Output resistance, Rout** — Resistance at block output 100 Ohm (default)

The resistance at the output of the operational amplifier that the
block uses to calculate the drop in output voltage due to output
current.

### **Minimum output, Vmin** — Output voltage lower limit -15 V (default)

The lower limit on the operational amplifier output voltage.

### **Maximum output, Vmax** — Output voltage upper limit 15 V (default)

The upper limit on the operational amplifier output voltage.

### Noise

### **Noise mode** — Select whether op-amp generates thermal noise `Disabled` (default) | `Enabled`

Select whether to model thermal noise effects:

- `Disabled` — Op-amp does not
  generate thermal noise.
- `Enabled` — Op-amp generates
  thermal noise voltage and current, and the associated parameters
  become visible in the **Noise** section.

### **Input noise voltage density** — Density of voltage noise 30e-9 V/Hz^0.5 (default)

Single-sided, spectral amplitude density of the voltage noise applied
to the noninverting input.

#### Dependencies

Enabled when the **Noise mode** parameter is set
to `Enabled`.

### **Noise current parameterization** — Select whether noise current density is different or the same for both inputs `Apply same density function to both inputs` (default) | `Apply different density function to each input`

Select whether current density values applied to block inputs are
different or the same.

#### Dependencies

Enabled when the **Noise mode** parameter is set
to `Enabled`.

### **Input noise current density** — Current noise at both inputs 0.5e-12 A/Hz^0.5 (default)

Single-sided, spectral amplitude density of the current noise applied
to both inputs. Note that even though the density function is the same
for both inputs, the actual noise current also depends on the random
number seed. If the seeds used for the random number generation are
different, then the actual noise currents at the inputs are also
different.

#### Dependencies

Enabled when the **Noise current
parameterization** parameter is set to
`Apply same density function to both
inputs`.

### **Noninverting input noise current density** — Current noise at noninverting input 0.5e-12 A/Hz^0.5 (default)

Single-sided, spectral amplitude density of the current noise applied
to noninverting input.

#### Dependencies

Enabled when the **Noise current
parameterization** parameter is set to
`Apply different density function to each
input`.

### **Inverting input noise current density** — Current noise at inverting input 0.5e-12 A/Hz^0.5 (default)

Single-sided, spectral amplitude density of the current noise applied
to inverting input.

#### Dependencies

Enabled when the **Noise current
parameterization** parameter is set to
`Apply different density function to each
input`.

### **Sample time** — Rate at which the noise source is sampled 1e-3 s (default)

Defines the rate at which the noise source is sampled. Choose it to
reflect the frequencies of interest in your model. Making the sample
time too small will unnecessarily slow down your simulation.

#### Dependencies

Enabled when the **Noise mode** parameter is set
to `Enabled`.

### **Repeatability** — Select the noise control option `Not repeatable` (default) | `Repeatable` | `Specify seed`

Select the noise control option:

- `Not repeatable` — The random
  sequence used for noise generation is not repeatable.
- `Repeatable` — The random
  sequence used for noise generation is repeatable, with a
  system-generated seed.
- `Specify seed` — The random
  sequence used for noise generation is repeatable, and you
  control the seed by using the seed parameters. You specify seed
  values separately for input noise voltage, noninverting input
  noise current, and inverting input noise current.

#### Dependencies

Enabled when the **Noise mode** parameter is set
to `Enabled`.

### **Input noise voltage auto-generated seed used for repeatable option** — Auto-generated random number seed for voltage noise random real number

Random number seed stored inside the block to make the random sequence
repeatable. The parameter value is automatically generated using the
MATLAB random number generator command. You can modify this
parameter value, but it gets overwritten by a new random value if you
copy the block to another block in the model. Therefore, if you want to
control the seed of the random sequence, use the `Specify
seed` option for the **Repeatability**
parameter and specify the desired seed value using the **Input
noise voltage seed** parameter.

#### Dependencies

Enabled when the **Repeatability** parameter is
set to `Repeatable`.

### **Noninverting input noise current auto-generated seed used for repeatable option** — Auto-generated random number seed for current noise at noninverting input random real number

Random number seed stored inside the block to make the random sequence
repeatable. The parameter value is automatically generated using the
MATLAB random number generator command. You can modify this
parameter value, but it gets overwritten by a new random value if you
copy the block to another block in the model. Therefore, if you want to
control the seed of the random sequence, use the `Specify
seed` option for the **Repeatability**
parameter and specify the desired seed value using the
**Noninverting input noise current seed**
parameter.

#### Dependencies

Enabled when the **Repeatability** parameter is
set to `Repeatable`.

### **Inverting input noise current auto-generated seed used for repeatable option** — Auto-generated random number seed for current noise at inverting input random real number

Random number seed stored inside the block to make the random sequence
repeatable. The parameter value is automatically generated using the
MATLAB random number generator command. You can modify this
parameter value, but it gets overwritten by a new random value if you
copy the block to another block in the model. Therefore, if you want to
control the seed of the random sequence, use the `Specify
seed` option for the **Repeatability**
parameter and specify the desired seed value using the
**Inverting input noise current seed**
parameter.

#### Dependencies

Enabled when the **Repeatability** parameter is
set to `Repeatable`.

### **Input noise voltage seed** — Random number seed for voltage noise 0 (default)

Seed used by the noise random number generator.

#### Dependencies

Enabled when the **Repeatability** parameter is
set to `Specify seed`.

### **Noninverting input noise current seed** — Random number seed for current noise at noninverting input 0 (default)

Seed used by the noise random number generator.

#### Dependencies

Enabled when the **Repeatability** parameter is
set to `Specify seed`.

### **Inverting input noise current seed** — Random number seed for current noise at inverting input 0 (default)

Seed used by the noise random number generator.

#### Dependencies

Enabled when the **Repeatability** parameter is
set to `Specify seed`.
## Libraries

Simscape / Electrical / Integrated Circuits

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008b**

## Description

Gain-limited operational amplifier model with optional noise

The Finite-Gain Op-Amp block models a gain-limited
operational amplifier. If the voltages at the positive and negative ports are
*V*p and
*V*m, respectively, the output voltage is:

Vout = A(Vp-Vm)−Iout\*Rout

where:

- *A* is the gain.
- *R*out is the output
  resistance.
- *I*out is the output
  current.

The input current is:

Vp-VmRin

where *R*in is the input
resistance.

The output voltage is limited by the minimum and maximum output values you specify in
the block dialog box.

### Thermal Noise

The Finite-Gain Op-Amp block can generate thermal
noise. If you set the **Noise mode** parameter to
`Enabled`, then the equivalent circuit for the block
includes a noise current source attached to each of the inputs, and a noise voltage
source attached to the noninverting input. These three noise sources are independent
and uncorrelated.

The block generates noise voltage and current according to:

vnoise=vdensity2hN(0,1)

inoise=idensity2hN(0,1)

where:

- *v*noise is the noise
  voltage.
- *v*density is the single-sided,
  spectral amplitude density of the voltage noise.
- *i*noise is the noise current at
  an input.
- *i*density is the single-sided,
  spectral amplitude density of the current noise applied to that
  input.
- *h* is the sampling time.
- *N* is a Gaussian random number with zero mean and
  standard deviation of one.

The block generates Gaussian noise by using the PS Random Number source in
the Simscape™ Foundation library. You can control the random number seed by setting
the **Repeatability** parameter:

- `Not repeatable` — Every time you simulate
  your model, the block resets the random seed using the MATLAB® random number generator:

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — The block automatically
  generates a seed value and stores it inside the block, to always start the
  simulation with the same random number. This auto-generated seed value is
  set when you add a Finite-Gain Op-Amp block
  from the block library to the model. When you make a new copy of the
  Finite-Gain Op-Amp block from an existing
  one in a model, a new seed value is generated. The block sets the value
  using the MATLAB random number generator command shown above.
- `Specify seed` — If you select this
  option, additional parameters let you directly specify the random number
  seed values for input voltage, noninverting input current, and inverting
  input current.
