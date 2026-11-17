---
type: simulink-block
title: 'Compare To Zero'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'comparetozero'
documentation_source_path: 'slref/comparetozero.html'
language: zh-CN
chinese_source: worker-translation
---

# Compare To Zero

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出信号 0 | 1 | 标量 | 向量 | 矩阵
  direction: output
  data_types: uint8 | Boolean
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵，与零进行比较。如果输入数据类型无法表示零，则会发生参数溢出。要检测此溢出，请转到配置参数对话框的**诊断 > 数据有效性**窗格，并将**参数 > 检测溢出**设置为 `warning` 或 `error`。

在这种情况下，模块将输入信号与输入数据类型的*接地值*进行比较。例如，如果输入信号类型为 `fixdt(0,8,2^0,10)`，由于偏置为 10，输入数据类型可以表示从 10 到 265 的无符号 8 位整数。接地值为 10，而不是 0。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 0 | 1 | 标量 | 向量 | 矩阵

如果比较结果为假，输出为 `0`；如果为真，输出为 `1`。

模块输出为 `uint8` 或 `boolean`，取决于您对**输出数据类型**参数的选择。

**数据类型：** `uint8` | `Boolean`
## 参数
```yaml
parameters:
- name: Operator
  summary: 逻辑运算符 <= （默认） | == | ~= | < | >= | >
  group: ''
  block_parameter: relop
  type: 字符向量
  values: '''=='' | ''~=''| ''<'' |''<=''| ''>=''| ''>'''
  default: '''<='''
- name: Output data type
  summary: 输出的数据类型 boolean （默认） | uint8
  group: ''
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''boolean'' | ''uint8'''
  default: '''boolean'''
- name: Enable zero-crossing detection
  summary: 选择以启用零交叉检测 on （默认） | off
  group: ''
  block_parameter: ZeroCross
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''on'''
```

### **Operator** — 逻辑运算符 <= （默认） | == | ~= | < | >= | >

此参数可以具有以下值：

- `==` — 确定输入是否等于零。
- ~`=` — 确定输入是否不等于零。
- `<` — 确定输入是否小于零。
- `<=` — 确定输入是否小于或等于零。
- `>` — 确定输入是否大于零。
- `>=` — 确定输入是否大于或等于零。

#### 编程使用

|  |
| --- |
| **模块参数**： `relop` |
| **类型**： 字符向量 |
| **值**： `'=='` | `'~='`| `'<'` |`'<='`| `'>='`| `'>'` |
| **默认值**： `'<='` |

### **Output data type** — 输出的数据类型 `boolean` （默认） | `uint8`

指定输出的数据类型，`boolean` 或 `uint8`。

#### 编程使用

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型**： 字符向量 |
| **值**：`'boolean'` | `'uint8'` |
| **默认值**： `'boolean'` |

### **Enable zero-crossing detection** — 选择以启用零交叉检测 on （默认） | off

选择以启用零交叉检测。有关更多信息，请参阅零交叉检测。

#### 编程使用

|  |
| --- |
| **模块参数**： `ZeroCross` |
| **类型**： 字符向量 |
| **值**： `'off'` | `'on'` |
| **默认值**： `'on'` |
## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **零交叉检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

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

确定信号与零的比较方式

Compare To Zero 模块将输入信号与零进行比较。使用**Operator**参数指定输入与零的比较方式。

如果比较结果为假，输出为 `0`；如果为真，输出为 `1`。
