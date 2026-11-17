---
type: simulink-block
title: 'Rigid Transform'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Frames and Transforms'
documentation_page: 'rigidtransform'
documentation_source_path: 'ref/rigidtransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Rigid Transform

## 端口

### Frame

### **B** — 基础坐标系 frame

用于指定变换所相对于的坐标系。

### **F** — 从动坐标系 frame

应用变换的坐标系。

## 参数

### Rotation

### **Method** — 指定相对旋转的方法 `None`（默认）| `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

用于指定基础坐标系与从动坐标系之间相对旋转的方法。将参数设置为 `None`，以将基础坐标系和从动坐标系约束为相同方向。

### **Pair 1: Follower** — 用于与指定基础坐标系轴对齐的从动坐标系轴 `+X`（默认）| `-X` | `+Y` | `-Y` | `+Z` | `-Z`

用于与由 **Pair 1: Base** 参数设置的基础坐标系轴对齐的从动坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基础坐标系旋转，以实现基础坐标系和从动坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 1: Base** — 基础坐标系轴 `+Y`（默认）| `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 1: Follower** 指定的从动坐标系对齐的基础坐标系轴，指定为基础坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Pair 2: Follower** — 用于与指定基础坐标系轴对齐的从动坐标系轴 `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

要与由 **Pair 2: Follower** 指定的从动坐标系对齐的基础坐标系轴，指定为从动坐标系的正交轴。从动坐标系相对于基础坐标系旋转，以实现基础坐标系和从动坐标系所选轴之间的对齐。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Pair2: Base** — 基础坐标系轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

用于让 **Pair2: Follower** 参数中设置的从动坐标系轴与之对齐的基础坐标系轴，指定为基础坐标系的正交轴。**Pair 2** 的轴选项取决于 **Pair 1** 的轴选择。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将 **Method** 参数设置为 `Aligned Axis`。

### **Axis** — 相对旋转的标准轴 `+Z`（默认）| `+X` | `-X` | `+Y` | `-Y` | `-Z`

相对旋转的轴，指定为基础坐标系的正交轴。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将 **Method** 参数设置为 `Standard Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示从动坐标系相对于基础坐标系绕指定轴的旋转。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将 **Method** 参数设置为 `Standard Axis`。

### **Axis** — 相对旋转的轴 [0 0 1]（默认）| 3×1 向量

相对旋转的轴，指定为 3×1 单位向量。该向量无量纲，表示在基础坐标系中分解的旋转轴。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将 **Method** 参数设置为 `Arbitrary Axis`。

### **Angle** — 相对旋转的角度 0.0 `deg`（默认）| 标量

相对旋转的角度，指定为标量。该角度表示从动坐标系相对于基础坐标系绕由 **Axis** 参数指定的轴的旋转。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将 **Method** 参数设置为 `Arbitrary Axis`。

### **Rotation About** — 要绕其轴旋转从坐标系的坐标系 `Follower Axes`（默认）| `Base Axes`

要绕其轴旋转从坐标系的坐标系，指定为
`Follower Axes` 或 `Base
Axes`。如果将该参数设置为
`Follower Axes`，则从坐标系绕其自身轴旋转，并且从坐标系在每次连续旋转时改变方向。如果将该参数设置为 `Base
Axes`，则从坐标系绕固定的基础坐标系轴旋转。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将
**Method** 参数设置为 `Rotation
Sequence`。

### **Sequence** — 旋转轴序列 `X-Y-X`（默认）| `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

用于三次连续基本旋转的旋转轴序列。有关详细信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将
**Method** 参数设置为 `Rotation
Sequence`。

### **Angles** — 基本旋转的角度 [0 0 0] `deg`（默认）| 3×1 向量

基本旋转的角度，指定为 3×1 向量。有关详细信息，请参阅
Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将
**Method** 参数设置为 `Rotation
Sequence`。

### **Matrix** — 旋转矩阵 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵

相对旋转，指定为 3×3 矩阵。该矩阵必须正交且行列式为 1。有关详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将
**Method** 参数设置为 `Rotation
Matrix`。

### **Quaternion** — 使用四元数的相对旋转 [1 0 0 0]（默认）| 单位四元数向量

相对旋转，指定为四元数参数化中的向量。有关四元数的详细信息，请参阅 Rotational Measurements。

#### 依赖关系

要启用此参数，请在 **Rotation** 下将
**Method** 参数设置为
`Quaternion`。

### Translation

### **Method** — 用于指定平移的方法 `None`（默认）| `Cartesian` | `Standard Axis` | `Cylindrical`

用于指定基座坐标系与从动坐标系之间相对平移的方法。下表汇总了可用选项。

| Method | 描述 |
| --- | --- |
| `None` | 使基座坐标系与从动坐标系重合。此方法不需要参数。 |
| `Cartesian` | 以笛卡尔坐标指定三维平移 |
| `Standard Axis` | 沿 *x*、*y* 或 *z* 轴指定一维平移 |
| `Cylindrical` | 以柱坐标指定三维平移 |

`Cartesian Axis`
:   指定从动坐标系相对于基座坐标系的 **Offset**。这是使基座坐标系与从动坐标系重合的三维平移向量。选择或输入物理单位。

`Standard Axis`
:   指定从动坐标系相对于基座坐标系沿基座坐标系 *x*、*y* 或 *z* 轴的偏移。选择或输入物理单位。

    | 参数 | 描述 |
    | --- | --- |
    | **Axis** | 从动坐标系沿其平移的轴 |
    | **Offset** | 从动坐标系相对于基座坐标系沿指定轴的平移 |

`Cylindrical`
:   以柱坐标指定使基座坐标系与从动坐标系重合的平移。选择或输入物理单位。

    | 参数 | 描述 |
    | --- | --- |
    | **Radius** | 从动坐标系原点与基座坐标系 *z* 轴之间的距离。这是柱坐标的半径坐标。 |
    | **Theta** | 连接基座坐标系与从动坐标系原点的直线相对于基座坐标系 *x* 轴的旋转角度。这是柱坐标的方位角坐标。 |
    | **Z Offset** | 基座坐标系与从动坐标系原点之间沿基座坐标系 *z* 轴的距离。这是柱坐标的长度坐标。 |

## 所属库

Simscape / Multibody / Frames and Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

坐标系之间的固定空间关系

Rigid Transform 模块在仿真期间指定并保持两个坐标系之间的固定空间关系。该空间关系可以包括平移和旋转。

该模块有多种方法用于指定从动坐标系相对于基座坐标系的位置和方向。有关详细信息，请参阅 Rotation and Translation。
