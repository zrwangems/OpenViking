---
type: simulink-block
title: 'XCP CAN FD Configuration'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'XCP / CAN FD'
documentation_page: 'xcpcanfdconfiguration'
documentation_source_path: 'io_ref/xcpcanfdconfiguration.html'
language: en
---

# XCP CAN FD Configuration

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Config name
  summary: Specify XCP CAN FD session name 'CAN FD_Config1' (default)
  group: ''
- name: A2L File
  summary: Select an A2L file file name
  group: ''
- name: Enable seed/key security
  summary: Select that key required to establish connection off (default) | on
  group: ''
- name: File (\*.DLL)
  summary: Select file for seed and key security file name
  group: ''
- name: User-defined connect mode
  summary: Allow special connect mode off (default) | on
  group: ''
- name: Output connection status
  summary: Display connection status off (default) | on
  group: ''
```

### **Config name** — Specify XCP CAN FD session name `'CAN FD_Config1'` (default)

Specify a unique name for your XCP CAN FD session.

### **A2L File** — Select an A2L file file name

Click **Browse** to select an A2L file for your XCP CAN
FD session.

### **Enable seed/key security** — Select that key required to establish connection `off` (default) | `on`

Select this option if your server requires a secure key to establish
connection. Use the **File (\*DLL)** parameter to specify
the DLL file that contains the seed/key definition. **Note:** Seed/key security is not supported on Linux® systems.

### **File (\*.DLL)** — Select file for seed and key security file name

If you select **Enable seed/key security**
(`EnableSecurity`), this field is enabled. Click
**Browse** to select the file that contains the seed
and key security algorithm that unlocks an XCP server module. This parameter
is available in Windows Desktop Simulation for Vehicle Network Toolbox™.

The **File (\*.DLL)** parameter specifies the name of the
DLL file that contains the seed and key security algorithm used to unlock an
XCP server module. The file defines the algorithm for generating the access
key from a given seed according to ASAM standard definitions. For
information on the file format and API, see the Vector web page Steps to Use Seed&Key Option in CANape or "Seed and Key
Algorithm" in National Instruments™
CAN ECU Measurement and Calibration Toolkit User Manual.
**Note:** The DLL must be the same bitness
as MATLAB (64-bit).

### **User-defined connect mode** — Allow special connect mode `off` (default) | `on`

Select this option to allow a special (user-defined) connect mode. When
`off`, only a normal mode connection is
supported.

### **Output connection status** — Display connection status `off` (default) | `on`

Select this option to display the status of the connection to the server
module. Selecting this option adds a new output port.
## Libraries

Vehicle Network Toolbox / XCP Communication / CAN FD Simulink Real-Time / XCP / CAN FD

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The XCP communication blocks support code generation
with limited deployment portability that runs only on the host computer or Simulink
Real-Time™ targets.

Code generation requires a C++ compiler that is
compatible with the code generation target. For more information, see Supported and Compatible Compilers.

## Version History

**Introduced in R2022b**

### R2024b: New parameter: User-defined connect mode

The parameter **User-defined connect mode** allows a special
connect mode.

## Description

Configure XCP server connection

The XCP CAN FD Configuration block uses the parameters specified in the
A2L file and the ASAP2 database to establish an XCP server connection.

Before you acquire or stimulate data, specify the A2L file to use in your XCP
CAN FD Configuration. Use one XCP CAN FD Configuration to
configure one server connection for data acquisition or stimulation. If you add
XCP CAN FD Data Acquisition and XCP CAN FD Data
Stimulation blocks, your model checks to see if there is a corresponding
XCP CAN FD Configuration block. If there is no corresponding
XCP CAN FD Configuration block, the model editor prompts you to add
one.

The XCP CAN FD communication blocks support Simulink® accelerator mode and rapid accelerator mode. You can speed up the
execution of Simulink models by using these modes. For more information about these
simulation modes, see Acceleration.
