---
type: simulink-block
title: 'Network Coupler (Voltage-Current)'
family: 'utilities'
product_id: 'network-couplers'
product_name: 'Network Couplers'
documentation_release: R2025b
official_category: 'Network Couplers'
documentation_page: 'networkcouplervoltagecurrent'
documentation_source_path: '../simscape/ref/networkcouplervoltagecurrent.html'
language: en
---

# Network Coupler (Voltage-Current)

## Ports

### Conserving

### **1** — Connect this port to the variable-step network, or to the fixed-step network with the smaller sample time electrical | three-phase electrical | electrical node array

If one of the coupled networks is running variable step, connect it to port
**1** of the Network Coupler (Voltage-Current)
block. If both networks are running fixed step, connect this port to the network with
the smaller sample time. If both networks are running variable step, or fixed step
with the same step size, then the block polarity does not matter.

### **2** — Connect this port to the fixed-step network with the larger sample time electrical | three-phase electrical | electrical node array

If one of the coupled networks is running variable step, connect port
**2** of the Network Coupler (Voltage-Current) block
to the fixed-step network. If both networks are running fixed step, connect this port
to the network with the larger sample time.

## Parameters

### Main

### **Use three-phase electrical connections** — Break connections between three-phase electrical ports off (default) | on

Select this check box when breaking connections between three-phase electrical
ports. Because the top-level subsystem is unmasked, you need to select this check box
both for Port 1 Interface and Port 2 Interface blocks.
Selecting this check box disables the **Electrical node array size**
parameter because ports **1** and **2** become
three-phase electrical ports.

### **Electrical node array size** — Specify number of electrical nodes `1` (default) | positive integer

Specify the size of the electrical node array connected to the two electrical
ports, **1** and **2**. Because the top-level
subsystem is unmasked, you need to set this parameter to the same value both for
Port 1 Interface and Port 2 Interface blocks.

If you are breaking a regular electrical connection, leave the default value of
`1` unchanged.

#### Dependencies

To enable this parameter, clear the **Use three-phase electrical
connections** check box.

### **Sampling type** — Select sampling types scenario for coupled networks `Variable step at ports 1 and 2` (default) | `Variable step at port 1 and fixed step at port 2` | `Fixed step both ports with common sample time` | `Fixed step both ports with faster sampling at port 1`

Select how the coupled networks are sampled:

- `Variable step at ports 1 and 2` — Both networks are variable-step.
- `Variable step at port 1 and fixed step at port 2` — Network 1 is variable-step and Network 2 is fixed-step.
- `Fixed step both ports with common sample time` — Both networks are fixed-step, with the same step size.
- `Fixed step both ports with faster sampling at port 1` — Both
  networks are fixed-step, with different step sizes.

### **Separator time constant (s)** — Specify filter time constant `1e-3` (default) | positive scalar

Specify the filter time constant, in seconds, to remove the algebraic loop.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Variable step at ports 1 and 2`.

### **Port 1 network discrete sample time (s)** — Specify sample time for Network 1 `0.0002` (default) | positive scalar

Specify sample time for Network 1, in seconds.

#### Dependencies

To enable this parameter, set the **Sampling type** parameter
to `Fixed step both ports with common sample time` or
`Fixed step both ports with faster sampling at port
1`.

### **Port 2 network discrete sample time (s)** — Specify sample time for Network 2 `0.001` (default) | positive scalar

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

For information on how to use the **Derived values** section, see Using the Derived Values to Estimate Block Parameters.

### Initial Conditions

### **Initial current (A)** — Specify initial current transmitted by the coupler `0` (default) | positive scalar

Specify initial condition for the current transmitted by the coupler, in A.

### **Initial voltage (V)** — Specify initial voltage across the coupler `0` (default) | positive scalar

Specify initial condition for the voltage across the coupler, in V.

## Libraries

Simscape / Utilities / Network Couplers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2024a: Break connections between arrays of electrical nodes

The block now supports arrays of electrical nodes and three-phase connections. The new
parameter, **Electrical node array size**, lets you specify the array size.
Alternatively, you can use the new check box, **Use three-phase electrical
connections**. If you look under mask, the Port 1 Interface and
Port 2 Interface subsystems contain custom blocks that support vectorized
electrical nodes, instead of the regular Foundation library electrical blocks.

This change has no compatibility impact. The default values of the **Use
three-phase electrical connections** check box and the **Electrical node
array size** parameter correspond to a regular electrical connection. If you open
an existing model containing this block, the simulation results are the same as in previous
releases.

## Description

Split network at an electrical connection

The Network Coupler (Voltage-Current) block provides a starting point for
you to split a Simscape™ network into two coupled networks at an electrical connection. Use this block
when Network 1 (as described in Naming Conventions) has series-connected
inductors or current sources, but Network 2 does not.

This block changes the behavior of the system because it adds a first-order lag to break
the algebraic loop.

Port 1 interface of the Network Coupler (Current-Voltage) block is
implemented as a voltage source. Therefore, you cannot connect this port to a voltage loop,
such as a set of series-connected voltage sources and capacitors, because this would cause an
Index-2 topology (for more information, see Avoiding Numerical Simulation Issues). Port 2
interface is implemented as a current source. Therefore, you cannot connect this port to a
series-connected inductor or current source because this would also cause an Index-2
topology.

To facilitate working with models that contain arrays of electrical nodes or three-phase
connection, the Port 1 Interface and Port 2 Interface subsystems
contain custom blocks, such as Controlled Voltage Source or Current
Sensor. These custom blocks are based on the equivalent Foundation library blocks
but are modified to support vectorized and three-phase electrical nodes. The source files for
these custom blocks are located in the following namespace:

```
matlabroot/toolbox/physmod/simscape/library/m/+foundation/+internal/+couplers/+electrical
```

where *`matlabroot`* is the MATLAB® root directory on your machine, as returned by entering

```
matlabroot
```

at the MATLAB command prompt. The namespace contains source files for voltage and current
sources and sensors, as well as a resistor and an electrical reference with array and
three-phase support. You can use these blocks to customize your network coupler
configuration.

### Working with the Block on the Model Canvas

When you add the block to your model and double-click it, the Network Coupler
(Voltage-Current) subsystem opens.

Network Coupler (Voltage-Current) subsystem diagram

The Port 1 Interface block contains the dynamics that break the algebraic
loop. Double-click this block to set all of the Network Coupler
(Voltage-Current) subsystem parameters and view the derived values.

The rate transition blocks are, by default, commented through. Uncomment them if at least one of the coupled networks is running fixed step.

### Using the Derived Values to Estimate Block Parameters

On the **Analysis** tab of the Port 1
Interface block dialog box, the **Derived values** section contains
the **Calculated fastest trackable time constant (s)** value, based on the
impact of the coupler lag. If both networks are variable-step, then you specify the filter time
constant directly, as a block parameter. If at least one of the networks is fixed-step, the
block calculates the time constant automatically based on the sample times that you specify, and
the **Derived values** section displays the **Calculated filter time
constant (s)** value.

The **Update** button lets you recalculate
the derived values after you change the parameters of the connected networks.
