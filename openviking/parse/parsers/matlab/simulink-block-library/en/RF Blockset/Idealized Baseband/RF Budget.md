---
type: simulink-block
title: 'RF Budget'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'rfbudget'
documentation_source_path: 'ref/rfbudget.html'
language: en
---

# RF Budget

## Ports

### Input

### **Port\_1** — Time-dependent input signal real scalar | real column | complex scalar | complex column

Time-dependent input signal, specified as a real scalar, real column, complex
scalar, or complex column. A column represents consecutive points in time.

**Data Types:** `double` | `single`
### Output

### **Port\_1** — Time-dependent output signal complex scalar | complex column

Time-dependent output signal, returned as a complex scalar or complex column. The
time-dependent output signal is equal in size to the time-dependent input
signal.

**Data Types:** `double` | `single`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **RF budget source** — RF budget source `rfbudget object` (default) | `RF Budget Analyzer App`

RF budget source, specified as `rfbudget object` or `RF
Budget Analyzer App`

### **rfbudget object** — `rfbudget` object as source `rfbudget([],2.1e9,-30,100e6)` (default) | `rfbudget` object

Specify an `rfbudget` object as source to model mismatch
loss.

#### Dependencies

To enable this parameter, set **RF budget source** to
`rfbudget object`.

### **Open RF Budget Analyzer App** — RF Budget Analyzer app as source button

Click this button to open the RF Budget Analyzer app to create an RF chain and use
it as a source to model mismatch loss. After creating the your RF chain, click the
**Update Block** button to update the RF Budget block with the
designed RF chain.

#### Dependencies

To enable this parameter, set **RF budget source** to
`RF Budget Analyzer App`.

### **Simulate supported blocks using code generation** — Simulate model using generated C code `off` (default) | `on`

Select this option to simulate the model using generated C code. The first time
you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
simulations as long as the model does not change. This option requires additional
startup time, but the speed of the subsequent simulations is faster than interpreted
execution simulation.

### **Edit System** — Edit or expand RF Budget block button

Click this button to break the RF Budget block's links to the
library and replace the variables with values that the block estimates using the block
parameters. When clicking this button, the software converts the RF Budget block is
either made a simple unmasked subsystem, or gets expanded.

Clicking this button opens a dialog box with these options:

- **Edit System** — Edit the internal variables without
  expanding the subsystem.
- **Expand System** — Edit the subsystem and Expand the
  subsystem in the Simulink canvas. The block will expand
  into a chain of elements.

  **Note**

  Mismatch loss will not computed between two elements if the elements are
  unidirectional and perfectly matched.
- **Cancel** — Cancel the operation.

**Note**

You cannot undo the operation once you click the **Edit
System** or **Expand System** button.

### Advanced

### **Frequency resolution** — Frequency resolution for calculating mismatch loss `51` (default) | positive scalar

Frequency resolution at which the block models the mismatch loss, specified as a
positive scalar. You can:

- Increase the frequency resolution if your input signal is fast
  varying.
- Decrease the frequency resolution if your input signal is slow varying. This
  option decreases the computation time.
- Set the frequency resolution to `1` if your input signal is
  constant.

### **Modeling bandwidth (Hz)** — Modeling bandwidth for calculating mismatch loss `100e6` (default) | positive scalar

Bandwidth at which mismatch loss is modeled, specified as a positive scalar. You
can

- Increase the modeling bandwidth if your input signal bandwidth is wider.
- Decrease the modeling bandwidth if your input signal bandwidth is narrower.
  In this case, you can decrease the frequency resolution as well to reduce the
  computation time.

## Libraries

RF Blockset / Idealized Baseband

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Simulate RF budget chain of 2-port elements in Idealized Baseband simulation environment

Use the RF Budget block to simulate RF budget results for a chain of 2-port elements in
Idealized Baseband simulation environment. While simulating the RF budget, the block accounts
for mismatch losses by considering the effects of reflection and bidirectional power flow. You
can use the `rfbudget` object or use
the RF
Budget Analyzer app as a source for the RF Budget block.
