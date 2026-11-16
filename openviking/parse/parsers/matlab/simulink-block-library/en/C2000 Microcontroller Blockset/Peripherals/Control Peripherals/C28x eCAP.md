---
type: simulink-block
title: 'C28x eCAP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Control Peripherals'
documentation_page: 'c28xecap'
documentation_source_path: 'ref/c28xecap.html'
language: en
---

# C28x eCAP

## Ports

### Input

### **SI** — Synchronization input from software scalar

The input from the software used to synchronize the eCAP counter. The
synchronization occurs when the synchronization input value is 1.

#### Dependencies

The port appears only when:

- On the **General** tab, you select **Operating mode** > **eCAP** or **APWM**.
- On the **General** tab, you select
  **Enable counter Sync-In mode**
  and **Enable software-forced counter
  synchronizing input**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **RA** — One-Shot capture sequence scalar

Starts a One-Shot capture sequence.

A 2-bit stop register is used to compare the Mod4 counter output, and
when the register and counter values are equal the Mod4 counter is
stopped.

#### Dependencies

The port appears only when:

- On the **General** tab, you select **Operating mode** > **eCAP**.
- On the **eCAP** tab, you set **Select mode control** > **One-Shot** and select **Enable One-Shot
  re-arming control input**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **T** — APWM period scalar

Period of the APWM.

#### Dependencies

The port appears only when:

- On the **General** tab, you select **Operating mode** > **APWM**.
- On the **APWM** tab, you select **Waveform period source** > **Input port**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **W** — APWM width scalar

Width of the APWM.

#### Dependencies

The port appears only when:

- On the **General** tab, you select **Operating mode** > **APWM**.
- On the **APWM** tab, you select **Duty cycle source** > **Input port**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
### Output

The output ports appear only in eCAP mode.

### **TS** — Output timestamps of capture events vector

TS is a vector of 4 signal dimension corresponding to CAP1, CAP2, CAP3
and CAP4 time stamp values depending on the capture event selected in
**Stop value after** on the
**eCAP** tab. Use the **Enable reset
counter after capture event # time-stamp** option to reset
the counter after an event. This option is useful for finding the time
difference between the events.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **CF** — Status of capture event vector

CF is a vector of dimension 4, corresponds to CEVT1-CEVT2. The status
of the capture event. `0` indicates that no event has
occurred.`1` indicates that the event specified by
the **Stop value after** parameter has occurred
at the eCAP pin.

#### Dependencies

The port appears only when you select **Enable capture
event status flag output** on the
**eCAP** tab.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **OF** — Status of overflow scalar

The status of overflow. `0` indicates that counter
has not overflowed.`1` indicates that the counter has
overflowed from the highest value to 0.

#### Dependencies

The port appears only when you select ****Enable overflow status flag
output**** on the
**eCAP** tab.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Scale factor** — Scale factor of HRCLK cycles scalar

The factor which can be used to convert capture value from HRCLK
cycles count to its equivalent SYSCLK cycles count.

#### Dependencies

The port appears only when you select ****Enable high resolution
capture**** parameter and set **Output
type** to **HRCLK/ SYSCLK cycles** on
the **eCAP** tab.

**Data Types:** `single` | `double`

## Parameters

### General

### **Operating mode** — Select eCAP or APWM mode `eCAP` (default) | `APWM`

When you select `eCAP`, the block captures
and logs pin transitions for each capture unit to a FIFO buffer. When
you select `APWM`, the block generates
asymmetric pulse width modulation (APWM) waveforms for driving
downstream systems.

### **eCAPx pin** — Select capture unit pin `eCAP1` (default) | `eCAP2` | `eCAP3` | `eCAP4` | `eCAP5` | `eCAP6` | `eCAP7`

Select the required eCAP module to have a dedicated eCAP pin for
capturing the external events.

The pin selection for the eCAP module can be done by browsing to **Hardware Implementation** > **Target hardware resources**. The selection option is provided only if the module has
more than one pin that can be configured for an eCAP module.

### **Counter phase offset value (0 ~ 4294967295)** — Time base for event captures `0` (default) | integer in [0 4294967295]

This value provides the time base for event captures, clocked by the
system clock. A phase register is used to synchronize with other
counters via software- or hardware-forced synchronization. For
information about software- or hardware-forced synchronization, see
**Enable counter Sync-In mode** parameter. This
value is useful in APWM mode when you need a phase offset between
capture modules. Set the phase offset to an integer from 0 to
42949667295 (232) counts.

### **Enable counter Sync-In mode** — Enable TSCTR counter to load from CTRPHS register `off` (default) | `on`

Synchronization can be done using the SYNCI event or the software.
When synchronization occurs, the shadow register CTRPHS is loaded into
the active counter TSCTR in the current eCAP module and the eCAP modules
downstream.

### **Enable software-forced counter synchronizing input** — Synchronize one or more eCAP time bases `off` (default) | `on`

A software method for synchronizing one or more eCAP time bases. The
synchronization occurs when the synchronization input value is 1.

#### Dependencies

This parameter appears only when **Enable counter Sync-In
mode** is selected.

### **Sync output selection** — Synchronize eCAP counter with other eCAP counters `Disabled` (default) | `Pass through` | `CTR=PRD`

Synchronizes an eCAP counter with other eCAP counters. The options
are:

- `CTR=PRD` — Triggers the sync-out
  signal when the counter value equals the period.

- `Pass through` — The sync-in
  event is passed through as the sync-out signal.

  **Note**

  - Pass through option in case of F2838x/002x
    and 003x processor is only applicable for
    `SWSYNC input`.
    `ECAPSYNCIN` signals cannot be
    passed through and must be configured by the
    downstream eCAP modules under **Hardware Implementation** > **Target hardware
    resources** > **eCAP**.
  - Sync output selection of
    `CTR=PRD` is only applicable for
    eCAP when **Operating mode** is
    set to `APWM`.
- `Disabled` — Disables the
  sync-out signal.

### **Sample time** — Frequency at which block reads input pin value `0.001` (default)

Sample time for the block in seconds.

### eCAP

To enable configuration parameters on the eCAP tab, set **Operating
mode** to `eCAP` on the
**General** tab.

### **Event prescaler (integer from 0 to 31)** — Prescales input signal in multiples of 2 `0` (default) | scalar integer in [0 31]

The input signal is prescaled by twice the value of this parameter.
For example, if you enter `1`, the input is prescaled
by 2, and for `31`, the input is prescaled by 62.
Entering `0` bypasses the input prescaler, leaving the
input capture signal unchanged.

### **Enable high resolution capture** — Select to enable high resolution capture or HRCAP mode `off` (default) | `on`

Select **Enable high resolution capture** (HRCAP
mode) parameter to capture the pulses in high resolution.

#### Dependencies

This parameter is available only for specific TI
processors.

### **Enable continuous calibration mode** — Select to enable continuous calibration mode `off` (default) | `on`

Select **Enable continuous calibration mode**
parameter to perform the calibration periodically.

If continuous calibration mode is not enabled, then calibration occurs
only once (Initialization only). High resolution interrupt is used to
monitor the status of calibration internally to get the updated scale
factor for calculation of time period. Hence Hardware Interrupt block
cannot use high resolution interrupt.

Calibration process provides scale factor which is used to calculate
high resolution capture values in seconds.

#### Dependencies

To enable this parameter, select **Enable high resolution
capture** parameter. This parameter is available only
for specific TI processors.

### **Calibration period in seconds** — Specify calibration period `0.0016` (default) | `on`

Specify the calibration period in seconds.

#### Dependencies

To enable this parameter, select **Enable high resolution
capture** parameter and **Enable continuous
calibration mode**. This parameter is available only
for specific TI processors.

### **Select mode control** — Mode of capture `Continuous` (default) | `One-Shot`

The `Continuous` option performs continuous
timestamp captures (events 1 through 4) using a circular buffer.

The `One-Shot` option enables the
**Enable One-Shot rearming control via input port**
option.

### **Enable One-Shot rearming control via input port** — Re-arms a One-Shot capture sequence `off` (default) | `on`

When this parameter is selected, a One-Shot capture sequence is
re-armed as follows:

1. Mod4 counter is reset to zero.
2. Mod4 counter is unfrozen.
3. Capture register loading is enabled.

#### Dependencies

This parameter appears only when you select
`One-Shot` for **Select mode
control**.

### **Stop value after** — Number of capture events after which capture stops `Capture Event 1` (default) | `Capture Event 2` | `Capture Event 3` | `Capture Event 4`

The number of capture events after which you want to stop the capture
sequence.

### **Enable reset counter after capture event # time-stamp** — Resets counter after capture event `off` (default) | `on`

The eCAP process resets the counter after receiving a capture event
timestamp. In this case, `#` represents the number of
the capture event set in the **Stop value after**
parameter.

### **Select capture event # polarity** — Start capture event on rising edge or falling edge `Rising Edge` (default) | `Falling Edge`

The option that starts a capture event. In this case,
`#` represents the number of the capture event set
in the **Stop value after** parameter.

### **Output type** — Select output type for eCAP `HRCLK/SYSCLK cycles` (default) | `Microseconds`

Select the output type for eCAP.

The output type is int the form of HRCLK cycles when used in HRCAP
mode (high resolution mode) and SYSCLK when used in normal mode. When
you set the output type to HRCLK/SYSCLK cycles in HRCAP mode (high
resolution mode), it enables the port **Scale
factor**.

### **Time-Stamp counter data type** — Data type of counter `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

The data type of the timestamp counter.

### **Enable capture event status flag output** — Output capture event status `off` (default) | `on`

Outputs the capture event status flag at the output port
**CF**. The block outputs `0`
until the event is captured. After the event, the flag value is
`1`.

### **Capture flag data type** — Data type of output port CF `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

The data type of the output port **CF**.

#### Dependencies

This parameter appears only when you select **Enable
capture event status flag output**.

### **Enable overflow status flag output** — Output status of elements of FIFO buffer off (default) | on

Outputs the status of the elements of the FIFO buffer at the output
port **OF**.

### **Overflow flag data type** — Data type of output port OF `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

The data type of the output port **OF**.

#### Dependencies

This parameter appears only when you select **Enable
overflow status flag output**.

### APWM

To enable configuration parameters on the APWM tab, set **Operating
mode** to `APWM` in the
**General** tab.

### **Waveform period units** — Units for measuring waveform period `Seconds` (default) | `Clock cycles`

`Clock cycles` uses the high-speed peripheral
clock cycles of the processor.

### **Waveform period source** — Source from which waveform period value is obtained `Specify via dialog` (default) | `Input port`

Select `Specify via dialog` to enter the
value in **Waveform period**, or select
`Input port` to use a value from the
**T** input port.

### **Waveform period** — Period of PWM waveform `0.001` (default)

Period of the PWM waveform measured in clock cycles or seconds, as
specified in **Waveform period units**.

**Note**

The term *clock cycles* refers to the
high-speed peripheral clock on the F2812 chip. This high-speed
peripheral clock is 75 MHz by default because the high-speed
peripheral clock prescaler is set to 2 (150 MHz/2).

#### Dependencies

This parameter appears only when **Waveform period
source** is set to `Specify via
dialog`.

### **Duty cycle units** — Units for measuring duty cycle `Percentages` (default) | `Clock cycles`

The units used for measuring the duty cycle.

### **Duty cycle source** — Source from which duty cycle for PWM waveform is obtained `Specify via dialog` (default) | `Input port`

Select `Specify via dialog` to enter the
value in **Duty cycle**, or select `Input
port` to use a value from the
**W** input port.

### **Duty cycle** — Ratio of PWM waveform pulse duration to PWM waveform period 50 (default)

The ratio of PWM waveform pulse duration to PWM waveform period. This
ratio is expressed in **Duty cycle units**.

### **Output polarity select** — Set active level for output `Active High` (default) | `Active Low`

When you select `Active High`, the compare
value (duty cycle) defines the high time. Selecting `Active
Low` directs the compare value to define the low
time.

### Interrupt

### **Post interrupt on capture event #** — Set interrupt source to capture event `off` (default) | `on`

You can use the C28x Hardware Interrupt block to
respond to this interrupt. In this case, `#` represents
the number of the capture event set in the **Stop value
after** parameter.

#### Dependencies

This parameter appears only when you set **Operating
mode** to `eCAP` in the
**General** tab.

### **Post interrupt on counter overflow** — Trigger interrupt on counter overflow `off` (default) | `on`

Triggers an interrupt when the counter overflows.

#### Dependencies

This parameter appears only when you set **Operating
mode** to `eCAP` in the
**General** tab.

### **Post interrupt on counter equal period match** — Post interrupt when counter equals period register `off` (default) | `on`

Posts interrupt when the value of counter is same as the value of the
period register (CTR = PRD).

#### Dependencies

This parameter appears only when you set **Operating
mode** to `APWM` in the
**General** tab.

### **Post interrupt on counter equal compare match** — Post interrupt when counter equals compare register `off` (default) | `on`

Posts interrupt when the value of the counter is same as the value of
the compare register (CTR = CMP).

#### Dependencies

This parameter appears only when you set **Operating
mode** to `APWM` in the
**General** tab.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Receive and log transitions on capture input pin or configure auxiliary pulse width modulator

The eCAP block captures the timing of important external events, such
as Hall sensor signals in speed measurements of rotating machinery. When not used in
capture mode, the block can be used in APWM mode, which is a single-channel, asymmetric
pulse width modulator (APWM). You can add one eCAP block to your model for each capture
pin. You cannot assign the same eCAP pin to two eCAP blocks in a model. eCAP and APWM
modes use the same pins. In eCAP mode, the pins are used as input to capture the
transitions. In APWM mode, the pins are used to output a PWM waveform.

The high resolution mode (HRCAP mode) in eCAP block is available only for specific TI
processors. For F2803x and F2806x processors, see HRCAP block.
