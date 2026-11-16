---
type: simulink-block
title: 'Varying Transfer Function'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'varyingtransferfunction'
documentation_source_path: 'ref/varyingtransferfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Varying Transfer Function

## 端口

### 输入

### **u** — 传递函数输入 scalar

传递函数输入信号。

### **b0, b1, ...** — 分子系数 scalar

传递函数分子系数。系数端口的数量由 **Transfer function order** 参数决定。

对于零馈通传递函数，请清除 **Enable feedthrough** 复选框。清除此复选框会禁用 **b0** 输入端口。*（自 R2023a 起）*

### **a1, a2, ...** — 分母系数 scalar

传递函数分母系数。系数端口的数量由 **Transfer function order** 参数决定。最低阶项的系数 (*a*0) 固定为 1。

*R2023a 之前：分母系数为 `a0`、`a1`、…。系数 *a*N 固定为 1。有关详细信息，请参阅“Varying Transfer Function 模块公式已更改”。*
### 输出

### **y** — 传递函数输出 scalar

传递函数输出信号。

## 参数

### **Transfer function order** — 极点数 N 1（默认值）| 正整数

传递函数阶次 *N*，指定为正整数。此参数决定模块上系数输入端口的数量。

### **Enable feedthrough** — 为馈通项添加输入端口 `on`（默认值）| `off`

*自 R2023a 起*

为具有直接馈通的传递函数启用 **b0** 输入端口。对于零馈通传递函数，请清除此复选框。对于零馈通模型，禁用该端口比向该端口输入零常量在数值上更可靠。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**引入于 R2017b**

### R2023a：Varying Transfer Function 模块公式已更改

在 R2023a 中，Varying Transfer Function 模块的公式已更改，以使多项式系数定义与 Discrete Varying Transfer Function 模块保持一致。在 R2022b 或更早版本中添加了该模块的框图不受此更改影响。

- 在 R2023a 或更高版本中添加到 Simulink® 模型的 Varying Transfer Function 模块，其瞬时传递函数如下：

  H(s)=b0+b1s−1+⋯+bNs−N1+a1s−1+⋯+aNs−N=b0sN+b1sN−1+⋯+bNsN+a1sN−1+⋯+aN.
- 在 R2022b 或更早版本中添加的模块，其瞬时传递函数如下：

  H(s)=b0+b1s+⋯bNsNa0+a1s+⋯aN−1sN−1+sN.

  请注意，用新模块替换 R2023a 之前的模块时，需要重新连接系数输入。例如，考虑以下二阶传递函数：

  H22b(s)=10+9s+8s27+6s+s2.

  使用在 R2022b 或更早版本中添加的模块时，请按下图所示连接该模块。该模块将 `a2` 固定为 1。

  R2022b Varying Transfer Function 模块，其中 Constant 模块连接到系数输入，b0 = 10, a0 = 7, b1 = 9, a1 = 6, b2 = 8

  要在 R2023a 或更高版本中替换该模块，请将传递函数重写为：

  H23a(s)=8+9s−1+10s−21+6s−1+7s−2.

  按图所示重新连接该模块。此时，该模块将 `a0` 固定为 1。

  R2023a Varying Transfer Function 模块，其中 Constant 模块连接到系数输入，b0 = 8, a1 = 6, b1 = 9, a2 = 7, b2 = 10

### R2023a：添加了 Enable feedthrough 复选框

对于零馈通传递函数，请清除 **Enable feedthrough** 复选框。清除此复选框会禁用 **b0** 输入端口。对于零馈通模型，禁用该端口比向该端口输入零常量在数值上更可靠。

## 描述

系数可变的传递函数

此模块实现一个系数可变的连续时间传递函数。其瞬时传递函数为：

H(s)=b0+b1s−1+⋯+bNs−N1+a1s−1+⋯+aNs−N=b0sN+b1sN−1+⋯+bNsN+a1sN−1+⋯+aN.

*N* 为极点数，通过 **Transfer function order** 参数指定。将系数 *b*0、*b*1、…、*bN* 和 *a*1、*a*2、…、*a**N* 的值提供给相应的模块输入端口。

**注意**

上述 *H*(*s*) 表达式仅适用于在 R2023a 或更高版本中添加到模型的 Varying Transfer Function 模块。有关在 R2022b 或更早版本中创建的 Varying Transfer Function 模块的信息，请参阅“Varying Transfer Function 模块公式已更改”。

使用此模块以及 Linear Parameter Varying 库中的其他模块，可实现具有可变参数或系数的常用控制元素。有关详细信息，请参阅“在 Simulink 中对增益调度控制系统进行建模”。

**警告**

避免使传递函数系数依赖于模块输出 **y**。如果存在这种依赖关系，生成的传递函数会导致代数环，因为计算模块输出值需要已知模块输出值。此代数环容易出现不稳定和发散。请尝试用时间 *t* 和模块输入 **u** 来表示系数，而不要使用输出。
