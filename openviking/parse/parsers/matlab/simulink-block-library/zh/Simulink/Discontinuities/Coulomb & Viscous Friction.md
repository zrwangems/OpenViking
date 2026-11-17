---
type: simulink-block
title: 'Coulomb and Viscous Friction'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'coulombandviscousfriction'
documentation_source_path: 'slref/coulombandviscousfriction.html'
language: zh-CN
chinese_source: worker-translation
---

# Coulomb and Viscous Friction

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

Coulomb and Viscous Friction 模型的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

通过对输入应用摩擦模型计算得到的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Coulomb friction value
  summary: 静摩擦偏移量 [1320]（默认）| 实数值
  group: ''
  block_parameter: offset
  type: 字符向量
  values: 实数值
  default: '''[1 3 2 0]'''
- name: Coefficient of viscous friction
  summary: 动摩擦系数 1（默认）| 实数值
  group: ''
  block_parameter: gain
  type: 字符向量
  values: 实数值
  default: '''1'''
```

要编辑 Coulomb and Viscous Friction 模块的参数，请双击模块图标。

### **Coulomb friction value** — 静摩擦偏移量 `[1320]`（默认）| 实数值

指定应用于所有输入值的偏移量。

#### 编程使用

|  |
| --- |
| **模块参数**：`offset` |
| **类型**：字符向量 |
| **Value**：实数值 |
| **默认值**：`'[1 3 2 0]'` |

### **Coefficient of viscous friction** — 动摩擦系数 `1`（默认）| 实数值

指定非零输入值的信号增益。

#### 编程使用

|  |
| --- |
| **模块参数**：`gain` |
| **类型**：字符向量 |
| **Value**：实数值 |
| **默认值**：`'1'` |
## 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

HDL 代码生成不支持复数输入。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

在零点处建模不连续性，在其他位置具有线性增益

Coulomb and Viscous Friction 模块对库仑（静）摩擦和黏性（动）摩擦进行建模。该模块在零点处建模不连续性，在其他位置建模线性增益。

该模块的输出与以下 MATLAB® 表达式的结果一致：

```
y = sign(x) .* (Gain .* abs(x) + Offset)
```

其中 `y` 是输出，`x` 是输入，`Gain` 是非零输入值的信号增益，`Offset` 是库仑摩擦力。

该模块接受一个输入并生成一个输出。输入可以是标量、向量或矩阵，元素可以是实数或复数。

- 对于标量输入，`Gain` 和 `Offset` 的维度可以与输入不同。输出是标量、向量或矩阵，取决于 `Gain` 和 `Offset` 的维度。
- 对于向量或矩阵输入，`Gain` 和 `Offset` 必须是标量，或者与输入具有相同的维度。输出是与输入具有相同维度的向量或矩阵。
