---
type: simulink-block
title: 'Variant Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Architecture Modeling'
documentation_page: 'variantcomponent'
documentation_source_path: 'ref/variantcomponent.html'
language: en
---

# Variant Component

## Ports

### Input

### **Source** — Input of variant choices interface

The inputs of the Variant Component block must match the inputs of
the variant choices the block contains.
### Output

### **Destination** — Output of variant choices interface

The outputs of the Variant Component block must match the outputs
of the variant choices the block contains.

## Parameters

Not documented in R2025b.

## Libraries

AUTOSAR Blockset

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Conditional variations of AUTOSAR architecture models

Use the Variant Component block to manage variations within an AUTOSAR
architecture model.

Add variant choices to a Variant Component block by right-clicking the
Variant Component block and selecting **Add Variant
Choice**.

To control the active variant choice right-click the Variant Component
block and select **Variant** > **Label Mode Active Choice**.

For AUTOSAR architecture models the active variant choice is treated as a top-level
component or composition block. Upon generating code and exporting ARXML only the variant
choices active at the time of export and code generation have descriptions.
