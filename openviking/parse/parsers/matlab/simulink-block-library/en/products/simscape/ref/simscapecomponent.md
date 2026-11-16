---
type: simulink-block
title: 'Simscape Component'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Utility Blocks'
documentation_page: 'simscapecomponent'
documentation_source_path: 'ref/simscapecomponent.html'
language: en
---

# Simscape Component

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Deploy Simscape language component as custom block in model diagram

The Simscape Component block lets you
generate a Simscape™ block directly from a textual component file, skipping the library build
process.

You can use the `ssc_build` command to generate a custom block library from
all the Simscape component files located in a namespace. However, you can also do
on-the-fly conversion of a component file directly into a custom block in your model by
using a Simscape Component block.

To deploy a component file directly into a block diagram:

1. Open the Simscape > Utilities library and add the Simscape
   Component block to your model. At first, the block does not
   point to any component file. Therefore, it does not have any ports,
   and the block icon states it is `Unspecified`.
2. Double-click the block to open the source file selector
   dialog box.
3. Click  to open the browser. The browser opens in the
   current working directory and lists only the files with the
   `.ssc` or `.sscp` extension.

   Browse to the desired Simscape language component file. The file does not have to be in a
   namespace. However, the directory where the file resides has to be on the
   MATLAB® path. If the file resides in a namespace, then the namespace
   parent folder must be on the MATLAB path.
4. Select the source file and click **Open**. The name of the
   source file appears in the text field of the source file selector dialog box,
   and the block name, description, and the link to source code appear in the
   **Description** pane.

   The source component selection is applied immediately, regardless of whether
   you have the **Auto Apply** check box selected or not. The
   block icon changes, and the block acquires the ports, parameters, and variables
   based on the selected source component.
5. If you now double-click the block, its dialog box has all the same elements as
   if it was generated from the component file through a library build process:
   name, description, parameters, variables, and a link to **Source
   code**. However, the **Description** pane has the
   source selector field that displays the name of the current source file and lets
   you point the block to a different component file.

### Source File Selector

When a Simscape Component block points to a valid Simscape language component file, its dialog box has the name, description,
parameters, and variables defined by that source file. The
**Description** pane also has the source selector field that
displays the name of the current source file and lets you point the block to a
different component file.

A source component file can be located:

- In the current working directory
- In a directory on the MATLAB path
- In a namespace, with the namespace parent directory being on the
  MATLAB path

To specify the source file, you can either browse to it or type its name directly into the
source selector field in the selector dialog box:

- If you type the name of the file, it must satisfy the location
  requirements, listed above. If the file resides in a namespace, you must
  provide the file name relative to the namespace root. If these conditions
  are not met when you type the file name, the source location cannot be
  resolved, and you get an error message.
- If you browse to the source file, you can select any Simscape source
  or protected file (that is, any file with the `.ssc` or `.sscp` extension).
  However, if the selected file does not satisfy the location requirements,
  a File Not On Path dialog opens. Click **Add** to
  add the appropriate directory to the MATLAB path and resolve
  the source location. If you click **Cancel**, the
  source location cannot be resolved and the source selection process
  is cancelled.

The buttons next to the text field in the source file selector
dialog box perform the following actions:

|  |  |
| --- | --- |
|  | Opens a file browser, to let you select the source component file. By default, the browser displays only the files with the `.ssc` or `.sscp` extension. If the Simscape Component block currently points to a source file, and the source location is successfully resolved, the browser opens in the directory where that source file resides. Otherwise, the browser opens in the current working directory. |
|  | Refreshes the preview pane of the source file selector dialog box. If you type the source component name directly into the text field of the selector dialog box, the preview pane does not automatically update. If you want to preview the block name, description, or source code of the source component before finalizing the selection, click this button. |

### Block Icon Appearance

The Simscape Component block icon appearance
changes depending on the block state.

|  |  |
| --- | --- |
|  | Simscape Component block in the library. |
|  | Simscape Component block just added to the model, when it is not pointing to a source component yet. |
|  | Simscape Component block pointing to a valid component file. The block ports are defined by the underlying component. By default, the block icon displays the component name (for example, `my_resistor`). If there is an image file with a matching name (for example, `my_resistor.png`) in the same directory as the source component file, this image replaces the default block icon. For more information, see Customizing the Block Icon. |
|  | Simscape Component block pointing to an unresolved component file. This can happen if the source component file got moved, or if it is no longer on the path. The **Add** button adds the folder to the path only for the duration of the current MATLAB session. If you do not save the path and then open the model in a subsequent session, the Simscape Component block becomes unresolved. If the source component is located in the current working directory, then there is no requirement for it to be on the path. However, if you later try to open the model from another directory, the Simscape Component block also becomes unresolved. |
