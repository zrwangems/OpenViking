---
type: simulink-block
title: 'C281x GPIO Digital Input'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'c281xgpiodigitalinput'
documentation_source_path: 'ref/c281xgpiodigitalinput.html'
language: en
---

# C281x GPIO Digital Input

## Ports

Not documented in R2025b.

## Parameters

**IO Port**
:   Select the input/output port to use: `GPIOPA`,
    `GPIOPB`, `GPIOPD`,
    `GPIOPE`, `GPIOPF`, or
    `GPIOPG` and select the I/O Port bits to enable for digital
    input. (There is no GPIOPC port on the C281x.) If you
    select multiple bits, vector input is expected. Cleared bits are available for
    peripheral functionality. Multiple GPIO DI blocks cannot share the same I/O
    port.

    **Note**

    The input function of the digital I/O and the input path to the related
    peripheral are enabled on the board. If you configure a pin as digital I/O, the
    corresponding peripheral function cannot be used.

The following tables show the shared pins.

**GPIO A MUX**

| Bit | Peripheral Name   (Bit =1) | GPIO Name   (Bit = 0) |
| --- | --- | --- |
| 0 | PWM1 | GPIOA0 |
| 1 | PWM2 | GPIOA1 |
| 2 | PWM3 | GPIOA2 |
| 3 | PWM4 | GPIOA3 |
| 4 | PWM5 | GPIOA4 |
| 5 | PWM6 | GPIOA5 |
| 8 | QEP1/CAP1 | GPIOA8 |
| 9 | QEP2/CAP2 | GPIOA9 |
| 10 | CAP3 | GPIOA10 |

**GPIO B MUX**

| Bit | Peripheral Name   (Bit =1) | GPIO Name   (Bit = 0) |
| --- | --- | --- |
| 0 | PWM7 | GPIOB0 |
| 1 | PWM8 | GPIOB1 |
| 2 | PWM9 | GPIOB2 |
| 3 | PWM10 | GPIOB3 |
| 4 | PWM11 | GPIOB4 |
| 5 | PWM12 | GPIOB5 |
| 8 | QEP3/CAP4 | GPIOB8 |
| 9 | QEP4/CAP5 | GPIOB9 |
| 10 | CAP6 | GPIOB10 |

**Sample time**
:   Time interval, in seconds, between consecutive input from the pins.

**Data type**
:   Data type of the data to obtain from the GPIO pins. The data is read as 16-bit
    integer data and then cast to the selected data type. Valid data types are
    `auto`, `double`,
    `single`, `int8`,
    `uint8`, `int16`,
    `uint16`, `int32`,
    `uint32` or `boolean`.

    **Note**

    The width of the vectorized data output by this block is determined by the
    number of bits selected in the **Block Parameters** dialog
    box.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

General-purpose I/O pins for digital input

This block configures the general-purpose I/O (GPIO) registers that control the GPIO
shared pins for digital input. Each I/O port has one MUX register, which is used to select
peripheral operation or digital I/O operation.

**Note**

To avoid losing new settings, click **Apply** before changing the
**IO Port** parameter.
