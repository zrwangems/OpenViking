---
type: simulink-block
title: 'Average-Value Voltage Source Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluevoltagesourceconverter'
documentation_source_path: 'ref/averagevaluevoltagesourceconverter.html'
language: en
---

# Average-Value Voltage Source Converter

## Ports

### Input

### **ModWave** — Modulation wave vector

Physical signal input port associated with the normalized modulation wave.

#### Dependencies

To enable this port, set **Input type** to
`Modulation wave`.

### **Vt** — RMS voltage scalar

Physical signal input port associated with the RMS voltage.

#### Dependencies

To enable this port, set **Input type** to
`Sinusoidal magnitude and phase shift`.

### **ph** — Phase shift scalar

Physical signal input port associated with the phase shift.

#### Dependencies

To enable this port, set **Input type** to
`Sinusoidal magnitude and phase shift`.
### Conserving

### **A** — AC-side terminal A electrical

Electrical conserving port associated with an AC-side terminal.

### **B** — AC-side terminal B electrical

Electrical conserving port associated with an AC-side terminal.

### **+** — DC-side positive terminal electrical

Electrical conserving port associated with the DC-side positive terminal.

### **-** — DC-side negative terminal electrical

Electrical conserving port associated with the DC-side negative terminal.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Input type** — Option to specify input of the block `Modulation wave` (default) | `Sinusoidal magnitude and phase shift`

Option to specify the input of the block as a modulation wave or through sinusoidal
magnitude and phase shift.

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` | scalar

Rated electrical frequency. The value of this parameter must be equal to the value
of the rated electrical frequencies of other sinusoidal sources in your model, if
present.

### **Initial current at DC side** — Initial current at DC side `0` `A` | scalar

Initial current at the DC-side of the converter.

### **Time for holding initial current at DC side** — Time for holding initial current at DC side `1/60` `s` | scalar

Time for holding the initial current at the DC side of the converter.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Single-phase average-value bidirectional AC/DC voltage source converter

The Average-Value Voltage Source Converter block converts
electrical energy from AC to DC voltage or from DC to AC voltage according to an input
single-phase modulation wave. You can specify the modulation wave directly or through phasor
quantities such as the magnitude and phase shift. The corresponding input power is equal to
the output power.

This block can work in both time and frequency-and-time simulation modes. For more
information, see Frequency and Time Simulation Mode.
