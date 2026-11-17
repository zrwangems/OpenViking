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
```yaml
ports:
- name: A
  summary: 液体端口，等温液体
  direction: conserving
- name: B
  summary: 液体端口，等温液体
  direction: conserving
- name: L
  summary: 可变重叠长度，物理信号
  direction: input
- name: E
  summary: 可变偏心距，物理信号
  direction: input
```

### 守恒端口

### **A** — 液体端口，等温液体

液体进入或离开节流孔的入口或出口端口。

### **B** — 液体端口，等温液体

液体进入或离开节流孔的入口或出口端口。
### 输入

### **L** — 可变重叠长度，物理信号

可选的物理信号端口，提供套筒与环形插入件之间的可变重叠长度。

#### 依赖关系

要显示此端口，请将 **Overlap length specification** 设置为
`Variable`。

### **E** — 可变偏心距，物理信号

可选的物理信号端口，提供环形插入件相对于套筒的可变偏心距。

#### 依赖关系

要显示此端口，请将 **Eccentricity specification** 设置为
`Variable`。
## 参数
```yaml
parameters:
- name: Overlap length specification
  summary: 插入件-套筒重叠类型 Constant（默认）| Variable
  group: ''
- name: Overlap length
  summary: 管与插入件之间的重叠 1e-3 m（默认）| 正标量
  group: ''
- name: Minimum overlap length
  summary: 管与插入件之间的最小重叠 1e-6 m（默认）| 正标量
  group: ''
- name: Eccentricity specification
  summary: 偏心距可变性 Constant（默认）| Variable
  group: ''
- name: Eccentricity
  summary: 插入件中心相对于套筒中心的偏移 0 m（默认）| 正标量
  group: ''
- name: Inner radius
  summary: 插入件半径 9.8e-3 m（默认）| 正标量
  group: ''
- name: Outer radius
  summary: 管半径 1e-2 m（默认）| 正标量
  group: ''
```

### **Overlap length specification** — 插入件-套筒重叠类型 `Constant`（默认）| `Variable`

沿长度方向的套筒-插入件重叠是恒定的还是可变的。

### **Overlap length** — 管与插入件之间的重叠 `1e-3 m`（默认）| 正标量

插入件与管之间沿长度方向的重叠。

#### 依赖关系

要启用此参数，请将 **Overlap length specification** 设置为
`Constant`。

### **Minimum overlap length** — 管与插入件之间的最小重叠 `1e-6 m`（默认）| 正标量

插入件与管之间沿长度方向重叠的下限。任何短于此值的长度都将被设置为指定的最小值。

#### 依赖关系

要启用此参数，请将 **Overlap length specification** 设置为
`Variable`。

### **Eccentricity specification** — 偏心距可变性 `Constant`（默认）| `Variable`

节流孔偏心距是变化还是保持在设定值。

### **Eccentricity** — 插入件中心相对于套筒中心的偏移 `0 m`（默认）| 正标量

节流孔中心与插入件中心之间的距离。

#### 依赖关系

要启用此参数，请将 **Eccentricity specification** 设置为
`Constant`。

### **Inner radius** — 插入件半径 `9.8e-3 m`（默认）| 正标量

插入件半径 *r*。

### **Outer radius** — 管半径 `1e-2 m`（默认）| 正标量

管半径 *R*，从管中心测量到内壁。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

对等温流动中圆管与圆形插入件之间的环形泄漏进行建模

Annular Leakage (IL) 模块对等温液体网络中圆管与圆形插入件之间的环形泄漏进行建模。插入件可以偏离管的中心，并且可以与管具有不同的沿长度方向重叠。

端口 **A** 和 **B** 分别对应节流孔入口和出口。输入端口 **L** 和 **E** 是可选的物理信号端口，用于对可变重叠长度（L）和可变偏心距（E）进行建模。

### 质量流量方程

泄漏质量流量由压力-流量方程计算

m˙=π(R−r)3(R+r)12v(pA−pB)l[1+3εsat2R(R+r)+38ε4(R−r)(R+r)]，

其中：

- *R* 是环形外半径。
- *r* 是环形内半径。
- *p*A 是端口 **A** 处的压力。
- *p*B 是端口 **B** 处的压力。
- *ν* 是流体运动黏度。
- *l* 是重叠长度。
- ε 是偏心比，ε=eR−r，其中 *e* 是偏心距，可以定义为物理信号或常数值。
- *ε*sat 是饱和偏心比，对于恒定节流孔为 ε，对于可变节流孔为连接到端口 **L** 的物理信号。偏心比始终介于 0 和 1 之间。

当对可变重叠长度进行建模时，如果物理信号低于 **Minimum overlap length** 参数的值，则使用用户定义的最小重叠长度。

### 假设与限制

压力-流量方程仅对充分发展的层流有效。流动雷诺数可以使用 Re=m˙Dhμπ(R2−r2) 确定，也可以通过查看 Results Explorer 或 Simulation Data Inspector 中的仿真日志来确定。有关更多信息，请参见 Data Logging。
