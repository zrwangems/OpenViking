---
type: simulink-block
title: 'Sign'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'sign'
documentation_source_path: 'slref/sign.html'
language: zh-CN
chinese_source: worker-translation
---

# Sign

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

其符号将决定输出的输入信号。

该模块仅对浮点数据类型 `double` 和 `single` 支持复数输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

作为输入信号符号的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Enable zero-crossing detection
  summary: 启用过零检测 on（默认）| off
  group: ''
  block_parameter: ZeroCross
  type: 字符向量 | 字符串
  values: '''off'' | ''on'''
  default: '''on'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的时间间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
```

### **Enable zero-crossing detection** — 启用过零检测 `on`（默认）| `off`

选择以启用过零检测。有关详细信息，请参阅过零检测。

#### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Sample time (-1 for inherited)** — 采样之间的时间间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |
## 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

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

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

指示输入的符号

对于实数输入，Sign 模块输出输入的符号：

| 输入 | 输出 |
| --- | --- |
| 大于零 | 1 |
| 等于零 | 0 |
| 小于零 | –1 |

当输入 `u` 为复数标量时，模块输出与 MATLAB® 的结果一致：

|  |  |
| --- | --- |
| `sign(u) = u./ abs(u)` | **(1)** |
