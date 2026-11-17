---
type: simulink-block
title: 'Rounding Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'roundingfunction'
documentation_source_path: 'slref/roundingfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Rounding Function

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

应用舍入函数的输入信号。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

对输入信号应用舍入函数后的输出信号。输出信号具有与输入相同的维度和数据类型。输出信号的每个元素是将所选舍入函数应用于输入信号对应元素的结果。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Function
  summary: 舍入函数 floor（默认） | ceil | round | fix
  group: ''
  block_parameter: Operator
  type: 字符向量
  values: '''floor'' | ''ceil'' | ''round'' | ''fix'''
  default: '''floor'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认） | 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认） | 带引号的标量或向量'
```

### **Function** — 舍入函数 `floor`（默认） | `ceil` | `round` | `fix`

选择应用于输入信号的舍入函数。

| 舍入函数 | 对输入信号的每个元素进行舍入 |
| --- | --- |
| `floor` | 向负无穷方向舍入到最接近的整数值 |
| `ceil` | 向正无穷方向舍入到最接近的整数 |
| `round` | 舍入到最接近的整数 |
| `fix` | 向零方向舍入到最接近的整数 |

#### 编程用法

|  |
| --- |
| **模块参数**：`Operator` |
| **类型**：字符向量 |
| **值**：`'floor'` | `'ceil'` | `'round'` | `'fix'` |
| **默认值**：`'floor'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认） | 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 带引号的标量或向量 |
## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 代码生成要求**

该模块的 HDL 代码生成要求您使用单一数据类型作为模块的输入，并启用本机浮点模式。在“配置参数”对话框中，在 **HDL Code Generation** > **Floating Point** 窗格中，对于 **Library**，选择 `Native
Floating Point`。要了解有关使用本机浮点模式的更多信息，请参阅 Getting Started with HDL Coder Native Floating-Point Support (HDL Coder) 和 Generate Target-Independent HDL Code with Native Floating-Point (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 本机浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定是将设计中的模块映射为 `inherit`、`Max`、`Min`、`Zero` 还是 `Custom` 以用于浮点运算符。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 添加的延迟等于您为 **NFPCustomLatency** 设置指定的值。另请参阅 NFPCustomLatency (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对信号应用舍入函数

Rounding Function 模块对输入信号的每个元素进行舍入以产生输出信号。

您从 **Function** 参数列表中选择舍入类型。所选函数的名称会显示在模块上。

**提示**

当您需要向量或矩阵输出时，请使用 Rounding Function 模块。
