---
type: simulink-block
title: 'Digital Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'digitalread'
documentation_source_path: 'beagleboneblue/ref/digitalread.html'
language: en
---

# Digital Read

## Ports

### Output

### **Port\_1** — Output signal scalar

The port outputs the logical state of the digital pin on the board that you
specify in the **Pin** parameter.

**Data Types:** `Boolean`

## Parameters

### **Pin** — Pin number of the digital input GPIO1\_17 (default) | GPIO1\_25 | GPIO3\_1 | GPIO3\_2 | GPIO3\_17 | GPIO3\_20

Specify the digital pin number.

To see the pin mapping table, click **View pin map**.

Each block must have a unique pin number within a model.

### **Sample time** — Frequency at which the block reads the input pin value `0.1` (default)

Specify in seconds how often this block reads the pin value.

When you specify this parameter as`-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read logical state of digital input pin

The Digital Read block outputs the logical state of a specified digital pin
on the board.

During the external mode simulation, the block outputs the simulation results returned
from the executable running on the target hardware.

During simulation in all other modes, the block outputs zeroes.
