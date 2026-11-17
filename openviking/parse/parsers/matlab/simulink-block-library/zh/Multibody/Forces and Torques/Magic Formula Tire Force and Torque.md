---
type: simulink-block
title: 'Magic Formula Tire Force and Torque'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'magicformulatireforceandtorque'
documentation_source_path: 'ref/magicformulatireforceandtorque.html'
language: zh-CN
chinese_source: worker-translation
---

# Magic Formula Tire Force and Torque

## 端口

### 几何

### **B** — 基础几何 geometry

表示轮胎所接触表面的基础几何。接触表面可以相对于世界坐标系移动或固定。必须将此端口连接至 Infinite Plane 或 Grid Surface 模块。
### 坐标系

### **F** — 从动坐标系 frame

表示轮胎的从动坐标系。该坐标系原点位于轮胎中心。
### 输入

### **lmux** — 纵向摩擦系数缩放因子，无量纲物理信号

物理信号端口，接受轮胎纵向摩擦系数的缩放因子。

#### 依赖关系

要启用此端口，请在 **Scaling Coefficients** 下，将 **LMUX** 设置为 `Provided by Input`。

### **lmuy** — 横向摩擦系数缩放因子，无量纲物理信号

物理信号端口，接受轮胎横向摩擦系数的缩放因子。

#### 依赖关系

要启用此端口，请在 **Scaling Coefficients** 下，将 **LMUY** 设置为 `Provided by Input`。
### 输出

### **con** — 接触信号，无量纲物理信号

物理信号输出端口，提供用于确定轮胎与接触表面是否有效接触的信号。当它们接触且接触有效时，信号等于 `1`，否则信号等于 `0`。

如果从动坐标系位于接触表面下方，则轮胎与表面为无效接触，模块不会向轮胎施加力和力矩。

#### 依赖关系

要启用此端口，请在 **Sensing** 下，选择 **Contact Signal**。

#### 力/力矩

### **ft** — 轮胎力，*N* 物理信号

物理信号输出端口，提供施加到模块接触坐标系的 magic formula 轮胎力。输出包含三部分：

- Fx 是在接触点处与接触表面相切的纵向力。
- Fy 是与由 Fx 和 Fz 定义的平面正交的横向力。
- Fz 是在接触点处与接触表面垂直的法向力。

如果将 **Resolution Frame** 参数设置为 `Follower`，模块将在轮胎的从动坐标系中解析该力。

#### 依赖关系

要启用此端口，请在 **Sensing > Force/Torque** 下，选择 **Tire Force**。

### **tt** — 轮胎力矩，*N\*m* 物理信号

物理信号输出端口，提供施加到模块接触坐标系的 magic formula 轮胎力矩。输出包含三部分：

- Mx 是翻转力矩。
- My 是滚动阻力矩。
- Mz 是回正力矩。

如果将 **Resolution Frame** 参数设置为 `Follower`，模块将在轮胎的从动坐标系中解析该力矩。

#### 依赖关系

要启用此端口，请在 **Sensing > Force/Torque** 下，选择 **Tire Torque**。

### **t** — 气胎拖距，*m* 物理信号

物理信号输出端口，提供从接触点到合成横向力作用点的距离。该值具有长度单位。

可以使用气胎拖距来计算回正力矩 *M*z。

#### 依赖关系

要启用此端口，请在 **Sensing > Force/Torque** 下，选择 **Pneumatic Trail**。

#### 滑移

### **kappa** — 纵向滑移，无量纲物理信号

物理信号输出端口，提供纵向滑移速度与轮胎纵向速度之比。

#### 依赖关系

要启用此端口，请在 **Sensing > Slip** 下，选择 **Longitudinal Slip**。

### **kappas** — 饱和纵向滑移，无量纲物理信号

物理信号输出端口，提供始终饱和在 KPUMIN 和 KPUMAX 参数所定义限值内的纵向滑移。

#### 依赖关系

要启用此端口，请在 **Sensing > Slip** 下，选择 **Saturated Longitudinal Slip**。

### **alpha** — 侧偏角，*rad* 物理信号

物理信号输出端口，提供由侧向滑移速度 *V*sy 和纵向速度 *V*x 构成的直角三角形的角度。该值的单位为角度。

侧偏角示意图

#### 依赖关系

要启用此端口，请在 **Sensing > Slip** 下选择 **Slip Angle**。

### **alphas** — 饱和侧偏角，*rad* 物理信号

物理信号输出端口，提供始终限制在 ALPMIN 和 ALPMAX 参数所定义范围内的饱和侧偏角。该值的单位为角度。

#### 依赖关系

要启用此端口，请在 **Sensing > Slip** 下选择 **Saturated Slip Angle**。

### **phit** — 转向滑移，*rad/m* 物理信号

物理信号输出端口，提供轮胎横摆角速度与接触坐标系 *xy* 平面内轮胎速度大小之比。该值的单位为角度/长度。

转向滑移在建模低速转弯（如泊车操作）时非常有用。

#### 依赖关系

要启用此端口，请在 **Sensing > Slip** 下选择 **Turn Slip**。

#### 线速度

### **vx** — 相对纵向速度，*m/s* 物理信号

物理信号输出端口，提供从动坐标系与基础几何体上接触点之间的相对速度沿接触坐标系 *x* 方向的分量。该值的单位为长度/时间。

#### 依赖关系

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Relative Longitudinal Velocity**。

### **vy** — 相对侧向速度，*m/s* 物理信号

物理信号输出端口，提供从动坐标系与基础几何体上接触点之间的相对速度沿接触坐标系 *y* 方向的分量。该值的单位为长度/时间。

#### 依赖关系

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Relative Lateral Velocity**。

### **vsx** — 纵向滑移速度，*m/s* 物理信号

物理信号输出端口，提供轮胎上的滑移点与基础几何体上重合点之间的相对速度沿接触坐标系 *x* 方向的分量。该值的单位为长度/时间。

#### 依赖关系

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Longitudinal Slip Velocity**。

### **vsy** — 侧向滑移速度，*m/s* 物理信号

物理信号输出端口，提供轮胎上的滑移点与基础几何体上重合点之间的相对速度沿接触坐标系 *y* 方向的分量。该值的单位为长度/时间。

#### 依赖关系

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Lateral Slip Velocity**。

#### 横摆

### **psid** — 横摆角速度，*rad/s* 物理信号

物理信号输出端口，提供横摆角的一阶导数。该值的单位为角度/时间。

#### 依赖关系

要启用此端口，请在 **Sensing > Yaw** 下选择 **Velocity**。

#### 外倾

### **gamma** — 外倾角，*rad* 物理信号

物理信号输出端口，提供轮胎的外倾角。该值的单位为角度。

#### 依赖关系

要启用此端口，请在 **Sensing > Camber** 下选择 **Angle**。

### **gammas** — 饱和外倾角，*rad* 物理信号

物理信号输出端口，提供始终限制在 CAMMIN 和 CAMMAX 参数所定义范围内的轮胎外倾角。该值的单位为角度。

#### 依赖关系

要启用此端口，请在 **Sensing > Camber** 下选择 **Angle**。

### **gammad** — 外倾角速度，*rad/s* 物理信号

物理信号输出端口，提供外倾角的一阶导数。该值的单位为角度/时间。

#### 依赖关系

要启用此端口，请在 **Sensing > Camber** 下选择 **Velocity**。

#### 自旋

### **omega** — 自旋速度，*rad* 物理信号

提供自旋角一阶导数的物理信号输出端口。该值的单位为角度/时间。

#### 依赖项

要启用此端口，请在 **Sensing > Spin** 下选择 **Velocity**。

#### 轮胎半径

### **romega** — 自由半径，*m* 物理信号

提供轮胎自由半径的物理信号输出端口。半径随着轮胎旋转加快而增大。该值的单位为长度。

#### 依赖项

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Free Radius**。

### **rl** — 加载半径，*m* 物理信号

提供从轮胎中心到轮胎与接触面之间接触点距离的物理信号输出端口。该值的单位为长度。

#### 依赖项

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Loaded Radius**。

### **re** — 有效滚动半径，*m* 物理信号

提供从从动坐标系到滑移点距离的物理信号输出端口。该值的单位为长度。

#### 依赖项

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Effective Rolling Radius**。

### **rho** — 径向变形，*m* 物理信号

提供 **romega** 端口输出的自由半径与 **rl** 端口输出的加载半径之间差值的物理信号输出端口。该值的单位为长度。

#### 依赖项

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Radial Deflection**。

#### 摩擦力

### **mux** — 纵向摩擦系数，无量纲物理信号

提供由魔术公式方程计算的轮胎纵向摩擦系数的物理信号输出端口。

#### 依赖项

要启用此端口，请在 **Sensing > Friction** 下选择 **Longitudinal Friction Coefficient**。

### **muy** — 侧向摩擦系数，无量纲物理信号

提供由魔术公式方程计算的轮胎侧向摩擦系数的物理信号输出端口。

#### 依赖项

要启用此端口，请在 **Sensing > Friction** 下选择 **Lateral Friction Coefficient**。

#### 接触坐标系

### **Rb** — 基座旋转，无量纲物理信号

输出一个 3×3 旋转矩阵的物理信号端口，该矩阵将接触坐标系中的向量映射到基座几何参考坐标系中的向量。输出信号在基座几何关联的参考坐标系中解析。

#### 依赖项

要启用此端口，请在 **Sensing > Contact Frame** 部分中选择 **Base Rotation**。

### **pb** — 基座平移，*m* 物理信号

输出一个 3×1 向量的物理信号端口，该向量包含在基座几何参考坐标系中解析的接触坐标系原点坐标。

#### 依赖项

要启用此端口，请在 **Sensing > Contact Frame** 部分中选择 **Base Translation**。

### **Rf** — 从动旋转，无量纲物理信号

输出一个 3×3 旋转矩阵的物理信号端口，该矩阵将接触坐标系中的向量映射到从动几何参考坐标系中的向量。输出信号在从动几何关联的参考坐标系中解析。

#### 依赖项

要启用此端口，请在 **Sensing > Contact Frame** 部分中选择 **Follower Rotation**。

### **pf** — 从动平移，*m* 物理信号

输出一个 3×1 向量的物理信号端口，该向量包含在从动几何参考坐标系中解析的接触坐标系原点坐标。

#### 依赖项

要启用此端口，请在 **Sensing > Contact Frame** 部分中选择 **Follower Translation**。

## 参数

### **Tire Side** — 建模时的轮胎位置 `Left`（默认）| `Right`

建模时的轮胎位置，指定为 `Left` 或 `Right`。将该参数设置为轮胎安装在车辆上的那一侧。

### **Tire Parameters** — 轮胎参数 []（默认）| 标量结构体数组

轮胎参数，指定为标量结构体数组。使用 `simscape.multibody.tirread` 函数从 TIR 文件生成该结构体数组。该结构体数组必须包含所有必要的轮胎参数，而任何额外参数在轮胎建模中将被忽略。有关必需参数的列表，请参阅 Required Tire Parameters。

### **Slip Mode** — 滑移模式 `Combined`（默认）| `Combined + Turn`

滑移模式，指定为 `Combined` 或 `Combined + Turn`。

要对组合滑移建模，请选择 `Combined`。要对带转向滑移效应的组合滑移建模，请选择 `Combined + Turn`。选择此选项时，轮胎参数需要转向滑移系数。

**转向滑移系数**

|  |  |
| --- | --- |
| PDXP1 | 由于自旋引起的峰值 FX 降低参数 |
| PDXP2 | 由于自旋并随载荷变化引起的峰值 FX 降低参数 |
| PDXP3 | 由于自旋并随 kappa 变化引起的峰值 FX 降低参数 |
| PKYP1 | 由于自旋引起的侧偏刚度降低 |
| PDYP1 | 由于自旋引起的峰值 FY 降低参数 |
| PDYP2 | 由于自旋并随载荷变化引起的峰值 FY 降低参数 |
| PDYP3 | 由于自旋并随 alpha 变化引起的峰值 FY 降低参数 |
| PDYP4 | 由于自旋平方根引起的峰值 FY 降低参数 |
| PHYP1 | FY-alpha 曲线横向偏移限制 |
| PHYP2 | FY-alpha 曲线最大横向偏移参数 |
| PHYP3 | FY-alpha 曲线最大横向偏移随载荷变化参数 |
| PHYP4 | FY-alpha 曲线最大横向偏移参数 |
| PECP1 | 外倾刚度中相对于自旋的降低因子参数 |
| PECP2 | 外倾刚度中相对于自旋并随载荷变化的降低因子参数 |
| QDTP1 | 由于转向滑移引起的气胎拖距降低因子参数 |
| QCRP1 | 恒定转向且前进速度为零时的转向力矩参数 |
| QCRP2 | 转向滑移力矩（在 alpha=90deg 时）随自旋增加的参数 |
| QBRP1 | 由于侧偏引起的残余（自旋）力矩降低因子参数 |
| QDRP1 | 转向滑移力矩峰值幅值参数 |

[1]

### **Contact Frame Method** — 用于计算接触坐标系位置和方向的方法 `Closest Point`（默认）| `Weighted Penetration`

用于计算接触坐标系位置和方向的方法，指定为：

- `Closest Point`：此方法通过定位接触表面上最接近轮胎中心且位于轮胎平面内的点来确定接触点。接触法向量位于接触点处，并在接触点处垂直于接触印迹。
- `Weighted Penetration`：此方法由于接触表面的不规则性而简化了计算，并在每个仿真时间步计算一个等效平面以近似实际接触面积。接触点是该等效平面上最接近轮胎中心的点。接触法向量位于接触点处，并垂直于等效平面。有关详细信息，请参阅 Custom Tire Force and Torque 的描述。

对于这两种设置，接触坐标系均位于接触点处，并且该坐标系的 *z* 轴与接触法向量对齐。

### Scaling Coefficients

### **LMUX** — 纵向摩擦系数缩放因子 `From Tire Parameters`（默认）| `Provided by Input`

纵向摩擦系数的缩放因子。选择 `From Tire Parameters` 以使用 TIR 文件提供的常数缩放因子，或选择 `Provided by Input` 以使用输入信号作为缩放因子。

### **LMUY** — 横向摩擦系数缩放因子 `From Tire Parameters`（默认）| `Provided by Input`

横向摩擦系数的缩放因子。选择 `From Tire Parameters` 以使用 TIR 文件提供的常数缩放因子，或选择 `Provided by Input` 以使用输入信号作为缩放因子。

### Sensing

#### Force/Torque

### **Resolution Frame** — 用于解析测量值的坐标系 `Contact`（默认）| `Follower`

用于解析计算得到的轮胎力和力矩的坐标系，指定为 `Contact` 或 `Follower`。

## 所属库

Simscape / Multibody / Forces and Torques

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2024b：计算接触坐标系

使用最近点法或加权穿透法计算轮胎与接触面之间接触坐标系的位置和方向。

### R2024b：计算径向变形

使用 **rho** 端口输出径向变形。径向变形是轮胎自由半径与负载半径之差。

### R2023a：基础几何支持 Grid Surface 模块

使用 Grid Surface 模块表示接触面。

## 描述

使用 Magic Formula 轮胎方程施加稳态轮胎力和力矩

Magic Formula Tire Force and Torque 模块实现了组合滑移稳态 Magic Formula 模型，并可选择包含转向滑移效应 [1]。您可以将该模块用于具有类方形横截面的轮胎，例如乘用车、卡车和越野车辆的轮胎。

该模块仅计算轮胎力和力矩。要对轮胎的几何和惯性特性进行建模，必须使用实体模块，例如 Cylindrical Solid 模块。Magic Formula 轮胎模型假设轮胎为圆盘，如下图所示。

从动坐标系位于轮胎中心并随轮胎旋转。接触坐标系位于轮胎与接触面之间的接触点处。该轮胎模块有两种方法计算接触坐标系的位置和方向。对于仅需要单点接触的场景，使用最近点法。对于需要多点接触的行驶工况，使用加权穿透法。有关详细信息，请参阅 Contact Frame Method。

下图显示了零位形时轮胎的接触坐标系和从动坐标系。

偏航角、外倾角和自旋角对应于绕轮胎从动坐标系的 *y*-*x*-*z* 顺序旋转。

要指定轮胎模型的属性，请使用 `simscape.multibody.tirread` 函数生成标量结构体数组，并将该数组输入到 **Tire Parameters** 参数中。该结构体数组必须包含所有必要的轮胎参数，而任何多余参数在轮胎建模中将被忽略。有关必需参数的列表，请参阅 Required Tire Parameters。该模块使用 ISO 符号约定。

要指定轮胎安装在车辆的哪一侧，请使用 **Tire Side** 参数。指定错误的侧别可能导致意外的仿真结果。要正确地将轮胎定向在车辆上，必须将从动坐标系的 *z* 轴与图中所示的蓝色箭头对齐。

轮胎从动坐标系的 z 轴

**con** 端口输出的信号指示轮胎与接触面是否具有有效接触。如果轮胎与表面未接触或接触无效，则所有感测输出（如轮胎力、轮胎力矩和滑移角）均变为零。
