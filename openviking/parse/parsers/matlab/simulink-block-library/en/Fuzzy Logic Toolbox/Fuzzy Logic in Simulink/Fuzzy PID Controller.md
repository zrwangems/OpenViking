---
type: simulink-block
title: 'Fuzzy PID Controller'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Fuzzy Logic in Simulink'
documentation_page: 'fuzzypidcontroller'
documentation_source_path: 'fuzzypidcontroller.html'
language: en
---

# Fuzzy PID Controller

## Ports

### Input

### **r** — Reference scalar

Reference signal to track.

### **y** — Plant output scalar

Output of the system under control.
### Output

### **u** — Controller output scalar

Controller output, based on a sum of the PI, PD, and feedforward controller
paths.

### **e** — Error scalar

Difference between the reference signal **r** and plant output
**y**. Use this output for tracking error metrics, such as the
integral of absolute (IAE).

#### Dependencies

- To enable this port, select the **Add error (e) output**
  parameter.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Controller Options

### **Time Domain** — Controller time domain **Discrete-time** (default) | **Continuous-time**

Specify either a discrete-time or continuous-time controller.

When you select **Discrete-time**, it is recommended that you
specify an explicit sample time for the block using the **Sample
time** parameter. Selecting **Discrete-time** also enables
the **Integrator method**, and **Filter method**
parameters.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `TimeDomainType` |
| **Values:** | `"Discrete-time"` (default) | `"Continuous-time"` |

### **Ce** — Gain for error `1` (default) | scalar

Specify a gain factor to scale the error signal to the range of the corresponding
input variable of the FIS.

For more information on selecting initial controller gains, see Derive Controller Gains from Conventional PID Gains.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `CE` |
| **Values:** | `"1"` (default) | nonnegative scalar in quotes |

### **Cd** — Gain for derivative signal `1` (default) | scalar

Specify the gain factor applied to the derivative signal before it enters the
FIS.

This gain factor is also applied in the reference feedforward path when
**Derivative signal** is `Process output
(y)`.

For more information on selecting initial controller gains, see Derive Controller Gains from Conventional PID Gains.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `CD` |
| **Values:** | `"1"` | nonnegative scalar in quotes |

### **C0** — Gain for change in FIS output `1` (default) | scalar

Specify the gain factor applied to the FIS output in the PI control branch.

This gain factor is also applied in the reference feedforward path when
**Derivative signal** is `Process output
(y)`.

To design a PD controller, set **C0** to zero.

For more information on selecting initial controller gains, see Derive Controller Gains from Conventional PID Gains.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `C0` |
| **Values:** | `"1"` | nonnegative scalar in quotes |

### **C1** — Gain for FIS output `1` (default) | scalar

Specify the gain factor applied to the FIS output in the PD control path.

To design a PI controller, set **C1** to zero.

For more information on selecting initial controller gains, see Derive Controller Gains from Conventional PID Gains.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `C1` |
| **Values:** | `"1"` | nonnegative scalar in quotes |

### **Integrator method** — Method for computing integral in discrete-time controller `Forward Euler` (default) | `Backward Euler` | `Trapezoidal`

In discrete time, the integral term of the controller transfer function is
*Iα*(*z*), where
*α*(*z*) depends on the integrator method you
specify with this parameter.

You can specify one of the following integration methods:

- `Forward Euler` — Forward rectangular
  (left-hand)
- `Backward Euler` — Backward rectangular (right-hand)
  approximation
- `Trapezoidal` — Bilinear approximation

For more information about the filtered derivative, see the **Integrator method (Simulink)** parameter of the PID Controller
block.

#### Dependencies

- To enable this parameter, set the **Time Domain** parameter
  to **Discrete-time**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `IntegratorMethod` |
| **Values:** | `"Forward Euler"` (default) | `"Backward Euler"` | `"Trapezoidal"` |

### **Use accumulator** — Accumulate signal in integrator `off` (default) | `on`

Select this parameter to accumulate signal in the integration stage.

When you clear **Use accumulator**, the integration sample time
for the controller is the block sample time, as specified in the **Sample
time** parameter.

When you select **Use accumulator**, the integration sample time
for the controller is 1. In this case, the block sample time determines when the
integral output is computed but does not impact the integral output value.

When you use an accumulator, multiply **C0** by the
**Sample time**.

#### Dependencies

- To enable this parameter, set the **Time Domain** parameter
  to **Discrete-time**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `UseAccumulator` |
| **Values:** | `"off"` (default) | `"on"` |

### **Derivative signal** — Signal used for computing derivative `Error (e)` (default) | `Process output (y)`

Compute the derivative from one of the following signals:

- `Error (e)` —Use the error signal, which is the
  difference between the plant output and the reference signal, as shown in the
  following figure.

  Fuzzy PID controller structure with the error signal used for computing the derivative.
- `Process output (y)` — Use the plant output directly,
  as shown in the following figure. When you select this option, the controller
  includes a feedforward path from the reference signal to the controller
  output.

  Fuzzy PID controller structure with the plant output used for computing the derivative. The controller now includes a feedforward path that contains the Cd and C0 controller gains.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `DerivativeSignal` |
| **Values:** | `"Error (e)"` (default) | `"Process output (y)"` |

### **Use filtered derivative** — Apply filter to derivative term `on` (default) | `off`

For discrete-time controllers, clear this option to replace the filtered
derivative with an unfiltered discrete-time differentiator with pole locations that
depend on the **Filter method** parameter.

For continuous-time controllers, the derivative term is always filtered.

For more information about the filtered derivative, see the **Use filtered derivative (Simulink)** parameter of the PID Controller
block.

#### Dependencies

To enable this parameter, set **Time domain** to
**Discrete-time**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `UseFilter` |
| **Values:** | `"on"` (default) | `"off"` |

### **Filter coefficient** — Derivative filter coefficient `100` (default) | positive scalar

Specify a finite, real gain value for the filter coefficient. The filter
coefficient determines the pole location of the filter in the derivative action of the
block. The location of the filter pole depends on the **Time
domain** parameter.

For more information about the filter coefficient and its impact on pole
locations, see the **Filter coefficient (N) (Simulink)** parameter of the PID Controller
block.

#### Dependencies

- To enable this parameter for discrete-time controllers, select the
  **Use filtered derivative** parameter.
- This parameter is always enabled for continuous-time controllers.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `N` |
| **Values:** | `"100"` (default) | positive scalar in quotes |

### **Filter method** — Method for computing derivative in discrete-time controller `Forward Euler` (default) | `Backward Euler` | `Trapezoidal`

You can specify one of the following filter methods for the derivative term of the
controller:

- `Forward Euler` — Forward rectangular
  (left-hand)
- `Backward Euler` — Backward rectangular (right-hand)
  approximation
- `Trapezoidal` — Bilinear approximation

For more information about these methods, see the **Filter method (Simulink)** parameter of the PID Controller
block.

#### Dependencies

- To enable this parameter, set the **Time Domain** parameter
  to **Discrete-time** and select the **Use filtered
  derivative** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `DerivativeFilterMethod` |
| **Values:** | `"Forward Euler"` (default) | `"Backward Euler"` | `"Trapezoidal"` |

### **Add error (e) output** — Enable `e` output port `off` (default) | `on`

Enable **e** output port for accessing the error signal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `E` |
| **Values:** | `"off"` (default) | `"on"` |

### **Sample time (–1 for inherited)** — Sample time `-1` (default) | positive scalar

Specify a sample time by entering a positive scalar value, such as 0.1. The
default discrete sample time of –1 means that the block inherits its sample time from
upstream blocks. However, it is recommended that you set the controller sample time
explicitly, especially if you expect the sample time of upstream blocks to change. The
effect of the controller coefficients depend on the sample time. Thus, for a given set
of coefficient values, changing the sample time changes the performance of the
controller.

#### Dependencies

- To enable this parameter, set the **Time Domain** parameter
  to **Discrete-time**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | positive scalar in quotes |

### Fuzzy Inference System

### **FIS name** — Fuzzy inference system `mamfis` object | `sugfis` object | `mamfistype2` object | `sugfistype2` object | FIS file name in quotes | MAT file name in quotes

Fuzzy inference system, specified as one of the following:

- `mamfis` or
  `sugfis`
  object — Specify the name of a type-1 FIS object in the MATLAB® workspace.
- `mamfistype2` or `sugfistype2` object — Specify the name of a type-2 FIS object in the
  MATLAB workspace.
- Name of a FIS file (`*.fis`) in the current working folder or
  on the MATLAB path. Including the file extension in the file name is optional.
  Specify the filename in quotes.
- Name of a MAT file (`*.mat`) in the current working folder or
  on the MATLAB path. The MAT file must contain only one FIS object. Including the
  file extension in the file name is optional. Specify the filename in
  quotes.

The FIS must have two input variables (error signal and derivative signal) and one
output variable.

The default FIS, `fuzzycontroller`, is a linear FIS configured to
allow easier selection of fuzzy PID controller gains based on specified conventional
PID controller gains. For more information about this FIS, see Default FIS.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `FIS` |
| **Values:** | `'"fuzzycontroller"'` (default) | variable name in quotes | file name in quotes |

### **Number of samples for output discretization** — Number of points in output fuzzy sets 101 (default) | integer greater than `1`

Number of samples for discretizing the range of FIS output variables, specified as an integer greater than `1`. This value corresponds to the number of points in the output fuzzy set for each rule.

To reduce memory usage while evaluating Mamdani FISs, specify a lower number of samples. Doing so sacrifices the accuracy of the defuzzified output value. Specifying a low number of samples can make the output area for defuzzification zero. In this case, the defuzzified output value is the midpoint of the output variable range.

**Note**

The block ignores this parameter when evaluating Sugeno FISs.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputSampleNumber` |
| **Values:** | `"101"` (default) | integer greater than `1` in quotes |

### **Implement FIS as lookup table** — Convert FIS to lookup table `off` (default) | `on`

To reduce the processing time for the controller, you can represent your FIS as a
lookup table.

The block divides the input range of each FIS input into equally sized regions
based on the number of breakpoints, which you specify using the **Number of
input breakpoints** parameter.

For each input combination, the block calculates a corresponding FIS output.
During evaluation, the controller uses these precomputed outputs instead of performing
the fuzzy inference process.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `UseLookupTable` |
| **Values:** | `"off"` (default) | `"on"` |

### **Number of input breakpoints (samples)** — Number of lookup table breakpoints `10` (default) | positive integer

Number of lookup table breakpoints, specified as a positive integer. Increasing
the number of breakpoints improves the accuracy of the lookup table while increasing
its memory requirements.

#### Dependencies

- To enable this parameter, select the **Implement FIS as lookup
  table** parameter.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `NumBreakpoints` |
| **Values:** | `"10"` (default) | positive integer in quotes |

## Libraries

Fuzzy Logic Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Continuous-time controller:

  - Not recommended for production code.
- Discrete-time controller:

  - Depends on absolute time when placed inside a triggered subsystem
    hierarchy.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced in R2024b**

## Description

Fuzzy logic-based PID controller

The Fuzzy PID Controller block implements a PID controller with a single
Fuzzy Logic Controller block and parallel structure. The control architecture
is shown in the following figure.

Fuzzy PID controller structure

For this controller:

- The inputs to the block are the reference signal (*r*) and the plant
  output (*y*).
- The inputs to the FIS are the error (*E*) and the change in error
  (*ΔE*).
- The error signal is scaled by gain factor
  *Ce*.
- The change in error is scaled by gain factor
  *Cd*.
- The FIS has a single output that splits into a PI control branch and a PD control
  branch.
- The PI control branch contains gain *C0* and
  an integrator.
- The PD control branch contains gain
  *C1*.
- The control signal output by the block is the sum of the PI and PD branches.

For more information on this controller structure, see [1].
