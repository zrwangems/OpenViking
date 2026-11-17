---
type: simulink-block
title: 'Mux'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'mux'
documentation_source_path: '../simulink/slref/mux.html'
language: zh-CN
chinese_source: worker-translation
---

# Mux

## 端口

### 输入

### **Port\_1** — 要包含在 mux 信号中的输入信号 标量 | 向量

要包含在 mux 信号中的输入信号，指定为标量或向量。

Mux 模块的输入信号可以是标量和向量的任意组合，但它们必须具有相同的数据类型和复数性，或者是函数调用信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`
**复数支持：** 是
### 输出

### **Port\_1** — 输出 mux 信号 向量

由组合输入信号构成的输出 mux 信号，以向量形式返回。

输出 mux 信号的元素顺序取决于输入信号的端口顺序。有关各种模块方向的端口顺序说明，请参阅 Identify Port Location on Rotated or Flipped Block。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

## 参数

### **Number of inputs** — 输入信号的数量 2（默认）| 标量 | 向量 | 元胞数组 | 以逗号分隔的信号名称列表

输入信号的数量，指定为标量、向量、元胞数组或以逗号分隔的信号名称列表。其中一些格式允许您指定信号名称和大小，如下表所述。

| 格式 | 模块行为 |
| --- | --- |
| 标量 | Mux 模块的输入数量。使用此格式时，模块接受任意大小的标量或向量信号。软件为每个输入分配名称 `signalN`，其中 `N` 是输入端口编号。 |
| 向量 | 向量的长度指定输入数量。每个元素指定对应输入的大小。正值指定对应端口只能接受该大小的向量。例如，`[2 3]` 指定两个输入端口，大小分别为 `2` 和 `3`。如果输入信号宽度与预期宽度不匹配，将显示错误消息。值为 `-1` 指定对应端口可以接受任意大小的标量或向量。 |
| 元胞数组 | 元胞数组的长度指定输入数量。每个元胞的值指定对应输入的大小。标量值 `N` 指定大小为 `N` 的向量。值为 `-1` 表示对应端口可以接受任意大小的标量或向量信号。 |
| 以逗号分隔的信号名称列表 | 以逗号分隔的信号名称列表。软件将每个名称分配给对应的端口和信号。例如，如果您输入 `position,velocity`，则 Mux 模块有两个输入，分别命名为 `position` 和 `velocity`。 |

不支持指定非 double 值，例如 `single(3)`。

#### 提示

如果您为 **Number of inputs** 参数指定标量，并且所有输入端口都已连接，当您在 Mux 模块输入侧附近绘制新的信号线时，软件会添加一个端口并更新该参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Inputs` |
| **值：** | `'2'`（默认）| 带引号的标量 | 带引号的向量 | 带引号的元胞数组 | 带引号的以逗号分隔的信号名称列表 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,'Inputs','5')`

**示例：** `set_param(gcb,'Inputs','[2 3]')`

**示例：** `set_param(gcb,'Inputs','{3}')`

**示例：** `set_param(gcb,'Inputs','position,velocity')`

### **Display option** — 模块图标外观 `bar`（默认）| `signals` | `none`

模块图标外观，指定为 `bar`、`signals` 或 `none`。

- `bar` — 不显示文本
- `signals` — 显示输入信号名称
- `none` — 显示模块类型（Mux）

根据需要调整模块大小，以使文本适合模块图标。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DisplayOption` |
| **值：** | `'bar'`（默认）| `'signals'` | `'none'` |

**示例：** `set_param(gcb,'DisplayOption','signals')`

## 所属库

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际的数据类型或功能支持取决于模块实现。

为提高生成代码的效率，请使用 Vector Concatenate 模块代替 Mux 模块。Vector Concatenate 模块创建非虚拟向量。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

HDL 代码生成不支持总线。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际的数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2006a 之前推出**

## 描述

将具有相同数据类型和复数性的输入信号合并为虚拟向量

Mux 模块将具有相同数据类型和复数性的输入合并为虚拟向量。您可以使用多个 Mux 模块分阶段创建 mux 信号，但结果与使用单个 Mux 模块一样是扁平的。

理想情况下，使用 Mux 模块仅对函数调用信号进行分组。

虽然 Mux 模块可以从具有相同数据类型和复数性的信号创建虚拟向量，但其他模块以提供更多灵活性和效率的方式对信号进行分组。

- 要对信号或消息进行分组，请使用 Bus Creator 模块代替 Mux 模块。Bus Creator 模块创建虚拟总线，使您可以灵活地对不同数据类型和复数性的元素进行分组。虚拟总线还允许您按名称而不是按索引访问元素。如果模块需要虚拟向量而不是虚拟总线，模型编译会将总线转换为向量。
- 要串联输入信号，请使用 Vector Concatenate 模块代替 Mux 模块。Vector Concatenate 模块创建非虚拟向量，从而提高生成代码的效率。

有关 mux 信号、虚拟总线和串联信号的比较，请参阅 Explore Composite Interfaces。
