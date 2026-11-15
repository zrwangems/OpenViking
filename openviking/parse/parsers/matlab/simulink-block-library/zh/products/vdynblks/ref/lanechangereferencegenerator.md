---
type: simulink-block
title: 'Lane Change Reference Generator'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'lanechangereferencegenerator'
documentation_source_path: 'ref/lanechangereferencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Lane Change Reference Generator

## 端口

### 输入

### **VehFdbk** — 车辆反馈 `Bus`

包含车辆反馈信号的 Bus，包括速度、加速度和方向盘扭矩。
### 输出

### **Lane** — 车道边界 `Bus`

包含左、右和横向参考车道边界的 Bus。

### **Ref** — 车辆参考信号 `Bus`

包含车辆参考信号的 Bus，包括纵向和横向位移，以及转向。

## 参数

#### 机动

### **稳态初始条件** — 从稳态开始机动 `Initialize from model`（默认） | `Solve using block parameters` | `Resume from a workspace variable`

使用 **稳态初始条件** 参数指定机动的稳态初始条件。默认情况下，仿真不会查找稳态工作点，也不会在稳态工作点启动仿真。

| 设置 | 描述 |
| --- | --- |
| `Initialize from model` | 仿真在 **机动开始时间, t\_start** 指定的仿真开始时间，以纵向速度 0 开始机动。 |
| `Solve using block parameters` | 仿真使用 **稳态求解器** 选项卡上的参数*查找*稳态工作点。 |
| `Resume from a workspace variable` | 仿真*从* **要从其开始的稳态解, ssVar** 指定的稳态工作点工作区变量开始。 |

### **要从其开始的稳态解, ssVar** — 具有稳态工作点的工作区变量 `char`

包含稳态工作点的工作区变量。

#### 依赖关系

要启用此参数，请将 **稳态求解器模式** 设置为 `Resume from a workspace variable`。

### **机动开始时间, t\_start** — 开始时间 `scalar`

机动开始时间，单位为 s。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Initialize from model`。

### **门入口的惯性纵向位置, XGate** — 位置 `175`（默认） | `scalar`

门入口的惯性纵向位置，单位为 m。

### **纵向入口速度设定值, xdot\_r** — 目标速度 `35`（默认） | `scalar`

目标速度。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Initialize from model` 或 `Solve using block parameters`。

### **纵向入口速度设定值单位, xdotUnit** — 单位 `mph`（默认）

目标速度的单位。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Initialize from model` 或 `Solve using block parameters`。

### **车辆宽度, vehW** — 车辆宽度 `2`（默认） | `scalar`

车辆宽度，单位为 m。

左和右车道边界是 **车辆宽度** 参数的函数。

### **横向偏移, latoff** — 横向偏移 `scalar`

横向偏移，单位为 m。

### **横向参考位置断点, latRefbp** — 断点 `scalar`

横向参考位置断点，单位为 m。

使用 **横向参考位置断点** 和 **横向参考数据** 参数，将横向参考轨迹指定为纵向距离的函数。

### **横向参考数据, latRef** — 横向数据 `scalar`

使用 **横向参考位置断点** 和 **横向参考数据** 参数，将横向参考轨迹指定为纵向距离的函数。

#### 依赖关系

要启用此参数，请将 **稳态初始条件** 设置为 `Initialize from model` 或 `Solve using block parameters`。

#### 稳态求解器

### **初始纵向位置, X\_o** — 初始纵向位置 `175`（默认） | `scalar`

沿大地固定 *X* 轴的初始车辆 CG 位置，单位为 m。

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

生成双车道变换机动参考信号

Lane Change Reference Generator 模块设置用于配置双车道变换机动的参数。

在车辆达到参考速度后，模块发出零加速度信号，并生成作为纵向位移函数的横向参考轨迹。该模块还生成表示左和右车道边界的信号，作为轴宽的函数。

使用 **稳态初始条件** 参数指定机动的初始条件。默认情况下，该参数设置为 `Initialize from model`，仿真从车辆在指定初始位置静止开始。如果要在非零稳态速度下启动仿真：

1. 将 **稳态初始条件** 设置为 `Solve using block parameters`。
2. 在 **稳态求解器** 选项卡上，指定初始条件、工作区变量和求解器设置。点击 **生成稳态解**。
3. 仿真完成后，将 **稳态初始条件** 设置为 `Resume from a workspace variable`。
4. 将 **要从其开始的稳态解, ssVar** 设置为在第 2 步中指定的工作区变量。
5. 运行仿真。

有关示例，请参阅“在目标速度下开始双车道变换机动”。
