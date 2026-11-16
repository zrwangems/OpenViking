---
type: simulink-block
title: 'Test Condition'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Objectives and Constraints'
documentation_page: 'testcondition'
documentation_source_path: 'ref/testcondition.html'
language: zh-CN
chinese_source: official
---

# Test Condition

## 端口

### 输入

### **Port\_1** — 输入信号指定为标量或元胞数组 标量 | 元胞数组

Test Condition 模块接受 Simulink 软件支持的所有内置数据类型的信号。有关支持的数据类型的更多信息，请参阅 Simulink 支持的数据类型。该模块不支持复杂的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号以标量或元胞数组返回 标量 | 元胞数组

Test Condition 模块返回 Simulink 软件支持的所有内置数据类型的信号。有关支持的数据类型的更多信息，请参阅 Simulink 支持的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **启用** — 是否启用模块 `on` (默认) | `off`

选择此参数来为模型生成测试。清除此选项将禁用模块。如果清除此选项，则该模块在 Simulink 编辑器中将显示为灰色。

### **类型** — 该模块是否表现为测试条件或 Proof Assumption 模块 `Test Condition` (默认) | `Assumption`

指定该模块是否表现为测试条件或 Proof Assumption 模块。选择**假设**将 Test Condition 模块转换为 Proof Assumption 模块。

### **值** — 测试条件 标量 | 元胞数组

使用**值**参数来约束测试用例中的信号值。以 MATLAB® 元胞数组的形式指定标量和区间的任意组合。有关详细信息，请参阅 使用参数配置文件设置参数。

或者，您可以使用 `Sldv.Point` 构造函数指定标量值，该构造函数接受单个值作为其参量。您还可以使用 `Sldv.Interval` 构造函数指定间隔，该构造函数需要两个输入参量，一个用于间隔的下限，一个用于区间的上限。

例如，**值**参数

```
{0, [1, 3]}
```

指定：

- `0` - 标量
- `[1, 3]` - 闭区间

**值**参数

```
{Sldv.Interval(0, 1, '[)'), Sldv.Point(1)}
```

指定：

- `Sldv.Interval(0, 1, '[)')` - 右开区间[0, 1)
- `Sldv.Point(1)` - 标量

如果为 Test Condition 模块指定多个标量和间隔，则 Simulink Design Verifier™ 软件在生成测试用例时使用逻辑或运算将它们组合在一起。因此，如果任何单个标量或区间得到满足，软件就会认为整个测试条件得到满足。

在单个标量或区间内，使用逻辑“与”运算生成测试条件。在这种情况下，所有信号都必须满足约束，以便输入满足条件。

例如，考虑一个二维开区间：

```
Sldv.Interval([-5 -5],[5 2],'()')
```

零向量 `[0 0]` 满足条件，因为零元素位于区间 `-5` 到 `5` 和 `-5` 到 `2` 内。

向量 `[0 3]` 不满足条件，因为第二个元素 3 超出了区间 `-5` 到 `2` 的范围。

### **显示值** — 显示 values 参数的内容 `on` (默认) | `off`

指定模块是否在 Simulink 编辑器中显示其**值**参数的内容。

### **直通模式(显示输出端口)** — 模块是否在 Simulink 编辑器中显示输出端口 `on` (默认) | `off`

如果选中，该模块将显示其输出端口，这允许输入信号传递到模块输出。如果未选择，该模块将隐藏其输出端口并终止输入信号。

**示例:** 下图说明了每种情况下模块的外观。

**直通模式：已选择**

**直通模式：已清除**

## 所属库

Simulink Design Verifier / Objectives and Constraints

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和合成逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **无 HDL** | 不要为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制不相关逻辑的移除。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

## 版本历史

**在 R2007a 中推出**

## 描述

限制测试用例中的信号值

Test Condition 模块定义了在测试生成模式下运行的模型中的信号的测试条件。（见）。使用**值**参数指定信号值的约束。该模块将指定的**值**参数应用于其输入信号并尝试生成测试用例。

您可以使用该模块来：

- 启用或禁用该条件。
- 指定模块是否应在 Simulink® 编辑器中显示其**值**参数。
- 指定该模块是否应显示其输出端口。

当您使用 Simulink 和 Simulink Coder™ 生成代码时，Test Condition 模块将被忽略。Test Condition 模块在模型仿真期间不会修改信号，而仅使用该信号来生成测试条件。
