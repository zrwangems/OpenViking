---
type: simulink-block
title: 'Conductive Heat Transfer'
family: 'thermal'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'conductiveheattransfer'
documentation_source_path: 'ref/conductiveheattransfer.html'
language: zh-CN
chinese_source: worker-translation
---

# Conductive Heat Transfer

## 端口

### 输入

### **K** — Thermal conductivity control signal, W/(K\*m) physical signal

控制热导率的输入物理信号。当值超出 **Minimum thermal conductivity** 参数指定的最小限制时，该信号饱和。

#### 依赖关系

要启用此端口，请将 **Conductivity type** 参数设置为 `Variable input`。
### 守恒

### **A** — Layer A thermal

与层 A 关联的热守恒端口。

### **B** — Layer B thermal

与层 B 关联的热守恒端口。对于圆柱壁几何，层 B 是内层。

## 参数

### **Conductivity type** — How to specify thermal conductivity `Constant`（默认） | `Variable input` | `Tabulated data`

是否将热导率指定为：

- `Constant` — 热导率在仿真期间保持恒定。您使用 **Thermal conductivity** 参数指定热导率。
- `Variable input` — 您使用端口 **K** 处的输入物理信号指定热导率，该信号可在仿真期间变化。**Minimum thermal conductivity** 参数指定该物理信号的下界。
- `Tabulated data` — 您使用基于温度的查找表指定热导率。在这种情况下，热导率也可在仿真期间变化。

### **Wall geometry** — Wall shape for heat conduction `Planar`（默认） | `Cylindrical`

用于热传导的壁形状，指定为：

- `Planar` — 热传递通过平坦的矩形壁。指定壁面积和厚度。
- `Cylindrical` — 热传递通过圆管壁。指定管道内径、外径和长度。

### **Area** — Area of heat transfer `1e-4 m^2`（默认） | positive scalar

垂直于热流方向的热传递面积。

#### 依赖关系

要启用此参数，请将 **Wall geometry** 设置为 `Planar`。

### **Thickness** — Thickness of material `0.1 m`（默认） | positive scalar

材料厚度，即层之间的距离。

#### 依赖关系

要启用此参数，请将 **Wall geometry** 设置为 `Planar`。

### **Inner diameter** — Inner diameter of pipe `0.05 m`（默认） | positive scalar

管道内径，即材料内层的直径。

#### 依赖关系

要启用此参数，请将 **Wall geometry** 设置为 `Cylindrical`。

### **Outer diameter** — Outer diameter of pipe `0.1 m`（默认） | positive scalar

管道外径，即材料外层的直径。

#### 依赖关系

要启用此参数，请将 **Wall geometry** 设置为 `Cylindrical`。

### **Length** — Pipe length `1 m`（默认） | positive scalar

管道长度。

#### 依赖关系

要启用此参数，请将 **Wall geometry** 设置为 `Cylindrical`。

### **Thermal conductivity** — Thermal conductivity of the material `401 W/(K*m)`（默认） | positive scalar

材料的热导率。

#### 依赖关系

要启用此参数，请将 **Conductivity type** 设置为 `Constant`。

### **Minimum thermal conductivity** — Lower bound for thermal conductivity `10 W/(K*m)`（默认） | positive scalar

热导率值的下界。端口 **K** 处的输入信号在此值处饱和，以防止热导率进一步降低。

#### 依赖关系

要启用此参数，请将 **Conductivity type** 设置为 `Variable input`。

### **Thermal conductivity vector** — Vector of thermal conductivity values for use in table lookup `[413, 401, 392, 383, 371, 357, 342] W/(K*m)`（默认） | vector of positive values

热导率值向量，对应于 **Temperature vector** 参数值。向量大小必须与 **Temperature vector** 参数相同。模块使用模块的平均温度、线性插值和最近邻外插执行热导率的一维表查找。有关插值和外插算法的更多信息，请参阅 PS Lookup Table (1D)。

#### 依赖关系

要启用此参数，请将 **Conductivity type** 设置为 `Tabulated data`。

### **Temperature vector** — Vector of temperature values for use in table lookup `[200, 273, 400, 600, 800, 1000, 1200] K`（默认） | strictly increasing vector

温度值向量，对应于 **Thermal conductivity vector** 参数值。向量必须严格递增。值可以非均匀间隔。向量必须至少包含两个值。

#### 依赖关系

要启用此参数，请将 **Conductivity type** 设置为 `Tabulated data`。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2022b：对可变热导率和通过圆管壁的热传递进行建模

新的 **Conductivity type** 参数使热导率可以是常量（通过 **Thermal conductivity** 参数指定）或变量。您可以将可变热导率指定为端口 **K** 处的物理信号，或指定为基于温度的查找表。

此外，您可以将新的 **Wall geometry** 参数设置为 `Planar` 或 `Cylindrical`。`Planar` 指平坦的矩形壁。`Cylindrical` 指圆管壁。

在默认配置中，当 **Conductivity type** 设置为 `Constant` 且 **Wall geometry** 设置为 `Planar` 时，模块的功能与先前版本相同。

## 描述

通过传导的热传递

Conductive Heat Transfer 模块表示同一材料的两个层之间的热传导。对于平面，傅里叶定律描述该传递：

Q=k⋅AD(TA−TB),

其中：

- *Q* 是热流。
- *k* 是材料的热导率。
- *A* 是垂直于热流方向的面积。
- *D* 是层之间的距离，即材料厚度。
- *T*A 是层 A 的温度。
- *T*B 是层 B 的温度。

通过圆管壁的热传导为

Qcyl=2πk⋅Lln(doutdin)(TA−TB),

其中：

- *L* 是管道长度。
- *d*in 是内径。
- *d*out 是外径。

您可以使用 **Conductivity type** 参数指定热导率：

- `Constant` — 热导率在仿真期间保持恒定。您使用 **Thermal conductivity** 参数指定热导率。
- `Variable input` — 您使用端口 **K** 处的输入物理信号指定热导率，该信号可在仿真期间变化。**Minimum thermal conductivity** 参数指定该物理信号的下界。
- `Tabulated data` — 您使用基于温度的查找表指定热导率。在这种情况下，热导率也可在仿真期间变化。

`Tabulated data` 选项使用模块的平均温度来查找热导率。对于平面壁几何，平均温度为

Tavg=TA+TB2.

对于圆柱壁几何，平均温度为

Tavg=(TA−TB)⋅(doutdout−din−1ln(doutdin))+TB,

该式假设 *T*B 位于圆柱内侧。

**A** 和 **B** 是与材料层关联的热守恒端口。由于模块正方向是从端口 **A** 到端口 **B**，如果热流从 **A** 流向 **B**，则热流为正。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 Modify Nominal Values for a Block Variable。
