---
type: simulink-block
title: 'Radiative Heat Transfer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Models / Thermal Elements'
documentation_page: 'radiativeheattransfer'
documentation_source_path: 'ref/radiativeheattransfer.html'
language: zh-CN
chinese_source: official
---

# Radiative Heat Transfer

## 端口

### 守恒

### **A** — 物体 A 热

与物体 A 关联的热守恒端口。

### **B** — 物体 B 热

与物体 B 关联的热守恒端口。

## 参数

### **面积** — 传热面积 `0.0001 m^2` (默认) | 正标量

辐射体的传热面积。

### **辐射系数** — 辐射传热系数 `4e-8 W/m^2/K^4` (默认) | 正标量

两个物体的辐射系数（基于其几何形状、尺寸和表面发射率）。有关详细信息，请参阅[1]。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007b 中推出**

## 描述

辐射传热

Radiative Heat Transfer 模块表示两个物体之间的辐射传热。该传热由斯特藩-玻尔兹曼定律控制：

Q=k⋅A⋅(TA4−TB4),

其中：

- *Q* 是热流。
- *k* 是辐射系数。
- *A* 是发射体表面积。
- *T*A 和 *T*B 是两个物体的温度。

辐射系数由几何形状、尺寸和表面发射率确定。例如，两个平行板之间的辐射传热常数的计算方式为

k=σ1ε1+1ε2−1,

其中：

- *σ* 是斯特藩-玻尔兹曼常数。
- *ε*1 是发射板的表面发射率。
- *ε*2 是接收板的表面发射率。

类似地，同心圆柱的辐射系数由以下公式确定

k=σ1ε1+1−ε2ε2r1r2,

其中，*r*1 和 *r* 2 分别是发射圆柱体和接收圆柱体的半径。有关详细信息（包括针对各种形状的公式），请参阅[1]。

连接端 **A** 和 **B** 分别是与发射体和接收体关联的热守恒端口。此模块的正方向是从端口 **A** 到端口 **B**。这意味着如果热流从 **A** 流向 **B**，则热流为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
