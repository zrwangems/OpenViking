---
type: simulink-block
title: 'PMOS Capacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'pmoscapacitor'
documentation_source_path: 'ref/pmoscapacitor.html'
language: zh-CN
chinese_source: worker-translation
---

# PMOS Capacitor

## 端口
```yaml
ports:
- name: G
  summary: 栅极端子电气端口
  direction: conserving
- name: B
  summary: 体端子电气端口
  direction: conserving
```

### 守恒端口

### **G** — 栅极端子电气端口

与 NMOS 电容器栅极端子关联的电气守恒端口。

### **B** — 体端子电气端口

与 NMOS 电容器体端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Capacitor model
  summary: 电容器的参数化选项 Fundamental nonlinear equations（默认）| Lookup table (2-D, temperature dependent)
  group: 主要
- name: Gate-bulk capacitance lookup table, Cgb(T,Vgb)
  summary: 栅极-体电容查找表 [3.4574, 3.4541, 3.4407, 3.4274, 3.404, 3.374, 3.3339, 3.2938, 3.227, 3.1402, 3.0467, 2.9332, 2.8063,
    2.6828, 2.5426, 2.3255, 2.0985, 1.7679, 1.5576, 1.2671, .9466, .6895, .4691, .2688, .182, .1386, .1152, .1085, .0952,
    .0851, .08, .0785, .0751, .0751, .0751] nF（默认）| 正元素向量或矩阵
  group: 主要
- name: Temperature, T
  summary: 栅极-体电容查找表的温度 25 degC（默认）| 标量 | 向量
  group: 主要
- name: Gate-bulk voltage, Vgb
  summary: 栅极-体电压 [.9897, .7165, .3995, .201, .0851, -.0309, -.134, -.2216, -.3015, -.4021, -.5, -.6082, -.6804, -.7268, -.7706,
    -.8093, -.8428, -.8686, -.9149, -.9536, -1.0077, -1.0567, -1.1031, -1.1624, -1.2526, -1.3608, -1.4948, -1.6701, -1.8402,
    -2.0464, -2.2887, -2.5052, -2.7216, -2.8711, -2.9897] V（默认）| 向量
  group: 主要
- name: Oxide capacitance, Cox
  summary: 电容器的总氧化层电容 345.31 nF（默认）| 正标量
  group: 半导体材料参数
- name: Band-gap energy, EG
  summary: 带隙能量 1.12 eV（默认）| 标量
  group: 半导体材料参数
- name: Threshold voltage, Vth
  summary: 反型模式的阈值栅极电压 -1.0222 V（默认）| 标量
  group: 半导体材料参数
- name: Surface potential, phib
  summary: 表面势 0.9115 V（默认）| 正标量
  group: 半导体材料参数
- name: Body factor, gamma
  summary: 体效应参数 1.1798 V^(1/2)（默认）| 正标量
  group: 半导体材料参数
- name: Model high-frequency C-V behavior for strong inversion
  summary: 为强反型模式建模高频 C-V 特性的选项 off（默认）| on
  group: 半导体材料参数
- name: Measurement temperature
  summary: 模块引用参数时的温度 25 degC（默认）| 正标量
  group: 半导体材料参数
- name: Parameterization
  summary: 指定器件仿真温度的选项 None - Simulate at parameter measurement temperature（默认）| Model temperature dependence
  group: 温度依赖性
- name: Device simulation temperature
  summary: 仿真器件的温度 25 degC（默认）| 正标量
  group: 温度依赖性
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### 主要

### **Capacitor model** — 电容器的参数化选项 `Fundamental nonlinear equations`（默认）| `Lookup table (2-D, temperature dependent)`

电容器的参数化选项。要直接指定方程参数，请将此参数设置为 `Fundamental nonlinear equations`。要手动将 C-V 特性制成表格，请将此参数设置为 `Lookup table (2-D, temperature dependent)`。

### **Gate-bulk capacitance lookup table, Cgb(T,Vgb)** — 栅极-体电容查找表 `[3.4574, 3.4541, 3.4407, 3.4274, 3.404, 3.374, 3.3339, 3.2938, 3.227, 3.1402, 3.0467, 2.9332, 2.8063, 2.6828, 2.5426, 2.3255, 2.0985, 1.7679, 1.5576, 1.2671, .9466, .6895, .4691, .2688, .182, .1386, .1152, .1085, .0952, .0851, .08, .0785, .0751, .0751, .0751]` `nF`（默认）| 正元素向量或矩阵

栅极-体电容的查找表，指定为温度和栅极-体电压的函数。行数必须等于 **Temperature, T** 参数的元素数。列数必须等于 **Gate-bulk voltage, Vgb** 参数的元素数。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Lookup table (2-D, temperature dependent)`。

### **Temperature, T** — 栅极-体电容查找表的温度 `25` `degC`（默认）| 标量 | 向量

栅极-体电容查找表的温度。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Lookup table (2-D, temperature dependent)`。

### **Gate-bulk voltage, Vgb** — 栅极-体电压 `[.9897, .7165, .3995, .201, .0851, -.0309, -.134, -.2216, -.3015, -.4021, -.5, -.6082, -.6804, -.7268, -.7706, -.8093, -.8428, -.8686, -.9149, -.9536, -1.0077, -1.0567, -1.1031, -1.1624, -1.2526, -1.3608, -1.4948, -1.6701, -1.8402, -2.0464, -2.2887, -2.5052, -2.7216, -2.8711, -2.9897]` `V`（默认）| 向量

栅极-体电压。此向量的元素必须严格按降序排列。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Lookup table (2-D, temperature dependent)`。

### 半导体材料参数

### **Oxide capacitance, Cox** — 电容器的总氧化层电容 `345.31` `nF`（默认）| 正标量

电容器的总氧化层电容。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Fundamental nonlinear equations`。

### **Band-gap energy, EG** — 带隙能量 `1.12` `eV`（默认）| 标量

带隙能量。请将此参数设置为适合电容器中半导体材料的值。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Fundamental nonlinear equations`。

### **Threshold voltage, Vth** — 反型模式的阈值栅极电压 `-1.0222` `V`（默认）| 标量

阈值栅极电压。如果栅极-体电压小于或等于此参数的值，则 PMOS 电容器进入反型模式。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Fundamental nonlinear equations`。

### **Surface potential, phib** — 表面势 `0.9115` `V`（默认）| 正标量

半导体表面势，在该值下表面少数载流子浓度等于体多数载流子浓度。模块在此值处进行耗尽模式和反型模式之间的转换。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Fundamental nonlinear equations`。

### **Body factor, gamma** — 体效应参数 `1.1798` `V^(1/2)`（默认）| 正标量

体效应参数，它将阈值电压 `Vth` 与平带电压关联起来。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Fundamental nonlinear equations`。

### **Model high-frequency C-V behavior for strong inversion** — 为强反型模式建模高频 C-V 特性的选项 `off`（默认）| `on`

为强反型模式建模高频 C-V 特性的选项。如果清除此参数，模块假定少数载流子能够快速响应电压变化，并在氧化层下方形成反型层电荷。否则，模块假定少数载流子没有足够的时间快速响应电压变化并在 MOS 电容器的氧化层下方形成反型层电荷。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Fundamental nonlinear equations`。

### **Measurement temperature** — 模块引用参数时的温度 `25` `degC`（默认）| 正标量

模块引用参数时的温度。

#### 依赖关系

要启用此参数，请将 **Capacitor model** 设置为 `Fundamental nonlinear equations`。

### 温度依赖性

### **Parameterization** — 指定器件仿真温度的选项 `None - Simulate at parameter measurement temperature`（默认）| `Model temperature dependence`

指定器件仿真温度的选项。

如果将此参数设置为 `None - Simulate at parameter measurement temperature`，并将 **Capacitor model** 设置为 `Lookup table (2-D, temperature dependent)`，则模块使用 25 `degC` 的仿真温度。

### **Device simulation temperature** — 仿真器件的温度 `25` `degC`（默认）| 正标量

仿真器件时的温度。

#### 依赖关系

要启用此参数，请设置以下选项之一：

- 将 **Capacitor model** 设置为 `Fundamental nonlinear equations`，并将 **Parameterization** 设置为 `Model temperature dependence`。
- 将 **Capacitor model** 设置为 `Lookup table (2-D, temperature dependent)`。
## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

P 型金属-氧化物-半导体电容器

PMOS Capacitor 模块表示 P 型金属-氧化物-半导体（PMOS）电容器。您可以使用 MOS 方程参数对此模块进行参数化，也可以使用表格化电容查找表将值参数化为温度和电压的函数。

下图显示了构成 MOS 电容器的元件：

MOS 电容器的示意图。顶部元件是栅极，中间元件是氧化物组件，底部元件是半导体。

PMOS Capacitor 模块使用 N 型体半导体。

### 基于方程的模型

当您将 **Capacitor model** 参数设置为 `Fundamental nonlinear equations` 时，PMOS Capacitor 模块根据栅极-体电压 `Vgb`、平带电压 `Vfb` 和阈值电压 `Vth` 的值在三种工作模式下运行：

- Vgb>Vfb — 积累模式。金属板上的电压将体材料的多数载流子（即电子）积累在半导体表面。
- Vth<Vgb≤Vfb — 耗尽模式。电压诱导少数载流子（即空穴）并在表面产生耗尽区。
- Vgb≤Vth — 反型模式。半导体表面的多数载流子类型发生反转。

为计算平带电压，模块使用以下方程：

Vfb=Vth+φ+γφ，

其中 *γ* 是体因子，*φ* 是表面势。

模块使用以下方程调整表面势 *φ* 的值

φ(Tsim)=kTsimqlog(TmeasTsim)3+TsimTmeasφ(Tmeas)+EG(1−TsimTmeas)，

其中：

- *Tsim* 是 **Device simulation temperature** 参数的值，单位为开尔文。
- *Tmeas* 是 **Measurement temperature** 参数的值，单位为开尔文。
- *EG* 是 **Band-gap energy** 参数的值，单位为电子伏特。模块假定此参数与温度无关。
- *q* 是电子电荷，单位为库仑，等于 `1.60217663e-19` `C`。
- *k* 等于 `1.380649e-23` `J/K`。

此方程定义了电容器的总栅极电荷 `QG`，

QG=−(Qacc+Qdep+Qinv)，

其中：

- *Qacc* 是多数载流子形成的积累电荷。
- *Qdep* 是半导体层内的耗尽区电荷。
- *Qinv* 是少数载流子形成的反型电荷。

**积累模式**

当栅极-体电压大于平带电压时，模块进入积累工作模式。在积累模式下，多数载流子积累在半导体表面。模块使用以下方程计算积累电荷、耗尽电荷和反型电荷：

Qacc=−Cox⋅(Vgb−Vfb)Qdep=0Qinv=0

其中 *Cox* 是总氧化层电容。

**耗尽模式**

当栅极-体电压小于或等于平带电压且大于阈值栅极电压时，模块进入耗尽工作模式。在耗尽模式下，少数载流子堆积在半导体表面。模块使用以下方程计算积累电荷、耗尽电荷和反型电荷：

Qacc=0Qdep=Coxγ22(1−4(Vgb−Vfb)γ2−1)Qinv=0

其中 *Cox* 是总氧化层电容，*γ* 是体因子。

**反型模式**

当栅极-体电压小于或等于阈值栅极电压时，模块进入反型工作模式。在反型模式下，半导体表面的多数载流子类型发生反转。模块使用以下方程计算积累电荷、耗尽电荷和反型电荷：

Qacc=0Qdep={Coxγ22(1−4(Vth−Vfb)γ2−1)如果清除强反型下的高频 C-V 行为模型Coxγ22(1−4(Vth−Vfb)γ2−1)−11Cox+1Cdep(Vgb−Vth)如果选择强反型下的高频 C-V 行为模型}Qinv={−Cox⋅(Vgb−Vth)如果清除强反型下的高频 C-V 行为模型0如果选择强反型下的高频 C-V 行为模型}

其中 *Cox* 是总氧化层电容，*γ* 是体因子，*Cdep* 是耗尽电容。

如果选择 **Model high-frequency C-V behavior at strong inversion** 参数，模块假定少数载流子没有足够的时间对施加电压的变化做出反应。因此，反型电荷 *Qinv* 为零，施加电压降落在氧化层电容和耗尽区电容上。

如果清除 **Model high-frequency C-V behavior at strong inversion** 参数，模块则假定少数载流子有足够的时间快速响应电压变化，并在 MOS 电容器的氧化层下方形成反型层电荷。

### 表格化模型

当您将 **Capacitor model** 参数设置为 `Lookup table (2-D, temperature dependent)` 时，PMOS Capacitor 模块将电容器的总栅极电荷 `QG` 表示为电压和温度的表格。要使用表格化电容查找表将模块参数参数化为温度和电压的函数，请指定 **Gate-bulk capacitance lookup table, Cgb(T,Vgb)**、**Gate-bulk voltage, Vgb** 和 **Temperature, T** 参数。

如果 **Temperature, T** 参数中仅指定一个值，则电容器的 C-V 特性变得与温度无关。

为确保在一个完整 AC 周期内的栅极电荷守恒，模块将 **Gate-bulk capacitance lookup table, Cgb(T,Vgb)** 参数转换为等效电荷查找表。模块使用此等效电荷表，通过线性插值和外推方法计算栅极电荷 *Qg* 相对于电压的变化。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
