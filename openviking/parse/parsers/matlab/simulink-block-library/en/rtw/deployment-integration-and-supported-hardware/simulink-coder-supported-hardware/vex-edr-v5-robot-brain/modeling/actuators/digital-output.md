---
type: simulink-block
title: 'Digital Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Actuators'
documentation_page: 'digitaloutput'
documentation_source_path: 'vexv5/ref/digitaloutput.html'
language: en
---

# Digital Output

## Ports

### Input

### **Port\_1** — Sets logical value (1 or 0) of pin `1` | `0`

Connect the input port to a block that generates a logical value
(`1` or `0`).

**Data Types:** `Boolean`

## Parameters

### **3-Wire Expander (smart port)** — Select the smart port that is used by 3-Wire Expander `None` (default) | `1` to `21`

If you are using a 3-Wire Expander, specify the smart port on VEX EDR V5 Robot Brain to which the expander is connected.

### **Port** — Select the 3-wire port to which you want to send the digital signal `A` (default) | `A` to `H`

Select the 3-wire port on the VEX EDR V5 Robot Brain to which you want to send the digital signal.

Do not assign the same port to more than one Digital Output block
within the same model.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Set logical value to the 3-wire port on VEX EDR V5 Robot Brain

The Digital Output block is used to set the digital/logical value (1 or 0)
to the selected 3-wire port on a VEX® EDR V5 Robot Brain.
