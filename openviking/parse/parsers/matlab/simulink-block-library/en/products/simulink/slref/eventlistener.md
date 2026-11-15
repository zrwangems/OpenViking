---
type: simulink-block
title: 'Event Listener'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Event Functions'
documentation_page: 'eventlistener'
documentation_source_path: 'slref/eventlistener.html'
language: en
---

# Event Listener

## Ports

Not documented in R2025b.

## Parameters

### **Event type** — Select event type for subsystem `Initialize` (default) | `Reinitialize` | `Reset` | `Terminate`

Select event type for subsystem to execute initialize, reinitialize,
reset, or terminate algorithms.

`Initialize`
:   Select to trigger the execution of an Initialize
    Function block with an initialize event.

`Reinitialize`
:   Select to trigger the execution of an Reinitialize
    Function block with an reinitialize event.

`Reset`
:   Select to trigger the execution of a Reset
    Function block with a reset event.

`Terminate`
:   Select to trigger the execution of a Terminate
    Function block with a terminate event.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EventType` |
| **Type:** character vector |
| **Value:** `'Initialize'` | `'Reinitialize'` | `'Reset'` | `'Terminate'` |
| **Default:** `'Initialize'` |

### **Event name** — Specify event name `reinit` | `reset` | event name

Specify event name for Reinitialize Function or
Reset Function block. Simulink® displays the name on the face of the Reinitialize
Function or Reset Function block. The event name
is also the name of the reinitialize event port on the Model
or Subsystem block containing the Reinitialize
Function block or the name of the reset event port on the
Model block containing the Reset Function
block.

`reinit`
:   Default event name when **Event type** is set
    to `Reinitialize`.

`reset`
:   Default event name when **Event type** is set
    to `Reset`.

When entering the **Event name**, the auto-completion
list provides some suggestions. The list is not complete.

The **Event name** must be a valid MATLAB® variable name.

#### Dependency

To enable this parameter, set the **Event type**
parameter to `Reinitialize` or
`Reset`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EventName` |
| **Type:** character vector |
| **Value:** `'reinit'` | `'reset'` | `'<event name>'` |
| **Default:** `'reinit'` or `'reset'` |

### **Enable variant condition** — Control activating the variant control (condition) off (default) | on

Control activating the variant control (condition) defined with the
**Variant control** parameter.

off
:   Deactivate variant control of subsystem.

on
:   Activate variant control of subsystem.

When you select **Enable variant condition**, a badge
indicates the change:

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Variant` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

**Note**

- A reinitialize event port of a Model or
  Subsystem block can be conditional and propagates the net
  variant conditions defined on the corresponding Reinitialize
  Function block in the referenced model or subsystem.
- A reset event port of a Model block can be conditional and
  propagates the net variant conditions defined on the corresponding
  Reset Function block in the referenced model.
- Initialize and terminate event ports are always unconditional because they
  control both the model default and block-specific initialize and terminate
  events of the referenced model. If you define an Initialize
  Function block in the referenced model, it corresponds to an
  explicit initialize event.

### **Variant control** — Specify variant control (condition) expression `Variant` (default) | logical expression

Specify variant control (condition) expression that executes a variant
Initialize Function, Reinitialize
Function, Reset Function, or Terminate
Function block when the expression evaluates to
`true`.

`Variant`
:   Default name for a logical (Boolean) expression.

logical expression
:   A logical (Boolean) expression or a
    `Simulink.VariantExpression` object
    representing a Boolean expression.

    If you want to generate code for your model, define the
    variables in the expression as
    `Simulink.Parameter` objects.

#### Dependency

To enable this parameter, select the **Enable variant
condition** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControl` |
| **Type:** character vector |
| **Value:** `'Variant'` | `'<logical expression>'` |
| **Default:** `'Variant'` |

### **Generate preprocessor conditionals** — Select if variant choices are enclosed within C preprocessor conditional statements off (default) | on

Select if variant choices are enclosed within C preprocessor conditional
statements.

off
:   Do not enclose variant choices within C preprocessor
    conditional statements.

on
:   When generating code for an ERT target, enclose variant
    choices within C preprocessor conditional statements
    (`#if`).

#### Dependency

To enable this parameter, select the **Enable variant
condition** parameter.

When you select **Generate preprocessor
conditionals**, a badge indicates the change:

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GeneratePreprocessorConditionals` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

### R2025a: Variant control variables in mask and model workspaces supported

You can define variant control variables in the mask and model workspaces to
control active variants in Initialize Function, Reset Function, Reinitialize
Function, and Terminate Function blocks, provided
the **Generate preprocessor conditionals** parameter is
`off`.

## Description

Event port for Initialize Function, Reinitialize Function, Reset Function, and Terminate Function blocks

The Event Listener block serves as an event port for the Initialize Function, Reinitialize
Function, Reset Function, and Terminate Function blocks.
