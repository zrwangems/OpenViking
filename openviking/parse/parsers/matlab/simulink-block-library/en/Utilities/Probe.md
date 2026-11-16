---
type: simulink-block
title: 'Probe'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'probe'
documentation_source_path: '../simscape/ref/probe.html'
language: en
---

# Probe

## Ports

### Output

### **x** — Value of selected variable during simulation scalar | vector | matrix

Outputs the values of one selected variable during simulation as a Simulink signal. The port name matches the name of selected variable. The output
signal unit matches the unit of the variable. You can modify the port label and change
the unit of the output signal by using the Property Inspector.

If you select more than one variable, the block acquires additional output
ports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2025a: Probe across subsystem boundaries

The Probe
block now has a dialog box, which you can use to connect the
Probe block to another Simscape block, select which variables to probe, and customize the
Probe port names and the output units for the variables.

In previous releases, you could connect the Probe block
only to a block at the same level of the model hierarchy. Now, when you double-click a
Probe block, its dialog box opens. Use the
**Connect** button to attach (bind) the
Probe block to another Simscape block, which can be located at the same level, in a subsystem, or at any other
level of the model hierarchy. Click **Done connecting** to complete the
binding process. You can also end the binding process by clicking the X in the upper-right
corner of the model canvas.

### R2024b: Use Property Inspector or command-line interface to specify variables to probe

Instead of selecting variables to probe on the model canvas, you can now use
Property Inspector for the Probe block to
select or unselect variables, change port labels, or select different output units.

New command-line interface in this release includes:

- `simscape.probe.defaultVariableTable`
- `simscape.probe.getVariableTable`
- `simscape.probe.setVariableTable`
- `simscape.probe.VariableTable`
- `simscape.probe.VariableConfiguration`

### R2023b: Select or unselect all variables for probing

To facilitate working with long lists of variables, when you select variables for
probing, the context menu now contains an additional check box at the top of the list, just
below the **Type to Filter** field. Toggling this check box lets you select
all or unselect all the currently listed variables. You can use this check box together with
filtering to select or unselect groups of variables.

### R2023a: Extended list of variables available for probing

In previous releases, when you were selecting the variables to output, the context menu
contained only the variables exposed in the **Initial Targets**
section of the block dialog box, that is, the same variables that can be used for
block-level variable initialization.

Starting in R2023a, the context menu contains all the externally accessible block
variables, regardless of whether they are exposed in the **Initial
Targets** section of the block dialog box. Externally accessible variables
include: block variables declared with the `ExternalAccess` attribute value
of either `modify` or `observe`, inputs, outputs,
intermediates, modecharts, and domain Across variables at each of the nodes. Essentially,
these are the same variables that you can see in the simulation data log.

To facilitate scanning through long lists of variables, especially in composite
components, the display format of variables in the context menu has been reversed from
`Name:id` to `id:Name`. For example, instead of
`Current:i`, the same variable now appears as
`i:Current`. This view is more consistent with the variable display in
the Variable Viewer, Simscape Results Explorer, and Simulation Data Inspector.

The context menu now also has a filter field at the top. Type in this field to filter
the variables displayed in the context menu.

## Description

Output block variables as signals during simulation

The Probe block lets you select variables from another
block in the model and output them as Simulink® signals. Double-click a Probe block and use the
**Connect** button to attach (bind) the
Probe block to another Simscape™ block, which can be located at the same level of the model diagram, in a
subsystem, or at any other level of the model hierarchy. However, the block must be located in
the same model. You cannot bind the Probe block across model
reference boundaries.

Once you select the block to probe, a list of its variables appears on the model canvas.
You can select the variables on the model canvas, or skip this step. Click **Done
connecting** to complete the binding process. At this point, the
Probe dialog box is populated with the list of variables from
the attached block. If you have selected any of the variables on the model canvas, they are
selected in the dialog box as well. You can use the dialog box to continue selecting which
variables to probe, customize the port names, and specify the output units.

When you select the variables to probe:

- The list contains all the externally accessible block variables, regardless of whether
  they are exposed in the **Initial Targets** section of the block dialog
  box. Externally accessible variables include:

  - Component variables, including event variables
  - Domain Across variables at each of the nodes
  - Inputs
  - Outputs
  - Intermediates
  - Mode chart elements

  These members must be declared with the `ExternalAccess` attribute
  value of either `modify` or `observe`. Essentially,
  these are the same variables that you can see in the simulation data log or
  instrumentation table.
- In case of conditional visibility, if a variable is active only in a subset of block
  parameterizations, such a variable is always available for probing, regardless of whether
  it is active in the current block configuration.
- In case of conditional declaration, variables are not available for probing,
  regardless of whether the conditional branch is active in the current block configuration.
  For composite components, this limitation includes all the externally accessible variables
  of conditionally declared components.
- The block outputs each of the selected variables as a separate signal.

The Probe block outputs Simulink signals. Therefore, you can connect it directly to Simulink blocks, such as scopes or buses.

You can attach (bind) a Probe block to only one block at a
time. However, you can bind multiple Probe blocks to the same
block in the model at the same time.

### Working with the Block on the Model Canvas

To use a Probe block in a model:

1. Add the Probe block to any level of the model
   hierarchy.
2. Double-click the Probe block. The block dialog box
   opens.

   Unconnected Probe dialog box

   At this point, the Probe block is unconnected, that
   is, not attached to any other block.
3. Click **Connect** to start the binding process.
4. Select a Simscape block. That block can be located at any level of the model hierarchy.
5. When you select a block, a list of its variables appears on the model canvas. You
   can select the variables on the model canvas, or skip this step and select the variables
   later, from the Probe dialog box. The benefit of
   selecting variables on the model canvas is that you can filter them and select or
   unselect multiple variables at once.

   For example, if you selected a Rotational Electromechanical
   Converter block, the available variables include current, voltage,
   torque, and angular velocity, as well as voltage at each of the electrical ports and the
   rotational velocity at ports **C** and **R**.

   Selecting variables to probe on the model canvas

   To facilitate working with long lists of variables, the context menu has a
   **Type to Filter** field at the top. Type in this field to display
   only the variables that contain the filter string in their name or id.

   You can also use the top check box, located just below the **Type to
   Filter** field, to select all or unselect all the currently listed
   variables.
6. In the Probe block dialog box, click **Done
   connecting** next to **Connect Mode** to complete the
   binding process.

   **Note**

   When selecting a block, if you navigate across the subsystem boundaries to a
   subsystem that is not open in a model tab, the Probe
   block dialog box can close automatically. In this case, you can end the binding
   process by clicking the X in the upper-right corner of the model canvas.

   Ending the binding process takes you to the model diagram level where the
   Probe block is situated and reopens the
   Probe dialog box.
7. Once you have completed the binding process, the
   Probe dialog box is populated with the list of
   variables from the attached block. The Probe dialog box
   also contains a link to the block to which the probe is connected. If you click this
   link, the block being probed is highlighted. If this block is at a different level than
   the Probe block, the subsystem containing the block opens
   and the block is highlighted.

   If you have selected any of the variables on the model canvas, they are selected in
   the dialog box as well. (In this example, current and angular velocity are selected.) If
   a variable is selected in the dialog box, you can expand it in the list to view the
   associated port label and unit. You can use the dialog box to continue selecting which
   variables to probe, customize the port names, and specify the output units.

   Probe dialog box attached to the Rotational Electromechanical Converter block
8. For each selected variable, the Probe block acquires
   an additional output port. (In this example, the port names are **i**
   and **w**.) Initially, the port label matches the variable name, but
   you can edit it by double-clicking its name in the Probe
   dialog box, in the cell to the right of **Port Label**. You can also
   click in the cell to the right of **Unit** and select a different
   output unit for the output signal from the drop-down list.
9. Connect the Probe block output ports to scopes or
   other blocks from the Simulink Sinks library to view the signal values during simulation.

   Block diagram with Probe outputs connected to scopes

   Current scope showing simulation results

   RPM scope showing simulation results

To bind a Probe block to a different block in the model,
or to change the selected variables, double-click the Probe
block again.

If you copy a Probe block together with the block that it
is bound to, the connection is preserved and the same variables are automatically selected
in the new pair.

### Command Line Workflow

Instead of the interactive workflow on the model canvas, you can bind a
Probe block and select variables by using these
commands:

- `simscape.probe.setBoundBlock(probeBlock,
  boundBlock)` — Binds
  *`probeBlock`* to *`boundBlock`*.
  *`probeBlock`* must be a valid full block path or a handle to a
  Probe block. *`boundBlock`* must
  be a valid full block path or a handle to another block at the same level of the model
  hierarchy as *`probeBlock`*. The command does not check whether
  *`boundBlock`* is a Simscape block or whether it has variables to probe.

  `simscape.probe.setBoundBlock(probeBlock,
  [])` returns the Probe block to the unbound
  state. Does not affect the selected variables.
- `simscape.probe.setVariables(probeBlock,
  variables)` — Selects variables for the
  *`probeBlock`* to output. *`probeBlock`*
  must be a valid full block path or a handle to a Probe
  block. *`variables`* must be a character vector, cell array of
  character vectors, or string array that specifies the variables. The character vectors
  or strings must be unique variable identifiers, lexicographically sorted. The command
  does not check whether the currently selected *`boundBlock`*
  contains these variables.

  Instead of lexicographically sorting the variables, you can use this syntax:

  ```
  I = simscape.probe.setVariables(probeBlock, variables, 'Sort', true)
  ```

  The command then sorts the variables before applying them to
  *`probeBlock`*. Variable identifiers must still be unique.
  *`I`* returns the order in which the sorted
  *`variables`* appear as ports on the
  Probe block.

The programmatic equivalent of the interactive binding and variable selection shown in
the example in Working with the Block on the Model Canvas is:

```
simscape.probe.setBoundBlock('PermanentMagnetDCMotor/DC Motor/Probe','PermanentMagnetDCMotor/DC Motor/Rotational Electromechanical Converter');
simscape.probe.setVariables('PermanentMagnetDCMotor/DC Motor/Probe',["i", "w"]);
```

As a result, the Probe block also has two output ports,
**i** and **w**, bound to the **Current :
i** and **Angular velocity : w** variables of the
Rotational Electromechanical Converter block, respectively.

If you supply unsorted variables, the command returns the sorted order:

```
I = simscape.probe.setVariables('PermanentMagnetDCMotor/DC Motor/Probe', ["w", "i"], 'Sort', true)
```

```
I =

     2     1
```

In this example, the second variable, `i`, appears as the first port on
the Probe block, followed by the first variable,
`w`.

You can use the
`simscape.probe.getBoundBlock(probeBlock)`
and `simscape.probe.getVariables(probeBlock)`
commands, where *`probeBlock`* is a valid full block path or a handle
to a Probe block, to return its bound block and variables,
respectively.

You can also use the `simscape.probe.defaultVariableTable`, `simscape.probe.setVariableTable`, and `simscape.probe.getVariableTable` functions to construct
`VariableTable` objects and attach them to a
Probe block.
