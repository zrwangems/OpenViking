---
type: simulink-block
title: 'Vehicle Body 1DOF Longitudinal'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'vehiclebody1doflongitudinal'
documentation_source_path: 'ref/vehiclebody1doflongitudinal.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Body 1DOF Longitudinal

## 端口

### 输入

### **FExt** — 车辆质心处的外部力 `array`

施加在车辆质心处的外部力，
*Fxext*、
*Fyext*、
*Fzext*，在
车辆固定坐标系下，单位为 N。信号向量维度为
`[1x3]` 或 `[3x1]`。

#### 依赖

要启用此端口，请选择 **External
forces**。

### **MExt** — 绕车辆质心的外部力矩 `array`

绕车辆质心的外部力矩，
*Mx*、
*My*、
*Mz*，在
车辆固定坐标系下，单位为 N·m。信号向量维度为
`[1x3]` 或 `[3x1]`。

#### 依赖

要启用此端口，请选择 **External
moments**。

### **FwF** — 前轴上的总纵向力 `scalar`

前轴上的纵向力，
*Fxf*，沿
车辆固定 `x` 轴方向，单位为 N。

### **FwR** — 后轴上的总纵向力 `scalar`

后轴上的纵向力，
*FwR*，沿
车辆固定 `x` 轴方向，单位为 N。

### **Grade** — 道路坡度角 `scalar`

道路坡度角，γ，单位为 deg。

### **WindX** — 纵向风速 `scalar`

纵向风速，*Ww*，
沿地面固定 `X` 轴方向，单位为 m/s。

#### 依赖

要启用此端口，请清除 **Wind X,Y,Z
components**。

### **WindXYZ** — 风速 `array`

风速，*Ww*、
*WwY*、
*WwZ*，沿惯性
*X*、*Y* 和
*Z* 轴方向，单位为 m/s。信号向量维度为
`[1x3]` 或 `[3x1]`。

#### 依赖

要启用此端口，请选择 **Wind X,Y,Z
components**。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，
*Tair*，单位为 K。如果您希望在运行时改变温度，请考虑此选项。

#### 依赖

要启用此端口，请选择 **Air
temperature**。
### 输出

### **Info** — 总线信号总线

包含这些模块值的总线信号。

| 信号 | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | 车辆质心沿大地固定 `X` 轴的位移 | 相对于道路坡度计算。 | m |
| `Y` | | 车辆质心沿大地固定 `Y` 轴的位移 | `0` | m |
| `Z` | | 车辆质心沿大地固定 `Z` 轴的位移 | 相对于道路坡度计算。 | m |
| `Vel` | `Xdot` | | 车辆质心沿大地固定 `X` 轴的速度 | 相对于道路坡度计算。 | m/s |
| `Ydot` | | 车辆质心沿大地固定 `Y` 轴的速度 | `0` | m/s |
| `Zdot` | | 车辆质心沿大地固定 `Z` 轴的速度 | 相对于道路坡度计算。 | m/s |
| `Ang` | `phi` | | 车辆固定坐标系绕大地固定 `X` 轴的旋转（横滚） | `0` | rad |
| `theta` | | 车辆固定坐标系绕大地固定 `Y` 轴的旋转（俯仰） | 相对于坡度角计算。 | rad |
| `psi` | | 车辆固定坐标系绕大地固定 `Z` 轴的旋转（横摆） | `0` | rad |
| `FrntAxl` | `Disp` | `X` | | 前轴沿大地固定 `X` 轴的位移 | 计算值 | m |
| `Y` | | 前轴沿大地固定 `Y` 轴的位移 | `0` | m |
| `Z` | | 前轴沿大地固定 `Z` 轴的位移 | 计算值 | m |
| `Vel` | `Xdot` | | 前轴沿大地固定 `X` 轴的速度 | 计算值 | m/s |
| `Ydot` | | 前轴沿大地固定 `Y` 轴的速度 | `0` | m/s |
| `Zdot` | | 前轴沿大地固定 `Z` 轴的速度 | 计算值 | m/s |
| `RearAxl` | `Disp` | `X` | | 后轴沿大地固定 `X` 轴的位移 | 计算值 | m |
| `Y` | | 后轴沿大地固定 `Y` 轴的位移 | `0` | m |
| `Z` | | 后轴沿大地固定 `Z` 轴的位移 | 计算值 | m |
| `Vel` | `Xdot` | | 后轴沿大地固定 `X` 轴的速度 | 计算值 | m/s |
| `Ydot` | | 后轴沿大地固定 `Y` 轴的速度 | `0` | m/s |
| `Zdot` | | 后轴沿大地固定 `Z` 轴的速度 | 计算值 | m/s |
| `BdyFrm` | `Cg` | `Disp` | `x` | | 车辆质心沿车辆固定 `x` 轴的位移 | 计算值 | m |
| `y` | | 车辆质心沿车辆固定 `y` 轴的位移 | `0` | m |
| `z` | | 车辆质心沿车辆固定 `z` 轴的位移 | `0` | m |
| `Vel` | `xdot` | | 车辆质心沿车辆固定 `x` 轴的速度 | 计算值 | m/s |
| `ydot` | | 车辆质心沿车辆固定 `y` 轴的速度 | `0` | m/s |
| `zdot` | | 车辆质心沿车辆固定 `z` 轴的速度 | `0` | m/s |
| `AngVel` | `p` | | 车辆绕车辆固定 `x` 轴的角速度（横滚角速率） | `0` | rad/s |
| `q` | | 车辆绕车辆固定 y 轴的角速度（俯仰角速率） | `0` | rad/s |
| `r` | | 车辆绕车辆固定 z 轴的角速度（横摆角速率） | `0` | rad/s |
| `Accel` | `ax` | | 车辆质心沿车辆固定 *x* 轴的惯性加速度 | 计算值 | gn |
| `ay` | | 车辆质心沿车辆固定 *y* 轴的惯性加速度 | `0` | gn |
| `az` | | 车辆质心沿车辆固定 *z* 轴的惯性加速度 | `0` | gn |
| `xddot` | | 车辆质心沿车辆固定 *x* 轴的加速度，不包括离心分量 | 计算值 | m/s^2 |
| `yddot` | | 车辆质心沿车辆固定 *y* 轴的加速度，不包括离心分量 | 计算值 | m/s^2 |
| `zddot` | | 车辆质心沿车辆固定 *z* 轴的加速度，不包括离心分量。 | `0` | m/s^2 |
| `Forces` | `Body` | `Fx` | | 车辆质心沿车辆固定 `x` 轴上的净力 | `0` | N |
| `Fy` | | 车辆质心沿车辆固定 `y` 轴上的净力 | `0` | N |
| `Fz` | | 车辆质心沿车辆固定 `z` 轴上的净力 | `0` | N |
| `Ext` | `Fx` | | 车辆质心沿车辆固定 `x` 轴上的外力 | `Computed` | N |
| `Fy` | | 车辆质心沿车辆固定 `y` 轴上的外力 | `Computed` | N |
| `Fz` | | 车辆质心沿车辆固定 `z` 轴上的外力 | `Computed` | N |
| `FrntAxl` | `Fx` | | 前轴上的纵向力，沿车辆固定 `x` 轴 | `0` | N |
| `Fy` | | 前轴上的侧向力，沿车辆固定 `y` 轴 | `0` | N |
| `Fz` | | 前轴上的法向力，沿车辆固定 `z` 轴 | 计算值 | N |
| `RearAxl` | `Fx` | | 后轴上的纵向力，沿车辆固定 `x` 轴 | `0` | N |
| `Fy` | | 后轴上的侧向力，沿车辆固定 `y` 轴 | `0` | N |
| `Fz` | | 后轴上的法向力，沿车辆固定 `z` 轴 | 计算值 | N |
| `Tires` | `FrntTire` | `Fx` | 前轮胎力，沿车辆固定 `x` 轴 | `0` | N |
| `Fy` | 前轮胎力，沿车辆固定 `y` 轴 | `0` | N |
| `Fz` | 前轮胎力，沿车辆固定 `z` 轴 | 计算值 | N |
| `RearTire` | `Fx` | 后轮胎力，沿车辆固定 `x` 轴 | `0` | N |
| `Fy` | 后轮胎力，沿车辆固定 `y` 轴 | `0` | N |
| `Fz` | 后轮胎力，沿车辆固定 `z` 轴 | 计算值 | N |
| `Drag` | `Fx` | | 车辆质心沿车辆固定 `x` 轴上的阻力 | 计算值 | N |
| `Fy` | | 车辆质心沿车辆固定 `y` 轴上的阻力 | 计算值 | N |
| `Fz` | | 车辆质心沿车辆固定 `z` 轴上的阻力 | 计算值 | N |
| `Grvty` | `Fx` | | 车辆质心沿车辆固定 `x` 轴上的重力 | 计算值 | N |
| `Fy` | | 车辆质心沿车辆固定 `y` 轴上的重力 | `0` | N |
| `Fz` | | 车辆质心沿车辆固定 `z` 轴上的重力 | 计算值 | N |
| `Moments` | `Body` | `Mx` | | 车辆质心绕车辆固定 `x` 轴上的净力矩 | `0` | N·m |
| `My` | | 车辆质心绕车辆固定 `y` 轴上的净力矩 | `0` | N·m |
| `Mz` | | 车辆质心绕车辆固定 `z` 轴上的净力矩 | `0` | N·m |
| `Drag` | `Mx` | | 车辆质心绕车辆固定 `x` 轴上的阻力矩 | 计算值 | N·m |
| `My` | | 车辆质心绕车辆固定 `y` 轴上的阻力矩 | 计算值 | N·m |
| `Mz` | | 车辆质心绕车辆固定 `z` 轴上的阻力矩 | 计算值 | N·m |
| `Ext` | `Fx` | | 车辆质心绕车辆固定 `x` 轴上的外力矩 | `Computed` | N·m |
| `Fy` | | 车辆质心绕车辆固定 `y` 轴上的外力矩 | `Computed` | N·m |
| `Fz` | | 车辆质心绕车辆固定 `z` 轴上的外力矩 | `Computed` | N·m |
| `FrntAxl` | `Disp` | `x` | | 前轴沿车辆固定 `x` 轴的位移 | 计算值 | m |
| `y` | | 前轴沿车辆固定 `y` 轴的位移 | `0` | m |
| `z` | | 前轴沿车辆固定 `z` 轴的位移 | 计算值 | m |
| `Vel` | `xdot` | | 前轴沿车辆固定 `x` 轴的速度 | 计算值 | m/s |
| `ydot` | | 前轴沿车辆固定 `y` 轴的速度 | `0` | m/s |
| `zdot` | | 前轴沿车辆固定 `z` 轴的速度 | 计算值 | m/s |
| `Steer` | `WhlAngFL` | | 前左车轮转向角 | 计算值 | rad |
| `WhlAngFR` | | 前右车轮转向角 | 计算值 | rad |
| `RearAxl` | `Disp` | `x` | | 后轴沿车辆固定 `x` 轴的位移 | 计算值 | m |
| `y` | | 后轴沿车辆固定 `y` 轴的位移 | `0` | m |
| `z` | | 后轴沿车辆固定 `z` 轴的位移 | 计算值 | m |
| `Vel` | `xdot` | | 后轴沿车辆固定 `x` 轴的速度 | 计算值 | m/s |
| `ydot` | | 后轴沿车辆固定 `y` 轴的速度 | `0` | m/s |
| `zdot` | | 后轴沿车辆固定 `z` 轴的速度 | 计算值 | m/s |
| `Steer` | `WhlAngRL` | | 后左车轮转向角 | 计算值 | rad |
| `WhlAngRR` | | 后右车轮转向角 | 计算值 | rad |
| `Pwr` | `PwrExt` | | | 施加的外部功率 | 计算值 | W |
| `Drag` | | | 阻力导致的功率损失 | 计算值 | W |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | | | 外部施加力的功率 | 计算值 | W |
| `PwrFwFx` | | | 施加在前轴上的纵向力功率 | 计算值 | W |
| `PwrFwRx` | | | 施加在后轴上的纵向力功率 | 计算值 | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | | | 阻力功率 | 计算值 | W |
| `PwrStored` | `wrStoredGrvty` | | | 重力势能变化率 | 计算值 | W |
| `PwrStoredxdot` | | | 纵向动能变化率 | 计算值 | W |

### **xdot** — 车身纵向速度 `scalar`

车身沿车辆固定参考坐标系 `x` 轴的纵向速度，单位为 m/s。

### **FzF** — 前轮法向力 `scalar`

前轮单个车轮沿车辆固定 `z` 轴的法向力 *Fzf*，单位为 N。

### **FzR** — 后轮法向力 `scalar`

后轮单个车轮沿车辆固定 `z` 轴的法向力 *Fzr*，单位为 N。

## 参数

#### 选项

### **External forces** — `FExt` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `FExt`。

### **External moments** — `MExt` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `MExt`。

### **Air temperature** — `AirTemp` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `AirTemp`。

### **Wind X,Y,Z components** — `WindXYZ` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `WindXYZ`。

#### 纵向

### **Number of wheels on front axle, NF** — 前轮数量 `2`（默认）| `scalar`

前轴上的车轮数量 *NF*。该值无量纲。

### **Number of wheels on rear axle, NR** — 后轮数量 `2`（默认）| `scalar`

后轴上的车轮数量 *NR*。该值无量纲。

### **Mass, m** — 车辆质量 `1500`（默认）| `scalar`

车辆质量 *M*，单位为 kg。

### **Horizontal distance from CG to front axle, a** — 前轴距离 `1.4`（默认）| `scalar`

从车辆质心到前轮轴的水平距离 *a*，单位为 m。

### **Horizontal distance from CG to rear axle, b** — 后轴距离 `1.8`（默认）| `scalar`

从车辆质心到后轮轴的水平距离 *b*，单位为 m。

### **CG height above axles, h** — 高度 `.35`（默认）| `scalar`

车辆质心距地面的高度 *h*，单位为 m。

### **Longitudinal drag coefficient, Cd** — 阻力 `.3`（默认）| `scalar`

空气阻力系数 *Cd*。该值无量纲。

### **Longitudinal lift coefficient, Cl** — 升力 `0`（默认）| `scalar`

空气升力系数 *Cl*。该值无量纲。

### **Longitudinal drag pitch moment, Cpm** — 俯仰阻力矩 `0`（默认）| `scalar`

俯仰阻力矩系数 *Cpm*。该值无量纲。

### **Frontal area, Af** — 面积 `4`（默认）| `scalar`

用于计算车辆气动阻力的有效车辆横截面积 *A*，单位为 m2。

### **Initial position, x\_o** — 位置 `0`（默认）| `scalar`

车身沿车辆固定 `x` 轴的纵向初始位置 *xo*，单位为 m。

### **Initial velocity, xdot\_o** — 速度 `0`（默认）| `scalar`

车身沿车辆固定 `x` 轴的纵向初始速度 x˙0，单位为 m/s。

#### 环境

### **Absolute air pressure, Pabs** — 压力 `101325`（默认）| `scalar`

环境空气绝对压力 *Pabs*，单位为 Pa。

### **Air temperature, T** — 环境空气温度 `273`（默认）| `scalar`

环境空气温度 *Tair*，单位为 K。

#### 依赖关系

要启用此参数，请清除 **Air temperature**。

### **Gravitational acceleration, g** — 重力 `9.81`（默认）| `scalar`

重力加速度 *g*，单位为 m/s2。

## 所属库

Powertrain Blockset / Vehicle Dynamics Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

前进和倒车运动中的双轴车辆

Vehicle Body 1DOF Longitudinal 模块实现了一个具有恒定质量、进行纵向（即前进和倒车）运动的单自由度（1DOF）刚性车身。使用该模块：

- 在动力总成和燃油经济性研究中，当来自垂向和俯仰运动的重量转移可忽略时，用于表示车辆惯性和阻力载荷。
- 用于确定车辆跟随指定行驶循环所需的发动机扭矩和功率。

您可以选择模块选项来创建外部力、力矩、空气温度和风速的输入端口。

| 模块选项设置 | **外部输入端口** | 描述 |
| --- | --- | --- |
| **外部力** | `FExt` | 施加在车辆固定坐标系中车辆质心上的外部力。 |
| **外部力矩** | `MExt` | 车辆固定坐标系中绕车辆质心的外部力矩。 |
| **空气温度** | `AirTemp` | 环境空气温度。如果您希望在运行时改变温度，请考虑此选项。 |
| **风速 X,Y,Z** | `WindXYZ` | 沿地面固定 *X*、*Y* 和 *Z* 轴的风速。如果您不选择此选项，模块将实现输入端口 `WindX` —— 沿地面固定 *X* 轴的纵向风速。 |

### 车身模型

车辆车轴平行并形成一个平面。纵向方向位于该平面内且垂直于车轴。如果车辆在倾斜坡道上行驶，法线方向不平行于重力，但始终垂直于车轴-纵向平面。

该模块利用作用在其上的所有力和力矩的净效应来确定车辆运动。纵向轮胎力推动车辆前进或后退。车辆重量通过其重心（CG）作用。坡度角改变了作用在车辆质心上的分解重力方向。类似地，该模块分解作用在车辆质心上的阻力空气动力阻力。

车辆自由体受力图，显示作用在质心和轮胎上的力

Vehicle Body 1DOF Longitudinal 模块实现以下方程。

Fb=mx¨Fb=FxF+FxR−Fd,x+Fext,x−mgsinγ

零法向加速度和零俯仰力矩确定前轴和后轴上的法向力。

FzF=−Mext,y−Md,y+  b(Fd,z+Fext,z+ mgcosγ)−h(−Fext,x+Fd,x+ mgsinγ+mx¨)NF(a+b) FzR=Mext,y+Md,y+ a(Fd,z+Fext,z+ mgcosγ)+h(−Fext,x+Fd,x+ mgsinγ+mx¨)NR(a+b)

车轮法向力满足以下方程。

NFFzF+NRFzR−Fext,z=mgcosγ

### 风力和阻力

该模块从车辆速度分量中减去风速，以获得净相对空速。为了计算作用在车辆上的阻力和力矩，该模块使用净相对空速。

Fd,x=12TRCdAfPabs(x˙−wx)2Fd,z=12TRClAfPabs(x˙−wx)2Md,y=12TRCpmAfPabs(x˙−wx)2(a+b)

默认情况下，为了计算沿车辆固定 *x* 轴的风速，该模块使用沿地面固定 *X* 轴的纵向风速。如果您选择 **WindX,Y,Z**，该模块将使用沿地面固定 *X*、*Y*、*Z* 轴的风速。

### Power Accounting

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrFxExt` | 外部施加力的功率 | PFxExt=FxExtx˙ |
| `PwrFwFx` | 施加在前轴上的纵向力功率 | PFwFx=FwFx˙ |
| `PwrFwRx` | 施加在后轴上的纵向力功率 | PFwRx=FwRx˙ |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFxDrag` | 阻力功率 | Pd=−0.5CdAfPabs(x˙2−wx)2287.058Tx˙ |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `wrStoredGrvty` | 重力势能的变化率 | Pg=−mgZ˙ |
| `PwrStoredxdot` | 纵向动能的变化率 | Px˙=mx¨x˙ |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Fxf*、*Fxr* | 分别作用在前、后接地点的每个车轮上的纵向力 |
| *Fzf*、*Fzr* | 分别作用在前、后接地点的每个车轮上的法向载荷力 |
| *FwF*、*FwR* | 沿车辆固定 *x* 轴作用在前、后轴上的纵向力 |
| *FxExt*、*FwR* | 沿车辆固定 *x* 轴的外部力 |
| *Fd,x*、*Fd,z* | 作用在车辆 CG 上的纵向和法向阻力 |
| *Md,y* | 阻力对车辆绕车辆固定 *y* 轴产生的扭矩 |
| *Fd* | 空气阻力 |
| *Vx* | 车辆速度。当 *Vx* > 0 时，车辆向前运动。当 *Vx* < 0 时，车辆向后运动。 |
| *Nf*、*Nr* | 前轴和后轴上的车轮数量 |
| γ | 道路坡度角 |
| *m* | 车身质量 |
| *a*、*b* | 前轴和后轴分别距车辆 CG 在公共轴平面上的法向投影点的距离 |
| *h* | 车辆 CG 高于轴平面的高度 |
| *Cd* | 正面空气阻力系数 |
| *Af* | 正面面积 |
| *Pabs* | 绝对压力 |
| *ρ* | 空气质量密度 |
| *x*、x˙、x¨ | 车辆沿车辆固定 *x* 轴的纵向位置、速度和加速度 |
| *wx* | 沿车辆固定 *x* 轴的风速 |
| Z˙ | 车辆沿车辆固定 *z* 轴的垂直速度 |
