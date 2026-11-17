---
type: simulink-block
title: 'Rolling Resistance'
family: 'tires-vehicles'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles / Tire Subcomponents'
documentation_page: 'rollingresistance'
documentation_source_path: 'ref/rollingresistance.html'
language: zh-CN
chinese_source: worker-translation
---

# Rolling Resistance

## 端口

### 输入

### **N** — 法向力，N 物理信号

与法向力关联的物理信号输入端口，单位为 N。正力方向向下。

### **T** — 胎面摩擦力，N 物理信号

与来自路面对轮胎的摩擦力关联的物理信号输入端口，单位为 N。正力方向向前。

#### 依赖关系

要启用此端口，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### 守恒

### **H** — 轮毂，m/s 机械平移

与轮毂关联的机械平移守恒端口，单位为 m/s。

## 参数

### **Resistance model** — 滚动阻力计算建模方法 `Constant coefficient`（默认）| `Pressure and velocity dependent (SAE J2542)` | `Pressure and velocity dependent (Magic Formula)`

计算轮毂上滚动阻力的方法。该参数有三个选项：

- `Constant coefficient`
- `Pressure and velocity dependent (SAE J2542)`
- `Pressure and velocity dependent (Magic Formula)`

### **Constant coefficient** — 滚动轮胎的阻力系数 `0.015`（默认）| 正标量

用于计算滚动阻力的恒定系数值。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Constant coefficient`。

### **Tire pressure** — 滚动轮胎的充气压力 `250e3` `Pa`（默认）| 正标量

滚动轮胎的恒定充气压力。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (SAE J2542)` 或 `Pressure and velocity dependent (Magic Formula)`。

### **Alpha** — 近似系数 α `-0.003`（默认）| 标量

用于压力和速度参数化的 SAE J2452 系数。您根据 SAE J2452 使用经验数据确定此值。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (SAE J2542)`。

### **Beta** — 近似系数 β `0.97`（默认）| 标量

用于压力和速度参数化的 SAE J2452 系数。您根据 SAE J2452 使用经验数据确定此值。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (SAE J2542)`。

### **Coefficient A** — 近似系数 A `84e-4`（默认）| 正标量

用于压力和速度参数化的 SAE J2452 系数。您根据 SAE J2452 使用经验数据确定此值。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (SAE J2542)`。

### **Coefficient B** — 近似系数 B `6.2e-4` `s/m`（默认）| 非负标量

用于压力和速度参数化的 SAE J2452 系数。您根据 SAE J2452 使用经验数据确定此值。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (SAE J2542)`。

### **Coefficient C** — 近似系数 C `1.6e-4` `s^2/m^2`（默认）| 非负标量

用于压力和速度参数化的 SAE J2452 系数。您根据 SAE J2452 使用经验数据确定此值。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (SAE J2542)`。

### **Tire nominal pressure, NOMPRES** — 标称轮胎压力 `240e3` `Pa`（默认）| 正标量

标称轮胎压力。`NOMPRES` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Tire nominal vertical load, FNOMIN** — 法向力 `4000` `N`（默认）| 正标量

轮胎上的标称法向力 *Fz0*。`FNOMIN` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Nominal hub longitudinal speed, LONGVL** — 标称轮毂纵向速度 `16` `m/s`（默认）| 正标量

标称轮毂纵向速度。`LONGVL` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Q-coefficient parameters [qsy1 qsy2 qsy3 qsy4 qsy5 qsy6 qsy7 qsy8]** — Magic Formula Q 系数 `[.0082, 0, .0014, .001, 0, 0, 1.08, -.5]` `1`（默认）| 长度为 8 的向量

Magic Formula Q 系数。`qsy1`,…, `qsy8` 对应 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Scale factor of rolling resistance, LMY** — 滚动阻力 `1`（默认）| 正标量

滚动阻力的比例因子，*λMY*。`LMY` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Velocity threshold** — 完整滚动阻力传递到滚动轮毂时的速度 `0.001` `m/s`（默认）| 正标量

达到最大滚动阻力量的最小速度。

## 所属库

Simscape / Driveline / Tires & Vehicles / Tire Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2023a: Magic Formula 兼容性增强

该模块现在与 Magic Formula 兼容。您可以将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)` 以启用 Magic Formula 阻力参数。

## 描述

对滚动阻力建模

Rolling Resistance 模块表示由于道路-车轮接触面处的滚动阻力而作用在轮毂上的阻力。该模块可使用恒定阻力系数、SAE J2452 标准的压力和速度相关性，或 Magic Formula。当作用在车轮-道路接触面的法向力小于或等于零时，阻力为零。

### 恒定阻力系数参数化

当您将 **Resistance model** 设置为 `Constant coefficient` 时，滚动阻力与阻力系数成正比 *F* = *Nμ*，其中：

- *F* 是滚动阻力。
- *N* 是法向力。
- *μ* 是滚动阻力系数。

滚动阻力系数具有双曲形式，可消除 *vhub* = 0 处的不连续性

μ=μ0⋅tanh(4⋅vhubvthreshold),

其中：

- *μ0* 是渐近滚动阻力系数。
- *vhub* 是轮毂速度。
- *vthreshold* 是阈值速度。

### 压力和速度相关参数化

当您将 **Resistance model** 设置为 `Pressure and velocity dependent (SAE J2542)` 时，该模块使用以下公式：

F=(PP0)α(NN0)βN0⋅(A+B|vhub|+Cvhub2)tanh(4vhubvthreshold),

其中：

- *P* 是轮胎压力。
- *vhub* 是轮毂速度。
- *α, β, A, B, and C* 是近似系数。
- *P0* 是 1 Pascal (Pa)。
- *N0* 是 1 Newton (N)。

在此方程中，参数 *P0* 和 *N0* 从每个指数表达式的底数中移除物理单位。

当您将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)` 时，该模块使用 Magic Formula 计算滚动阻力，如下式：

F=FZ0λMy(qsy1+qsy2FX,TreadFZ0+qsy3|VHV0|+qsy4(VHV0)4)(FZFZ0)qsy7(pipi0)qsy8tanh(4vhubvthreshold),

其中：

- *FZ0* 是 **Tire nominal vertical load, FNOMIN** 参数。
- *λMy* 是 **Scale factor of rolling resistance, LMY** 参数。
- *qsy1,...,qsy8* 是 **Q-coefficient parameters [qsy1 qsy2 qsy3 qsy4 qsy5 qsy6 qsy7 qsy8]** 参数的元素。
- *V0* 是 **Hub nominal longitudinal speed, LONGVL** 参数。
- *pi* 是 **Tire pressure** 参数。
- *pi0* 是 **Tire nominal pressure, NOMPRES** 参数。
- *VH* 是轮毂纵向速度。
- *FX,Tread* 是路面对轮胎胎面施加的纵向摩擦力。
- *FZ* 是轮胎上的垂直载荷。

此参数化中的 `tanh` 表达式在 *vhub = 0* 时平滑地改变阻力的符号。
