---
type: simulink-block
title: 'Cannon'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'cannon'
documentation_source_path: 'supportpkg/parrot_ref/cannon.html'
language: en
---

# Cannon

## Ports

### Input

### **Port\_1** — Input signal to control the Cannon module `1` | `0`

The Cannon module fires one ball whenever the input changes from
`0` to `1`.

If there are multiple input commands to the Cannon block (to fire the
balls in succession), the commands are queued and they are executed one
after the other.

**Tip**

You can also use multiple Cannon blocks in the same Simulink
model (instead of queuing the commands in one Cannon block) to
fire the balls in succession.

**Data Types:** `Boolean`
### Output

### **Port\_1** — Number of firing commands pending in the queue scalar integer | `-1`

The number of firing commands that are pending in the queue while the
Cannon module is busy.

An output value of `-1` indicates that the Cannon
module is not connected to the drone, or the Cannon module is not
working.

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

Control the Cannon module connected to a Parrot Mambo minidrone

The Cannon block controls the Cannon module that is connected to a Parrot® Mambo minidrone.
