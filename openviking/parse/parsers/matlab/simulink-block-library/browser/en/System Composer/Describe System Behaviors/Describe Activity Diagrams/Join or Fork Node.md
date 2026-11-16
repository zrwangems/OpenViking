---
type: simulink-block
title: 'Join or Fork Node'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Describe System Behaviors / Describe Activity Diagrams'
documentation_page: 'joinorforknode'
documentation_source_path: 'ref/joinorforknode.html'
language: en
---

# Join or Fork Node

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Synchronize multiple input tokens into one output, or replicate one input token on all output flows

A Join or Fork Node block is represented by a thick gray line with rounded
ends. You can use the Join or Fork Node block for either join or fork
functions, depending on how you configure input and output token flows.

- Join node — Consists of only one output token flow, but can have multiple input
  token flows
- Fork node — Consists of only one input token flow, but can have multiple output
  token flows

### Join

The purpose of the join node is to join all incoming token flows, including control
flows, into one output flow. When an object token is present on all input flows, the join
node synchronizes these tokens into one consolidated token that exits through the output
flow. When a control token is present on all input flows, the join node outputs one
representative control token. The data type of all input object tokens to the join node must
be the same.

### Fork

The function of the fork node is to replicate the incoming token, and send a copy to
each output flow.

### Create a Join or Fork Node

You can create a join or fork node on the activity diagram canvas in two ways:

- Drag and drop the Join or Fork Node block from the palette on the
  left to any location on the canvas.
- Hold down the left mouse button at the desired location on the canvas and drag in
  any direction. A blue outline of a node appears on the canvas. Select
  **Create JoinFork** from the horizontal menu that appears
  below the outline.
