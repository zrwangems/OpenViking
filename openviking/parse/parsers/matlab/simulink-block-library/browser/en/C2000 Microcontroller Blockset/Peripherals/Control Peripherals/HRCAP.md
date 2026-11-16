---
type: simulink-block
title: 'HRCAP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Control Peripherals'
documentation_page: 'hrcap'
documentation_source_path: 'ref/hrcap.html'
language: en
---

# HRCAP

## Ports

### Output

### **Rise[0,1]** — Output capture value vector

The block outputs two consecutive **On** time values. On
time values corresponds to the time between rising and falling edge.

#### Dependencies

To enable this port, set the **HRCAP mode**
parameter to `Normal`.

**Data Types:** `uint16`

### **Fall[0,1]** — Output capture value vector

The block outputs two consecutive **Off** time values. Off
time values corresponds to the time between falling and rising edge.

#### Dependencies

To enable this port, set the **HRCAP mode**
parameter to `Normal`.

**Data Types:** `uint16`

### **CounterOverflow** — Overflow status scalar

The value of `0` indicates that counter has not
overflowed. `1` indicates that the counter has overflowed from
the highest value to `0`.

#### Dependencies

To enable this port, set the HRCAP mode to **Normal**
and select the **Enable counter overflow output**
parameter.

**Data Types:** `uint16`

### **Period** — Output capture data scalar

The block outputs the value period of the waveform. This is sum of on and
off time.

#### Dependencies

To enable this port, set the **HRCAP mode**
parameter to `High resolution` and HRCAP output to either
`Period only` or `All above(Period, On,
Off)`.

**Data Types:** `Fixed point[0,16,16]` | `uint32`

### **On** — Output capture data scalar

The block outputs the value of **On** continuously. On time
values corresponds to the time between rising and falling edge.

#### Dependencies

To enable this port, set the **HRCAP mode**
parameter to `High resolution` and HRCAP output to either
`On time only` or `All above(Period, On,
Off)`.

**Data Types:** `Fixed point[0,16,16]` | `uint32`

### **Off** — Output capture data scalar

The block outputs the value of **Off** continuously. Off
time values corresponds to the time between falling and rising edge.

#### Dependencies

To enable this port, set the **HRCAP mode**
parameter to `High resolution` and HRCAP output to either
`Off time only` or `All above(Period, On,
Off)`.

**Data Types:** `Fixed point[0,16,16]` | `uint32`

## Parameters

### **HRCAP module** — Select HRCAP module `HRCAP1` (default) | `HRCAP2` | `HRCAP3` | `HRCAP4`

Select the HRCAP module which captures the input signal.

### **HRCAP mode** — Select HRCAP mode `Normal` (default) | `High resolution`

Select the HRCAP mode.

You can operate the HRCAP block in the normal or the high resolution mode. In
high resolution mode, the calibration function uses additional HRCAP module and
HRPWM in ePWM module internally.

The unused HRCAP module is used for calibration and HRPWM of highest instance
is used for calibration.

For calibration, the block utilizes unused HRCAP module and largest instance of
HRPWM module. Additionally, this calibration process is executed continuously in
the background.

### **HRCAP clock** — Select HRCAP clock `SYSCLKOUT` (default) | `PLL clock`

Select the HRCAP clock for normal HRCAP mode. You can either select
`SYSCLKOUT` or `PLL clock`
when set to normal mode.

PLL clock is the only clock that is supported in high resolution mode and uses
PLLCLK or PLL2CLK based on the processor.

#### Dependencies

To enable this parameter, set the **HRCAP
mode** parameter to `Normal`.

### **Enable rising edge interrupt** — Enable interrupt when rising edge is detected `on` (default) | `off`

Select this parameter when rising edge interrupt is detected for the HRCAP
block.

### **Enable falling edge interrupt** — Enable interrupt when falling edge is detected `on` (default) | `off`

Select this parameter when falling edge interrupt is detected for the HRCAP
block.

### **Enable counter overflow interrupt** — Enable interrupt when counter overflow is detected `off` (default) | `on`

Select this parameter to when counter overflow interrupt is detected for HRCAP
block.

### **Output type** — Select output data type `HRCAPCLK cycles` (default) | `Microseconds` | `uint32` | `fixdt(0,16,16)`

Select the output type for the HRCAP in the normal mode and high resolution
mode. When you set Output type to uint32, the data is in Q16 format.

### **Enable counter overflow output** — Select to capture HCCOUNTER overflows `off` (default) | `on`

enable the counter overflow interrupt. The block outputs the HCCOUNTER overflow
status at the **CounterOverflow** output port.

#### Dependencies

To enable this parameter, set the **HRCAP
mode** parameter to `Normal`.

### **HRCAP output** — High resolution HRCAP output `Period only` (default) | `ON time only` | `Off time only` | `On and Off time` | `All above(Period, On time, Off time )`

Select the required high resolution outputs. HRCAP output parameter will
configure the ports **Period**, **On**,
**Off** or **All above (Period, On time, Off
time)**.

#### Dependencies

To enable this parameter, set the **HRCAP
mode** parameter to `High resolution`.

### **Sample time** — Frequency at which block reads data from HRCAP `0.1` (default)

Use this parameter to specify the time interval between samples. To inherit
sample time from an upstream block, set this parameter to -1.

## Libraries

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2806x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Capture pulse width in normal or high resolution modes for F2803x and F2806x processors

Use the high resolution capture (HRCAP) block to capture the pulse width in the normal
or high resolution modes and perform conventional and high resolution delta time
measurements. The block uses the HRCAP type 0 module for F2803x and F2806x processors.

**Note**

You can enable high resolution mode (HRCAP mode) using eCAP block for TI F28002x,
F28003x, F28004x, F2838x, F28P55x, and F28P65x processors. For more, see C28x eCAP

You can operate the block in normal or high resolution mode. In high resolution mode,
the calibration function uses additional HRCAP and HRPWM modules internally in the ePWM
module. The block supports only the PLL clock in the high resolution mode and uses the
PLLCLK or PLL2CLK as the PLL clock source based on the processor.

The block does not support SYSCLK in the high resolution mode. For the block to
calibrate the output, the clock frequency has to be higher than 98 MHz, and the maximum
SYSCLK frequency for the F2806x is 90MHz and F2803x boards is 60MHz.

For high resolution mode, only PLL clock is supported and clock frequency should be in
the range between 98 to 120 MHz for calibration.

Output in high resolution mode will be in counts of HCCAPCLK (16-bit HRCAP clock) cycles
in Q16 format and output in normal mode will be vector outputs for rise (0,1) and fall
(0,1) signals which can be in microseconds or HRCAPCLK cycles.
