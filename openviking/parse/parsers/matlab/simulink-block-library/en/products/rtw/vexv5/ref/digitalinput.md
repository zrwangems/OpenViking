---
type: simulink-block
title: 'Digital Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'digitalinput'
documentation_source_path: 'vexv5/ref/digitalinput.html'
language: en
---

# Digital Input

## Ports

### Output

### **Port\_1** — Logical value read from the 3-wire port 0 | 1

Logical value read from the 3-wire port, returned as a boolean value.

**Data Types:** `Boolean`

## Parameters

### **3-Wire Expander (smart port)** — Select the smart port that is used by 3-Wire Expander `None` (default) | `1` to `21`

If you are using a 3-Wire Expander, specify the smart port on VEX EDR V5 Robot Brain to which the expander is connected.

### **Port** — Select the 3-wire port to read the logical value A (default) | `A` to `H`

Select the 3-wire port on the VEX EDR V5 Robot Brain from which you want to read the digital signal.

Do not assign the same port to more than one Digital Input block
within the same model.

### **Sample time** — Sample time for obtaining the value from the 3-wire port `0.2` (default) | seconds

Specify how often the block should read the values from the 3-wire port.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read logical values from the 3-wire port on VEX EDR V5 Robot Brain

The Digital Input block reads the logical value from the selected 3-wire port on
VEX® EDR V5 Robot Brain. You can use up to eight 3-wire ports on the VEX EDR V5 Robot Brain to read logical values.
