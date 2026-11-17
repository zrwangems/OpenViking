---
type: simulink-block
title: 'Machine Mechanical Power'
family: 'electromechanical'
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

### **Pm** — 机械功率物理 | 正

与机械功率关联的物理信号输入端口，单位为 W。

#### 依赖项

仅当您将 **主要** 设置中的 **PS 输入单位** 参数设置为 `SI` 时，此端口才可见。

### **pu** — 标幺值机械功率物理 | 正

与机械功率关联的物理信号输入端口，单位为标幺值。

#### 依赖项

仅当您将 **主要** 设置中的 **PS 输入单位** 参数设置为 `Per unit` 时，此端口才可见。
### 守恒

### **R** — 机器转子机械

与机器转子关联的机械旋转守恒端口。

### **C** — 机器机壳机械

与机器机壳关联的机械旋转守恒端口。

## 参数

### 主要

### **输入功率符号约定** — 类型规范 `Generator` (默认) | `Motor`

机器类型规范。

### **额定视在功率** — 额定视在功率 `555e6` `V*A` (默认)

所连接机器的额定视在功率。

### **额定电气频率** — 标称电气频率 `60` `Hz` (默认)

与所连接机器的额定视在功率对应的标称电气频率。

### **极对数** — 极对数 `1` (默认)

所连接机器的极对数。

### **PS 输入单位** — 物理信号单位制 `SI` (默认) | `Per unit`

物理信号输入的单位制。

选择 `SI` 以显示 **Pm** 端口，或选择 `Per unit` 以显示 **pu** 端口。

### **峰值转矩与额定转矩之比** — 峰值转矩与额定转矩之比 `2` (默认)

模块将该比率乘以基准转矩，以提供用于加速惯量的转矩上限。

### 惯量

### **指定惯量参数化的方式** — 惯量参数化 `Inertia constant, H` (默认) | `Actual Inertia, J`

惯量规范。

### **惯量常数, H** — 惯量常数 `3.525` `s*W/VA` (默认)

惯量常数。

#### 依赖项

仅当您将 **指定惯量参数化的方式** 参数设置为 `Inertia constant, H` 时，此参数才可见。

### **实际惯量, J** — 实际惯量 `27548` `kg*m^2` (默认)

机器转子的总旋转机械惯量。仅当您将 **指定惯量参数化的方式** 设置为 `Actual Inertia, J` 时，此参数才可见。

#### 依赖项

仅当您将 **指定惯量参数化的方式** 参数设置为 `Actual Inertia, J` 时，此参数才可见。

### **指定阻尼器参数化的方式** — 阻尼参数化 `Per-unit damping coefficient, pu_D` (默认) | `SI damping coefficient, D`

阻尼规范。

### **标幺值阻尼系数** — 标幺值阻尼系数 `0.01` (默认)

以标幺值表示的阻尼系数。

#### 依赖项

仅当您将 **指定阻尼器参数化的方式** 参数设置为 `Per-unit damping coefficient, pu_D` 时，此参数才可见。

### **SI 阻尼系数** — 阻尼系数 `39.0509` `Nm/(rad/s)` (默认)

以 SI 单位表示的阻尼系数。

#### 依赖项

仅当您将 **指定阻尼器参数化的方式** 参数设置为 `SI damping coefficient, D` 时，此参数才可见。

### 初始条件

### **指定初始化的方式** — 频率初始化 `Initial electrical frequency` (默认) | `Initial mechanical frequency`

频率初始化。

### **初始电气频率** — 初始电气频率 `60` `Hz` (默认)

初始电气频率。

#### 依赖项

仅当您将 **指定初始化的方式** 参数设置为 `Initial electrical frequency` 时，此参数才可见。

### **初始机械频率** — 初始机械频率 `60` `Hz` (默认)

初始机械频率。

#### 依赖项

仅当您将 **指定初始化的方式** 参数设置为 `Initial mechanical frequency` 时，此参数才可见。

## 所属库

Simscape / Electrical / Electromechanical / Mechanical

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

以 SI 或标幺值系统定义的机器机械功率

Machine Mechanical Power 模块向其所连接的机器提供指定功率，或从其所连接的机器吸收指定功率。它包括机器惯量和机械旋转参考的表示。在发电机模式下，物理信号输入定义输入到机器的机械功率。在电动机模式下，它定义机器的机械功率输出。

该图显示了使用 Simscape™ 机械旋转组件构建的、与 Machine Mechanical Power 模块的标幺值变体模型等效的配置。

### 电气定义方程

SI 模型将您在对话框中输入的 SI 值转换为用于仿真的标幺值。有关 SI 与标幺值机器参数之间关系的信息，请参阅 Per-Unit Conversion for Machine Parameters。有关标幺值参数化的信息，请参阅 Per-Unit System of Units。

为了计算其施加到惯量上的转矩，该模块将功率需求除以当前转速。要设置峰值转矩限值，请为 **峰值转矩与额定转矩之比** 参数指定一个值。使用 **指定惯量参数化的方式** 参数，可直接指定惯量 *J*，也可通过机器的惯量常数 *H* 间接指定。

如果您指定机器的惯量常数，则该模块按以下公式计算惯量：

J=2HSrated(2πFrated/N)2,

其中：

- *J* 是惯量，单位为 kg⋅m2。
- *H* 是惯量常数，单位为 sW/VA。
- *Srated* 是所连接机器的额定视在功率，单位为 VA。
- *Frated* 是所连接机器的额定电气频率，单位为 Hz。
- *N* 是机器极对数。

阻尼表示机器转子与机械旋转参考之间的粘性摩擦。根据您为 **指定阻尼器参数化的方式** 参数选择的值，您可以以标幺值或 SI 单位指定阻尼系数。如果您以标幺值指定阻尼系数，则该模块使用以下公式计算 SI 单位下的阻尼系数：

ωbase=2πFratedN,

Tbase=Sratedωbase,

Dbase=Tbaseωbase,

以及

D=DpuDbase,

其中：

- *ωbase* 是基准机械转速，单位为 rad/s。
- *Tbase* 是基准阻尼转矩，单位为 Nm。
- *Dbase* 是基准阻尼系数，单位为 Nm/(rad/s)。
- *Dpu* 是阻尼系数，以标幺值表示。
- *D* 是阻尼系数，SI 单位为 Nm/(rad/s)。
