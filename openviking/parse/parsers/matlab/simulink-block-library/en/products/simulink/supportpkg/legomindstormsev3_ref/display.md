---
type: simulink-block
title: 'Display'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'display'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/display.html'
language: en
---

# Display

## Ports

### Input

### **Data** — Data to display on EV3 display positive or negative integer, character array

The block inputs the inputs data to display on EV3.

**Data Types:** `int32`

## Parameters

### **Label** — Static label character

Enter a static label. The EV3 brick displays the prefix to the left of the input
value. The prefix cannot be longer than 8 characters. For example, to display the state
of the EVR Button, enter
`Button:`.

### **Row** — EV3 display row number `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

Select the EV3 display row number upon which to display the number. Row 1 indicates
the top while row 10 indicates the bottom of the EV3 display.

### **Format** — Display format `Decimal` (default) | `Hex`

Select format of the number to display on the EV3 brick.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Display label and integer on EV3 display

Use the Display block to display integer or label on a specific line of the
EV3 display.

During simulations without hardware, this block does nothing. See Block Produces Zeros or Does Nothing in Simulation.
