---
type: simulink-block
title: 'Invoke AUTOSAR Server Operation'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Component Modeling / Component Development / AUTOSAR Communication'
documentation_page: 'invokeautosarserveroperation'
documentation_source_path: 'ref/invokeautosarserveroperation.html'
language: en
---

# Invoke AUTOSAR Server Operation

## Ports

### Input

### **Input argument** — Input signal for an input argument scalar | vector | matrix

Input signal for an input argument that is sent to the block.

The **Operation prototype** parameter determines the number and
names of input ports that appear on the block. Connect signal lines to the input
ports.
### Output

### **Output argument** — Output signal for an output argument scalar | vector | matrix

Output signal for an output argument that the function returns.

The **Operation prototype** parameter determines the number and
names of output ports that appear on the block. Connect signal lines to the output
ports.

## Parameters

### **Client port name** — AUTOSAR client port short name character vector

Specify a valid AUTOSAR short-name identifier for the client port.

### **Operation prototype** — Controls the type and number of inports and outports of the block character vector

Specify an operation prototype in this format:

`operation(prt1
datatype1
arg1, prt2
datatype2
arg2, ... prtN
datatypeN
argN, ...)`

- *`operation`* — Name of the operation
- *`prtN`*. Either `IN` or
  `OUT`, which indicates whether data passes into or out of the
  function.
- *`datatypeN`* — Text indicating data type, which
  can be an AUTOSAR basic data type or record, Simulink data type, or array.
- *`argN`* — Name of the argument

### **Interface path** — Path to client-server interface XML file character vector

Specify the reference path for the client-server interface XML file that you
provide.

### **Server type** — Server type value `Application software` (default) | `Basic software`

Select a server type:

- `Application software` — For communication with
  an application software component.
- `Basic software` — For communication with
  AUTOSAR Basic Software.

### **Show error status** — Whether client port receives error status of client-server communication `off` | `on`

If you select this check box, the client port receives the error status of
client-server communication.

### **Sample time (-1 for inherited)** — Block sample time -1 (default) | scalar

Block sample time. The default sets the block to inherit its sample time from the
model.

## Libraries

AUTOSAR Blockset

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009b**

## Description

Configure AUTOSAR client port to access Basic Software or application software components

Use this block to configure an AUTOSAR client port for your Simulink® model, which provides access to Basic Software or application
software components. To configure this block:

1. Copy or drag this block from the AUTOSAR library into your
   model.
2. Double-click the block to open the Invoke AUTOSAR Server
   Operation dialog box.
3. Specify the parameters and click **OK**.
   This action updates the number of inports and outports to
   match the operation prototype.
4. Connect this block to other blocks in your model as
   required.
5. Save and build the model to generate AUTOSAR-compliant code
   and XML files.

If you run a SIL simulation with a model that contains an Invoke AUTOSAR
Server block, the software sets the return arguments from the block to
ground values.

Simulink does not support pointer data types. If you want to pass a
`NULL` pointer as an input argument to your operation:

1. Specify the data type of the argument as
   `uint8`.
2. Connect a constant signal with data type
   `uint8` and value 0 to the
   corresponding input port of the block.
3. Check that your client-server interface XML file
   specifies the argument as an array with data type
   `uint8`.
