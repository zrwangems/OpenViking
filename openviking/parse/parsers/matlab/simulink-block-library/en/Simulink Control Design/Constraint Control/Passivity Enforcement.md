---
type: simulink-block
title: 'Passivity Enforcement'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Constraint Control'
documentation_page: 'passivityenforcement'
documentation_source_path: 'ug/passivityenforcement.html'
language: en
---

# Passivity Enforcement

## Ports

### Input

### **u0** — Control actions scalar | vector

Unmodified control actions, specified as a scalar or a vector.

If the **Number of actions** parameter is
`1`, connect **u0** to a scalar
signal. Otherwise, connect **u0** to a vector signal
with length equal to **Number of actions**.

### **fp** — Passivity input function offset coefficient scalar | vector

Offset coefficient *fp* in the
following constraint equation.

up=fp(x)+gp(x)u

Connect **fp** to an
*Nu*-by-1 signal, where
*Nu* is equal to the
**Number of actions** parameter.

### **gp** — Passivity input function linear coefficient scalar | matrix

Linear coefficient *gp* in the
following constraint equation.

up=fp(x)+gp(x)u

Connect **gp** to an
*Nu*-by-*Nu*
signal, where *Nu* is equal to
the **Number of actions** parameter.

### **yp** — Passivity output function scalar | vector

Passivity output function, defined as the following function of plant
states.

yp=hp(x)

Connect **yp** to an
*Nu*-by-1 signal, where
*Nu* is equal to the
**Number of actions** parameter.

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
| negative integer | The initial optimization problem was infeasible. |

#### Dependencies

To enable this output port, select the **Optimization
status** parameter.

## Parameters

#### Parameters Tab

### **Number of actions** — Number of control actions `1` (default) | positive integer

Specify the number of actions to apply bounds to and optimize.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nu` |
| **Type:** character vector |
| **Default:** `'1'` |

### **Passivity index** — Passivity index `0.1` (default) | nonnegative scalar | nonnegative vector

Specify passivity index to enforce. Specify **Passivity index** as a
nonnegative scalar or as a vector of nonnegative values with dimensions
equal to *Nu*-by-1, where
*Nu* is equal to the
**Number of actions** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `rho` |
| **Type:** character vector |
| **Default:** `'0.1'` |

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

The Passivity Enforcement block supports code generation for
double-precision signals only.

## Version History

**Introduced in R2023a**

### R2023b: Library location changed

The Passivity Enforcement block is now in the **Simulink
Control Design/Constraint Control** sublibrary.

In R2023b, when you open a model saved in a previous release, the library links
for Passivity Enforcement blocks update automatically.

## Description

Modify control actions to satisfy passivity constraints and action bounds

The Passivity Enforcement block computes the modified control actions
that are closest to specified control actions subject to passivity constraints and
action bounds.

The block uses a quadratic programming (QP) solver to find the control action
*u* that minimizes the function |u−u0|2 in real time. Here, *u*0 is
the unmodified control action from the controller.

The solver applies the following constraints to the optimization problem.

ρypTyp+ypTfp+ypTgpu≤0umin≤u≤umax

Here:

- *ρ* is the passivity index.
- *y**p* is the
  passivity output function, defined as yp=hp(x).
- *f**p* and
  *g**p* are the
  functions defined by the passivity input function up=fp(x)+gp(x)u.
- *u*min is a lower bound for the
  control action.
- *u*max is an upper bound for the
  control action.

For more information on passivity enforcement, see Passivity Enforcement for Control Design.
