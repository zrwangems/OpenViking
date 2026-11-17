---
type: simulink-block
title: 'Wind Turbine (Mechanical)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical'
documentation_page: 'windturbinemechanical'
documentation_source_path: 'ref/windturbinemechanical.html'
language: zh-CN
chinese_source: worker-translation
---

# Wind Turbine (Mechanical)

## 端口

### 输入

### **V** — 入射风速，m/s，物理信号

与入射风速关联的物理信号输入，单位为 m/s。

### **β** — 桨距角，deg，物理信号

与涡轮叶片桨距角关联的物理信号输入，单位为 deg。

### 守恒

### **R** — 涡轮轴机械旋转

与风力涡轮轴关联的机械旋转守恒端口。

## 参数

### 主要

### **Turbine radius** — 叶尖半径 `80` `m`（默认）| 正标量

从涡轮轮毂中心到叶尖的距离。

### **Pitch angle vector, β** — 参考桨距角 `[0, 3, 5, 10, 20, 90]` `deg`（默认）| 长度为 *M* 的向量

参考集合叶片桨距角。该向量的长度定义了 **Power coefficient table, Cp(β,TSR)** 参数的行数。

### **Tip speed ratio vector, TSR** — 参考叶尖速比 `[0, 2, 4, 6, 8, 10, 12, 14, 15]`（默认）| 长度为 *N* 的向量

参考叶尖速比（TSR）。TSR 是叶尖速度与风速之比。该向量的长度定义了 **Power coefficient table, Cp(β,TSR)** 参数的列数。该模块支持负 TSR 值。这些值必须严格单调递增。

### **Power coefficient table, Cp(β,TSR)** — 功率系数表 *M*×*N*（默认）

给定桨距角和叶尖速比下的功率系数。每一行对应 **Pitch angle vector, β** 参数中的一个元素，每一列对应 **Tip speed ratio vector, TSR** 参数中的一个元素。默认参数值为 `[0.0010, 0.0161, 0.1446, 0.3865, 0.5009, 0.4404, 0.2545, 0.0002, -0.1384; 0.0016, 0.0173, 0.1079, 0.2676, 0.3779, 0.4111, 0.3838, 0.3176, 0.2753; 0.0027, 0.0197, 0.1151, 0.2606, 0.3469, 0.3558, 0.3069, 0.2222, 0.1718; 0.0054, 0.0283, 0.1315, 0.2364, 0.2589, 0.2022, 0.0929, -0.0455, -0.1204; 0.0109, 0.0536, 0.1320, 0.1256, 0.0120, -0.1752, -0.4017, -0.6435, -0.7655; -0.01 * ones(1, 9)]`。

### **Wind speed threshold** — 速度平滑阈值 `0.01` `m/s`（默认）| 正标量

阈值速度平滑位置。当转速接近或越过 0 时，该参数对扭矩、推力和功率进行平滑处理。增大该参数的值时，模块将在更大的速度范围内施加更多平滑。

### **Rotational velocity threshold** — 速度平滑阈值 `0.01` `rad/s`（默认）| 正标量

阈值速度平滑位置。当转速接近或越过 0 时，该参数对扭矩、推力和功率进行平滑处理。增大该参数的值时，模块将在更大的速度范围内施加更多平滑。

### **Air density** — 空气密度 `1.225` `kg/m^3`（默认）| 正标量

空气的恒定密度。

### 机械

### **Include inertia** — 是否对转子惯量建模 `Off`（默认）| `On`

是否对机械平移端口 **R** 的转子惯量建模。

### **Rotor Inertia** — 转子转动惯量 `0.1` `kg*m^2`（默认）| 正标量

连接到机械平移端口 **R** 的转子的惯量。

#### 依赖关系

要启用此参数，请选中 **Include inertia** 参数。

### **Rotor damping** — 转子阻尼 `0` `N*m*s/rad`（默认）| 正标量

转子的阻尼。

## 所属库

Simscape / Electrical / Electromechanical

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

将风动能转换为机械功率的涡轮机

Wind Turbine (Mechanical) 模块表示一个将风动能转换为机械功率的风力涡轮机。涡轮机的功率取决于无量纲功率系数 *Cp*。您可以通过指定 **Power coefficient table, Cp(β,TSR)** 参数，以桨距角和叶尖速比为索引来制表该系数。

物理信号端口 **V** 和 **β** 处的值分别表示风速和集体桨距。端口 **R** 表示与轴相关联的机械旋转守恒端口。

### 方程

该模块通过查表计算功率系数，使得

Cp=tablelookup(βRef,λRef,Cp,Ref,β,λsmooth,interpolation = linear, extrapolation = nearest),

其中：

- *βRef* 是参考桨距角。
- *λRef* 是参考叶尖速比。
- *CP,Ref* 是 **Power coefficient table** 参数。
- *λSmooth* 是平滑后的叶尖速比。

该模块使用此方程作为瞬时叶尖速比的基础

λ=RωV,

其中：

- *R* 是 **Turbine radius** 参数。
- *ɷ* 是轴与壳体之间的微分角速度。
- *V* 是作用在转子上的入射风速。该值是物理信号输入端口 **V**。

该模块使用此方程来描述瞬时叶尖速比方程的平滑版本

λSmooth=RωV(V2+VThr2),

其中 *VThr* 是 **Wind speed threshold** 参数。该模块使用此方程作为功率的基础

Power=12CpρAV3=Torque⋅ω,

其中：

- *ρ* 是 **Air density** 参数。
- *A* 是涡轮机叶片扫过的圆的面积，且 *A = πr2*。

要将模块参数与风力涡轮机机械额定功率关联起来，请确定在峰值功率系数和额定风速下的风力涡轮机功率。额定功率通过以下方程与模块参数对应

Powerrated=12CP,maxρAVrated3,

其中：

- *CP,max* 是峰值功率系数。这是 **Power coefficient table, Cp(β,TSR)** 参数中的最大值。
- *Vrated* 是额定风速。额定风速通常为 10 至 15 m/s。风力涡轮机控制器的设计可以在该风速下改变策略以维持额定功率。
- *A* 是转子扫掠面积，其中 *A = πr2*。

该模块对功率使用数值平滑方程，使得

PowerSmooth=CPρA(V2+Vthr2)3/22.

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
