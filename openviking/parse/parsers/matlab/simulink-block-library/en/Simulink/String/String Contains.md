---
type: simulink-block
title: 'String Contains'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringcontains'
documentation_source_path: 'slref/stringcontains.html'
language: en
---

# String Contains

## Ports
```yaml
ports:
- name: str
  summary: String to search scalar
  direction: input
  data_types: string
- name: sub
  summary: String pattern to search for scalar
  direction: input
  data_types: string
- name: T/F
  summary: String pattern detected 1 | 0
  direction: output
  data_types: Boolean
```

### Input

### **str** — String to search scalar

String to search for the pattern in, specified as a scalar.

**Data Types:** `string`

### **sub** — String pattern to search for scalar

String pattern to search for in string, specified as a scalar.

**Data Types:** `string`
### Output

### **T/F** — String pattern detected `1` | `0`

Whether the string pattern was detected, returned as detected
(`1`) or not detected (`0`).

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Case sensitive
  summary: Case sensitivity on (default) | off
  group: ''
  block_parameter: CaseSensitive
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Function
  summary: Pattern search function Contains | Starts with | Ends with
  group: ''
  block_parameter: Function
  type: character vector
  values: '''Contains'' | ''Starts with'' | ''Ends with'''
  default: '''Contains'' for String Contains block, ''Starts with'' for String Starts With block, ''Ends with'' for String
    Ends With block'
```

### **Case sensitive** — Case sensitivity on (default) | off

Case sensitivity for the pattern detection:

on
:   Consider string case when searching for the pattern.

off
:   Do not consider string case when searching for the pattern.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CaseSensitive` |
| **Type**: character vector |
| **Values:** `'on'` | `'off'` |
| **Default**: `'on'` |

### **Function** — Pattern search function `Contains` | `Starts with` | `Ends with`

Pattern search function, specified as:

- `Contains`

  Search for the pattern anywhere in the string. This is the default for the
  String Contains block.
- `Starts with`

  Search for the pattern only at the beginning of the string. This is the default
  for the String Starts With block.
- `Ends with`

  Search for the pattern only at the end of the string. This is the default for
  the String Ends With block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Function` |
| **Type**: character vector |
| **Values:** `'Contains'` | `'Starts with'` | `'Ends with'` |
| **Default**: `'Contains'` for String Contains block, `'Starts with'` for String Starts With block, `'Ends with'` for String Ends With block |
## Libraries

Simulink / String

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Determine if string contains, starts with, or ends with pattern

The String Contains, String Starts With, and String
Ends With blocks determine if a string (**str**) contains, starts
with, or ends with a pattern (**sub**).

The String Contains, String Starts With, and String
Ends With blocks are identical. When **Function** is set to
`Contains`, the block determines if the string contains a specified
pattern. When **Function** is set to `Starts with`,
the block determines if the string starts with a specified pattern. When
**Function** is set to `Ends with`, the block
determines if the string ends with a specified pattern.
