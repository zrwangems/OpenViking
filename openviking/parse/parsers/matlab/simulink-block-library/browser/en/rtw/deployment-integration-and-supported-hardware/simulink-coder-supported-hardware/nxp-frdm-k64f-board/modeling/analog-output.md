---
type: simulink-block
title: 'Analog Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'analogoutput'
documentation_source_path: 'freescalefrdmk64fboard/ref/analogoutput.html'
language: en
---

# Analog Output

## Ports

### Input

### **Port\_1** — Input signal scalar

The block accepts values between 0 and +1.

When you provide a value between 0–1, this block outputs
an analog signal to the DAC0\_OUT pin, such that:

```
Vout = Vref *[(1+(input*4095))/4096]
```

Vref is the reference voltage for the DAC that you select from **Configuration Parameters**  > **Hardware
Implementation pane** > **DAC** > **DAC0 reference voltage**.

**Data Types:** `single` | `double`

## Parameters

### **Sample time** — How often to read value from the input port `0.1` (default)

Specify how often this block reads the value from the input
port, in seconds.

When you specify this parameter as`-1`, Simulink®
determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Coder Support Package for NXP FRDM-K64F Board

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Send analog output signal to DAC0_OUT pin

The Analog Output block sends an analog signal
to the DAC0\_OUT pin that is on the board.

When you provide a value between 0–1, this block outputs
an analog signal to the DAC0\_OUT pin, such that:

```
Vout = Vref *[(1+(input*4095))/4096]
```

Vref is the reference voltage for the DAC that you select from **Configuration Parameters**  > **Hardware
Implementation pane** > **DAC** > **DAC0 reference voltage**.

Make sure to use only one Analog Output block
within the same model.
