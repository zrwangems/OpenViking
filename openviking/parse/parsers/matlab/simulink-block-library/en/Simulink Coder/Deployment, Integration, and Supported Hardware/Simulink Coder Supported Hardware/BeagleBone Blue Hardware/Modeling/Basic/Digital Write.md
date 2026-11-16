---
type: simulink-block
title: 'Digital Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'digitalwrite'
documentation_source_path: 'beagleboneblue/ref/digitalwrite.html'
language: en
---

# Digital Write

## Ports

### Input

### **Port\_1** — Input signal scalar

The block sets this value to the digital output pin that you specify in the
**Pin** parameter.

**Data Types:** `Boolean`

## Parameters

### **Pin** — Pin number of the digital output GPIO1\_25 (default) | GPIO1\_17 | GPIO3\_1 | GPIO3\_2 | GPIO3\_17 | GPIO3\_20

Specify the digital pin number.

To open the pin mapping table, click **View pin map**.

Each block must have a unique pin number within a model.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Set the logical state of the digital output pin

The Digital Write block sets the logical state of the specified digital pin
on the board.

During the external mode simulation, the block sets the value to the pin that you specify
in the **Pin** parameter.

During simulation in all other modes, the block does nothing.
