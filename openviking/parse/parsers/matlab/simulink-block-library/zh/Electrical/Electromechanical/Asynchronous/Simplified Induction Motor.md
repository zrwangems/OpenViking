---
type: simulink-block
title: 'Simplified Induction Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Asynchronous'
documentation_page: 'simplifiedinductionmotor'
documentation_source_path: 'ref/simplifiedinductionmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Simplified Induction Motor

## 端口
```yaml
ports:
- name: W
  summary: 有功功率物理信号
  direction: output
- name: wm
  summary: 机械转速物理信号
  direction: output
- name: VAR
  summary: 无功功率物理信号
  direction: output
- name: s
  summary: 电机转差率物理信号
  direction: output
- name: R
  summary: 转子机械
  direction: output
- name: C
  summary: 机壳机械
  direction: output
- name: H1
  summary: 转子热
  direction: output
- name: H2
  summary: 转子热
  direction: output
```

### 输出

### **W** — 有功功率物理信号

与电机有功功率相关联的物理信号端口。

### **wm** — 机械转速物理信号

与电机机械转速相关联的物理信号端口。

### **VAR** — 无功功率物理信号

与电机无功功率相关联的物理信号端口。

### **s** — 电机转差率物理信号

与电机转差率相关联的物理信号端口。
### 守恒

### **R** — 转子机械

与转子相关联的机械旋转守恒端口。

### **C** — 机壳机械

与电机机壳相关联的机械旋转守恒端口。

### **H1** — 转子热

定子热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **H2** — 转子热

转子热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Model parameterization
  summary: 模块参数化 By motor ratings（默认）| By equivalent circuit parameters
  group: 电磁转矩
- name: Stator resistance R1
  summary: 定子绕组电阻 1 Ohm（默认）
  group: 电磁转矩
- name: Rotor resistance R2
  summary: 转子电阻 1 Ohm（默认）
  group: 电磁转矩
- name: Stator inductance L1
  summary: 定子绕组电感 0.02 H（默认）
  group: 电磁转矩
- name: Rotor inductance L2
  summary: 转子电感 0.02 H（默认）
  group: 电磁转矩
- name: Magnetizing inductance Lm
  summary: 定子励磁电感 0.5 H（默认）
  group: 电磁转矩
- name: Rated mechanical power
  summary: 电机机械功率 825 W（默认）
  group: 电磁转矩
- name: Rated speed
  summary: 电机额定转速 3500 rpm（默认）
  group: 电磁转矩
- name: Rated RMS line-to-line voltage
  summary: 额定线电压 200 V（默认）
  group: 电磁转矩
- name: Rated supply frequency
  summary: 交流电源电压频率 60 Hz（默认）
  group: 电磁转矩
- name: Rated RMS line current
  summary: 额定线电流 2.7 A（默认）
  group: 电磁转矩
- name: R1 parameterization
  summary: 等效电路电阻参数化 From motor efficiency（默认）| From power factor | Use measured stator resistance R1
  group: 电磁转矩
- name: Motor efficiency (percent)
  summary: 电机效率 95（默认）
  group: 电磁转矩
- name: Motor power factor
  summary: 电机功率因数 0.93（默认）
  group: 电磁转矩
- name: Measured stator resistance R1
  summary: 测量的定子电阻 1 Ohm（默认）
  group: 电磁转矩
- name: Number of pole pairs
  summary: 电机极对数 1（默认）
  group: 电磁转矩
- name: Number of phases
  summary: 电源相数 3（默认）
  group: 电磁转矩
- name: Stator connections
  summary: 电机定子配置 Delta configuration（默认）| Star configuration
  group: 电磁转矩
- name: Supply RMS line-to-line voltage
  summary: 电源 RMS 线电压 200 V（默认）
  group: 电源
- name: Supply frequency
  summary: 交流电源频率 60 Hz（默认）
  group: 电源
- name: Rotor inertia
  summary: 转子惯量 1e-3 kg*m^2（默认）
  group: 机械
- name: Rotor damping
  summary: 转子阻尼 1e-4 N*m/(rad/s)（默认）
  group: 机械
- name: Initial rotor speed
  summary: 初始转子转速 0 rpm（默认）
  group: 机械
- name: Stator and rotor resistance temperature coefficients, [alpha_1 alpha_2]
  summary: 定子和转子电阻温度系数 [.00393, .00393] 1/K（默认）
  group: 温度依赖性
- name: Measurement temperature
  summary: 测量温度 25 C（默认）
  group: 温度依赖性
- name: Stator and rotor thermal masses, [M_1 M_2]
  summary: 定子和转子热质量 [100, 100] J/K（默认）
  group: 热端口
- name: Stator and rotor initial temperatures, [T_1 T_2]
  summary: 定子和转子初始温度 [25, 25] C（默认）
  group: 热端口
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 电磁转矩

### **Model parameterization** — 模块参数化 `By motor ratings`（默认）| `By equivalent circuit parameters`

选择以下模块参数化方法之一：

- `By motor ratings` —
  提供电磁转矩参数，模块在假设励磁电感
  Lm 的影响可忽略的情况下将其转换为电机的等效电路模型。
- `By equivalent circuit
  parameters` — 为电机的等效电路模型提供电气
  参数。

### **Stator resistance R1** — 定子绕组电阻 `1` `Ohm`（默认）

定子绕组的电阻。默认值为
`1` Ω。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Rotor resistance R2** — 转子电阻 `1` `Ohm`（默认）

归算到定子侧的转子电阻。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Stator inductance L1** — 定子绕组电感 `0.02` `H`（默认）

定子绕组的电感。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Rotor inductance L2** — 转子电感 `0.02` `H`（默认）

归算到定子侧的转子电感。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Magnetizing inductance Lm** — 定子励磁电感 `0.5` `H`（默认）

定子的励磁电感。其值难以从电机参数中估算，但影响通常很小。如果不知道其值，请使用 **Stator
inductance L1** 值的 25 倍作为典型值。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Rated mechanical power** — 电机机械功率 `825` `W`（默认）

电机在额定转速下运行时输出的机械功率。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **Rated speed** — 电机额定转速 `3500` `rpm`（默认）

电机输出指定 **Rated
mechanical power** 值时的转速。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **Rated RMS line-to-line voltage** — 额定线电压 `200` `V`（默认）

指定电机额定值时的线电压。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **Rated supply frequency** — 交流电源电压频率 `60` `Hz`（默认）

指定电机额定值时的交流电源电压频率。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **Rated RMS line current** — 额定线电流 `2.7` `A`（默认）

电机输出指定 **Rated
mechanical power** 值时的线电流。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **R1 parameterization** — 等效电路电阻参数化 `From motor efficiency`（默认）| `From power factor` | `Use measured stator resistance R1`

选择以下电机等效电路电阻 R1 的参数化方法之一：

- `From motor efficiency` —
  根据电机效率计算 R1。这是默认方法。
- `From power factor` —
  根据电机功率因数计算 R1。
- `Use measured stator resistance
  R1` — 直接测量
  R1。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **Motor efficiency (percent)** — 电机效率 `95`（默认）

电机在 **Rated speed**
值下运行时，输入功率中传递给机械负载的百分比。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 且将 **R1
parameterization** 参数设置为 `From motor
efficiency` 时，此参数才可见。

### **Motor power factor** — 电机功率因数 `0.93`（默认）

电机在 **Rated mechanical power**
值下运行时，电源电流滞后电源电压的角度的余弦值。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 且将 **R1
parameterization** 参数设置为 `From power
factor` 时，此参数才可见。

### **Measured stator resistance R1** — 测量的定子电阻 `1` `Ohm`（默认）

测量的定子电阻。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 且将 **R1
parameterization** 参数设置为 `Use
measured stator resistance R1` 时，此参数才可见。

### **Number of pole pairs** — 电机极对数 `1`（默认）

电机的总极对数。

### **Number of phases** — 电源相数 `3`（默认）

电源相数。

### **Stator connections** — 电机定子配置 `Delta configuration`（默认）| `Star configuration`

选择以下电机配置之一：

- `Delta configuration` —
  将电机定子绕组连接为三角形配置。
- `Star configuration` —
  将电机定子绕组连接为星形配置。

### 电源

### **Supply RMS line-to-line voltage** — 电源 RMS 线电压 `200` `V`（默认）

为电机供电的线电压。

### **Supply frequency** — 交流电源频率 `60` `Hz`（默认）

交流电源电压的频率。

### 机械

### **Rotor inertia** — 转子惯量 `1e-3` `kg*m^2`（默认）

转子惯量。该值可以为零。

### **Rotor damping** — 转子阻尼 `1e-4` `N*m/(rad/s)`（默认）

转子阻尼。该值可以为零。

### **Initial rotor speed** — 初始转子转速 `0` `rpm`（默认）

仿真开始时转子的转速。

### 温度依赖性

此选项卡仅对具有暴露热端口的模块显示。

### **Stator and rotor resistance temperature coefficients, [alpha\_1 alpha\_2]** — 定子和转子电阻温度系数 `[.00393, .00393]` `1/K`（默认）

一个 1×2 行向量，定义电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。第一个元素对应定子，第二个对应转子。默认值为铜的值。

### **Measurement temperature** — 测量温度 `25` `C`（默认）

定义电机参数时的温度。

### 热端口

此选项卡仅对具有暴露热端口的模块显示。

### **Stator and rotor thermal masses, [M\_1 M\_2]** — 定子和转子热质量 `[100, 100]` `J/K`（默认）

一个 1×2 行向量，定义定子和转子绕组的热质量。热质量是使温度升高一度所需的能量。

### **Stator and rotor initial temperatures, [T\_1 T\_2]** — 定子和转子初始温度 `[25, 25]` `C`（默认）

一个 1×2 行向量，定义仿真开始时定子和转子热端口的温度。
## 所属库

Simscape / Electrical / Electromechanical / Asynchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

由理想交流电源供电的感应电机

Simplified Induction Motor 模块表示由理想交流电源供电的感应电机的电气和转矩特性。下图显示了 Simplified Induction Motor 模块的等效电路模型。

图中：

- *R1* 是定子
  电阻。
- *R2* 是归算到定子侧的转子电阻。
- *L1* 是定子
  电感。
- *L2* 是归算到定子侧的转子电感。
- *Lm* 是励磁
  电感。
- s 是转子转差率。
- V¯ 和 I¯ 是正弦电源电压和电流
  相量。

转子转差率 s 由机械转速 ωm、极对数 p 和电源频率 ω 定义为

s=1−pωmω

这意味着启动时转差率为一，而与电源频率同步运行时为零。

对于 *n* 相感应电机，转矩-转速关系由下式给出：

T=npR2sωVrms2(R1+R2+1−ssR2)2+(X1+X2)2

其中：

- *Vrms* 是星形配置感应电机的相电压，三角形配置感应电机的线电压。
- *n* 是相数。

您可以按照上述等效电路模型参数来参数化此模块，也可以按照模块用于推导这些参数的电机额定值来参数化此模块。

此模块产生从机械 C 端口到 R 端口的正向转矩。

### 热效应建模

您可以暴露热端口来对将功率转换为热量的损耗效应进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含
  热端口。
- `Show thermal port` — 模块包含多个
  热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。
