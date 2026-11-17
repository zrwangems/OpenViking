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

### **Translation** — 对象平移状态 `1` 或 `true` | `0` 或 `false`

对象平移状态，未按下时返回 `0` 或 `false`，按下时返回 `1` 或 `true`。

**数据类型：** `Boolean`

### **Rotation** — 对象旋转状态 `1` 或 `true` | `0` 或 `false`

对象旋转状态，未按下时返回 `0` 或 `false`，按下时返回 `1` 或 `true`。

**数据类型：** `Boolean`

### **Buttons** — 按钮状态 `1` 或 `true` | `0` 或 `false`

按钮状态，未按下时返回 `0` 或 `false`，按下时返回 `1` 或 `true`。

**数据类型：** `Boolean`

## 参数

### **Port** — 鼠标连接的串口 `COM1`（默认）| `COM2` | `COM3` | `COM4` | `USB1` | `USB2` | `USB3` | `USB4`

空间鼠标连接的串口。可能的值为 `USB1`...`USB4` 和 `COM1`...`COM4`。

### **Output type** — 输出类型 `Speed`（默认）| `Position` | `Viewpoint coordinates`

指定来自设备的输入如何变换：

- `Speed` — 不进行变换。输出为平移速度和旋转速度。
- `Position` — 对平移和旋转进行积分。输出为位置和姿态，形式为 roll/pitch/yaw 角度。
- `Viewpoint coordinates` — 对平移和旋转进行积分。输出为位置和姿态，形式为轴和角度。您可以将这些值用作虚拟世界中的视点坐标。

### **Dominant mode** — 仅接受主导运动和旋转的选项 `off`（默认）| `on`

如果选中此复选框，鼠标仅接受主导运动和旋转，忽略其他运动。此模式对于使用 Simulation 3D Space Mouse 模块的初学者可能很有用。

### **Disable position movement** — 将旋转固定为初始值的选项 `off`（默认）| `on`

选中此复选框可将旋转固定为初始值，仅允许更改位置。

### **Disable rotation movement** — 将位置固定为初始值的选项 `off`（默认）| `on`

选中此复选框可将位置固定为初始值，仅允许更改旋转。

### **Normalize output angle** — 确定旋转角度是否应在整圆内环绕的选项 `off`（默认）| `on`

选择积分的旋转角度是否应在整圆（360°）内环绕。当您将 **Output Type** 设置为 `Speed` 时，软件忽略此参数。

#### 依赖

要启用此参数，请将 **Output type** 设置为 `Position`。

### **Limit position** — 限制鼠标位置的选项 `off`（默认）| `on`

选择是否限制鼠标的位置上限和下限。

#### 依赖

要启用此参数，请将 **Output type** 设置为 `Position`。

### **Position sensitivity** — 平移的鼠标灵敏度 `0.0001`（默认）

平移的鼠标灵敏度。较高的值对应较高的灵敏度。

### **Rotation sensitivity** — 旋转的鼠标灵敏度 `0.00001`（默认）

旋转的鼠标灵敏度。较高的值对应较高的灵敏度。

### **Initial position** — 平移的初始条件 `[0 0 0]`（默认）

积分平移的初始条件。当您将 **Output Type** 设置为 `Speed` 时，软件忽略此参数。

#### 依赖

要启用此参数，请将 **Output type** 设置为 `Position` 或 `Viewpoint coordinates`。

### **Initial rotation** — 旋转的初始条件 `[0 0 0]`（默认）

积分旋转的初始条件。当您将 **Output Type** 设置为 `Speed` 时，软件忽略此参数。

#### 依赖

要启用此参数，请将 **Output type** 设置为 `Position` 或 `Viewpoint coordinates`。

### **Lower position limit** — 鼠标的下限 `[-100 -100 -100]`（默认）

鼠标下限的位置坐标。

#### 依赖关系

要启用此参数：

- 将 **输出类型** 设置为
  `Position`。
- 选中 **限制位置**
  参数。

### **位置上限** — 鼠标上限 `[100 100 100]`（默认值）

鼠标上限的位置坐标。

#### 依赖关系

要启用此参数：

- 将 **输出类型** 设置为
  `Position`。
- 选中 **限制位置**
  参数。

## 所属库

Simulink 3D Animation / Simulation 3D / Hardware Interface

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2007b 中引入**

### R2025a：从 Space Mouse Input 重命名

为反映 Simulink® 库的变更，Space Mouse Input 模块现在
称为 Simulation 3D Space Mouse。行为保持
不变。

## 描述

处理来自空间鼠标设备的输入

空间鼠标是一种用途类似于操纵杆的设备，但它还提供
六自由度的运动控制。此模块读取空间
鼠标的状态，并提供一些常用的输入变换。
Simulation 3D Space Mouse 模块支持由 3Dconnexion
（`https://www.3dconnexion.com`）制造的当前型号的 3D 导航设备。
