---
type: simulink-block
title: 'Discrete Varying Transfer Function'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Gain Scheduling / Discrete Time'
documentation_page: 'discretevaryingtransferfunction'
documentation_source_path: '../control/ref/discretevaryingtransferfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Varying Transfer Function

## 端口

### 输入

### **u** — 传递函数输入标量

传递函数输入信号。

### **b0, b1, ...** — 分子系数标量

传递函数分子系数。系数端口数量由 **Transfer function order** 参数确定。

对于零直通传递函数，清除 **Enable feedthrough** 复选框。清除此复选框会禁用 **b0** 输入端口。*(自 R2023a 起)*

### **a1, a2, ...** — 分母系数标量

传递函数分母系数。系数端口数量由 **Transfer function order** 参数确定。
### 输出

### **y** — 传递函数输出标量

传递函数输出信号。

## 参数

### **Transfer function order** — 极点数 1（默认）| 正整数

传递函数（极点数），指定为正整数。此参数确定模块上系数输入端口的数量。

### **Enable feedthrough** — 为直通项添加输入端口 `on`（默认）| `off`

*自 R2023a 起*

为具有直接直通的传递函数启用 **b0** 输入端口。对于零直通传递函数，清除此复选框。对于零直通模型，禁用该端口比向该端口馈入零常量在数值上更可靠。

### **Sample time (-1 for inherited)** — 模块采样时间 –1（默认）| 正标量

模块采样时间，指定为 –1（继承采样时间）或正标量值。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2017b 中引入**

### R2023a：添加了 Enable feedthrough 复选框

对于零直通传递函数，清除 **Enable feedthrough** 复选框。清除此复选框会禁用 **b0** 输入端口。对于零直通模型，禁用该端口比向该端口馈入零常量在数值上更可靠。

## 描述

带可变系数的离散时间传递函数

此模块实现带可变系数的离散时间传递函数。瞬时传递函数由下式给出：

H(z)=b0+b1/z+⋯+bN/zN1+a1/z+⋯+aN/zN,

其中 *N* 是极点数，用 **Transfer function order** 参数指定。将系数 *a*1、…、*aN* 和 *b*0、*b*1、…、*bN* 的值馈入对应的模块输入端口。

使用此模块以及 Linear Parameter Varying 库中的其他模块来实现具有可变参数或系数的常见控制元素。有关详细信息，请参阅“在 Simulink 中对增益调度控制系统建模”。

**注意**

避免使传递函数系数依赖模块输出 **y**。如果存在这种依赖关系，则所得传递函数会导致代数环，因为计算模块输出值需要知道模块输出值。此代数环容易不稳定和发散。相反，尝试用时间 *t* 和模块输入 **u** 表示系数。
