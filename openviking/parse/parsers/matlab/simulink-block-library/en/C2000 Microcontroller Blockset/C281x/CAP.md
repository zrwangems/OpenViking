---
type: simulink-block
title: 'C281x CAP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C281x'
documentation_page: 'c281xcap'
documentation_source_path: 'ref/c281xcap.html'
language: en
---

# C281x CAP

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

### Data Format Pane

**Module**
:   Select the Event Manager (EV) module to use:

    - `A` — Use CAPs 1, 2, and 3.
    - `B` — Use CAPs 4, 5, and 6.

**Output overrun status flag**
:   Select to output the status of the elements in the FIFO. The data type of the
    status flag is uint16.

**Output data format**
:   The type of data to output:

    - `Send 2 elements (FIFO Buffer)` — Sends the
      latest two values. The output is updated when there are two elements in the
      FIFO, which is indicated by bit 13 or 11 or 9 being sent (CAP x FIFO). If the
      CAP is polled when fewer than two elements are captures, old values are
      repeated. The CAP registers are read as follows:

      1. The CAP x FIFO status bits are read and the value is stored in the
         status flag.
      2. The top value of the FIFO is read and stored in the output at index 0.
      3. The new top value of the FIFO (the previously stored bottom stack value)
         is read and stored in the output at index 1.

    - `Send 1 element (oldest)` — Sends the older
      of the two most recent values. The output is updated when there is at least one
      element in the FIFO, which is indicated by the bits 13:12, or 11:10, or 9:8
      being sent. The CAP registers are read as follows:

      1. The CAP x FIFO status bits are read and the value is stored in the
         status flag.
      2. The top value of the FIFO is read and stored in the output.

    - `Send 1 element (latest)` — Sends the most
      recent value. The output is updated when there is at least one element in the
      FIFO, which is indicated by the bits 13:12, or 11:10, or 9:8 being sent. The CAP
      registers are read as follows:

      1. The CAP x FIFO status bits are read and the value is stored in the
         status flag.
      2. If the FIFO buffer contains two entries, the bottom value is read and
         stored in the output. If the FIFO buffer contains one entry, the top value
         is read and stored in the output.

**Sample time**
:   Time between outputs from the FIFO. If new data is not available, the previous
    data is sent.

**Data type**
:   Data type of the output data. Available options are
    `auto`, `double`,
    `single`, `int8`,
    `uint8`, `int16`,
    `uint16`, `int32`,
    `uint32`, and `boolean`. The
    `auto` option uses the data type of a connected block
    that outputs data to this block. If this block does not receive an input,
    `auto` sets the data type to
    `double`.

    **Note**

    The output of the C281x CAP block can be vectorized.

### CAP Panes

The CAP panes set parameters for individual CAPs. The particular CAP affected by a CAP
pane depends on the EV module you selected:

- **CAP1** controls CAP 1 or CAP 4, for EV module A or B,
  respectively.
- **CAP2** controls CAP 2 or CAP 5, for EV module A or B,
  respectively.
- **CAP3** controls CAP 3 or CAP 6, for EV module A or B,
  respectively.

**Enable CAP**
:   Select to use the specified capture unit pin.

**Edge Detection**
:   Type of transition detection to use for this CAP. Available types are
    `Rising Edge`, `Falling Edge`,
    `Both Edges`, and
    `No transition`.

**Time Base**
:   Select which target board GP timer the CAP uses as a time base. CAPs 1, 2, and 3
    can use `Timer 1` or
    `Timer 2`. CAPs 4, 5, and 6 can use
    `Timer 3` or
    `Timer 4`.

**Clock source**
:   This option is available only for the CAP 3 pane. You can select
    `Internal` to use the internal time base. Also configure
    the **Counting mode**, **Timer prescaler**, and
    **Timer period source** for the internal time base.

    Select `QEP circuit` to generate the input clock from
    the quadrature encoder pulse (QEP) submodule.

**Counting mode**
:   Select `Up` to generate an asymmetrical waveform
    output, or `Up-down` to generate a symmetrical waveform
    output, as shown in the following illustration.

    The Counting mode is for the internal timer settings.

    When you specify the **Counting mode** as
    `Up` (asymmetric) the waveform:

    - Starts low
    - Goes high when the rising period counter value matches the **Compare
      value**
    - Goes low at the end of the period

    When you specify the **Counting mode** as
    `Up-down` (symmetric) the waveform:

    - Starts low
    - Goes high when the increasing period counter value matches the
      **Compare value**
    - Goes low when the decreasing period counter value matches the
      **Compare value**

    **Counting mode** becomes unavailable when you set
    **Clock source** to `QEP
    circuit`.

**Timer Prescaler**
:   Clock divider factor by which to prescale the selected GP timer to produce the
    desired timer counting rate. Available options are
    `none`,
    `1/2`, `1/4`,
    `1/8`, `1/16`,
    `1/32`, `1/64`, and
    `1/128`. The following table shows the rates that result
    from selecting each option.

    | Scaling | Resulting Rate (µs) |
    | --- | --- |
    | none | 0.01334 |
    | 1/2 | 0.02668 |
    | 1/4 | 0.05336 |
    | 1/8 | 0.10672 |
    | 1/16 | 0.21344 |
    | 1/32 | 0.42688 |
    | 1/64 | 0.85376 |
    | 1/128 | 1.70752 |

    **Note**

    These rates assume a 75 MHz input clock.

**Timer period source**
:   Select `Specify via dialog` to enable the
    **Timer period** parameter. Select `Input
    port` to create a block input, **T1**, that accepts
    the timer period value.

**Timer period**
:   Set the length of the timer period in clock cycles. Enter a value from
    `0` to `65535`. The value defaults to
    `65535`.

    If you know the length of a clock cycle, you can easily calculate how many clock
    cycles to set for the timer period. The following calculation determines the length
    of one clock cycle:

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    In this calculation, you divide the System clock frequency of
    150 MHz by the high-speed clock prescaler of 2. Then, you divide the resulting value
    by the timer control input clock prescaler, 128. The resulting frequency is 0.586
    MHz. Thus, one clock cycle is 1/.586 MHz, which is 1.706 µs.

**Post interrupt on CAP**
:   Check this check box to post an asynchronous interrupt on CAP.

### See Also

C28x Hardware Interrupt

### Data Format Pane

**Module**
:   Select the Event Manager (EV) module to use:

    - `A` — Use CAPs 1, 2, and 3.
    - `B` — Use CAPs 4, 5, and 6.

**Output overrun status flag**
:   Select to output the status of the elements in the FIFO. The data type of the
    status flag is uint16.

**Output data format**
:   The type of data to output:

    - `Send 2 elements (FIFO Buffer)` — Sends the
      latest two values. The output is updated when there are two elements in the
      FIFO, which is indicated by bit 13 or 11 or 9 being sent (CAP x FIFO). If the
      CAP is polled when fewer than two elements are captures, old values are
      repeated. The CAP registers are read as follows:

      1. The CAP x FIFO status bits are read and the value is stored in the
         status flag.
      2. The top value of the FIFO is read and stored in the output at index 0.
      3. The new top value of the FIFO (the previously stored bottom stack value)
         is read and stored in the output at index 1.

    - `Send 1 element (oldest)` — Sends the older
      of the two most recent values. The output is updated when there is at least one
      element in the FIFO, which is indicated by the bits 13:12, or 11:10, or 9:8
      being sent. The CAP registers are read as follows:

      1. The CAP x FIFO status bits are read and the value is stored in the
         status flag.
      2. The top value of the FIFO is read and stored in the output.

    - `Send 1 element (latest)` — Sends the most
      recent value. The output is updated when there is at least one element in the
      FIFO, which is indicated by the bits 13:12, or 11:10, or 9:8 being sent. The CAP
      registers are read as follows:

      1. The CAP x FIFO status bits are read and the value is stored in the
         status flag.
      2. If the FIFO buffer contains two entries, the bottom value is read and
         stored in the output. If the FIFO buffer contains one entry, the top value
         is read and stored in the output.

**Sample time**
:   Time between outputs from the FIFO. If new data is not available, the previous
    data is sent.

**Data type**
:   Data type of the output data. Available options are
    `auto`, `double`,
    `single`, `int8`,
    `uint8`, `int16`,
    `uint16`, `int32`,
    `uint32`, and `boolean`. The
    `auto` option uses the data type of a connected block
    that outputs data to this block. If this block does not receive an input,
    `auto` sets the data type to
    `double`.

    **Note**

    The output of the C281x CAP block can be vectorized.

### CAP Panes

The CAP panes set parameters for individual CAPs. The particular CAP affected by a CAP
pane depends on the EV module you selected:

- **CAP1** controls CAP 1 or CAP 4, for EV module A or B,
  respectively.
- **CAP2** controls CAP 2 or CAP 5, for EV module A or B,
  respectively.
- **CAP3** controls CAP 3 or CAP 6, for EV module A or B,
  respectively.

**Enable CAP**
:   Select to use the specified capture unit pin.

**Edge Detection**
:   Type of transition detection to use for this CAP. Available types are
    `Rising Edge`, `Falling Edge`,
    `Both Edges`, and
    `No transition`.

**Time Base**
:   Select which target board GP timer the CAP uses as a time base. CAPs 1, 2, and 3
    can use `Timer 1` or
    `Timer 2`. CAPs 4, 5, and 6 can use
    `Timer 3` or
    `Timer 4`.

**Clock source**
:   This option is available only for the CAP 3 pane. You can select
    `Internal` to use the internal time base. Also configure
    the **Counting mode**, **Timer prescaler**, and
    **Timer period source** for the internal time base.

    Select `QEP circuit` to generate the input clock from
    the quadrature encoder pulse (QEP) submodule.

**Counting mode**
:   Select `Up` to generate an asymmetrical waveform
    output, or `Up-down` to generate a symmetrical waveform
    output, as shown in the following illustration.

    The Counting mode is for the internal timer settings.

    When you specify the **Counting mode** as
    `Up` (asymmetric) the waveform:

    - Starts low
    - Goes high when the rising period counter value matches the **Compare
      value**
    - Goes low at the end of the period

    When you specify the **Counting mode** as
    `Up-down` (symmetric) the waveform:

    - Starts low
    - Goes high when the increasing period counter value matches the
      **Compare value**
    - Goes low when the decreasing period counter value matches the
      **Compare value**

    **Counting mode** becomes unavailable when you set
    **Clock source** to `QEP
    circuit`.

**Timer Prescaler**
:   Clock divider factor by which to prescale the selected GP timer to produce the
    desired timer counting rate. Available options are
    `none`,
    `1/2`, `1/4`,
    `1/8`, `1/16`,
    `1/32`, `1/64`, and
    `1/128`. The following table shows the rates that result
    from selecting each option.

    | Scaling | Resulting Rate (µs) |
    | --- | --- |
    | none | 0.01334 |
    | 1/2 | 0.02668 |
    | 1/4 | 0.05336 |
    | 1/8 | 0.10672 |
    | 1/16 | 0.21344 |
    | 1/32 | 0.42688 |
    | 1/64 | 0.85376 |
    | 1/128 | 1.70752 |

    **Note**

    These rates assume a 75 MHz input clock.

**Timer period source**
:   Select `Specify via dialog` to enable the
    **Timer period** parameter. Select `Input
    port` to create a block input, **T1**, that accepts
    the timer period value.

**Timer period**
:   Set the length of the timer period in clock cycles. Enter a value from
    `0` to `65535`. The value defaults to
    `65535`.

    If you know the length of a clock cycle, you can easily calculate how many clock
    cycles to set for the timer period. The following calculation determines the length
    of one clock cycle:

    Sysclk(150MHz)→HISPCLK(1/2)→InputClockPrescaler(1/128)

    In this calculation, you divide the System clock frequency of
    150 MHz by the high-speed clock prescaler of 2. Then, you divide the resulting value
    by the timer control input clock prescaler, 128. The resulting frequency is 0.586
    MHz. Thus, one clock cycle is 1/.586 MHz, which is 1.706 µs.

**Post interrupt on CAP**
:   Check this check box to post an asynchronous interrupt on CAP.

### See Also

C28x Hardware Interrupt
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Receive and log capture input pin transitions

# C281x CAP

Receive and log capture input pin transitions

The C281x CAP module provides input capture functionality for systems where
precise timing of external events is important. The C281x CAP block sets parameters for the
capture units (CAPs) of the Event Manager (EV) module. The capture units log transitions
detected on the capture unit pins by recording the times of the input signal transitions
into a two-level deep FIFO stack. You can set the capture unit pins to detect rising edge,
falling edge, either type of transition, or no transition. The
cnt output of the block gives the captured value of the EV running timer.

The C281x chip has six capture units — three associated with each EV module.
Capture units 1, 2, and 3 are associated with EVA and capture units 4, 5, and 6 are
associated with EVB. Each capture unit is associated with a capture input pin.

Each group of EV module capture units can use one of two general-purpose (GP) timers on
the target board. EVA capture units can use GP timer 1 or 2. EVB capture units can use GP
timer 3 or 4. When a transition occurs, the module stores the value of the selected timer in
the two-level deep FIFO stack.

The C281x CAP module shares GP Timers with other C281 blocks. For more information and
guidance on sharing timers, see Sharing General Purpose Timers Between C281x Peripherals.

**Note**

You can have up to two C281x CAP blocks in a model—one block for each EV
module.

### Outputs

This block has up to two outputs: a `cnt` (count) output and an
optional, FIFO status `flag` output. The `cnt` output
holds the value of the EV timer captured during the detected transitions. The
`cnt` output gives the captured values of the running counter based on
the value set in **Output data format** parameter. The status flag
outputs are:

- `0` — The FIFO is empty. Either
  no captures have occurred or the previously stored
  captures have been read from the stack. (The binary version of this flag is
  `00`.)
- `1` — The FIFO has one entry in the top register of the
  stack. (The binary version of this flag is `01`.)
- `2` — The FIFO has two entries in the stack registers.
  (The binary version of this flag is `10`.)
- `3` — The FIFO has two entries in the stack registers and
  one or more captured values have been lost. This occurs because another capture
  occurred before the FIFO stack was read. This means that the FIFO stack is read when
  you execute the block as specified by your scheduling scheme synchronously, if a
  sample time is used or asynchronously, if triggered by an interrupt or an idle task.
  The new value is placed in the bottom register. The bottom register value is pushed to
  the top of the stack and the top value is pushed out of the stack. (The binary version
  of this flag is `11`.)

- C281x CAP block
