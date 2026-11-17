---
type: simulink-block
title: 'Bus Assignment'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'busassignment'
documentation_source_path: 'slref/busassignment.html'
language: zh-CN
chinese_source: worker-translation
---

# Bus Assignment

## 端口
```yaml
ports:
- name: Bus
  summary: 带有要重新分配元素的输入总线 bus
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | string
- name: :=
  summary: 要分配给总线元素的新值 标量 | 向量 | 矩阵 | 数组 | 总线
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | string
- name: Bus
  summary: 输出总线 bus
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | string
```

### 输入

### **Bus** — 带有要重新分配元素的输入总线 bus

输入虚拟或非虚拟总线可以包含具有软件支持的任何数据类型的实数或复数值的元素，包括总线对象、定点数据类型和枚举数据类型。总线还可以包含总线数组。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**复数支持：** 是

### **:=** — 要分配给总线元素的新值 标量 | 向量 | 矩阵 | 数组 | 总线

**Elements that are being assigned** 列表中的每个元素接收一个赋值端口。端口标签指示与该端口对应的总线元素。对于名为 `signal1` 的元素，端口标签为 **:= signal1**。

连接到赋值端口的总线或非总线信号必须具有与对应元素相同的结构、数据类型和采样时间。要更改一个或多个元素的采样时间，请使用 Rate Transition 模块。有关详细信息，请参阅 Modify Sample Times for Nonvirtual Buses。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**复数支持：** 是
### 输出

### **Bus** — 输出总线 bus

输出虚拟或非虚拟总线包含所选元素的已赋值总线元素值以及其他元素的未修改总线元素值。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Elements in the bus
  summary: 输入总线的元素 只读：元素名称列表
  group: ''
  block_parameter: InputSignals
  values: 只读：元胞数组或元胞数组的元胞数组中的元素名称列表
- name: Elements that are being assigned
  summary: 要赋予新值的总线元素 元素名称列表
  group: ''
  block_parameter: AssignedSignals
  values: '''signal1''（默认）| 以逗号分隔的带引号的元素名称列表'
```

要交互式编辑 Bus Assignment 模块参数，请双击该模块。

### **Elements in the bus** — 输入总线的元素 只读：元素名称列表

此参数为只读。

选择输入总线中的元素以对其进行操作。

元素名称旁边的箭头表示该元素是嵌套总线。要显示嵌套总线中的元素，请单击箭头。

选中一个或多个元素后，单击：

- **Find** — 查找所选元素的源。软件将打开并高亮显示包含该元素源的系统。
- **Select** — 将所选元素添加到要赋值的元素列表中。有关详细信息，请参阅 **Elements that are being assigned**。

要筛选较长的输入元素列表，请在 **Filter by name** 框中指定搜索词。不要将搜索词用引号括起来。筛选器执行部分字符串搜索。

要访问筛选选项，请单击 **Filter by name** 框右侧的 Show filtering options。

- **Enable regular expression** — 启用使用 MATLAB® 正则表达式来筛选元素名称。例如，要显示所有名称以小写 `t` 结尾的元素及其直接父级，请在 **Filter by name** 框中输入 `t$`。有关详细信息，请参阅 Regular Expressions。
- **Show filtered results as a flat list** — 以扁平列表显示筛选后的元素，该列表使用点表示法反映总线层次结构。默认情况下，输入元素列表以层次树的形式显示元素。

要刷新列表以反映对输入总线的修改，请单击 **Refresh**。

#### 编程使用

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InputSignals` |
| **值**：| 只读：元胞数组或元胞数组的元胞数组中的元素名称列表 |

**Example:** `get_param(gcb,'InputSignals')`

### **Elements that are being assigned** — 要赋予新值的总线元素 元素名称列表

对于此列表中的每个元素，模块都有一个赋值端口。端口标签包含对应元素的名称。

要为元素添加赋值端口：

1. 从 **Elements in the bus** 列表中选择一个或多个元素。

   如果从 **Elements in the bus** 列表中选择多个元素，则选择它们的顺序决定了它们在 **Elements that are being assigned** 列表中的顺序。
2. 可选地，指定希望元素在 **Elements that are being assigned** 列表中显示的位置。选择希望添加的元素显示在其下方的元素。如果未选择元素，则添加的元素显示在列表末尾。
3. 单击 **Select**。

要更改赋值端口的顺序，请在列表中选择一个元素或多个连续元素，然后单击 **Up** 或 **Down**。更改元素顺序时，端口连接性保持不变。

要移除赋值端口，请在列表中选择相应的元素，然后单击 **Remove**。

如果列表中的某个元素不在输入总线中，则该元素名称以三个问号（`???`）开头。请修改输入总线以包含指定名称的元素，或从列表中移除该元素。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `AssignedSignals` |
| **值**：| `'signal1'`（默认）| 以逗号分隔的带引号的元素名称列表 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'AssignedSignals','sine,chirp')`
## 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际的数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**数据类型支持**

此模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 布尔 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes |

**HDL 建模指南**

有关最佳实践，请参阅：

- 使用总线提高模型可读性并生成 HDL 代码（HDL Coder）

**限制和注意事项**

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅 Buses (HDL Coder)。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际的数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2006a 之前引入**

## 描述

为指定的总线元素赋予新值

Bus Assignment 模块为选定的总线元素赋予新值。使用 Bus Assignment 模块可以在不提取元素并使用所需元素重新组装总线的情况下更改元素值。Bus Assignment 模块简化了更新总线以反映在单独组件（如子系统或引用模型）中发生的处理过程。

Bus Assignment 模块将连接到赋值端口的元素分配给连接到总线输入端口的总线的指定元素。该模块替换先前分配给这些元素的元素。该更改不影响总线的组成。该更改仅影响元素的值。未被替换的元素不受其他元素替换的影响。

要赋值的元素可以是非总线信号或总线（包括总线数组），只要它们是输入总线的元素即可。新值必须与原始总线中元素的属性匹配。

默认情况下，软件会修复由于上游总线层次结构更改而导致的 Bus Assignment 模块的损坏选择。当修复修改模型时，会发出警告通知您。要阻止软件自动进行这些修复，请将 **Repair bus selections** 配置参数设置为 `Error without repair`。
