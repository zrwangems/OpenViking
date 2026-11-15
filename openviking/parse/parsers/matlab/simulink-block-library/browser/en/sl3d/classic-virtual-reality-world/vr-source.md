---
type: simulink-block
title: 'VR Source'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrsource'
documentation_source_path: 'vrsource.html'
language: en
---

# VR Source

## Ports

### Output

### **Output 1** — Output signal real scalar | real vector

Output signal that drives the virtual reality visualization of nodes
selected in the **Virtual World Tree**.

**Data Types:** `double`

## Parameters

### **Source file** — File name specifying virtual world that connects to block string scalar | character vector

By default, the full path to the associated virtual world 3D file appears in this text
box. If you enter only the file name in this box, the software assumes that the virtual
world 3D file resides in the same folder as the model file. You can specify a VRML file
or an X3D file.

- Click **New** to open an empty default virtual world
  editor. When you either enter a source file name or use the
  **Browse** button, the **New** button
  becomes an **Edit** button.
- Click **Edit** to launch the default virtual world editor
  with the source file open.
- Click **View** to view the world in the Simulink
  3D Animation Viewer or a Web browser.
- Click **Reload** to reload the world after you change it.

### **Open Viewer automatically** — Display virtual world on model load off | on

Enable this parameter to display the virtual world after loading the Simulink model.

### **Allow viewing from the Internet** — View virtual world over network off (default) | on

Enable this parameter to make the virtual world accessible for viewing on a client
computer. If you do not select this check box, then the world is visible only on the
host computer. This parameter is equivalent to the `RemoteView`
property of a `vrworld` object.

### **Description** — Virtual reality object description string scalar | character vector

The description is displayed in all virtual reality object listings, in the title bar of the Simulink
3D Animation Viewer, and in the list of virtual worlds on the Simulink
3D Animation HTML page. This parameter is equivalent to the `Description` property of a `vrworld` object.

### **Sample time** — Block sample time for simulation 0.1 (default) | scalar | vector

Specify the sample time for the block, or specify `-1` to inherit the sample
time.

### **Virtual World Tree** — View structure of virtual world node

This box shows the structure of the virtual world 3D file and the virtual world
itself.

Nodes that have names are marked with red arrows. You can access them from the
Simulink
3D Animation interface. Nodes without names but whose children are named are also
marked with red arrows. This marking scheme makes it possible for you to find all
accessible nodes by traversing the tree using arrows. Other nodes have a blue dot before
their names.

Fields with values that you set have check boxes. Use these check boxes to select the
fields whose values you want the Simulink software to update. For every field that you select, an input port is
created in the block. Input ports are assigned to the selected nodes and fields in the
order that corresponds to the virtual world 3D file.

Fields whose values cannot be written (because their parent nodes do not have names,
or because they are not of virtual world data class `eventIn` or
`exposedField`) have an X-shaped icon.

### **Show node types** — Display node types in virtual world tree off (default) | on

Enable this parameter to show node types in the virtual world tree.

### **Show field types** — Display field types in virtual world tree off (default) | on

Enable this parameter to show field types in the virtual scene tree.

## Libraries

Simulink 3D Animation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011b**

### R2025a: Warns

The `VR Source` block will be removed in a
future release. The Simulink
3D Animation Viewer has been removed so `VR Source` does not open the
virtual world. For alternate functionality, see Transition Virtual Reality World to Unreal Engine 3D Environment.

### R2023b: To be removed

The `VR Source` runs without warning and will be removed in a future release.

## Description

(To be removed) Read data from virtual world to Simulink model

Use the VR Source block to provide interactivity between a user
navigating the virtual world and the simulation of a Simulink® model. The VR Source block registers user interactions with
the virtual world and passes that data to the model to affect the simulation of the
model. The VR Source reads values from virtual world
fields specified in the Block Parameters dialog box and inputs their values to a
model.

Examples of some ways that you can use a VR Source block to input data
from a virtual world to a Simulink model include:

- Use sensor data from a virtual world to control a simulation.
- Provide interactivity between user navigation and interaction in a virtual
  world and the simulation of the model.
- Have a simulation react to virtual world events, such as time ticks or outputs
  from scripts.
- Use static information from the virtual world, such as the size of a box, to
  control a simulation.

For example, you can specify setpoints in the virtual world, so that user can specify
the location of a virtual world object interactively. The simulation then responds to
the changed location of the object. The VR Source block can read into the
model events from the virtual world, such as time ticks or outputs from scripts. The
VR Source block can also read into the model static information about
the virtual world (for example, the size of a box defined in the virtual world 3D
file).

**Note**

The current internal viewer window (`vrfigure`) properties are
saved together with the Simulink model. The next time that you open the model, the internal viewer
window opens with the same parameters that were saved, such as position, size, and
navigation mode. When closing the viewer window, the Simulink software does not alert you if these properties have changed.

To open the Block Parameters dialog box VR Source block:

- When you first add a VR Source block and it is still not
  associated with a virtual world, double-click the block.
- Otherwise, in the Simulink
  3D Animation™ Viewer, select
  **Simulation****Block
  parameters**. If the viewer is not already open, you can open it
  by double-clicking the VR Source block.

You cannot use the Simulink
Coder™ software to compile a model that includes a VR Source
block.
