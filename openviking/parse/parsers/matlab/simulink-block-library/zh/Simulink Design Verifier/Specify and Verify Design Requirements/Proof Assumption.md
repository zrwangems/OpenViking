---
type: simulink-block
title: 'Proof Assumption'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Specify and Verify Design Requirements'
documentation_page: 'proofassumption'
documentation_source_path: 'ref/proofassumption.html'
language: zh-CN
chinese_source: official
---

# Proof Assumption

## 端口

### 输入

### **Port\_1** — 输入信号指定为标量或元胞数组 标量 | 元胞数组

Proof Assumption 模块接受 Simulink 软件支持的所有内置数据类型的信号。有关 Simulink 软件支持的数据类型的讨论，请参阅Simulink 支持的数据类型。该模块不支持复杂的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号以标量或元胞数组返回 标量 | 元胞数组

Proof Assumption 模块返回 Simulink 软件支持的所有内置数据类型的信号。有关支持的数据类型的更多信息，请参阅 Simulink 支持的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **启用** — 是否启用模块 `on` (默认) | `off`

指定该模块是否启用。如果选中（默认），Simulink Design Verifier 软件在证明模型的属性时使用该模块。清除此选项将禁用该模块，也就是说，导致 Simulink Design Verifier 软件的行为就像 Proof Assumption 模块不存在一样。如果未选择此选项，则该模块将在 Simulink 编辑器中显示为灰色。

### **类型** — 该模块是否表现为证明假设或 Test Condition 模块 `on` (默认) | `off`

指定该模块是否表现为 Proof Assumption 或 Test Condition 模块。选择**测试条件**将 Proof Assumption 模块转换为 Test Condition 模块。

### **值** — Proof Assumption 标量 (默认) | 元胞数组

使用**值**参数来约束测试用例中的信号值。以 MATLAB® 元胞数组的形式指定标量和区间的任意组合。有关详细信息，请参阅 使用参数配置文件设置参数。

### **显示值** — 显示 values 参数的内容 `on` (默认) | `off`

指定模块是否在 Simulink 编辑器中显示其**值**参数的内容。

### **直通模式(显示输出端口)** — 模块是否在 Simulink 编辑器中显示输出端口 `on` (默认) | `off`

如果选中，该模块将显示其输出端口，这允许输入信号传递到模块输出。如果未选择，该模块将隐藏其输出端口并终止输入信号。

**示例:** 下图说明了每种情况下模块的外观。

**直通样式（显示输出端口）：已选择**

**直通样式（显示输出端口）：取消选定**

## 所属库

Simulink Design Verifier / Objectives and Constraints

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2007a 中推出**

## 描述

在证明模型属性时约束信号值

在属性证明模式下运行时，Simulink® Design Verifier™ 软件会证明您的模型的属性满足指定的准则（请参阅 使用 Simulink Design Verifier 证明模型属性）。在这种模式下，您可以使用 Proof Assumption 模块来定义模型中信号的假设。**值**参数允许您在属性证明期间指定对信号值的约束。该模块将指定的**值**参数应用于其输入信号，并且 Simulink Design Verifier 软件证明或反驳您的模型的属性是否满足指定的准则。

该模块的参数对话框还允许您：

- 启用或禁用假设。
- 指定该模块应在 Simulink 编辑器中显示其**值**参数。
- 指定该模块应显示其输出端口。

**注意**

Simulink 和 Simulink Coder™ 软件分别在模型仿真和代码生成期间忽略 Proof Assumption 模块。Simulink Design Verifier 软件仅在证明模型属性时使用 Proof Assumption 模块。

您可以使用**值**参数来约束属性证明中的信号值。有关详细信息，请参阅 使用参数配置文件设置参数。
