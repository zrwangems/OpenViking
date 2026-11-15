---
type: simulink-block
title: 'Collision Box'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Collision Detection'
documentation_page: 'collisionboxblock'
documentation_source_path: 'ref/collisionboxblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Collision Box

## 端口

### 输入

### **X** — 沿 *x* 轴的盒几何长度 标量

盒几何沿 *x* 轴的边长，
指定为正标量。单位是 meters。

### **Y** — 沿 *y* 轴的盒几何长度 标量

盒几何沿 *y* 轴的边长，
指定为正标量。单位是 meters。

### **Z** — 沿 *z* 轴的盒几何长度 标量

盒几何沿 *z* 轴的边长，
指定为正标量。单位是 meters。

### **Pose** — 碰撞几何的位姿矩阵

碰撞几何相对于世界坐标系的位姿，指定为 4×4 齐次矩阵。

### 输出

### **CollGeom** — 碰撞几何总线

碰撞几何，以总线形式返回。

要执行碰撞检查，请将此输出作为输入连接到 Check Collision 模块。

### **ExitFlag** — 碰撞盒尺寸的有效性 标量

碰撞盒尺寸的有效性，以整数标量返回，其中每个数字表示一个维度的有效性：

- **第一位** — **X** 端口处
  *x* 轴长度的有效性。
- **第二位** — **Y** 端口处
  *y* 轴长度的有效性。
- **第三位** — **Z** 端口处
  *z* 轴长度的有效性。

这些数字中的每一个均可以是以下值之一：

- `4` — 指定的维度值不是数值。
- `3` — 指定的维度值不是实数。
- `2` — 指定的维度值非有限。
- `1` — 指定的维度值不是正数。
- `0` — 指定的维度值有效。

例如，如果退出标志为 `230`，则
盒的 *x* 长度非有限，*y* 长度
不是实数值，*z* 长度有效。

要改为在运行时验证维度，请选择 **Enable Runtime Input Dimensions Error** 参数。

**数据类型：** `uint16`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条上的 **仿真** 选项卡中，在
**准备** 库中，选择 **属性检查器**。

### **Enable Runtime Input Dimensions Error** — 碰撞盒尺寸的验证 `on`（默认）| `off`

选择此参数可启用碰撞盒尺寸的运行时验证，并在 **X**、**Y** 或 **Z** 无效时返回错误。

如果清除此参数，模块在仿真期间不会报错，而是
使用 **ExitFlag** 端口标识无效的碰撞盒尺寸。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` — 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，该模块会在后续仿真中
  重用该 C 代码。
- `Interpreted execution` — 使用
  MATLAB® 解释器仿真模型。有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Robotics System Toolbox / Collision Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Collision Box 模块支持在
禁用动态内存分配的情况下进行代码生成。有关禁用动态内存
分配的详细信息，请参阅 MATLAB 函数中的动态内存分配 (Simulink)。

## 版本历史

**在 R2025a 中引入**

## 描述

创建盒碰撞几何

Collision Box 模块输出一个盒碰撞几何，该几何与其固连坐标系轴对齐，
并且其固连坐标系的原点位于盒的中心。
