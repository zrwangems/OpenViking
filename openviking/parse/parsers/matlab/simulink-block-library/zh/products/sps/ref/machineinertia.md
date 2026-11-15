---
type: simulink-block
title: 'Machine Inertia'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Mechanical'
documentation_page: 'machineinertia'
documentation_source_path: 'ref/machineinertia.html'
language: zh-CN
chinese_source: worker-translation
---

# Machine Inertia

## 端口

### 守恒

### **R** — 电机转子机械

与电机转子关联的机械旋转守恒端口。

## 参数

### 主要

### **额定视在功率** — 额定视在功率 `555e6` `V*A`（默认）

电机额定视在功率。

### **额定电气频率** — 标称电气频率 `60` `Hz`（默认）

对应于电机额定视在功率的标称电气频率。

### **极对数** — 极对数 `1`（默认）

所连接电机的极对数。

### 惯量

### **指定惯量参数化方式** — 惯量参数化 `Inertia constant, H`（默认） | `Actual Inertia, J`

惯量指定。

### **惯量常数，H** — 惯量常数 `3.525` `s*W/VA`（默认）

惯量常数。

#### 依赖关系

要启用此参数，请将 **指定惯量参数化方式** 设置为 `Inertia constant, H`。

### **实际惯量，J** — 实际惯量 `27548` `kg*m^2`（默认）

电机转子的总旋转机械惯量。仅当将 **指定惯量参数化方式** 设置为 `Actual Inertia, J` 时，此参数才可见。

#### 依赖关系

要启用此参数，请将 **指定惯量参数化方式** 设置为 `Actual Inertia, J`。

### **指定阻尼参数化方式** — 阻尼参数化 `Per-unit damping coefficient, pu_D`（默认） | `SI damping coefficient, D`

阻尼指定。

### **标幺值阻尼系数** — 标幺值阻尼系数 `0.01`（默认）

以标幺值表示的阻尼系数。

#### 依赖关系

要启用此参数，请将 **指定阻尼参数化方式** 设置为 `Per-unit damping coefficient, pu_D`。

### **SI 阻尼系数** — 阻尼系数 `39.0509` `Nm/(rad/s)`（默认）

SI 单位下的阻尼系数。

#### 依赖关系

要启用此参数，请将 **指定阻尼参数化方式** 设置为 `SI damping coefficient, D`。

### 初始条件

### **指定初始化方式** — 频率初始化 `Initial electrical frequency`（默认） | `Initial mechanical frequency`

频率初始化。

### **初始电气频率** — 初始电气频率 `60` `Hz`（默认）

初始电气频率，以 SI 频率单位指定，例如 `Hz`、`kHz`、`MHz` 或 `GHz`。

有关此参数单位的详细信息，请参阅角速度和频率的单位。

#### 依赖关系

要启用此参数，请将 **指定初始化方式** 设置为 `Initial electrical frequency`。

### **初始机械频率** — 初始机械频率 `60` `Hz`（默认）

初始机械频率，以 SI 频率单位指定，例如 `Hz`、`kHz`、`MHz` 或 `GHz`。

有关此参数单位的详细信息，请参阅角速度和频率的单位。

#### 依赖关系

要启用此参数，请将 **指定初始化方式** 设置为 `Initial mechanical frequency`。

## 所属库

Simscape / Electrical / Electromechanical / Mechanical

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

电机惯量使用电机惯量常数或锚定惯量进行参数化

Machine Inertia 模块对连接到三相电机的机械旋转 R 端口的惯量和阻尼进行建模。该模块具有到机械旋转参考的内部连接。该图展示了使用 Simscape™ 机械旋转组件构成的与 Machine Inertia 模块等效的配置。

根据为 **指定惯量参数化方式** 参数选择的值，可直接指定惯量 *J*，或使用电机惯量常数 *H* 指定惯量。

如果指定惯量常数，则该模块通过以下公式计算惯量

J=2HSrated(2πFrated/N)2,

其中：

- *J* 是惯量，单位为
  kg⋅m2。
- *H* 是惯量常数，单位为 sW/VA。
- *Srated* 是电机额定
  视在功率，单位为 VA。
- *Frated* 是电机额定
  电气频率，单位为 Hz。
- *N* 是电机极对数。

您指定表示电机转子与机械旋转参考之间黏性摩擦的阻尼。根据为 **指定阻尼参数化方式** 参数选择的值，可以 SI 单位或标幺值指定阻尼系数。如果以标幺值指定阻尼系数，则该模块通过以下公式计算 SI 单位下的阻尼系数

ωbase=2πFratedN,

Tbase=Sratedωbase,

Dbase=Tbaseωbase,

以及

D=DpuDbase,

其中：

- *ωbase* 是基准机械
  角速度，单位为 rad/s。
- *Tbase* 是基准阻尼转矩，
  单位为 Nm。
- *Dbase* 是基准阻尼
  系数，单位为 Nm/(rad/s)。
- *Dpu* 是阻尼系数，
  以标幺值表示。
- *D* 是 SI 单位下的阻尼系数，单位为
  Nm/(rad/s)。

### 显示选项

您可以使用模块上下文菜单中的 **电气** 菜单显示电机参数。

右键单击该模块，然后从 **电气** 菜单中选择 **显示参数**，以在 MATLAB® 命令窗口中显示电机标幺基准值和惯量参数。
