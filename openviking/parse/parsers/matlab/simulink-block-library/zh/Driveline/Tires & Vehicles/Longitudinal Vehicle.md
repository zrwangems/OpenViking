---
type: simulink-block
title: 'Longitudinal Vehicle'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles'
documentation_page: 'longitudinalvehicle'
documentation_source_path: 'ref/longitudinalvehicle.html'
language: zh-CN
chinese_source: worker-translation
---

# Longitudinal Vehicle

## 端口

### 输入

### **Brake** — 纵向制动力，N physical signal

与制动器关联的 physical signal 输入端口。Brake 端口会忽略负值。

#### 依赖项

要启用此端口，请将 **显示制动力输入端口** 设置为 `On`。

### **Angle** — 道路倾角，rad physical signal

与道路倾角关联的 physical signal 输入端口，单位为弧度。此值表示道路相对于水平面的角度，`0` 表示水平面，`pi/4` 表示 100% 坡度。

#### 依赖项

要启用此端口，请设置

- **显示道路坡度输入端口** 为
  `On`
- **坡度输入类型** 为
  `Incline angle`

### **NG** — 归一化道路坡度，unitless physical signal

与归一化道路坡度关联的 physical signal 输入端口。归一化道路坡度为 `1` 等效于 π/4 弧度角。

#### 依赖项

要启用此端口，请设置

- **显示道路坡度输入端口** 为
  `On`
- **坡度输入类型** 为
  `Normalized grade`

### **PG** — 百分比道路坡度，unitless physical signal

与百分比道路坡度关联的 physical signal 输入端口。百分比道路坡度为 `100` 等效于 π/4 弧度角。

#### 依赖项

要启用此端口，请设置

- **显示道路坡度输入端口** 为
  `On`
- **坡度输入类型** 为
  `Percent grade`

### **Wind** — 纵向风速，m/s physical signal

与纵向风速关联的 physical signal 输入端口。此值是风速的纵向分量，其中正值表示逆风，负值表示顺风。

#### 依赖项

要启用此端口，请将 **显示风速输入端口** 设置为 `On`。

### 输出

### **VehSpd** — 车辆速度，m/s physical signal

与车辆纵向速度关联的 physical signal 输出端口。

### **G** — 纵向 G 力，unitless physical signal

与纵向车辆加速度 *ax* 与重力加速度 *g* 之比关联的 physical signal 端口。

#### 依赖项

要启用此端口，请将 **显示 G 输出端口** 设置为 `On`。

### 守恒

### **Axle** — 车轮旋转 mechanical rotational

与车轴到轮毂连接关联的 mechanical rotational 守恒端口。将此端口连接到齿轮系统，例如减速齿轮。

## 参数

### 车辆

### **参数化类型** — 车辆参数化选择 `Regular parameter set`（默认）| `Road-load` | `Typical small car` | `Typical medium-sized car` | `Typical large sports utility vehicle`

用于参数化纵向车辆的选项。您可以通过选择 `Regular parameter set` 或 `Road-load` 来参数化任意车辆，也可以选择三种典型车身规格之一。有关详细信息，请参阅参数化。

### **车辆质量** — 惯性质量 `1200` `kg`（默认）| positive scalar

纵向车辆的有效质量。

#### 依赖项

要启用此参数，请将 **参数化类型** 设置为 `Regular parameter set` 或 `Road-load`。

### **轮胎滚动半径** — 轮胎滚动半径 `0.3` `m`（默认）| positive scalar

在抵抗车辆重力作用时，从车轮中心到轮胎外表面的距离。

#### 依赖项

要启用此参数，请将 **参数化类型** 设置为 `Regular parameter set` 或 `Road-load`。

### **轮胎滚动系数** — 轮胎滚动系数 `0.0136`（默认）| nonnegative scalar

轮胎滚动阻力的无量纲系数。模块使用此值按 *Ftire = CRmg* 计算 *Ftire*。这里，变量 *CR* 表示此参数。

#### 依赖项

要启用此参数，请将 **参数化类型** 设置为 `Regular parameter set`。

### **空气阻力系数** — 车辆阻力系数 `0.31`（默认）| nonnegative scalar

车辆阻力的无量纲系数。模块使用此值按 *Fair = 1/2·CDAfρ(vx+vw)2* 计算 *Fair*，其中 *CD* 表示此参数。

#### 依赖项

要启用此参数，请将 **参数化类型** 设置为 `Regular parameter set`。

### **车辆迎风面积** — 迎风表面积 `2.3` `m^2`（默认）| positive scalar

车辆受阻力作用的有效面积。在早期设计中，可以使用低保真启发式公式确定此度量：*Af = 0.9·height·width*。

#### 依赖项

要启用此参数，请将 **参数化类型** 设置为 `Regular parameter set`。

### **道路载荷系数 A** — ARL 系数 `120` `N`（默认）| positive scalar

道路载荷系数 *ARL*。

#### 依赖项

要启用此参数，请将 **参数化类型** 设置为 `Road-load`。

### **道路载荷系数 B** — BRL 系数 `1.8` `N/(m/s)`（默认）| positive scalar

道路载荷系数 *BRL*。

#### 依赖项

要启用此参数，请将 **参数化类型** 设置为 `Road-load`。

### **道路载荷系数 C** — CRL 系数 `0.389` `N*s^2/m^2`（默认）| positive scalar

道路载荷系数 *CRL*。

#### 依赖项

要启用此参数，请将 **参数化类型** 设置为 `Road-load`。

### **重力加速度** — 重力加速度 `9.81` `m/s^2`（默认）| positive scalar

作用于车辆质量的重力常数，作为车轴旋转的函数。这里，车辆重量 *=* 车辆质量*·*重力加速度。模块将此重量施加到轮胎以计算滚动阻力。当将 **显示 G 输出端口** 设置为 `On` 时，模块还使用此值确定 G-force 倍数。

### 仿真

### **车辆速度阈值** — 车辆运动的容差 `0.3` `m/s`（默认）| scalar

模块仿真车辆运动的最低速度。低于此阈值的绝对值时，模块平滑过渡到零。

### **车轴速度阈值** — 车轴旋转的容差 `0.01` `rad/s`（默认）| scalar

模块仿真车轴旋转的最低转速。低于此阈值的绝对值时，模块平滑过渡到零。

### **显示制动力输入端口** — 理想制动器端口 `On`（默认）| `Off`

用于显示 **Brake** 端口的选项。

### **显示道路坡度输入端口** — 道路坡度端口 `On`（默认）| `Off`

用于启用端口以输入与道路坡度或斜坡相关数据的选项。将此参数设置为 `On` 会启用 **坡度输入类型** 参数。

### **坡度输入类型** — 坡度测量类型 `Percent grade`（默认）| `Normalized grade` | `Incline angle`

用于输入道路坡度的选项。这些选项使用以下定义：

- `Percent grade` — 模块使用百分比坡度标度，其中 `0` 为平坦，`100` 等效于斜率为 π/4。
- `Normalized grade` — 模块使用归一化坡度标度，其中 `0` 为平坦，`1` 等效于斜率为 π/4。
- `Incline angle` — 模块使用倾角，其中 `0` 为平坦，`pi/4` 等效于斜率为 π/4。

#### 依赖项

要启用此参数，请将 **显示道路坡度输入端口** 设置为 `On`。

### **显示风速输入端口** — 风端口 `On`（默认）| `Off`

用于显示 **Wind** 端口的选项。

### **显示 G 输出端口** — G-force 输出端口 `Off`（默认）| `On`

用于显示 **G** 端口的选项。将 G-force 记录为 **重力加速度** 参数的倍数。

## 所属库

Simscape / Driveline / Tires & Vehicles

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2022b：选择坡度输入类型

您可以使用 **坡度输入类型** 根据以下参数来参数化道路坡度：

- `Percent grade`
- `Normalized grade`
- `Incline angle`

### R2022b：查看道路载荷力可视化

您可以通过单击源代码中的 **车辆属性** 超链接来访问车辆属性的可视化。

## 描述

具有理想制动器和轮胎的纵向运动抽象车辆

Longitudinal Vehicle 模块表示限于纵向运动的抽象车辆。您可以参数化任意车辆，或从预定义参数化中选择。该模块包含可选的非滑移轮胎和理想制动器。

您可以将此模块用作 Vehicle Body 模块的更简单替代方案。Longitudinal Vehicle 模块参数化所需的信息更少，更适合早期设计。您可以使用 Longitudinal Vehicle Performance Design App 应用为该模块设计性能规格。

模块方程使用以下变量：

- *m* 是 **车辆质量** 参数。
- *vx* 是 **VehSpd** 端口处的纵向速度输出。
- *Fx* 是纵向力之和。
- *rtire* 是轮胎半径，等效于 **轮胎滚动半径** 参数。
- *Fdrive*、*Fbrake* 和 *Fresist* 分别是车辆的驱动力、制动力和车辆阻力。在力平衡方程中，*Fbrake* 和 *Fresist* 与车辆的驱动运动相反。
- *τaxle* 是车轴处的转矩。
- *FB* 是来自 **Brake** 端口的制动力输入。
- *ωaxle* 是车轴的转速。
- *ω1* 是任意常数，用于调整模块抑制 *Fbrake* 的速度范围。
- *Ftire* 是轮胎滚动阻力。
- *Fair* 是由空气阻力引起的阻力。
- *θ* 是来自 **Angle**、**NG** 或 **PG** 端口的道路倾角输入。
- *v1* 是任意常数，用于调整模块抑制 *Fair* 和 *Ftire* 的速度范围。

您可以通过单击源代码中的 **车辆属性** 超链接来访问车辆属性的可视化。该图显示默认模块属性，其中第一个图是不同道路坡度下阻力随车辆速度变化的函数，第二个图是不同道路坡度下给定速度的阻力功率。

默认属性子图，其中上方子图显示给定车辆速度下的阻力随道路坡度增大而增大，下方子图显示给定速度下的阻力功率随道路坡度增大而增大。

### 参数化

对于 **参数化类型** 参数的所有设置，模块按如下方式计算纵向车速方程：

mdvxdt=∑Fx,

其中

vx=rtireωaxle,

以及

∑Fx=Fdrive−Fbrake−Fresist.

该模块在力平衡方程中将驱动方向视为正方向。它使用以下代换求解此方程：

∑Fx=τaxlertire︸Fdrive−FBtanh(ωaxleω1)︸Fbrake−{(Ftirecosθ+Fair)tanh(vxv1)+mgsinθ}.︸Fresist

您可以将 **参数化类型** 设置为 `Road-load` 或 `Regular parameter set` 来仿真任意车辆。您还可以从三种预定义参数化中选择：`Typical small car`、`Typical medium-sized car` 和 `Typical large sports utility vehicle`。

**Regular parameter set**

当将 **参数化类型** 设置为 `Regular parameter set` 时，您可以指定车辆的 **轮胎滚动系数**、**空气阻力系数** 和 **车辆迎风面积** 参数，模块会将其转换为道路载荷系数。

模块按如下方式计算轮胎滚动阻力：

Ftire=CRmg,

其中 *CR* 是 **轮胎滚动系数** 参数。

模块按如下方式计算空气阻力：

Fair=12CDAfρa(vx+vw)2,

其中 *CD* 是 **空气阻力系数** 参数，*Af* 是 **车辆迎风面积** 参数，单位为 *m2*，*ρA* 是干空气密度。模块假设在 1 个大气压下 *ρA = 1.184 kg/m3*。

**Road-load**

当将 **参数化类型** 设置为 `Road-load` 时，模块应用标准道路载荷公式，并按如下方式计算核心物理量：

FRL=ARL+BRLvx︸Ftire+CRLvx2︸Fair,

其中 *ARL*、*BRL* 和 *CRL* 是道路载荷系数。

**注意**

每个道路载荷系数都特定于其关联的 *vx* 单位。这些系数没有标准单位；但是，某些文献可能会假设特定单位。在参数化这些系数时，请选择正确的单位。

模块使用这些系数按如下方式求解核心物理量中的值：

Ftire=ARL+BRLvx,

以及

Fair=CRL(vx+vw)2.

其中，*vw* 是来自 **Wind** 端口的风速。

**预定义参数化**

您可以将 **参数化类型** 设置为三种预定义参数化：`Typical small car`、`Typical medium-sized car` 和 `Typical large sports utility vehicle`。这些值表示行业平均值，而不是特定车辆。您可以从这些预定义参数化之一开始，稍后通过将 **参数化类型** 设置为 `Road-load` 或 `Regular parameter set` 并使用表中的相关信息来调整这些值。

**`Regular parameter set`**

| **参数化类型** | **车辆质量** | **轮胎滚动半径** | **轮胎滚动系数** | **阻力系数** | **迎风面积** |
| --- | --- | --- | --- | --- | --- |
| `Typical small car` | `1100` `kg` | `0.3` `m` | `0.013` | `0.3` | 0.9\*1.65\*1.45 = `2.153` `m^2` |
| `Typical medium-sized car` | `1800` `kg` | `0.3` `m` | `0.0136` | `0.31` | 0.9\*1.75\*1.5 = `2.36` `m^2` |
| `Typical large sports utility vehicle` | `2600` `kg` | `0.4` `m` | `0.014` | `0.36` | 0.9\*1.88\*1.85 = `3.13` `m^2` |

请注意，每个预定义参数化都假设道路载荷方法中的 *B = 0*。

**`Road-load`**

| **参数化类型** | **A** | **B** | **C** |
| --- | --- | --- | --- |
| `Typical small car` | `140.3` `N` | `0` `N/(m/s)` | `0.3824` `N*s^2/m^2` |
| `Typical medium-sized car` | `240.1` `N` | `0` `N/(m/s)` | `0.4336` `N*s^2/m^2` |
| `Typical large sports utility vehicle` | `357.1` `N` | `0` `N/(m/s)` | `0.6671` `N*s^2/m^2` |

其中 **车辆迎风面积** 方程对应于 *0.9·*vehicle width*·*vehicle height。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅“修改模块变量的标称值”。
