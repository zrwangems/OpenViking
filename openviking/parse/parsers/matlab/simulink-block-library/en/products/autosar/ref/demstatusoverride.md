---
type: simulink-block
title: 'Dem Status Override'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'demstatusoverride'
documentation_source_path: 'ref/demstatusoverride.html'
language: en
---

# Dem Status Override

## Ports

Not documented in R2025b.

## Parameters

### **EventID** — Specify the event 0 (default) | integer

Specify the AUTOSAR event that you want to override by using this block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EventId` |
| **Type:** integer |
| **Values:** 0 | integer |
| **Default:** `0` |

### **Test Failed** — Indicates the result of the most recently performed test `Clear` (default) | `Set`

Test failed the last time it was checked.

To set this property, select `Dialog` to manually configure
the status or `Input port` to have the status configured
dynamically in response to the behavior of a connected input.

### **Test Failed this Operation Cycle** — Indicates whether a diagnostic test has reported a failure during the current operation cycle `Clear` (default) | `Set`

Test failed during the current operation cycle.

To set this property, select `Dialog` to manually configure
the status or `Input port` to have the status configured
dynamically in response to the behavior of a connected input.

### **Pending DTC** — Indicates whether a diagnostic test has reported a failure during the current or last completed operation cycle `Clear` (default) | `Set`

Test failed during the current or previous operation cycle.

To set this property, select `Dialog` to manually configure
the status or `Input port` to have the status configured
dynamically in response to the behavior of a connected input.

### **Confirmed DTC** — Indicates whether a malfunction was detected enough times to warrant that the DTC should be stored in long-term memory `Clear` (default) | `Set`

Test failure confirmed at the time of the request.

To set this property, select `Dialog` to manually configure
the status or `Input port` to have the status configured
dynamically in response to the behavior of a connected input.

### **Test Not Completed Since Last Clear** — Indicates whether a test has run and completed since the last time a call was made to `ClearDiagnosticInformation` `Clear` (default) | `Set`

Test not performed since the last code clear.

To set this property, select `Dialog` to manually configure
the status or `Input port` to have the status configured
dynamically in response to the behavior of a connected input.

### **Test Failed Since Last Clear** — Indicates whether a test has failed since the last time a call was made to `ClearDiagnosticInformation` `Clear` (default) | `Set`

Test failed at least once since last code clear.

To set this property, select `Dialog` to manually configure
the status or `Input port` to have the status configured
dynamically in response to the behavior of a connected input.

### **Test Not Completed This Operation Cycle** — Test not performed during the current operation cycle `Clear` (default) | `Set`

Test not completed during this operation cycle.

To set this property, select `Dialog` to manually configure
the status or `Input port` to have the status configured
dynamically in response to the behavior of a connected input.

### **Warning Indicator Requested** — Indicates the status of any warning indicators associated with a particular DTC `Clear` (default) | `Set`

Test failure so severe that it alerts the server.

To set this property, select `Dialog` to manually configure
the status or `Input port` to have the status configured
dynamically in response to the behavior of a connected input.

## Libraries

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Override an event to simulate and verify behavior

The Dem Status Override block can be configured to set the diagnostic
status for an AUTOSAR event simulated in the Diagnostic Service Component block. This status
value can be configured according to the Unified Diagnostic Services (UDS) standard.
Specifically, you can use this block to set the return value of
`GetEventStatus` calls for a specific event regardless of the behavior of
the other events in the model. Other blocks that attempt to modify the event status during
simulation are ignored. This block allows a predictable entry-point for testing specific
behavior that you can use as a low-cost method to quickly gain coverage of a component
model.
