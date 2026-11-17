---
type: simulink-block
title: 'Network Coupler (Thermal Mass)'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Network Couplers'
documentation_page: 'networkcouplerthermalmass'
documentation_source_path: '../simscape/ref/networkcouplerthermalmass.html'
language: en
---

# Network Coupler (Thermal Mass)

## Ports
```yaml
ports:
- name: '1'
  summary: Connect this port to the variable-step network, or to the fixed-step network with the smaller sample time thermal
    | thermal node array
  direction: conserving
- name: '2'
  summary: Connect this port to the fixed-step network with the larger sample time thermal | thermal node array
  direction: conserving
```

### Conserving

### **1** — Connect this port to the variable-step network, or to the fixed-step network with the smaller sample time thermal | thermal node array

If one of the coupled networks is running variable step, connect it to port
**1** of the Network Coupler (Thermal Mass) block.
If both networks are running fixed step, connect this port to the network with the
smaller sample time. If both networks are running variable step, or fixed step with
the same step size, then the block polarity does not matter.

### **2** — Connect this port to the fixed-step network with the larger sample time thermal | thermal node array

If one of the coupled networks is running variable step, connect port
**2** of the Network Coupler (Thermal Mass) block to
the fixed-step network. If both networks are running fixed step, connect this port to
the network with the larger sample time.
## Parameters
```yaml
parameters:
- name: Thermal node array size
  summary: Specify number of thermal nodes 1 (default) | positive integer
  group: Main
- name: Thermal mass (J/K)
  summary: Specify thermal mass value 100 (default) | positive scalar
  group: Main
- name: Sampling type
  summary: Select sampling types scenario for coupled networks Variable step at ports 1 and 2 (default) | Variable step at
    port 1 and fixed step at port 2 | Fixed step both ports with common sample time | Fixed step both ports with faster sampling
    at port 1
  group: Main
- name: Port 1 network discrete sample time (s)
  summary: Specify sample time for Network 1 0.02 (default) | positive scalar
  group: Main
- name: Port 2 network discrete sample time (s)
  summary: Specify sample time for Network 2 0.1 (default) | positive scalar
  group: Main
- name: Use prediction when connecting fixed step to variable step
  summary: Lets you enable the prediction (discrete->continuous) algorithm off (default) | on
  group: Main
- name: Use smoothing when connecting variable step to fixed step
  summary: Lets you enable the smoothing (continuous->discrete) algorithm off (default) | on
  group: Main
- name: Smoothing time constant (s)
  summary: Specify time constant for the first-order filter 0.01 (default) | positive scalar
  group: Main
- name: Use prediction when connecting slow to fast sample times
  summary: Lets you enable the prediction (slow->fast) algorithm off (default) | on
  group: Main
- name: Use smoothing when connecting fast to slow sample times
  summary: Lets you enable the smoothing (fast->slow) algorithm off (default) | on
  group: Main
- name: Number of samples over which to smooth
  summary: Specify number of samples for averaging 1 (default) | positive scalar
  group: Main
- name: Approximate connected network thermal conductance (W/K)
  summary: Specify approximate thermal conductance of connected network 1 (default) | positive scalar
  group: Analysis
- name: Initial temperature (K)
  summary: Specify initial temperature of the thermal mass 300 (default) | positive scalar
  group: Initial Conditions
```

### Main

### **Thermal node array size** — Specify number of thermal nodes `1` (default) | positive integer

Specify the size of the thermal node array connected to the two thermal ports,
**1** and **2**. Because the top-level subsystem
is unmasked, you need to set this parameter to the same value both for Port 1
Interface and Port 2 Interface blocks.

If you are breaking a regular thermal connection, leave the default value of
`1` unchanged. However, some models use arrays of thermal nodes,
for example, to connect a battery pack modeled using Simscape
Battery to a corresponding cooling plate. In this case there are multiple
thermal nodes in the battery pack that have corresponding thermal nodes on the cooling
plate. You can use the Network Coupler (Thermal Mass) block to separate
the two networks, to use a slower sample time for the thermal part and a faster one
for the electrical part. Using the Network Coupler (Thermal Mass) block
in such a model helps speed up desktop simulation and makes it easier to deploy the
model to real-time hardware.

### **Thermal mass (J/K)** — Specify thermal mass value `100` (default) | positive scalar

Specify the thermal mass value. Calculate this value by using the
**Mass** and **Specific heat** parameters from the
Thermal Mass block being replaced. The
**Analysis** tab also provides assistance on selecting a suitable
thermal mass value. For more information, see Using the Derived Values to Estimate Block Parameters.

### **Sampling type** — Select sampling types scenario for coupled networks `Variable step at ports 1 and 2` (default) | `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

Select how the coupled networks are sampled:

- `Variable step at ports 1 and 2` — Both networks are variable-step.
- `Variable step at port 1 and fixed step at port 2` — Network 1 is variable-step and Network 2 is fixed-step.
- `Fixed step both ports with common sample time` — Both networks are fixed-step, with the same step size.
- `Fixed step both ports with faster sampling at port 1` — Both
  networks are fixed-step, with different step sizes.

### **Port 1 network discrete sample time (s)** — Specify sample time for Network 1 `0.02` (default) | positive scalar

Specify sample time for Network 1, in seconds.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Fixed step both ports with common sample time` or
`Fixed step both ports with faster sampling at port
1`.

### **Port 2 network discrete sample time (s)** — Specify sample time for Network 2 `0.1` (default) | positive scalar

Specify sample time for Network 2, in seconds.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Variable step at port 1 and fixed step at port 2` or
`Fixed step both ports with faster sampling at port
1`.

### **Use prediction when connecting fixed step to variable step** — Lets you enable the prediction (discrete->continuous) algorithm off (default) | on

Select this check box to enable the prediction (discrete->continuous) algorithm.
For more information, see Prediction and Smoothing.

#### Dependencies

To display this option, set the **Sampling type** parameter to
`Variable step at port 1 and fixed step at port
2`.

### **Use smoothing when connecting variable step to fixed step** — Lets you enable the smoothing (continuous->discrete) algorithm off (default) | on

Select this check box to enable the smoothing (continuous->discrete) algorithm.
For more information, see Prediction and Smoothing.

#### Dependencies

To display this option, set the **Sampling type** parameter to
`Variable step at port 1 and fixed step at port
2`.

### **Smoothing time constant (s)** — Specify time constant for the first-order filter `0.01` (default) | positive scalar

Specify time constant, in seconds, for the first-order filter that the smoothing
algorithm uses to remove unwanted high-frequency information.

#### Dependencies

To enable this parameter, select the **Use smoothing when connecting
variable step to fixed step** check box.

### **Use prediction when connecting slow to fast sample times** — Lets you enable the prediction (slow->fast) algorithm off (default) | on

Select this check box to enable the prediction (slow->fast) algorithm. For more
information, see Prediction and Smoothing.

#### Dependencies

To display this option, set the **Sampling type** parameter to
`Fixed step both ports with faster sampling at port
1`.

### **Use smoothing when connecting fast to slow sample times** — Lets you enable the smoothing (fast->slow) algorithm off (default) | on

Select this check box to enable the smoothing (fast->slow) algorithm. For more
information, see Prediction and Smoothing.

#### Dependencies

To display this option, set the **Sampling type** parameter to
`Fixed step both ports with faster sampling at port
1`.

### **Number of samples over which to smooth** — Specify number of samples for averaging `1` (default) | positive scalar

The smoothing algorithm works by averaging the last *N* samples.
You specify *N* by using this parameter.

#### Dependencies

To enable this parameter, select the **Use smoothing when connecting
fast to slow sample times** check box.

### Analysis

### **Approximate connected network thermal conductance (W/K)** — Specify approximate thermal conductance of connected network `1` (default) | positive scalar

Specify approximate thermal conductance of the connected network, in W/K. If the
thermal conductances of the two networks differ, provide the higher value.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Variable step at port 1 and fixed step at port 2`,
`Fixed step both ports with common sample time`, or
`Fixed step both ports with faster sampling at port
1`.

For information on how to use the **Derived values** section, see Using the Derived Values to Estimate Block Parameters.

### Initial Conditions

### **Initial temperature (K)** — Specify initial temperature of the thermal mass `300` (default) | positive scalar

Specify initial condition for the thermal mass temperature, in K.
## Libraries

Simscape / Utilities / Network Couplers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2023b: Break connections between arrays of thermal nodes

The Network Coupler (Thermal Mass) block now supports
arrays of thermal nodes. The new parameter, **Thermal node array size**,
lets you specify the array size. If you look under mask, the Port 1 Interface
and Port 2 Interface subsystems contain custom blocks that support vectorized
thermal nodes, instead of the regular Foundation library thermal blocks.

This change has no compatibility impact. The default value of the **Thermal node
array size** parameter corresponds to a regular thermal connection. If you open
an existing model containing this block, the simulation results are the same as in previous
releases.

## Description

Split network at a thermal connection

The Network Coupler (Thermal Mass) block uses a thermal mass to break a
network connection. If your existing network has a suitable thermal mass already modeled, then
replace it with the network coupler block. Otherwise, introduce a new thermal mass to the
system using the Network Coupler (Thermal Mass) block.

Both of the port interfaces of the Network Coupler (Thermal Mass) block are
implemented as temperature sources. Therefore, you cannot connect this block directly to a
thermal mass or other temperature source because this would cause an Index-2 topology (for
more information, see Avoiding Numerical Simulation Issues).

To facilitate working with models that contain arrays of thermal nodes, such as
Simscape™
Battery™ models, the Port 1 Interface and Port 2 Interface
subsystems contain custom blocks, such as Controlled Temperature Source or
Heat Flow Rate Sensor. These custom blocks are based on the equivalent
Foundation library blocks but are modified to support vectorized thermal nodes. The source
files for these custom blocks are located in the following package directory:

```
matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+thermal
```

where *`matlabroot`* is the MATLAB® root directory on your machine, as returned by entering

```
matlabroot
```

at the MATLAB command prompt. The package contains source files for heat flow and temperature
sources and sensors and a thermal reference with array support. You can use these blocks to
customize your network coupler configuration.

### Working with the Block on the Model Canvas

When you add the block to your model and double-click it, the Network Coupler
(Thermal Mass) subsystem opens.

Network Coupler (Thermal Mass) subsystem diagram

The Port 1 Interface block contains the dynamics that break the algebraic
loop. Double-click this block to set all of the Network Coupler (Thermal
Mass) subsystem parameters and view the derived values.

The rate transition blocks are, by default, commented through. Uncomment them if at least one of the coupled networks is running fixed step.

### Using the Derived Values to Estimate Block Parameters

On the **Analysis** tab of the Port 1 Interface block dialog box, the **Derived values** section contains a list of recommended values that you can use when specifying block parameters. For example, use the **Recommended max discrete sample time (s)** derived value to verify that your **Port 1 network discrete sample time (s)** and **Port 2 network discrete sample time (s)** parameter values are within acceptable limits.

The derived values list is based on the chosen block configuration.

If both networks are running variable step, then the **Analysis** tab
is empty, and there are no restrictions on the thermal mass value you specify.

If one or both networks are running fixed step, then the **Analysis**
tab provides assistance on selecting a suitable thermal mass value, by asking you for an
approximate thermal conductance value for the connected networks. If the thermal
conductances of the two networks differ, provide the higher value. The
**Update** button then provides a maximum recommended discrete sample
time to use.
