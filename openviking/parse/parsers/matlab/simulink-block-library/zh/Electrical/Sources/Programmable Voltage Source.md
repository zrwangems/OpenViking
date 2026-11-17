---
type: simulink-block
title: 'Programmable Voltage Source'
family: 'sources'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'programmablevoltagesource'
documentation_source_path: 'ref/programmablevoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Programmable Voltage Source

## 端口

### 输入

### **DC** — 直流分量物理信号

与电压的直流分量关联的物理信号输入。

### **F** — 频率物理信号

与频率关联的物理信号输入。

### **M** — 幅值物理信号

与幅值关联的物理信号输入。

### **Phi** — 相移物理信号

与相移关联的物理信号输入。
### 守恒

### **+** — 正电压电气

与正电压关联的电气守恒端口。

### **-** — 负电压电气

与负电压关联的电气守恒端口。

## 参数

### 交流幅值

### **AC magnitude configuration** — 交流电压幅值配置 `Constant` (默认) | `Ramp``Step``Modulation``External`

配置电压交流分量的幅值。

#### 依赖关系

选择 `Constant`、`Ramp`、`Step` 或 `Modulation` 将显示相关参数。

选择 `External` 将显示物理信号输入端口。

### **AC voltage peak magnitude** — 交流电压峰值幅值 `100` `V` (默认)

交流电压峰值幅值。

#### 依赖关系

当 **AC magnitude configuration** 参数设置为 `Constant`、`Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### **Rate of change** — 交流电压变化率 `1` **V/s** (默认)

交流电压变化率。

#### 依赖关系

当 **AC magnitude configuration** 参数设置为 `Ramp` 时，将显示此参数。

### **Step amplitude** — 交流电压阶跃幅值 `1` **V** (默认)

交流电压阶跃幅值。

#### 依赖关系

当 **AC magnitude configuration** 参数设置为 `Step` 时，将显示此参数。

### **Modulation magnitude** — 交流电压调制幅值 `1` `V` (默认)

交流电压调制幅值。

#### 依赖关系

当 **AC magnitude configuration** 参数设置为 `Modulation` 时，将显示此参数。

### **Modulation frequency** — 交流电压调制频率 `1` `Hz` (默认)

交流电压调制频率。

#### 依赖关系

当 **AC magnitude configuration** 参数设置为 `Modulation` 时，将显示此参数。

### **Start time** — 交流电压起始时间 `1``s` (默认)

交流电压开始的仿真时间。

#### 依赖关系

当 **AC magnitude configuration** 参数设置为 `Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### **Stop time** — 交流电压停止时间 `2``s` (默认)

交流电压停止的仿真时间。

#### 依赖关系

当 **AC magnitude configuration** 参数设置为 `Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### 频率

### **AC frequency configuration** — 交流频率配置 `Constant` (默认) | `Ramp``Step``Modulation``External`

配置电压交流分量的频率。

#### 依赖关系

选择 `Constant`、`Ramp`、`Step` 或 `Modulation` 将显示相关参数。

选择 `External` 将显示物理信号输入端口。

### **AC voltage frequency** — 交流电压频率 `60` `Hz` (默认)

交流电压频率。

#### 依赖关系

当 **AC frequency configuration** 参数设置为 `Constant`、`Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### **Rate of change** — 交流频率变化率 `1` `Hz/s` (默认)

交流频率变化率。

#### 依赖关系

当 **AC frequency configuration** 参数设置为 `Ramp` 时，将显示此参数。

### **Step amplitude** — 交流频率阶跃幅值 `1` `Hz` (默认)

交流频率阶跃幅值。

#### 依赖关系

当 **AC frequency configuration** 参数设置为 `Step` 时，将显示此参数。

### **Modulation magnitude** — 交流频率调制幅值 `1` `Hz` (默认)

交流频率调制幅值。

#### 依赖关系

当 **AC frequency configuration** 参数设置为 `Modulation` 时，将显示此参数。

### **Modulation frequency** — 交流频率调制频率 `1` `Hz` (默认)

交流频率调制频率。

#### 依赖关系

当 **AC frequency configuration** 参数设置为 `Modulation` 时，将显示此参数。

### **Start time** — 交流频率起始时间 `1``s` (默认)

启动交流频率的仿真时间。

#### 依赖关系

当 **AC frequency configuration** 参数设置为 `Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### **Stop time** — 交流频率起始时间 `2``s` (默认)

停止交流频率的仿真时间。

#### 依赖关系

当 **AC frequency configuration** 参数设置为 `Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### 相位

### **AC phase shift configuration** — 交流相移配置 `Constant` (默认) | `Ramp``Step``Modulation``External`

配置电压交流分量的相位。

#### 依赖关系

选择 `Constant`、`Ramp`、`Step` 或 `Modulation` 将显示相关参数。

选择 `External` 将显示物理信号输入端口。

### **AC voltage phase shift** — 交流电压相移 `0` `deg` (默认)

交流电压相移。

#### 依赖关系

当 **AC phase shift configuration** 参数设置为 `Constant`、`Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### **Rate of change** — 交流相移变化率 `1` `deg/s` (默认)

交流相移变化率。

#### 依赖关系

当 **AC phase shift configuration** 参数设置为 `Ramp` 时，将显示此参数。

### **Step amplitude** — 交流相移阶跃幅值 `1` `deg` (默认)

交流相移阶跃幅值。

#### 依赖关系

当 **AC phase shift configuration** 参数设置为 `Step` 时，将显示此参数。

### **Modulation magnitude** — 交流相移调制幅值 `1` `deg` (默认)

交流相移调制幅值。

#### 依赖关系

当 **AC phase shift configuration** 参数设置为 `Modulation` 时，将显示此参数。

### **Modulation frequency** — 交流相移调制频率 `1` `Hz` (默认)

交流相移调制频率。

#### 依赖关系

当 **AC phase shift configuration** 参数设置为 `Modulation` 时，将显示此参数。

### **Start time** — 交流相移起始时间 `1``s` (默认)

启动交流相移的仿真时间。

#### 依赖关系

当 **AC phase shift configuration** 参数设置为 `Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### **Stop time** — 交流相移起始时间 `2``s` (默认)

停止交流相移的仿真时间。

#### 依赖关系

当 **AC phase shift configuration** 参数设置为 `Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### 直流电压

### **DC voltage configuration** — 直流电压配置 `Constant` (默认) | `Ramp``Step``Modulation``External`

配置电压的直流分量。

#### 依赖关系

选择 `Constant`、`Ramp`、`Step` 或 `Modulation` 将显示相关参数。

选择 `External` 将显示物理信号输入端口。

### **DC voltage** — 直流电压幅值 `0` `V` (默认)

直流电压幅值。

#### 依赖关系

当 **DC magnitude configuration** 参数设置为 `Constant`、`Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### **Rate of change** — 直流电压变化率 `1` **V/s** (默认)

直流电压变化率。

#### 依赖关系

当 **DC magnitude configuration** 参数设置为 `Ramp` 时，将显示此参数。

### **Step amplitude** — 直流电压阶跃幅值 `1` **V** (默认)

直流电压阶跃幅值。

#### 依赖关系

当 **DC magnitude configuration** 参数设置为 `Step` 时，将显示此参数。

### **Modulation magnitude** — 直流电压调制幅值 `1` `V` (默认)

直流电压调制幅值。

#### 依赖关系

当 **DC magnitude configuration** 参数设置为 `Modulation` 时，将显示此参数。

### **Modulation frequency** — 直流电压调制频率 `1` `Hz` (默认)

直流电压调制频率。

#### 依赖关系

当 **DC magnitude configuration** 参数设置为 `Modulation` 时，将显示此参数。

### **Start time** — 直流电压起始时间 `1``s` (默认)

直流电压开始的仿真时间。

#### 依赖关系

当 **DC magnitude configuration** 参数设置为 `Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### **Stop time** — 直流电压停止时间 `2``s` (默认)

直流电压停止的仿真时间。

#### 依赖关系

当 **DC magnitude configuration** 参数设置为 `Ramp`、`Step` 或 `Modulation` 时，将显示此参数。

### 谐波

### **Source harmonics** — 源谐波配置 `None` (默认) | `Generate harmonics`

配置源谐波。

#### 依赖关系

选择 `Generate harmonics` 将显示相关参数。

### **Harmonic orders** — 谐波次数 `[5, 7, 11, 13]` (默认)

谐波次数。

#### 依赖关系

当 **Source harmonics** 参数设置为 `Generate harmonics` 时，将显示此参数。

### **Harmonic to base magnitude ratios** — 谐波与基波幅值比 `[.1, .1, .1, .1]` (默认)

谐波与基波幅值比。指定的元素数量应与 **Harmonic orders** 参数指定的元素数量相同。

#### 依赖关系

当 **Source harmonics** 参数设置为 `Generate harmonics` 时，将显示此参数。

### **Harmonic phase shifts** — 谐波相移 `[0, 0, 0, 0]` `deg` (默认)

谐波相移。指定的元素数量应与 **Harmonic orders** 参数指定的元素数量相同。

#### 依赖关系

当 **Source harmonics** 参数设置为 `Generate harmonics` 时，将显示此参数。

### **Start time** — 源谐波起始时间 `-inf``s` (默认)

源谐波开始的仿真时间。

#### 依赖关系

当 **Source harmonics** 参数设置为 `Generate harmonics` 时，将显示此参数。

### **Stop time** — 源谐波停止时间 `inf``s` (默认)

源谐波停止的仿真时间。

#### 依赖关系

当 **Source harmonics** 参数设置为 `Generate harmonics` 时，将显示此参数。

### 噪声

### **Noise mode** — 包含噪声的选项 `Disabled` (默认) | `Enabled`

噪声配置。

#### 依赖关系

选择 `Enabled` 将显示相关参数。

### **Power spectral density** — 功率谱密度 `0` `V^2/Hz` (默认)

单边频谱噪声功率。电压平方的密度函数，通常视为进入 1 ohm 负载的功率。为避免单位歧义，一些数据手册将噪声电压表示为噪声密度，单位为 V/√Hz。在这种情况下，请输入数据手册中给出的噪声密度的平方作为参数值。

为 **Noise mode** 参数选择 `Enabled` 将显示此参数。

#### 依赖关系

为 **Noise mode** 参数选择 `Enabled` 将显示此参数。

### **Repeatability** — 随机数种子控制 `Not repeatable` (默认) | `Repeatable` | `Specify seed`

随机数种子是用于初始化随机数生成器的数字。种子为 `0` 或正整数。要控制随机数种子，请将此参数设置为：

- `Not repeatable` — 每次仿真模型时种子都会改变。该模块使用 MATLAB® 随机数生成器命令重置随机种子：

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — 每次仿真开始时种子都是相同的随机数。该模块使用 `Not repeatable` 参数所用的同一 MATLAB 随机数生成器命令设置该值。

  当您从 Sources 库向模型中添加 Force Noise Source 模块时，该模块会为重复种子生成并存储一个随机值。当您从模型中的现有模块复制 Force Noise Source 模块时，副本会为重复种子生成一个新的随机值。
- `Specify seed` — 种子是您使用 **Seed** 参数指定的数字。仅当您为 **Repeatability** 参数选择 `Specify seed` 时，**Seed** 参数才可用。

#### 依赖关系

为 **Noise mode** 参数选择 `Enabled` 将显示此参数。

选择 `Repeatable` 或 `Specify seed` 将显示相关参数。

### **Auto-generated seed used for repeatable option** — 自动生成种子 `0` (默认)

种子是自动生成的。

#### 依赖关系

为 **Noise mode** 参数选择 `Enabled` 并且为 **Repeatability** 参数选择 `Repeatable` 将显示此参数。

### **Seed** — 随机数生成种子值 `0` (默认)

种子必须为 `0` 或正整数。仅当您为 **Repeatability** 参数选择 `Specify seed` 时，此参数才可用。

#### 依赖关系

为 **Noise mode** 参数选择 `Enabled` 并且为 **Repeatability** 参数选择 `Specify seed` 将显示此参数。

### **Sample time** — 时间步周期和偏移量 `1e-3` `s` (默认) | `[step, offset]` `s`

时间 *step* 周期和初始时间 *offset* 的值。如果为 *step* 指定标量值，则该模块假定 *offset* 值为 `0`。要为初始时间偏移量指定非零值，请使用向量 `[step, offset]` 指定参数值。*offset* 值必须小于 *step* 值且大于或等于零。

#### 依赖关系

为 **Noise mode** 参数选择 `Enabled` 将显示相关参数。

## 所属库

Simscape / Electrical / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

具有可选可编程幅值、频率、相移和直流偏移的单相交流电压源

Programmable Voltage Source 模块对具有可编程幅值、频率、相移和直流偏移的单相交流电压源进行建模。选择外部模式以通过物理输入信号 **M**、**F**、**Phi** 和 **DC** 指定这些量。电压源中可以包含谐波和噪声。

相关方程，请参阅 Voltage Source 模块。

### 局限性

启用谐波会减慢仿真速度。如果包含谐波，请选择这样的采样时间：仅在感兴趣的频率处生成谐波，而不在更高频率处生成。

启用噪声会减慢仿真速度。如果包含噪声，请选择这样的采样时间：仅在感兴趣的频率处生成噪声，而不在更高频率处生成。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

额定值提供了一种指定模型中变量预期幅值的方法。使用基于额定值的系统缩放可提高仿真鲁棒性。您可以使用不同来源指定额定值，包括模块对话框或属性检查器中的 **额定值** 部分。有关详细信息，请参阅通过额定值进行系统缩放。
