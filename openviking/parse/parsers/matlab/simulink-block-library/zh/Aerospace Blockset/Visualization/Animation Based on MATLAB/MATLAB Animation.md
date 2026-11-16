---
type: simulink-block
title: 'MATLAB Animation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Animation Based on MATLAB'
documentation_page: 'matlabanimation'
documentation_source_path: 'matlabanimation.html'
language: zh-CN
chinese_source: worker-translation
---

# MATLAB Animation

## 端口

### 输入

### **Port\_1** — 飞行器的下程位置、横程位置和高度三元素向量

飞行器在地球坐标中的下程位置、横程位置和高度，指定为三元素向量。端口上的数字表示飞行器编号。

**数据类型:** `double`

### **1.Xe** — 飞行器的下程位置、横程位置和高度三元素向量

飞行器在地球坐标中的下程位置、横程位置和高度，指定为三元素向量。端口上的数字表示飞行器编号。

**数据类型:** `double`

### **1.φ θ ψ** — 欧拉角三元素向量

飞行器的欧拉角（滚转、俯仰和偏航），指定为三元素向量。端口上的数字表示飞行器编号。

**数据类型:** `double`

### **Port\_N** — 第 N 个下程位置、横程位置和高度（向下为正）三元素向量

第 N 个飞行器的下程位置、横程位置和高度（向下为正），指定为三元素向量。端口上的数字表示飞行器编号。

#### 依赖关系

要启用此端口，请从 `2` 到 `10` 中选择一个 **Vehicles** 编号。

**数据类型:** `double`

### **Port\_N** — 欧拉角三元素向量

第 N 个飞行器的输入欧拉角（滚转、俯仰和偏航），指定为三元素向量。端口上的数字表示飞行器编号。

#### 依赖关系

要启用此端口，请从 `2` 到 `10` 中选择一个 **Vehicles** 编号。

**数据类型:** `double`

## 参数

### **Vehicles** — 要动画显示的飞行器 `1`（默认） | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

要动画显示的飞行器，指定为从 `1` 到 `10`。

#### 依赖关系

选择从 `2` 到 `10` 的飞行器编号会添加相应的输入端口。每个飞行器都有自己的一组输入端口，由输入端口标签开头的数字表示。

#### 编程用法

|  |
| --- |
| **模块参数**: `Vehicles` |
| **类型**: character vector |
| **值**: `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` |
| **默认值**: `'1'` |

### **Geometries (use 'quotes' on filenames)** — 飞行器几何 `'astredwedge.mat'`（默认） | MAT-file

飞行器几何，在 MAT-file 中指定。您可以使用以下方式指定这些几何：

- 变量名称，例如 `geomVar`
- 变量名称的元胞数组，例如 `{geomVar, AltGeomVar}`
- 带单引号的字符向量，例如，`'astredwedge.mat'`
- 变量名称和字符向量的混合元胞数组，例如 `{'file1.mat', 'file2.mat', 'file3.ac', geomVar}`

**注意**

所有指定的几何都必须存在于 MATLAB 工作区中，并且文件名必须存在于当前文件夹中或位于 MATLAB 路径上。

#### 编程用法

|  |
| --- |
| **模块参数**: `Geometries` |
| **类型**: character vector |
| **值**: MAT-file |
| **默认值**: `'astredwedge.mat'` |

### **Bounding box coordinates** — 边界坐标 `[-50,50,-50,50,-50,50]`（默认） | six-element vector

飞行器的边界坐标，指定为六元素向量。

此参数在仿真期间不可调。对此参数的更改在仿真停止后生效。

#### 编程用法

|  |
| --- |
| **模块参数**: `BoundingBoxCoordinates` |
| **类型**: character vector |
| **值**: six-element vector |
| **默认值**: `'[-50,50,-50,50,-50,50]'` |

### **Camera offset** — 从相机瞄准点到相机的距离 `[-150,-50,0]`（默认） | three-element vector

从相机瞄准点到相机本身的距离，指定为三元素向量。

此参数在仿真期间不可调。对此参数的更改在仿真停止后生效。

#### 编程用法

|  |
| --- |
| **模块参数**: `CameraOffset` |
| **类型**: character vector |
| **值**: three-element vector |
| **默认值**: `'[-150,-50,0]'` |

### **Camera view angle** — 相机视角 `3`（默认） | scalar

相机视角，指定为 double scalar。默认情况下，相机瞄准点是第一个本体的位置，该位置动态滞后以指示运动。

此参数在仿真期间不可调。对此参数的更改在仿真停止后生效。

#### 编程用法

|  |
| --- |
| **模块参数**: `CameraViewAngle` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'3'` |

### **Sample time** — 采样时间 `0.2`（默认） | scalar

采样时间（-1 表示继承），指定为 double scalar。

#### 编程用法

|  |
| --- |
| **模块参数**: `SampleTime` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0.2'` |

## 所属库

Aerospace Blockset / Animation / MATLAB-Based Animation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

创建六自由度多体自定义几何模块

MATLAB Animation 模块基于 `Aero.Animation` 对象创建六自由度多体自定义几何模块。此模块通过指定的边界框、相机偏移和视场，使用 *`x-y-z`* 位置和欧拉角对一个或多个飞行器几何进行动画显示。此模块期望旋转顺序为 *`z-y-x`*（psi、theta、phi）。

要更新动画中的相机参数，请先设置参数，然后关闭并双击该模块以重新打开 MATLAB® Animation 窗口。

要访问此模块的参数，请执行以下操作之一：

- 右键单击该模块，然后选择 **Mask** > **Mask Parameters**。
- 双击该模块以显示 MATLAB Animation 窗口，然后单击 **Block Parameters** 图标。

**注意**

底层图形系统以单精度存储值。因此，您可能会注意到，坐标位置大于约 1e6 时的运动会显得不稳定。这是因为单精度数大约有六位精度。这种不稳定性是由于在 `eps` MATLAB 函数的局部值处发生量化所致。要为超过 1e6 的坐标可视化更稳定的运动，可以将输入数据偏移到局部零点，或者缩小馈送到可视化的坐标值。
