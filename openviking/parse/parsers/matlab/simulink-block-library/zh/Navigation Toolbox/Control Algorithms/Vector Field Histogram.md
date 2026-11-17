---
type: simulink-block
title: 'Vector Field Histogram'
family: 'control-algorithms'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Control Algorithms'
documentation_page: 'vectorfieldhistogram'
documentation_source_path: 'ref/vectorfieldhistogram.html'
language: zh-CN
chinese_source: worker-translation
---

# Vector Field Histogram

## 端口

### 输入

### **Ranges** — 来自扫描数据的距离值，scalars 的 vector

来自扫描数据的距离值，指定为 scalars 的 vector，单位为 meters。这些距离值是传感器在指定角度处的距离。该 vector 的长度必须与对应的 **Angles** vector 相同。

### **Angles** — 来自扫描数据的角度值，scalars 的 vector

来自扫描数据的角度值，指定为 scalars 的 vector，单位为 radians。这些角度值是所指定距离的特定角度。该 vector 的长度必须与对应的 **Ranges** vector 相同。

### **TargetDir** — 车辆的目标方向 scalar

车辆的目标方向，指定为 scalar，单位为 radians。
车辆的前进方向被认为是零 radians，正角度以逆时针方向测量。
当从一组 waypoints 生成控制时，可以使用 Pure Pursuit 模块的
**TargetDir** 输出。

### 输出

### **SteerDir** — 车辆的转向方向 scalar

车辆的转向方向，指定为 scalar，单位为 radians。
此无障碍方向基于 VFH+ 算法计算。
车辆的前进方向被认为是零 radians，正角度以逆时针方向测量。

## 参数

#### 主要

### **Number of angular sectors** — 用于创建直方图的 bin 数量 `180`（默认）| scalar

用于创建直方图的 bin 数量，指定为 scalar。此参数不可调。仅当对象初始化时才能设置此参数。

### **Range distance limits (m)** — 距离读数的限制 `[0.05 2]`（默认）| two-element vector of scalars

距离读数的限制，单位为 meters，指定为 two-element vector of scalars。仅当距离读数输入位于距离限制范围内时，才会考虑该输入。使用较低的距离限制来忽略较低范围下传感器性能不佳导致的误报。使用上限来忽略距离车辆太远的障碍物。

### **Histogram thresholds** — 用于计算二值直方图的阈值 `[3 10]`（默认）| two-element vector of scalars

用于计算二值直方图的阈值，指定为 two-element vector of scalars。该算法使用这些阈值根据极坐标障碍物密度计算二值直方图。高于上限阈值的极坐标障碍物密度值在二值直方图中表示为占用空间 (1)。小于下限阈值的值表示为空闲空间 (0)。介于限制之间的值将设置为先前计算的二值直方图的值（如果先前迭代中存在这样的值）。如果先前直方图不存在，则该值设置为空闲空间 (0)。

### **vehicle radius (m)** — 车辆的半径 `0.1`（默认）| scalar

车辆的半径，指定为 scalar，单位为 meters。此尺寸定义了可以外接车辆的最小圆。计算无障碍方向时，使用 vehicle radius 来考虑车辆大小。

### **Safety distance (m)** — 车辆周围的安全距离 `0.1`（默认）| scalar

除 **vehicle radius** 之外，在车辆位置周围留出的安全距离，指定为 scalar，单位为 meters。
vehicle radius 和安全距离用于计算无障碍方向。

### **Minimum turning radius (m)** — 当前速度下的最小转弯半径 `0.1`（默认）| scalar

车辆以当前速度行驶时的最小转弯半径，指定为 scalar，单位为 meters。

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` — 使用生成的 C 代码仿真模型。第一次运行仿真时，
  Simulink® 为该模块生成 C 代码。只要模型不变，后续仿真将重用
  该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与
  `Interpreted execution` 相当。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真
  模型。此选项缩短启动时间，但仿真速度比 `Code
  generation` 慢。在此模式下，您可以调试模块的源代码。

**可调:** No

#### 代价函数权重

### **Target direction weight** — 目标方向的代价函数权重 `5`（默认）| scalar

朝目标方向移动的代价函数权重，指定为 scalar。要跟随目标方向，请将此权重设置为高于 **Current direction weight** 和 **Previous direction weight** 之和。要忽略目标方向代价，请将此权重设置为 `0`。

### **Current direction weight** — 当前方向的代价函数权重 `2`（默认）| scalar

使车辆沿当前航向方向移动的代价函数权重，指定为 scalar。此权重值越高，生成的路径越高效。要忽略当前方向代价，请将此权重设置为 `0`。

### **Previous direction weight** — 先前方向的代价函数权重 `2`（默认）| scalar

沿先前选择的转向方向移动的代价函数权重，指定为 scalar。此权重值越高，生成的路径越平滑。要忽略先前方向代价，请将此权重设置为 `0`。

## 所属库

Navigation Toolbox / Control Algorithms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用向量场直方图避障

Vector Field Histogram (VFH) 模块使您的车辆能够基于距离传感器数据避开障碍物。给定以距离和角度表示的距离传感器读数，以及要驶向的目标方向，VFH 控制器会计算无障碍转向方向。

有关算法细节的更多信息，请参阅 Algorithms 下的 Vector Field Histogram。
