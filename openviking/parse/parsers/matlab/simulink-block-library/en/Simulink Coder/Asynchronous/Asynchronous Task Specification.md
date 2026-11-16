---
type: simulink-block
title: 'Asynchronous Task Specification'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Asynchronous'
documentation_page: 'asynchronoustaskspecification'
documentation_source_path: 'ref/asynchronoustaskspecification.html'
language: en
---

# Asynchronous Task Specification

## Ports

### Input

### **Port\_1** — Interrupt input signal scalar

Interrupt input signal received from a root-level Inport block.
### Output

### **Port\_1** — Interrupt signal with priority scalar

Interrupt signal with specified task priority that triggers a
function-call subsystem.

## Parameters

### **Task priority** — Priority of asynchronous task that calls function-call subsystem `10` (default)

Specify an integer or [] as the priority of the asynchronous task that
calls the connected function-call subsystem. The priority must be a value
that generates relevant rate transition behaviors.

- If you specify an integer, it must match the priority value of the
  interrupt signal initiator in the parent model.
- If you specify [], the priority does not have to match the
  priority of the interrupt signal initiator in the top model. The
  rate transition algorithm is conservative (not optimized). The
  priority is unknown but static.

Consider the following model.

The referenced model has the following content.

If the **Task priority** parameter is set to 10, the
Async Interrupt block in the parent model must also have
a priority of 10. If the parameter is set to [], the priority of the
Async Interrupt block can be a value other than
10.

## Libraries

Simulink Coder / Asynchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011a**

## Description

Specify priority of asynchronous task represented by referenced model triggered by asynchronous interrupt

The Asynchronous Task Specification block specifies parameters, such as
the task priority, of an asynchronous task represented by a function-call subsystem with
a trigger from an asynchronous interrupt. Use this block to control scheduling of
function-call subsystems with triggers from asynchronous events. You control the
scheduling by assigning a priority to each function-call subsystem within a referenced
model.

To use this block, follow the procedure in Convert Asynchronous Subsystem to a Referenced Model.

Observe in the figure:

- The block must reside in a referenced model between a root-level Inport block
  and a function-call subsystem. The Asynchronous Task
  Specification block must immediately follow and connect directly to
  the Inport block. The combination of these two blocks constitutes
  the modeling style known as JMAAB-B.
- The Inport block must receive an interrupt signal from an Async Interrupt
  block that is in the parent model.
- The Inport block must be configured to receive and send function-call trigger
  signals.

How to use Asynchronous Task Specification block
