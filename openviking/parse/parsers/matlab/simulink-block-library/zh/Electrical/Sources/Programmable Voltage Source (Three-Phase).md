---
type: simulink-block
title: 'Programmable Voltage Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'programmablevoltagesourcethreephase'
documentation_source_path: 'ref/programmablevoltagesourcethreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Programmable Voltage Source (Three-Phase)

## 端口

### 输入

### **F** — 频率物理信号

与频率关联的物理信号输入。

### **M** — 幅值物理信号

与幅值关联的物理信号输入。

### **Phi** — 相移物理信号

与相移关联的物理信号输入。
### 守恒

### **n** — 中性点电气

与中性点关联的电气守恒端口。

### **~** — 三相交流电压电气

与交流电压关联的可扩展电气守恒三相端口。

## 参数

### **Modeling option** — 是否对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图对应的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### 交流幅值

### **AC magnitude configuration** — 交流电压幅值配置 `Constant`（默认）| `Ramp` | `Step` | `Modulation` | `External`

配置电压交流分量的幅值。

#### 依赖关系

选择 `Constant`、`Ramp`、`Step` 或 `Modulation` 会显示相关参数。

选择 `External` 会显示一个物理信号输入端口。

### **Rated voltage (phase-to-phase RMS)** — 额定交流电压 `100` `V`（默认）

额定交流电压（相间 RMS）。

#### 依赖关系

要启用此参数，请将 **AC magnitude configuration** 设置为 `Constant`、`Ramp`、`Step` 或 `Modulation`。

### **Rate of change** — 交流电压变化率 `1` **V/s**（默认）

交流电压变化率。

#### 依赖关系

要启用此参数，请将 **AC magnitude configuration** 设置为 `Ramp`。

### **Step amplitude** — 交流电压阶跃幅值 `1` **V**（默认）

交流电压阶跃幅值。

#### 依赖关系

要启用此参数，请将 **AC magnitude configuration** 设置为 `Step`。

### **Modulation magnitude** — 交流电压调制幅值 `1` `V`（默认）

交流电压调制幅值。

#### 依赖关系

要启用此参数，请将 **AC magnitude configuration** 设置为 `Modulation`。

### **Modulation frequency** — 交流电压调制频率 `1` `Hz`（默认）

交流电压调制频率。

#### 依赖关系

要启用此参数，请将 **AC magnitude configuration** 设置为 `Modulation`。

### **Start time** — 交流电压起始时间 `1``s`（默认）

交流电压开始的仿真时间。

#### 依赖关系

要启用此参数，请将 **AC magnitude configuration** 设置为 `Ramp`、`Step` 或 `Modulation`。

### **Stop time** — 交流电压停止时间 `2``s`（默认）

交流电压停止的仿真时间。

#### 依赖关系

要启用此参数，请将 **AC magnitude configuration** 设置为 `Ramp`、`Step` 或 `Modulation`。

### 频率

### **AC frequency configuration** — 交流频率配置 `Constant`（默认）| `Ramp` | `Step` | `Modulation` | `External`

配置电压交流分量的频率。

#### 依赖关系

选择 `Constant`、`Ramp`、`Step` 或 `Modulation` 会显示相关参数。

选择 `External` 会显示一个物理信号输入端口。

### **Rated frequency** — 额定频率 `60` `Hz`（默认）

额定频率。

#### 依赖关系

要启用此参数，请将 **AC frequency configuration** 设置为 `Constant`、`Ramp`、`Step` 或 `Modulation`。

### **Rate of change** — 交流频率变化率 `1` `Hz/s`（默认）

交流频率变化率。

#### 依赖关系

要启用此参数，请将 **AC frequency configuration** 设置为 `Ramp`。

### **Step amplitude** — 交流频率阶跃幅值 `1` `Hz`（默认）

交流频率阶跃幅值。

#### 依赖关系

要启用此参数，请将 **AC frequency configuration** 设置为 `Step`。

### **Modulation magnitude** — 交流频率调制幅值 `1` `Hz`（默认）

交流频率调制幅值。

#### 依赖关系

要启用此参数，请将 **AC frequency configuration** 设置为 `Modulation`。

### **Modulation frequency** — 交流频率调制频率 `1` `Hz`（默认）

交流频率调制频率。

#### 依赖关系

要启用此参数，请将 **AC frequency configuration** 设置为 `Modulation`。

### **Start time** — 交流频率起始时间 `1``s`（默认）

交流频率开始的仿真时间。

#### 依赖关系

要启用此参数，请将 **AC frequency configuration** 设置为 `Ramp`、`Step` 或 `Modulation`。

### **Stop time** — 交流频率起始时间 `2``s`（默认）

交流频率停止的仿真时间。

#### 依赖关系

要启用此参数，请将 **AC frequency configuration** 设置为 `Ramp`、`Step` 或 `Modulation`。

### 相位

### **AC phase shift configuration** — 交流相移配置 `Constant`（默认）| `Ramp` | `Step` | `Modulation` | `External`

配置电压交流分量的相位。

#### 依赖关系

选择 `Constant`、`Ramp`、`Step` 或 `Modulation` 会显示相关参数。

选择 `External` 会显示一个物理信号输入端口。

### **Phase shift** — 交流电压相移 `0` `deg`（默认）

交流电压相移。

#### 依赖关系

要启用此参数，请将 **AC phase shift configuration** 设置为 `Constant`、`Ramp`、`Step` 或 `Modulation`。

### **Rate of change** — 交流相移变化率 `1` `deg/s`（默认）

交流相移变化率。

#### 依赖关系

要启用此参数，请将 **AC phase shift configuration** 设置为 `Ramp`。

### **Step amplitude** — 交流相移阶跃幅值 `1` `deg`（默认）

交流相移阶跃幅值。

#### 依赖关系

要启用此参数，请将 **AC phase shift configuration** 设置为 `Step`。

### **Modulation magnitude** — 交流相移调制幅值 `1` `deg`（默认）

交流相移调制幅值。

#### 依赖关系

要启用此参数，请将 **AC phase shift configuration** 设置为 `Modulation`。

### **Modulation frequency** — 交流相移调制频率 `1` `Hz`（默认）

交流相移调制频率。

#### 依赖关系

要启用此参数，请将 **AC phase shift configuration** 设置为 `Modulation`。

### **Start time** — 交流相移起始时间 `1``s`（默认）

交流相移开始的仿真时间。

#### 依赖关系

要启用此参数，请将 **AC phase shift configuration** 设置为 `Ramp`、`Step` 或 `Modulation`。

### **Stop time** — 交流相移起始时间 `2``s`（默认）

交流相移停止的仿真时间。

#### 依赖关系

要启用此参数，请将 **AC phase shift configuration** 设置为 `Ramp`、`Step` 或 `Modulation`。

### 阻抗

### **Source impedance** — 源阻抗配置 `None`（默认）| `X/R Ratio` | `Series R` | `Series L` | `Series RL`

源阻抗配置。

#### 依赖关系

选择 `X/R Ratio`、`Series R`、`Series L` 或 `Series RL` 会显示相关参数。

### **Short-circuit power level** — 短路功率水平 `1e6` `V*A`（默认）

短路功率水平。

#### 依赖关系

要启用此参数，请将 **Source impedance** 设置为 `X/R Ratio`。

### **Source X/R ratio** — X/R 比 `15`（默认）

源 X/R 比。

#### 依赖关系

要启用此参数，请将 **Source impedance** 设置为 `X/R Ratio`。

### **Source resistance** — 电阻 `0.01` `Ohm`（默认）

源电阻。

#### 依赖关系

要启用此参数，请将 **Source impedance** 设置为 `Series R` 或 `Series RL`。

### **Source inductance** — 电感 `3.97e-4` `H`（默认）

源电感。

#### 依赖关系

要启用此参数，请将 **Source impedance** 设置为 `Series L` 或 `Series RL`。

### **Parasitic parallel conductance** — 寄生并联电导 `1e-6` `1/Ohm`（默认）

寄生并联电导。

#### 依赖关系

要启用此参数，请将 **Source impedance** 设置为 `X/R Ratio`、`Series L` 或 `Series RL`。

### 谐波

### **Source harmonics** — 源谐波配置 `None`（默认）| `Generate harmonics`

源谐波的配置。

#### 依赖关系

选择 `Generate harmonics` 会显示相关参数。

### **Harmonic orders** — 谐波次数 `[5, 7, 11, 13]`（默认）

谐波次数。

#### 依赖关系

要启用此参数，请将 **Source harmonics** 设置为 `Generate harmonics`。

### **Harmonic to base magnitude ratios** — 谐波与基波幅值比 `[.1, .1, .1, .1]`（默认）

谐波与基波幅值比。指定的元素数量应与 **Harmonic orders** 参数指定的数量相同。

#### 依赖关系

要启用此参数，请将 **Source harmonics** 设置为 `Generate harmonics`。

### **Harmonic phase shifts** — 谐波相移 `[0, 0, 0, 0]` `deg`（默认）

谐波相移。指定的元素数量应与 **Harmonic orders** 参数指定的数量相同。

#### 依赖关系

要启用此参数，请将 **Source harmonics** 设置为 `Generate harmonics`。

### **Harmonic sequences** — 谐波序 `[1, 1, 1, 1]`（默认）

谐波序：

- `0` 表示零序
- `1` 表示正序
- `2` 表示负序

指定的元素数量应与 **Harmonic orders** 参数指定的数量相同。

#### 依赖关系

要启用此参数，请将 **Source harmonics** 设置为 `Generate harmonics`。

### **Start time** — 源谐波起始时间 `-inf``s`（默认）

源谐波开始的仿真时间。

#### 依赖关系

要启用此参数，请将 **Source harmonics** 设置为 `Generate harmonics`。

### **Stop time** — 源谐波停止时间 `inf``s`（默认）

源谐波停止的仿真时间。

#### 依赖关系

要启用此参数，请将 **Source harmonics** 设置为 `Generate harmonics`。

## 所属库

Simscape / Electrical / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

具有可选可编程交流幅值、频率和相移的三相电压源

Programmable Voltage Source (Three-Phase) 模块对具有可编程交流幅值、频率和相移的三相电压源进行建模。选择外部模式可通过物理输入信号 **M**、**F** 和 **Phi** 指定这些量。您可以向电压源添加谐波和内部阻抗。

有关相关方程，请参阅 Voltage Source (Three-Phase) 模块。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
