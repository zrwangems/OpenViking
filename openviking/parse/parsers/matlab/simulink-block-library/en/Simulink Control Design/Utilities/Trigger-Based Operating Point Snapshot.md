---
type: simulink-block
title: 'Trigger-Based Operating Point Snapshot'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'triggerbasedoperatingpointsnapshot'
documentation_source_path: 'ug/triggerbasedoperatingpointsnapshot.html'
language: en
---

# Trigger-Based Operating Point Snapshot

## Ports
```yaml
ports:
- name: Trigger
  summary: Trigger control signal scalar
  direction: input
```

### Input

### **Trigger** — Trigger control signal scalar

Trigger control signal, specified as a scalar signal.
## Parameters
```yaml
parameters:
- name: Trigger type
  summary: Type of control signal rising (default) | falling | either | function-call
  group: ''
  block_parameter: '''TriggerType'''
  type: character vector
  values: '''rising''''falling''''either''''function-call'''
  default: '''rising'''
```

### **Trigger type** — Type of control signal `rising` (default) | `falling` | `either` | `function-call`

Type of control signal that triggers the operating point snapshot.

- `rising` — Trigger when the control signal crosses zero
  while increasing.
- `falling` — Trigger when the control signal crosses
  zero while decreasing.
- `either` — Trigger when the control signal crosses zero
  while either increasing or decreasing.
- `function-call`: Trigger when the control signal
  receives a function-call event from a Stateflow® chart, a Function-Call Generator block, an
  S-Function block, or a Hit Crossing block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'TriggerType'` |
| **Type:** `character vector` |
| **Values:** `'rising'``'falling'``'either'``'function-call'` |
| **Default:** `'rising'` |
## Libraries

Simulink Control Design / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

### R2023b: Library location changed

The Trigger-Based Operating Point Snapshot block is now in the
**Simulink Control Design/Utilities** sublibrary.

In R2023b, when you open a model saved in a previous release, the library links for
Trigger-Based Operating Point Snapshot blocks update automatically.

## Description

Generate operating points at triggered events

The Trigger-Based Operating Point Snapshot block takes snapshot operating
points of a Simulink® model at triggered events indicated by the input trigger signal. For example,
you can configure the block to take a snapshot whenever the trigger signal crosses zero while
increasing.

You can then linearize your model at the operating points using the
`linearize` function or the Model Linearizer app.
