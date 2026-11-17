---
type: simulink-block
title: 'Bitwise Operator'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'LOG'
documentation_page: 'bitwiseoperator'
documentation_source_path: 'slref/bitwiseoperator.html'
language: zh-CN
chinese_source: worker-translation
---

# Bitwise Operator

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。

- NOT 运算符仅接受一个输入，该输入可以是标量或向量。如果输入是向量，则输出是相同大小的向量，包含输入向量元素的按位逻辑补码。
- 对于单个向量输入，该模块对向量的所有元素应用运算（NOT 运算符除外）。
- 对于两个或更多输入，该模块在所有输入之间执行运算。如果输入是向量，该模块在向量的对应元素之间执行运算，以产生向量输出。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号指定为输出数据类型，该模块从驱动模块继承此类型，必须能精确表示零。满足此条件的数据类型包括有符号和无符号整数数据类型。

模块输出的大小取决于输入数量、向量大小以及您选择的运算符。如果未指定位掩码，则输出为标量。如果指定了位掩码，则输出为向量。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Operator
  summary: 按位逻辑运算符 AND（默认）| OR | NOR | NAND | XOR | NOT
  group: ''
  block_parameter: logicop
  type: character vector
  values: '''AND''|''OR''|''NAND''|''NOR''|''XOR''  | ''NOT'''
  default: '''AND'''
- name: Use bit mask
  summary: 选择以使用位掩码 已选中（默认）| 未选中
  group: ''
  block_parameter: UseBitMask
  type: character vector
  values: '''off''|''on'''
  default: '''on'''
- name: Number of input ports
  summary: 输入信号数量 1（默认）| 整数
  group: ''
  block_parameter: NumInputPorts
  type: character vector
  values: positive integer
  default: '''1'''
- name: Bit Mask
  summary: 与单个输入关联的位掩码 bin2dec（默认）
  group: ''
  block_parameter: BitMask
  type: character vector
  values: positive integer
  default: '''bin2dec(''11011001'')'''
- name: Treat mask as
  summary: 将掩码视为实际值或存储整数 Stored Integer（默认）| Real World Value
  group: ''
  block_parameter: BitMaskRealWorld
  type: character vector
  values: '''Real World Value'' | ''Stored Integer'''
  default: '''Stored Integer'''
```

### **Operator** — 按位逻辑运算符 AND（默认）| OR | NOR | NAND | XOR | NOT

指定模块操作数的按位逻辑运算符。

您可以选择以下按位运算之一：

| 按位运算 | 描述 |
| --- | --- |
| AND | 如果对应位全部为 TRUE，则为 TRUE |
| OR | 如果对应位中至少有一位为 TRUE，则为 TRUE |
| NAND | 如果对应位中至少有一位为 FALSE，则为 TRUE |
| NOR | 如果没有对应位为 TRUE，则为 TRUE |
| XOR | 如果对应位中为 TRUE 的位数为奇数，则为 TRUE |
| NOT | 如果输入为 FALSE，则为 TRUE（仅适用于单输入） |

#### 编程使用

|  |
| --- |
| **模块参数**：`logicop` |
| **类型**：character vector |
| **值**：`'AND'`|`'OR'`|`'NAND'`|`'NOR'`|`'XOR'`  | `'NOT'` |
| **默认值**：`'AND'` |

### **Use bit mask** — 选择以使用位掩码 已选中（默认）| 未选中

选择以使用位掩码。清除此复选框将启用 **Number of input ports** 并禁用 **Bit Mask** 和 **Treat mask as**。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseBitMask` |
| **类型**：character vector |
| **值**：`'off'`|`'on'` |
| **默认值**：`'on'` |

### **Number of input ports** — 输入信号数量 1（默认）| 整数

指定输入数量。您可以有多个输入端口。

#### 依赖关系

清除 **Use bit mask** 复选框将启用 **Number of input ports** 并禁用 **Bit Mask** 和 **Treat mask as**。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumInputPorts` |
| **类型**：character vector |
| **值**：positive integer |
| **默认值**：`'1'` |

### **Bit Mask** — 与单个输入关联的位掩码 bin2dec（默认）

指定与单个输入关联的位掩码。此参数将值读取为十六进制值。

您可以使用位掩码来设置、获取或清除输入上的位。

| 要执行... | 将 Operator 参数设置为... | 并创建位掩码，其中... |
| --- | --- | --- |
| 位设置 | OR | 对于要设置为 1 的每个对应输入位，设为 1 |
| 位清除 | AND | 对于要清除为 0 的每个对应输入位，设为 0 |
| 位获取 | AND | 对于要获取的每个对应输入位，设为 1 |

假设您要设置 8 位输入向量的第四位。位掩码将是 00010000，您可以为 **Bit Mask** 参数指定为 `2^4`。要清除该位，位掩码将是 11101111，您可以为 **Bit Mask** 参数指定为 `2^7+2^6+2^5+2^3+2^2+2^1+2^0`。

**提示**

不要使用大于 53 位的掩码。否则，仿真期间会出现错误消息。

#### 依赖关系

此参数仅在您选择 **Use bit mask** 时可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`BitMask` |
| **类型**：character vector |
| **值**：positive integer |
| **默认值**：`'bin2dec('11011001')'` |

### **Treat mask as** — 将掩码视为实际值或存储整数 `Stored Integer`（默认）| `Real World Value`

指定将掩码视为实际值还是存储整数。

编码方案为 *`V`* = *`SQ`* + *`B`*，如 Fixed-Point Designer™ 文档中的 Scaling (Fixed-Point Designer) 所述。`Real World Value` 将掩码视为 *`V`*。`Stored Integer` 将掩码视为 *`Q`*。

#### 依赖关系

此参数仅在您选择 **Use bit mask** 时可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`BitMaskRealWorld` |
| **类型**：character vector |
| **值**：`'Real World Value'` | `'Stored Integer'` |
| **默认值**：`'Stored Integer'` |
## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `fixed point` | `integer` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 不建议将位运算与布尔信号一起使用。 | |

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

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

对输入执行指定的按位运算

Bitwise Operator 模块对一个或多个操作数执行您指定的按位运算。与 Logical Operator 模块的逻辑运算不同，按位运算将操作数视为位向量而非单个值。

### 模块运算的限制

Bitwise Operator 模块不支持移位运算。对于移位运算，请使用 Shift Arithmetic 模块。

当配置为多输入 XOR 门时，此模块根据 IEEE® 逻辑元件标准执行模 2 加法。
