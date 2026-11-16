---
type: simulink-block
title: 'System Requirements'
family: 'slrequirements'
product_id: 'slrequirements'
product_name: 'Requirements Toolbox'
documentation_release: R2025b
official_category: 'Link Requirements / Create Requirement Links'
documentation_page: 'systemrequirements'
documentation_source_path: 'ref/systemrequirements.html'
language: en
---

# System Requirements

## Ports

Not documented in R2025b.

## Parameters

**Block Title**
:   The title of the system requirements list in the model. The default title
    is `System Requirements`. You can enter a customized title,
    for example, `Engine Requirements`.

## Libraries

Requirements Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

List system requirements in Simulink models

The System Requirements block lists the system-level requirements
associated with a model or subsystem. This block is dynamically populated. It displays
system requirements associated with the level of hierarchy in which the block appears in
the model. It does not list requirements associated with individual blocks in the model.
To list desired requirement links in the System Requirements block:

1. Right-click the background of your model.
2. Select
   **Requirements at This Level**.
3. From the top of the context menu, verify that
   all the requirements you want to list
   appear in the System Requirements block.

You can place this block anywhere in your model. It does not connect to other
Simulink® blocks. You can have only one System Requirements block in
a given subsystem.

When you insert this block into your Simulink model, it is populated with the system requirements.

A System Requirements block with one requirement

Each of the listed requirements is an active link to the requirements document. When
you double-click a requirement label, the associated requirements document opens in its
editor window, scrolled to the target location.
