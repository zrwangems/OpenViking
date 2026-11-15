---
type: simulink-block
title: 'Data Input'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / User Interface'
documentation_page: 'datainput'
documentation_source_path: 'supportpkg/android_ref/datainput.html'
language: en
---

# Data Input

## Ports

### Output

### **Port\_1** — Value entered in data input field `1.0` (default) | vector

The block outputs the value that you enter in the data input field by
typing on the device keyboard.

**Data Types:** `uint8` | `int8` | `uint16` | `int16` | `uint32` | `int32` | `single` | `double`

## Parameters

### **Character vector input** — Option to specify if the input data is a character vector data off (default)

Select this option to enable entry of character vector data in the data
input field.

- When you select the **Character vector
  input** option, the layout of the keyboard on your
  Android device changes
  to QWERTY. The data input field accepts any value supported by
  the QWERTY keyboard.

  The block outputs a 1-by-*N* vector with
  `uint8` values that corresponds to the
  ASCII values of the characters entered in the data input field.
  *N* is the length specified in the
  **Number of characters** parameter.
- When you clear the **Character vector input**
  option, the layout of the keyboard remains numeric. The data
  input field accepts only those values that are aligned to the
  type specified in the **Data type**
  parameter.

  | When Input Is a Character Vector | When Input Is Numeric |
  | --- | --- |
  |  |  |

### **Initial value** — Default value of data input field `0.1` (default) | any valid value of the current data type

- For numeric input, the block converts the initial value to the
  type specified in the **Data type** parameter,
  and then displays it on the data input field. For example, if
  **Initial value** is specified as
  `1` and the **Data type**
  parameter is set to `double`, the value
  displayed in the data input field is
  `1.0000000000000`.
- For character vector input, ensure that the length of the
  character vector in the **Initial value**
  parameter does not exceed the value specified in the
  **Number of characters** parameter.

### **Number of characters** — Maximum length of character vector `100` (default) | any positive integer less than 256

Specify the maximum number of characters that can be entered in the data
input field. The data input field does not accept any input beyond the
length specified in the **Number of characters**
parameter.

If the number of characters in the character vector is less than the
length specified in the **Number of characters** parameter,
the block fills the empty spaces in the output array with zeros.

This table shows the block output when the length of the character vector
entered in the data input field is less than, equal to, or greater than the
length specified in the **Number of characters** parameter,
using the text `Hello` as an example.

| Length of Data in Data Input Field < Number of Characters | Length of Data in Data Input Field = Number of Characters | Length of Data in Data Input Field > Number of Characters |
| --- | --- | --- |
| **Number of Characters** = `8` | **Number of Characters** = `5` | **Number of Characters** = `2` |
|  |  |  |

#### Dependencies

The **Number of characters** parameter appears when
you select the **Character vector input**
option.

### **Data type** — Data type of entered data `double` (default) | `uint8` | `int8` | `uint16` | `int16` | `uint32` | `int32` | `single`

Specify the type of the data entered in data input field. The data input
field accepts input only within the range specified in the **Data
type** parameter. For example, if you set **Data
type** to `int8`, the data input field does
not accept any value beyond the range of −128 to 127.

**Note**

You may observe that the floating-point computation of a
`single` or a `double` data
entered in the data input field is not as precise as you had expected.
Conforming to the IEEE standard 754, Simulink® represent numbers to finite precision. For more
information on computation of floating-point data, see Floating-Point Numbers.

#### Dependencies

The **Data type** parameter appears when you clear
the **Character vector input** option.

### **Sample time** — How often the block reads data `0.1` (default) | `-1` | any positive integer

Specify how often the block reads data from the data input field, measured
in seconds. When you specify this parameter as `-1`,
Simulink determines the best sample time for the block based on the
block context within the model.

## Libraries

Simulink Support Package for Android Devices / User Interface

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Generate data input field on device screen

The Data Input block generates a data input field on the Android™ device screen. The data input field is an edit box
to enter or modify data by typing on the device keyboard. The **Data
Type** parameter in the Block Parameters dialog box specifies the type of
data that can be entered in the data input field.

The block outputs the value that you enter in the data input field. For a character
vector input, the block outputs the corresponding ASCII values.

**Note**

During simulation without hardware, this block outputs zeros. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
