---
type: simulink-block
title: 'Display'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'display'
documentation_source_path: '../simulink/slref/display.html'
language: zh-CN
chinese_source: worker-translation
---

# Display

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入数据 标量 | 向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated
```

### 输入

### **Port\_1** — 输入数据 标量 | 向量

要显示的输入数据。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated`
## 参数
```yaml
parameters:
- name: Numeric display format
  summary: 用于显示数值输入数据的格式 short（默认） | long | short_e | long_e | bank | hex (Stored Integer) | binary (Stored Integer) | decimal
    (Stored Integer) | octal (Stored Integer)
  group: ''
  block_parameter: Format
  type: character vector
  values: '''short'' | ''long'' | ''short_e'' | ''long_e'' | ''bank'' | ''hex (Stored Integer)'' | ''binary (Stored Integer)''
    | ''decimal (Stored Integer)'' | ''octal (Stored Integer)'''
  default: '''short'''
- name: Decimation
  summary: 显示速率 1（默认） | integer
  group: ''
  block_parameter: Decimation
  type: character vector
  values: '''1'' | integer'
  default: '''1'''
- name: Floating display
  summary: 浮动显示 off（默认） | on
  group: ''
  block_parameter: Floating
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Numeric display format** — 用于显示数值输入数据的格式 `short`（默认） | `long` | `short_e` | `long_e` | `bank` | `hex (Stored Integer)` | `binary (Stored Integer)` | `decimal (Stored Integer)` | `octal (Stored Integer)`

指定所显示数值数据的格式。

| 如果选择... | 模块显示... |
| --- | --- |
| `short` | 具有固定小数点的 5 位缩放值 |
| `long` | 具有固定小数点的 15 位缩放值 |
| `short_e` | 具有浮动小数点的 5 位值 |
| `long_e` | 具有浮动小数点的 16 位值 |
| `bank` | 固定美元和美分格式的值（但不含 $ 或逗号） |
| `hex (Stored Integer)` | 定点输入的存储整数值，以十六进制格式表示 |
| `binary (Stored Integer)` | 定点输入的存储整数值，以二进制格式表示 |
| `decimal (Stored Integer)` | 定点输入的存储整数值，以十进制格式表示 |
| `octal (Stored Integer)` | 定点输入的存储整数值，以八进制格式表示 |

如果 Display 模块的数值输入具有 `single`、`double` 或 `half` 数据类型，并且显示格式为存储整数格式，则输出使用 `long` 格式显示。

如果 Display 模块的数值输入具有枚举数据类型（请参阅 Simulink Enumerations 和 Define Simulink Enumerations）：

- 模块显示枚举值，而不是底层整数的值。
- 将 **Numeric display format** 设置为任何 `Stored Integer` 设置都会导致错误。

如果输入信号为 string 类型，则 **Numeric display format** 参数的选择不会影响字符串的显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`Format` |
| **类型**：character vector |
| **值**：`'short'` | `'long'` | `'short_e'` | `'long_e'` | `'bank'` | `'hex (Stored Integer)'` | `'binary (Stored Integer)'` | `'decimal (Stored Integer)'` | `'octal (Stored Integer)'` |
| **默认值**：`'short'` |

### **Decimation** — 显示速率 `1`（默认） | `integer`

指定显示数据的频率。

显示的数据量以及数据出现的时间步取决于 **Decimation** 模块参数和 `SampleTime` 属性。

- **Decimation** 参数使您能够每隔第 *n* 个采样显示数据，其中 *n* 是抽取因子。默认抽取值为 `1`，即在每个时间步显示数据。

  **注意**

  即使 **Decimation** 值大于 1，Display 模块也会在初始时间更新其显示。
- `SampleTime` 属性可通过 `set_param` 设置，使您能够指定显示点的采样间隔。当使用变步长求解器且时间步之间的间隔不相等时，此属性非常有用。默认采样时间为 `-1`，使模块在确定要显示的点时忽略采样间隔。

  **注意**

  如果模块继承的采样时间为 `Inf`，则忽略 **Decimation** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`Decimation` |
| **类型**：character vector |
| **值**：`'1'` | integer |
| **默认值**：`'1'` |

### **Floating display** — 浮动显示 `off`（默认） | `on`

要将模块用作浮动显示，请选择 **Floating display**。模块输入端口消失，模块显示所选信号线上的信号值。

如果选择 **Floating display**：

- 关闭模型的信号存储重用。有关详细信息，请参阅 Signal storage reuse (Simulink Coder)。
- 不要将多维信号连接到浮动显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`Floating` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |
## 所属库

Simulink / Sinks HDL Coder / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在代码生成中被忽略。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，表示未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

显示输入的值

Display 模块显示输入数据的值。您可以指定显示的频率。对于数值输入数据，您还可以指定显示的格式。

如果模块输入为数组，您可以垂直或水平调整模块大小，以显示除第一个元素之外的更多元素。如果模块输入为向量，模块会从左到右、从上到下依次添加显示字段。模块会尽可能多地显示值。黑色三角形表示模块未显示所有输入数组元素。

Display 模块显示向量信号的前 200 个元素以及矩阵信号的前 20 行和 10 列。

**注意**

如果指定的数值显示格式不足以显示某个值的所有数字，则显示的值可能会丢失精度。结果取决于您的计算机硬件和操作系统。

### 显示缩写

以下缩写会出现在 Display 模块上，以帮助您识别值的格式。

| 当您看到... | 出现的值为... |
| --- | --- |
| `(SI)` | 存储整数值  **注意**  当信号为整数数据类型时，不会出现 `(SI)`。 |
| `hex` | 十六进制格式 |
| `bin` | 二进制格式 |
| `oct` | 八进制格式 |

### 显示字符串

在处理字符串时，Display 模块显示：

- 带双引号的字符串。
- 特殊字符（如换行符）显示为转义序列，例如 `'\n'`。
- 不可显示字符显示为转义八进制数，例如 `'\201'`。

如果输入信号为 string 类型，则 **Numeric display format** 参数的选择不会影响字符串的显示。
