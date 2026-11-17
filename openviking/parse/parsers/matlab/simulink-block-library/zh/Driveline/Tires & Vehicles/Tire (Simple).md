---
type: simulink-block
title: 'Tire (Simple)'
family: 'tires-vehicles'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles'
documentation_page: 'tiresimple'
documentation_source_path: 'ref/tiresimple.html'
language: zh-CN
chinese_source: worker-translation
---

# Tire (Simple)

## 端口

### 守恒

### **A** — 车轴机械旋转

与轮胎所在车轴关联的机械旋转端口。

### **H** — 轮毂机械旋转

与车轮轮毂关联的机械旋转端口。

## 参数

该表显示了某些 Tire (Simple) 参数的可见性如何取决于你为其他参数选择的选项。

**参数依赖关系**

| 参数 | |
| --- | --- |
| Rolling Radius | |
| Compliance — 选择 `No compliance - Suitable for HIL simulation` 或 `Specify stiffness and damping` | |
| **No compliance - Suitable for HIL simulation** | **Specify stiffness and damping** |
| Longitudinal stiffness |
| Longitudinal damping |
| Inertia — 选择 `No Inertia` 或 `Specify inertia and initial velocity` | |
| **No Inertia** | **Specify inertia and initial velocity** |
| Tire inertia |
| Initial velocity |

### **Rolling radius** — 半径 `0.3` `m`（默认）| 正标量

轮胎的滚动半径。滚动半径必须大于零。

### **Compliance** — 柔度模型 `No compliance - Suitable for HIL simulation`（默认）| `Specify stiffness and damping`

包括或忽略纵向刚度和阻尼。

#### 依赖关系

选择 `Specify stiffness and damping` 会显示其他参数。有关详细信息，请参阅参数依赖关系。

### **Longitudinal stiffness** — 纵向刚度 `1e6` `N/m`（默认）| 正标量

轮胎的纵向刚度。该参数必须大于零。

#### 依赖关系

仅当 **Compliance** 参数设置为 `Specify stiffness and damping` 时，此参数才会出现。有关详细信息，请参阅参数依赖关系。

### **Longitudinal damping** — 纵向阻尼 `1000` `N/(m/s)`（默认）| 正标量

轮胎的纵向阻尼。该参数必须大于零。

#### 依赖关系

仅当 **Compliance** 参数设置为 `Specify stiffness and damping` 时，此参数才会出现。有关详细信息，请参阅参数依赖关系。

### **Inertia** — 惯性模型 `No inertia`（默认）| `Specify inertia and initial velocity`

包括或忽略轮胎惯性。

#### 依赖关系

选择 `Specify inertia and initial velocity` 会显示其他参数。有关详细信息，请参阅参数依赖关系。

### **Tire inertia** — 轮胎惯性 `1` `kg*/m^2`（默认）| 正标量

轮胎的旋转惯性。

#### 依赖关系

仅当 **Inertia** 参数设置为 `Specify inertia and initial velocity` 时，此参数才会出现。有关详细信息，请参阅参数依赖关系。

### **Initial velocity** — 初始速度 `0` `rad/s`（默认）

轮胎的初始旋转速度。

#### 依赖关系

仅当 **Inertia** 参数设置为 `Specify inertia and initial velocity` 时，此参数才会出现。有关详细信息，请参阅参数依赖关系。

## 所属库

Simscape / Driveline / Tires & Vehicles

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

具有最少参数的无滑动轮胎模型

Tire (Simple) 模块表示一个简单的无滑动轮胎模型，你通过轮胎半径对其进行参数化。

你可以选择添加惯性、刚度或阻尼。这些动力学需要额外的计算，这往往会使模型不太适合实时仿真。
