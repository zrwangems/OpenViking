---
type: simulink-block
title: 'Switch'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Junctions'
documentation_page: 'switch'
documentation_source_path: 'ref/switch.html'
language: en
---

# Switch

## Ports

### Input

### **Vctl** — Simulink control signal scalar

Simulink control signal, specified as a scalar.

**Data Types:** `double`

## Parameters

### **On resistance** — On resistance `10` (default) | positive scalar

On resistance value of the switch, specified as a positive scalar in
ohms.

### **Off resistance** — Off resistance `1e-6` (default) | positive scalar

Off resistance value of the switch, specified as a positive scalar in
ohms.

### **Threshold voltage** — Threshold voltage `0` (default) | scalar

Threshold voltage of the switch, specified as a scalar in volts.

## Libraries

RF Blockset / Circuit Envelope / Junctions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Simulink controlled two–terminal switch

The switch block models a two terminal switch. The input Simulink® signal, *Vctl*, controls the transfer of the RF Blockset™ signal from the `In` terminal to the
`Out` terminal.

If the control voltage is less than the threshold voltage, the block attenuates the
signal using the resistance value specified in **Off resistance**
between the input and output terminals. If the control voltage is greater than the
threshold voltage, the block passes the signal using the resistance value specified in
**On resistance** between the input and output terminals.
