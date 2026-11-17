---
type: simulink-block
title: 'Radiative Heat Transfer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'radiativeheattransfer'
documentation_source_path: 'ref/radiativeheattransfer.html'
language: zh-CN
chinese_source: worker-translation
---

# Radiative Heat Transfer

## 端口
```yaml
ports:
- name: A
  summary: Body A thermal
  direction: conserving
- name: B
  summary: Body B thermal
  direction: conserving
```

### 守恒端口

### **A** — Body A thermal

与 body A 关联的热守恒端口。

### **B** — Body B thermal

与 body B 关联的热守恒端口。
## 参数
```yaml
parameters:
- name: Area
  summary: Area of heat transfer 0.0001 m^2 (default) | positive scalar
  group: ''
- name: Radiation coefficient
  summary: Radiation heat transfer coefficient 4e-8 W/m^2/K^4 (default) | positive scalar
  group: ''
```

### **Area** — Area of heat transfer `0.0001 m^2` (default) | positive scalar

辐射体的传热面积。

### **Radiation coefficient** — Radiation heat transfer coefficient `4e-8 W/m^2/K^4` (default) | positive scalar

两个物体的辐射系数，基于其几何形状、尺寸和表面发射率。有关详细信息，请参阅 [1]。
## 所属库

Simscape / Foundation Library / Thermal / Thermal Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

## 描述

通过辐射进行的热传递

Radiative Heat Transfer 模块表示两个物体之间通过辐射进行的热传递。该传递由 Stefan-Boltzmann 定律控制：

Q=k⋅A⋅(TA4−TB4),

其中：

- *Q* 是热流量。
- *k* 是辐射系数。
- *A* 是发射体的表面积。
- *T*A 和 *T*B 是两个物体的温度。

辐射系数由几何形状、尺寸和表面发射率决定。例如，两个平行板之间传热的辐射常数计算为

k=σ1ε1+1ε2−1,

其中：

- *σ* 是 Stefan-Boltzmann 常数。
- *ε*1 是发射板的表面发射率。
- *ε*2 是接收板的表面发射率。

类似地，同心圆柱的辐射系数由以下公式确定

k=σ1ε1+1−ε2ε2r1r2,

其中 *r*1 和 *r*2 分别是发射圆柱和接收圆柱的半径。有关更多信息，包括各种形状的公式，请参阅 [1]。

连接 **A** 和 **B** 分别是与发射体和接收体关联的热守恒端口。模块正方向是从端口 **A** 到端口 **B**。这意味着如果热流从 **A** 流向 **B**，则热流为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
