---
type: simulink-block
title: 'C281x QEP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C281x'
documentation_page: 'c281xqep'
documentation_source_path: 'ref/c281xqep.html'
language: en
---

# C281x QEP

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Module**
:   Specify which QEP pins to use:

    - `A` — Uses QEP1 and QEP2 pins.
    - `B` — Uses QEP3 and QEP4 pins.

**Counting mode**
:   Specify how to count the QEP pulses:

    - `Counter` — Count the pulses based on GP Timer
      2 (or GP Timer 4 for EVB).
    - `RPM` — Count the rotations per minute.

**Positive rotation**
:   Defines whether to use `Clockwise` or
    `Counterclockwise` as the direction to use as positive
    rotation. This field appears only if you select `RPM`.

**Initial count**
:   Initial value for the counter. The value defaults to `0`.

**Encoder resolution (pulse/revolution)**
:   Number of QEP pulses per revolution. This field appears only if you select
    `RPM`.

**Enable QEP index**
:   Reset the QEP counter to zero when the QEP index input on CAP3\_QEPI1 transitions
    from low to high.

**Enable index qualification mode**
:   Qualify the QEP index input on CAP3\_QEPI1. Check that the levels on CAP1\_QEP1 and
    CAP2\_QEP2 are high before asserting the index signal as valid.

**Timer period**
:   Set the length of the timer period in clock cycles. Enter a value from
    `0` to `65535`. The value defaults to
    `65535`.

    If you know the length of a clock cycle, you can easily calculate how many clock
    cycles to set for the timer period. The following calculation determines the length of
    one clock cycle:

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    In this calculation, you divide the System clock frequency of 150
    MHz by the high-speed clock prescaler of 2. Then, you divide the resulting value by
    the timer control input clock prescaler, 128. The resulting frequency is 0.586 MHz.
    Thus, one clock cycle is 1/.586 MHz, which is 1.706 µs.

**Sample time**
:   Time interval, in seconds, between consecutive reads from the QEP pins.

**Data type**
:   Data type of the QEP pin data. The circuit reads the data as 16-bit data and then
    casts it to the selected data type. Valid data types are
    `auto`, `double`,
    `single`, `int8`,
    `uint8`, `int16`,
    `uint16`, `int32`,
    `uint32` or `boolean`.

**Module**
:   Specify which QEP pins to use:

    - `A` — Uses QEP1 and QEP2 pins.
    - `B` — Uses QEP3 and QEP4 pins.

**Counting mode**
:   Specify how to count the QEP pulses:

    - `Counter` — Count the pulses based on GP Timer
      2 (or GP Timer 4 for EVB).
    - `RPM` — Count the rotations per minute.

**Positive rotation**
:   Defines whether to use `Clockwise` or
    `Counterclockwise` as the direction to use as positive
    rotation. This field appears only if you select `RPM`.

**Initial count**
:   Initial value for the counter. The value defaults to `0`.

**Encoder resolution (pulse/revolution)**
:   Number of QEP pulses per revolution. This field appears only if you select
    `RPM`.

**Enable QEP index**
:   Reset the QEP counter to zero when the QEP index input on CAP3\_QEPI1 transitions
    from low to high.

**Enable index qualification mode**
:   Qualify the QEP index input on CAP3\_QEPI1. Check that the levels on CAP1\_QEP1 and
    CAP2\_QEP2 are high before asserting the index signal as valid.

**Timer period**
:   Set the length of the timer period in clock cycles. Enter a value from
    `0` to `65535`. The value defaults to
    `65535`.

    If you know the length of a clock cycle, you can easily calculate how many clock
    cycles to set for the timer period. The following calculation determines the length of
    one clock cycle:

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    In this calculation, you divide the System clock frequency of 150
    MHz by the high-speed clock prescaler of 2. Then, you divide the resulting value by
    the timer control input clock prescaler, 128. The resulting frequency is 0.586 MHz.
    Thus, one clock cycle is 1/.586 MHz, which is 1.706 µs.

**Sample time**
:   Time interval, in seconds, between consecutive reads from the QEP pins.

**Data type**
:   Data type of the QEP pin data. The circuit reads the data as 16-bit data and then
    casts it to the selected data type. Valid data types are
    `auto`, `double`,
    `single`, `int8`,
    `uint8`, `int16`,
    `uint16`, `int32`,
    `uint32` or `boolean`.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Quadrature encoder pulse circuit

# C281x QEP

Quadrature encoder pulse circuit

Each F2812 Event Manager has three capture units, which can log transitions on its
capture unit pins. Event Manager A (EVA) uses capture units 1, 2, and 3. Event Manager B
(EVB) uses capture units 4, 5, and 6.

The quadrature encoder pulse (QEP) circuit decodes and counts quadrature encoded input
pulses on these capture unit pins. QEP pulses are two sequences of pulses with varying
frequency and a fixed phase shift of 90 degrees (or one-quarter of a period). The circuit
counts both edges of the QEP pulses, so the frequency of the QEP clock is four times the
input sequence frequency.

The QEP, in combination with an optical encoder, is useful for obtaining speed and
position information from a rotating machine. Logic in the QEP circuit determines the
direction of rotation by which sequence is leading. For module A, if the QEP1 sequence
leads, the general-purpose (GP) Timer counts up and if the QEP2 sequence leads, the timer
counts down. The pulse count and frequency determine the angular position and speed.

The C281x QEP module shares GP Timers with other C281 blocks. For more information and
guidance on sharing timers, see Sharing General Purpose Timers Between C281x Peripherals.

- C281x QEP block
