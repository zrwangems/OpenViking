---
type: simulink-block
title: 'Network Coupler (Constant Volume Chamber (IL))'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Network Couplers'
documentation_page: 'networkcouplerconstantvolumechamberil'
documentation_source_path: '../simscape/ref/networkcouplerconstantvolumechamberil.html'
language: en
---

# Network Coupler (Constant Volume Chamber (IL))

## Ports
```yaml
ports:
- name: '1'
  summary: Connect this port to the variable-step network, or to the fixed-step network with the smaller sample time isothermal
    liquid
  direction: conserving
- name: '2'
  summary: Connect this port to the fixed-step network with the larger sample time isothermal liquid
  direction: conserving
```

### Conserving

### **1** — Connect this port to the variable-step network, or to the fixed-step network with the smaller sample time isothermal liquid

If one of the coupled networks is running variable step, connect it to port
**1** of the Network Coupler (Constant Volume Chamber
(IL)) block. If both networks are running fixed step, connect this port to
the network with the smaller sample time. If both networks are running variable step,
or fixed step with the same step size, then the block polarity does not matter.

### **2** — Connect this port to the fixed-step network with the larger sample time isothermal liquid

If one of the coupled networks is running variable step, connect port
**2** of the Network Coupler (Constant Volume Chamber
(IL)) block to the fixed-step network. If both networks are running fixed
step, connect this port to the network with the larger sample time.
## Parameters
```yaml
parameters:
- name: Volume (m^3)
  summary: Specify total volume of the chamber 0.001 (default) | positive scalar
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
- name: Approximate connected network flow conductance (kg/s/Pa)
  summary: Specify approximate connected network flow conductance 1e-6 (default) | positive scalar
  group: Analysis
- name: Approximate fluid density (kg/m^3)
  summary: Specify approximate fluid density in the connected network 1000 (default) | positive scalar
  group: Analysis
- name: Approximate fluid bulk modulus (Pa)
  summary: Specify approximate fluid bulk modulus in the connected network 2e9 (default) | positive scalar
  group: Analysis
- name: Initial pressure (MPa)
  summary: Specify initial pressure 0.101325 (default) | positive scalar
  group: Initial Conditions
```

### Main

### **Volume (m^3)** — Specify total volume of the chamber `0.001` (default) | positive scalar

Specify the total volume of the chamber, in m^3. Because the top-level subsystem
is unmasked, you need to set this parameter to the same value both for Port 1
Interface and Port 2 Interface blocks.

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

### **Approximate connected network flow conductance (kg/s/Pa)** — Specify approximate connected network flow conductance `1e-6` (default) | positive scalar

Specify approximate connected network flow conductance, that is, the mass flow per
unit pressure difference, in kg/s/Pa.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Variable step at port 1 and fixed step at port 2`,
`Fixed step both ports with common sample time`, or
`Fixed step both ports with faster sampling at port
1`.

### **Approximate fluid density (kg/m^3)** — Specify approximate fluid density in the connected network `1000` (default) | positive scalar

Specify approximate fluid density in the connected network, in kg/m^3.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Variable step at port 1 and fixed step at port 2`,
`Fixed step both ports with common sample time`, or
`Fixed step both ports with faster sampling at port
1`.

### **Approximate fluid bulk modulus (Pa)** — Specify approximate fluid bulk modulus in the connected network `2e9` (default) | positive scalar

Specify approximate fluid bulk modulus in the connected network, in Pa.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Variable step at port 1 and fixed step at port 2`,
`Fixed step both ports with common sample time`, or
`Fixed step both ports with faster sampling at port
1`.

For information on how to use the **Derived values** section, see Using the Derived Values to Estimate Block Parameters.

### Initial Conditions

### **Initial pressure (MPa)** — Specify initial pressure `0.101325` (default) | positive scalar

Specify initial condition for the pressure in the chamber, in MPa.
## Libraries

Simscape / Utilities / Network Couplers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2023b: Default parameter value changed

The default value of the **Volume** parameter has been changed to match
the default value of the corresponding Foundation library block, Constant Volume
Chamber (IL).

| Parameter Name | Old Value | New Value |
| --- | --- | --- |
| **Volume** | `0.01` | `0.01` |

This change has no compatibility impact. If you open an existing model containing this
block, the parameter values and simulation results are the same as in previous releases.

## Description

Split network at an isothermal liquid connection

The Network Coupler (Constant Volume Chamber (IL)) block uses a volume of
fluid to break the connection between two networks. If your existing network has a suitable
volume of fluid already modeled, then replace it with the fluid network coupler block.
Otherwise, introduce a new volume of fluid to the system using the Network Coupler
(Constant Volume Chamber (IL)) block. Try to make the volume of fluid representative
of the dimensions of the part of the system where you are dividing the network, for example,
use the volume of a connecting pipe. If you make the volume too small, it would require
smaller step sizes, which would make real-time deployment more difficult.

Both of the port interfaces of the Network Coupler (Constant Volume Chamber
(IL)) block are implemented as pressure sources. Therefore, you cannot connect this
block directly to another volume of fluid or pressure source because this would cause an
Index-2 topology (for more information, see Avoiding Numerical Simulation Issues).

### Working with the Block on the Model Canvas

When you add the block to your model and double-click it, the Network Coupler
(Constant Volume Chamber (IL)) subsystem opens.

Network Coupler (Constant Volume Chamber (IL)) subsystem diagram

The Port 1 Interface block contains the dynamics that break the algebraic
loop. Double-click this block to set most of the Network Coupler (Constant Volume
Chamber (IL)) subsystem parameters and view the derived values.

However, unlike most of the other coupler blocks, the Port 2 Interface
block also has one parameter, **Volume (m^3)**, which you need
to set separately.

The Network Coupler (Constant Volume Chamber (IL)) block implements a
constant volume chamber using two copies of the custom Simscape™ component `partialChamberIL.ssc`. Each of these partial
chambers models the full chamber, but calculates only the derivative of pressure due to flow
into its fluid port. The Simulink® integrator that forms part of the coupler subsystem then sums and integrates
the two derivatives. It is this Simulink integrator that is being used to break the algebraic pressure constraint,
which would have existed if connecting two fluid networks directly.

**Note**

- The **Volume (m^3)** parameter requested by the two subsystems is
  the total volume of the chamber in both cases, not half the volume.
- The network coupler blocks break the transmission of fluid property data between
  the two networks. Therefore, you must attach a fluid properties block to both of the
  networks, setting fluid property values to be the same for each instance.

The rate transition blocks are, by default, commented through. Uncomment them if at least one of the coupled networks is running fixed step.

### Using the Derived Values to Estimate Block Parameters

On the **Analysis** tab of the Port 1 Interface block dialog box, the **Derived values** section contains a list of recommended values that you can use when specifying block parameters. For example, use the **Recommended max discrete sample time (s)** derived value to verify that your **Port 1 network discrete sample time (s)** and **Port 2 network discrete sample time (s)** parameter values are within acceptable limits.

The derived values list is based on the chosen block configuration.

If both networks are running variable step, then the **Analysis** tab
is empty, and there are no restrictions on the fluid volume value you specify.

If one or both networks are running fixed step, then the **Analysis**
tab provides advice on the recommended maximum discrete sample time to use. To do this, you
must provide some additional information about the connected networks:

- Approximate connected network flow conductance, that is, the mass flow per unit
  pressure difference.
- Approximate fluid density.
- Approximate fluid bulk modulus.

These values only need to be approximate because they do not impact the model. They
serve only to provide advice on the recommended maximum discrete sample time.

The **Update** button lets you recalculate
the derived values after you change the parameters of the connected networks.
