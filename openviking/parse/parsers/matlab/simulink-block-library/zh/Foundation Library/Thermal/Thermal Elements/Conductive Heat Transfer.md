---
type: simulink-block
title: 'Conductive Heat Transfer'
family: 'simscape'
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

### **K** — 热导率控制信号，W/(K\*m) 物理信号

控制热导率的输入物理信号。当该值超出 **Minimum thermal conductivity** 参数指定的最小限值时，信号饱和。

#### 依赖

要启用此端口，请将 **Conductivity type** 参数设置为 `Variable input`。
### 守恒

### **A** — 层 A 热

与层 A 关联的热守恒端口。

### **B** — 层 B 热

与层 B 关联的热守恒端口。对于圆柱壁几何形状，层 B 是内层。

## 参数

### **Conductivity type** — 如何指定热导率 `Constant`（默认）| `Variable input` | `Tabulated data`

是否将热导率指定为：

- `Constant` — 热导率在仿真期间保持恒定。您使用 **Thermal conductivity** 参数指定热导率。
- `Variable input` — 您使用端口 **K** 处的输入物理信号指定热导率，该信号可在仿真期间变化。**Minimum thermal conductivity** 参数指定物理信号的下界。
- `Tabulated data` — 您使用基于温度的查找表指定热导率。在这种情况下，热导率也可以在仿真期间变化。

### **Wall geometry** — 热传导的壁形状 `Planar`（默认）| `Cylindrical`

热传导的壁形状，指定为：

- `Planar` — 热传递通过平坦的矩形壁进行。指定壁面积和厚度。
- `Cylindrical` — 热传递通过圆管壁进行。指定管道内径、外径和长度。

### **Area** — 传热面积 `1e-4 m^2`（默认）| 正标量

垂直于热流方向的传热面积。

#### 依赖

要启用此参数，请将 **Wall geometry** 设置为 `Planar`。

### **Thickness** — 材料厚度 `0.1 m`（默认）| 正标量

材料厚度，即层之间的距离。

#### 依赖

要启用此参数，请将 **Wall geometry** 设置为 `Planar`。

### **Inner diameter** — 管道内径 `0.05 m`（默认）| 正标量

管道内径，即材料内层的直径。

#### 依赖

要启用此参数，请将 **Wall geometry** 设置为 `Cylindrical`。

### **Outer diameter** — 管道外径 `0.1 m`（默认）| 正标量

管道外径，即材料外层的直径。

#### 依赖

要启用此参数，请将 **Wall geometry** 设置为 `Cylindrical`。

### **Length** — 管道长度 `1 m`（默认）| 正标量

管道长度。

#### 依赖

要启用此参数，请将 **Wall geometry** 设置为 `Cylindrical`。

### **Thermal conductivity** — 材料的热导率 `401 W/(K*m)`（默认）| 正标量

材料的热导率。

#### 依赖

要启用此参数，请将 **Conductivity type** 设置为 `Constant`。

### **Minimum thermal conductivity** — 热导率的下界 `10 W/(K*m)`（默认）| 正标量

热导率值的下界。端口 **K** 处的输入信号在此值处饱和，以防止热导率进一步降低。

#### 依赖

要启用此参数，请将 **Conductivity type** 设置为 `Variable input`。

### **Thermal conductivity vector** — 用于表查找的热导率值向量 `[413, 401, 392, 383, 371, 357, 342] W/(K*m)`（默认）| 正值向量

与 **Temperature vector** 参数值对应的热导率值向量。向量大小必须与 **Temperature vector** 参数相同。该模块使用模块的平均温度、线性插值和最近外推来执行热导率的一维表查找。有关插值和外推算法的更多信息，请参阅 PS Lookup Table (1D)。

#### 依赖关系

要启用此参数，请将 **Conductivity type** 设置为 `Tabulated data`。

### **Temperature vector** — 用于表查找的温度值向量 `[200, 273, 400, 600, 800, 1000, 1200] K`（默认）| 严格递增向量

与 **Thermal conductivity vector** 参数值对应的温度值向量。该向量必须严格递增。各值可以是非均匀间隔的。该向量必须至少包含两个值。

#### 依赖关系

要启用此参数，请将 **Conductivity type** 设置为 `Tabulated data`。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2022b：对圆管壁的变热导率和传热进行建模

新增的 **Conductivity type** 参数允许热导率为常数（由 **Thermal conductivity** 参数指定）或可变。您可以将可变热导率指定为端口 **K** 处的物理信号，或指定为基于温度的表查找。

此外，您可以将新增的 **Wall geometry** 参数设置为 `Planar` 或 `Cylindrical`。`Planar` 指平坦的矩形壁。`Cylindrical` 指圆管壁。

在默认配置中，当 **Conductivity type** 设置为 `Constant` 且 **Wall geometry** 设置为 `Planar` 时，该模块的功能与之前版本相同。

## 描述

通过传导进行的热传递

Conductive Heat Transfer 模块表示同一材料的两个层之间通过传导进行的热传递。对于平面，傅里叶定律描述该传递，

Q=k⋅AD(TA−TB)，

其中：

- *Q* 是热流量。
- *k* 是材料的热导率。
- *A* 是垂直于热流方向的面积。
- *D* 是层之间的距离，即材料厚度。
- *T*A 是层 A 的温度。
- *T*B 是层 B 的温度。

通过圆管壁的热传导为

Qcyl=2πk⋅Lln(doutdin)(TA−TB)，

其中：

- *L* 是管道长度。
- *d*in 是内径。
- *d*out 是外径。

您可以通过 **Conductivity type** 参数指定热导率：

- `Constant` — 热导率在仿真期间保持恒定。您通过 **Thermal conductivity** 参数指定热导率。
- `Variable input` — 您使用端口 **K** 处的输入物理信号指定热导率，该信号可在仿真期间变化。**Minimum thermal conductivity** 参数指定物理信号的下界。
- `Tabulated data` — 您使用基于温度的查找表指定热导率。在这种情况下，热导率也可以在仿真期间变化。

`Tabulated data` 选项使用模块的平均温度来查找热导率。对于平面壁几何，平均温度为

Tavg=TA+TB2。

对于圆柱壁几何，平均温度为

Tavg=(TA−TB)⋅(doutdout−din−1ln(doutdin))+TB，

其假设 *T*B 位于圆柱内侧。

**A** 和 **B** 是与材料层相关的热守恒端口。由于模块正方向是从端口 **A** 到端口 **B**，因此如果热流从 **A** 流向 **B**，则热流为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
