---
type: simulink-block
title: 'Piezo Rotary Actuator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechatronic Actuators'
documentation_page: 'piezorotaryactuator'
documentation_source_path: 'ref/piezorotaryactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Piezo Rotary Actuator

## 端口

### 输入

### **f** — 电机驱动频率物理量

与电机驱动频率相关联的物理信号输入端口，单位为 Hz。

### **v** — RMS 电源电压和旋转方向物理量

物理信号输入幅值端口，指定 RMS 电源电压，符号指定旋转方向。如果 `v` 为正，则正扭矩从端口 **C** 作用于端口 **R**。

### 输出

### **i** — RMS 相电流物理量

与 RMS 相电流相关联的物理信号输出端口。

### **wm** — 转子速度物理量

与转子转速相关联的物理信号输出端口。

### 守恒

### **C** — 外壳机械

与电机外壳相关联的机械平移守恒端口。

### **R** — 转子机械

与电机转子相关联的机械平移守恒端口。

## 参数

### 电气扭矩

### **Motor natural frequency** — 电机固有频率 `40` `kHz`（默认值）

压电晶体自然共振的频率。对于大多数应用，将端口 **f** 处的输入信号设置为此频率。要降低电机速度，例如在闭环速度控制中，使用略低于电机固有频率的频率。默认值为 `40``kHz`。

### **Rated RMS voltage** — 额定 RMS 电压 `130` `V`（默认值）

电机设计工作时的电压。

### **Rated torque** — 额定扭矩 `0.5` `N*m`（默认值）

电机在额定 RMS 电压下输出的扭矩。

### **Rated rotational speed** — 额定转速 `100` `rpm`（默认值）

电机在额定扭矩下驱动负载时的电机速度。

### **No-load maximum rotational speed** — 空载最大转速 `160` `rpm`（默认值）

电机在空载、额定电压和驱动频率供电时的转速。

### **Maximum torque** — 最大扭矩 `1` `N*m`（默认值）

电机在额定电压和频率下主动驱动负载时输出的最大扭矩。默认值为 `1``N*m`。

**注意**

**Holding torque** 参数值，即电机静止时保持的负载扭矩，可能大于 **Maximum torque** 参数值。

### **Resonance quality factor** — 共振品质因数 `100`（默认值）

品质因数 *Q*，指定扭矩随驱动频率变化的函数关系。增加品质因数会导致当驱动频率偏离固有频率时扭矩下降得更快。

### **Capacitance per phase** — 每相电容 `5` `nF`（默认值）

与两个电机相位中每一相关联的电容。

### 机械

### **Rotor inertia** — 转子惯量 `200` `g*cm^2`（默认值）

转子对电机运动变化的阻力。

### 电机关闭摩擦

### **Holding torque** — 保持扭矩 `1.5` `N*m`（默认值）

库仑摩擦和静摩擦之和。它必须大于或等于 **Coulomb friction torque** 参数值。

### **Coulomb friction torque** — 库仑摩擦力矩 `1.0` `N*m`（默认值）

在任何速度下以恒定扭矩阻碍旋转的摩擦。

### **Viscous friction coefficient** — 粘性摩擦系数 `0.001` `N*m/(rad*s)`（默认值） | 非负标量

摩擦力矩与相对角速度之间的比例系数。

### **Transition approximation coefficient** — 过渡近似系数 `10` `s/rad`（默认值）

该参数设置用于近似静摩擦和库仑摩擦之间过渡的系数值。有关系数 *cv* 的详细信息，请参阅 Simscape Rotational Friction 模块参考页。

### **Linear region velocity threshold** — 线性区域速度阈值 `1e-4` `rad/s`（默认值）

该参数设置零速度附近的小邻域，在该邻域内摩擦力矩被认为与相对速度成线性比例。MathWorks® 建议使用 `1e-5` 到 `1e-3` `rad/s` 范围内的值。

## 所属库

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

旋转压电行波电机的转矩-速度特性

Piezo Rotary Actuator 模块表示压电行波电机的转矩-速度特性。该模块在适合系统级建模的层面上表示电机的转矩-速度关系。为了仿真该电机，该模块使用以下模型：

- 未通电电机的惯量与摩擦模型
- 通电电机的谐振电路模型

### 未通电电机的惯量与摩擦模型

当物理信号输入 *v* 为零时，电机未通电。这对应于向电机施加零 RMS 伏特。在此场景下，该模块使用以下元素对电机建模：

- 一个惯量，其值为 **Rotor inertia** 参数值。
- 一个摩擦，其特性由 **Motor-Off Friction** 选项卡中的参数值确定。

  该模块使用 Simscape™ Rotational Friction 模块来对摩擦分量建模。有关摩擦模型的详细信息，请参阅 Rotational Friction 模块参考页。

### 用于动力电机的谐振电路模型

当电机处于活动状态时，Piezo Rotary Actuator 模块使用以下等效电路模型来表示电机特性。

在上图中：

- 交流电压源表示模块的物理信号输入，其频率为 *f*，幅值为 *v*。
- 电阻 *R* 提供主要的电气和机械阻尼项。
- 电感 *L* 表示转子振动惯量。
- 电容 *C* 表示压电晶体刚度。
- 电容 *Cp* 表示相位电容。这是与两个电机相位中的每一个相关联的电容。
- 转矩常数 *kt* 将 RMS 电流 *i* 与产生的机械转矩相关联。
- 二次机械阻尼项 *λωm*2 主要在接近最大 RPM 的速度下决定转矩-速度曲线的形状。*ωm* 是机械转速。
- 项 Jω˙m 表示转子惯量。

在模型初始化时，模块会计算模型参数 *R*、*L*、*C*、*kt* 和 *λ*，以确保稳态转矩-速度曲线与以下用户指定参数值的值匹配：

- **额定转矩**
- **额定转速**
- **空载最大转速**
- **最大转矩**

这些参数值是为 **额定 RMS 电压** 和 **电机固有频率**（或额定频率）参数值定义的。

二次机械阻尼项会产生二次转矩-速度曲线。压电电机的转矩-速度曲线通常使用二次函数比使用线性函数能更准确地近似，因为当电机接近最大速度时，转矩-速度梯度会变得更陡。

如果数据表中未指定转子惯量 *J*，您可以选择一个能够与所给响应时间很好匹配的值。响应时间通常定义为在空载条件下，转子从静止开始达到最大速度所需的时间。

您使用 **谐振品质因数** 参数指定的品质因数与等效电路模型参数的关系如下：

Q=1RLC

该项通常不会在数据表中提供。您可以通过匹配转矩对驱动频率的灵敏度来计算其值。

要使电机反向运行，请将物理信号输入 *v* 设为负值。
