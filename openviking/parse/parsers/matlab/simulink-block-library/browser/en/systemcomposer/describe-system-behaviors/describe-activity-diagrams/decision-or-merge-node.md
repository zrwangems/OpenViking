---
type: simulink-block
title: 'Decision or Merge Node'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Describe System Behaviors / Describe Activity Diagrams'
documentation_page: 'decisionormergenode'
documentation_source_path: 'ref/decisionormergenode.html'
language: en
---

# Decision or Merge Node

## Ports

Not documented in R2025b.

## Parameters

### Decision or Merge Node

### **Show Name** — Show name of decision or merge node `off` (default) | `on`

When you select **Show Name**, the name of the node,
`MergeDecision`, is displayed within its boundaries. You can then
change the name of the node, as required. As you add more decision or merge nodes, the
editor attaches increasing numerical suffixes to the name
`MergeDecision`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Route input tokens based on evaluation of MATLAB expressions, or merge multiple input tokens onto one output flow

A decision or merge node is represented by a gray diamond. You can use the Decision
or Merge Node block for decision or merge functions, depending on how you configure
input and output token flows.

- Decision node — Consists of only one input token flow, but can have multiple output
  token flows.
- Merge node — Consists of only one output token flow, but can have multiple input
  token flows.

### Decision

The purpose of the decision node is to route incoming tokens, including control flows,
to one of the output flows based on the evaluation of boolean expressions associated with
each flow. These expressions are called *guard expressions*. The decision
node routes an input token to an output flow if the corresponding guard expression evaluates
to `true`. You can use an incoming token value in a guard expression
through the `token` keyword.

Simple activity diagram with a Merge or Decision node using the token keyword on its output branches.

All guard expressions of a decision node have an evaluation order. The activity diagram
editor routes the input token to the first output flow whose guard expression is satisfied.
This means that if the value of an incoming object token value satisfies more than one guard
expression, it exits through the output branch that is evaluated first.

### Merge

The purpose of the merge node is to allow all incoming token flows to exit through a
single, common output flow as input tokens arrive at the node.

### Decision and Merge

The Decision or Merge Node block can also behave as both a decision and
merge node. If you want to use this configuration, you must create the node with multiple
input and output flows.

If the node is both a decision and a merge node, then it is equivalent to a merge node
immediately followed by a decision node. That is, input object tokens are first merged
before routing along the most suitable output flow.

### Create a Decision or Merge Node

You can create a decision or merge node on the activity diagram canvas in two ways:

- Drag and drop the Decision or Merge Node block from the palette on
  the left to any location on the canvas.
- Hold down the left mouse button at the desired location on the canvas and drag in
  any direction. A blue outline of a node appears on the canvas. Select
  **Create MergeDecision** from the horizontal menu that
  appears below the outline.
