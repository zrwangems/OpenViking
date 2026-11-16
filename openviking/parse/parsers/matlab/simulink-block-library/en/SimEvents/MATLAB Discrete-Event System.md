---
type: simulink-block
title: 'MATLAB Discrete-Event System'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'matlabdiscreteeventsystem'
documentation_source_path: 'ref/matlabdiscreteeventsystem.html'
language: en
---

# MATLAB Discrete-Event System

## Ports

Not documented in R2025b.

## Parameters

### **System object name** — Specify the full name of the System object™ character vector

Specify the full name of the user-defined discrete-event System object class without the file extension. This entry is case
sensitive. The class name must exist on the MATLAB path.

You can specify a discrete-event System object name in one of these ways:

- Enter the name in the text box.
- Click the list arrow attached to the text box. If valid System
  objects exist in the current folder, the names appear in the list.
  Select a System object from this list.
- Browse to a folder that contains a valid discrete-event
  System object. If the folder is not on your MATLAB path, the software prompts you to add it.

If you need to create a discrete-event System object, you can create one from a template by clicking
**New**.

After you save the SimEvents®
System object, the name appears in the **System object
name** text box.

Use the full name of the user-defined discrete-event System object class name. The block does not accept a MATLAB variable that you have assigned to a discrete-event
System object class name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `System` |
| **Type**: character vector |
| **Values**: `'<Enter System Class Name>'` | character vector |
| **Default**: `'<Enter System Class Name>'` |

### **New** — Create a SimEvents System object from a template SimEvents System object

Click this button to create a SimEvents
System object from a template.

Select one of these options.

- `Basic`

  Starts MATLAB Editor and displays a template for a simple
  discrete-event System object using the fewest System object methods.

After you save the SimEvents
System object, you can enter the name in the **System object
name** text box.

### **Simulate using** — Specify the simulation mode `Code generation` (default) | `Interpreted execution`

Specify the simulation mode as `Code generation`
or `Interpreted execution`.

- `Interpreted execution`

  This mode simulates the System object based on the interpreted MATLAB language with debuggers enabled.
- `Code generation`

  This code generation mode reduces simulation time of
  SimEvents models. On the first model run, the MATLAB
  Discrete-Event System block simulates and generates
  code using only MATLAB functions supported for code generation. If the
  System object code and the block parameters do not change,
  subsequent model runs do not regenerate the code. MATLAB
  Discrete-Event System blocks also support code reuse
  for models that have multiple MATLAB Discrete-Event
  System blocks using the same System object source file. For more information, see Generate
  Code for MATLAB Discrete-Event System Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SimulateUsing` |
| **Type**: character vector |
| **Values**: `'Code generation'` | `Interpreted execution` |
| **Default**: `'Code generation'` |

## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

MATLAB discrete-event system

The MATLAB Discrete-Event System block allows you to create and author
custom discrete-event systems. With this block, you can author an event-driven
entity-flow system using MATLAB®, and use it in your Simulink® model. For more information about implementing `matlab.DiscreteEventSystem` class with MATLAB Discrete-Event
System block, see Create Custom Blocks Using MATLAB Discrete-Event System Block.

Below, there are six examples to help you learn how to create custom blocks using the
MATLAB Discrete-Event System block.

1. Delay Entities with a Custom Entity Storage Block
2. Create a Custom Entity Storage Block with Iteration Event
3. Custom Entity Storage Block with Multiple Timer Events
4. Custom Entity Generator Block with Signal Input and Signal Output
5. Build a Custom Block with Multiple Storages
6. Create a Custom Resource Acquirer Block
