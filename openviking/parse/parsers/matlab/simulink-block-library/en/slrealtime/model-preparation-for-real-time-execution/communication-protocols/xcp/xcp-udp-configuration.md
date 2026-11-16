---
type: simulink-block
title: 'XCP UDP Configuration'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / XCP'
documentation_page: 'xcpudpconfiguration'
documentation_source_path: 'io_ref/xcpudpconfiguration.html'
language: en
---

# XCP UDP Configuration

## Ports

Not documented in R2025b.

## Parameters

### **Config name** — Specify XCP UDP session name `'UDP_Config1'` (default)

Specify a unique name for your XCP session.

### **A2L File** — Select an A2L file file name

Click **Browse** to select an A2L file for your XCP
session.

### **Enable seed/key security** — Select that key required to establish connection `off` (default) | `on`

Select this option if your server requires a secure key to establish
connection. Select a file that contains the seed/key definition to enable
security. **Note:** Seed/key security is not
support on Linux® systems.

### **File (\*.DLL)** — Select file for seed and key security file name

If you select **Enable seed/key security**, this field is
enabled. Click **Browse** to select the file that contains
the seed and key security algorithm that unlocks an XCP server module. This
parameter is available in Windows Desktop Simulation for Vehicle Network
Toolbox.

### **User-defined connect mode** — Allow special connect mode `off` (default) | `on`

Select this option to allow a special (user-defined) connect mode. When
`off`, only a normal mode connection is
supported.

### **Output connection status** — Display connection status `off` (default) | `on`

Select this option to display the status of the connection to the server
module. Selecting this option adds a new output port.

### **Disable CTR error detection** — Disable CTR error detection scheme `on` (default) | `off`

To detect missing packets, the block can check the counter value in each
XCP packet header. When `on`, counter error detection for
packet headers is disabled. When `off`, the counter
**Error detection scheme** is enabled.

### **Error detection scheme** — Select CTR error detection scheme `One counter for all CTOs and DTOs` (default) | `Separate counters for (RES,ERR,EV,SERV) and (DAQ)` | `Separate counters for (RES,ERR), (EV,SERV) and (DAQ)`

To detect missing packets, the block can check the counter value in each
XCP packet header and apply an error-detection scheme.

### **Sample time** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample time.
`-1` means that sample time is inherited. For
information about simulation sample timing, see What Is Sample Time?.

### **Local IP Address** — Client IP address `x.x.x.x`

Enter the IP address to which you want to connect.

### **Local Port** — Client IP port `1–65535`

The combination of **Local IP address** and
**Local port** must be unique.

Ports
in the range `5500` through `5560` are
reserved for Simulink Real-Time communications.

## Libraries

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

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

**Introduced in R2019a**

### R2024b: New parameter: User-defined connect mode

The parameter **User-defined connect mode** allows a special
connect mode.

## Description

Configure XCP UDP server connection

The XCP UDP Configuration block uses the parameters specified in the
A2L file and the ASAP2 database to establish an XCP server connection.

Before you acquire or stimulate data, specify the A2L file to use in your XCP
UDP Configuration. Use one XCP UDP Configuration to configure
one server connection for data acquisition or stimulation. If you add XCP UDP
Data Acquisition and XCP UDP Data Stimulation blocks, your
model checks to see if there is a corresponding XCP UDP Configuration
block. If there is no corresponding XCP UDP Configuration block, the
model prompts you to add one.

The XCP UDP communication blocks support Simulink® accelerator mode and rapid accelerator mode. You can speed up the
execution of Simulink models by using these modes. For more information about these
simulation modes, see Acceleration.
