---
type: simulink-block
title: 'Coordinate Transformation Conversion'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'coordinatetransformationconversion'
documentation_source_path: 'ref/coordinatetransformationconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Coordinate Transformation Conversion

## 端口

### 输入

### **Input transformation** — 坐标变换列向量 | 3-by-3 matrix | 4-by-4 matrix

Input transformation，指定为坐标变换。支持以下表示：

- Axis-Angle (`AxAng`) – `[x y z theta]`
- Euler Angles (`Eul`) – 三元素向量。例如 `[z y x]`。
- Homogeneous Transformation (`TForm`) – 4-by-4 matrix
- Quaternion (`Quat`) – `[w x y z]`
- Rotation Matrix (`RotM`) – 3-by-3 matrix
- Translation Vector (`TrVec`) – `[x y z]`

所有向量都必须是 **列向量**。

为了适应仅包含位置或方向信息的表示（例如 `TrVec` 或 `Eul`），您可以指定两个输入或输出来处理所有变换信息。当您选择 Homogeneous Transformation 作为输入或输出时，可以在模块掩码上选择可选的 **Show TrVec input port** 或 **Show TrVec output port** 参数，以切换多个端口。

### **TrVec** — 平移向量 3 元素列向量

平移向量，指定为 3 元素列向量 `[x y z]`，分别对应于 *x*、*y* 和 *z* 轴上的平移。此端口可用于与旋转向量分开输入或输出平移信息。

#### 依赖项

必须为输出 **Representation** 参数选择 `Homogeneous Transformation`，才能获得显示附加 **TrVec** 输入端口的选项。通过点击 **Show TrVec input port** 启用该端口。

### 输出参数

### **Output transformation** — 坐标变换列向量 | 3-by-3 matrix | 4-by-4 matrix

Output transformation，返回为具有指定表示的坐标变换。支持以下表示：

- Axis-Angle (`AxAng`) – `[x y z theta]`
- Euler Angles (`Eul`) – 三元素向量。例如 `[z y x]`。
- Homogeneous Transformation (`TForm`) – 4-by-4 matrix
- Quaternion (`Quat`) – `[w x y z]`
- Rotation Matrix (`RotM`) – 3-by-3 matrix
- Translation Vector (`TrVec`) – `[x y z]`

为了适应仅包含位置或方向信息的表示（例如 `TrVec` 或 `Eul`），您可以指定两个输入或输出来处理所有变换信息。当您选择 `Homogeneous Transformation` 作为输入或输出时，可以在模块掩码上选择可选的 **Show TrVec input port** 或 **Show TrVec output port** 参数，以切换多个端口。

### **TrVec** — 平移向量 三元素列向量

平移向量，返回为三元素列向量 `[x y z]`，分别对应于 *x*、*y* 和 *z* 轴上的平移。此端口可用于与旋转向量分开输入或输出平移信息。

#### 依赖项

必须为输入 **Representation** 参数选择 `Homogeneous Transformation`，才能获得显示附加 **TrVec** 输出端口的选项。通过点击 **Show TrVec output port** 启用该端口。

## 参数

#### 输入

### **Representation** — 输入表示 `Axis-Angle` | `Euler Angles` | `Homogeneous Transformation` | `Quaternion` | `Rotation Matrix` | `Translation Vector`

选择模块输入端口的表示。如果您使用的变换仅包含方向信息，则在转换到 homogeneous transformation 或从 homogeneous transformation 转换时，还可以选择 **Show TrVec input port** 或 **Show TrVec output port**。

### **Axis rotation sequence** — Euler 角轴旋转顺序 `ZYX` (default) | `ZYZ` | `XYZ`

Euler 角轴旋转顺序，指定为以下字符串标量之一：

- `ZYX` (default)
- `ZYZ`
- `ZXY`
- `ZXZ`
- `YXY`
- `YZX`
- `YXZ`
- `YZY`
- `XYX`
- `XYZ`
- `XZX`
- `XZY`

输入端口 `Eul` 中角度的顺序必须与此旋转序列匹配。每个字符表示对应的轴。例如，如果序列为 `ZYX`，则指定的三个 Euler 角按顺序解释为绕 *z* 轴的旋转、绕 *y* 轴的旋转以及绕 *x* 轴的旋转。将此旋转应用于一个点时，它将按 *x*、然后 *y*、然后 *z* 的顺序应用轴旋转。

#### 依赖项

必须为输入 **Representation** 参数选择 `Euler Angles`。轴旋转序列仅适用于 Euler 角旋转。

### **Show TrVec input port** — 切换 `TrVec` 端口 off (default) | on

当您希望随方向表示一起为位置信息指定单独的平移向量时，切换 **TrVec** 输入端口。

#### 依赖项

必须为输出 **Representation** 参数选择 `Homogeneous Transformation`，才能获得显示附加 **TrVec** 输入端口的选项。通过点击 **Show TrVec input port** 启用该端口。

#### 输出

### **Representation** — 输出表示 `Axis-Angle` | `Euler Angles` | `Homogeneous Transformation` | `Quaternion` | `Rotation Matrix` | `Translation Vector`

选择模块输出端口的表示。如果您使用的变换仅包含方向信息，则在转换到 homogeneous transformation 或从 homogeneous transformation 转换时，还可以选择 **Show TrVec input port** 或 **Show TrVec output port**。

### **Axis rotation sequence** — Euler 角轴旋转顺序 `ZYX` (default) | `ZYZ` | `XYZ`

Euler 角轴旋转顺序，指定为以下字符串标量之一：

- `ZYX` (default)
- `ZYZ`
- `ZXY`
- `ZXZ`
- `YXY`
- `YZX`
- `YXZ`
- `YZY`
- `XYX`
- `XYZ`
- `XZX`
- `XZY`

输出端口 `Eul` 中角度的顺序必须与此旋转序列匹配。每个字符表示对应的轴。例如，如果序列为 `ZYX`，则返回的三个 Euler 角按顺序解释为绕 *z* 轴的旋转、绕 *y* 轴的旋转以及绕 *x* 轴的旋转。将此旋转应用于一个点时，它将按 *x*、然后 *y*、然后 *z* 的顺序应用轴旋转。

#### 依赖项

必须为输出 **Representation** 参数选择 `Euler Angles`。轴旋转序列仅适用于 Euler 角旋转。

### **Show TrVec output port** — 切换 `TrVec` 端口 off (default) | on

当您希望随方向表示一起接收用于位置信息的单独平移向量时，切换 **TrVec** 输出端口。

#### 依赖项

必须为输入 **Representation** 参数选择 `Homogeneous Transformation`，才能获得显示附加 **TrVec** 输出端口的选项。通过点击 **Show TrVec output port** 启用该端口。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**Tunable:** No

## 所属库

Robotics System Toolbox / Utilities Navigation Toolbox / Utilities ROS Toolbox / Utilities UAV Toolbox / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2024b：额外的 Euler 序列支持

Coordinate Transformation Conversion 模块为 **Axis rotation sequence** 参数支持额外的 Euler 序列。以下是所有支持的 Euler 序列：

- `ZYX`
- `ZYZ`
- `ZXY`
- `ZXZ`
- `YXY`
- `YZX`
- `YXZ`
- `YZY`
- `XYX`
- `XYZ`
- `XZX`
- `XZY`

## 描述

转换为指定的坐标变换表示

Coordinate Transformation Conversion 模块将坐标变换从输入表示转换为指定的输出表示。输入和输出表示使用以下形式：

- Axis-Angle (`AxAng`) – `[x y z theta]`
- Euler Angles (`Eul`) – 三元素向量。例如 `[z y x]`。
- Homogeneous Transformation (`TForm`) – 4-by-4 matrix
- Quaternion (`Quat`) – `[w x y z]`
- Rotation Matrix (`RotM`) – 3-by-3 matrix
- Translation Vector (`TrVec`) – `[x y z]`

所有向量都必须是 **列向量**。

为了适应仅包含位置或方向信息的表示（例如 `TrVec` 或 `Eul`），您可以指定两个输入或输出来处理所有变换信息。当您选择 Homogeneous Transformation 作为输入或输出时，可以在模块掩码上选择可选的 **Show TrVec input port** 或 **Show TrVec output port** 参数，以切换多个端口。
