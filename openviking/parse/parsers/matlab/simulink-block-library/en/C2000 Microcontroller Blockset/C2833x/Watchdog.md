---
type: simulink-block
title: 'C28x Watchdog'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'watchdog'
documentation_source_path: 'ref/watchdog.html'
language: en
---

# C28x Watchdog

## Ports

### Input

### **Input** — Resets watchdog counter scalar

When the input signal is `1`, the counter is
reset.

#### Dependencies

This parameter appears only when **Watchdog counter reset
source** is set to `Input
port`.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## Parameters

### **Watchdog counter reset source** — Watchdog counter reset source `Specify via dialog` (default) | `Input port`

The watchdog counter reset source.

- `Input` — Create an input port on the
  watchdog block. When the input signal is `1`, the
  counter is reset.
- `Specify via dialog` — The watchdog timer
  is reset based on the **Sample time** value.

### **Sample time** — Frequency at which processor resets Watchdog timer `–1` (default) | scalar

Sample time for the block in seconds. To execute this block
asynchronously, set this parameter to `-1`.

#### Dependencies

This parameter appears only when **Watchdog counter reset
source** is set to `Specify via
dialog`.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Configure counter reset source of processor watchdog module

This block configures the counter reset source of the watchdog module on the
processor. The watchdog module, after configuration, resets the system if not serviced
periodically.
