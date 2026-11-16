---
type: simulink-block
title: 'Simulation 3D Space Mouse'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Hardware Interface'
documentation_page: 'simulation3dspacemouse'
documentation_source_path: 'simulation3dspacemouse.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Space Mouse

## 端口

### 输出

### **Translation** — 对象平移的状态 `1` 或 `true` | `0` 或 `false`

对象平移的状态，如果未按下则返回 `0` 或 `false`，如果按下则返回 `1` 或 `true`。

**数据类型：** `Boolean`

### **Rotation** — 对象旋转的状态 `1` 或 `true` | `0` 或 `false`

对象旋转的状态，如果未按下则返回 `0` 或 `false`，如果按下则返回 `1` 或 `true`。

**数据类型：** `Boolean`

### **Buttons** — 按钮的状态 `1` 或 `true` | `0` 或 `false`

按钮的状态，如果未按下则返回 `0` 或 `false`，如果按下则返回 `1` 或 `true`。

**数据类型：** `Boolean`

## 参数

### **端口** — 鼠标连接的串行端口 `COM1`（默认） | `COM2` | `COM3` | `COM4` | `USB1` | `USB2` | `USB3` | `USB4`

空间鼠标连接的串行端口。可能的值包括 `USB1`...`USB4` 和 `COM1`...`COM4`。

### **输出类型** — 输出的类型 `Speed`（默认） | `Position` | `Viewpoint coordinates`

指定如何变换来自设备的输入：

- `Speed` — 不执行任何变换。输出为平移速度和旋转速度。
- `Position` — 对平移和旋转进行积分。输出为采用 roll/pitch/yaw 角形式的位置和方向。
- `Viewpoint coordinates` — 对平移和旋转进行积分。输出为采用轴和角形式的位置和方向。可以将这些值用作虚拟世界中的视点坐标。

### **主导模式** — 用于仅接受占主导地位的移动和旋转的选项 `off`（默认） | `on`

如果选中此复选框，鼠标仅接受占主导地位的移动和旋转，而忽略其他移动和旋转。此模式对于使用 Simulation 3D Space Mouse 模块的初学者可能很有用。

### **禁用位置移动** — 用于将旋转固定在初始值的选项 `off`（默认） | `on`

选中此复选框可将旋转固定在初始值，从而只允许更改位置。

### **禁用旋转移动** — 用于将位置固定在初始值的选项 `off`（默认） | `on`

选中此复选框可将位置固定在初始值，从而只允许更改旋转。

### **归一化输出角度** — 用于确定旋转角度是否应在整圆上回绕的选项 `off`（默认） | `on`

选择积分后的旋转角度是否应在整圆（360°）上回绕。当将 **输出类型** 设置为 `Speed` 时，软件会忽略此参数。

#### 依赖关系

要启用此参数，请将 **输出类型** 设置为 `Position`。

### **限制位置** — 用于限制鼠标位置的选项 `off`（默认） | `on`

选择是否限制鼠标的位置上限和下限。

#### 依赖关系

要启用此参数，请将 **输出类型** 设置为 `Position`。

### **位置灵敏度** — 用于平移的鼠标灵敏度 `0.0001`（默认）

鼠标的平移灵敏度。值越大，灵敏度越高。

### **旋转灵敏度** — 用于旋转的鼠标灵敏度 `0.00001`（默认）

鼠标的旋转灵敏度。值越大，灵敏度越高。

### **初始位置** — 平移的初始条件 `[0 0 0]`（默认）

积分平移的初始条件。当将 **输出类型** 设置为 `Speed` 时，软件会忽略此参数。

#### 依赖关系

要启用此参数，请将 **输出类型** 设置为 `Position` 或 `Viewpoint coordinates`。

### **初始旋转** — 旋转的初始条件 `[0 0 0]`（默认）

积分旋转的初始条件。当将 **输出类型** 设置为 `Speed` 时，软件会忽略此参数。

#### 依赖关系

要启用此参数，请将 **输出类型** 设置为 `Position` 或 `Viewpoint coordinates`。

### **位置下限** — 鼠标的下限 `[-100 -100 -100]`（默认）

鼠标位置下限的坐标。

#### 依赖关系

要启用此参数：

- 将 **输出类型** 设置为
  `Position`。
- 选择 **限制位置**
  参数。

### **位置上限** — 鼠标的上限 `[100 100 100]`（默认）

鼠标位置上限的坐标。

#### 依赖关系

要启用此参数：

- 将 **输出类型** 设置为
  `Position`。
- 选择 **限制位置**
  参数。

## 所属库

Simulink 3D Animation / Simulation 3D / Hardware Interface

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2007b 中引入**

### R2025a：从 Space Mouse Input 重命名

为反映 Simulink® 库更改，Space Mouse Input 模块现在称为 Simulation 3D Space Mouse。行为保持不变。

## 描述

处理来自空间鼠标设备的输入

空间鼠标是一种用途类似于操纵杆的设备，但它还提供六自由度的运动控制。该模块读取空间鼠标的状态，并提供输入的一些常用变换。Simulation 3D Space Mouse 模块支持由 3Dconnexion（`https://www.3dconnexion.com`）制造的当前型号的 3D 导航设备。
