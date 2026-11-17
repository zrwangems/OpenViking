---
type: simulink-block
title: 'Barrier Certificate Enforcement'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Constraint Control'
documentation_page: 'barriercertificateenforcement'
documentation_source_path: 'ug/barriercertificateenforcement.html'
language: en
---

# Barrier Certificate Enforcement

## Ports
```yaml
ports:
- name: u0
  summary: Control actions scalar | vector
  direction: input
- name: fx
  summary: State function scalar | vector
  direction: input
- name: gx
  summary: Input function scalar | vector | matrix
  direction: input
- name: hx
  summary: Control barrier function scalar | vector
  direction: input
- name: qx
  summary: Partial derivative of control barrier function scalar | vector | matrix
  direction: input
- name: umax
  summary: Action signal upper bounds scalar | vector
  direction: input
- name: umin
  summary: Action signal lower bounds scalar | vector
  direction: input
- name: u\*
  summary: Modified control action scalar | vector
  direction: output
- name: exitflag
  summary: Optimization status 1 | 0 | negative integer
  direction: output
```

### Input

### **u0** — Control actions scalar | vector

Unmodified control actions, specified as a scalar or a vector.

If the **Number of actions** parameter is
`1`, connect **u0** to a scalar
signal. Otherwise, connect **u0** to a vector signal
with length equal to **Number of actions**.

### **fx** — State function scalar | vector

State function *f*(*x*) in the
following plant dynamics equation.

x˙=f(x)+g(x)u

Connect **fx** to an
*Nx*-by-1 signal, where
*Nx* is equal to the
**Number of states** parameter.

### **gx** — Input function scalar | vector | matrix

Input function *g*(*x*) in the
following plant dynamics equation.

x˙=f(x)+g(x)u

Connect **gx** to an
*Nx*-by-*Nu*
signal, where *Nx* is equal to
the **Number of states** parameter and
*Nu* is equal to the
**Number of actions** parameter.

### **hx** — Control barrier function scalar | vector

Control barrier function, defined as the following safety set for plant states.

{x:h(x)≥0}

Connect **hx** to an
*Nc*-by-1 signal, where
*Nc* is equal to the
**Number of barrier certificates**
parameter.

### **qx** — Partial derivative of control barrier function scalar | vector | matrix

Partial derivative of the control barrier function over plant
states.

q(x)=∂h∂x

Connect **qx** to an
*Nc*-by-*Nx*
signal, where *Nc* is equal to
the **Number of barrier certificates** parameter and
*Nx* is equal to the
**Number of states** parameter.

### **umax** — Action signal upper bounds scalar | vector

To specify run-time upper bounds to the action signals, enable this
input port. If this port is disabled, the block does not apply any upper
bounds to the control actions.

If the **Number of actions** parameter is
`1`, connect **umax** to a scalar
signal. Otherwise, connect **umax** to a vector signal
with length equal to **Number of actions**.

#### Dependencies

To enable this input port, select the **Use external
source for upper bound** parameter.

### **umin** — Action signal lower bounds scalar | vector

To specify run-time lower bounds to the action signals, enable this
input port. If this port is disabled, the block does not apply any lower
bounds to the control actions.

If the **Number of actions** parameter is
`1`, connect **umin** to a scalar
signal. Otherwise, connect **umin** to a vector signal
with length equal to **Number of actions**.

#### Dependencies

To enable this input port, select the **Use external
source for lower bound** parameter.
### Output

### **u\*** — Modified control action scalar | vector

Modified control action returned by the QP solver.

If the solver finds a solution before reaching the maximum number of
iterations, **u\*** outputs this optimal
solution.

If the solver reaches the maximum number of iterations, optimization
stops and **u\*** outputs a suboptimal solution.

If the initial optimization problem is infeasible, the returned
control action depends on the whether the block is configured to ignore
constraint or action bounds. For more information, see the
**exitflag** parameter.

If the **Number of actions** parameter is
`1`, **u\*** outputs a scalar
signal. Otherwise, **u\*** outputs a vector signal with
length equal to **Number of actions**.

### **exitflag** — Optimization status `1` | `0` | negative integer

Optimization status of the QP solver. The following table shows the
possible status values.

| Exit Flag | Description |
| --- | --- |
| `1` | The solver converged to an optimal solution with all constraints and bounds active. In this case, **u\*** outputs the optimal control actions. |
| `0` | The solver reached the maximum number of iterations. The control actions output in **u\*** might be suboptimal. |
| negative integer | The initial optimization problem was infeasible and one of the following scenarios applies.  - Rerunning the optimization without action   bounds did not produce a feasible solution. - Rerunning the optimization without   constraint bounds did not produce a feasible   solution.  In this case, the control actions output in **u\*** are zero. |

#### Dependencies

To enable this output port, select the **Optimization
status** parameter.
## Parameters
```yaml
parameters:
- name: Number of states
  summary: Number of plant states 1 (default) | positive integer
  group: ''
  block_parameter: nx
  type: character vector
  default: '''1'''
- name: Number of actions
  summary: Number of control actions 1 (default) | positive integer
  group: ''
  block_parameter: nu
  type: character vector
  default: '''1'''
- name: Number of barrier certificates
  summary: Number of barrier certificate constraints 1 (default) | positive integer
  group: ''
  block_parameter: nc
  type: character vector
  default: '''1'''
- name: Constraint factor
  summary: Constraint factor 10 (default) | positive scalar | vector
  group: ''
  block_parameter: gamma
  type: character vector
  default: '''10'''
- name: Constraint power
  summary: Constraint power 1 (default) | positive odd integer | vector
  group: ''
  block_parameter: beta
  type: character vector
  default: '''1'''
- name: Use external source for upper bound
  summary: Add upper action bound input port off (default) | on
  group: ''
  block_parameter: external_umax
  type: character vector
  values: '''off''|''on'''
  default: '''off'''
- name: Use external source for lower bound
  summary: Add lower action bound input port off (default) | on
  group: ''
  block_parameter: external_umin
  type: character vector
  values: '''off''|''on'''
  default: '''off'''
- name: Sample time
  summary: Optimization sample time 0.1 (default) | positive scalar
  group: ''
  block_parameter: Ts
  type: character vector
  default: '''0.1'''
- name: Maximum iterations
  summary: Maximum optimization iterations 200 (default) | positive integer
  group: ''
  block_parameter: maxiter
  type: character vector
  default: '''200'''
- name: Constraint tolerance
  summary: Tolerance for constraint violations 1e-6 (default) | nonnegative scalar
  group: ''
  block_parameter: tol
  type: character vector
  default: '''1e-6'''
- name: Optimization status
  summary: Add exit flag output port off (default) | on
  group: ''
  block_parameter: exitflag
  type: character vector
  values: '''off''|''on'''
  default: '''off'''
```

#### Parameters Tab

### **Number of states** — Number of plant states `1` (default) | positive integer

Specify the number of states in your plant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nx` |
| **Type:** character vector |
| **Default:** `'1'` |

### **Number of actions** — Number of control actions `1` (default) | positive integer

Specify the number of actions to apply bounds to and optimize.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nu` |
| **Type:** character vector |
| **Default:** `'1'` |

### **Number of barrier certificates** — Number of barrier certificate constraints `1` (default) | positive integer

Specify the number of barrier certificate constraints to enforce.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nc` |
| **Type:** character vector |
| **Default:** `'1'` |

### **Constraint factor** — Constraint factor `10` (default) | positive scalar | vector

Specify the constraint factor *γ* in the barrier certificate
constraint.

If the **Number of barrier certificates** parameter is
`1`, specify **Constraint factor** as
a finite positive scalar. Otherwise, you can specify **Constraint
factor** as either a finite positive scalar value or a column
vector of positive scalars with length equal to **Number of barrier
certificates**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `gamma` |
| **Type:** character vector |
| **Default:** `'10'` |

### **Constraint power** — Constraint power `1` (default) | positive odd integer | vector

Specify the constraint power *β* in the barrier certificate
constraint.

If the **Number of barrier certificates** parameter is
`1`, specify **Constraint power** as a
positive odd integer. Otherwise, you can specify **Constraint
power** as either a positive odd integer or a column vector of
positive odd integers with length equal to **Number of barrier
certificates**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `beta` |
| **Type:** character vector |
| **Default:** `'1'` |

### **Use external source for upper bound** — Add upper action bound input port `off` (default) | `on`

Select this parameter to add the **umax** input port for
external upper action bounds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `external_umax` |
| **Type:** character vector |
| **Values:** `'off'`|`'on'` |
| **Default:** `'off'` |

### **Use external source for lower bound** — Add lower action bound input port off (default) | on

Select this parameter to add the **umin** input port for
external lower action bounds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `external_umin` |
| **Type:** character vector |
| **Values:** `'off'`|`'on'` |
| **Default:** `'off'` |

#### Block Tab

### **Sample time** — Optimization sample time `0.1` (default) | positive scalar

Specify the sample time for running the optimization.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Ts` |
| **Type:** character vector |
| **Default:** `'0.1'` |

### **Maximum iterations** — Maximum optimization iterations `200` (default) | positive integer

Specify the maximum number of optimization iterations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `maxiter` |
| **Type:** character vector |
| **Default:** `'200'` |

### **Constraint tolerance** — Tolerance for constraint violations `1e-6` (default) | nonnegative scalar

Specify a tolerance value for constraint violations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `tol` |
| **Type:** character vector |
| **Default:** `'1e-6'` |

### **Optimization status** — Add exit flag output port `off` (default) | `on`

Select this parameter to add the **exitflag** output port
for the optimization status of the QP solver.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `exitflag` |
| **Type:** character vector |
| **Values:** `'off'`|`'on'` |
| **Default:** `'off'` |
## Libraries

Simulink Control Design / Constraint Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Barrier Certificate Enforcement block supports code generation
for double-precision signals only.

## Version History

**Introduced in R2022a**

### R2023b: Library location changed

The Barrier Certificate Enforcement block is now in the
**Simulink Control Design/Constraint Control**
sublibrary.

In R2023b, when you open a model saved in a previous release, the library links
for Barrier Certificate Enforcement blocks update
automatically.

## Description

Modify control actions to satisfy barrier certificate constraints and action bounds

The Barrier Certificate Enforcement block computes the modified control
actions that are closest to specified control actions subject to barrier certificate
constraints and action bounds.

The block uses a quadratic programming (QP) solver to find the control action
*u* that minimizes the function |u−u0|2. Here, *u*0 is the unmodified
control action.

The solver applies the following constraints to the optimization problem.

qxfx+qxgxu+γhxβ≥0umin≤u≤umax

Here:

- *f*x** and
  *g*x** are
  functions defined by the plant dynamics x˙=f(x)+g(x)u.
- *h*x** is the control
  barrier function.
- *q*x** is the partial
  derivative of the control barrier function over states
  *x*.
- *γ* is the constraint factor.
- *β* is the constraint power.
- *u*min is a lower bound for the
  control action.
- *u*max is an upper bound for the
  control action.

The Barrier Certificate Enforcement block requires Optimization Toolbox™ software.

For more information on barrier certificate enforcement, see Barrier Certificate Enforcement for Control Design.
