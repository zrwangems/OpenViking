---
type: simulink-block
title: 'PLC Controller Suite'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Organizational Units'
documentation_page: 'plccontrollersuite'
documentation_source_path: 'ref/plccontrollersuite.html'
language: en
---

# PLC Controller Suite

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

**Introduced in R2019a**

## Description

PLC Controller

In Ladder Diagram, the controller is a top organizational unit that typically consists of
task and controller tags. There can be a single task or multiple tasks. Tasks inside a
controller are executed in parallel. There are two types of controller blocks available in
Simulink®
PLC Coder™:

- PLC Controller Suite
- PLC Controller

PLC controller suite is a block hierarchy that models a simple complete Ladder Logic
Controller structure whereas a PLC controller block consists of ladder logic semantics. The
controller tags store the information of global variables such as DataType, Mapping type,
Port, Address etc. The global variables defined for a ladder diagram form the input and output
ports of the controller.
