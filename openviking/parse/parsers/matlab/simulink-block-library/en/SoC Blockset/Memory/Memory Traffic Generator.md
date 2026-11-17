---
type: simulink-block
title: 'Memory Traffic Generator'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'memorytrafficgenerator'
documentation_source_path: 'ref/memorytrafficgenerator.html'
language: en
---

# Memory Traffic Generator

## Ports
```yaml
ports:
- name: burstDone
  summary: End of burst and access to memory scalar
  direction: input
  data_types: BurstRequest2BusObj
- name: burstReq
  summary: Request memory access from memory controller scalar
  direction: output
  data_types: BurstRequest2BusObj
```

### Input

### **burstDone** — End of burst and access to memory scalar

This message port receives control messages from a connected Memory
Controller block that the requested burst transaction
completed. Connect the **burstDone** output signal from
the Memory Controller block to this port. For more
information on messages, see Messages.

#### Dependencies

This port is visible when you select the **Show Memory
Controller ports** parameter.

**Data Types:** `BurstRequest2BusObj`
### Output

### **burstReq** — Request memory access from memory controller scalar

This message port sends a message requesting burst access from the
memory controller. Connect this port to the
**burstReq** input port of the Memory
Controller block. For more information on messages, see
Messages.

#### Dependencies

This port is visible when you select the **Show Memory
Controller ports** parameter.

**Data Types:** `BurstRequest2BusObj`
## Parameters
```yaml
parameters:
- name: Show Memory Controller ports
  summary: Show input and output ports on (default) | off
  group: ''
- name: Memory selection
  summary: Choose between memory regions PS memory (default) | PL memory
  group: ''
- name: Request type
  summary: Choose between write or read request Writer (default) | Reader
  group: ''
- name: Total burst requests
  summary: Number of burst requests to generate 100 (default) | integer greater than 1
  group: ''
- name: Burst size (bytes)
  summary: Size of generated burst transactions 256 (default) | scalar
  group: ''
- name: Time between bursts (s)
  summary: Simulation time between burst requests 1e-6 (default) | time, in seconds
  group: ''
- name: Allow simulation only parameters
  summary: Configure additional parameters for simulation only on (default) | off
  group: ''
- name: First burst time
  summary: Simulation time for initial burst request 10e-6 (default) | time, in seconds
  group: ''
- name: Random time between bursts (s)
  summary: Range of simulation time for recurring requests [1e-6 1e-6] (default) | vector of the form [*min* *max*]
  group: ''
- name: Wait for burst done
  summary: Wait for burst-done signal before generating next request off (default) | on
  group: ''
- name: Enable assertion
  summary: Enable verbose information off (default) | on
  group: ''
- name: View performance plots
  summary: Display performance metrics button
  group: ''
```

### **Show Memory Controller ports** — Show input and output ports `on` (default) | `off`

Select this option when using the Memory Traffic Generator
block in a system with a Memory
Channel block and a Memory
Controller block.

Clear this option when using a Memory Traffic Generator
block with one of these specialized memory blocks:

- AXI4 Random Access Memory
- Software to AXI4-Stream
- AXI4-Stream to Software
- AXI4 Video Frame Buffer

When you use a specialized memory block in your design, that block includes
a memory controller which the Memory Traffic Generator block
communicates with implicitly and ports are not necessary.

### **Memory selection** — Choose between memory regions `PS memory` (default) | `PL memory`

Select between processing subsystem (PS) or programming logic (PL)
memory.

- If the selected board supports only a PL memory, then the default
  value is `PL memory`.
- If the selected board supports only PS memory or only PL memory,
  then this parameter is read-only.
- If the selected board is not a supported SoC board, then this
  parameter is not visible.

#### Dependencies

To enable this parameter, clear the **Show Memory Controller
ports** parameter.

### **Request type** — Choose between write or read request `Writer` (default) | `Reader`

Choose between a write or read request type for the block to generate.
Specify `Writer` or `Reader`,
respectively.

### **Total burst requests** — Number of burst requests to generate `100` (default) | integer greater than 1

Generate recurring traffic patterns by setting this value to an integer
greater than one.

### **Burst size (bytes)** — Size of generated burst transactions `256` (default) | scalar

Specify the size of each burst transaction in bytes. This parameter, along
with the width of the datapath (as configured in the configuration
parameters), controls the burst length.

For example, if burst size is 256 bytes, and the Memory
Channel block is configured with **Data width
(bits)** set to 64 (8 bytes), then **Burst
length** is calculated as 256/8 = 32.

### **Time between bursts (s)** — Simulation time between burst requests `1e-6` (default) | time, in seconds

Specify simulation time between burst requests, in seconds.

#### Dependencies

To enable this parameter, clear the **Allow simulation only
parameters** parameter.

**Tip**

If you cleared **Allow simulation only
parameters** and this parameter is not visible – click
**Apply** at the bottom of the Block
Parameters dialog box.

### **Allow simulation only parameters** — Configure additional parameters for simulation only `on` (default) | `off`

Select this parameter to enable configuration of simulation-only
parameters.

### **First burst time** — Simulation time for initial burst request `10e-6` (default) | time, in seconds

Specify simulation time, in seconds, for sending the initial burst
request. This value must be a positive real scalar.

#### Dependencies

To enable this parameter, select **Allow simulation only
parameters** parameter.

### **Random time between bursts (s)** — Range of simulation time for recurring requests `[1e-6 1e-6]` (default) | vector of the form [*min* *max*]

Specify the range of simulation time between burst requests with a vector
of the form [*min*
*max*].

- *min* is the minimum time, in seconds, between
  recurring requests.
- *max* is the maximum time, in seconds, between
  recurring requests.

*min* and *max* must be nonnegative, and
*max* must be greater than
*min*.

To specify a deterministic rate, set the minimum and maximum time between
requests to the same value. If you want reproducible randomization, specify
a seed in the configuration parameters, on the **Hardware
Implementation** pane. For more information on setting the seed
value, see Simulation settings.

#### Dependencies

To enable this parameter, select the **Allow simulation only
parameters** parameter.

### **Wait for burst done** — Wait for burst-done signal before generating next request `off` (default) | `on`

Select this parameter to
wait for a burst-done signal from the previous burst before generating the
next burst request. Clear this parameter to generate burst requests
regardless of other master traffic. To get a known data rate, clear this
parameter.

### **Enable assertion** — Enable verbose information `off` (default) | `on`

Select this parameter to view diagnostic messages when the Traffic
Generator block drops a packet. Clearing this parameter enhances
simulation performance.

### **View performance plots** — Display performance metrics button

Clicking the button opens the **Performance Plots for Memory
Controller** window. You can then select to plot bandwidth,
bursts, or latencies. For more information about performance graphs, see
Memory Controller Latency Plots.

#### Dependencies

To enable this parameter, clear the **Show Memory Controller
ports** parameter.
## Libraries

SoC Blockset / Memory

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design, and execute
on an SoC device, use the **SoC Builder** tool. See Use SoC Builder to Generate SoC Design.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2019a**

## Description

Generate traffic towards memory controller

When connected to a memory controller, the Memory Traffic Generator
block generates read or write requests to the memory, acting as a master. Use this block
to model the impact that a master’s memory accesses has on your algorithm without
explicitly simulating the behavior of that master. You can also use the Memory
Traffic Generator block to characterize performance of your memory subsystem
under varying levels of memory access contention.

**Note**

To model memory contention, the Memory Traffic Generator block
gains memory access, competes in arbitration, and releases access. The Memory
Traffic Generator block does not actively read or write from
memory.
