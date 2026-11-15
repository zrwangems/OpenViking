---
type: simulink-block
title: '5x5 LED Matrix'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / LED'
documentation_page: '5x5ledmatrix'
documentation_source_path: 'microbit/ref/5x5ledmatrix.html'
language: en
---

# 5x5 LED Matrix

## Ports

### Input

### **Matrix** — Input signal matrix

The port accepts a 5x5 matrix with all the elements as either
`0` or `1`. When the element value
is greater than 0, the corresponding LED turns on. Otherwise, it turns
off.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

## Parameters

Not documented in R2025b.

## Libraries

Simulink Coder Support Package for BBC micro:bit/ LED

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Output 5x5 LED image on board

The 5x5 LED Matrix block outputs a 5x5 LED image on a built-in 5x5 LED
matrix on the board. The block has one input port, Matrix. The Matrix port accepts a 5x5
matrix with all the elements as either `0` or
`1`.

### Use the 5x5 LED Matrix

The BBC micro:bit uses x, y coordinates to identify a particular LED in the 5x5
matrix. The coordinates start from `0` from the top-left corner of
the matrix.

Place the board horizontally on a table with the LEDs facing upwards. The
horizontal line represents the x-coordinates and the vertical line represent the
y-coordinates.

Suppose that you are sending a matrix with values `[1 0 0 0 1;0 1 0 1 0;0
0 1 0 0;0 1 0 1 0;1 0 0 0 1]` as an input to the block. All the LEDs
corresponding to elements with value `1` turn on.
