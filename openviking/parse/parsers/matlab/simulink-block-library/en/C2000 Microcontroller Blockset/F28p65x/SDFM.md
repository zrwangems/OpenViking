---
type: simulink-block
title: 'F2807x/F2837xD/F2837xS/F28004x/F28003x/F2838x/F28p65x SDFM'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F28003x'
documentation_page: 'f2807xf2837xdf2837xsf28004xf28003xf2838xf28p65xsdfm'
documentation_source_path: 'ref/f2807xf2837xdf2837xsf28004xf28003xf2838xf28p65xsdfm.html'
language: en
---

# F2807x/F2837xD/F2837xS/F28004x/F28003x/F2838x/F28p65x SDFM

## Ports

### Output

### **DFSTS** — Data filter status `0` | `1` | `-1`

Status of the data filter returned as one of the following:

- 0 - Data filter not ready
- 1 - Data filter ready
- -1 - Modulator clock failure

### **DFLTX** — Data filter `scalar`

The primary filter data output. It is represented in either a 32-bit or a 16-bit
format.

**DFLTX** - x represents the filter channel.

### **CFSTS** — Comparator Status `0` | `1` | `2` | `3` | `4` | `5` | `-1`

The comparator status value differs for different processors.

**The comparator status value**

| Comp Status Values | F2837x/07 | F28004x | F2838x/003x/P65x |
| --- | --- | --- | --- |
| 0 | No comparator event occurred | No comparator event occurred | No comparator event occurred |
| 1 | Lower threshold event (LLT) | Lower threshold event (LLT)  No HLTZ | Comparator event 1 (CEVT1).  No HLTZ |
| 2 | Higher threshold event (HLT) | Higher threshold event (HLT)  No HLTZ | Comparator event 2 (CEVT2).  No HLTZ |
| 3 | NA | HLTZ. No HLT and no LLT | HLTZ. No CEVT1 and no CEVT2 |
| 4 | NA | HLTZ and LLT | CEVT1 and HLTZ |
| 5 | NA | HLTZ and HLT | CEVT2 and HLTZ |
| -1 | Modulator clock failure | Modulator clock failure | Modulator clock failure |

#### Dependencies

To enable this port, select the **Enable comparator filter
output** parameter.

### **CFLTX** — Comparator filter `scalar`

The secondary data filter output. **CFLTX** - x represents the
filter channel.

This comparator filter is available only for specific processors.

#### Dependencies

To enable this port, select the **Enable comparator filter
output** parameter.

## Parameters

### **SDFM module** — Indicates which register to use `1` (default) | `2`

Select the SDFM register that should be configured to output the result.

**Note**

The F28004x processor has only one SDFM module.

### **Filter channel** — Select filter module `Filter1` (default) | `Filter2` | `Filter3` | `Filter4`

Each filter channel consists of an input control unit, a data filter unit, and a
comparator filter unit. Each of these filter modules can be independently configured.
The SDFM module consists of four primary filters and four secondary filters.

### **Data representation** — Source of internal DAC `16-bit` (default) | `32-bit`

The data filter output can be represented in either 32-bit or 16-bit format.

By default, the data filter output is represented in a 16-bit format. When the
output is represented in a 16-bit format, required shifts are handled
internally.

### **Sample time** — Frequency at which data is read `0.1` (default)

Use this parameter to specify the time interval between samples. To inherit sample
time from an upstream block, set this parameter to `-1`.

### **Enable comparator filter output** — Enables comparator output ports `off` (default) | `on`

Select this option to enable the comparator status (CFSTS) and comparator filter
(CFLTX) output ports.

## Libraries

C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Configure filter channel for SDFM Module

The sigma delta filter module (SDFM) is a four-channel digital filter designed
specifically for current measurement and resolver position decoding in motor control
applications. Each input channel can receive an independent delta-sigma (ΔΣ) modulator bit
stream. The bit streams are processed by four individually-programmable digital decimation
filters.

The filter set includes a fast comparator (secondary filter) for immediate digital
threshold comparisons for over-current and under-current monitoring and a primary data
filter.

Each SDFM module consists of:

- Four independent configurable primary filter (data filter) units.
- Four independent, configurable secondary filter (comparator) units.
- Eight external pins (four sigma-delta data input pins and four sigma-delta clock
  input pins).
- Four different configurable modulator clock modes.

For more information on configuring filter channels, refer to SDFM Configuration
Parameters.
