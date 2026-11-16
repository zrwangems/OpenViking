---
type: simulink-block
title: 'Varying Transfer Function'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Gain Scheduling / Continuous Time'
documentation_page: 'varyingtransferfunction'
documentation_source_path: '../control/ref/varyingtransferfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Varying Transfer Function

## 端口

### 输入

### **u** — 传递函数输入标量

传递函数输入信号。

### **b0, b1, ...** — 分子系数标量

传递函数分子系数。系数端口的数量由 **传递函数阶数** 参数确定。

对于零直通传递函数，清除 **启用直通** 复选框。清除此复选框会禁用 **b0** 输入端口。*(自 R2023a 起)*

### **a1, a2, ...** — 分母系数标量

传递函数分母系数。系数端口的数量由 **传递函数阶数** 参数确定。最低阶项 (*a*0) 的系数固定为 1。

*R2023a 之前：分母系数为 `a0`、`a1`、…。系数 *a*N 固定为 1。有关详细信息，请参阅 Varying Transfer Function 模块公式已更改。*

### 输出

### **y** — 传递函数输出标量

传递函数输出信号。

## 参数

### **传递函数阶数** — 极点数 N 1（默认）| 正整数

传递函数阶数 *N*，指定为正整数。此参数确定模块上系数输入端口的数量。

### **启用直通** — 为直通项添加输入端口 `on`（默认）| `off`

*自 R2023a 起*

为具有直通的传递函数启用 **b0** 输入端口。对于零直通传递函数，清除此复选框。对于零直通模型，禁用该端口比向该端口馈入零常量在数值上更可靠。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2023a: Varying Transfer Function 模块公式已更改

在 R2023a 中，更改了 Varying Transfer Function 模块公式，以使多项式系数定义与 Discrete Varying Transfer Function 模块一致。在 R2022b 或更早版本中已将模块添加到的框图不受此更改影响。

- 在 R2023a 或更高版本中添加到 Simulink® 模型的 Varying Transfer Function 模块具有以下瞬时传递函数：

  H(s)=b0+b1s−1+⋯+bNs−N1+a1s−1+⋯+aNs−N=b0sN+b1sN−1+⋯+bNsN+a1sN−1+⋯+aN.
- 在 R2022b 或之前添加的模块具有以下瞬时传递函数：

  H(s)=b0+b1s+⋯bNsNa0+a1s+⋯aN−1sN−1+sN.

  请注意，将 R2023a 之前的模块替换为新模块需要重新连接系数输入。例如，考虑以下二阶传递函数：

  H22b(s)=10+9s+8s27+6s+s2.

  使用在 R2022b 或之前添加的模块时，可按下图所示连接模块。该模块将 `a2` 固定为 1。

  R2022b Varying Transfer Function 模块，Constant 模块连接到系数输入，b0 = 10, a0 = 7, b1 = 9, a1 = 6, b2 = 8

  要在 R2023a 或之后替换该模块，请按如下方式重写传递函数：

  H23a(s)=8+9s−1+10s−21+6s−1+7s−2.

  按所示重新连接模块。现在，该模块将 `a0` 固定为 1。

  R2023a Varying Transfer Function 模块，Constant 模块连接到系数输入，b0 = 8, a1 = 6, b1 = 9, a2 = 7, b2 = 10

### R2023a: 添加了启用直通复选框

对于零直通传递函数，清除 **启用直通** 复选框。清除此复选框会禁用 **b0** 输入端口。对于零直通模型，禁用该端口比向该端口馈入零常量在数值上更可靠。

## 描述

具有变系数的传递函数

此模块实现具有变系数的连续时间传递函数。瞬时传递函数由下式给出：

H(s)=b0+b1s−1+⋯+bNs−N1+a1s−1+⋯+aNs−N=b0sN+b1sN−1+⋯+bNsN+a1sN−1+⋯+aN.

*N* 是极点数，由 **传递函数阶数** 参数指定。将系数 *b*0, *b*1,…, *bN* 和 *a*1, *a*2,…, *a**N* 的值馈送到对应的模块输入端口。

**注意**

上述 *H*(*s*) 表达式仅适用于在 R2023a 或更高版本中添加至模型的 Varying Transfer Function 模块。有关在 R2022b 或更早版本中创建的 Varying Transfer Function 模块的信息，请参阅 Varying Transfer Function 模块公式已更改。

使用此模块以及 Linear Parameter Varying 库中的其他模块来实现具有可变参数或系数的常见控制元件。有关详细信息，请参阅在 Simulink 中对增益调度控制系统建模。

**小心**

避免使传递函数系数依赖于模块输出 **y**。如果存在这种依赖关系，则所得传递函数会导致代数环，因为计算模块输出值需要知道模块输出值。此代数环容易出现不稳定和发散。不要使用输出，而是尝试用时间 *t* 和模块输入 **u** 来表示系数。
