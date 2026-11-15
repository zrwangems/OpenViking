---
type: simulink-block
title: 'Action Node'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Describe System Behaviors / Describe Activity Diagrams'
documentation_page: 'actionnode'
documentation_source_path: 'ref/actionnode.html'
language: en
---

# Action Node

## Ports

Not documented in R2025b.

## Parameters

### Action Node

### **Name** — Action node name `Action` (default) | action node name

Name of the action node. By default, the activity diagram editor names the first
action node placed on the canvas as `Action`. As you add more action
nodes, the editor attaches increasing numerical suffixes to the name
`Action`.

**Example:** `Action2`

### **Behavior Type** — Activity diagram or MATLAB function `MATLAB` (default) | `Activity`

Indicate the type of activity that the action node represents.

- `MATLAB` — Contains an existing MATLAB function such as `rand`, or a custom function
  written in an `.m` file
- `Activity` — Contains another activity diagram that
  consumes and produces tokens

### **Visibility of Pin Name** — Option to show pin names on action node `off` (default) | `on`

When you select this check box, the names of all input and output pins to the
selected action node are displayed.

### **MATLAB Function Name** — Name of MATLAB function function name

Name of the MATLAB function that an action node implements. The function can either be an
existing MATLAB function, or a custom function that you have authored in an
`.m` file.

**Example:** `customfunction_add`

#### Dependencies

To enable this parameter, set **Behavior Type** to
`MATLAB` in the Property Inspector.

### **Duration** — Time spent on execution of action node `0` (default) | positive integer

The number of time units an activity diagram spends on the execution of an action
node. An activity diagram executes MATLAB functions of an action node at the end of
the duration period.

### **Stereotype** — List of stereotypes from imported profiles names of available stereotypes

This list contains stereotypes from imported profiles. To assign a stereotype to
an action node, select the stereotype from the list.

You can also use `<new/edit>` option to manage profiles using
Profile
Editor.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Process object tokens through MATLAB function or nested activity diagram

An action node represents a specific action to execute within an activity diagram. This
action is realized either through a MATLAB® function or a nested activity diagram.

Action nodes process incoming tokens to produce new tokens. Input pins consume input
tokens. Newly generated tokens exit through the output pins.

For action node to execute, their input pins must hold the minimum number of object tokens
specified by the token multiplicity parameter, and all incoming control flows must offer a
control token.

Action nodes with MATLAB behavior terminate when the MATLAB function completes. However,
action nodes with activity behavior terminate when all the output parameter nodes, flow final
nodes and activity final nodes have at least one token each.

For a roadmap of the activity diagram topics, see Describe System Behavior Using Activity Diagrams.

### Create an Action Node

You can create an action node on the activity diagram canvas in two ways:

- Drag the Action Node block from the palette on the left to any
  location on the canvas.
- Hold the left pointer at the desired location on the canvas and drag in any
  direction. A blue outline of a node appears on the canvas. From the menu that appears
  below the outline, select **Create Action**.
