---
type: simulink-block
title: 'Mass'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'mass'
documentation_source_path: 'ref/mass.html'
language: zh-CN
chinese_source: worker-translation
---

# Mass

## 端口

### 守恒

### **M** — 将质量连接到电路机械平移网络的端口

机械平移守恒端口，用于将质量连接到物理网络。

### **N** — 第二个图形端口 机械平移

第二个机械平移守恒端口，允许您在框图中将质量与其他元件串联连接。该端口与端口 **M** 刚性连接，因此单端口和双端口模块表示之间的区别纯粹是图形上的。

#### 依赖关系

要启用此端口，请将 **Number of graphical ports** 参数设置为 `2`。

## 参数

### **Mass** — 恒定质量 `1 kg`（默认）| 正标量

质量值。质量在仿真期间保持恒定。

### **Number of graphical ports** — 选择模块是以图形方式连接到电路的一侧还是与其他元件串联 `1`（默认）| `2`

选择如何将模块连接到电路的其余部分：

- `1` — 模块有一个守恒端口，将其连接到机械平移电路。当模块有一个端口时，将其连接到其他两个模块之间的连接线上。
- `2` — 选择此选项会显示第二个端口，允许您将模块与电路中的其他模块串联连接。两个端口刚性连接并具有相同的速度，因此模块的功能与只有一个端口时完全相同。

## 所属库

Simscape / Foundation Library / Mechanical / Translational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

理想机械平移质量

Mass 模块表示一个理想机械平移质量，用以下方程描述：

F=mdvdt

其中：

- *F* 是惯性力。
- *m* 是质量。
- *v* 是速度。
- *t* 是时间。

默认情况下，该模块有一个机械平移守恒端口。模块的正方向从其端口指向参考点。这意味着如果质量沿正方向加速，则惯性力为正。

在某些应用中，习惯上在框图布局中将质量与其他元件串联显示。为支持此用例，**Number of graphical ports** 参数允许您在模块图标对侧显示第二个端口。双端口变体纯粹是图形上的：两个端口具有相同的速度，因此无论模块有一个还是两个端口，其功能完全相同。模块图标会根据 **Number of graphical ports** 参数的值而变化。

| 图形端口数量 | 模块图标 |
| --- | --- |
| `1` |  |
| `2` |  |

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
