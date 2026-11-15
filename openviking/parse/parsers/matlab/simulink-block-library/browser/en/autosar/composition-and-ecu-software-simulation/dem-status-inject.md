---
type: simulink-block
title: 'Dem Status Inject'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'demstatusinject'
documentation_source_path: 'ref/demstatusinject.html'
language: en
---

# Dem Status Inject

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

### **Fault type** — Specify the type of fault `Event Fail` (default) | `Event Pass` | `Operation Cycle Start` | `Operation Cycle End` | `Fault Record Overwritten` | `Fault Maturation` | `Clear Diagnostic` | `Aging` | `Healing` | `Indicator Conditions Met`

Specify the type of diagnostic event that you want to inject into the system.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FaultType` |
| **Type:** character vector |
| **Values:** `'Event Fail' | 'Event Pass' | 'Operation Cycle Start' | 'Operation Cycle End' | 'Fault Record Overwritten' | 'Fault Maturation' | 'Clear Diagnostic' | 'Aging' | 'Healing' | 'Indicator Conditions Met'` |
| **Default:** `'Event Fail'` |

### **Trigger type** — Specify the inject condition `rising` (default) | `falling` | `either` | `function-call`

Specify when to inject the diagnostic event into the system.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InjectTriggerType` |
| **Type:** character vector |
| **Values:** `'rising' | 'falling' | 'either' | 'function-call'` |
| **Default:** `'rising'` |

### **Test Failed** — Indicates the result of the most recently performed test `Clear` (default) | `Set`

Test failed the last time it was checked.

This read-only property is set by the **Fault type**.

### **Test Failed this Operation Cycle** — Indicates whether a diagnostic test has reported a failure during the current operation cycle `Clear` (default) | `Set`

Test failed during the current operation cycle.

This read-only property is set by the **Fault type**.

### **Pending DTC** — Indicates whether a diagnostic test has reported a failure during the current or last completed operation cycle `Clear` (default) | `Set`

Test failed during the current or previous operation cycle.

This read-only property is set by the **Fault type**.

### **Confirmed DTC** — Indicates whether a malfunction was detected enough times to warrant that the DTC should be stored in long-term memory `Clear` (default) | `Set`

Test failure confirmed at the time of the request.

This read-only property is set by the **Fault type**.

### **Test Not Complete Since Last Clear** — Indicates whether a test has run and completed since the last time a call was made to `ClearDiagnosticInformation` `Clear` (default) | `Set`

Test not performed since the last code clear.

This read-only property is set by the **Fault type**.

### **Test Failed Since Last Clear** — Indicates whether a test has failed since the last time a call was made to `ClearDiagnosticInformation` `Clear` (default) | `Set`

Test failed at least once since last code clear.

This read-only property is set by the **Fault type**.

### **Test Not Complete This Operation Cycle** — Test not performed during the current operation cycle `Clear` (default) | `Set`

Test not completed during this operation cycle.

This read-only property is set by the **Fault type**.

### **Warning Indicator Requested** — Indicates the status of any warning indicators associated with a particular DTC `Clear` (default) | `Set`

Test failure so severe that it alerts the server.

This read-only property is set by the **Fault type**.

## Libraries

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Inject an event failure to test recovery

The Dem Status Inject block can be configured to instantaneously set the
diagnostic status for an AUTOSAR event simulated in the Diagnostic Service
Component block. This status value can be configured according to the Unified
Diagnostic Services (UDS) standard. Specifically, you can use this block to inject a transient
failure into a system to test its ability to recover. This block simulates and responds to
other blocks affecting its status to show system recovery.
