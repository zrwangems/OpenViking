---
type: simulink-block
title: 'Grabber'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'grabber'
documentation_source_path: 'supportpkg/parrot_ref/grabber.html'
language: en
---

# Grabber

## Ports

### Input

### **Port\_1** — Input signal to control the Grabber module `1` | `0`

The grabber closes (to grab the object) if the input is
`1`, and it opens (to place the object in position)
if the input is `0`.

**Note**

The change of value of the input signal (`0` to
`1` or `1` to
`0` results in an immediate action by the
Grabber. For example, the grabber closes immediately if the input
signal becomes `1` even though an opening action is
in progress due to a previous input signal of value
`0`.

**Data Types:** `Boolean`
### Output

### **Port\_1** — Current state of the grabber module `0` | `1` | `-1`

The block outputs one of these three values that correspond to the
current state of the Grabber module:

- `1` – Grabber is closed
- `0` – Grabber is opened
- `-1` – Grabber is not connected to the
  drone or it is not working

**Data Types:** `uint8`

## Parameters

Not documented in R2025b.

## Libraries

Simulink Support Package for Parrot Minidrones

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Control the Grabber module connected to a Parrot Mambo minidrone

The Grabber block controls the Grabber module that is connected to a Parrot® Mambo minidrone.
