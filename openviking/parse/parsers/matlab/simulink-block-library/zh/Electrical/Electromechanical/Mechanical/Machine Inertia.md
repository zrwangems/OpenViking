---
type: simulink-block
title: 'Machine Inertia'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechanical'
documentation_page: 'machineinertia'
documentation_source_path: 'ref/machineinertia.html'
language: zh-CN
chinese_source: worker-translation
---

# Machine Inertia

## 端口

### 守恒端口

### **R** — 电机转子机械

与电机转子相关联的机械旋转守恒端口。

## 参数

### 主参数

### **Rated apparent power** — 额定视在功率 `555e6` `V*A`（默认值）

电机额定视在功率。

### **Rated electrical frequency** — 标称电气频率 `60` `Hz`（默认值）

与电机额定视在功率对应的标称电气频率。

### **Number of pole pairs** — 极对数 `1`（默认值）

所连接电机的极对数。

### 惯量

### **Specify inertia parameterization by** — 惯量参数化方式 `Inertia constant, H`（默认值） | `Actual Inertia, J`

惯量指定方式。

### **Inertia constant, H** — 惯量常数 `3.525` `s*W/VA`（默认值）

惯量常数。

#### 依赖关系

要启用此参数，请将 **Specify inertia
parameterization by** 设置为 `Inertia constant,
H`。

### **Actual inertia, J** — 实际惯量 `27548` `kg*m^2`（默认值）

电机转子的总旋转机械惯量。仅当将 **Specify inertia parameterization
by** 设置为 `Actual Inertia,
J` 时，此参数才可见。

#### 依赖关系

要启用此参数，请将 **Specify inertia
parameterization by** 设置为 `Actual Inertia,
J`。

### **Specify damper parameterization by** — 阻尼参数化方式 `Per-unit damping coefficient, pu_D`（默认值） | `SI damping coefficient, D`

阻尼指定方式。

### **Per-unit damping coefficient** — 标幺值阻尼系数 `0.01`（默认值）

标幺值阻尼系数。

#### 依赖关系

要启用此参数，请将 **Specify damper
parameterization by** 设置为 `Per-unit damping
coefficient, pu_D`。

### **SI damping coefficient** — 阻尼系数 `39.0509` `Nm/(rad/s)`（默认值）

国际单位制阻尼系数。

#### 依赖关系

要启用此参数，请将 **Specify damper
parameterization by** 设置为 `SI damping
coefficient, D`。

### 初始条件

### **Specify initialization by** — 频率初始化方式 `Initial electrical frequency`（默认值） | `Initial mechanical frequency`

频率初始化方式。

### **Initial electrical frequency** — 初始电气频率 `60` `Hz`（默认值）

初始电气频率，以国际单位制频率单位指定，例如
`Hz`、`kHz`、
`MHz` 或 `GHz`。

有关此参数单位的详细信息，请参阅 Units for Angular Velocity and Frequency。

#### 依赖关系

要启用此参数，请将 **Specify initialization
by** 设置为 `Initial electrical
frequency`。

### **Initial mechanical frequency** — 初始机械频率 `60` `Hz`（默认值）

初始机械频率，以国际单位制频率单位指定，例如
`Hz`、`kHz`、
`MHz` 或 `GHz`。

有关此参数单位的详细信息，请参阅 Units for Angular Velocity and Frequency。

#### 依赖关系

要启用此参数，请将 **Specify initialization
by** 设置为 `Initial mechanical
frequency`。

## 所属库

Simscape / Electrical / Electromechanical / Mechanical

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

使用电机惯量常数或锚点惯量参数化的电机惯量

Machine Inertia 模块对惯量和阻尼进行建模，将其连接到三相电机的机械旋转 R 端口。该模块具有到机械旋转参考的内部连接。图中展示了使用 Simscape™ 机械旋转组件实现的与 Machine Inertia 模块等效的配置。

根据为 **Specify inertia parameterization
by** 参数选择的值，可以直接指定惯量 *J*，或使用电机惯量常数 *H* 指定。

如果指定惯量常数，则该模块通过下式计算惯量

J=2HSrated(2πFrated/N)2，

其中：

- *J* 为惯量，单位为
  kg⋅m2。
- *H* 为惯量常数，单位为 sW/VA。
- *Srated* 为电机额定
  视在功率，单位为 VA。
- *Frated* 为电机额定
  电气频率，单位为 Hz。
- *N* 为电机极对数。

指定表示电机转子与机械旋转参考之间粘性摩擦的阻尼。根据为
**Specify damper parameterization by** 参数选择的值，
可以以国际单位制或标幺值指定阻尼系数。如果以标幺值指定阻尼系数，
则该模块通过下式计算国际单位制阻尼系数

ωbase=2πFratedN，

Tbase=Sratedωbase，

Dbase=Tbaseωbase，

以及

D=DpuDbase，

其中：

- *ωbase* 为基准机械
  角速度，单位为 rad/s。
- *Tbase* 为基准阻尼转矩，
  单位为 Nm。
- *Dbase* 为基准阻尼
  系数，单位为 Nm/(rad/s)。
- *Dpu* 为标幺值阻尼系数。
- *D* 为国际单位制阻尼系数，单位为
  Nm/(rad/s)。

### 显示选项

可以使用模块上下文菜单上的 **Electrical**
菜单显示电机参数。

右键单击该模块，然后从 **Electrical** 菜单中选择 **Display Parameters**，以在 MATLAB® 命令窗口中显示
电机标幺值基准值和惯量参数。
