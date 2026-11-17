---
type: simulink-block
title: 'Motor & Drive'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
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

### **Tr** — 参考转矩需求，N\*m 物理信号

与参考转矩需求关联的物理信号输入端口。
### 输出

### **W** — 机械转速，rad/s 物理信号

与机械转速关联的物理信号输出端口。
### 守恒

### **+** — 正直流电源电气

与正直流电源关联的电气守恒端口。

### **-** — 负直流电源电气

与负直流电源关联的电气守恒端口。

### **C** — 电机壳体机械旋转

与电机壳体关联的机械旋转守恒端口。

### **R** — 电机转子机械旋转

与电机转子关联的机械旋转守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。电机的电气损耗通过此端口贡献热流。

#### 依赖关系

要启用此端口，请将 **Thermal port** 设置为
`Model`。

## 参数

### **Maximum torque** — 用于定义转矩-转速包络边界的转矩 `400` `N*m`（默认）| 正标量

最大允许转矩值。该模块使用此值和
**Maximum power** 参数来定义转矩-转速
包络。

### **Maximum power** — 用于定义转矩-转速包络边界的功率 `200` `kW`（默认）| 正标量

最大允许功率值。该模块使用此值和
**Maximum torque** 参数来定义转矩-转速
包络。

### **Torque control time constant, Tc** — 输出转矩时间步长 `0.02` `s`（默认）| 正标量

转矩控制器输出时间间隔。使用此参数告知模块在发出转矩值输出信息之间等待多长时间。

### **Motor and driver overall efficiency (percent)** — 给定转速和转矩下的能效 `100`（默认）| 范围 (0,100] 内的标量

将电能转换为机械旋转能的效率。

### **Speed at which efficiency is measured** — 用于效率测量的给定转速 `3750` `rpm`（默认）| 正标量

模块用于计算转矩相关电气损耗的转速。

### **Torque at which efficiency is measured** — 用于效率测量的给定转矩 `100` `N*m`（默认）| 正标量

模块用于计算转矩相关电气损耗的转矩。

### **Thermal port** — 在电气布线质量中模拟热损耗 `Omit`（默认）| `Model`

启用热端口并在仿真中包含热损耗的选项。

### **Thermal mass** — 布线保持热量的倾向 `100` `J/K`（默认）| 正标量

电气绕组的熱质量，定义为使温度升高一个温度单位所需的能量。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为
`Model`。

## 所属库

Simscape / Driveline / Engines & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

具有闭环转矩控制的通用电机和驱动器

Motor & Drive 模块表示具有闭环转矩控制的通用无刷
电机和驱动器。它是
Motor & Drive (System
Level) (Simscape Electrical) 模块的简化版本。当您需要在系统中使用通用或低保真度电机实现时，Motor & Drive
模块非常有用。它也适用于您不了解所有电机
规格或希望使用该模块为系统找到合适电机的情况。

为了实现更快的仿真，该模块对电机、驱动电子设备和控制器进行了抽象。
该模块生成一个转矩-转速包络，使输入转矩饱和，并且
仅允许该包络定义的转矩和转速范围。

### 电气损耗建模

Motor & Drive 模块基于给定转速和转矩下的整体效率对一阶损耗进行建模，您需要分别指定
**Motor and driver overall efficiency (percent)**、
**Speed at which efficiency is measured** 和 **Torque
at which efficiency is measured**。该模块使用
转速和转矩生成转矩-转速包络。该包络使
输入转矩饱和，从而得到电机响应的转矩，
*τelec*。这也是模块用于计算电气损耗的转矩。

该模块仅考虑转矩相关电阻损耗，使得

Plosses=kτelec2,

其中

k=ωη(1−η/100)τη⋅η/100.

电阻损耗也称为欧姆损耗，是由于
电枢绕组抵抗电子流动的倾向而产生的。电功率
包含这些损耗，使得

Pelec=Plosses+ωτelec.

电能到热能的转换速率
由焦耳定律定义：

I=PelecV,

其中：

- *Pelec* 是模块计算并在控制
  方程中使用的电功率。
- *Plosses* 是运行期间损失的电
  功率。当您对热流和
  温度变化的影响进行建模时，此值表示分配到
  热质量中或流出端口
  **H** 的热流速率。
- *ω* 是转子的角速度。这
  等效于 **W** 输出端口值。
- *τelec* 是饱和
  转矩需求。
- *k* 是电阻
  损耗的比例常数，其单位为
  *(energy\*time)-1*。
- *η* 是给定转速和转矩下电机和驱动器的效率。此值等效于 **Motor
  and driver overall efficiency (percent)** 参数。
- *ωη* 是对应于整体效率的角速度。此值等效于
  **Speed at which efficiency is measured**
  参数。
- *τη* 是对应于整体效率的转矩。此值等效于
  **Torque at which efficiency is measured**
  参数。
- *V* 是端子间的电压。
- *I* 是通过端子的电流。

当您启用热建模时，
*Plosses* 表示模块对热流的
贡献。

要包含串联电阻、固定损耗和铁损耗，您可以向模型添加模块，或使用 Motor & Drive (System
Level) (Simscape Electrical) 模块。

**提示**

您可以分别使用 Rotational Damper
模块和 Inertia 模块添加阻尼和惯量。

### 热建模

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Thermal port** 设置为
`Model`。

当您对热流和温度变化的影响进行建模时，电机的电气
损耗会对这些影响产生贡献。

### 变量

使用 **Variables** 选项卡在仿真前设置模块变量的优先级和初始
目标值。有关更多信息，
请参阅 Set Priority and Initial Target for Block Variables。

**依赖关系**

要启用此设置，请将 **Thermal port** 设置为
`Model`。

### 假设和限制

- 电机驱动器以时间常数
  *Tc* 跟踪转矩需求。
- 由机械负载引起的电机转速波动不会影响电机
  转矩跟踪。
