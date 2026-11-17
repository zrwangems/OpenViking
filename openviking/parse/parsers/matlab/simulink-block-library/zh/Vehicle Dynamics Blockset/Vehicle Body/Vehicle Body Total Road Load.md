---
type: simulink-block
title: 'Vehicle Body Total Road Load'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'vehiclebodytotalroadload'
documentation_source_path: 'ref/vehiclebodytotalroadload.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Body Total Road Load

## 端口

### 输入

### **xdot** — 车辆纵向速度 `scalar`

车辆总纵向速度，x˙，单位为 m/s。

#### 依赖

要启用此端口，对于 **Input Mode** 参数，选择 `Kinematic`。

### **xddot** — 车辆纵向加速度 `scalar`

车辆总纵向加速度，x¨，单位为 m/s^2。

#### 依赖

要启用此端口，对于 **Input Mode** 参数，选择 `Kinematic`。

### **PwrTot** — 牵引输入功率 `scalar`

牵引输入功率，
*Ptotal*，单位为 W。

#### 依赖

要启用此端口，对于 **Input Mode** 参数，选择 `Power`。

### **ForceTot** — 牵引输入力 `scalar`

牵引输入力，
*Ftotal*，单位为 N。

#### 依赖

要启用此端口，对于 **Input Mode** 参数，选择 `Force`。

### **Grade** — 道路坡度角 `scalar`

道路坡度角，*Θ*，单位为 deg。
### 输出

### **Info** — 总线信号总线

包含这些模块计算的总线信号。

| 信号 | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | 车辆质心沿地球固定 `X` 轴的位移 | 相对于道路坡度计算。 | m |
| `Y` | 车辆质心沿地球固定 `Y` 轴的位移 | `0` | m |
| `Z` | 车辆质心沿地球固定 `Z` 轴的位移 | 相对于道路坡度计算。 | m |
| `Vel` | `Xdot` | 车辆质心沿地球固定 `X` 轴的速度 | 相对于道路坡度计算。 | m/s |
| `Ydot` | 车辆质心沿地球固定 `Y` 轴的速度 | `0` | m/s |
| `Zdot` | 车辆质心沿地球固定 `Z` 轴的速度 | 相对于道路坡度计算。 | m/s |
| `Ang` | `phi` | 车辆固定坐标系绕地球固定 `X` 轴的旋转（横滚） | `0` | rad |
| `theta` | 车辆固定坐标系绕地球固定 `Y` 轴的旋转（俯仰） | 相对于坡度角计算。 | rad |
| `psi` | 车辆固定坐标系绕地球固定 `Z` 轴的旋转（横摆） | `0` | rad |
| `BdyFrm` | `Cg` | `Disp` | `x` | 车辆质心沿车辆固定 `x` 轴的位移 | 计算得出 | m |
| `y` | 车辆质心沿车辆固定 `y` 轴的位移 | `0` | m |
| `z` | 车辆质心沿车辆固定 `z` 轴的位移 | `0` | m |
| `Vel` | `xdot` | 车辆质心沿车辆固定 `x` 轴的速度 | 计算得出 | m/s |
| `ydot` | 车辆质心沿车辆固定 `y` 轴的速度 | `0` | m/s |
| `zdot` | 车辆质心沿车辆固定 `z` 轴的速度 | `0` | m/s |
| `Acc` | `ax` | 车辆质心沿车辆固定 *x* 轴的惯性加速度 | 计算得出 | gn |
| `ay` | 车辆质心沿车辆固定 *y* 轴的惯性加速度 | `0` | gn |
| `az` | 车辆质心沿车辆固定 *z* 轴的惯性加速度 | `0` | gn |
| `xddot` | 车辆质心沿车辆固定 *x* 轴的加速度，不包括离心分量 | 计算得出 | m/s^2 |
| `yddot` | 车辆质心沿车辆固定 *y* 轴的加速度，不包括离心分量 | 计算得出 | m/s^2 |
| `zddot` | 车辆质心沿车辆固定 *z* 轴的加速度，不包括离心分量。 | `0` | m/s^2 |
| `Forces` | `Body` | `Fx` | 车辆质心沿车辆固定 `x` 轴上的净力 | 计算得出 | N |
| `Fy` | 车辆质心沿车辆固定 `y` 轴上的净力 | `0` | N |
| `Fz` | 车辆质心沿车辆固定 `z` 轴上的净力 | `0` | N |
| `Ext` | `Fx` | 车辆质心沿车辆固定 `x` 轴上的外力 | 计算得出 | N |
| `Fy` | 车辆质心沿车辆固定 `y` 轴上的外力 | `0` | N |
| `Fz` | 车辆质心沿车辆固定 `z` 轴上的外力 | `0` | N |
| `Drag` | `Fx` | 车辆质心沿车辆固定 `x` 轴上的阻力 | 计算得出 | N |
| `Fy` | 车辆质心沿车辆固定 `y` 轴上的阻力 | `0` | N |
| `Fz` | 车辆质心沿车辆固定 `z` 轴上的阻力 | `0` | N |
| `Grvty` | `Fx` | 车辆质心沿车辆固定 `x` 轴上的重力 | 计算得出 | N |
| `Fy` | 车辆质心沿车辆固定 `y` 轴上的重力 | `0` | N |
| `Fz` | 车辆质心沿车辆固定 `z` 轴上的重力 | 计算得出 | N |
| `Pwr` | `PwrExt` | | 施加的外部功率 | 计算得出 | W |
| `Drag` | | 阻力导致的功率损失 | 计算得出 | W |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | | 外部施加力的功率 | *PFxExt* | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | | 阻力功率 | *PD* | W |
| `PwrStored` | `wrStoredGrvty` | | 重力势能变化率 | *Pg* | W |
| `PwrStoredxdot` | | 纵向动能变化率 | *Pxdot* | W |

### **xdot** — 车辆纵向速度 `scalar`

车辆总纵向速度，x˙，单位为 m/s。

#### 依赖关系

要启用此端口，对于 **Input Mode** 参数，选择 `Power` 或 `Force`。

### **ForceTot** — 牵引输入力 `scalar`

牵引输入力，
*Ftotal*，单位为 N。

#### 依赖

要启用此端口，对于 **Input Mode**
参数，选择 `Kinematic`。

## 参数

### **Input Mode** — 指定输入模式 `Kinematic`（默认）| `Force` | `Power`

指定输入类型。

- `Kinematic` — 模块使用
  车辆纵向速度和加速度来计算
  牵引力和功率。将此配置用于动力总成、
  传动系统和制动系统设计，或部件
  选型。
- `Force` — 模块使用
  牵引力来计算车辆纵向
  位移和速度。将此配置用于
  系统级性能、燃油经济性或驾驶循环跟踪
  研究。
- `Power` — 模块使用
  发动机或变速器功率来计算车辆
  纵向位移和速度。将此配置
  用于系统级性能、燃油经济性或驾驶循环
  跟踪研究。

#### 依赖

此表总结了端口和输入模式配置。

| 输入模式 | 创建端口 |
| --- | --- |
| `Kinematic` | `xdot`  `xddot` |
| `Force` | `Force` |
| `Power` | `Power` |

### **Mass** — 车身质量 `1200`（默认）| `scalar`

车身质量，*m*，单位为 kg。

### **Rolling resistance coefficient, a** — 滚动 `196`（默认）| `scalar`

稳态滚动阻力系数，*a*，单位为
N。

### **Rolling and driveline resistance coefficient, b** — 滚动和传动系 `2.232`（默认）| `scalar`

粘性传动系和滚动阻力系数，
*b*，单位为 N\*s/m。

### **Aerodynamic drag coefficient, c** — 阻力 `0.389`（默认）| `scalar`

空气动力学阻力系数，*c*，单位为 N·s^2/m。

### **Gravitational acceleration, g** — 重力 `9.81`（默认）| `scalar`

重力加速度，*g*，单位为 m/s^2。

### **Initial position, x\_o** — 位置 `0`（默认）| `scalar`

车辆纵向初始位置，单位为 m。

### **Initial velocity, xdot\_o** — 速度 `0`（默认）| `scalar`

车辆相对于地面的纵向初始速度，单位为
m/s。

## 所属库

Powertrain Blockset / Vehicle Dynamics Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

使用滑行测试系数的车辆运动

Vehicle Body Total Road Load 模块使用滑行测试系数实现单
自由度 (1DOF) 刚性车辆模型。您
可以在车辆模型中使用此模块来表示传动系统和
底盘施加到变速器或发动机的负载。它适用于系统级
性能、部件选型、燃油经济性或驾驶循环跟踪研究。该模块
以最少的参数化或计算
成本计算动态动力总成负载。

您可以将该模块配置为运动学、力或总功率输入。

- Kinematic — 模块使用车辆纵向速度
  和加速度来计算牵引力和功率。
- Force — 模块使用牵引力来计算车辆
  纵向位移和速度。
- Power — 模块使用发动机或变速器功率来计算
  车辆纵向位移和速度。

### 动力学

为计算作用在车辆上的总道路载荷，该模块实现以下方程。

Froad=a+bx˙+cx˙2+mgsin(θ)

为确定系数 *a*、*b* 和 *c*，您可以使用与 *Road Load Measurement and Dynamometer Simulation Using Coastdown Techniques* 中描述的过程类似的测试过程。您还可以使用 Simulink® Design Optimization™ 将系数拟合到测量数据（参见 Estimate Vehicle Drag Coefficients by Coast-Down Testing (Simulink Design Optimization)）。

为计算车辆运动，该模块使用刚体牛顿定律。

Ftotal=mx¨+Froad

总功率输入是总力与纵向速度的乘积。道路力和重力产生的功率是道路力与纵向速度的乘积。

Ptotal=Ftotalx˙Proad=Froadx˙

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrFxExt` | 外部施加力的功率 | *PFxExt* | PFxExt=Ftotalx˙ |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFxDrag` | 阻力功率 | *PD* | Pd=−(a+bx˙+cx˙2)x˙ |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `wrStoredGrvty` | 重力势能变化率 | *Pg* | Pg=−mgZ˙ |
| `PwrStoredxdot` | 纵向动能变化率 | *Pxdot* | Px˙=mx¨x˙ |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *a* | 稳态滚动阻力系数 |
| *b* | 粘性传动系和滚动阻力系数 |
| *c* | 空气阻力系数 |
| *g* | 重力加速度 |
| *x* | 车辆相对于地面的纵向位移，在车辆固定坐标系中 |
| x˙ | 车辆相对于地面的纵向速度，在车辆固定坐标系中 |
| x¨ | 车辆相对于地面的纵向加速度，车辆固定坐标系 |
| *m* | 车体质量 |
| *Θ* | 道路坡度角 |
| *Ftotal* | 作用在车辆上的总力 |
| *Froad* | 由于损耗和重力载荷产生的阻力道路载荷 |
| *Ptotal* | 总牵引输入功率 |
| *Proad* | 由于损耗和重力载荷产生的总功率 |
| Z˙ | 车辆沿车辆固定 `z` 轴的垂直速度 |
