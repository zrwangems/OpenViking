---
type: simulink-block
title: 'Gear Box'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanisms'
documentation_page: 'gearbox'
documentation_source_path: 'ref/gearbox.html'
language: zh-CN
chinese_source: worker-translation
---

# Gear Box

## 端口
```yaml
ports:
- name: S
  summary: 输入轴机械旋转
  direction: conserving
- name: O
  summary: 输出轴机械旋转
  direction: conserving
```

### 守恒端口

### **S** — 输入轴机械旋转

与输入轴关联的机械旋转守恒端口。

### **O** — 输出轴机械旋转

与输出轴关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Gear ratio
  summary: 齿轮速度比 5（默认值）
  group: ''
```

### **Gear ratio** — 齿轮速度比 `5`（默认值）

输入轴角速度与输出轴角速度之比。您可以指定正值和负值。
## 所属库

Simscape / Foundation Library / Mechanical / Mechanisms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

机械系统中的齿轮箱

Gear Box 模块表示理想的、非行星式、固定齿轮传动比的齿轮箱。齿轮传动比确定为输入轴角速度与输出轴角速度之比。

齿轮箱用以下方程描述：

ωS=N·ωO

TO=N⋅TS

PS=ωS⋅TS

PO=−ωO⋅TO

其中

- *ω*S 是输入轴角速度。
- *ω*O 是输出轴角速度。
- *N* 是齿轮传动比。
- *T*S 是输入轴上的扭矩。
- *T*O 是输出轴上的扭矩。
- *P*S 是输入轴上的功率。
- *P*O 是输出轴上的功率。请注意计算 *P*O 时的负号。网络规则之一是，如果功率从电路中移除（耗散），则流经守恒端口的功率为正；如果元件向系统生成功率，则为负。

连接 S 和 O 分别是与齿轮箱输入轴和输出轴关联的机械旋转守恒端口。模块正方向为从 S 到参考点，以及从参考点到 O。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
