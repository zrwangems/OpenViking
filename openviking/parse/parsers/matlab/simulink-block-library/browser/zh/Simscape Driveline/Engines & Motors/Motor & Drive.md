---
type: simulink-block
title: 'Motor & Drive'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors'
documentation_page: 'motordrive'
documentation_source_path: 'ref/motordrive.html'
language: zh-CN
chinese_source: worker-translation
---

# Motor & Drive

## 端口

### 输入

### **Tr** — 参考转矩需求，N\*m physical signal

与参考转矩需求关联的 physical signal 输入端口。
### 输出

### **W** — 机械转速，rad/s physical signal

与机械转速关联的 physical signal 输出端口。
### 守恒

### **+** — 正极直流电源 electrical

与正极直流电源关联的 electrical 守恒端口。

### **-** — 负极直流电源 electrical

与负极直流电源关联的 electrical 守恒端口。

### **C** — 电机壳体 mechanical rotational

与电机壳体关联的 mechanical rotational 守恒端口。

### **R** — 电机转子 mechanical rotational

与电机转子关联的 mechanical rotational 守恒端口。

### **H** — 热流 thermal

与热流关联的 thermal 守恒端口。电机的电气损耗会通过该端口对热流产生贡献。

#### 依赖关系

要启用该端口，请将 **Thermal port** 设置为 `Model`。

## 参数

### **Maximum torque** — 用于定义转矩-转速包络边界的转矩 `400` `N*m`（默认）| positive scalar

最大允许转矩值。该模块使用此值和 **Maximum power** 参数来定义转矩-转速包络。

### **Maximum power** — 用于定义转矩-转速包络边界的功率 `200` `kW`（默认）| positive scalar

最大允许功率值。该模块使用此值和 **Maximum torque** 参数来定义转矩-转速包络。

### **Torque control time constant, Tc** — 输出转矩时间步长 `0.02` `s`（默认）| positive scalar

转矩控制器输出时间间隔。使用此参数告诉模块在发出转矩值输出信息之间等待多长时间。

### **Motor and driver overall efficiency (percent)** — 给定转速和转矩下的能量效率 `100`（默认）| scalar in the range (0,100]

将电能转换为机械旋转能的效率。

### **Speed at which efficiency is measured** — 用于效率测量的给定转速 `3750` `rpm`（默认）| positive scalar

模块用于计算转矩相关电气损耗的转速。

### **Torque at which efficiency is measured** — 用于效率测量的给定转矩 `100` `N*m`（默认）| positive scalar

模块用于计算转矩相关电气损耗的转矩。

### **Thermal port** — 模拟电气布线质量中的热损耗 `Omit`（默认）| `Model`

用于启用热端口并在仿真中包含热损耗的选项。

### **Thermal mass** — 布线保持热量的倾向 `100` `J/K`（默认）| positive scalar

电气绕组的热质量，定义为使温度升高一个温度单位所需的能量。

#### 依赖关系

要启用该参数，请将 **Thermal port** 设置为 `Model`。

## 所属库

Simscape / Driveline / Engines & Motors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021a 中引入**

## 描述

具有闭环转矩控制的通用电机和驱动

Motor & Drive 模块表示具有闭环转矩控制的通用无刷电机和驱动。它是 Motor & Drive (System Level) (Simscape Electrical) 模块的简化版本。当您的系统中需要通用或低保真度电机实现时，Motor & Drive 模块非常有用。它也适用于您不知道所有电机规格，或者希望使用该模块为系统寻找合适电机的情况。

为了实现更快的仿真，该模块对电机、驱动电子设备和控制器进行了抽象。该模块生成一个转矩-转速包络，该包络会饱和输入转矩，并且仅允许包络所定义的转矩和转速范围。

### 电气损耗建模

Motor & Drive 模块基于给定转速和转矩下的总体效率对一阶损耗进行建模，您分别通过 **Motor and driver overall efficiency (percent)**、**Speed at which efficiency is measured** 和 **Torque at which efficiency is measured** 指定这些值。该模块使用转速和转矩生成转矩-转速包络。该包络会饱和输入转矩，从而得到电机响应的转矩 *τelec*。这也是模块用于计算电气损耗的转矩。

该模块仅考虑与转矩相关的电阻损耗，即

Plosses=kτelec2,

其中

k=ωη(1−η/100)τη⋅η/100.

电阻损耗也称为欧姆损耗，其产生原因是电枢绕组阻碍电子流动的趋势。电功率包含这些损耗，即

Pelec=Plosses+ωτelec.

从电能到热能的转换速率由焦耳定律定义：

I=PelecV,

其中：

- *Pelec* 是模块计算并在控制方程中使用的电功率。
- *Plosses* 是运行期间损失的电功率。当您对热流和温度变化的影响进行建模时，该值表示分配到热质量中或通过端口 **H** 流出的热流速率。
- *ω* 是转子的角速度。它等效于 **W** 输出端口的值。
- *τelec* 是饱和后的转矩需求。
- *k* 是电阻损耗的比例常数，其单位为 *(energy\*time)-1*。
- *η* 是电机和驱动器在给定转速和转矩下的效率。该值等效于 **Motor and driver overall efficiency (percent)** 参数。
- *ωη* 是对应于总体效率的角速度。该值等效于 **Speed at which efficiency is measured** 参数。
- *τη* 是对应于总体效率的转矩。该值等效于 **Torque at which efficiency is measured** 参数。
- *V* 是端子间的电压。
- *I* 是流过端子的电流。

当您启用热建模时，*Plosses* 表示模块对热流的贡献。

若要包含串联电阻、固定损耗和铁损耗，您可以向模型中添加模块，或使用 Motor & Drive (System Level) (Simscape Electrical) 模块。

**提示**

您可以分别使用 Rotational Damper 模块和 Inertia 模块添加阻尼和惯性。

### 热建模

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Thermal port** 设置为 `Model`。

当您对热流和温度变化的影响进行建模时，电机的电气损耗会对这些影响产生贡献。

### 变量

在仿真前，使用 **Variables** 选项卡设置模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

**依赖关系**

要启用此设置，请将 **Thermal port** 设置为 `Model`。

### 假设与限制

- 电机驱动器以时间常数 *Tc* 跟踪转矩需求。
- 由机械负载引起的电机转速波动不影响电机转矩跟踪。
