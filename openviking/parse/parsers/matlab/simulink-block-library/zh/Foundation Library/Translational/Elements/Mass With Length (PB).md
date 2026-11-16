---
type: simulink-block
title: 'Mass With Length (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'masswithlengthpb'
documentation_source_path: 'ref/masswithlengthpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Mass With Length (PB)

## 端口

### 守恒

### **B** — 基础端口，基于位置的机械平移

表示基础连接的基于位置的机械平移守恒端口。

### **F** — 从动端口，基于位置的机械平移

表示从动连接的基于位置的机械平移守恒端口。对于非零长度，端口 **F** 的位置比端口 **B** 更正。

## 参数

### **Mass** — 恒定质量 `1 kg`（默认） | 正标量

质量值。质量在仿真期间保持恒定。

### **Length** — 质量长度 `0 m`（默认） | 非负标量

质量的长度，即端口 **B** 和 **F** 之间的距离。该距离在仿真期间保持恒定。

### **Log the position of an intermediate point** — 是否记录中间点的位置 `off`（默认） | `on`

选中此复选框可记录端口 **B** 和 **F** 之间某个中间点的位置，例如质心。有关详细信息，请参阅数据记录。

### **Intermediate point fractional length from B** — 记录点距端口 B 的分数长度 `0.5`（默认） | 0 到 1 之间的无单位标量

端口 **B** 与所记录中间点之间的分数距离。

#### 依赖关系

要启用此参数，请选中 **Log the position of an intermediate point** 复选框。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

带长度和重力效应的质量

Mass With Length (PB) 模块表示一个带长度和重力效应的质量，它沿倾斜轨道移动。重力可引起沿轨道的运动。

Mass With Length (PB) 模块本质上是一个结构组件，由连接到 Spacer (PB) 模块的 Mass (PB) 模块组成。

带长度的质量示意图

力流方程为：

facc=m⋅v˙

facc=f+fgp

fgp=−m⋅g⋅sin(θ)

length=xF−xB

xLog=xB+fractionLog⋅length

其中：

- *f*acc 是与质量加速度成比例的力。正力使质量沿正方向加速。
- *f* 是网络中其他机械组件作用在质量上的净力。
- *f*gp 是与重力加速度的平行分量成比例的力，即与沿轨道作用的重力加速度成比例的力。
- *m* 是质量。
- *v* 是质量速度。端口 **B** 和 **F** 具有相同速度，*v*B = *v*F。
- *g* 是重力加速度。
- *θ* 是轨道倾角。
- *length* 是质量长度。
- *x*B 和 *x*F 分别是端口 **B** 和 **F** 的绝对位置。
- *x*Log 是中间点的绝对位置（如果启用 **Log the position of an intermediate point** 选项）。
- *fraction*Log 是中间点距端口 **B** 的分数长度。

例如，要记录质心的位置，请选中 **Log the position of an intermediate point** 复选框，并将 **Intermediate point fractional length from B** 参数设置为 `0.5`。

Mechanical Translational Properties (PB) 模块指定网络中的重力加速度和轨道倾角。有关详细信息，请参阅解释质量模块中记录的力。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅修改模块变量的标称值。
