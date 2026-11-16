---
type: simulink-block
title: 'Timer'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Integrated Circuits / General Circuits'
documentation_page: 'timer'
documentation_source_path: 'ref/timer.html'
language: en
---

# Timer

## Ports

### Conserving

### **THRES** — Threshold pin electrical

Electrical conserving port associated to the timer threshold pin

### **TRIG** — Trigger pin electrical

Electrical conserving port associated to the timer trigger pin

### **CONT** — Control pin electrical

Electrical conserving port associated to the timer control pin

### **RESET** — Reset pin electrical

Electrical conserving port associated to the timer reset pin

### **OUT** — Output pin electrical

Electrical conserving port associated to the timer output pin

### **DISCH** — Discharge pin electrical

Electrical conserving port associated to the timer discharge pin

## Parameters

### Supply

### **Power supply voltage** — Power supply voltage `15` `V` (default)

The voltage value Vcc that the block applies internally to the timer component.

### Outputs

### **Low level output voltage** — Low level output voltage `0` `V` (default)

The output voltage when the timer output is low and no output current is drawn.

### **High level output voltage** — High level output voltage `14.1` `V` (default)

The output voltage VOH when the timer output is high and no current is drawn.

### **Output resistance** — Output resistance `8` `Ohm` (default)

The ratio of output voltage drop to output current. Set this parameter to (VOH−VOH1)/IOH1, where VOH1 is the reduced output high voltage when the output current is IOH1.

### **Propagation delay** — Propagation delay `100e-9` `s` (default)

Set this value to the input-pulse or output-pulse rise time.

### Discharge

### **Discharge switch on-resistance** — Discharge switch on-resistance `12` `Ohm` (default)

A representative value is the discharge pin saturation voltage divided by the
corresponding current.

### **Discharge switch off-resistance** — Discharge switch off-resistance `500e6` `Ohm` (default)

A representative value is the discharge pin leakage current divided by the corresponding
pin voltage.

### Potential Divider

### **Potential divider component resistance** — Potential divider component resistance `5` `kOhm` (default)

A typical value for a 555-type timer is 5 kΩ. You can measure it directly across the
positive supply and control pins when the chip does not connect to a circuit.

## Libraries

Simscape / Electrical / Integrated Circuits

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009b**

## Description

Behavioral model of a timer integrated circuit

The Timer block is a behavioral model of a timer integrated
circuit such as the NE555.

The following figure shows the implementation structure.

The **Potential divider component resistance** parameter sets the values of
the three resistors creating the potential divider. The two comparator inputs have infinite input
resistance and zero input capacitance. The S-R Latch block
provides the functionality of the set-reset latch. It includes an output capacitor and a resistor
with values set to match the **Propagation delay** parameter value. The block
models the output stage inverter using a CMOS NOT block. You
define the output resistance, low-level output voltage, and high-level output voltage for the
CMOS gate in the Timer block dialog box. The discharge switch
approximates the NPN bipolar transistor on a real timer as a switch with defined switch
on-resistance and off-resistance values.
