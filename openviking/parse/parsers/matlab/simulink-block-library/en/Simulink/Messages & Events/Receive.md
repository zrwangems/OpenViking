---
type: simulink-block
title: 'Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'receive'
documentation_source_path: 'slref/receive.html'
language: en
---

# Receive

## Ports

### Input

### **Port\_1** — Input message scalar | vector | matrix

The input port for the message.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_S** — Show whether a message was received scalar

Outputs `1` if the block receives a message
successfully, and `0` otherwise.

#### Dependencies

To enable this port, select the check box labeled **Show
receive status**.

**Data Types:** `double`

### **Port\_1** — Output signal scalar | vector | matrix

Output port for the signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## Parameters

### **Use internal queue** — Select to use an internal queue on (default for SimEvents®) | off (default for Simulink®)

Select this check box if you use an internal queue to receive
messages.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `UseInternalQueue` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Overwrite the oldest element if queue is full** — Specify queue overwriting policy on (default for Simulink) | off (default for SimEvents)

Select this check box to choose between two queue overwriting
policies.

- If you select the check box, an incoming message overwrites the
  oldest if the queue is full.
- If you clear the check box, the block does not accept new messages
  if the queue is full.

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueOverwriting` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` (for Simulink) and `'off'` (for SimEvents) |

### **Queue length** — Specify the length of the message queue `16` (default) | `scalar`

Specify message queue capacity. The queue length can be specified as a
positive integer between `1` and *2*26-*1* (both included).

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueLength` |
| **Type**: character vector |
| **Values**: `'16'` | scalar |
| **Default**: `'16'` |

### **Queue type** — Specify message queue sorting policy `FIFO` (default) | `LIFO` | `Priority`

The block supports three message sorting policies:

- First-in-first-out (`FIFO`) — The oldest
  message in the storage departs first.
- Last-in-first-out (`LIFO`) — The newest
  message in the storage departs first.
- `Priority` — Messages or entities are
  sorted based on their priority.

  The priority queue can be used only when the **Overwrite the oldest element if queue is full** check
  box is cleared.

  **Note**

  Priority queue accepts only non-bus scalar and it does not
  support `fixed point` data type.

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QueueType` |
| **Type**: character vector |
| **Values**: `'FIFO'` | `'LIFO'` | `'Priority'` |
| **Default**: `'FIFO'` |

### **Priority order** — Specify message queue priority `Ascending` (default) | `Descending`

Choose the direction of sorting messages based on priority.

- `Ascending` — Messages with smaller
  priority values appear in front of the queue.
- `Descending` — Messages with greater
  priority values appear in front of the queue.

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue** and**Queue type** > **Priority**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PriorityOrder` |
| **Type**: character vector |
| **Values**: `'Ascending'` | `'Descending'` |
| **Default**: `'Ascending'` |

### **Show receive status** — Show whether a message was received `off` (default) | on

Select this check box to show whether a message was received. If this
check box is selected the block outputs `1` if it receives
a message successfully, and `0` otherwise.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowQueueStatus` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Initial value** — Set initial data value `[](unspecified)` (default) | `scalar` | `vector` | `matrix`

Enter an initial data value for the queue before the arrival of the first
message. The default value `[](unspecified)` is treated as
`0` with data type double.

To use this block to initialize a nonvirtual bus signal, specify the
initial value as a MATLAB® structure. For more information about initializing nonvirtual
bus signals using structures, see Specify Initial Conditions for Bus Elements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialValue` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Value source when queue is empty** — Value source for empty queue `Hold last value` (default) | `Use initial value`

Specify the value to receive when received message queue is empty.

- `Hold last value` (default) — Holds data
  read from the last message.

  Initially, if the block tries to receive a message and fails, it
  outputs the initial value.
- `Use initial value` — Writes default
  data.

#### Dependencies

This parameter is visible when you select the box labeled
**Use internal queue**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ValueSourceWhenQueueIsEmpty` |
| **Type**: character vector |
| **Values**: `'Hold last value'` | `'Use initial value'` |
| **Default**: `'Hold last value'` |

### **Sample time (-1 for inherited)** — Specify the time interval between samples `-1` (default) | `scalar`

To inherit the sample time, set this parameter to `-1`.
See Specify Sample Time for
more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: `'-1'` | scalar |
| **Default**: `'-1'` |

## Libraries

Simulink / Messages & Events SimEvents

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

When you generate code for a model that uses a message queue and has multitasking
enabled, enable concurrent tasking behavior if that model will be deployed to a
multitasking environment. Otherwise, the generated code has the potential for data
corruption. You enable concurrent tasking behavior by selecting Allow tasks to execute concurrently on target.

**Note**

Receive blocks do not support row-major code generation.

## Version History

**Introduced in R2016a**

## Description

Receive messages

The Receive block extracts data from received messages and writes them
to the output signal port. If there are no new messages when the block executes, the
block uses the **Value source when queue is empty** value.
Receive and Message Receive blocks are identical
blocks.

- Select `Hold last value` to hold data read from the
  last message.
- Select `Use initial value` to write default
  data.
