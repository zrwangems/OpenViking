---
type: simulink-block
title: 'Signal Conversion'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'signalconversion'
documentation_source_path: 'slref/signalconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Signal Conversion

## 端口
```yaml
ports:
- name: Port_1
  summary: 要转换的输入信号 标量 | 向量 | 矩阵 | 数组 | 总线
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus | image
- name: Port_1
  summary: 转换后的信号 标量 | 向量 | 矩阵 | 数组 | 总线
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
```

### 输入

### **Port\_1** — 要转换的输入信号 标量 | 向量 | 矩阵 | 数组 | 总线

输入信号是标量、向量、矩阵、数组或总线，此模块将其转换为另一种类型。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 转换后的信号 标量 | 向量 | 矩阵 | 数组 | 总线

输出信号是转换为指定类型的输入信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: Output
  summary: 转换类型 Signal copy | Virtual bus | Nonvirtual bus
  group: ''
  block_parameter: ConversionOutput
  values: '''Signal copy''（默认） | ''Virtual bus'' | ''Nonvirtual bus'''
- name: Data type
  summary: '非虚拟总线数据类型 Inherit: auto（默认） | Bus: <object name> | <data type expression>'
  group: ''
  block_parameter: OutDataTypeStr
  values: '''Inherit: auto''（默认） | ''Bus: <object name>'' | ''<data type expression>'''
- name: Exclude this block from 'Block reduction' optimization
  summary: 将模块从模块缩减优化中排除的选项 off（默认） | on
  group: ''
  block_parameter: OverrideOpt
  values: '''off''（默认） | ''on'''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上，在**准备**库中选择**属性检查器**。

### **Output** — 转换类型 `Signal copy` | `Virtual bus` | `Nonvirtual bus`

指定要执行的转换类型。

- `Signal copy` — 创建输入信号的连续副本。此值是 Signal Conversion 和 Signal Copy 模块的默认值。
- `Virtual bus` — 将非虚拟总线转换为虚拟总线。此值是 To Virtual Bus 模块的默认值。
- `Nonvirtual bus` — 将虚拟总线转换为非虚拟总线。此值是 To Nonvirtual Bus 模块的默认值。

对于 `Signal copy` 选项，输入类型决定了模块如何执行复制。

例如，假设模块接收一个 mux 信号，其元素占用不连续的内存区域。转换会为 mux 信号的元素分配一块连续的内存区域，并在每个时间步将模块输入所表示的不连续区域中的值复制到模块输出所表示的连续区域中。输出是一个向量，其元素占用连续的内存区域。

使用的转换类型取决于您的建模目标。

| 建模目标 | 选项 |
| --- | --- |
| 减少 mux 信号的生成代码。有关涉及 Simulink Coder™ 软件的示例，请参阅 Generate Reentrant Code from Subsystems (Simulink Coder)。 | `Signal copy` |
| 将具有常量采样时间的模块连接到使能子系统的输出端口。 | `Signal copy` |
| 通过将非虚拟总线转换为虚拟总线来节省内存。 | `Virtual bus` |
| 将虚拟总线传递给需要非虚拟总线的建模构造。 | `Nonvirtual bus` |
| 创建总线数组的副本。该模块无法将总线数组转换为非虚拟总线或虚拟总线。要从总线数组中提取总线，请使用 Selector 模块。 | `Signal copy` |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ConversionOutput` |
| **值：** | `'Signal copy'`（默认） | `'Virtual bus'` | `'Nonvirtual bus'` |

**示例：** `set_param(gcb,'ConversionOutput','Virtual
bus')`

### **Data type** — 非虚拟总线数据类型 `Inherit: auto`（默认） | `Bus: <object name>` | `<data type expression>`

指定此模块生成的非虚拟总线的输出数据类型。

- `Inherit: auto` — 从上游模块继承数据类型。例如，从上游 Bus Creator 模块继承 `Simulink.Bus` 对象数据类型。
- `Bus: <object name>` 或 `<data type
  expression>` — 指定与输入总线层次结构匹配的 `Simulink.Bus` 对象。如果上游 Bus Creator 模块指定了总线对象，请指定相同的总线对象。

**数据类型助手**可帮助您设置数据类型属性。要使用**数据类型助手**，请点击显示数据类型助手按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Output** 设置为 `Nonvirtual
bus`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: auto'`（默认） | `'Bus: <object name>'` | `'<data type expression>'` |

**示例：** `set_param(gcb,'OutDataTypeStr','Bus:
myBusObj')`

### **Exclude this block from 'Block reduction' optimization** — 将模块从模块缩减优化中排除的选项 `off`（默认） | `on`

当输入信号的元素占用连续的内存区域时，默认情况下，软件会作为优化从编译模型中消除此模块。有关详细信息，请参阅 Block reduction。

要防止此模块从编译模型中被消除，请选中此参数。

对此参数的更改将在您下次编译模型时生效。

#### 依赖关系

要启用此参数，请将 **Output** 设置为 `Signal copy`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OverrideOpt` |
| **值：** | `'off'`（默认） | `'on'` |

**示例：** `set_param(gcb,'OverrideOpt','on')`
## 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有直通实现。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

在不改变信号值的情况下将信号转换为新类型

Signal Conversion 模块将信号从一种类型转换为另一种类型。要选择要执行的转换类型，请使用 **Output** 参数或以下预配置的 Signal Conversion 模块之一：

- Signal Copy 模块
- To Virtual Bus 模块
- To Nonvirtual Bus 模块
