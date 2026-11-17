---
type: simulink-block
title: 'Discrete Varying Transfer Function'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'discretevaryingtransferfunction'
documentation_source_path: 'ref/discretevaryingtransferfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Varying Transfer Function

## 端口
```yaml
ports:
- name: u
  summary: 传递函数输入 标量
  direction: input
- name: b0, b1, ...
  summary: 分子系数 标量
  direction: input
- name: a1, a2, ...
  summary: 分母系数 标量
  direction: input
- name: y
  summary: 传递函数输出 标量
  direction: output
```

### 输入

### **u** — 传递函数输入 标量

传递函数输入信号。

### **b0, b1, ...** — 分子系数 标量

传递函数分子系数。系数端口的数量由 **Transfer function order** 参数决定。

对于零直通传递函数，清除 **Enable feedthrough** 复选框。清除此复选框将禁用 **b0** 输入端口。*（自 R2023a 起）*

### **a1, a2, ...** — 分母系数 标量

传递函数分母系数。系数端口的数量由 **Transfer function order** 参数决定。
### 输出

### **y** — 传递函数输出 标量

传递函数输出信号。
## 参数
```yaml
parameters:
- name: Transfer function order
  summary: 极点数量 1（默认）| 正整数
  group: ''
- name: Enable feedthrough
  summary: 为直通项添加输入端口 on（默认）| off
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 –1（默认）| 正标量
  group: ''
```

### **Transfer function order** — 极点数量 1（默认）| 正整数

传递函数（极点数量），指定为正整数。此参数决定模块上系数输入端口的数量。

### **Enable feedthrough** — 为直通项添加输入端口 `on`（默认）| `off`

*自 R2023a 起*

为具有直接直通的传递函数启用 **b0** 输入端口。对于零直通传递函数，清除此复选框。对于零直通模型，禁用该端口比向端口馈入零常数在数值上更可靠。

### **Sample time (-1 for inherited)** — 模块采样时间 –1（默认）| 正标量

模块采样时间，指定为 –1（继承采样时间）或正标量值。
## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2017b 中引入**

### R2023a：添加了 Enable feedthrough 复选框

对于零直通传递函数，清除 **Enable feedthrough** 复选框。清除此复选框将禁用 **b0** 输入端口。对于零直通模型，禁用该端口比向端口馈入零常数在数值上更可靠。

## 描述

具有可变系数的离散时间传递函数

此模块实现具有可变系数的离散时间传递函数。瞬时传递函数由下式给出：

H(z)=b0+b1/z+⋯+bN/zN1+a1/z+⋯+aN/zN，

其中 *N* 为极点数量，由 **Transfer function order** 参数指定。将系数 *a*1、…、*aN* 和 *b*0、*b*1、…、*bN* 的值馈入相应的模块输入端口。

使用此模块以及 Linear Parameter Varying 库中的其他模块来实现具有可变参数或系数的常见控制元件。有关详细信息，请参阅 Model Gain-Scheduled Control Systems in Simulink。

**注意**

避免使传递函数系数依赖于模块输出 **y**。如果您有这样的依赖关系，所得到的传递函数会导致代数环，因为计算模块输出值需要知道模块输出值。此代数环容易产生不稳定和发散。相反，请尝试将系数表示为时间 *t* 和模块输入 **u** 的函数。
