---
type: simulink-block
title: 'Solver Configuration'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Utility Blocks'
documentation_page: 'solverconfiguration'
documentation_source_path: 'ref/solverconfiguration.html'
language: en
---

# Solver Configuration

## Ports

### Conserving

### **Port\_1** — Connection port untyped conserving port

Conserving connection port. This port is untyped. You can connect it anywhere on a
physical network circuit by creating a branching point on a connection line between
conserving ports of any type. The block provides solver setting to the whole physical
network, regardless of the connection type.

## Parameters

### **Equation formulation** — Specify how the solver treats sinusoidal variables `Time` (default) | `Frequency and time`

Specifies how the solver treats sinusoidal variables.

Use the `Frequency and time` value to speed up simulation
of systems with a single nominal frequency. For more information, see Frequency and Time Simulation Mode.

### **Index reduction method** — Choose index reduction method for solving nonlinear high-index DAEs `Derivative replacement` (default) | `Projection` | `None`

Choose nonlinear index reduction method best suited for the network connected to the
Solver Configuration block:

- `Derivative replacement` — In this method, parts of the
  DAE are differentiated analytically and appended to the original system. For each
  additional equation, a derivative is selected to be replaced by a new algebraic
  variable called a *dummy derivative*. For more information, see
  https://epubs.siam.org/doi/abs/10.1137/0914043?journalCode=sjoce3. It is recommended that you start with this method.
- `Projection` — Use this option if the
  `Derivative replacement` method fails due to issues with
  dynamic state selection.
- `None` — If your model does not contain nonlinear
  high-index DAEs, use this option to completely bypass nonlinear index reduction and
  remove the analysis overhead.

### **Start simulation from steady state** — Select whether to start simulation from the initial state or from steady state off (default) | on

By default, when this check box is cleared, simulation starts from the initial state
obtained from the initial conditions computation.

When you select this check box, the solver attempts to find the steady state that
would result if the inputs to the system were held constant for a sufficiently large
time. For more information, see Initial Conditions Computation. Simulation
then starts from this steady state.

For models compatible with frequency-and-time equation formulation, when you select
this check box, the solver attempts to perform sinusoidal steady-state initialization.
In other words, initialization is performed using frequency-time equations, and then the
simulation proceeds using the actual equation formulation and other options selected in
the Solver Configuration block. For more information, see
Frequency and Time Simulation Mode.

**Note**

Using the **Initial state** option on the **Data
Import/Export** pane of the Configuration Parameters dialog box overrides
the **Start simulation from steady state** option.

### **Consistency tolerance** — State-based tolerance schema used for initial conditions and transient initialization computation `Model AbsTol and RelTol` (default) | `Local tolerance settings`

This parameter affects the nonlinear solver used for computing initial conditions
and for transient initialization. Select the state-based tolerance source:

- `Model AbsTol and RelTol` — Use the model tolerance
  settings, specified as **Absolute tolerance** and
  **Relative tolerance** parameters on the
  **Solver** pane of the Configuration Parameters dialog box.
- `Local tolerance settings` — Replace the model
  tolerance settings with local values. When you select this option, the
  **Absolute tolerance** and **Relative
  tolerance** parameters appear in the Solver
  Configuration block dialog box.

Independent of whether you use the model tolerances or the local tolerance settings,
the **Tolerance factor** parameter provides a scaling factor for these
values. The resulting value determines how accurately the algebraic constraints are to
be satisfied at the beginning of simulation and after every discrete event (for example,
a discontinuity resulting from a valve opening, a hard stop, and so on).

### **Absolute tolerance** — Local absolute tolerance `0.001` (default) | positive scalar

Specify a local value to be used for computing initial conditions and for transient
initialization, instead of using the **Absolute tolerance** parameter
on the **Solver** pane of the Configuration Parameters dialog
box.

#### Dependencies

To enable this parameter, set **Consistency tolerance** to
`Local tolerance settings`.

### **Relative tolerance** — Local relative tolerance `0.001` (default) | positive scalar

Specify a local value to be used for computing initial conditions and for transient
initialization, instead of using the **Relative tolerance** parameter
on the **Solver** pane of the Configuration Parameters dialog
box.

#### Dependencies

To enable this parameter, set **Consistency tolerance** to
`Local tolerance settings`.

### **Tolerance factor** — Scaling factor used for absolute and relative tolerances `0.001` (default) | scalar in the range (0,1]

This parameter provides the scaling factor for the state-based absolute and relative
tolerances, independent of whether you use the model tolerances or the local tolerance
settings. Decrease the parameter value (that is, tighten tolerance) to obtain a more
reliable time simulation. Increase the parameter value (that is, relax the tolerance) if
solving for initial conditions failed to converge, or to reduce the computation
time.

### **Use local solver** — Use sample-based local solver for physical network in the model off (default) | on

Lets you use a sample-based local solver with a sample time specified by the
**Sample time** parameter. In sample-based simulation, all the
physical network states, which are otherwise continuous, become represented to
Simulink® as discrete states. The solver updates the states once per time step. This
option is especially useful for generated code or hardware-in-the-loop (HIL)
simulations.

**Note**

If you use a local solver, simultaneous use of Simulink or Simulink
Control Design™ linearization tools is not recommended.

### **Solver type** — Solver type used by local solver for updating the states `Backward Euler` (default) | `Trapezoidal Rule` | `Partitioning`

Select the solver type used for updating the states:

- `Backward Euler` — Tends to damp out oscillations, but
  is more stable, especially if you increase the time step.
- `Trapezoidal Rule` — Captures oscillations better than
  `Backward Euler`, but is less stable.
- `Partitioning` — Lets you increase real-time simulation
  speed by partitioning the entire system of equations corresponding to a Simscape network into a cascade of smaller equation systems. Not all networks
  can be partitioned. However, when a system can be partitioned, this solver provides
  a significant increase in real-time simulation speed. For more information, see
  Understanding How the Partitioning Solver Works and Increase Simulation Speed Using the Partitioning Solver.

Regardless of which local solver you choose, the Backward Euler method is always
applied:

- Right at the start of simulation.
- Right after an instantaneous change, when the corresponding block undergoes an
  internal discrete change. Such changes include clutches locking and unlocking, valve
  actuators opening and closing, and the switching of the PS Asynchronous Sample &
  Hold block.

#### Dependencies

To enable this parameter, select the **Use local solver** check
box.

### **Sample time** — Sample time for the local solver `0.001` (default) | positive scalar

Specify the local solver sample time, in seconds. The solver updates the states once
per time step.

#### Dependencies

To enable this parameter, select the **Use local solver** check
box.

### **Partition method** — Select whether to prioritize speed or robustness when using Partitioning local solver `Robust simulation` (default) | `Fast simulation`

Select whether to prioritize speed or robustness when using Partitioning local
solver:

- `Fast simulation` — Improve simulation
  performance by solving most differential equations using the forward Euler scheme.
- `Robust simulation` — Increase simulation
  robustness by solving more equations using the backward Euler scheme.

#### Dependencies

To enable this parameter, select the **Use local solver** check
box and set **Solver type** to
`Partitioning`.

### **Partition storage method** — Select method used for storing partitioning data when using Partitioning local solver `As needed` (default) | `Exhaustive`

When you use the Partitioning solver, it solves the small switched linear equations
consecutively. You can choose to store the matrix inverses, to improve the simulation
performance. Then, if the same configuration is detected in a subsequent time step, the
partitioning solver uses the stored matrix inverses, instead of recomputing them. Select
the method used for storing partitioning data:

- `As needed` — Compute matrix inverses during
  simulation, as needed. This method does not require as much memory but can result in
  performance spikes.
- `Exhaustive` — Compute and store matrix inverses
  before simulation. This method improves the simulation performance but requires more
  memory. Use the **Partition memory budget [kB]** parameter to
  specify the maximum allowed memory budget for storing the data.

#### Dependencies

To enable this parameter, select the **Use local solver** check
box and set **Solver type** to
`Partitioning`.

### **Partition memory budget [kB]** — Memory budget for exhaustive method of storing partition data `1024` (default) | positive scalar

Specify the maximum memory budget, in kB, allowed for storing cached partition data.
If this budget is exceeded, simulation errors out. You can adjust the default value
based on your available memory resources and on the **Total memory
estimate** data in the Statistics Viewer. For more information, see Partitioning Solver Statistics.

#### Dependencies

To enable this parameter, select the **Use local solver** check
box. Set **Solver type** to `Partitioning`
and **Partition storage method** to
`Exhaustive`.

### **Resolve indeterminate equations during runtime** — Applies runtime regularization to solve statically indeterminate systems on (default) | off

Certain model configurations, such as parallel clutches locking, or current sensors
connected in parallel, allow an infinite number of solutions, which makes them
statically indeterminate. Regularization is a transformation that turns models with
indeterminate Through variables into solvable systems. By default, if the solver
encounters a statically indeterminate system, it applies runtime regularization to solve
it.

If your model does not contain configurations with lossless parallel flow paths, you
can clear the **Resolve indeterminate equations during runtime** check
box to speed up simulation.

#### Dependencies

To enable this check box, select the **Use local
solver** check box and set **Solver type** to either
`Backward Euler` or `Trapezoidal
Rule`.

### **Use fixed-cost runtime consistency iterations** — Fixed-cost simulation option off (default) | on

Whether to compute the transient initialization and solver phase at a fixed cost.
When you select this parameter, you can specify the number of nonlinear and mode
iterations for transient initialization and solver computations. If the system does not
converge once it performs the specified number of iterations, the solver ignores the
failure and proceeds to the next step.

If you clear the check box, the system uses a more robust and time-consuming
algorithm, performing as many iterations as necessary to reach convergence, and errors
out if it fails to reach convergence at the time of transient initialization.

For more information, see Fixed-Cost Simulation.

### **Nonlinear iterations** — Number of Newton iterations for transient initialization `3` (default) | positive integer

Specify the number of Newton iterations to be performed at the time of transient
initialization. You can use the `simscape.getLocalSolverFixedCostInfo` function to find the necessary
iterations per step to run as a fixed step, fixed cost simulation.

#### Dependencies

To enable this parameter, select the **Use fixed-cost runtime consistency
iterations** check box.

### **Mode iterations** — Number of mode iterations for transient initialization `2` (default) | positive integer

Specify the number of mode iterations to be performed at the time of transient
initialization.

#### Dependencies

To enable this parameter, select the **Use fixed-cost runtime consistency
iterations** check box and clear the **Use local solver**
check box. Only one major mode update per step is performed when using local solvers,
therefore this parameter is not available if the **Use local solver**
check box is selected.

### **Compute impulses** — Lets you manage computational cost of impulse detection during transient initialization off (default) | on

Lets you manage computational cost of impulse detection during transient
initialization, both for global and local solvers.

Event-based methods of state reinitialization and impulse handling let you model
physical phenomena, such as collisions and bouncing balls, and provide a significant
boost in simulation speed for such models. However, impulse detection can add cost to
transient initialization. This cost is proportional to the number of impulse iterations
performed to reach convergence.

If you select the **Compute impulses** check box, you can specify
the number of impulse iterations to perform during transient initialization. If the
system does not converge upon reaching these numbers, it ignores the failure and goes to
the next step.

If you clear the check box, the system computes impulses as many times as necessary
to reach convergence.

#### Dependencies

To enable this check box, select the **Use fixed-cost runtime consistency
iterations** check box.

### **Impulse iterations** — Number of impulse iterations for transient initialization `2` (default) | positive integer

Specify the number of impulse iterations to be performed at the time of transient
initialization. If the system does not converge upon reaching these numbers, it ignores
the failure and goes to the next step.

#### Dependencies

To enable this parameter, select the **Compute impulses** check
box.

### **Maximum threads for function evaluation** — Use multithreading to speed up Newton iterations for Backward Euler solver `1` (default) | positive integer

Specify the maximum number of threads for function evaluation when using the
Backward Euler solver for real-time simulation. The actual number of threads used is the
nearest power of 2 not to exceed the parameter value. For example, if you specify
`5` as the parameter value, the solver uses 4 threads. The default,
`1`, corresponds to single-thread function evaluation.

To use multithread function evaluation, you must clear the **Resolve
indeterminate equations during runtime** check box. If you select the
**Resolve indeterminate equations during runtime** check box, the
solver warns and switches to single-thread function evaluation.

Other unsupported simulation modes include frequency-and-time simulation, delay,
scalable compilation, accelerator mode, and rapid accelerator mode. You can generate
code using Simulink
Real-Time™, but other types of code generation are not supported.

#### Dependencies

To enable this parameter, select the **Use local solver** check
box, set the **Local solver** parameter to `Backward
Euler`, and select the **Use fixed-cost runtime consistency
iterations** check box.

### **Linear Algebra** — Specify how the solver treats matrices `auto` (default) | `Sparse` | `Full`

Specifies how the solver treats matrices:

- `auto` — The solver automatically selects the
  appropriate option, either sparse or full, for treating the matrices.
- `Sparse` — The solver treats matrices as sparse.
- `Full` — The solver treats matrices as full.

### **Number of threads (specify n for 2^n)** — Use multithread linear algebra to speed up desktop simulation on a multicore machine `0` (default) | positive integer

Specify the number of threads for multithread linear algebra by providing an integer
exponent for 2. The number of threads equals 2 to the power of the parameter value. The
default, `0`, corresponds to single-thread linear algebra.

For small models, multithread algorithms that use numbers higher than 0 may be
slower than single-thread.

#### Dependencies

To enable this parameter, select the **Use local solver** check
box and set the **Linear algebra** parameter to
`Sparse`. For a global solver, Simulink solves the equations without using Simscape linear algebra algorithms.

### **Delay memory budget [kB]** — Memory budget for processing delays `1024` (default) | positive scalar

Specify the maximum memory budget, in kB, allowed for processing delays when
simulating models that contain either blocks from the Delays library or custom blocks
using the `delay`
Simscape language construct. The purpose of this parameter is to protect against
excessive memory swapping. If this budget is exceeded, simulation errors out. You can
adjust this value based on your available memory resources.

### **Apply filtering at 1-D/3-D connections when needed** — Automatically provides additional derivative needed by Simscape Multibody™ blocks on (default) | off

This option is applicable only for models that connect blocks from Simscape
Multibody library to Simscape blocks, or blocks from other add-on products. Use the Statistics Viewer to
determine whether your model has 1-D/3-D connections. For more information, see 1-D/3-D Interface Statistics.

When a Simscape
Multibody block is connected directly to a Simscape network, an additional derivative may be required for the network to be
solved. When you select this check box, the solver automatically applies input filtering
to the signal entering the Simulink-PS Converter block to
obtain this additional derivative. The **Filtering time constant**
parameter provides the time constant for the delay.

**Note**

This check box is selected by default. If you clear it, and the 1-D/3-D connection
requires the additional derivative, the solver issues an error message.

### **Filtering time constant** — Time constant for the delay, in seconds `0.001` (default) | positive scalar

This parameter specifies the filtering time constant, in seconds, for the automatic
input filtering for 1-D/3-D connections. The parameter value applies globally to all
connections belonging to the network that includes this Solver
Configuration block.

#### Dependencies

To enable this parameter, select the **Apply filtering at 1-D/3-D
connections when needed** check box.

#### Multibody

### **Use local solver** — Use sample-based local solver for Simscape Multibody network off (default) | on

Lets you use a sample-based local solver for the connected Simscape
Multibody network. Using a local solver can reduce the computational cost for a
complex Simulink model that has simple Simscape
Multibody networks. A Simscape
Multibody network using a local solver appears to the global Simulink solver as if it has discrete states. The local solver updates the states
once per time step.

**Note**

This setting is independent from the **Use local solver** setting
in the main part of the block dialog box, which applies to the Simscape network connected to the block.

### **Solver type** — Solver type used by local solver for updating the states in Simscape Multibody network `First-order explicit formula` (default) | `Second-order explicit formula` | `Third-order explicit formula` | `Fourth-order explicit formula` | `Fifth-order explicit formula` | `Eight-order explicit formula`

Select the solver type used for updating the states in the Simscape
Multibody network:

- `First-order explicit formula` — Explicit fixed-step
  solver that uses the same mathematical equations as `ode1`.
- `Second-order explicit formula` — Explicit fixed-step
  solver that uses the same mathematical equations as `ode2`.
- `Third-order explicit formula` — Explicit fixed-step
  solver that uses the same mathematical equations as `ode3`.
- `Fourth-order explicit formula` — Explicit fixed-step
  solver that uses the same mathematical equations as `ode4`.
- `Fifth-order explicit formula` — Explicit fixed-step
  solver that uses the same mathematical equations as `ode5`.
- `Eight-order explicit formula` — Explicit fixed-step
  solver that uses the same mathematical equations as `ode8`.

#### Dependencies

To enable this parameter, in the **Multibody** section, select
the **Use local solver** check box.

### **Sample time** — Sample time for the Multibody local solver `0.001` (default) | positive scalar

Specify the Multibody local solver sample time, in seconds. The solver updates the
states of the connected Simscape
Multibody network once per time step.

#### Dependencies

To enable this parameter, in the **Multibody** section, select
the **Use local solver** check box.

## Libraries

Simscape / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2024a: Control runtime regularization independently of fixed-cost simulation

The **Resolve indeterminate equations** check box in the
Solver Configuration block, which applies runtime regularization to solve statically
indeterminate systems, has been renamed to **Resolve indeterminate
equations at runtime** and moved to a different section of the dialog box.
Previously, you needed to select the **Use fixed-cost runtime
consistency iterations** check box to enable it. Now, to enable the **Resolve indeterminate equations at runtime** check box, you need to
select the **Use local solver** check box and set
**Solver type** to either `Backward Euler` or
`Trapezoidal Rule`. Unless your model contains lossless parallel
flow paths, such as ideal parallel clutches or switches, you can now clear the **Resolve indeterminate equations at runtime** check box and speed up
simulation whenever you use these types of local solver, independently of whether the
simulation is fixed-cost or not.

You can no longer turn off runtime regularization for global solvers.

### R2023b: Multibody local solver

The new **Multibody** section contains settings and parameters specific
to solving the connected Simscape
Multibody network. The **Use local solver** check box lets you reduce
the computational cost by representing the Simscape
Multibody network as if it has discrete states. The **Solver type** and
**Sample time** parameters in this section apply to the Multibody local
solver only.

### R2022b: New ways to specify consistency tolerance

The block uses state-based absolute and relative consistency tolerances, multiplied by a
scaling factor, to compute the initial conditions and for transient initialization. The
**Consistency tolerance** parameter lets you select between the model
tolerances or the local tolerance settings. The new **Tolerance factor**
parameter provides a scaling factor for these values. This state-based method provides
better robustness and efficiency, especially if used in conjunction with scaling the model
by nominal values.

In previous releases, the **Consistency tolerance** parameter had a
numeric value, and the block used a nonlinear solver based on the equation residual
tolerance to initialize the model.

If you open an existing model where the **Consistency tolerance**
parameter has a numeric value, the model continues to use the same residual-based
computation method that it used in previous releases. Your simulation results do not change.

To upgrade your existing models to use the state-based method, use the **Check
Simscape use of state-based consistency tolerances** check in the Upgrade
Advisor.

### R2022b: Multithread function evaluation for fixed-cost simulation

If your model uses the Backward Euler local solver, computing Newton iterations is
time-consuming and may present an issue for fixed-cost simulations. You can use multithread
function evaluation to speed up simulation on a multicore machine by using the new
**Maximum threads for function evaluation** parameter and clearing the
new **Resolve indeterminate equations** check box.

In previous releases, the solver used single-thread function evaluation and always
applied runtime regularization. The default values of the **Maximum threads for
function evaluation** parameter and **Resolve indeterminate
equations** check box are equivalent to the algorithm used in previous
releases.

## Description

Physical network environment and solver configuration

Each physical network represented by a connected Simscape™ block diagram requires solver settings information for simulation. The
Solver Configuration block specifies the solver parameters
that your model needs before you can begin simulation.

Each topologically distinct Simscape block diagram requires exactly one Solver
Configuration block to be connected to it.
