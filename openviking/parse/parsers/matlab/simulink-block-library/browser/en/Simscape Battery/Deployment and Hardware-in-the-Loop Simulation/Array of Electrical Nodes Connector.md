---
type: simulink-block
title: 'Array of Electrical Nodes Connector'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Deployment and Hardware-in-the-Loop Simulation'
documentation_page: 'arrayofelectricalnodesconnector'
documentation_source_path: 'ref/arrayofelectricalnodesconnector.html'
language: en
---

# Array of Electrical Nodes Connector

## Ports

### Conserving

### **inConnk** — Array of electrical nodes *k* to concatenate electrical array-of-nodes

Array of electrical nodes *k* that you want to concatenate, where
*k* is an integer in the range [1, **Number of Input
Connections**]. The number of ports of this type is equal to the value to
which you set the **Number of Input Connections** parameter.

### **outConn** — Concatenated array of electrical nodes electrical array-of-nodes

Concatenated array of electrical nodes.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of Input Connections** — Number of array of electrical nodes to concatenate `one` (default) | `two` | `three` | `four` | ...

Number of array of electrical nodes that you want to concatenate. You can specify
any value between `one` and
`fifty`.

### **Number of Elements in Node k** — Number of elements in connection node *k* `1` (default)

Number of elements in connection node *k*, where
*k* is an integer in the range [1, **Number of Input
Connections**]. The number of parameters of this type is equal to the value
to which you set the **Number of Input Connections** parameter.

## Libraries

Simscape / Battery / Connectors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2025a: To be removed

The Array of Electrical Nodes Connector block will be removed in a future release. Use
the Array
Connection block instead.

## Description

(To be removed) Concatenate arrays of electrical nodes into single array of electrical nodes port

The Array of Electrical Nodes Connector block concatenates
different arrays of electrical nodes into a single array of electrical nodes. This block acts
as a mux for the Simscape™ electrical domain by concatenating all input array of nodes into a single 1-D
array.

To specify the number of arrays of electrical nodes that you want to concatenate, set the
**Number of Input Connections** parameter. This action enables a number of
ports and parameters equal to the value of the **Number of Input
Connections** parameter. This block supports from one to 50 different connections
from different battery modules with different `ElectricalNodes`
properties.

To specify the number of elements in each connection node, set the **Number of
Elements in Node k** parameter, where *k* is an integer in the
range [1, **Number of Input Connections**].
