---
type: simulink-block
title: 'Inertia'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Rotational Elements'
documentation_page: 'inertia'
documentation_source_path: 'ref/inertia.html'
language: zh-CN
chinese_source: worker-translation
---

# Inertia

## 端口
```yaml
ports:
- name: I
  summary: 将惯量连接到回路机械旋转网络的端口
  direction: conserving
- name: J
  summary: 第二个图形端口 机械旋转
  direction: conserving
```

### 守恒端口

### **I** — 将惯量连接到回路机械旋转网络的端口

机械旋转守恒端口，用于将惯量连接到物理网络。

### **J** — 第二个图形端口 机械旋转

第二个机械旋转守恒端口，允许您将惯量与其他元件串联连接在框图中。该端口与端口 **I** 刚性连接，因此单端口和双端口模块表示之间的区别纯粹是图形上的。

#### 依赖关系

要启用此端口，请将 **Number of graphical ports** 参数设置为 `2`。
## 参数
```yaml
parameters:
- name: Inertia
  summary: 恒定惯量 0.01 kg*m^2（默认）| 正标量
  group: ''
- name: Number of graphical ports
  summary: 选择模块是以图形方式连接到回路的一侧还是与其他元件串联 1（默认）| 2
  group: ''
```

### **Inertia** — 恒定惯量 `0.01 kg*m^2`（默认）| 正标量

惯量值。惯量在仿真期间保持恒定。

### **Number of graphical ports** — 选择模块是以图形方式连接到回路的一侧还是与其他元件串联 `1`（默认）| `2`

选择如何将模块连接到回路的其余部分：

- `1` — 模块有一个守恒端口，将其连接到机械旋转回路。当模块有一个端口时，将其连接到其他两个模块之间的连接线上。
- `2` — 选择此选项会显示第二个端口，允许您将模块与回路中的其他模块串联连接。两个端口刚性连接并具有相同的角速度，因此模块的功能与只有一个端口时完全相同。
## 所属库

Simscape / Foundation Library / Mechanical / Rotational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

理想机械旋转惯量

Inertia 模块表示一个理想机械旋转惯量，用以下方程描述：

T=Jdωdt

其中：

- *T* 是惯量力矩。
- *J* 是惯量。
- *ω* 是角速度。
- *t* 是时间。

默认情况下，该模块有一个机械旋转守恒端口。模块的正方向从其端口指向参考点。这意味着如果惯量沿正方向加速，则惯量力矩为正。

在某些应用中，习惯在框图布局中将惯量与其他元件串联显示。为支持此用例，**Number of graphical ports** 参数允许您在模块图标的另一侧显示第二个端口。双端口变体纯粹是图形上的：两个端口具有相同的角速度，因此无论模块有一个还是两个端口，其功能完全相同。模块图标根据 **Number of graphical ports** 参数的值而变化。

| 图形端口数量 | 模块图标 |
| --- | --- |
| `1` |  |
| `2` |  |

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
