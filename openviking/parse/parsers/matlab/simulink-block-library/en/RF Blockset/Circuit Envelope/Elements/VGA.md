---
type: simulink-block
title: 'VGA'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'vga'
documentation_source_path: 'ref/vga.html'
language: en
---

# VGA

## Ports

### Input

### **Gain** — Power gain signal scalar

Power gain signal, specified as a scalar in dB. The power gain signal
is a Simulink signal.

**Data Types:** `double`

### **IP2** — Second-order intercept point signal scalar

Second-order intercept point signal, specified as a scalar in dBm. The
second-order intercept point signal is a Simulink signal.

**Data Types:** `double`

### **IP3** — Third-order intercept point signal scalar

Third-order intercept point signal, specified as a scalar in dBm. The
third-order intercept point signal is a Simulink signal.

**Data Types:** `double`

## Parameters

### **Input impedance (Ohm)** — Input impedance of VGA `50` (default) | scalar

Input impedance of the VGA, specified as
a scalar in ohms.

### **Output impedance (Ohm)** — Output impedance of VGA `50` (default) | positive scalar

Output impedance of the VGA, specified as
a scalar in ohms.

### **Intercept points convention** — Input-referred or output-referred convention `Output` (default) | `Input`

Input-referred or output-referred convention for IP2 or IP3 intercept
points, specified as `Input` or
`Output`.

### **Ground and hide negative terminals** — Ground and hide negative terminals `on` (default) | `off`

Ground and hide negative terminals, specified as `on` or
`off`. Select this parameter to internally ground and
hide the negative terminals. Clear the option to expose the negative
terminals. By exposing these terminals, you can connect them to other parts
of your model.

## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Model variable gain amplifier

The VGA block models a RF Blockset™ variable gain amplifier (VGA). The Simulink® signal controls the non-linear gain.

The three Simulink input ports are `Gain`, `IP2`
(second-order intercept point), and `IP3` (third-order intercept
point). The port, `In` is the RF Blockset voltage input and the port
`OUT` is RF Blockset voltage output.
