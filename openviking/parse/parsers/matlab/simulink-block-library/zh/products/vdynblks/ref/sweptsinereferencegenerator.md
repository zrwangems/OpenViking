---
type: simulink-block
title: 'Swept Sine Reference Generator'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'sweptsinereferencegenerator'
documentation_source_path: 'ref/sweptsinereferencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Swept Sine Reference Generator

## 端口

### 输入

### **VehFdbk** — 车辆反馈 `Bus`

包含车辆反馈信号的 Bus，包括速度、加速度和方向盘扭矩。
### 输出

### **Ref** — 车辆参考信号 `Bus`

包含车辆参考信号的 Bus，包括纵向和横向位移以及转向。

## 参数

#### 机动

### **稳态求解器模式** — 从稳态启动机动 `Initialize from model`（默认） | `Solve using block parameters` | `Resume from a workspace variable`

使用 **稳态求解器模式** 参数来指定机动的稳态初始条件。默认情况下，仿真不会查找稳态工作点，也不会在稳态工作点启动仿真。

| 设置 | 描述 |
| --- | --- |
| `Initialize from model` | 仿真在由 **机动开始时间, t\_start** 指定的仿真开始时间以纵向速度 0 启动机动。 |
| `Solve using block parameters` | 仿真使用 **稳态求解器** 选项卡上的参数*查找*稳态工作点。 |
| `Resume from a workspace variable` | 仿真在由 **要从中启动的稳态解, ssVar** 指定的稳态工作点工作区变量处*启动*。 |

### **要从中启动的稳态解, ssVar** — 具有稳态工作点的工作区变量 `char`

包含稳态工作点的工作区变量。

#### 依赖关系

要启用此参数，请将 **稳态求解器模式** 设置为 `Resume from a workspace variable`。

### **机动开始时间, t\_start** — 开始时间 `scalar`

机动开始时间，单位为 s。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Initialize from model`。

### **纵向速度设定点, xdot\_ref** — 目标速度 `50`（默认） | `scalar`

目标速度。

### **纵向速度设定点单位, xdotUnit** — 单位 `mph`（默认）

目标速度的单位。

### **转向幅度, theta\_hw** — 转向幅度 `scalar`

正弦转向幅度，单位为 deg。

### **最终频率, theta\_hw\_final** — 最终频率 `scalar`

用于停止机动的截止频率，单位为 Hz。

### **扫频时间, t\_sweep** — 扫频时间 `scalar`

扫频时间，单位为 s。

#### 稳态求解器

### **初始纵向位置, X\_o** — 初始纵向位置 `175`（默认） | `scalar`

车辆 CG 沿大地固定 *X* 轴的初始位置，单位为 m。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **初始横向位置, Y\_o** — 初始横向位置 `scalar`

车辆 CG 沿大地固定 *Y* 轴的初始位置，单位为 m。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **初始航向（偏航）角, psi\_o** — 初始偏航角 `scalar`

车辆绕大地固定 *Z* 轴的初始偏航角，单位为 rad。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **稳态求解器容差, ssTol** — 求解器速度容差 `scalar`

稳态求解器速度容差。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **达到稳态的最大仿真时间, ssMaxTime** — 最大时间 `scalar`

达到稳态的最大仿真时间，单位为 s。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **要生成的工作区变量名称, ssWSName** — 稳态工作点 `scalar`

包含稳态工作点的工作区变量名称。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2019a 中引入**

## 描述

生成扫频正弦机动参考信号

Swept Sine Reference Generator 模块设置用于配置扫频正弦机动的参数。一旦车辆达到目标纵向速度，该模块会生成频率线性增加的正弦转向命令，直至在规定时间内达到指定的最大值。

使用 **稳态求解器模式** 参数来指定机动的初始条件。默认情况下，该参数设置为 `Initialize from model`，仿真从车辆在指定初始位置静止开始。如果要在非零稳态速度下启动仿真：

1. 将 **稳态求解器模式** 设置为 `Solve using block parameters`。
2. 在 **稳态求解器** 选项卡上，指定初始条件、工作区变量和求解器设置。点击 **生成稳态解**。
3. 仿真完成后，将 **稳态求解器模式** 设置为 `Resume from a workspace variable`。
4. 将 **要从中启动的稳态解, ssVar** 设置为在步骤 2 中指定的工作区变量。
5. 运行仿真。
