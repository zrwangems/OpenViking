---
type: simulink-block
title: 'Bus Assignment'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'busassignment'
documentation_source_path: '../simulink/slref/busassignment.html'
language: zh-CN
chinese_source: official
---

# Bus Assignment

## 端口

### 输入

### **Bus** — 具有要重新赋值的元素的输入总线 总线

输入虚拟或非虚拟总线可以包含该软件支持的任何数据类型的实数值或复数值元素，包括总线对象、定点数据类型和枚举数据类型。总线也可以包含总线数组。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**复数支持:** 是

### **:=** — 要赋给总线元素的新值 标量 | 向量 | 矩阵 | 数组 | 总线

**要赋值的元素**列表中的每个元素都对应一个赋值端口。端口标签指示对应于该端口的总线元素。对于名为 `signal1` 的元素，端口标签为**:= signal1**。

连接到赋值端口的总线或非总线信号必须具有与对应元素相同的结构体、数据类型和采样时间。要更改一个或多个元素的采样时间，请使用 Rate Transition 模块。有关详细信息，请参阅 Modify Sample Times for Nonvirtual Buses。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**复数支持:** 是
### 输出

### **Bus** — 输出总线 总线

输出虚拟或非虚拟总线包含选定元素所赋予的总线元素值和其他元素的未修改的总线元素值。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**复数支持:** 是

## 参数

要以交互方式编辑 Bus Assignment 模块参数，请双击该模块。

### **总线中的元素** — 输入总线的元素 只读: 元素名称列表

此 参数 为只读。

选择输入总线中要对其进行操作的元素。

元素名称旁边的箭头表示该元素是嵌套总线。要显示嵌套总线中的元素，请点击该箭头。

选择一个或多个元素后，点击：

- **查找** - 查找选定元素的源。软件将打开并突出显示包含元素源的系统。
- **选择** - 将选定元素添加到要赋值的元素列表中。有关详细信息，请参阅**要赋值的元素**。

要过滤输入元素长列表，请在**按名称过滤**框中指定搜索词。请勿将搜索词括在引号内。过滤器执行部分字符串搜索。

要访问过滤选项，请点击**按名称过滤**框右侧的 Show filtering options。

- **启用正则表达式** - 允许使用 MATLAB® 正则表达式来过滤元素名称。例如，要显示其名称以小写字母 `t` 结尾的所有元素（及其直接父级），请在**按名称过滤**框中输入 `t$`。有关详细信息，请参阅 正则表达式。
- **将过滤结果显示为扁平列表** - 以扁平列表形式显示过滤后的元素，该列表使用圆点表示法来反映总线层次结构。默认情况下，输入元素的列表以层次结构树形式显示元素。

要刷新列表以反映对输入总线的修改，请点击**刷新**。

#### 编程用法

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `InputSignals` |
| **值:** | 只读: list of element names in a cell array or cell array of cell arrays |

**示例:** `get_param(gcb,'InputSignals')`

### **要赋值的元素** — 要被赋予新值的总线元素 元素名称列表

对于此列表中的每个元素，模块都有一个对应的赋值端口。端口标签包含对应元素的名称。

要为元素添加赋值端口，请执行以下操作：

1. 从**总线中的元素**列表中选择一个或多个元素。

   如果您从**总线中的元素**列表中选择了多个元素，则您选择它们的顺序将确定它们在**要赋值的元素**列表中的顺序。
2. （可选）指定希望元素出现在**要赋值的元素**列表中的位置。选择希望添加的元素出现在其下方的元素。如果不选择元素，添加的元素会出现在列表的末尾。
3. 点击**选择**。

要更改赋值端口的顺序，请选择列表中的一个元素或多个连续元素，然后点击**上移**或**下移**。当您更改元素顺序时，端口会保持连接。

要删除赋值端口，请在列表中选择对应的元素，然后点击**删除**。

如果列表中的某个元素不在输入总线中，则该元素名称以三个问号 (`???`) 开头。请修改输入总线以包含指定名称的元素，或从列表中删除该元素。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `AssignedSignals` |
| **值:** | `'signal1'` (默认) | comma-separated list of element names in quotes |
| **数据类型:** | `char` | `string` |

**示例:** `set_param(gcb,'AssignedSignals','sine,chirp')`

## 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**数据类型支持**

此模块支持使用以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 布尔 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量  向量  矩阵 | 是 | 半精度  单精度  双精度 | 是 | 是 | 是 |

**HDL 建模规范**

有关最佳做法，请参阅：

- Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)

**限制和注意事项**

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅Buses (HDL Coder)。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2006a 之前推出**

## 描述

为指定的总线元素赋予新值

Bus Assignment 模块为选定总线元素赋予新值。使用 Bus Assignment 模块更改元素值，而无需提取元素并用所需元素重新组合为总线。Bus Assignment 模块简化了总线的更新，以反映在一个单独的组件（如子系统或引用模型）中发生的处理。

Bus Assignment 模块将连接到赋值端口的元素赋给连接到总线输入端口的总线的指定元素。该模块将替换先前分配给这些元素的元素。此更改不影响总线的构成。此更改仅影响元素的值。未替换的元素不受其他元素替换的影响。

被赋值的元素可以是非总线信号或总线（包括总线数组），只要它们是输入总线的元素即可。新值必须与原始总线中元素的属性匹配。

默认情况下，软件会修复 Bus Assignment 模块中由于上游总线层次结构发生变化而失效的选择。如果修复修改了模型，系统会向您发送警告通知。为防止软件自动进行这些修复，请将**修复总线选择**配置参数设置为**报错但不修复**。
