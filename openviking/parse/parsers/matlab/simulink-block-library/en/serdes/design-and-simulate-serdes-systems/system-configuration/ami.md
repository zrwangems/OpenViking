---
type: simulink-block
title: 'AMI'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Design and Simulate SerDes Systems / System Configuration'
documentation_page: 'ami'
documentation_source_path: 'ref/ami.html'
language: en
---

# AMI

## Ports

### Input

### **WaveIn** — Input signal scalar | vector

Input signal, specified as a waveform.

**Data Types:** `double`
### Output

### **WaveOut** — Modified output data scalar | vector

Modified output data that includes the effect of a lossy printed circuit board
transmission line model according to the method outlined in [1].

**Data Types:** `double`

## Parameters

### **DLL File** — Executable file DLL file | SO file

Browse to select a DLL or SO file that contains the code and data to execute the
SerDes system. You can get the files from a third party vendor you are co-designing
with. You can also get them from another SerDes system you designed and exported that
you want to correlate to current system.

### **AMI File** — AMI settings file text file

Browse to select a AMI file that contains the AMI parameters and settings. The
contents of the AMI file sets up the AMI tree and defines how to run the DLL files. The
AMI tree is represented in the block parameters dialog box. For more information about
how to manage the AMI parameters, see Manage Contents of IBIS and AMI files.

A short summary of the AMI tree is reported by the **Input String**
parameter. If you make any changes to the tree parameters, the **Input
String** parameter is updated to reflect the change.

### **Operation** — Define whether block is used as transmitter or receiver `Tx` (default) | `Rx`

Define whether the block is used as transmitter (Tx) or receiver (Rx). This sets the
priority of the operation and calls the block in the right order for Init simulations.
For more information about Init simulations, see Statistical Analysis in SerDes Systems.

### **Correlation Flow** — Define whether block runs in parallel with another transmitter or receiver off (default) | on

Select this option to run the AMI block in parallel with another
transmitter (Tx) or receiver (Rx).

## Libraries

SerDes Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Co-design SerDes architecture with other vendor designs

The AMI block allows you to co-design SerDes projects with other vendor
IPs. It also allows you to correlate the code-generated/compiled IBIS-AMI models with the
Simulink® models they were generated from.

The block can replace a transmitter or receiver component or run alongside them. To
restore the transmitter or receiver component to their default settings, replace the
AMI block with a Tx or Rx block.

You can only use the block in a Simulink model exported from the SerDes Designer app. The SerDes
Designer sets up the required AMI tree for the block to work correctly. The block must
be used on the top-level of a SerDes Simulink model.

In order to get exact correlation between Rx and AMI, you must add a delay block of length
1024 after the Rx. This delay accounts for the buffer/unbuffer inside the AMI
block which handles the Block Size.

**Note**

You need license to both SerDes Toolbox™ and Signal Integrity
Toolbox™ to use this block.
