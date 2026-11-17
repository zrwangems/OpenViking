---
type: simulink-block
title: 'Mutual Inductor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'mutualinductor'
documentation_source_path: 'ref/mutualinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Mutual Inductor

## 端口
```yaml
ports:
- name: 1+
  summary: 一次绕组正极端子 electrical
  direction: conserving
- name: 1-
  summary: 一次绕组负极端子 electrical
  direction: conserving
- name: 2+
  summary: 二次绕组正极端子 electrical
  direction: conserving
- name: 2-
  summary: 二次绕组负极端子 electrical
  direction: conserving
```

### 守恒端口

### **1+** — 一次绕组正极端子 electrical

与一次绕组正极端子关联的电气守恒端口。

### **1-** — 一次绕组负极端子 electrical

与一次绕组负极端子关联的电气守恒端口。

### **2+** — 二次绕组正极端子 electrical

与二次绕组正极端子关联的电气守恒端口。

### **2-** — 二次绕组负极端子 electrical

与二次绕组负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Inductance L1
  summary: 一次绕组的自感 10 H（默认）| 正标量
  group: ''
- name: Inductance L2
  summary: 二次绕组的自感 0.1 H（默认）| 正标量
  group: ''
- name: Perfect coupling – no leakage
  summary: 使用理想互感 Off（默认）| On
  group: ''
- name: Coefficient of coupling
  summary: 互感的耦合系数 0.9（默认）| (0,1) 范围内的标量
  group: ''
```

### **Inductance L1** — 一次绕组的自感 `10 H`（默认）| 正标量

一次绕组的自感。

### **Inductance L2** — 二次绕组的自感 `0.1 H`（默认）| 正标量

二次绕组的自感。

### **Perfect coupling – no leakage** — 使用理想互感 `Off`（默认）| `On`

如果选中此复选框，模块会将耦合系数设置为 1，并将漏磁阻设置为 0。在这种情况下，模块表示无漏磁、无快速极点的理想互感，同时保持正确的低频行为，阻断直流。

### **Coefficient of coupling** — 互感的耦合系数 `0.9`（默认）| (0,1) 范围内的标量

耦合系数，用于定义互感。参数值应大于零且小于 1。避免将此参数设置为接近 1 的值（例如 0.9999），因为这会引入快速仿真动态。

#### 依赖关系

要启用此参数，请清除 **Perfect coupling – no leakage** 复选框。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

电气系统中的互感

Mutual Inductor 模块对互感进行建模，由以下方程描述：

V1=L1dI1dt+MdI2dt

V2=L2dI2dt+MdI1dt

M=kL1·L2

其中：

- *V1* 是一次绕组两端的电压。
- *V2* 是二次绕组两端的电压。
- *I1* 是流入一次绕组 **+** 端子的电流。
- *I2* 是流出二次绕组 **+** 端子的电流。
- *L1*、*L2* 是绕组自感。
- *M* 是互感。
- *k* 是耦合系数，0 < *k* < 1。
- *t* 是时间。

连接到一次绕组和二次绕组的两个电气网络必须各自拥有自己的 Electrical Reference 模块。

使用此模块表示交流变压器。如果电感项和互感项在模型中不重要或未知，可以改用 Ideal Transformer 模块。

Simscape™ 和 Simscape Electrical™ 库包含多个可以对同一类型变压器设备进行建模的模块。但是，这些模块做出不同的建模假设。要为您的应用选择合适的模块，必须了解这些假设如何影响模块行为随频率的变化。有关详细信息，请参阅 Choose Blocks to Model Transformers (Simscape Electrical)。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
