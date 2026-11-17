---
type: simulink-block
title: 'Machine Mechanical Power'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechanical'
documentation_page: 'machinemechanicalpower'
documentation_source_path: 'ref/machinemechanicalpower.html'
language: zh-CN
chinese_source: worker-translation
---

# Machine Mechanical Power

## 端口

### 输入

### **Pm** — 机械功率 物理 | 正

与机械功率相关联的物理信号输入端口，单位为
W。

#### 依赖关系

仅当您将 **Main** 设置中的 **PS input
unit** 参数设置为 `SI` 时，此端口才可见。

### **pu** — 标幺值机械功率 物理 | 正

与机械功率相关联的物理信号输入端口，单位为
标幺值。

#### 依赖关系

仅当您将 **Main** 设置中的 **PS input
unit** 参数设置为 `Per unit` 时，此端口才可见。
### 守恒

### **R** — 电机转子 机械

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机机壳 机械

与电机机壳相关联的机械旋转守恒端口。

## 参数

### 主要参数

### **Input power sign convention** — 类型规格 `Generator`（默认）| `Motor`

电机类型规格。

### **Rated apparent power** — 额定视在功率 `555e6` `V*A`（默认）

所连接电机的额定视在功率。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）

与所连接电机的额定视在功率相对应的额定电气频率。

### **Number of pole pairs** — 极对数 `1`（默认）

所连接电机的极对数。

### **PS input unit** — 物理信号单位制 `SI`（默认）| `Per unit`

物理信号输入的单位制。

选择 `SI` 以显示
**Pm** 端口，或选择 `Per unit`
以显示 **pu** 端口。

### **Peak torque to rated torque ratio** — 峰值转矩与额定转矩之比 `2`（默认）

该模块将此比值乘以基准转矩，以提供加速惯量的转矩上限。

### Inertia

### **Specify inertia parameterization by** — 惯量参数化 `Inertia constant, H`（默认）| `Actual Inertia, J`

惯量规格。

### **Inertia constant, H** — 惯量常数 `3.525` `s*W/VA`（默认）

惯量常数。

#### 依赖关系

仅当您将 **Specify
inertia parameterization by** 参数设置为
`Inertia constant, H` 时，此参数才可见。

### **Actual inertia, J** — 实际惯量 `27548` `kg*m^2`（默认）

电机转子的总旋转机械惯量。仅当您将 **Specify inertia parameterization
by** 设置为 `Actual Inertia,
J` 时，此参数才可见。

#### 依赖关系

仅当您将 **Specify
inertia parameterization by** 参数设置为
`Actual Inertia, J` 时，此参数才可见。

### **Specify damper parameterization by** — 阻尼参数化 `Per-unit damping coefficient, pu_D`（默认）| `SI damping coefficient, D`

阻尼规格。

### **Per-unit damping coefficient** — 标幺值阻尼系数 `0.01`（默认）

标幺值阻尼系数。

#### 依赖关系

仅当您将 **Specify
damper parameterization by** 参数设置为
`Per-unit damping coefficient,
pu_D` 时，此参数才可见。

### **SI damping coefficient** — 阻尼系数 `39.0509` `Nm/(rad/s)`（默认）

SI 单位下的阻尼系数。

#### 依赖关系

仅当您将 **Specify
damper parameterization by** 参数设置为
`SI damping coefficient, D` 时，此参数才可见。

### 初始条件

### **Specify initialization by** — 频率初始化 `Initial electrical frequency`（默认）| `Initial mechanical frequency`

频率初始化。

### **Initial electrical frequency** — 初始电气频率 `60` `Hz`（默认）

初始电气频率。

#### 依赖关系

仅当您将 **Specify
initialization by** 参数设置为 `Initial
electrical frequency` 时，此参数才可见。

### **Initial mechanical frequency** — 初始机械频率 `60` `Hz`（默认）

初始机械频率。

#### 依赖关系

仅当您将 **Specify
initialization by** 参数设置为 `Initial
mechanical frequency` 时，此参数才可见。

## 所属库

Simscape / Electrical / Electromechanical / Mechanical

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

以 SI 或标幺值系统定义的电机机械功率

Machine Mechanical Power 模块向其所连接的电机提供指定功率，或从其所连接的电机抽取指定功率。它包含电机惯量和机械旋转参考的表示。在发电机模式下，物理信号输入定义输入到电机的机械功率。在电动机模式下，它定义从电机输出的机械功率。

该图展示了使用 Simscape™ 机械旋转组件实现的 Machine Mechanical Power 模块标幺值变体模型的等效配置。

### 电气定义方程

SI 模型将您在对话框中输入的 SI 值转换为标幺值以进行仿真。有关 SI 与标幺值电机参数之间关系的信息，请参阅 Per-Unit Conversion for Machine Parameters。有关标幺值参数化的信息，请参阅 Per-Unit System of Units。

为计算施加到惯量上的转矩，该模块将功率需求除以当前转速。要设置峰值转矩限值，请为 **Peak torque to rated torque ratio** 参数指定一个值。使用 **Specify inertia parameterization by** 参数可直接或间接地指定惯量 *J*，并使用电机的惯量常数 *H*。

如果您指定电机的惯量常数，则该模块按如下方式计算惯量

J=2HSrated(2πFrated/N)2，

其中：

- *J* 为惯量，单位为
  kg⋅m2。
- *H* 为惯量常数，单位为 sW/VA。
- *Srated* 为所连接电机的额定视在
  功率，单位为 VA。
- *Frated* 为所连接电机的额定
  电气频率，单位为 Hz。
- *N* 为电机极对数。

阻尼表示电机转子与机械旋转参考之间的粘性摩擦。根据您为 **Specify damper parameterization by** 参数选择的值，您可以以标幺值或 SI 单位指定阻尼系数。如果您以标幺值指定阻尼系数，则该模块使用以下方程计算 SI 单位下的阻尼系数：

ωbase=2πFratedN，

Tbase=Sratedωbase，

Dbase=Tbaseωbase，

以及

D=DpuDbase，

其中：

- *ωbase* 为基准机械
  转速，单位为 rad/s。
- *Tbase* 为基准阻尼
  转矩，单位为 Nm。
- *Dbase* 为基准阻尼
  系数，单位为 Nm/(rad/s)。
- *Dpu* 为标幺值
  阻尼系数。
- *D* 为 SI 单位下的阻尼系数，
  单位为 Nm/(rad/s)。
