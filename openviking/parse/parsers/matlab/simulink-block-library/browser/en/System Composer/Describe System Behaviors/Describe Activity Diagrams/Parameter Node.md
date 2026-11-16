---
type: simulink-block
title: 'Parameter Node'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Describe System Behaviors / Describe Activity Diagrams'
documentation_page: 'parameternode'
documentation_source_path: 'ref/parameternode.html'
language: en
---

# Parameter Node

## Ports

Not documented in R2025b.

## Parameters

### Parameter Node

Parameter nodes act as buffers for object tokens during execution of a nested
activity. Parameter nodes inherently affect the corresponding pins.

### **Name** — Name of parameter node string

Name of the input or output parameter node. By default inheritance,
the parameter is called `InputPin` or
`OutputPin` depending on its configuration. As you
add more input or output pins to action nodes, increasing numerical
suffixes are added to `InputPin` or
`OutputPin`, respectively.

### **Token Multiplicity** — Number of tokens required to begin execution `1` (default) | positive integer

The number of tokens required at an input parameter node for the corresponding action node to
begin execution. If an input parameter node has a multiplicity greater
than one, it can hold multiple tokens. Upon execution, an action node
takes in exactly the number of object tokens specified by the
multiplicity parameter.

### **Is Streaming** — Option to enable or disable streaming `off` (default) | `on`

Enable or disable streaming for the input or output parameter node.
The value of this streaming control automatically applies to the
corresponding input or output activity pin of the action node.

### **Stereotype** — List of stereotypes from imported profiles names of available stereotypes

This list contains stereotypes from imported profiles. To assign a
stereotype to a parameter node, select the stereotype from the
list.

You can also use `<new/edit>` option to manage
profiles using Profile Editor.

### Object Type

An input or output pin can handle object tokens of a certain type. In the Property Inspector, the **Object Type** section for a pin allows you to specify the type and other properties of an object token.

### **Name** — Object type held by parameter node `<owned>` (default) | `<inherit>` | `custom type`

The type of object held by a parameter node.

- `<owned>` — Select properties for
  an object token, such as type, dimension, complexity, and
  unit from the Property Inspector.
- `<inherit>` — Inherit the object
  type from the previous pin.
- `custom type` — Choose from the list of
  custom types you created using the Types Editor.

### **Direction** — Direction of token flow through a parameter node `Input` | `Output`

This parameter is automatically set to `Input` or
`Output`, depending on whether you create an input
pin or output pin, respectively.

### **Type** — Token data type `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `MATLAB Class`

Data type of the token. For more information on using MATLAB class type, see Model Complex Objects in Activity Diagrams Using MATLAB Class Tokens.

#### Dependencies

To enable this parameter, set **Name** to `<owned>`.

### **Dimensions** — Token dimensions `1` (default) | positive integer

Dimensions of the token.

#### Dependencies

To enable this parameter, set **Name** to `<owned>`.

### **Unit** — Token unit string

Custom unit that you assign to the token.

#### Dependencies

To enable this parameter, set **Name** to `<owned>`.

### **Complexity** — Token complexity `real` (default) | `complex` | `auto`

Complexity of the token.

#### Dependencies

To enable this parameter, set **Name** to `<owned>`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Process tokens through a nested activity diagram

A parameter node acts as a buffer for object tokens and
directs tokens into or out of a nested activity. The directionality of the parameter
node represents input or output. You can connect parameter node by object flows.

For an action node with activity behavior type, when you create a pin, the software
creates a corresponding parameter node inside the nested activity.

These are the two types of input and output parameter nodes:

- Streaming parameter node

  Streaming input parameter node
- Non-streaming parameter node

  Non-streaming input parameter node
