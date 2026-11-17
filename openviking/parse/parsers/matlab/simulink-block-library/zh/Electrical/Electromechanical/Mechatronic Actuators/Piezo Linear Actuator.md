---
type: simulink-block
title: 'Piezo Linear Actuator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechatronic Actuators'
documentation_page: 'piezolinearactuator'
documentation_source_path: 'ref/piezolinearactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Piezo Linear Actuator

## 端口
```yaml
ports:
- name: f
  summary: 电机驱动频率物理量
  direction: input
- name: v
  summary: RMS 电源电压和旋转方向物理量
  direction: input
- name: i
  summary: RMS 相电流物理量
  direction: output
- name: vel
  summary: 转子速度物理量
  direction: output
- name: C
  summary: 外壳机械
  direction: output
- name: R
  summary: 转子机械
  direction: output
```

### 输入

### **f** — 电机驱动频率物理量

与电机驱动频率相关联的物理信号输入端口，单位为 Hz。

### **v** — RMS 电源电压和旋转方向物理量

物理信号输入幅值端口，指定 RMS 电源电压，符号指定旋转方向。如果
`v` 为正，则正力从端口 **C** 作用于端口 **R**。
### 输出

### **i** — RMS 相电流物理量

与 RMS 相电流相关联的物理信号输出端口。

### **vel** — 转子速度物理量

与转子线速度相关联的物理信号输出端口。
### 守恒

### **C** — 外壳机械

与电机外壳相关联的机械平移守恒端口。

### **R** — 转子机械

与电机转子相关联的机械平移守恒端口。
## 参数
```yaml
parameters:
- name: Motor natural frequency
  summary: 电机固有频率 92 kHz（默认值）
  group: 电力
- name: Rated RMS voltage
  summary: 额定 RMS 电压 5.7 V（默认值）
  group: 电力
- name: Rated force
  summary: 额定力 0.1 N（默认值）
  group: 电力
- name: Rated speed
  summary: 额定速度 50 mm/s（默认值）
  group: 电力
- name: No-load maximum speed
  summary: 空载最大速度 150 mm/s（默认值）
  group: 电力
- name: Maximum (stall) force
  summary: 最大力 0.15 N（默认值）
  group: 电力
- name: Resonance quality factor
  summary: 共振品质因数 100（默认值）
  group: 电力
- name: Capacitance per phase
  summary: 每相电容 5 nF（默认值）
  group: 电力
- name: Plunger mass
  summary: 柱塞质量 0.3 g（默认值）
  group: 机械
- name: Holding force
  summary: 保持力 0.3 N（默认值）
  group: 电机关闭摩擦
- name: Coulomb friction force
  summary: 库仑摩擦力 0.15 N（默认值）
  group: 电机关闭摩擦
- name: Viscous friction coefficient
  summary: 粘性摩擦系数 1e-5 s*N/mm（默认值）| 非负标量
  group: 电机关闭摩擦
- name: Transition approximation coefficient
  summary: 过渡近似系数 0.1 s/mm（默认值）
  group: 电机关闭摩擦
- name: Linear region velocity threshold
  summary: 线性区域速度阈值 0.1 mm/s（默认值）
  group: 电机关闭摩擦
```

### 电力

### **Motor natural frequency** — 电机固有频率 `92` `kHz`（默认值）

压电晶体自然共振的频率。对于大多数应用，将端口 `f` 处的输入信号设置为此频率。要降低电机速度，例如在闭环速度控制中，使用略低于电机固有频率的频率。

### **Rated RMS voltage** — 额定 RMS 电压 `5.7` `V`（默认值）

电机设计工作时的电压。

### **Rated force** — 额定力 `0.1` `N`（默认值）

电机在额定 RMS 电压下输出的力。

### **Rated speed** — 额定速度 `50` `mm/s`（默认值）

电机以额定力驱动负载时的电机速度。

### **No-load maximum speed** — 空载最大速度 `150` `mm/s`（默认值）

在额定电压和驱动频率下驱动空载时的电机速度。

### **Maximum (stall) force** — 最大力 `0.15` `N`（默认值）

电机在额定电压和频率下主动驱动负载时输出的最大力。

**注意**

**Holding force** 参数值（电机静止时保持的负载力）可能大于 **Maximum (stall) force** 参数值。

### **Resonance quality factor** — 共振品质因数 `100`（默认值）

品质因数 *Q*，指定力随驱动频率变化的函数关系。增加品质因数会导致当驱动频率偏离固有频率时力下降得更快。

### **Capacitance per phase** — 每相电容 `5` `nF`（默认值）

与两个电机相位中每一相关联的电容。

### 机械

### **Plunger mass** — 柱塞质量 `0.3` `g`（默认值）

电机运动部件的质量。

### 电机关闭摩擦

### **Holding force** — 保持力 `0.3` `N`（默认值）

库仑摩擦和静摩擦之和。它必须大于或等于 **Coulomb friction force** 参数值。

### **Coulomb friction force** — 库仑摩擦力 `0.15` `N`（默认值）

在任何速度下以恒定力阻碍旋转的摩擦力。

### **Viscous friction coefficient** — 粘性摩擦系数 `1e-5` `s*N/mm`（默认值）| 非负标量

摩擦力与相对速度之间的比例系数。

### **Transition approximation coefficient** — 过渡近似系数 `0.1` `s/mm`（默认值）

该参数设置用于近似静摩擦和库仑摩擦之间过渡的系数值。有关系数 *cv* 的详细信息，请参阅 Simscape Translational Friction 模块参考页。

### **Linear region velocity threshold** — 线性区域速度阈值 `0.1` `mm/s`（默认值）

该参数设置零速度附近的小邻域，在该邻域内摩擦力被认为与相对速度成线性比例。MathWorks 建议使用 `1e-6` 到 `1e-4` mm/s 之间的值。
## 所属库

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

线性压电行波电机的力-速度特性

Piezo Linear Actuator 模块表示线性压电行波电机的力-速度特性。该模块在适合系统级建模的层面上表示电机的力-速度关系。为了仿真电机，该模块使用以下模型：

- 未通电电机的质量和摩擦模型
- 通电电机的谐振电路模型

### 未通电电机的质量和摩擦模型

当物理信号输入 *v* 为零时，电机未通电。这对应于向电机施加零 RMS 伏特。在此场景中，该模块使用以下元素对电机建模：

- 质量，其值为 **Plunger mass** 参数值。
- 摩擦，其特性使用 **Motor-Off Friction** 选项卡中的参数值指定。

  该模块使用 Simscape™ Translational Friction 模块对摩擦分量建模。有关摩擦模型的详细信息，请参阅 Translational Friction 模块参考页。

### 通电电机的谐振电路模型

当电机激活时，Piezo Linear Actuator 模块使用以下等效电路模型表示电机特性。

在前图中：

- 交流电压源表示模块的物理信号输入，频率为 *f*，幅值为 *v*。
- 电阻 *R* 提供主要的电气和机械阻尼项。
- 电感 *L* 表示转子振动惯性。
- 电容 *C* 表示压电晶体刚度。
- 电容 *Cp* 表示相位电容。这是与两个电机相位中每一相关联的电容。
- 力常数 *kf* 将 RMS 电流 *i* 与产生的机械力相关联。
- 二次机械阻尼项 λx˙2 主要在速度接近最大 RPM 时塑造力-速度曲线。x˙ 是线速度。
- 项 Mx˙ 表示柱塞惯性。

在模型初始化时，该模块计算模型参数 *R*、*L*、*C*、*kt* 和 *λ*，以确保稳态力-速度曲线与以下用户指定参数的值匹配：

- **Rated force**
- **Rated speed**
- **No-load maximum speed**
- **Maximum (stall) force**

这些参数值针对 **Rated RMS voltage** 和 **Motor natural frequency**（或额定频率）参数值定义。

二次机械阻尼项产生二次力-速度曲线。压电电机的力-速度曲线通常使用二次函数比线性函数能更准确地近似，因为当电机接近最大速度时，力-速度梯度变得更陡。

如果数据表中未指定柱塞质量 *M*，您可以选择一个与所引用响应时间良好匹配的值。响应时间通常定义为在空载条件下转子从静止达到最大速度所需的时间。

您使用 **Resonance quality factor** 参数指定的品质因数与等效电路模型参数的关系如下：

Q=1RLC

该术语通常不在数据表中提供。您可以通过匹配力对驱动频率的灵敏度来计算其值。

要反转电机运行方向，使物理信号输入 *v* 为负。
