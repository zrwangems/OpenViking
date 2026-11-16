---
type: simulink-block
title: 'Proof Assumption'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2023b
official_category: 'Objectives and Constraints'
documentation_page: 'proofassumption'
documentation_source_path: 'ref/proofassumption.html'
language: zh-CN
chinese_source: worker-translation
---

# Proof Assumption

## 端口

### 输入

### **Port\_1** — 输入信号，指定为 scalar 或 cell array scalar | cell array

Proof Assumption 模块接受 Simulink 软件支持的所有内置数据类型的信号。有关 Simulink 软件支持的数据类型的讨论，请参阅 Simulink 支持的数据类型。该模块不支持复数输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 输出

### **Port\_1** — 输出信号，返回为 scalar 或 cell array scalar | cell array

Proof Assumption 模块返回 Simulink 软件支持的所有内置数据类型的信号。有关支持的数据类型的详细信息，请参阅 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Enable** — 模块是否启用 `on`（默认） | `off`

指定模块是否启用。如果选中（默认），Simulink Design Verifier 软件在证明模型属性时使用该模块。清除此选项会禁用该模块，也就是说，使 Simulink Design Verifier 软件的行为如同 Proof Assumption 模块不存在。如果未选中此选项，模块在 Simulink 编辑器中显示为灰显。

### **Type** — 模块表现为 Proof Assumption 还是 Test Condition 模块 `on`（默认） | `off`

指定模块表现为 Proof Assumption 还是 Test Condition 模块。选择 `Test Condition` 可将 Proof Assumption 模块转换为 Test Condition 模块。

### **Values** — Proof Assumption scalar（默认） | cell array

使用 **Values** 参数约束测试用例中的信号值。以 MATLAB® cell array 的形式指定标量和区间的任意组合。有关详细信息，请参阅使用参数配置文件。

### **Display values** — 显示 values 参数的内容 `on`（默认） | `off`

指定模块是否在 Simulink 编辑器中显示其 **Values** 参数的内容。

### **Pass through style(show Outport)** — 模块是否在 Simulink 编辑器中显示输出端口 `on`（默认） | `off`

如果选中，模块显示其输出端口，这允许输入信号传递到模块输出。如果未选中，模块隐藏其输出端口并终止输入信号。

**示例：** 以下图形说明了每种情况下模块的外观。

**Pass through style (show Outport)：已选中**

**Pass through style (show Outport)：未选中**

## 所属库

Simulink Design Verifier / Objectives and Constraints

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2007a 中引入**

## 描述

在属性证明模式下运行时，Simulink® Design Verifier™ 软件证明您模型的属性满足指定条件（参见什么是属性证明？）。在此模式下，您可以使用 Proof Assumption 模块为模型中的信号定义假设。**Values** 参数允许您在属性证明期间指定对信号值的约束。模块将指定的 **Values** 参数应用于其输入信号，然后 Simulink Design Verifier 软件证明或反证您模型的属性满足指定条件。

模块的参数对话框还允许您：

- 启用或禁用该假设。
- 指定模块应在 Simulink 编辑器中显示其 **Values** 参数。
- 指定模块应显示其输出端口。

**注意**

Simulink 和 Simulink Coder™ 软件分别在模型仿真和代码生成期间忽略 Proof Assumption 模块。Simulink Design Verifier 软件仅在证明模型属性时使用 Proof Assumption 模块。

您可以通过使用 **Values** 参数在属性证明中约束信号值。有关详细信息，请参阅使用参数配置文件。
