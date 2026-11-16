---
type: simulink-block
title: 'VR Sink'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrsink'
documentation_source_path: 'vrsink.html'
language: en
---

# VR Sink

## Ports

### Input

### **Input 1** — Input signal real scalar | real vector

Input signal to drive the virtual reality visualization of nodes selected in the **Virtual World Tree**.

**Data Types:** `double`
### Output

### **Output 1** — Output video stream 3-element vector of video signal dimensions

Use the output port to access the RGB video stream of the VR signal input.

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
  3D Animation™ Viewer or a Web browser.
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

### **Show video output port** — Output VR signal to video off (default) | on

Enable a port to output an RGB video stream for further 2D video processing.

### **Video output signal dimensions** — Specify video output size `[200 320]` (default) | 2-element vector

Specify the dimensions ([height width]) of the video output signal in pixels.

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

**Introduced before R2006a**

### R2025a: Warns

The `VR Sink` block will be removed in a
future release. The Simulink
3D Animation Viewer has been removed so `VR Sink` does not open the
virtual world. For alternate functionality, see Transition Virtual Reality World to Unreal Engine 3D Environment.

### R2023b: To be removed

The `VR Sink` runs without warning and will be removed in a future release.

## Description

(To be removed) Write data from Simulink model to virtual world

To output data from the model to control and animate a virtual world, use a VR
Sink block. The VR Sink block writes values from its ports to
virtual world fields specified in the Block Parameters dialog box.

The VR Sink block is equivalent to the VR
To Video block, except that the **Show video output port**
parameter for the VR Sink block is cleared by default.

The VR Sink block cannot be compiled by the Simulink®
Coder™ software, but it can be used as a SimViewing device on the host
computer.

**Note**

The current internal viewer window (`vrfigure`) properties are
saved together with the Simulink model. Next time you open the model, the internal viewer window opens
with the same parameters that were last saved, such as position, size, and
navigation mode. When you close the viewer window, the Simulink software does not alert you if these properties have changed.

The VR Sink block is a Sim Viewing Device. You can include it in models
that you compile with Simulink
Coder software. If you use External mode to compile, build, and deploy the model
on a target platform, such as
Simulink
Real-Time™ or Simulink
Desktop Real-Time™, some sink blocks and Sim Viewing Device blocks stay in normal mode during
simulation, receive data from the target, and display that data. For more information,
see Use C/C++ S-Functions as Sim Viewing Devices in External Mode (Simulink).
