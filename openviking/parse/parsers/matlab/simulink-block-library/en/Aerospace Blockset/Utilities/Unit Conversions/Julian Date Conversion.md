---
type: simulink-block
title: 'Julian Date Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'juliandateconversion'
documentation_source_path: 'juliandateconversion.html'
language: en
---

# Julian Date Conversion

## Ports

### Input

### **day** — Clock source scalar | array

Clock source for model simulation, specified as a scalar or
array.

#### Dependencies

The presence and label of this port depends on the **Time
increment** parameter.

| Port | Time increment Setting |
| --- | --- |
| day | `Day` |
| hour | `Hour` |
| min | `Min` |
| sec | `Sec` |
| No inport port | `None` |

**Data Types:** `double`
### Output

### **JD** — Julian date scalar | array

Julian date, returned as a scalar or array.

#### Dependencies

**Data Types:** `double`

## Parameters

### **Year** — Year `2013` (default) | double, whole number, greater than 1

Year, specified as a scalar, to calculate the Julian date.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `year` |
| **Type**: character vector |
| **Values**: double, greater than 1 |
| **Default**: `'2013'` |

### **Month** — Month `January` (default) | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

Month to calculate the Julian date. From the list, select the month from
`January` to
`December`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `month` |
| **Type**: character vector |
| **Values**: `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **Default**: `'January'` |

### **Day** — Day `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

Day to calculate the Julian date. From the list, select the day from
`1` to `31`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `day` |
| **Type**: character vector |
| **Values**: `'1'` | `'2'` | `'3'` | `'4'` | `'5'` | `'5'` | `'6'` | `'7'` | `'8'` | `'9'` | `'10'` | `'11'` | `'12'` | `'13'` | `'14'` | `'15'` | `'16'` | `'17'` | `'18'` | `'19'` | `'20'` | `'21'` | `'22'` | `'23'` | `'24'` | `'25'` | `'26'` | `'27'` | `'28'` | `'29'` | `'30'` | `'31'` |
| **Default**: `'1'` |

### **Hour** — Hour `0` (default) | double, whole number, `0` to `24`

Hour used to calculate the Julian date. Enter a value from
`0` to `24`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `hour` |
| **Type**: character vector |
| **Values**: double, whole number, `0` to `24` |
| **Default**: `'0'` |

### **Minutes** — Minutes `0` (default) | double, whole number, `0` to `60`

Minutes to calculate the Julian date. Enter a number from
`0` to `60`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `min` |
| **Type**: character vector |
| **Values**: double, whole number, `0` to `60` |
| **Default**: `'0'` |

### **Seconds** — Seconds `0` (default) | double, whole number, `0` to `60`

Specify the seconds used to calculate the Julian date. Enter a number from
`0` to `60`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `sec` |
| **Type**: character vector |
| **Values**: double, whole number, `0` to `60` |
| **Default**: `'0'` |

### **Calculate modified Julian date** — Modified Julian data `off` (default) | `on`

Select this check box to calculate the modified Julian date (MJD) for
corresponding elements of the year, month, day, hour, minute, and
second.

#### Dependencies

Selecting this check box changes the output port label to MJD.
Clearing this check box changes the output port label to JD.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `modflag` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Time increment** — Time increment `Day` (default) | `Hour` | `Min` | `Sec` | `None`

Time increment between the specified date and the desired model simulation
time. The block adjusts the calculated Julian date to take into account the
time increment from model simulation. For example, selecting
`Day` and connecting a simulation timer to the port
means that each time increment unit is one day and the block adjusts its
calculation based on that simulation time.

If you select `None`, the calculated Julian date does not
take into account the model simulation time. Selecting this option removes
the first block input.

#### Dependencies

This parameter controls the presence and label of output port.

| Time increment Setting | Port |
| --- | --- |
| `Day` | day |
| `Hour` | hour |
| `Min` | min |
| `Sec` | sec |
| `None` | No inport port |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `deltaT` |
| **Type**: character vector |
| **Values**: `'Day'` | `'Hour'` | `'Min'` | `'Sec'` | `'None'` |
| **Default**: `'Day'` |

### **Action for out-of-range input** — Out-of-range block behavior `None` (default) | `Warning` | `Error`

Out-of-range block behavior, specified as follows.

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` (default) | Error in the Diagnostic Viewer, model simulation stops. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `errorflag` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Error'` |

## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Calculate Julian date or modified Julian date

The Julian Date Conversion block converts the specified date to the Julian
date or modified Julian date.
