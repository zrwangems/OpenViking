---
type: simulink-block
title: 'VR To Video'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrtovideo'
documentation_source_path: 'vrtovideo.html'
language: en
---

# VR To Video

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
- Click **View** to view the world in the Simulink®
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

### **Show video output port** — Output VR signal to video on (default) | off

Enables a port to output an RGB video stream for further 2D video
processing.

### **Video output signal dimensions** — Specify video output size `[200 320]` (default) | 2-element vector

Specify the dimensions ([height width]) of the video output signal in pixels.

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

**Introduced in R2007b**

### R2025a: Warns

The `VR To Video` block will be removed in a
future release. The Simulink
3D Animation Viewer has been removed so `VR To Video` does not open the
virtual world. For alternate functionality, see Transition Virtual Reality World to Unreal Engine 3D Environment.

### R2023b: To be removed

The `VR To Video` runs without warning and will be removed in a future release.

## Description

(To be removed) Write data from Simulink model to virtual world (video output port enabled)

The VR to Video block is equivalent to the VR
Sink block, except that its **Show video output port** is
selected by default.

To open the Block Parameters dialog box, double-click the block.

See the VR Sink block for details.
