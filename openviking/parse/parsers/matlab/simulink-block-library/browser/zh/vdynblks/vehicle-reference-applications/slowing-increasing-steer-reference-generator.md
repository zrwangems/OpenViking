---
type: simulink-block
title: 'Slowing Increasing Steer Reference Generator'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'slowlyincreasingsteerreferencegenerator'
documentation_source_path: 'ref/slowlyincreasingsteerreferencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Slowing Increasing Steer Reference Generator

## 端口

### 输入

### **VehFdbk** — 车辆反馈 `Bus`

包含车辆反馈信号的 `Bus`，包括速度、加速度和方向盘扭矩。

### 输出

### **Ref** — 车辆参考信号 `Bus`

包含车辆参考信号的 `Bus`，包括纵向和横向位移以及转向。

## 参数

#### 机动

### **稳态求解器模式** — 从稳态开始机动 `Initialize from model`（默认） | `Solve using block parameters` | `Resume from a workspace variable`

使用 **稳态求解器模式** 参数指定机动的稳态初始条件。默认情况下，仿真不会在稳态工作点查找或启动仿真。

| 设置 | 描述 |
| --- | --- |
| `Initialize from model` | 仿真在由 **机动开始时间, t\_start** 指定的仿真开始时间以纵向速度 0 开始机动。 |
| `Solve using block parameters` | 仿真使用 **稳态求解器** 选项卡上的参数 *查找* 稳态工作点。 |
| `Resume from a workspace variable` | 仿真 *从* 由 **要开始于的稳态解, ssVar** 指定的稳态工作点工作区变量 *启动*。 |

### **要开始于的稳态解, ssVar** — 具有稳态工作点的工作区变量 `char`

工作区变量，包含稳态工作点。

#### 依赖项

要启用此参数，请将 **稳态求解器模式** 设置为 `Resume from a workspace variable`。

### **机动开始时间, t\_start** — 开始时间 `scalar`

机动开始时间，以 s 为单位。

#### 依赖项

要启用此参数，请将 **稳态初始条件** 设置为 `Initialize from model`。

### **纵向速度设定点, xdot\_r** — 目标速度 `50`（默认） | `scalar`

目标速度。

### **纵向速度设定点单位, xdotUnit** — 单位 `mph`（默认）

目标速度的单位。

### **方向盘速率, omega\_hw** — 方向盘速率 `scalar`

方向盘速率，以 deg/s 为单位。

### **最大绝对方向盘角度, theta\_max** — 最大方向盘 `scalar`

最大方向盘角度，以 deg 为单位。

### **达到最大角度后的转向保持时间, t\_stop** — 转向保持 `scalar`

转向保持，以 s 为单位。

### **横向加速度绝对阈值, ay\_max** — 横向加速度 `scalar`

横向加速度阈值，以 g 为单位。

#### 稳态求解器

### **初始纵向位置, X\_o** — 初始纵向位置 `175`（默认） | `scalar`

车辆质心沿地球固定 *X* 轴的初始位置，以 m 为单位。

#### 依赖项

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **初始横向位置, Y\_o** — 初始横向位置 `scalar`

车辆质心沿地球固定 *Y* 轴的初始位置，以 m 为单位。

#### 依赖项

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **初始航向（偏航）角, psi\_o** — 初始偏航角 `scalar`

车辆绕地球固定 *Z* 轴的初始偏航角，以 rad 为单位。

#### 依赖项

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **稳态求解器容差, ssTol** — 求解器速度容差 `scalar`

稳态求解器速度容差。

#### 依赖项

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **达到稳态的最大仿真时间, ssMaxTime** — 最大时间 `scalar`

达到稳态的最大仿真时间，以 s 为单位。

#### 依赖项

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

### **要生成的工作区变量名称, ssWSName** — 稳态工作点 `scalar`

包含稳态工作点的工作区变量名称。

#### 依赖项

要启用此参数，请将 **稳态初始条件** 设置为 `Solve using block parameters`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

生成缓慢增加的转向机动参考信号

Slowly Increasing Steer Reference Generator 模块设置用于配置缓慢增加的转向机动的参数。

该模块生成转向、加速和制动命令，以执行线性增加的转向机动。一旦车辆达到纵向速度设定点，转向命令以指定速率开始。在车辆达到最大转向角后，车辆将转向角保持所需持续时间。然后，该模块以相同速率将转向角减小到零。纵向控制器在整个机动过程中将车辆调节到规定速度。

使用 **稳态求解器模式** 参数指定机动的初始条件。默认情况下，该参数设置为 `Initialize from model`，仿真在指定初始位置从车辆静止开始。如果要在非零稳态速度下启动仿真：

1. 将 **稳态求解器模式** 设置为 `Solve using block parameters`。
2. 在 **稳态求解器** 选项卡上，指定初始条件、工作区变量和求解器设置。点击 **生成稳态解**。
3. 仿真完成后，将 **稳态求解器模式** 设置为 `Resume from a workspace variable`。
4. 将 **要开始于的稳态解, ssVar** 设置为您在步骤 2 中指定的工作区变量。
5. 运行仿真。
