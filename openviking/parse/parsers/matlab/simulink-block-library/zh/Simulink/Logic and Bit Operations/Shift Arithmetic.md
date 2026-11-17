---
type: simulink-block
title: 'Shift Arithmetic'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'shiftarithmetic'
documentation_source_path: 'slref/shiftarithmetic.html'
language: zh-CN
chinese_source: worker-translation
---

# Shift Arithmetic

## 端口
```yaml
ports:
- name: u
  summary: 要进行运算的数 标量 | 向量 | 数组
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: s
  summary: 要移位的位数 标量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 运算结果 标量 | 向量 | 数组
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **u** — 要进行运算的数 标量 | 向量 | 数组

要进行运算的数，指定为标量、向量或数组。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **s** — 要移位的位数 标量

要移位的位数，指定为标量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 运算结果 标量 | 向量 | 数组

运算结果，以标量、向量或数组形式返回。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: 'Bits to shift: Source'
  summary: 要移位的位数的来源 Dialog（默认）| Input port
  group: ''
  block_parameter: BitShiftNumberSource
  type: 字符向量、字符串
  values: '''Dialog'' | ''Input port'''
  default: '''Dialog'''
- name: 'Bits to shift: Direction'
  summary: 移位方向 Bidirectional（默认）| Left | Right
  group: ''
  block_parameter: BitShiftDirection
  type: 字符向量、字符串
  values: '''Left'' | ''Right'' | ''Bidirectional'''
  default: '''Bidirectional'''
- name: 'Bits to shift: Number'
  summary: 要移位的位数 8（默认）| 标量 | 向量 | 数组
  group: ''
  block_parameter: BitShiftNumber
  type: 字符向量、字符串
  values: 标量 | 向量 | 数组
  default: '''8'''
- name: 'Binary points to shift: Number'
  summary: 要移动二进制点的位数 0（默认）| 标量
  group: ''
  block_parameter: BinPtShiftNumber
  type: 字符向量、字符串
  values: 标量
  default: '''0'''
- name: Diagnostic for out of range shift value
  summary: 诊断操作 None（默认）| Warning | Error
  group: ''
  block_parameter: DiagnosticForOORShift
  type: 字符向量、字符串
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''None'''
- name: Check for out-of-range 'Bits to shift' in generated code
  summary: 检查生成代码中超出范围的移位位数 off（默认）| on
  group: ''
  block_parameter: CheckOORBitShift
  type: 字符向量、字符串
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Bits to shift: Source** — 要移位的位数的来源 `Dialog`（默认）| `Input port`

指定是在对话框中输入要移位的位数，还是从输入端口继承这些值。

**可调：** 否

#### 编程用法

|  |
| --- |
| **模块参数**：`BitShiftNumberSource` |
| **类型**：字符向量、字符串 |
| **值**：`'Dialog'` | `'Input port'` |
| **默认值**：`'Dialog'` |

### **Bits to shift: Direction** — 移位方向 `Bidirectional`（默认）| `Left` | `Right`

指定移位方向：左移、右移或双向。

**可调：** 否

#### 编程用法

|  |
| --- |
| **模块参数**：`BitShiftDirection` |
| **类型**：字符向量、字符串 |
| **值**：`'Left'` | `'Right'` | `'Bidirectional'` |
| **默认值**：`'Bidirectional'` |

### **Bits to shift: Number** — 要移位的位数 `8`（默认）| 标量 | 向量 | 数组

指定移位值的标量、向量或数组。

| 如果方向为... | 则... |
| --- | --- |
| `Left` 或 `Right` | 使用正整数指定移位。 |
| `Bidirectional` | 使用正整数表示右移，使用负整数表示左移。 |

**可调：** 否

#### 依赖关系

要启用此参数，请将 **Bits to shift:
Source** 设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数**：`BitShiftNumber` |
| **类型**：字符向量、字符串 |
| **值**：标量 | 向量 | 数组 |
| **默认值**：`'8'` |

### **Binary points to shift: Number** — 要移动二进制点的位数 `0`（默认）| 标量

指定输入信号二进制点要移动的整数位数。正值表示右移，负值表示左移。

**可调：** 否

#### 编程用法

|  |
| --- |
| **模块参数**：`BinPtShiftNumber` |
| **类型**：字符向量、字符串 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Diagnostic for out of range shift value** — 诊断操作 `None`（默认）| `Warning` | `Error`

指定当模块包含超出范围的移位值时，是否在仿真期间生成警告或错误。选项包括：

- `None` — 软件不采取任何操作。
- `Warning` — 软件显示警告并继续仿真。
- `Error` — 软件终止仿真并显示错误。

有关详细信息，请参阅 Simulation and Accelerator Mode Results for Out-of-Range Bit Shift Values。

#### 编程用法

|  |
| --- |
| **模块参数**：`DiagnosticForOORShift` |
| **类型**：字符向量、字符串 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'None'` |

### **Check for out-of-range 'Bits to shift' in generated code** — 检查生成代码中超出范围的移位位数 `off`（默认）| `on`

选中此复选框可在生成的代码中包含条件语句，以防止超出范围的移位值。当 **Bits to shift: Source** 为 `Input port` 时，此复选框可用。

有关详细信息，请参阅 Code Generation for Out-of-Range Bit Shift Values。

#### 编程用法

|  |
| --- |
| **模块参数**：`CheckOORBitShift` |
| **类型**：字符向量、字符串 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |
## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

当 **Bits to shift: Source** 为 **Dialog** 或 **Input port** 时，您可以生成 HDL 代码。

**HDL 架构**

生成的 VHDL 代码使用 `shift_right` 函数和 `sll` 运算符。

生成的 Verilog 代码使用 `>>>` 和 `<<<` 移位运算符。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

当 **Bits to shift: Source** 为 **Input port** 时，不支持二进制点移位。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

对信号的位或二进制点进行移位

Shift Arithmetic 模块可以对输入信号的位或二进制点进行移位，或同时对两者进行移位。

例如，将数据类型为 `sfix(8)` 的输入的二进制点向右和向左移动两位，得到以下十进制值。

| 移位操作 | 二进制值 | 十进制值 |
| --- | --- | --- |
| 不移位（原始数值） | 11001.011 | –6.625 |
| 二进制点右移两位 | 1100101.1 | –26.5 |
| 二进制点左移两位 | 110.01011 | –1.65625 |

此模块对有符号数执行算术位移。因此，模块在每次移位时循环使用最高有效位。将数据类型为 `sfix(8)` 的输入的位向右和向左移动两位，得到以下十进制值。

| 移位操作 | 二进制值 | 十进制值 |
| --- | --- | --- |
| 不移位（原始数值） | 11001.011 | –6.625 |
| 位右移两位 | 11110.010 | –1.75 |
| 位左移两位 | 00101.100 | 5.5 |
