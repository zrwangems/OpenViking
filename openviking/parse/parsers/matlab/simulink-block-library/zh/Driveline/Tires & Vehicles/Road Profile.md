---
type: simulink-block
title: 'Road Profile'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles'
documentation_page: 'roadprofile'
documentation_source_path: 'ref/roadprofile.html'
language: zh-CN
chinese_source: worker-translation
---

# Road Profile

## 端口

### 守恒

### **H** — 水平运动机械平移

与水平运动关联的守恒端口。连接到 Vehicle Body 模块的 **H** 端口。

### 输出

### **MF** — 前轴摩擦系数向量

前轴摩擦系数的物理信号输出端口。

该向量对于 Magic Formula 摩擦模型包含四个元素，对于摩擦系数摩擦模型包含两个元素。连接到前轴 Tire (Friction Parameterized) 或 Tire (Magic Formula) 模块的 **M** 端口。

仅当 **Friction output** 参数设置为以下值之一时，此端口可见：

- **Physical signal Magic Formula coefficients**
- **Physical signal friction coefficients**

### **MR** — 后轴摩擦系数向量

后轴摩擦系数的物理信号输出端口。

该向量对于 Magic Formula 摩擦模型包含四个元素，对于摩擦系数摩擦模型包含两个元素。连接到后轴 Tire (Friction Parameterized) 或 Tire (Magic Formula) 模块的 **M** 端口。

#### 依赖关系

仅当 **Friction** 参数 **Friction output** 设置为以下值之一时，此端口可见：

- **Physical signal Magic Formula coefficients**
- **Physical signal friction coefficients**

### **beta** — 车辆角度标量

车辆角度的物理信号输出端口。

## 参数

### 主

### **Horizontal distance from CG to front axle** — 质心到前轴的距离 `1.4` `m`（默认）| 正标量

从质心（CG）到前轴的水平距离。指定的值应与所连接的 Vehicle Body 模块的 **Horizontal distance from CG to front axle** 参数所指定的值相同。

### **Horizontal distance from CG to rear axle** — 质心到后轴的距离 `1.6` `m`（默认）| 正标量

从质心（CG）到后轴的水平距离。指定的值应与所连接的 Vehicle Body 模块的 **Horizontal distance from CG to rear axle** 参数所指定的值相同。

### **Horizontal distance for vertical profile** — 垂直剖面的水平距离 `[-10, 0, 10]` `m`（默认）| 向量

对应于车辆质心相对于参考坐标系 *x* 轴移动距离的查表。例如，图中显示了 [-10, 0, 10] 的水平剖面。查表外推方式为最近邻。

### **Vertical profile** — 垂直剖面 `[0, 0, .25]` `m`（默认）| 向量

对应于车辆质心相对于参考坐标系 *y* 轴移动距离的查表。例如，图中显示了 [2, 0, 5] 的垂直剖面。查表外推方式为最近邻。

### 摩擦

### **Friction output** — 摩擦系数输出类型 `None`（默认）| `Physical signal Magic Formula coefficients` | `Physical signal friction coefficients`

模块输出的摩擦系数类型。选择 `Physical signal Magic Formula coefficients` 以改变 Tire (Magic Formula) 模块的摩擦。选择 `Physical signal friction coefficients` 以改变 Tire (Friction Parameterized) 模块的摩擦。

#### 依赖关系

将此参数设置为 **Physical signal Magic Formula coefficients** 或 **Physical signal friction coefficients** 会使 **MF** 和 **MR** 端口以及关联的 **Friction** 参数可见。

### **Horizontal distance for friction profile** — 摩擦剖面的水平距离 `[-10, 2, 2.1, 6, 6.1, 10]` `m`（默认）| 向量

摩擦剖面水平距离。

#### 依赖关系

仅当 **Friction** 参数 **Friction output** 设置为以下值之一时，此参数可见：

- **Physical signal Magic Formula coefficients**
- **Physical signal friction coefficients**

### **Magic Formula coefficients for front axle** — 前轴 Magic Formula 系数 `[10, 2, 1, 1; 10, 2, 1, 1; 8, 3, 1, 1; 8, 3, 1, 1; 9, 4, 1, 1; 9, 4, 1, 1]`（默认）| 矩阵

Magic Formula 系数，指定为 *n*×*4* 矩阵，其中 *n* 是由 **Horizontal distance for friction profile** 参数指定的向量中的点数。

#### 依赖关系

仅当 **Friction** 参数的 **Friction output** 设置为 **Physical signal Magic Formula coefficients** 时，此参数可见。

### **Magic Formula coefficients for rear axle** — 后轴 Magic Formula 系数 `[10, 2, 1, 1; 10, 2, 1, 1; 8, 3, 1, 1; 8, 3, 1, 1; 9, 4, 1, 1; 9, 4, 1, 1]`（默认）| 矩阵

Magic Formula 系数，指定为 *n*×*4* 矩阵，其中 *n* 是由 **Horizontal distance for friction profile** 参数指定的向量中的点数。

#### 依赖关系

仅当 **Friction** 参数的 **Friction output** 设置为 **Physical signal Magic Formula coefficients** 时，此参数可见。

### **Static and kinetic friction coefficients for front axle** — 前轴摩擦系数 `[.9, .7; .9, .7; .7, .5; .7, .5; .8, .6; .8, .6]`（默认）| 矩阵

前轴静摩擦系数和动摩擦系数，指定为 *n*×*2* 矩阵，其中 *n* 是由 **Horizontal distance for friction profile** 参数指定的向量中的点数。

#### 依赖关系

仅当 **Friction** 参数的 **Friction output** 设置为 **Physical signal friction coefficients** 时，此参数可见。

### **Static and kinetic friction coefficients for rear axle** — 后轴摩擦系数 `[.9, .7; .9, .7; .7, .5; .7, .5; .8, .6; .8, .6]`（默认）| 矩阵

后轴静摩擦系数和动摩擦系数，指定为 *n*×*2* 矩阵，其中 *n* 是由 **Horizontal distance for friction profile** 参数指定的向量中的点数。

#### 依赖关系

仅当 **Friction** 参数的 **Friction output** 设置为 **Physical signal friction coefficients** 时，此参数可见。

## 所属库

Simscape / Driveline / Tires & Vehicles

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

具有变化高程和摩擦特性的道路轮廓

Road Profile 模块表示具有变化高程和摩擦特性的道路轮廓。当车辆行驶时，车轴参数和重心（CG）位置决定前轴和后轴的位置。该模块使用车轴位置计算车辆角度，并可选地计算轮胎摩擦系数。该模块使用 Magic Formula 或动摩擦系数和静摩擦系数对摩擦进行建模。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
