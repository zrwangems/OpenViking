---
type: simulink-block
title: 'Reference Component'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Architectures, Requirements, and Allocations / Author Architecture Models'
documentation_page: 'referencecomponent'
documentation_source_path: 'ref/referencecomponent.html'
language: en
---

# Reference Component

## Ports

### Input

### **Source** — Input connection from another component interface

If you connect to a source component, the interfaces on the ports are
shared.
### Output

### **Destination** — Output connection to another component interface

If you connect to a destination component, the interfaces on the ports are
shared.
### Physical

### **Physical** — Physical connection to another component physical interface

If you connect to another component, the physical interfaces on the ports are
shared.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Link to architectural definition or Simulink behavior

Use a Reference Component block to link an architectural definition of a
System Composer™ component, an architectural definition of an AUTOSAR component, or a Simulink® behavior.

Add ports to the block to connect to other components. Define
an interface for the ports, add properties associated with the component using stereotypes, and
define parameters.

Reference Component block

To add or connect System Composer components:

- Add a Reference Component block from the
  **Modeling** tab or the palette. You can also click and drag a box on
  the canvas, then select the Reference Component block.

  **Tip**

  You can drag to add a reference component linked to a model or subsystem into a
  System Composer model. Drag a model or subsystem file from the file explorer to add a
  reference component to the architecture model canvas.

  For example, dragging a model SLX file into the architecture model canvas adds a
  Reference Component block that references the model in the SLX
  file.

  Files that you drag to add must be on the MATLAB® path. Creating reference components by dragging files from the
  MATLAB Editor into the model canvas is not supported.
- Attach a referenced model by double-clicking the Reference Component
  block to open the **Block Parameters** dialog box.
- Add and edit ports on a Reference Component block. Click the edge of
  the block to add a port, then use the Property
  Inspector to rename the port.
- To import your shared data dictionary from your System Composer architecture model, in the Model Explorer
  for your referenced model, under **Model Properties**, on the
  **External Data** tab, click **Browse**.
  Use the Interface
  Editor to assign interfaces to the ports of your referenced model and edit
  interface definitions.
- Click and drag any port to create a connection. Connect to another component. You
  can also create a new component to complete the connection.
- To connect Reference Component blocks to architecture or composition
  model root ports, drag from the component ports to the containing model boundary. When
  you release the connection, a root port is created at the boundary.

**Note**

You can add a mask icon to your component to illustrate the system represented by your component. For more information, see Add Mask Icon on Component.

To manage Reference Component block contents:

- When you create a Reference Component block, you have the option to
  right-click the component and select `Block Parameters`. From
  here, you can specify your reference model or subsystem name, if it already exists. The
  reference model or subsystem can be a System Composer architecture, AUTOSAR architecture, or a Simulink model or subsystem.
- To add or remove stereotypes from Reference Component blocks, first
  import the profile into the referenced model or subsystem using the Profile
  Editor. If you apply multiple stereotypes to the reference component, to change
  the stereotype order, see Change Stereotype Order Using Manage Profiles Tool.
- To break the reference link for a Reference Component block, you have
  the option to right-click and select **Inline Model**, which
  removes the contents of the architecture model referenced by the specified component and
  breaks the link to the reference model. The Reference Component block
  becomes a regular Component block.

With a regular Component
block, you can right-click the block and convert it to a reference component.

- To save the contents of the component as an architecture model or subsystem that can
  be referenced in multiple places and kept in sync, select **Create Architecture** > **Architecture**. The component becomes a reference component that links to the referenced
  architecture model or subsystem.

  **Note**

  To type ports on architecture subsystems with interfaces, you must link an external
  interface data dictionary. Architecture subsystems do not contain a model workspace. For
  more information, see Manage Interfaces with Data Dictionaries.
- To save the contents of the component as a software architecture model, select **Create Architecture** > **Software Architecture**. `Create Architecture` and then select
  `Software Architecture`. For more information, see Export Architecture to Software Architecture.
- To save the contents of the component as an AUTOSAR architecture model, select **Create Architecture** > **AUTOSAR Architecture**. For more information, see Create AUTOSAR Architecture from Component.
- To create a new Simulink reference model or subsystem and link to it, select **Create Behavior** > **Simulink Behavior**. For more information, see Implement Component Behavior Using Simulink.
- To link to a known model or subsystem, which can be a System Composer architecture model, a Simulink model, or an AUTOSAR architecture model, select **Link to
  Model**.

**Note**

Components with physical ports cannot be saved as architecture models, model references,
software architectures, or Stateflow® chart behaviors. Components with physical ports can only be saved as subsystem
references or as subsystem component behaviors.
