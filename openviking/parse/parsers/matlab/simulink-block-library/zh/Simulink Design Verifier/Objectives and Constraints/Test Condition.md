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
chinese_source: worker-translation
---

# Test Condition

## 端口

### 输入

### **Port\_1** — 输入信号，指定为标量或元胞数组 标量 | 元胞数组

Test Condition 模块接受 Simulink 软件支持的所有内置数据类型的信号。有关支持的数据类型的详细信息，请参阅 Simulink 支持的数据类型。该模块不支持复数输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号，以标量或元胞数组形式返回 标量 | 元胞数组

Test Condition 模块返回 Simulink 软件支持的所有内置数据类型的信号。有关支持的数据类型的详细信息，请参阅 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Enable** — 模块是否启用 `on`（默认）| `off`

选择此参数可为模型生成测试。清除此选项将禁用该模块。如果清除此选项，该模块在 Simulink Editor 中将显示为灰显状态。

### **Type** — 模块表现为 Test Condition 还是 Proof Assumption 模块 `Test Condition`（默认）| `Assumption`

指定模块表现为 Test Condition 还是 Proof Assumption 模块。选择 `Assumption` 可将 Test Condition 模块转换为 Proof Assumption 模块。

### **Values** — 测试条件 标量 | 元胞数组

使用 **Values** 参数来约束测试用例中的信号值。以 MATLAB® 元胞数组的形式指定标量和区间的任意组合。有关详细信息，请参阅 Set Parameters Using Parameter Configuration File。

或者，您可以使用 `Sldv.Point` 构造函数指定标量值，该构造函数接受单个值作为其参数。您还可以使用 `Sldv.Interval` 构造函数指定区间，该构造函数需要两个输入参数，一个用于区间的下界，一个用于区间的上界。

例如，**Values** 参数

```
{0, [1, 3]}
```

指定：

- `0` — 一个标量
- `[1, 3]` — 一个闭区间

**Values** 参数

```
{Sldv.Interval(0, 1, '[)'), Sldv.Point(1)}
```

指定：

- `Sldv.Interval(0, 1, '[)')`
  — 右开区间 [0, 1)
- `Sldv.Point(1)` — 一个标量

如果您为 Test Condition 模块指定多个标量和区间，Simulink
Design Verifier™ 软件在生成测试用例时会使用逻辑 OR 运算将它们组合起来。因此，只要
任何
单个标量或区间得到满足，软件就会认为整个测试条件得到满足。

在单个标量或区间内，测试条件通过逻辑 AND 运算生成。在这种情况下，所有
信号都必须满足
约束条件，输入才能满足该条件。

例如，考虑一个二维开区间：

```
Sldv.Interval([-5 -5],[5 2],'()')
```

零向量 `[0 0]` 满足该条件，因为零元素位于区间 `-5` 到
`5` 以及 `-5` 到
`2` 之内。

向量 `[0 3]` 不满足该条件，因为第二个元素 3 落在区间 `-5` 到
`2` 之外。

### **Display values** — 是否显示 values 参数的内容 `on`（默认）| `off`

指定模块是否在 Simulink Editor 中显示其
**Values** 参数的内容。

### **Pass through style (show Outport)** — 模块是否在 Simulink Editor 中显示输出端口 `on`（默认）| `off`

如果选中，模块将显示其输出端口，允许输入信号传递到模块输出。如果未选中，模块将隐藏其输出端口并终止输入信号。

**示例：** 以下图形说明了每种情况下模块的外观。

**Pass through style：选中**

**Pass through style：清除**

## 所属库

Simulink Design Verifier / Objectives and Constraints

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

## 版本历史

**在 R2007a 中引入**

## 描述

在测试用例中约束信号值

Test Condition 模块为在测试生成模式下运行的模型中的信号定义测试条件。（请参阅 。）使用 **Values** 参数指定对信号值的约束。该模块将指定的 **Values** 参数应用于其输入信号，并尝试生成测试用例。

您可以使用该模块来：

- 启用或禁用该条件。
- 指定该模块是否应在 Simulink® Editor 中显示其 **Values** 参数。
- 指定该模块是否应显示其输出端口。

当您使用 Simulink 和 Simulink Coder™ 生成代码时，Test Condition 模块会被忽略。Test Condition 模块在模型仿真期间不会修改信号，仅使用该信号来生成测试条件。
