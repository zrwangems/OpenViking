---
type: simulink-block
title: 'Piezo Rotary Actuator'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Mechatronic Actuators\u200b'
documentation_page: 'piezorotaryactuator'
documentation_source_path: 'ref/piezorotaryactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Piezo Rotary Actuator

## 端口

### 输入

### **f** — 电机驱动频率物理信号

与电机驱动频率相关联的物理信号输入端口，单位为 Hz。

### **v** — RMS 电源电压和旋转方向物理信号

指定 RMS 电源电压的物理信号输入幅值端口，符号指定旋转方向。如果 `v` 为正，则正转矩从端口 **C** 作用到端口 **R**。

### 输出

### **i** — RMS 相电流物理信号

与 RMS 相电流相关联的物理信号输出端口。

### **wm** — 转子速度物理信号

与转子转速相关联的物理信号输出端口。

### 守恒

### **C** — 外壳机械

与电机外壳相关联的机械平移守恒端口。

### **R** — 转子机械

与电机转子相关联的机械平移守恒端口。

## 参数

### 电气转矩

### **Motor natural frequency** — 电机固有频率 `40` `kHz`（默认）

压电晶体自然谐振的频率。对于大多数应用，将端口 **f** 处的输入信号设置为该频率。要使电机减速，例如在闭环速度控制中，使用略低于电机固有频率的频率。默认值为 `40``kHz`。

### **Rated RMS voltage** — 额定 RMS 电压 `130` `V`（默认）

电机设计运行时所用的电压。

### **Rated torque** — 额定转矩 `0.5` `N*m`（默认）

电机在额定 RMS 电压下输出的转矩。

### **Rated rotational speed** — 额定转速 `100` `rpm`（默认）

电机在额定转矩下驱动负载时的电机速度。

### **No-load maximum rotational speed** — 空载最大转速 `160` `rpm`（默认）

在额定电压和驱动频率下供电并驱动空载时的电机转速。

### **Maximum torque** — 最大转矩 `1` `N*m`（默认）

电机在额定电压和频率下供电并主动驱动负载时输出的最大转矩。默认值为 `1``N*m`。

**注意**

**Holding torque** 参数值（电机静止时保持的负载转矩）可能大于 **Maximum torque** 参数值。

### **Resonance quality factor** — 谐振品质因数 `100`（默认）

品质因数 *Q*，指定转矩如何随驱动频率变化。增大品质因数会导致当驱动频率偏离固有频率时转矩下降得快得多。

### **Capacitance per phase** — 每相电容 `5` `nF`（默认）

与两个电机相中每一相相关联的电气电容。

### 机械

### **Rotor inertia** — 转子惯量 `200` `g*cm^2`（默认）

转子对电机运动变化的阻力。

### 电机断电摩擦

### **Holding torque** — 保持转矩 `1.5` `N*m`（默认）

库仑摩擦和静摩擦之和。它必须大于或等于 **Coulomb friction torque** 参数值。

### **Coulomb friction torque** — 库仑摩擦转矩 `1.0` `N*m`（默认）

在任何速度下以恒定转矩阻碍旋转的摩擦。

### **Viscous friction coefficient** — 粘性摩擦系数 `0.001` `N*m/(rad*s)`（默认）| 非负标量

摩擦转矩与相对角速度之间的比例系数。

### **Transition approximation coefficient** — 过渡近似系数 `10` `s/rad`（默认）

该参数设置用于近似静摩擦与库仑摩擦之间过渡的系数值。有关系数 *cv* 的详细信息，请参阅 Simscape Rotational Friction 模块参考页。

### **Linear region velocity threshold** — 线性区域速度阈值 `1e-4` `rad/s`（默认）

该参数设置零速度附近的小邻域，在该邻域内摩擦转矩被视为与相对速度成线性比例。MathWorks® 建议使用 `1e-5` 到 `1e-3``rad/s` 范围内的值。

## 所属库

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

旋转压电行波电机的转矩-速度特性

Piezo Rotary Actuator 模块表示压电行波电机的转矩-速度特性。该模块在适合系统级建模的层级上表示电机的转矩-速度关系。为仿真该电机，模块使用以下模型：

- 未通电电机的惯量与摩擦模型
- 通电电机的谐振电路模型

### 未通电电机的惯量与摩擦模型

当物理信号输入 *v* 为零时，电机未通电。这对应于向电机施加零 RMS 电压。在此情形下，模块使用以下元素对电机建模：

- 一个惯量，其值为 **Rotor inertia** 参数值。
- 一个摩擦，其特性由 **Motor-Off Friction** 选项卡中的参数值确定。

  模块使用 Simscape™ Rotational Friction 模块对摩擦分量建模。有关摩擦模型的详细信息，请参阅 Rotational Friction 模块参考页。

### 通电电机的谐振电路模型

当电机处于活动状态时，Piezo Rotary Actuator 模块使用以下等效电路模型表示电机特性。

在上图中：

- AC 电压源表示模块的频率为 *f*、幅值为 *v* 的物理信号输入。
- 电阻 *R* 提供主要的电气和机械阻尼项。
- 电感 *L* 表示转子振动惯量。
- 电容 *C* 表示压电晶体刚度。
- 电容 *Cp* 表示相电容。这是与两个电机相中每一相相关联的电气电容。
- 转矩常数 *kt* 将 RMS 电流 *i* 与产生的机械转矩相关联。
- 二次机械阻尼项 *λωm*2 主要在速度接近最大 RPM 时塑造转矩-速度曲线。*ωm* 是机械转速。
- 项 Jω˙m 表示转子惯量。

在模型初始化时，模块计算模型参数 *R*、*L*、*C*、*kt* 和 *λ*，以确保稳态转矩-速度曲线与以下用户指定参数值匹配：

- **Rated torque**
- **Rated rotational speed**
- **No-load maximum rotational speed**
- **Maximum torque**

这些参数值针对 **Rated RMS voltage** 和 **Motor natural frequency**（或额定频率）参数值定义。

二次机械阻尼项产生二次转矩-速度曲线。压电电机的转矩-速度曲线通常可以用二次函数比线性函数更准确地近似，因为当电机接近最大速度时，转矩-速度梯度变得更陡。

如果数据手册中未指定转子惯量 *J*，则可以选择一个与所给响应时间良好匹配的值。响应时间通常定义为在空载条件下，转子从静止启动达到最大速度所需的时间。

使用 **Resonance quality factor** 参数指定的品质因数与等效电路模型参数的关系如下：

Q=1RLC

该项通常不会在数据手册中提供。您可以通过匹配转矩对驱动频率的敏感度来计算其值。

要使电机反向运行，请将物理信号输入 *v* 设为负值。
