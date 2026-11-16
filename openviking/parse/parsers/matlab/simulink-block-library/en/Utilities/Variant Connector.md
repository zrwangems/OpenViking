---
type: simulink-block
title: 'Variant Connector'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'variantconnector'
documentation_source_path: '../simscape/ref/variantconnector.html'
language: en
---

# Variant Connector

## Ports

### Conserving

### **Port\_1** — Condition port untyped conserving port

This port is located on the left side of the block and is labeled with a
rectangle. During simulation, if the variant choice associated with the block
evaluates to `true`, all the components that are connected to this
port become active. If the variant choice associated with the block evaluates to
`false`, all the components connected to this port become
inactive.

By default, this port is untyped. You define the type of this port by connecting
it to a conserving port of another block, components in the network, or a Simscape Bus port.

### **Port\_2** — Connection port untyped conserving port

Conserving connection port. By default, this port is untyped.

You define the type of the port by connecting it to a conserving port of another
block, components in the network, or a Simscape Bus port.

## Parameters

### **Connector Type** — Type of connector block `Leaf` (default) | `Primary` | `Nonprimary`

Select a connector type based on the components to deactivate.

- `Leaf`: If you want to deactivate all the components
  connected to the block, set **Connector Type** to
  `Leaf`.

  For example, in this model, the variant condition associated with the Variant
  Connector block, ConneBlk1, is `A == 1`. The variant condition
  associated with the Variant Connector block, ConneBlk2, is `B ==
  1`. During simulation, when `A == 1` evaluates to
  `true` and `B == 1` evaluates to
  `false`, all the components connected to ConneBlk1 block become
  active, and all the components connected to ConneBlk2 block become
  inactive.

  Deactivate all the components connected to the Leaf type of Variant Connector block
- `Primary and Nonprimary`: If you want to restrict the
  propagation of the variant condition to a set of components, create a Bounded region by using primary and nonprimary connector blocks. To
  form a bounded region, the primary and nonprimary connector blocks must have the
  same **Connector Tag** property.

  When you set **Connector Type** to
  `Primary` or `Nonprimary`, the
  connector tag of the block is displayed on the block icon. The connector tag of
  the primary connector block is displayed with double lines and the connector tag
  of the nonprimary connector block is displayed with single lines.

  A primary Variant Connector block and all nonprimary
  Variant Connector blocks with the same **Connector
  Tag** as the primary block constitute a set of related blocks.

  You can select a primary or nonprimary Variant Connector block
  to highlight all related Variant Connector blocks.

  The blocks that are highlighted in the model canvas are also highlighted in
  the miniature map.

  To show a related block in an open diagram, pause on the ellipsis that appears
  after selection. Then, select **Related Blocks**
  Related Blocks button. from the action bar. When multiple blocks
  correspond to the selected block, a list of related blocks opens. You can filter
  the list of related blocks by entering a search term in the text box. After you
  select a related block from the list, window focus goes to the open diagram or new
  tab that shows the related block.

Block icon for different types of Variant Connector block

### **Connector Tag** — Unique identifier of bounded region `A` (default) | valid MATLAB® identifier that starts with a letter, contains no spaces or special characters and is at most 2048 characters long

Specify an identifier in the **Connector Tag** parameter. The
primary and nonprimary connector blocks with the same tag form a Bounded region.

#### Dependencies

To enable this parameter, set **Connector Type** to
`Primary` or `Nonprimary`.

### **Variant control expression** — Variant controls available in global workspace `true` (default) | boolean condition expression

Displays the variant controls available in the global workspace. The variant control
can be a Boolean condition expression containing a regular MATLAB variable or a `Simulink.VariantExpression` object representing a Boolean condition
expression.

To edit a variant name, double-click a **Variant control
expression** cell and type in the variant control expression. Click
**Apply** after you edit a variant control name.

When the variant control associated with the block evaluates to
`true`, all the components connected to the block become
active.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControls` |
| **Type:** cell array of character vectors |
| **Value:** Variant control that is associated with the Variant choice |
| **Default:** `'Variant'` |

### **Condition (read-only)** — Condition for Variant controls no default

This read-only field is based on the condition for the associated Variant control in
the global workspace. Create or change a Variant condition in the
`Simulink.VariantExpression` parameter dialog box or in the global
workspace.

For more information, `Simulink.VariantExpression`.

### **Show variant condition on block** — Display variant condition on block icon off (default) | on

Select **Show variant condition on block** to display the variant
condition associated with the block on the block icon.

### **Open block in Variant Manager** — Open Variant Manager window no default

Click **Open block in Variant Manager** to open the Variant
Manager.

## Libraries

Simscape / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

The code is generated only for active blocks in the model. Inactive blocks do not
participate in code generation.

## Version History

**Introduced in R2020b**

## Description

Remove or disconnect physical components from network

The Variant Connector block lets you define variant choices
in a physical network. Variant choices allow you to exclude some components from simulation
without physically removing the components from the physical network. The components to be
disconnected must be connected to the port associated with condition data. During simulation,
the variant condition is propagated to all the connected components within the physical
network. If the variant control associated with the block evaluates to
`true`, all the components that are connected to the block become active. If
the variant control evaluates to `false`, all the components connected to the
block become inactive.
