---
type: simulink-block
title: 'Network Coupler (Compressible Link)'
family: 'utilities'
product_id: 'network-couplers'
product_name: 'Network Couplers'
documentation_release: R2025b
official_category: 'Network Couplers'
documentation_page: 'networkcouplercompressiblelink'
documentation_source_path: '../simscape/ref/networkcouplercompressiblelink.html'
language: en
---

# Network Coupler (Compressible Link)

## Ports
```yaml
ports:
- name: '1'
  summary: Connect this port to the variable-step network, or to the fixed-step network with the smaller sample time mechanical
    translational
  direction: conserving
- name: '2'
  summary: Connect this port to the fixed-step network with the larger sample time mechanical translational
  direction: conserving
```

### Conserving

### **1** — Connect this port to the variable-step network, or to the fixed-step network with the smaller sample time mechanical translational

If one of the coupled networks is running variable step, connect it to port
**1** of the Network Coupler (Compressible Link)
block. If both networks are running fixed step, connect this port to the network with
the smaller sample time. If both networks are running variable step, or fixed step
with the same step size, then the block polarity does not matter.

### **2** — Connect this port to the fixed-step network with the larger sample time mechanical translational

If one of the coupled networks is running variable step, connect port
**2** of the Network Coupler (Compressible Link)
block to the fixed-step network. If both networks are running fixed step, connect this
port to the network with the larger sample time.
## Parameters
```yaml
parameters:
- name: Separate using
  summary: Select separation type an actual link compliance (default) | an added numerical compliance
  group: Main
- name: Link stiffness (N/m)
  summary: Specify stiffness of compressible link 250 (default) | positive scalar
  group: Main
- name: Link damping (N/(m/s))
  summary: Specify damping coefficient of compressible link 20 (default) | positive scalar
  group: Main
- name: Sampling type
  summary: Select sampling types scenario for coupled networks Variable step at ports 1 and 2 (default) | Variable step at
    port 1 and fixed step at port 2 | Fixed step both ports with common sample time | Fixed step both ports with faster sampling
    at port 1
  group: Main
- name: Separator time constant (s)
  summary: Specify filter time constant 0.001 (default) | positive scalar
  group: Main
- name: Port 1 network discrete sample time (s)
  summary: Specify sample time for Network 1 0.001 (default) | positive scalar
  group: Main
- name: Port 2 network discrete sample time (s)
  summary: Specify sample time for Network 2 0.01 (default) | positive scalar
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
- name: Approximate mass at port 1 (kg)
  summary: Specify approximate mass at port 1 1 (default) | positive scalar
  group: Analysis
- name: Approximate mass at port 2 (kg)
  summary: Specify approximate mass at port 2 1 (default) | positive scalar
  group: Analysis
- name: Initial transmitted force (N)
  summary: Specify initial force transmitted by the link 0 (default) | positive scalar
  group: Initial Conditions
```

### Main

### **Separate using** — Select separation type `an actual link compliance` (default) | `an added numerical compliance`

Select how to separate the coupled networks:

- `an actual link compliance` — Split the network at a
  point where there is an actual compressible link (spring and damper). Use the
  shaft compliance to improve stability of the coupled networks.
- `an added numerical compliance` — Add a numerical
  compliance and use it to improve stability of the coupled networks.

### **Link stiffness (N/m)** — Specify stiffness of compressible link 250 (default) | positive scalar

If you are replacing an actual spring and damper in the model, specify the spring
rate. Use the **Spring rate** parameter value from the
Translational Spring block being replaced, converting
it to N/m, if necessary.

#### Dependencies

To enable this parameter, set the **Separate using** parameter
to `an actual link compliance`.

### **Link damping (N/(m/s))** — Specify damping coefficient of compressible link 20 (default) | positive scalar

If you are replacing an actual spring and damper in the model, specify the damping
coefficient. Use the **Damping coefficient** parameter value from the
Translational Damper block being replaced, converting
it to N/(m/s), if necessary.

#### Dependencies

To enable this parameter, set the **Separate using** parameter
to `an actual link compliance`.

### **Sampling type** — Select sampling types scenario for coupled networks `Variable step at ports 1 and 2` (default) | `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

Select how the coupled networks are sampled:

- `Variable step at ports 1 and 2` — Both networks are variable-step.
- `Variable step at port 1 and fixed step at port 2` — Network 1 is variable-step and Network 2 is fixed-step.
- `Fixed step both ports with common sample time` — Both networks are fixed-step, with the same step size.
- `Fixed step both ports with faster sampling at port 1` — Both
  networks are fixed-step, with different step sizes.

### **Separator time constant (s)** — Specify filter time constant `0.001` (default) | positive scalar

Specify the filter time constant, in seconds, to remove the algebraic loop.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Variable step at ports 1 and 2`.

### **Port 1 network discrete sample time (s)** — Specify sample time for Network 1 `0.001` (default) | positive scalar

Specify sample time for Network 1, in seconds.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Fixed step both ports with common sample time` or
`Fixed step both ports with faster sampling at port
1`.

### **Port 2 network discrete sample time (s)** — Specify sample time for Network 2 `0.01` (default) | positive scalar

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

### **Approximate mass at port 1 (kg)** — Specify approximate mass at port 1 `1` (default) | positive scalar

Specify approximate mass at port **1**, in kg.

### **Approximate mass at port 2 (kg)** — Specify approximate mass at port 2 `1` (default) | positive scalar

Specify approximate mass at port **2**, in kg.

For information on how to use the **Derived values** section, see Using the Derived Values to Estimate Block Parameters.

### Initial Conditions

### **Initial transmitted force (N)** — Specify initial force transmitted by the link `0` (default) | positive scalar

Specify initial condition for the force transmitted by the link, in N.
## Libraries

Simscape / Utilities / Network Couplers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Split network at a mechanical translational connection

The Network Coupler (Compressible Link) block provides a starting point for
you to split a Simscape™ network into two coupled networks at a mechanical translational
connection.

The Network Coupler (Compressible Link) block works by adding a compliance
between the two networks. It is assumed that there is a mass on either side of the coupler
block. Do not connect the block ports directly to a force source. You can connect the block
ports to an ideal translational velocity source.

If your model has an existing compressible link (modeled as a Translational
Spring block connected in parallel with a Translational
Damper block), then use the Network Coupler (Compressible
Link) block to directly replace these two blocks. This avoids adding a second
compliance with which to separate the network. If there is no existing model compliance that
you can use, then add a numeric one by inserting the Network Coupler (Compressible
Link) block at a mechanical translational connection and setting its
**Separate using** parameter to `an added numerical
compliance`.

### Working with the Block on the Model Canvas

When you add the block to your model and double-click it, the Network Coupler
(Compressible Link) subsystem opens.

Network Coupler (Compressible Link) subsystem diagram

The Port 1 Interface block contains the dynamics that
break the algebraic loop. Double-click this block to set all of the Network Coupler
(Compressible Link) subsystem parameters and view the derived values.

The rate transition blocks are, by default, commented through. Uncomment them if at least one of the coupled networks is running fixed step.

### Using the Derived Values to Estimate Block Parameters

On the **Analysis** tab of the Port 1 Interface block dialog box, the **Derived values** section contains a list of recommended values that you can use when specifying block parameters. For example, use the **Recommended max discrete sample time (s)** derived value to verify that your **Port 1 network discrete sample time (s)** and **Port 2 network discrete sample time (s)** parameter values are within acceptable limits.

The derived values list is based on the chosen block configuration. For example:

- If you are using an existing compliance, the block uses information about the
  masses of the connected networks, plus the compliance, to recommend either a maximum
  filter time constant, or a maximum discrete sample time. To do this, the block
  calculates overall network dynamic time constants and recommends the time constant
  (**Recommended max filter time constant (s)**) or sample time
  (**Recommended max discrete sample time (s)**) values that are
  commensurate with the fastest time constant.
- If you are adding a numeric compliance, the block calculates the stiffness and
  damping required, based on the connected network masses and the specified sample time
  or filter time constant. It also provides an estimate of the fastest trackable time
  constant. If the **Calculated fastest trackable time constant (s)**
  value is too slow for your application, then you must reduce the value you specified
  for the relevant block parameter, such as **Separator time constant
  (s)**, **Port 1 network discrete sample time (s)**, or
  **Port 2 network discrete sample time (s)**.

The **Update** button lets you recalculate
the derived values after you change the parameters of the connected networks.
