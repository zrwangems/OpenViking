---
type: simulink-block
title: 'Proof Assumption'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2023b
official_category: 'Objectives and Constraints'
documentation_page: 'proofassumption'
documentation_source_path: 'ref/proofassumption.html'
language: en
---

# Proof Assumption

## Ports

### Input

### **Port\_1** — Input signal specified as a scalar or cell array scalar | cell array

The Proof Assumption block accepts signals of
all built-in data types supported
by the Simulink software. For a discussion on the data types supported by
the Simulink software, see Data Types Supported by Simulink. The block does not
support complex input signals.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal returned as a scalar or a cell array scalar | cell array

The Proof Assumption block returns signals of all built-in data types
supported by the Simulink software. For more information about supported data types,
see Data Types Supported by Simulink.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Enable** — Whether block is enabled `on` (default) | `off`

Specify whether the block is enabled. If selected (the default), the
Simulink
Design Verifier software uses the block when proving properties of a model.
Clearing this option disables the block, that is, causes the Simulink
Design Verifier software to behave as if the Proof Assumption block did not
exist. If this option is not selected, the block appears grayed out in the
Simulink Editor.

### **Type** — Whether the block behaves as a Proof Assumption or Test Condition block `on` (default) | `off`

Specify whether the block behaves as a Proof Assumption or
Test Condition block. Select `Test
Condition` to transform the Proof Assumption block into a
Test Condition block.

### **Values** — Proof Assumption scalar (default) | cell array

Use the **Values** parameter to constrain signal values
in test cases. Specify any combination
of scalars and intervals in the form of a MATLAB® cell array. For more information, see Use Parameter Configuration File.

### **Display values** — Display the contents of values parameter `on` (default) | `off`

Specify whether the block displays the contents of its
**Values** parameter in the Simulink Editor.

### **Pass through style(show Outport)** — Whether block displays an output port in the Simulink Editor `on` (default) | `off`

If selected, the block displays its output port, which allows the input
signal to pass through to the block output. If not selected, the block hides
its output port and terminates the input signal.

**Example:** The following graphics illustrate the appearance of the block in
each case.

**Pass through style (show Outport): Selected**

**Pass through style (show Outport): Deselected**

## Libraries

Simulink Design Verifier / Objectives and Constraints

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007a**

## Description

Constrain signal values when proving model properties

When operating in property-proving mode, the Simulink®
Design Verifier™ software proves that properties of your model satisfy specified criteria
(see What Is Property Proving?). In this mode, you
can use Proof Assumption blocks to define assumptions for signals in your model. The
**Values** parameter lets you specify constraints on signal values
during a property proof. The block applies the specified **Values**
parameter to its input signal, and the Simulink
Design Verifier software proves or disproves that the properties of your model satisfy the
specified criteria.

The block's parameter dialog box also allows you to:

- Enable or disable the assumption.
- Specify that the block should display its **Values**
  parameter in the Simulink Editor.
- Specify that the block should display its output port.

**Note**

The Simulink and Simulink
Coder™ software ignore the Proof Assumption block during model simulation and
code generation, respectively. The Simulink
Design Verifier software uses the Proof Assumption block only when proving model
properties.

You can constrain signal values in property proofs by using
**Values** parameters. For more information, see Use Parameter Configuration File.
