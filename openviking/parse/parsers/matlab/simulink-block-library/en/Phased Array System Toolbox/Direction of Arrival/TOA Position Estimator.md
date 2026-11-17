---
type: simulink-block
title: 'TOA Position Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'toapositionestimator'
documentation_source_path: 'ref/toapositionestimator.html'
language: en
---

# TOA Position Estimator

## Ports
```yaml
ports:
- name: TOAest
  summary: Estimated times of arrival 1-by-*L* element real-valued vector
  direction: input
  data_types: single | double
- name: TOAVar
  summary: Variance of estimated times of arrival 1-by-*L* element real-valued vector
  direction: input
  data_types: single | double
- name: AnchorPos
  summary: Anchor positions 2-by-*L* real-valued matrix | 3-by-*L* real-valued matrix
  direction: input
  data_types: single | double
- name: TgtPosEst
  summary: Estimated target positions real-valued *Q*-by-1 vector
  direction: output
- name: TgtPosCov
  summary: Target position covariance matrix real-valued positive semi-definite *Q*-by-*Q* matrix
  direction: output
  data_types: single | double
```

### Input

### **TOAest** — Estimated times of arrival 1-by-*L* element real-valued vector

Estimated times of arrival of signals between anchors and single target, specified
as a 1-by-*L* element real-valued vector. Units are in
seconds.

**Data Types:** `single` | `double`

### **TOAVar** — Variance of estimated times of arrival 1-by-*L* element real-valued vector

Variances of the estimated times of arrival at anchors, specified as a
1-by-*L* element real-valued vector.

When `toavar` is unknown, you can set it to be a
1-by-*L* element vector with identical finite values without
affecting the solution `tgtposest`.

**Data Types:** `single` | `double`

### **AnchorPos** — Anchor positions 2-by-*L* real-valued matrix | 3-by-*L* real-valued matrix

Anchor positions, specified as 2-by-*L* real-valued matrix or
3-by-*L* real-valued matrix. A 2-by-*L* matrix
represents the anchor positions in 2-D Cartesian space, while a
3-by-*L* matrix represents the anchor positions in 3-D Cartesian
space.

**Data Types:** `single` | `double`
### Output

### **TgtPosEst** — Estimated target positions real-valued *Q*-by-1 vector

Estimated target positions, returned as a *Q*-by-1 vector
representing the estimated target position obtained from TOA and TDOA measurements.
Units are in meters.

### **TgtPosCov** — Target position covariance matrix real-valued positive semi-definite *Q*-by-*Q* matrix

Target position covariance matrix, returned as a real-valued positive
semi-definite *Q*-by-*Q* matrix. The covariance
matrix represents the estimated target position covariance calculated from the
Cramer-Rao lower bound (CRLB) of the TOA position estimator. Calculating the
covariance requires the knowledge of `toavar`. When
`toavar` is inaccurate, `tgtposcov` is also
inaccurate. When `toavar` is accurate and small, the
`tgtposcov` value represents the TOA position estimate CRLB.
Units are in ㎡eters-squared.

#### Dependencies

To enable this output port, select the **Output covariance of TOA
position estimate** check box.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: Signal propagation speed physconst("LightSpeed") (default) | positive real scalar
  group: ''
- name: Output covariance of TOA position estimate
  summary: Output covariance of TDOA position estimates false (0) (default) | true (1)
  group: ''
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst("LightSpeed")` (default) | positive real scalar

Signal propagation speed, specified as a positive real scalar. Units are in meters
per second.

**Example:** `3e8`

**Data Types:** `single` | `double`

### **Output covariance of TOA position estimate** — Output covariance of TDOA position estimates `false` (0) (default) | `true` (1)

Select the **Output covariance of TOA position estimates** check
box to enable the **TgtPosCov** output port containing the TOA position
covariances.

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
## Libraries

Phased Array System Toolbox / Direction of Arrival

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Estimate target position from time-of-arrival estimates and anchor positions

Estimate target position from time-of-arrival estimates and anchor positions
