---
type: simulink-block
title: 'Constraint Enforcement'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Constraint Enforcement'
documentation_page: 'constraintenforcement'
documentation_source_path: 'ug/constraintenforcement.html'
language: en
---

# Constraint Enforcement

## Ports

### Input

### **u0** — Control actions scalar | vector

Unmodified control actions, specified as a scalar or a vector.

If the **Number of actions** parameter is `1`,
connect **u0** to a scalar signal. Otherwise, connect
**u0** to a vector signal with length equal to **Number of
actions**.

### **fx** — Constraint function offset coefficient scalar | vector

Offset coefficient *fx* in the following
constraint equation.

fx+gxu≤c

If the **Number of constraints** parameter is
`1`, connect **fx** to a scalar signal. Otherwise,
connect **fx** to a vector signal with length equal to
**Number of constraints**.

### **gx** — Constraint function linear coefficient scalar | vector | matrix

Linear coefficient *gx* in the following
constraint equation.

fx+gxu≤c

Connect **gx** to an
*Nc*-by-*Nu*
signal, where *Nc* is equal to the
**Number of constraints** parameter and
*Nu* is equal to the **Number of
actions** parameter.

### **c** — Constraint bounds scalar | vector

Run-time constraint bound *c* in the following constraint
function.

fx+gxu≤c

If the **Number of constraints** parameter is
`1`, connect **c** to a scalar signal. Otherwise,
connect **c** to a vector signal with length equal to
**Number of constraints**.

If this port is disabled, the block uses the constant constraint bounds specified
using the **Constraint bound** parameter.

#### Dependencies

To enable this input port, select the **Use external source**
parameter.

### **umax** — Action signal upper bounds scalar | vector

To specify run-time upper bounds to the action signals, enable this input port. If
this port is disabled, the block does not apply any upper bounds to the control
actions.

If the **Number of actions** parameter is `1`,
connect **umax** to a scalar signal. Otherwise, connect
**umax** to a vector signal with length equal to **Number
of actions**.

#### Dependencies

To enable this input port, select the **Use external source for upper
bound** parameter.

### **umin** — Action signal lower bounds scalar | vector

To specify run-time lower bounds to the action signals, enable this input port. If
this port is disabled, the block does not apply any lower bounds to the control
actions.

If the **Number of actions** parameter is `1`,
connect **umin** to a scalar signal. Otherwise, connect
**umin** to a vector signal with length equal to **Number
of actions**.

#### Dependencies

To enable this input port, select the **Use external source for lower
bound** parameter.
### Output

### **u\*** — Modified control action scalar | vector

Modified control action returned by the QP solver.

If the solver finds a solution before reaching the maximum number of iterations,
**u\*** outputs this optimal solution.

If the solver reaches the maximum number of iterations, optimization stops and
**u\*** outputs a suboptimal solution.

If the initial optimization problem is infeasible, the returned control action
depends on the whether the block is configured to ignore constraint or action bounds.
For more information, see the **exitflag** parameter.

If the **Number of actions** parameter is `1`,
**u\*** outputs a scalar signal. Otherwise, **u\***
outputs a vector signal with length equal to **Number of
actions**.

### **exitflag** — Optimization status `1` | `2` | `3` | `4` | `0` | negative integer

Optimization status of the QP solver. The following table shows the possible
status values.

| Exit Flag | Description |
| --- | --- |
| `1` | The solver converged to an optimal solution with all constraints and bounds active. In this case, **u\*** outputs the optimal control actions. |
| `2` | The initial optimization problem was infeasible and the block is configured to ignore all constraints and bounds. In this case, **u\*** outputs the unmodified control action **u0**. |
| `3` | The initial optimization problem was infeasible. The block reran the optimization ignoring the action bounds and found a feasible solution, which the block outputs in **u\***. |
| `4` | The initial optimization problem was infeasible. The block reran the optimization ignoring the constraint bounds and found a feasible solution, which the block outputs in **u\***. |
| `0` | The solver reached the maximum number of iterations. The control actions output in **u\*** might be suboptimal. |
| negative integer | The initial optimization problem was infeasible and one of the following scenarios applies.  - Rerunning the optimization without action bounds did not produce a   feasible solution. - Rerunning the optimization without constraint bounds did not produce   a feasible solution. - The block is configured to not ignore constraint and action   bounds.  In this case, the control actions output in **u\*** are zero. |

#### Dependencies

To enable this output port, select the **Optimization status**
parameter.

## Parameters

#### Parameters Tab

### **Number of constraints** — Number of constraints `1` (default) | positive integer

Specify the number of constraints to enforce.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nc` |
| **Type:** character vector |
| **Default:** `'1'` |

### **Number of actions** — Number of actions `1` (default) | positive integer

Specify the number of actions to apply bounds to and optimize.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nu` |
| **Type:** character vector |
| **Default:** `'1'` |

### **Constraint bound** — Constraint bounds `0` (default) | finite scalar | vector

Specify constant bounds for constraints. If the **Number of
constraints** parameter is `1`, specify **Constraint
bound** as a finite scalar. Otherwise, specify **Constraint
bound** as a vector of finite value with length equal to **Number of
constraints**.

If your constraints vary at run time, select the **Use external
source** parameter and connect the run-time constraint signal to the
**c** input port.

#### Dependencies

To enable this parameter, clear the **Use external source**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `c` |
| **Type:** character vector |
| **Default:** `'0'` |

### **Use external source** — Add external constraint bound input port `off` (default) | `on`

Select this parameter to add the **c** input port for external
constraint bounds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `external_c` |
| **Type:** character vector |
| **Values:** `'off'`|`'on'` |
| **Default:** `'off'` |

### **Use external source for upper bound** — Add upper action bound input port `off` (default) | `on`

Select this parameter to add the **umax** input port for external
upper action bounds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `external_umax` |
| **Type:** character vector |
| **Values:** `'off'`|`'on'` |
| **Default:** `'off'` |

### **Use external source for lower bound** — Add lower action bound input port off (default) | on

Select this parameter to add the **umin** input port for external
lower action bounds.

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

Select this parameter to add the **exitflag** output port for the
optimization status of the QP solver.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `exitflag` |
| **Type:** character vector |
| **Values:** `'off'`|`'on'` |
| **Default:** `'off'` |

### **Ignore constraints when QP is infeasible** — Disable constraints when optimization is infeasible `off` (default) | `on`

When you select this parameter, if the initial QP problem is infeasible, the block
reruns the optimization with the constraints disabled.

When you select both this parameter and **Ignore action bounds when QP is
infeasible**, if the initial QP problem is infeasible, the block outputs the
unmodified action signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `relax_c` |
| **Type:** character vector |
| **Values:** `'off'`|`'on'` |
| **Default:** `'off'` |

### **Ignore action bounds when QP is infeasible** — Disable action bounds when optimization is infeasible `off` (default) | `on`

When you select this parameter, if the initial QP problem is infeasible, the block
reruns the optimization with the action bounds disabled. The block ignores this
parameter if both the **umax** and **umin** input
ports are disabled.

When you select both this parameter and **Ignore constraints when QP is
infeasible**, if the initial QP problem is infeasible, the block outputs the
unmodified action signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `relax_u` |
| **Type:** character vector |
| **Values:** `'off'`|`'on'` |
| **Default:** `'off'` |

## Libraries

Simulink Control Design / Constraint Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Constraint Enforcement block supports code generation for
double-precision signals only.

## Version History

**Introduced in R2021a**

### R2023b: Library location changed

The Constraint Enforcement block is now in the **Simulink Control
Design/Constraint Control** sublibrary.

In R2023b, when you open a model saved in a previous release, the library links for
Constraint Enforcement blocks update automatically.

## Description

Modify control actions to satisfy constraints and action bounds

The Constraint Enforcement block computes the modified control actions that
are closest to specified control actions subject to constraints and action bounds.

The block uses a quadratic programming (QP) solver to find the control action
*u* that minimizes the function |u−u0|2. Here, *u*0 is the unmodified
control action.

The solver applies the following constraints to the optimization problem.

fx+gxu≤cumin≤u≤umax

Here:

- *fx* and
  *gx* are coefficients of the constraint
  function.
- *c* is a bound for the constraint function.
- *u*min is a lower bound for the control
  action.
- *u*max is an upper bound for the control
  action.

The Constraint Enforcement block requires Optimization Toolbox™ software.

For more information on constraint enforcement, see Constraint Enforcement for Control Design.
