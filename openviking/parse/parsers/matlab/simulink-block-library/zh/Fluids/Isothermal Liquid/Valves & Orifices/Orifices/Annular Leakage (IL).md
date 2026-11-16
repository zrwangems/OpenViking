---
type: simulink-block
title: 'Annular Leakage (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Orifices'
documentation_page: 'annularleakageil'
documentation_source_path: 'ref/annularleakageil.html'
language: zh-CN
chinese_source: worker-translation
---

# Annular Leakage (IL)

## 端口

### 守恒

### **A** — 液体端口 等温液体

液体进入或离开孔口的入口或出口端口。

### **B** — 液体端口 等温液体

液体进入或离开孔口的入口或出口端口。
### 输入

### **L** — 可变重叠长度 物理信号

可选物理信号端口，提供套筒与环形插入件之间的可变重叠长度。

#### 依赖关系

要显示此端口，请将 **Overlap length specification** 设置为 `Variable`。

### **E** — 可变偏心度 物理信号

可选物理信号端口，提供环形插入件相对于套筒的可变偏心度。

#### 依赖关系

要显示此端口，请将 **Eccentricity specification** 设置为 `Variable`。

## 参数

### **Overlap length specification** — 插入件-套筒重叠的类型 `Constant`（默认）| `Variable`

沿长度方向的套筒-插入件重叠是恒定的还是可变的。

### **Overlap length** — 管与插入件之间的重叠 `1e-3 m`（默认）| 正标量

插入件与管之间沿长度方向的重叠。

#### 依赖关系

要启用此参数，请将 **Overlap length specification** 设置为 `Constant`。

### **Minimum overlap length** — 管与插入件之间的最小重叠 `1e-6 m`（默认）| 正标量

插入件与管之间沿长度方向重叠的下限。任何短于该值的长度都将设置为指定的最小值。

#### 依赖关系

要启用此参数，请将 **Overlap length specification** 设置为 `Variable`。

### **Eccentricity specification** — 偏心度可变性 `Constant`（默认）| `Variable`

孔口偏心度是变化还是保持为设定值。

### **Eccentricity** — 插入件中心相对于套筒中心的偏移 `0 m`（默认）| 正标量

孔口中心与插入件中心之间的距离。

#### 依赖关系

要启用此参数，请将 **Eccentricity specification** 设置为 `Constant`。

### **Inner radius** — 插入件的半径 `9.8e-3 m`（默认）| 正标量

插入件半径 *r*。

### **Outer radius** — 管的半径 `1e-2 m`（默认）| 正标量

管半径 *R*，从管中心到内壁测量。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Orifices

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

对等温流中圆管与圆形插入件之间的环形泄漏进行建模

Annular Leakage (IL) 模块对等温液体网络中圆管与圆形插入件之间的环形泄漏进行建模。插入件可以偏离管中心，并且沿长度方向与管的重叠可以变化。

端口 **A** 和 **B** 对应于孔口入口和出口。输入端口 **L** 和 **E** 是可选物理信号端口，用于对可变重叠长度 (L) 和可变偏心度 (E) 进行建模。

### 质量流量方程

泄漏质量流量根据压力-流量方程计算

m˙=π(R−r)3(R+r)12v(pA−pB)l[1+3εsat2R(R+r)+38ε4(R−r)(R+r)],

其中：

- *R* 是环隙外半径。
- *r* 是环隙内半径。
- *p*A 是端口 **A** 处的压力。
- *p*B 是端口 **B** 处的压力。
- *ν* 是流体运动黏度。
- *l* 是重叠长度。
- ε 是偏心比，ε=eR−r，其中 *e* 是偏心度，可定义为物理信号或常数值。
- *ε*sat 是饱和偏心比，对于恒定孔口它是 ε，对于可变孔口它是连接到端口 **L** 的物理信号。偏心比始终在 0 和 1 之间。

对可变重叠长度建模时，如果物理信号低于 **Minimum overlap length** 参数的值，则使用用户定义的最小重叠长度。

### 假设与限制

该压力-流量方程仅适用于充分发展的层流。可使用 Re=m˙Dhμπ(R2−r2) 确定流动雷诺数，或通过查看 Results Explorer 或 Simulation Data Inspector 中的仿真日志来确定。有关详细信息，请参阅 Data Logging。
