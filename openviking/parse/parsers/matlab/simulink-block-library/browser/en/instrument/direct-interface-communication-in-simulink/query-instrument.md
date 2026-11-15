---
type: simulink-block
title: 'Query Instrument'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: 'Direct Interface Communication in Simulink'
documentation_page: 'queryinstrument'
documentation_source_path: 'queryinstrument.html'
language: en
---

# Query Instrument

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

### R2024b: Errors

This block throws an error when added to a model. Opening any existing model
with this block causes an error. The model cannot be simulated because of this
error. You can still open the block parameter dialog and see the parameter
values.

Use the interface-specific blocks instead:

- Serial
  Configuration
- Serial Receive
- Serial Send
- TCP/IP
  Receive
- TCP/IP Send
- UDP Receive
- UDP Send
- VISA

These interface-specific blocks all support additional properties
and have improved performance compared to Query Instrument and
To Instrument.

### R2023b: To be removed

The Query Instrument and To Instrument
Simulink blocks will be removed.

## Description

(To be removed) Query or read instrument data
