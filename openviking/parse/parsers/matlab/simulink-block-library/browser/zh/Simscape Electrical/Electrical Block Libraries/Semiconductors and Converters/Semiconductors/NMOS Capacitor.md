---
type: simulink-block
title: 'NMOS Capacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'nmoscapacitor'
documentation_source_path: 'ref/nmoscapacitor.html'
language: zh-CN
chinese_source: worker-translation
---

# NMOS Capacitor

## 端口

### 守恒

### **G** — 栅极端子电气

与 NMOS Capacitor 的栅极端子关联的电气守恒端口。

### **B** — 体极端子电气

与 NMOS Capacitor 的体极端子关联的电气守恒端口。

## 参数

若要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条上的 **仿真** 选项卡中，在 **准备** 库中，选择 **属性检查器**。

### 主要

### **电容器模型** — 电容器的参数化选项 `Fundamental nonlinear equations`（默认）| `Lookup table (2-D, temperature dependent)`

电容器的参数化选项。要直接指定方程参数，请将此参数设置为 `Fundamental nonlinear equations`。要手动将 C-V 特性制成表格，请将此参数设置为 `Lookup table (2-D, temperature dependent)`。

### **栅-体电容查找表, Cgb(T,Vgb)** — 栅-体电容的查找表 `[3.4574, 3.4541, 3.4407, 3.4274, 3.404, 3.374, 3.3339, 3.2938, 3.227, 3.1402, 3.0467, 2.9332, 2.8063, 2.6828, 2.5426, 2.3255, 2.0985, 1.7679, 1.5576, 1.2671, .9466, .6895, .4691, .2688, .182, .1386, .1152, .1085, .0952, .0851, .0851, .0785, .0751, .0751, .0751]` `nF`（默认）| 正元素向量或矩阵

栅-体电容的查找表，指定为温度和栅-体电压的函数。行数必须等于 **温度, T** 参数的元素数。列数必须等于 **栅-体电压, Vgb** 参数的元素数。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Lookup table (2-D, temperature dependent)`。

### **温度, T** — 栅-体电容查找表的温度 `25` `degC`（默认）| 标量 | 向量

栅-体电容查找表的温度。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Lookup table (2-D, temperature dependent)`。

### **栅-体电压, Vgb** — 栅-体电压 `[-2.9897, -2.8711, -2.7216, -2.5052, -2.2887, -2.0464, -1.8402, -1.6701, -1.4948, -1.3608, -1.2526, -1.1624, -1.1031, -1.0567, -1.0077, -.9536, -.9149, -.8686, -.8428, -.8093, -.7706, -.7268, -.6804, -.6082, -.5, -.4021, -.3015, -.2216, -.134, -.0309, .0851, .201, .3995, .7165, .9897]` `V`（默认）| 向量

栅-体电压。此向量的元素必须严格按升序排列。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Lookup table (2-D, temperature dependent)`。

### 半导体材料参数

### **氧化层电容, Cox** — 电容器的总氧化层电容 `345.31` `nF`（默认）| 正标量

电容器的总氧化层电容。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Fundamental nonlinear equations`。

### **带隙能量, EG** — 带隙能量 `1.12` `eV`（默认）| 标量

带隙能量。将此参数设置为适合电容器中半导体材料的值。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Fundamental nonlinear equations`。

### **阈值电压, Vth** — 反型模式的阈值栅极电压 `1.1471` `V`（默认）| 标量

阈值栅极电压。如果栅-体电压大于或等于此参数的值，则 NMOS Capacitor 进入反型模式。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Fundamental nonlinear equations`。

### **表面电势, phib** — 表面电势 `0.9338` `V`（默认）| 正标量

半导体表面电势，在该电势下，表面少数载流子浓度等于体区多数载流子浓度。模块在此值处耗尽模式和反型模式之间转换。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Fundamental nonlinear equations`。

### **体因子, gamma** — 体效应参数 `1.1798` `V^(1/2)`（默认）| 正标量

体效应参数，它将阈值电压 `Vth` 与平带电压相关联。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Fundamental nonlinear equations`。

### **对强反型下的高频 C-V 行为建模** — 对强反型模式的高频 C-V 行为建模的选项 `off`（默认）| `on`

用于对强反型模式的高频 C-V 行为建模的选项。如果清除此参数，则模块假定少数载流子可以快速响应电压变化，并在氧化物下方形成反型层电荷。否则，模块假定少数载流子没有足够的时间快速响应电压变化并在 MOS 电容器的氧化层下方形成反型层电荷。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Fundamental nonlinear equations`。

### **测量温度** — 模块引用参数时的温度 `25` `degC`（默认）| 正标量

模块引用这些参数时的温度。

#### 依赖关系

要启用此参数，请将 **电容器模型** 设置为 `Fundamental nonlinear equations`。

### 温度依赖性

### **参数化** — 指定器件仿真温度的选项 `None - Simulate at parameter measurement temperature`（默认）| `Model temperature dependence`

用于指定器件仿真温度的选项。

如果将此参数设置为 `None - Simulate at parameter measurement temperature`，并将 **电容器模型** 设置为 `Lookup table (2-D, temperature dependent)`，则模块使用 25 `degC` 的仿真温度。

### **器件仿真温度** — 仿真器件时的温度 `25` `degC`（默认）| 正标量

仿真器件时的温度。

#### 依赖关系

要启用此参数，请设置以下选项之一：

- **电容器模型** 为 `Fundamental nonlinear equations`，且 **参数化** 为 `Model temperature dependence`。
- **电容器模型** 为 `Lookup table (2-D, temperature dependent)`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

N 型金属氧化物半导体电容器

NMOS Capacitor 模块表示 N 型金属氧化物半导体（NMOS）电容器。您可以使用 MOS 方程参数对此模块进行参数化，也可以使用表格式电容查找表将这些值参数化为温度和电压的函数。

此图显示了构成 MOS 电容器的元件：

MOS 电容器的示意图。顶部元件是栅极，中间元件是氧化物组件，底部元件是半导体。

NMOS Capacitor 模块使用 P 型体半导体。

### 基于方程的模型

当您将 **电容器模型** 参数设置为 `Fundamental nonlinear equations` 时，NMOS Capacitor 模块根据栅-体电压 `Vgb`、平带电压 `Vfb` 和阈值电压 `Vth` 在三种工作模式下运行：

- Vgb<Vfb — 积累模式。金属板上的电压将体区材料的多数载流子（即空穴）积累在半导体表面。
- Vfb≤Vgb<Vth — 耗尽模式。施加的电压感应出少数载流子（即电子），并在表面形成耗尽区。
- Vgb≥Vth — 反型模式。半导体表面的多数载流子类型发生反转。

为计算平带电压，模块使用以下方程：

Vfb=Vth−φ−γφ,

其中 *γ* 是体因子，*φ* 是表面电势。

模块使用以下方程调整表面电势 *φ* 的值

φ(Tsim)=kTsimqlog(TmeasTsim)3+TsimTmeasφ(Tmeas)+EG(1−TsimTmeas),

其中：

- *Tsim* 是 **器件仿真温度** 参数的值，单位为 Kelvin。
- *Tmeas* 是 **测量温度** 参数的值，单位为 Kelvin。
- *EG* 是 **带隙能量** 参数的值，单位为 electron-volts。模块假定此参数与温度无关。
- *q* 是电子电荷，单位为 Coulomb，等于 `1.60217663e-19` `C`。
- *k* 等于 `1.380649e-23` `J/K`。

此方程定义电容器的总栅极电荷 `QG`，

QG=−(Qacc+Qdep+Qinv),

其中：

- *Qacc* 是多数载流子形成的积累电荷。
- *Qdep* 是半导体层内的耗尽区电荷。
- *Qinv* 是少数载流子形成的反型电荷。

**积累模式**

当栅-体电压小于平带电压时，模块进入积累工作模式。在积累模式下，多数载流子积累在半导体表面。模块使用以下方程计算积累电荷、耗尽电荷和反型电荷：

Qacc=−Cox⋅(Vgb−Vfb)Qdep=0Qinv=0

其中 *Cox* 是总氧化层电容。

**耗尽模式**

当栅-体电压小于阈值栅极电压且大于或等于平带电压时，模块进入耗尽工作模式。在耗尽模式下，少数载流子堆积在半导体表面。模块使用以下方程计算积累电荷、耗尽电荷和反型电荷：

Qacc=0Qdep=Coxγ22(1−1+4(Vgb−Vfb)γ2)Qinv=0

其中 *Cox* 是总氧化层电容，*γ* 是体因子。

**反型模式**

当栅-体电压大于或等于阈值栅极电压时，模块进入反型工作模式。在反型模式下，半导体表面的多数载流子类型发生反转。模块使用以下方程计算积累电荷、耗尽电荷和反型电荷：

Qacc=0Qdep={Coxγ22(1−1+4(Vth−Vfb)γ2)if you clear Model high-frequency C-V behavior at strong inversionCoxγ22(1−1+4(Vth−Vfb)γ2)−CGB,th⋅(Vgb−Vth)if you select Model high-frequency C-V behavior at strong inversion}Qinv={−Cox⋅(Vgb−Vth)if you clear Model high-frequency C-V behavior at strong inversion0if you select Model high-frequency C-V behavior at strong inversion}

其中 *Cox* 是总氧化层电容，*γ* 是体因子，且 CGB,th=Cox1+CoxCdep=CoxCdepCox+Cdep 是反型阈值处的栅-体电容，它等效于 *Cox* 和 *Cdep* 串联。*Cdep* 是耗尽层电容。

如果选择 **对强反型下的高频 C-V 行为建模** 参数，则模块假定少数载流子没有足够的时间对施加电压的变化做出反应。因此，反型电荷 *Qinv* 为零，施加电压降在氧化层电容和耗尽区电容上。

如果清除 **对强反型下的高频 C-V 行为建模** 参数，则模块假定少数载流子有足够的时间快速响应电压变化，并在 MOS 电容器的氧化层下方形成反型层电荷。

### 表格式模型

当您将 **电容器模型** 参数设置为 `Lookup table (2-D, temperature dependent)` 时，NMOS Capacitor 模块将电容器的总栅极电荷 `QG` 制成电压和温度的表。要使用表格式电容查找表将模块参数参数化为温度和电压的函数，请指定 **栅-体电容查找表, Cgb(T,Vgb)**、**栅-体电压, Vgb** 和 **温度, T** 参数。

如果仅在 **温度, T** 参数中指定一个值，则电容器的 C-V 特性将与温度无关。

为确保在一个完整 AC 周期内栅极电荷守恒，模块将 **栅-体电容查找表, Cgb(T,Vgb)** 参数转换为等效电荷查找表。模块使用此等效电荷表，通过线性插值和外推方法计算栅极电荷 *Qg* 随电压的变化。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅按标称值进行系统缩放。
