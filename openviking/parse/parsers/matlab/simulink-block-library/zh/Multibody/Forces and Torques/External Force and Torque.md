---
type: simulink-block
title: 'External Force and Torque'
family: 'forces-and-torques'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'externalforceandtorque'
documentation_source_path: 'ref/externalforceandtorque.html'
language: zh-CN
chinese_source: worker-translation
---

# External Force and Torque

## 端口

### 坐标系

### **F** — 随动坐标系

外力和外力矩作用所在的随动坐标系。

### 输入

#### Force

### **fx** — 沿 *x* 轴的外力物理信号

接受力解析坐标系 *x* 方向外力的物理信号端口。输入信号是可随时间变化的标量。

此信号独立于 **f** 端口的 *x* 分量输入。当同时向此端口和 **f** 端口提供信号时，*x* 方向的外力等于这些输入之和。

#### 依赖项

要启用此端口，请在 **Force** 下选择 **Force (X)**。

### **fy** — 沿 *y* 轴的外力物理信号

接受力解析坐标系 *y* 方向外力的物理信号端口。输入信号是可随时间变化的标量。

此信号独立于 **f** 端口的 *y* 分量输入。当同时向此端口和 **f** 端口提供信号时，*y* 方向的外力等于这些输入之和。

#### 依赖项

要启用此端口，请在 **Force** 下选择 **Force (Y)**。

### **fz** — 沿 *z* 轴的外力物理信号

接受力解析坐标系 *z* 方向外力的物理信号端口。输入信号是可随时间变化的标量。

此信号独立于 **f** 端口的 *z* 分量输入。当同时向此端口和 **f** 端口提供信号时，*z* 方向的外力等于这些输入之和。

#### 依赖项

要启用此端口，请在 **Force** 下选择 **Force (Z)**。

### **f** — 外力向量物理信号

接受外力的物理信号端口。输入信号是 1-by-3 或 3-by-1 向量，[*Fx* *Fy* *Fz*]，可随时间变化。此信号独立于 **fx**、**fy** 和 **fz** 端口的输入。如果同时向 **f** 端口以及 **fx**、**fy** 和 **fz** 端口提供信号，则输入力变为所有输入之和。

#### 依赖项

要启用此端口，请在 **Force** 下选择 **Force**。

#### Torque

### **tx** — 关于 *x* 轴的外力矩物理信号

接受关于力矩解析坐标系 *x* 轴的外力矩的物理信号端口。输入信号是可随时间变化的标量。

#### 依赖项

要启用此端口，请在 **Torque** 下选择 **Torque (X)**。

### **ty** — 关于 *y* 轴的外力矩物理信号

接受关于力矩解析坐标系 *y* 轴的外力矩的物理信号端口。输入信号是可随时间变化的标量。

#### 依赖项

要启用此端口，请在 **Torque** 下选择 **Torque (Y)**。

### **tz** — 关于 *z* 轴的外力矩物理信号

接受关于力矩解析坐标系 *z* 轴的外力矩的物理信号端口。输入信号是可随时间变化的标量。

#### 依赖项

要启用此端口，请在 **Torque** 下选择 **Torque (Z)**。

### **t** — 外力矩向量物理信号

接受外力矩的物理信号端口。输入信号是 1-by-3 或 3-by-1 向量，[*Tx* *Ty* *Tz*]，可随时间变化。

#### 依赖项

要启用此端口，请在 **Torque** 下选择 **Torque**。

## 参数

#### Force

### **Force Resolution Frame** — 用于解析每个力输入的坐标系 `Attached Frame`（默认） | `World`

用于解析力输入的坐标系，指定为：

- `Attached Frame` — 模块在连接到 External Force and Torque 模块的随动坐标系的坐标系中解析输入。
- `World` — 模块在模型的世界坐标系中解析输入。

#### Torque

### **Torque Resolution Frame** — 用于解析每个力矩输入的坐标系 `Attached Frame`（默认） | `World`

用于解析力矩输入的坐标系，指定为：

- `Attached Frame` — 模块在连接到 External Force and Torque 模块的随动坐标系的坐标系中解析输入。
- `World` — 模块在模型的世界坐标系中解析输入。

## 所属库

Simscape / Multibody / Forces and Torques

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

对连接的坐标系施加外力和/或外力矩

External Force and Torque 模块将外力和/或外力矩施加到连接到该模块 **F** 端口的坐标系。力作用在该坐标系的原点，力矩绕该坐标系的对应轴作用。该模块接受物理信号来指定力和力矩。在整个仿真过程中，信号可以是常量或时变值。

您可以指定解析坐标系来解析力和力矩输入。正值力输入沿关联坐标系轴的正方向作用。正值力矩输入根据右手定则绕关联坐标系轴作用。
