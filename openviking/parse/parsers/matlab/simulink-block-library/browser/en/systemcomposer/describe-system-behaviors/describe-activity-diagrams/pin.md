---
type: simulink-block
title: 'Pin'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Describe System Behaviors / Describe Activity Diagrams'
documentation_page: 'pin'
documentation_source_path: 'ref/pin.html'
language: en
---

# Pin

## Ports

Not documented in R2025b.

## Parameters

### Pin

Pins act as buffers for object tokens during execution of an activity
diagram.

Each pin is associated with a certain data type. All tokens of a pin must have the data type associated with the pin.

For an action node with an activity behavior type, the pins represent their
corresponding parameter nodes. For more information, see Parameters.

### **Name** — Name of pin string

Name of the input or output pin. By default, the pin is called `InputPin` or `OutputPin` depending on its configuration. As more input or output pins are added to action nodes, increasing numerical suffixes are added to `InputPin` or `OutputPin`, respectively.

### **Token Multiplicity** — Number of tokens required to begin execution `1` (default) | positive integer

The number of tokens required at an input pin for the corresponding action node to begin execution. If an input pin has a multiplicity greater than one, it can hold multiple tokens. Upon execution, an action node takes in exactly the number of object tokens specified by the multiplicity parameter.

Token multiplicity applies only to input pins of an action node.

### **Argument Order** — Order of pin in argument list of MATLAB function `1` (default) | positive integer

In a MATLAB function defined for an action node, each input and output
argument corresponds to an input or output pin, respectively, specified
by the argument order of the pin.

For example, if the argument order of an input pin is 2, then this pin
represents the second input argument of the MATLAB function.

### **Is Streaming** — Option to enable or disable streaming `off` (default) | `on`

Enable or disable streaming for the input or output pin of an action
node with a nested activity. The value of this streaming control
automatically applies to the corresponding input or output activity
parameter nodes in the nested activity.

### **Stereotype** — List of stereotypes from imported profiles names of available stereotypes

This list contains stereotypes from imported profiles. To assign a
stereotype to a pin, select the stereotype from the list.

You can also use `<new/edit>` option to manage
profiles using Profile Editor.

### Object Type

An input or output pin can handle object tokens of a certain type. In the Property Inspector, the **Object Type** section for a pin allows you to specify the type and other properties of an object token.

### **Name** — Object type held by pin `<owned>` (default) | `<inherit>` | `custom type`

The type of object held by an action node pin.

- `<owned>` — Select properties for an object token, such as type, dimension, complexity, and unit from the Property Inspector.
- `<inherit>` — Inherit the object type from the previous pin.
- `custom type` — Choose from the list of custom types you created using the Types Editor.

### **Direction** — Direction of token flow through pin `Input` | `Output`

The direction of token flow through a pin of an action node. This parameter is automatically set to `Input` or `Output`, depending on whether you create an input pin or output pin, respectively.

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

### R2024b: Enable streaming for action nodes

You can configure streaming pins for action nodes with a nested activity diagram.

Enable or disable streaming for input or output pins by selecting the **Is Streaming** check box in the Property Inspector.

## Description

Direct tokens into or out of an action node

A pin acts as a buffer for object tokens and directs
tokens into or out of an action node. The directionality of the pin represents input or
output. You can connect pins by object flows.

These are the two types of input and output pins:

- Streaming pins

  Streaming input pin
- Non-streaming pins

  Non-streaming input pin

Action nodes with both types of pins begin execution only once all the input pins hold
the minimum number of object tokens. For input pins, once the multiplicity condition is
met, the software does not reevaluate the condition until the nested activity restarts.
Action nodes with both types of pins terminate only once all the output pins receive at
least one token.

Streaming pins and non-streaming pins differ based on how tokens are handled when the
action node is executing.

**Note**

Streaming pins can only be configured for action nodes with a nested activity
diagram.

### Streaming Pins

Streaming input pins continue to accept and buffer all the tokens that arrive at
the pin once the nested activity begins to execute. As the tokens arrive, the
software forwards the tokens to the corresponding input parameter node.

Streaming output pins enable the corresponding output parameter nodes to accept
and forward incoming tokens. Output parameter nodes can forward the tokens
regardless of whether the action is completed.

### Non-Streaming Pins

Non-streaming input pins block any incoming object tokens while the action node
executes, which causes output object tokens to go into a pending state in the output
pins of the previous nodes. If an output pin already has a pending token, any new
generated token is discarded. This action is called blocking behavior.

Non-streaming output pins rely on the corresponding output parameter node to hold
any incoming tokens. The tokens are forwarded to the output pin only when the action
node finishes execution.
