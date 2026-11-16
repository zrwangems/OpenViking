---
type: simulink-block
title: 'Path Smoother Spline'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'pathsmootherspline'
documentation_source_path: 'ref/pathsmootherspline.html'
language: zh-CN
chinese_source: worker-translation
---

# Path Smoother Spline

## 端口

### 输入

### **RefPoses** — 参考位姿，[*x*, *y*, *Θ*] 向量的 *M*×3 矩阵

沿路径的车辆参考位姿，指定为 [*x*, *y*, *Θ*] 向量的 *M*×3 矩阵，其中 *M* 是位姿数量。

*x* 和 *y* 指定车辆的位置，单位为 meters。*Θ* 指定车辆的朝向角，单位为 degrees。

**数据类型：** `single` | `double`

### **RefDirections** — 参考方向，1（前进运动）和 –1（倒车运动）的 *M*×1 列向量

沿路径的车辆参考方向，指定为由 1（前进运动）和 –1（倒车运动）组成的 *M*×1 列向量。*M* 是参考方向数量。**RefDirections** 的每个元素对应于 **RefPoses** 输入端口中的一个位姿。

**数据类型：** `single` | `double`
### 输出

### **Poses** — 平滑路径的离散位姿，[*x*, *y*, *Θ*] 向量的 *N*×3 矩阵

平滑路径的离散位姿，以 [*x*, *y*, *Θ*] 向量的 *N*×3 矩阵形式返回。*N* 是 **Number of output poses** 参数中指定的位姿数量。

*x* 和 *y* 指定车辆的位置，单位为 meters。*Θ* 指定车辆的朝向角，单位为 degrees。

**Poses** 中的值与 **RefPoses** 输入端口中的值具有相同的数据类型。

### **Directions** — 每个输出位姿处的行驶方向，1（前进运动）和 –1（倒车运动）的 *N*×1 列向量

车辆在 **Poses** 中每个输出位姿处的行驶方向，以由 1（前进运动）和 –1（倒车运动）组成的 *N*×1 列向量形式返回。*N* 是 **Number of output poses** 参数中指定的位姿数量。

**Directions** 中的值与 **RefDirections** 输入端口中的值具有相同的数据类型。

您可以使用 **Directions** 指定车辆的参考路径。您还可以将 **Directions** 与 **CumLengths** 和 **Curvatures** 一起使用，为车辆生成参考速度剖面。请参阅 Velocity Profiler 模块和 Automated Parking Valet in Simulink 示例。

### **CumLengths** — 累积路径长度，*N*×1 实值列向量

**Poses** 中每个输出位姿处的累积路径长度，以 *N*×1 实值列向量形式返回。*N* 是 **Number of output poses** 参数中指定的位姿数量。单位为 meters。

您可以将 **CumLengths** 与 **Directions** 和 **Curvatures** 一起使用，为车辆生成参考速度剖面。请参阅 Velocity Profiler 模块和 Automated Parking Valet in Simulink 示例。

#### 依赖项

要启用此端口，请选择 **Show CumLengths and Curvatures output ports** 参数。

### **Curvatures** — 带符号路径曲率，*N*×1 实值列向量

**Poses** 中每个输出位姿处的带符号路径曲率，以 *N*×1 实值列向量形式返回。*N* 是 **Number of output poses** 参数中指定的位姿数量。单位为 radians per meter。

您可以将 **Curvatures** 与 **Directions** 和 **CumLengths** 一起使用，为车辆生成参考速度剖面。请参阅 Velocity Profiler 模块和 Automated Parking Valet in Simulink 示例。

#### 依赖项

要启用此端口，请选择 **Show CumLengths and Curvatures output ports** 参数。

## 参数

### **Number of output poses** — 要返回的平滑位姿数量 `100`（默认）| positive integer

要在 **Poses** 输出端口中返回的平滑位姿数量，指定为正整数。要提高所返回位姿的粒度，请增加此参数值。

### **Minimum separation of input poses** — 位姿之间的最小间隔 `1e-3`（默认）| positive real scalar

位姿之间的最小间隔，单位为 meters，指定为正实数标量。如果两个位姿之间的欧几里得 (*x*, *y*) 距离小于此值，则该模块仅使用这些位姿中的一个进行插值。

### **Sample time** — 采样时间 `-1`（默认）| positive real scalar

模块的采样时间，单位为 seconds，指定为 `-1` 或正实数标量。默认值 `-1` 表示该模块从上游模块继承采样时间。

### **Show CumLengths and Curvatures output ports** — 输出累积路径长度和曲率 `off`（默认）| `on`

选择此参数可启用 **CumLengths** 和 **Curvatures** 输出端口。

### **Simulate using** — 要运行的仿真类型 `Code Generation`（默认）| `Interpreted Execution`

- `Code generation` — 使用生成的 C/C++ 代码仿真模型。第一次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不更改，C 代码就会在后续仿真中重用。此选项需要额外的启动时间。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。

## 所属库

Automated Driving Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

使用三次样条插值平滑车辆路径

Path Smoother Spline 模块通过将输入参考路径位姿拟合到三次样条，生成由一系列离散位姿组成的平滑车辆路径。给定输入参考路径方向，该模块还返回与每个位姿对应的方向。

使用此模块将 C1 连续路径转换为 C2 连续路径。C1 连续路径包括由路径规划器返回的 Dubins 或 Reeds-Shepp 路径。有关这些路径类型的更多详细信息，请参阅 C1-Continuous and C2-Continuous Paths。

您可以将返回的位姿和方向与车辆控制器（例如 Lateral Controller Stanley 模块）一起使用。
