---
type: simulink-block
title: 'LED Text Scroll'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / LED'
documentation_page: 'ledtextscroll'
documentation_source_path: 'microbit/ref/ledtextscroll.html'
language: en
---

# LED Text Scroll

## Ports

### Input

### **String** — Input text to be displayed vector

The port accepts data as an N-by-1 or 1-by-N array. The data can
include capital letters and the numerals 0-9. Any other character is
displayed as a minus sign on the micro:bit.
### Output

### **Out** — Output data matrix

The port outputs data as a 2-D, 5-by-5 vector array, which can be sent
to a 5x5 LED Matrix block. The 5x5 LED Matrix block can then take that
data and display the text on micro:bit.

## Parameters

### **Scroll speed (1–10)** — Scroll text speed `5` (default) | any integer from 1 to 10, inclusive

The speed at which you want the text to scroll. A higher number results in
a faster scroll speed.

## Libraries

Simulink Coder Support Package for BBC micro:bit/LED

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Create scrolling text for BBC micro:bit

The LED Text Scroll block creates scrolling text from an input string.
The scrolling text can then be sent as input to a 5x5 LED Matrix block. The 5x5 LED
Matrix block then displays the text on the micro:bit board.
