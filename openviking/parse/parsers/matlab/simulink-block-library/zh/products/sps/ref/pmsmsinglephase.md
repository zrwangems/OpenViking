---
type: simulink-block
title: 'PMSM (Single-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Permanent Magnet'
documentation_page: 'pmsmsinglephase'
documentation_source_path: 'ref/pmsmsinglephase.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM (Single-Phase)

## 端口

### 守恒

### **R** — 机器转子机械旋转

与机器转子关联的机械旋转守恒端口。

### **C** — 机器外壳机械旋转

与机器外壳关联的机械旋转守恒端口。

### **+** — 负电气

与电源正极端子关联的电气守恒端口。

### **-** — 正电气

与电源负极端子关联的电气守恒端口。

### **HS** — 定子热端口热

与定子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口热

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对产生的热量和电机温度的影响进行建模。

### 主要

### **Number of pole pairs** — 转子极对数 `2`（默认）| positive integer

转子上的永磁体极对数。

### **Permanent magnet flux linkage parameterization** — 参数化方法 `Specify flux linkage`（默认）| `Specify back EMF constant`

定子参数化方法。

#### 依赖关系

选择 `Specify flux linkage` 会显示 **Permanent magnet flux linkage** 参数。

选择 `Specify back EMF constant` 会显示 **Back EMF constant** 参数。

### **Permanent magnet flux linkage** — 磁链 `0.2` `Wb`（默认）| positive scalar

峰值永磁体磁链。

#### 依赖关系

为 **Permanent magnet flux linkage parameterization** 参数选择 `Specify flux linkage` 会显示 **Permanent magnet flux linkage** 参数。

### **Back EMF constant** — 反电动势常数 `0.4` `V/(rad/s)`（默认）| positive scalar

反电动势常数。

#### 依赖关系

为 **Permanent magnet flux linkage parameterization** 参数选择 `Specify back EMF constant` 会显示 **Back EMF constant** 参数。

### **Inductance of stator coil** — 电感 `1.15` `H`（默认）| positive scalar

直轴电感。

### **Resistance of stator coil** — 电阻 `150` `Ohm`（默认）| positive scalar

每个定子绕组的电阻。

### **Rotor position at standstill due to asymmetric airgap** — 静止时转子角位置 `45` `deg`（默认）| positive scalar in the interval [0, 360] deg

由于不对称气隙导致的静止时转子角位置。

### 机械

### **Rotor inertia** — 转子转动惯量 `1e-6` `kg*m^2`（默认）| positive scalar

连接到机械旋转端口 **R** 的转子惯量。

### **Rotor damping** — 转子阻尼 `0` `N*m/(rad/s)`（默认）| positive scalar

转子的阻尼。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `K`（默认）| real scalar

电机参数的引用温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| positive scalar

所有三个绕组的电阻与温度关系方程中的系数 α，如“执行器模块热模型”中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Permanent magnet flux temperature coefficient** — 永磁体磁通温度系数 `-0.001` `1/K`（默认）

永磁体磁通密度随温度变化的分数变化率。使用此参数可在温度升高时线性降低转矩和感应反电动势。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| positive scalar

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| positive scalar

转子的热质量。热质量是将转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

单相永磁同步电机

PMSM (Single-Phase) 表示单相永磁同步电机 (PMSM)，这是一种可用于自动化应用的直流电机。

该图展示了单相 PMSM 驱动器的拓扑结构。

该图展示了转子上具有单极对时的电机结构。除非气隙不对称，否则单相 PMSM 不能自启动。

该图展示了 PMSM (Single-Phase) 模块的等效电路。

### 方程

电机电压方程为

vs=Ri+Ldidt+e

and

vs=Vmsin(ωst+ε),

其中：

- *vs* 是电源电压。
- *i* 是瞬时电机电流。
- *R* 是绕组的电阻。
- *L* 是绕组的自感。
- *e* 是反电动势 (BEMF)。
- *ɷs* 是电源电压的角频率。
- *ε* 是电源电压的角度。

反电动势 (BEMF) 为

e=keωesin(θe),

其中：

- *ɷe* 是转子电角速度。
- *θe* 是转子电角度。
- *ke* 是 BEMF 常数。

由于定子与转子之间存在较大的低磁导率间隙，可以忽略饱和。因此，电磁转矩方程为

Te=p i ψmsin(θe)

and

ψm=kep,

其中：

- *Te* 是电磁转矩。
- *ψm* 是永磁体磁链。
- *p* 是极对数。

机械方程为

Jmdωrdt=Te−TL−Bmωr,

其中：

- *Jm* 是转子惯量。
- *TL* 是负载转矩。
- *Bm* 是摩擦系数。
- *ɷr* 是转子机械角速度。

### 对热效应建模

您可以显示热端口，以模拟产生的热量和电机温度的影响。要显示热端口和 **Thermal** 参数，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含用于定子和转子的热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅“在旋转和平移执行器中模拟热效应”。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅“为模块变量设置优先级和初始目标”。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。您可以使用不同来源指定标称值，包括模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅“按标称值进行系统缩放”。
