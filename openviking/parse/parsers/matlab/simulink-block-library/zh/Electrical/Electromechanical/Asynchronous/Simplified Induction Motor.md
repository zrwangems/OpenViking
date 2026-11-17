---
type: simulink-block
title: 'Simplified Induction Motor'
family: 'electromechanical'
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

### 输出

### **W** — 有功功率物理信号

与电机有功功率关联的物理信号端口。

### **wm** — 机械转速物理信号

与电机机械转速关联的物理信号端口。

### **VAR** — 无功功率物理信号

与电机无功功率关联的物理信号端口。

### **s** — 电机转差物理信号

与电机转差关联的物理信号端口。
### 守恒

### **R** — 转子机械

与转子关联的机械旋转守恒端口。

### **C** — 机壳机械

与电机机壳关联的机械旋转守恒端口。

### **H1** — 转子热

定子热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **H2** — 转子热

转子热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port` (默认) | `Show thermal port`

是否启用模块的热端口，并建模将功率转换为热量的损耗效应。

### 电气转矩

### **Model parameterization** — 模块参数化 `By motor ratings` (默认) | `By equivalent circuit parameters`

选择以下模块参数化方法之一：

- `By motor ratings` —
  提供电气转矩参数，模块将其转换为电机的等效电路模型，假设励磁电感
  Lm 的影响可忽略。
- `By equivalent circuit
  parameters` — 提供电机等效电路模型的电气参数。

### **Stator resistance R1** — 定子绕组电阻 `1` `Ohm` (默认)

定子绕组的电阻。默认值为
`1` Ω。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Rotor resistance R2** — 转子电阻 `1` `Ohm` (默认)

转子电阻，相对于定子指定。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Stator inductance L1** — 定子绕组电感 `0.02` `H` (默认)

定子绕组的电感。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Rotor inductance L2** — 转子电感 `0.02` `H` (默认)

转子电感，相对于定子指定。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Magnetizing inductance Lm** — 定子励磁电感 `0.5` `H` (默认)

定子的励磁电感。其值很难根据电机参数估计，但影响通常很小。如果不知道其值，请使用 **Stator
inductance L1** 值的 25 倍作为典型值。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Rated mechanical power** — 电机机械功率 `825` `W` (默认)

电机在额定转速下运行时输出的机械功率。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **Rated speed** — 电机额定转速 `3500` `rpm` (默认)

电机输出指定 **Rated
mechanical power** 值时的转速。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **Rated RMS line-to-line voltage** — 额定线电压 `200` `V` (默认)

指定电机额定值时的线电压。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **Rated supply frequency** — 交流供电电压的频率 `60` `Hz` (默认)

指定电机额定值时的交流供电电压频率。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **Rated RMS line current** — 额定线电流 `2.7` `A` (默认)

电机输出指定 **Rated
mechanical power** 值时的线电流。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings` 时，此参数才可见。

### **R1 parameterization** — 等效电路电阻参数化 `From motor efficiency` (默认) | `From power factor` | `Use measured stator resistance R1`

为电机的等效电路电阻 R1 选择以下参数化方法之一：

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

### **Motor efficiency (percent)** — 电机效率 `95` (默认)

在 **Rated speed**
值下运行时，电机输入功率中传递到机械负载的百分比。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings`，且将 **R1
parameterization** 参数设置为 `From motor
efficiency` 时，此参数才可见。

### **Motor power factor** — 电机功率因数 `0.93` (默认)

在 **Rated mechanical power**
值下运行时，供电电流滞后供电电压角度的余弦。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings`，且将 **R1
parameterization** 参数设置为 `From power
factor` 时，此参数才可见。

### **Measured stator resistance R1** — 实测定子电阻 `1` `Ohm` (默认)

实测的定子电阻。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By motor
ratings`，且将 **R1
parameterization** 参数设置为 `Use
measured stator resistance R1` 时，此参数才可见。

### **Number of pole pairs** — 电机极对数 `1` (默认)

电机的总极对数。

### **Number of phases** — 供电相数 `3` (默认)

供电相数。

### **Stator connections** — 电机定子配置 `Delta configuration` (默认) | `Star configuration`

选择以下电机配置之一：

- `Delta configuration` —
  将电机定子绕组连接为三角形配置。
- `Star configuration` —
  将电机定子绕组连接为星形配置。

### 电源

### **Supply RMS line-to-line voltage** — 电源 RMS 线电压 `200` `V` (默认)

为电机供电的线电压。

### **Supply frequency** — 交流供电频率 `60` `Hz` (默认)

交流供电电压的频率。

### 机械

### **Rotor inertia** — 转子惯量 `1e-3` `kg*m^2` (默认)

转子惯量。该值可以为零。

### **Rotor damping** — 转子阻尼 `1e-4` `N*m/(rad/s)` (默认)

转子阻尼。该值可以为零。

### **Initial rotor speed** — 初始转子转速 `0` `rpm` (默认)

仿真开始时转子的转速。

### 温度依赖性

此选项卡仅对暴露热端口的模块显示。

### **Stator and rotor resistance temperature coefficients, [alpha\_1 alpha\_2]** — 定子和转子电阻温度系数 `[.00393, .00393]` `1/K` (默认)

一个 1×2 行向量，用于定义将电阻与温度关联的方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。第一个元素对应定子，第二个对应转子。默认值适用于铜。

### **Measurement temperature** — 测量温度 `25` `C` (默认)

定义电机参数时所对应的温度。

### 热端口

此选项卡仅对暴露热端口的模块显示。

### **Stator and rotor thermal masses, [M\_1 M\_2]** — 定子和转子热质量 `[100, 100]` `J/K` (默认)

一个 1×2 行向量，用于定义定子和转子绕组的热质量。热质量是将温度升高一度所需的能量。

### **Stator and rotor initial temperatures, [T\_1 T\_2]** — 定子和转子初始温度 `[25, 25]` `C` (默认)

一个 1×2 行向量，用于定义仿真开始时定子和转子热端口的温度。

## 所属库

Simscape / Electrical / Electromechanical / Asynchronous

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

由理想交流电源供电的感应电机

Simplified Induction Motor 模块表示由理想交流电源供电的感应电机的电气和转矩特性。下图显示了 Simplified Induction Motor 模块的等效电路模型。

图中：

- *R1* 是定子电阻。
- *R2* 是相对于定子的转子电阻。
- *L1* 是定子电感。
- *L2* 是相对于定子的转子电感。
- *Lm* 是励磁电感。
- s 是转子转差。
- V¯ 和 I¯ 是正弦供电电压和电流相量。

转子转差 s 由机械转速 ωm、极对数 p 和电源频率 ω 定义为

s=1−pωmω

这意味着启动时转差为 1，与电源频率同步运行时转差为 0。

对于 *n* 相感应电机，转矩-转速关系由下式给出：

T=npR2sωVrms2(R1+R2+1−ssR2)2+(X1+X2)2

其中：

- *Vrms* 是星形配置感应电机的线-中性点供电电压，以及三角形配置感应电机的线电压。
- *n* 是相数。

您可以按前述等效电路模型参数对该模块进行参数化，或按模块用于推导这些参数的电机额定值进行参数化。

该模块产生从机械 C 端口作用到 R 端口的正转矩。

### 热效应建模

可以暴露热端口，以建模将功率转换为热量的损耗效应。要暴露热端口，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。
