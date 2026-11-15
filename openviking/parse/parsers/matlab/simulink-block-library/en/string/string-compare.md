---
type: simulink-block
title: 'String Compare'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringcompare'
language: en
---

# String Compare

## Ports

### Input

### **Port\_1** — First string to compare scalar

First string to compare, specified as a scalar.

**Data Types:** `string`

### **Port\_2** — Second string to compare scalar

Second string to compare, specified as a scalar.

**Data Types:** `string`
### Output

### **Port\_1** — True or false result scalar

True or false result, specified as a scalar:

- `1` — Match.
- `0` — No match.

**Data Types:** `Boolean`

## Parameters

### **Case sensitive** — Case sensitivity for string comparison on (default) | off

Case sensitivity for string comparison:

on
:   Consider string case when comparing strings.

off
:   Do not consider string case when comparing strings.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CaseSensitive` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Compare Option** — Amount of characters to compare `Entire string` (default) | `First N characters`

Amount of string to compare:

- `Entire string` — Compare both entire
  strings.
- `First N characters` — Compare the first
  *`N`* characters of both strings.

#### Dependencies

Setting this parameter to `First N
characters` enables the **Number of
characters** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CompareOption` |
| **Type:** character vector |
| **Values:** `'Entire string'` | `'First N characters'` |
| **Default:** `'Entire string'` |

### **Number of characters** — Number of characters to compare `1` (default) | scalar

Number of characters to compare

#### Dependencies

This parameter is enabled when the **Compare Option**
parameter is set to `First N
characters`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CompareOption` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'1'` |

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

**Introduced in R2018a**

## Description

Compare two input strings

String Compare compares two strings. To see if two strings are
identical, use this block. You can specify if the match is case sensitive and how much
of the string to compare.
