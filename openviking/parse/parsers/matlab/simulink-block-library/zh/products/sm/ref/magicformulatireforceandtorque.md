---
type: simulink-block
title: 'Magic Formula Tire Force and Torque'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Multibody Dynamics / Loads'
documentation_page: 'magicformulatireforceandtorque'
documentation_source_path: 'ref/magicformulatireforceandtorque.html'
language: zh-CN
chinese_source: worker-translation
---

# Magic Formula Tire Force and Torque

## 端口

### 几何

### **B** — 基础几何 geometry

基础几何，表示轮胎接触的表面。接触面可相对于世界坐标系移动或固定。必须将此端口连接到 Infinite Plane 或 Grid Surface 模块。
### 坐标系

### **F** — 从动坐标系 frame

从动坐标系，表示轮胎。该坐标系原点位于轮胎中心。
### 输入

### **lmux** — 纵向摩擦系数的缩放因子，unitless physical signal

物理信号端口，接受轮胎纵向摩擦系数的缩放因子。

#### 依赖项

要启用此端口，请在 **Scaling Coefficients** 下将 **LMUX** 设置为 `Provided by Input`。

### **lmuy** — 横向摩擦系数的缩放因子，unitless physical signal

物理信号端口，接受轮胎横向摩擦系数的缩放因子。

#### 依赖项

要启用此端口，请在 **Scaling Coefficients** 下将 **LMUY** 设置为 `Provided by Input`。
### 输出

### **con** — 接触信号，unitless physical signal

物理信号输出端口，提供用于确定轮胎与接触面是否具有有效接触的信号。当它们接触且接触有效时，信号等于 `1`，否则信号等于 `0`。

如果从动坐标系位于接触面下方，则轮胎与表面接触无效，模块不向轮胎施加力和力矩。

#### 依赖项

要启用此端口，请在 **Sensing** 下选择 **Contact Signal**。

#### 力/力矩

### **ft** — 轮胎力，*N* physical signal

物理信号输出端口，提供施加到模块接触坐标系的 magic formula 轮胎力。输出包含三部分：

- Fx 是接触点处与接触面相切的纵向力。
- Fy 是横向力，与由 Fx 和 Fz 定义的平面正交。
- Fz 是法向力，在接触点处与接触面法向。

如果将 **Resolution Frame** 参数设置为 `Follower`，模块会在轮胎的从动坐标系中解析力。

#### 依赖项

要启用此端口，请在 **Sensing > Force/Torque** 下选择 **Tire Force**。

### **tt** — 轮胎力矩，*N\*m* physical signal

物理信号输出端口，提供施加到模块接触坐标系的 magic formula 轮胎力矩。输出包含三部分：

- Mx 是翻倾力矩。
- My 是滚动阻力矩。
- Mz 是回正力矩。

如果将 **Resolution Frame** 参数设置为 `Follower`，模块会在轮胎的从动坐标系中解析力矩。

#### 依赖项

要启用此端口，请在 **Sensing > Force/Torque** 下选择 **Tire Torque**。

### **t** — 气胎拖距，*m* physical signal

物理信号输出端口，提供从接触点到合成横向力作用点的距离。该值具有长度单位。

可以使用气胎拖距计算回正力矩，*M*z。

#### 依赖项

要启用此端口，请在 **Sensing > Force/Torque** 下选择 **Pneumatic Trail**。

#### 滑移

### **kappa** — 纵向滑移，unitless physical signal

物理信号输出端口，提供纵向滑移速度与轮胎纵向速度的比值。

#### 依赖项

要启用此端口，请在 **Sensing > Slip** 下选择 **Longitudinal Slip**。

### **kappas** — 饱和纵向滑移，unitless physical signal

物理信号输出端口，提供始终饱和在 KPUMIN 和 KPUMAX 参数所定义限值内的纵向滑移。

#### 依赖项

要启用此端口，请在 **Sensing > Slip** 下选择 **Saturated Longitudinal Slip**。

### **alpha** — 侧偏角，*rad* physical signal

物理信号输出端口，提供由横向滑移速度 *V*sy 与纵向速度 *V*x 构成的直角三角形的角度。该值具有角度单位。

滑移角示意图

#### 依赖项

要启用此端口，请在 **Sensing > Slip** 下选择 **Slip Angle**。

### **alphas** — 饱和侧偏角，*rad* physical signal

物理信号输出端口，提供始终饱和在 ALPMIN 和 ALPMAX 参数所定义限值内的侧偏角。该值具有角度单位。

#### 依赖项

要启用此端口，请在 **Sensing > Slip** 下选择 **Saturated Slip Angle**。

### **phit** — 转向滑移，*rad/m* physical signal

物理信号输出端口，提供轮胎横摆角速度与接触坐标系 *xy* 平面中轮胎速度大小的比值。该值具有角度/长度单位。

转向滑移在建模低速转弯（例如泊车操作）时很有用。

#### 依赖项

要启用此端口，请在 **Sensing > Slip** 下选择 **Turn Slip**。

#### 线速度

### **vx** — 相对纵向速度，*m/s* physical signal

物理信号输出端口，提供从动坐标系与基础几何上接触点之间的相对速度沿接触坐标系 *x* 方向的分量。该值具有长度/时间单位。

#### 依赖项

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Relative Longitudinal Velocity**。

### **vy** — 相对横向速度，*m/s* physical signal

物理信号输出端口，提供从动坐标系与基础几何上接触点之间的相对速度沿接触坐标系 *y* 方向的分量。该值具有长度/时间单位。

#### 依赖项

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Relative Lateral Velocity**。

### **vsx** — 纵向滑移速度，*m/s* physical signal

物理信号输出端口，提供轮胎上滑移点与基础几何上重合点之间的相对速度沿接触坐标系 *x* 方向的分量。该值具有长度/时间单位。

#### 依赖项

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Longitudinal Slip Velocity**。

### **vsy** — 横向滑移速度，*m/s* physical signal

物理信号输出端口，提供轮胎上滑移点与基础几何上重合点之间的相对速度沿接触坐标系 *y* 方向的分量。该值具有长度/时间单位。

#### 依赖项

要启用此端口，请在 **Sensing > Linear Velocity** 下选择 **Lateral Slip Velocity**。

#### 横摆

### **psid** — 横摆角速度，*rad/s* physical signal

物理信号输出端口，提供横摆角的一阶导数。该值具有角度/时间单位。

#### 依赖项

要启用此端口，请在 **Sensing > Yaw** 下选择 **Velocity**。

#### 外倾

### **gamma** — 外倾角，*rad* physical signal

物理信号输出端口，提供轮胎的外倾角。该值具有角度单位。

#### 依赖项

要启用此端口，请在 **Sensing > Camber** 下选择 **Angle**。

### **gammas** — 饱和外倾角，*rad* physical signal

物理信号输出端口，提供始终饱和在 CAMMIN 和 CAMMAX 参数所定义限值内的轮胎外倾角。该值具有角度单位。

#### 依赖项

要启用此端口，请在 **Sensing > Camber** 下选择 **Angle**。

### **gammad** — 外倾角速度，*rad/s* physical signal

物理信号输出端口，提供外倾角的一阶导数。该值具有角度/时间单位。

#### 依赖项

要启用此端口，请在 **Sensing > Camber** 下选择 **Velocity**。

#### 自旋

### **omega** — 自旋速度，*rad* physical signal

物理信号输出端口，提供自旋角的一阶导数。该值具有角度/时间单位。

#### 依赖项

要启用此端口，请在 **Sensing > Spin** 下选择 **Velocity**。

#### 轮胎半径

### **romega** — 自由半径，*m* physical signal

物理信号输出端口，提供轮胎的自由半径。轮胎旋转越快，半径越大。该值具有长度单位。

#### 依赖项

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Free Radius**。

### **rl** — 加载半径，*m* physical signal

物理信号输出端口，提供从轮胎中心到轮胎与接触面之间接触点的距离。该值具有长度单位。

#### 依赖项

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Loaded Radius**。

### **re** — 有效滚动半径，*m* physical signal

物理信号输出端口，提供从动坐标系到滑移点的距离。该值具有长度单位。

#### 依赖项

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Effective Rolling Radius**。

### **rho** — 径向变形，*m* physical signal

物理信号输出端口，提供 **romega** 端口输出的自由半径与 **rl** 端口输出的加载半径之间的差值。该值具有长度单位。

#### 依赖项

要启用此端口，请在 **Sensing > Tire Radius** 下选择 **Radial Deflection**。

#### 摩擦

### **mux** — 纵向摩擦系数，unitless physical signal

物理信号输出端口，提供由 magic formula 方程计算的轮胎纵向摩擦系数。

#### 依赖项

要启用此端口，请在 **Sensing > Friction** 下选择 **Longitudinal Friction Coefficient**。

### **muy** — 横向摩擦系数，unitless physical signal

物理信号输出端口，提供由 magic formula 方程计算的轮胎横向摩擦系数。

#### 依赖项

要启用此端口，请在 **Sensing > Friction** 下选择 **Lateral Friction Coefficient**。

#### 接触坐标系

### **Rb** — 基础旋转，unitless physical signal

物理信号端口，输出一个 3×3 旋转矩阵，该矩阵将接触坐标系中的向量映射为基础几何参考坐标系中的向量。输出信号在基础几何关联的参考坐标系中解析。

#### 依赖项

要启用此端口，请在 **Sensing > Contact Frame** 部分中选择 **Base Rotation**。

### **pb** — 基础平移，*m* physical signal

物理信号端口，输出一个 3×1 向量，其中包含在基础几何参考坐标系中解析的接触坐标系原点坐标。

#### 依赖项

要启用此端口，请在 **Sensing > Contact Frame** 部分中选择 **Base Translation**。

### **Rf** — 从动旋转，unitless physical signal

物理信号端口，输出一个 3×3 旋转矩阵，该矩阵将接触坐标系中的向量映射为从动几何参考坐标系中的向量。输出信号在从动几何关联的参考坐标系中解析。

#### 依赖项

要启用此端口，请在 **Sensing > Contact Frame** 部分中选择 **Follower Rotation**。

### **pf** — 从动平移，*m* physical signal

物理信号端口，输出一个 3×1 向量，其中包含在从动几何参考坐标系中解析的接触坐标系原点坐标。

#### 依赖项

要启用此端口，请在 **Sensing > Contact Frame** 部分中选择 **Follower Translation**。

## 参数

### **Tire Side** — 建模时的轮胎位置 `Left` (default) | `Right`

建模时的轮胎位置，指定为 `Left` 或 `Right`。将该参数设置为车辆上安装轮胎的一侧。

### **Tire Parameters** — 轮胎参数 [] (default) | scalar structure array

轮胎参数，指定为 scalar structure array。使用 `simscape.multibody.tirread` 函数从 TIR 文件生成该结构体数组。该结构体数组必须包含所有必要的轮胎参数，而任何额外参数在轮胎建模中会被忽略。有关所需参数列表，请参阅 Required Tire Parameters。

### **Slip Mode** — 滑移模式 `Combined` (default) | `Combined + Turn`

滑移模式，指定为 `Combined` 或 `Combined + Turn`。

要对组合滑移建模，选择 `Combined`。要对带转向滑移效应的组合滑移建模，选择 `Combined + Turn`。选择此选项时，轮胎参数需要转向滑移系数。

**转向滑移系数**

|  |  |
| --- | --- |
| PDXP1 | 由于自旋参数的峰值 FX 减小 |
| PDXP2 | 由于自旋且载荷变化参数的峰值 FX 减小 |
| PDXP3 | 由于自旋且 kappa 参数的峰值 FX 减小 |
| PKYP1 | 由于自旋引起的侧偏刚度减小 |
| PDYP1 | 由于自旋参数的峰值 FY 减小 |
| PDYP2 | 由于自旋且载荷变化参数的峰值 FY 减小 |
| PDYP3 | 由于自旋且 alpha 参数的峰值 FY 减小 |
| PDYP4 | 由于自旋平方根的峰值 FY 减小 |
| PHYP1 | FY-alpha 曲线横向偏移限制 |
| PHYP2 | FY-alpha 曲线最大横向偏移参数 |
| PHYP3 | FY-alpha 曲线随载荷变化的最大横向偏移参数 |
| PHYP4 | FY-alpha 曲线最大横向偏移参数 |
| PECP1 | 外倾刚度中关于自旋的缩减因子参数 |
| PECP2 | 外倾刚度中关于自旋的缩减因子随载荷变化参数 |
| QDTP1 | 由于转向滑移参数的气胎拖距缩减因子 |
| QCRP1 | 恒定转弯且零前进速度下的转弯力矩参数 |
| QCRP2 | 随自旋增加的转向滑移力矩（在 alpha=90deg 时）参数 |
| QBRP1 | 由于侧偏的残余（自旋）力矩缩减因子参数 |
| QDRP1 | 转向滑移力矩峰值大小参数 |

[1]

### **Contact Frame Method** — 用于计算接触坐标系位置和方向的方法 `Closest Point` (default) | `Weighted Penetration`

用于计算接触坐标系位置和方向的方法，指定为：

- `Closest Point`：此方法通过定位接触面上最接近轮胎中心且位于轮胎平面内的点来确定接触点。接触法向向量位于接触点处，并且在接触点处垂直于接触印迹。
- `Weighted Penetration`：此方法由于接触面的不规则性简化了计算，并在每个仿真时间步计算一个等效平面来近似实际接触区域。接触点是该等效平面上距离轮胎中心最近的点。接触法向向量位于接触点处，并且垂直于等效平面。有关更多信息，请参阅 Custom Tire Force and Torque 的说明。

对于这两种设置，接触坐标系位于接触点，且坐标系的 *z* 轴与接触法向对齐。

### 缩放系数

### **LMUX** — 纵向摩擦系数的缩放因子 `From Tire Parameters` (default) | `Provided by Input`

纵向摩擦系数的缩放因子。选择 `From Tire Parameters` 以使用 TIR 文件提供的常数缩放因子，或选择 `Provided by Input` 以使用输入信号作为缩放因子。

### **LMUY** — 横向摩擦系数的缩放因子 `From Tire Parameters` (default) | `Provided by Input`

横向摩擦系数的缩放因子。选择 `From Tire Parameters` 以使用 TIR 文件提供的常数缩放因子，或选择 `Provided by Input` 以使用输入信号作为缩放因子。

### 传感

#### 力/力矩

### **Resolution Frame** — 用于解析测量的坐标系 `Contact`（默认）| `Follower`

用于解析计算得到的轮胎力和力矩的坐标系，指定为
`Contact` 或
`Follower`。

## 所属库

Simscape / Multibody / Forces and Torques

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2024b：计算接触坐标系

使用最近点方法或加权穿透方法计算轮胎与接触表面之间接触坐标系的位置和方向。

### R2024b：计算径向变形

使用 **rho** 端口输出径向变形。径向变形是轮胎自由半径与加载半径之差。

### R2023a：基础几何支持 Grid Surface 模块

使用 Grid Surface 模块表示接触表面。

## 描述

使用 Magic Formula 轮胎方程施加稳态轮胎力和力矩

Magic Formula Tire Force and Torque 模块实现组合滑移稳态 Magic Formula 模型，并可选包括转向滑移效应 [1]。您可以将该模块用于具有类方形横截面的轮胎，例如乘用车、卡车和越野车辆的轮胎。

该模块仅计算轮胎力和力矩。要对轮胎的几何形状和惯性特性进行建模，必须使用实体模块，例如 Cylindrical Solid 模块。Magic Formula 轮胎模型假设轮胎为圆盘，如图所示。

从动坐标系位于轮胎中心，并随轮胎旋转。接触坐标系位于轮胎与接触表面之间的接触点处。轮胎模块有两种方法计算接触坐标系的位置和方向。对于只需要单点接触的场景，使用最近点方法。对于需要多点接触的行驶工况，使用加权穿透方法。有关详细信息，请参阅 Contact Frame Method。

该图显示了零配置下轮胎的接触坐标系和从动坐标系。

横摆角、外倾角和自旋角对应于绕轮胎从动坐标系的 *y*-*x*-*z* 顺序旋转。

要指定轮胎模型的属性，请使用 `simscape.multibody.tirread` 函数生成标量结构体数组，并将该数组输入到 **Tire Parameters** 参数中。该结构体数组必须包括所有必要的轮胎参数，而任何额外参数在轮胎建模中都会被忽略。有关所需参数的列表，请参阅 Required Tire Parameters。该模块使用 ISO 符号约定。

要指定轮胎安装到车辆的哪一侧，请使用 **Tire Side** 参数。指定错误的一侧可能导致意外的仿真结果。要在车辆上正确定向轮胎，必须使从动坐标系的 *z* 轴与图中所示的蓝色箭头对齐。

轮胎从动坐标系的 z 轴

**con** 端口输出的信号指示轮胎与接触表面是否具有有效接触。如果轮胎与表面不接触或接触无效，则所有感测输出（例如轮胎力、轮胎力矩和滑移角）都变为零。
