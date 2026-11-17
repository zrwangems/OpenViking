---
type: simulink-block
title: 'C2802x/C2803x/C2806x/F28M3x AnalogIO Output'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c2802xc2803xc2806xf28m3xanalogiooutput'
documentation_source_path: 'ref/c2802xc2803xc2806xf28m3xanalogiooutput.html'
language: en
---

# C2802x/C2803x/C2806x/F28M3x AnalogIO Output

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Parameters (Output Pins)**
:   Select the analog output pins. Selecting **Toggle**
    inverts the output voltage levels of the pins if the input of the block
    is True.

**Parameters (Output Pins)**
:   Select the analog output pins. Selecting **Toggle**
    inverts the output voltage levels of the pins if the input of the block
    is True.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Configure Analog IO to output analog signals on specific pins

# C2802x/C2803x/C2806x/F28M3x AnalogIO Output

Configure Analog IO to output analog signals on specific pins

Use this block to drive the output voltage of Analog IO pins.

In regular mode, a value of True at the input of the block pulls the Analog IO pin
high while a value of False grounds the pin.

In toggle mode, a value of True at the input of the block switches the actual
output level of the Analog IO pin while a value of False does not alter the output
level of the Analog IO pin.

- C2802x/C2803x/C2806x/F28M3x AnalogIO Output block
