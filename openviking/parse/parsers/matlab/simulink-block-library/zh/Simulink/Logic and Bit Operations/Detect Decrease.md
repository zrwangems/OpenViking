---
type: simulink-block
title: 'Detect Decrease'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'detectdecrease'
documentation_source_path: 'slref/detectdecrease.html'
language: zh-CN
chinese_source: worker-translation
---

# Detect Decrease

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
- name: Port_1
  summary: 输出信号 0 | 1
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Port\_1** — 输出信号 0 | 1

输出信号，当输入信号小于其前一值时，为 true（等于 1）；当输入信号大于或等于其前一值时，为 false（等于 0）。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
## 参数
```yaml
parameters:
- name: Initial condition
  summary: 前一输入的初始条件 0 （默认） | 标量 | 向量
  group: ''
  block_parameter: vinit
  type: character vector
  values: scalar | vector
  default: '''0'''
- name: Input processing
  summary: 指定基于采样或基于帧的处理 Elements as channels (sample based) （默认） | Columns as channels (frame based)
  group: ''
  block_parameter: InputProcessing
  type: character vector
  values: '''Columns as channels (frame based)'' | ''Elements as channels (sample based)'''
  default: '''Elements as channels (sample based)'''
- name: Output data type
  summary: 输出的数据类型 boolean （默认） | uint8
  group: ''
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''boolean'' | ''uint8'''
  default: '''boolean'''
```

### **Initial condition** — 前一输入的初始条件 0 （默认） | 标量 | 向量

设置前一输入 U/z 的初始条件。

#### 编程使用

|  |
| --- |
| **模块参数**：`vinit` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'0'` |

### **Input processing** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)` （默认） | `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为独立通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。
- `Elements as channels (sample based)` — 将输入的每个元素视为独立通道（基于采样的处理）。

使用 **Input processing** 指定模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：character vector |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

### **Output data type** — 输出的数据类型 `boolean` （默认） | `uint8`

将输出数据类型设置为 `boolean` 或 `uint8`。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'boolean'` | `'uint8'` |
| **默认值**：`'boolean'` |
## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

检测信号值的下降

Detect Decrease 模块确定输入是否严格小于其前一值。

此模块仅支持离散采样时间。
