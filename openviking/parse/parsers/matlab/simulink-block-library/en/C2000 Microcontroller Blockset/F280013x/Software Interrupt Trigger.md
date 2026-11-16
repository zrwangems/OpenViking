---
type: simulink-block
title: 'C28x Software Interrupt Trigger'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c28xsoftwareinterrupttrigger'
documentation_source_path: 'ref/c28xsoftwareinterrupttrigger.html'
language: en
---

# C28x Software Interrupt Trigger

## Ports

### Input

### **PIEIFRx.INTy** — Triggers software interrupt scalar

The Software Interrupt Trigger block triggers the
software interrupt based on the **CUP interrupt
number** and **PIE interrupt
number** parameters when the input value is greater than
the value in the **Trigger software interrupt when input
value is greater than** parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## Parameters

### **CPU interrupt number** — CPU interrupt number corresponding to hardware interrupt `7` (default) | scalar

Enter an integer value to set the CPU interrupt number corresponding to
the hardware interrupt. For information about CPU numbers of C2000
processors, see C28x Hardware Interrupt.

### **PIE interrupt number** — PIE interrupt number corresponding to hardware interrupt `8` (default) | scalar

Enter an integer value to set the PIE number corresponding to the hardware
interrupt. For information about PIE numbers of C2000 processors, see C28x Hardware Interrupt.

### **Trigger software interrupt when input value is greater than** — Sets value above which block posts an interrupt `0` (default) | scalar

Enter the value for the level that indicates that the interrupt is
asserted by a requesting routine.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Generate software-triggered nonmaskable interrupt

When you add the Software Interrupt Trigger block to a model, the block
polls the values on the input port. When the input value is greater than the value in
the **Trigger software interrupt when input value is greater than**
parameter, the block posts the interrupt corresponding to the selected CPU and
Peripheral Interrupt Expansion (PIE) numbers to the Hardware Interrupt
block in the model.

To use this block, add a Hardware Interrupt block to your model. The
Hardware Interrupt block processes the software-triggered interrupt
from this block into an interrupt service routine on the processor. Set the interrupt
number in the Hardware Interrupt block to the value you set in the
Software Interrupt Trigger block.

The CPU and PIE interrupt numbers together specify a single interrupt for a single
peripheral module. For information about the mapping of CPU and PIE interrupt numbers to
these peripheral interrupts, see C28x Hardware Interrupt.

**Note**

Fixed-point inputs are not supported by the Software Interrupt
Trigger block.
