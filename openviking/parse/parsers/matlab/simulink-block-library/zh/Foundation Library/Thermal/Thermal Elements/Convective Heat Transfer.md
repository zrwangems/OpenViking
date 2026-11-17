---
type: simulink-block
title: 'Convective Heat Transfer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'convectiveheattransfer'
documentation_source_path: 'ref/convectiveheattransfer.html'
language: zh-CN
chinese_source: worker-translation
---

# Convective Heat Transfer

## 端口

### 输入

### **K** — 传热系数控制信号，W/(K\*m^2) 物理信号

用于控制传热系数的输入物理信号。当该值超出**Minimum heat transfer coefficient**模块参数指定的最小限值时，信号饱和。

#### 依赖关系

要启用此端口，请将 **Convection type** 参数设置为 `Variable`。
### 守恒

### **A** — 物体 A 热

与物体 A 关联的热守恒端口。

### **B** — 物体 B 热

与物体 B 关联的热守恒端口。

## 参数

### **Convection type** — 如何指定传热系数 `Constant`（默认）| `Variable`

是将材料的传热系数指定为模块参数还是输入信号：

- `Constant` — 由 **Heat transfer coefficient** 参数指定的传热系数在仿真期间保持恒定。
- `Variable` — 端口 **K** 处的输入物理信号指定传热系数，该系数可在仿真期间变化。**Minimum heat transfer coefficient** 参数指定传热系数的下界。

### **Area** — 传热面积 `1e-4 m^2`（默认）| 正标量

传热的表面积。

### **Heat transfer coefficient** — 对流换热系数 `20 W/(K*m^2)`（默认）| 正标量

对流换热系数。

#### 依赖关系

要启用此参数，请将 **Convection type** 设置为 `Constant`。

### **Minimum heat transfer coefficient** — 传热系数下界 `1e-3 W/(K*m^2)`（默认）| 正标量

对流换热系数的下界。端口 **K** 处的输入信号在此值处饱和，以防止传热系数进一步降低。

#### 依赖关系

要启用此参数，请将 **Convection type** 设置为 `Variable`。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2022b: 对可变传热系数建模

新增的 **Convection type** 参数允许传热系数为恒定值（由 **Heat transfer coefficient** 参数指定）或可变值（由端口 **K** 处的物理信号指定）。

在默认配置下，当 **Convection type** 参数设置为 `Constant` 时，该模块的功能与之前版本相同。

## 描述

通过对流进行的热传递

Convective Heat Transfer 模块表示通过流体运动在两个物体之间进行的对流传热。牛顿冷却定律描述了该传递过程，

Q=k⋅A⋅(TA−TB)，

其中：

- *Q* 是热流量。
- *k* 是对流换热系数。
- *A* 是表面积。
- *T*A 和 *T*B 是两个物体的温度。

传热系数 *k* 可以是恒定值（使用 **Heat transfer coefficient** 参数指定），也可以是可变值（使用端口 **K** 处的物理信号指定）。

**A** 和 **B** 是与对流传热发生点关联的热守恒端口。由于模块的正方向是从端口 **A** 到端口 **B**，因此当热流从 **A** 流向 **B** 时，热流为正。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
