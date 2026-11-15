---
type: simulink-block
title: 'Speaker'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'speaker'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/speaker.html'
language: en
---

# Speaker

## Ports

### Input

### **Freq** — Tone frequency integer

The block inputs the frequency of the tone the EV3 speaker emits. The speaker can
produce audible sound from approximately `32` to
`13000` Hz. To stop playing a tone, input `0` to
this block input.

#### Dependencies

- To enable this port, set **Input mode** to
  `Frequency and volume` or `Frequency
  only`.

**Data Types:** `uint32`

### **Vol** — Tone volume integer

The block inputs the volume of the tone the EV3 speaker emits. The speaker volume
ranges from `0` to `100` (lowest to highest). To
stop playing a tone, input `0` to this block input.

#### Dependencies

- To enable this port, set **Input mode** to
  `Frequency and volume` or `Volume
  only`.

**Data Types:** `uint32`

## Parameters

### **Input mode** — Accept frequency or volume of tone `Frequency and volume` (default) | `Frequency only` | `Volume only`

Select from these parameters to accept either frequency, volume, or both of the tone.

- `Frequency and volume` — Accept both frequency and
  volume of the tone as inputs to the block.
- `Frequency only` — Accepts only volume of the tone as
  input to the block.
- `Volume only` — Accepts only frequency of the tone as
  input to the block.

### **Volume (0 - 100)** — Tone volume `50` (default) | positive integer between `0` to `100`

Set volume of the tone the EV3 speaker emits.

#### Dependencies

- To enable this parameter, set **Input mode** to
  `Frequency only`.

### **Frequency (Hz)** — Tone frequency `100` (default) | positive integer between `32` to `13000`

Enter frequency of the tone the EV3 speaker emits.

#### Dependencies

- To enable this parameter, set **Input mode** to
  `Volume only`.

### **Duration (ms)** — Tone duration `100` (default) | positive integer

Set the duration to play a continuous tone or an intermittent tone (beeps) from the
EV3 speaker. If this value is equal to or greater than the sample time of the source
block, the speaker emits a continuous tone. If this value is shorter than the sample
time of the source block, the speaker emits an intermittent tone at each sample period.
For example, if the sample time of a source block is 0.1 seconds, and the speaker
duration is 100 milliseconds (0.1 seconds), the speaker plays a continuous tone. If you
change the speaker duration to 50 milliseconds, the speaker emits a beep every 0.1
seconds.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Play tune from EV3 speaker

Use the Speaker block to play tones from the speaker in the EV3 brick. To
play a tone, set the speaker volume and frequency to values that are audible.

This block converts the data type of the values it receives. You do not need to convert
the data type of the input signal.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
