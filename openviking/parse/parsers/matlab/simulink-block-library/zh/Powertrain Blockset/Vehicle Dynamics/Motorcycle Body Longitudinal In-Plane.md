---
type: simulink-block
title: 'Motorcycle Body Longitudinal In-Plane'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Vehicle Dynamics'
documentation_page: 'motorcyclebodylongitudinalinplane'
documentation_source_path: 'ref/motorcyclebodylongitudinalinplane.html'
language: zh-CN
chinese_source: worker-translation
---

# Motorcycle Body Longitudinal In-Plane

## 端口

### 输入

### **FCpF** — 前轮接地点处的纵向力和垂向力 `vector`

前轮接地点 *OCpF* 处的纵向力和垂向力，沿
*iCpF* 和
*kCpF*，单位为 N。信号
向量维度为 `[1x2]` 或
`[2x1]`。

### **FCpR** — 后轮接地点处的纵向力和垂向力 `vector`

后轮接地点 *OCpR* 处的纵向力和垂向力，沿 *iCpR* 和 *kCpR*，单位为 N。信号向量维度为 `[1x2]` 或 `[2x1]`。

### **MDrvArmR** — 后摇臂处的传动链力矩 `scalar`

后摇臂 *OArmRr* 处绕 *jArmRr* 的传动链力矩，单位为 N·m。

### **MDrvFrm** — 车架处的传动链力矩 `scalar`

车架 *OFrm* 处绕 *jFrm* 的传动链力矩，单位为 N·m。

### **FExt** — 车架处的外部纵向力和垂向力 `vector`

施加在等效骑手和摩托车质心 (CM) 处、沿
*iFrm* 和
*kFrm* 的外部纵向力和垂向力，单位为 N。信号
向量维度为 `[1x2]` 或
`[2x1]`。

#### 依赖项

要创建此端口，请选择 **External
forces**。

### **MExt** — 绕车架的外部力矩 `scalar`

绕等效骑手和摩托车质心 (CM) 的外部力矩，
*jFrm*，例如由骑手身体运动引起的力矩，单位为 N·m。

#### 依赖项

要创建此端口，请选择 **External
moments**。

### **MBrkF** — 前轮制动器力矩 `scalar`

前轮 *GWhlFr* 处绕 *jWhlFr* 的制动器力矩，单位为 N·m。

### **MBrkR** — 后轮制动器力矩 `scalar`

后轮 *GWhlRr* 处绕 *jWhlRr* 的制动器力矩，单位为 N·m。

### **MWhlF** — 前轮外部力矩 `scalar`

前轮 *GWhlFr* 处的外部力矩，单位为 N·m。

#### 依赖项

要创建此端口，请选择 **External front wheel
moment**。

### **MWhlR** — 后轮外部力矩 `scalar`

后轮 *GWhlRr* 处的外部力矩，单位为 N·m。

#### 依赖项

要创建此端口，请选择 **External rear wheel
moment**。

### **FSuspF** — 上叉处的外部悬架力 `scalar`

上叉 *OFrkUp* 处沿 *kFrkUp* 的外部悬架力，单位为 N。

#### 依赖项

要创建此端口，请将 **Suspension type** 设置为
`User-defined`。

### **MSuspR** — 后摇臂处的外部悬架力矩 `scalar`

后摇臂 *OArmRr* 处绕 *jArmRr* 的外部悬架力矩，单位为 N·m。

#### 依赖项

要创建此端口，请将 **Suspension type** 设置为
`User-defined`。

### **Grade** — 道路坡度角 `scalar`

道路坡度角，γ，单位为 deg。

#### 依赖项

要创建此端口，请选择 **Grade
angle**。

### **WindXYZ** — 风速 `array`

风速，*WX*、
*WY*、
*WZ*，沿地球固定
*X*、*Y* 和
*Z* 轴，单位为 m/s。信号向量维度为
`[1x3]` 或 `[3x1]`。

#### 依赖项

要创建此端口，请选择 **Wind
velocity**。

### **Temp** — 环境空气温度 `scalar`

环境空气温度，
*Tair*，单位为 K。如果你希望在运行时改变温度，可考虑此选项。

#### 依赖项

要创建此端口，请选择 **Ambient
temperature**。
### 输出

### **Info** — 总线信号 bus

总线信号，包含这些模块计算。

| 信号 | | | | | | 信号 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Geom` | | | | `PosOrgInert` | | 主车架沿地球固定轴的位置 | m |
| `PosFwBdy` | | 前轮中心相对于初始车辆固定车轮位置的位置，沿车辆 Z 向下 *X*、*Y* 和 *Z* 轴 | m |
| `PosRwBdy` | | 后轮中心相对于初始车辆固定车轮位置的位置，沿车辆 Z 向下 *X*、*Y* 和 *Z* 轴 | m |
| `AngOrgInert` | | 主车架绕地球固定轴的旋转 | rad |
| `Frame` | `Inert` | `Cg` | `Disp` | `X` | | | 车辆 CM 沿地球固定 *X* 轴的位移 | m |
| `Y` | | 车辆 CM 沿地球固定 *Y* 轴的位移 | m |
| `Z` | | 车辆 CM 沿地球固定 *Z* 轴的位移 | m |
| `Vel` | `Xdot` | | 车辆 CM 沿地球固定 *X* 轴的速度 | m/s |
| `Ydot` | | 车辆 CM 沿地球固定 *Y* 轴的速度 | m/s |
| `Zdot` | | 车辆 CM 沿地球固定 *Z* 轴的速度 | m/s |
| `Ang` | `phi` | | 车辆固定坐标系绕地球固定 *X* 轴的旋转（侧倾） | rad |
| `theta` | | 车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰） | rad |
| `psi` | | 车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆） | rad |
| `BdyFrm` | `Cg` | `Disp` | `x` | | | 车辆 CM 沿道路固定 *x* 轴的位置 | m |
| `y` | | 车辆 CM 沿道路固定 *y* 轴的位置 | m |
| `z` | | 车辆 CM 沿道路固定 *z* 轴的位置 | m |
| `Vel` | `xdot` | | 车辆 CM 沿道路固定 *x* 轴的速度 | m/s |
| `ydot` | | 车辆 CM 沿道路固定 *y* 轴的速度 | m/s |
| `zdot` | | 车辆 CM 沿道路固定 *z* 轴的速度 | m/s |
| `AngVel` | `p` | | 车辆绕道路固定 *x* 轴的角速度（侧倾角速度） | rad/s |
| `q` | | 车辆绕道路固定 *y* 轴的角速度（俯仰角速度） | rad/s |
| `r` | | 车辆绕道路固定 *z* 轴的角速度（横摆角速度） | rad/s |
| `Acc` | `ax` | | 车辆 CM 沿道路固定 *x* 轴的加速度 | m/s2 |
| `ay` | | 车辆 CM 沿道路固定 *y* 轴的加速度 | m/s2 |
| `az` | | 车辆 CM 沿道路固定 *z* 轴的加速度 | m/s2 |
| `xddot` | | 车辆 CM 沿道路固定 *x* 轴的加速度 | m/s2 |
| `yddot` | | 车辆 CM 沿道路固定 *y* 轴的加速度 | m/s2 |
| `zddot` | | 车辆 CM 沿道路固定 *z* 轴的加速度 | m/s2 |
| `AngAcc` | `pdot` | | 车辆绕道路固定 *x* 轴的角加速度 | rad/s2 |
| `qdot` | | 车辆绕道路固定 *y* 轴的角加速度 | rad/s2 |
| `rdot` | | 车辆绕道路固定 *z* 轴的角加速度 | rad/s2 |
| `Forces` | `Ext` | `Fx` | | 车辆 CM 上沿道路固定 *x* 轴的外部力 | N |
| `Fy` | | 车辆 CM 上沿道路固定 *y* 轴的外部力 | N |
| `Fz` | | 车辆 CM 上沿道路固定 *z* 轴的外部力 | N |
| `Drag` | `Fx` | | 车辆 CM 上沿道路固定 *x* 轴的阻力 | N |
| `Fy` | | 车辆 CM 上沿道路固定 *y* 轴的阻力 | N |
| `Fz` | | 车辆 CM 上沿道路固定 *z* 轴的阻力 | N |
| `Grvty` | `Fx` | | 车辆 CM 上沿道路固定 *x* 轴的重力 | N |
| `Fy` | | 车辆 CM 上沿道路固定 *y* 轴的重力 | N |
| `Fz` | | 车辆 CM 上沿道路固定 *z* 轴的重力 | N |
| `Moments` | `Drag` | `Mx` | | 车辆 CM 上绕道路固定 *x* 轴的阻力力矩 | N·m |
| `My` | | 车辆 CM 上绕道路固定 *y* 轴的阻力力矩 | N·m |
| `Mz` | | 车辆 CM 上绕道路固定 *z* 轴的阻力力矩 | N·m |
| `Ext` | `Mx` | | 车辆 CG 上绕道路固定 *x* 轴的外部力矩 | N·m |
| `My` | | 车辆 CG 上绕道路固定 *y* 轴的外部力矩 | N·m |
| `Mz` | | 车辆 CG 上绕道路固定 *z* 轴的外部力矩 | N·m |
| `Pwr` | `PwrExt` | | | 施加的外部功率 | W |
| `Drag` | | | 由于阻力导致的功率损失 | W |
| `PwrInfo` | `Pwr`  `Trnsfrd` | `PwrFxExt` | | | 来自纵向外部力的机械功率 | W |
| `PwrFzExt` | | | 来自垂向外部力的机械功率 | W |
| `PwrMyExt` | | | 来自外部俯仰力矩的机械功率 | W |
| `PwrNot`  `Trnsfrd` | `PwrFxDrag` | | | 来自纵向阻力力的机械功率损失 | W |
| `PwrFzDrag` | | | 来自垂向升力的机械功率损失 | W |
| `PwrMyDrag` | | | 来自俯仰力矩阻力的机械功率损失 | W |
| `PwrStored` | `PwrStoredGrvty` | | | 重力势能变化率 | W |
| `PwrStoredxdot` | | | 纵向动能变化率 | W |
| `PwrStoredzdot` | | | 垂向动能变化率 | W |
| `PwrStoredq` | | | 俯仰转动动能变化率 | W |
| `Genrl` | `Vel` | `xdot` | | | 车辆 CM 沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | | | 车辆 CM 沿道路固定 *z* 轴的速度 | m/s |
| `Ang` | `thetafrm` | | | 主车架俯仰角 | rad |
| `AngVel` | `thetafrmdot` | | | 主车架转动速度 | rad/s |
| `AngAcc` | `thetafrmddot` | | | 主车架转动加速度 | rad/s2 |
| `Whl` | `Genrl` | `Frnt` | `Cp` | `Disp` | `x` | 前轮接地点沿道路固定 *x* 轴的位置 | m |
| `z` | 前轮接地点沿道路固定 *z* 轴的位置 | m |
| `Vel` | `xdot` | 前轮接地点沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | 前轮接地点沿道路固定 *z* 轴的速度 | m/s |
| `Acc` | `xddot` | 前轮接地点沿道路固定 *x* 轴的加速度 | m/s2 |
| `zddot` | 前轮接地点沿道路固定 *z* 轴的加速度 | m/s2 |
| `Axl` | `Vel` | `xdot` | 前轮轴沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | 前轮轴沿道路固定 *z* 轴的速度 | m/s |
| `Rear` | `Cp` | `Disp` | `x` | 后轮接地点沿道路固定 *x* 轴的位置 | m |
| `z` | 后轮接地点沿道路固定 *z* 轴的位置 | m |
| `Vel` | `xdot` | 后轮接地点沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | 后轮接地点沿道路固定 *z* 轴的速度 | m/s |
| `Acc` | `xddot` | 后轮接地点沿道路固定 *x* 轴的加速度 | m/s2 |
| `zddot` | 后轮接地点沿道路固定 *z* 轴的加速度 | m/s2 |
| `Axl` | `Vel` | `xdot` | 后轮轴沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | 后轮轴沿道路固定 *z* 轴的速度 | m/s |
| `RearArm` | `Genrl` | `Vel` | `xdot` | | | 后摇臂沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | | | 后摇臂沿道路固定 *z* 轴的速度 | m/s |
| `Ang` | `thetara` | | | 后摇臂俯仰角 | rad |
| `AngVel` | `thetaradot` | | | 后摇臂转动速度 | rad/s |
| `AngAcc` | `thetaraddot` | | | 后摇臂转动加速度 | rad/s2 |
| `Fork` | `Genrl` | `Upr` | `Vel` | `xdot` | | 上叉沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | | 上叉沿道路固定 *z* 轴的速度 | m/s |
| `Lwr` | `Disp` | `df` | | 前叉长度 | m |
| `Vel` | `xdot` | | 下叉沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | | 下叉沿道路固定 *z* 轴的速度 | m/s |
| `dfdot` | | 前叉长度速度 | m/s |
| `Acc` | `dfddot` | | 前叉长度加速度 | m/s2 |
| `Susp` | `Genrl` | `Rear` | `Moments` | `Mthetafrm` | | 车架处的后悬架力矩 | N·m |
| `Frnt` | `Forces` | `Fdf` | | 上叉处的悬架力 | N |

### **VCpF** — 前轮接地点处的纵向、侧向和垂向速度 `vector`

前轮接地点 *OCpF* 处的纵向、侧向和垂向速度，沿
*iCpF* 和
*kCpF*，单位为 m/s。信号
向量维度为 `[1x3]` 或
`[3x1]`。侧向分量设置为 0。

### **PCpF** — 前轮接地点处的纵向、侧向和垂向位置 `vector`

前轮接地点 *OCpF* 处的纵向、侧向和垂向位置，沿
*iCpF* 和
*kCpF*，单位为 m。信号
向量维度为 `[1x3]` 或
`[3x1]`。侧向分量设置为 0。

### **VCpR** — 后轮接地点处的纵向、侧向和垂向速度 `vector`

后轮接地点 *OCpR* 处的纵向、侧向和垂向速度，沿
*iCpR* 和
*kCpR*，单位为 m/s。信号
向量维度为 `[1x3]` 或
`[3x1]`。侧向分量设置为 0。

### **PCpR** — 后轮接地点处的纵向、侧向和垂向位置 `vector`

后轮接地点 *OCpR* 处的纵向、侧向和垂向位置，沿
*iCpR* 和
*kCpR*，单位为 m。信号
向量维度为 `[1x3]` 或
`[3x1]`。侧向分量设置为 0。

### **ThetaFrm** — 主车架俯仰角 `scalar`

主车架俯仰角，*ϴfrm*，单位为 rad。

### **ThetaArmR** — 后摇臂俯仰角 `scalar`

后摇臂俯仰角，*ϴra*，单位为 rad。

## 参数

### 选项

### **Suspension type** — 悬架类型 `Simple` (default) | `User-defined`

使用 **Suspension type** 参数指定悬架类型。

| 设置 | 描述 |
| --- | --- |
| `Simple` | 模块将悬架力和力矩建模为弹簧-阻尼系统：  - 上叉处的悬架力 - 后摇臂处的悬架力矩 |
| `User-defined` | 输入悬架力和力矩：  - `FSuspF` – 上叉处的悬架力 - `MSuspR` – 后摇臂处的悬架力矩 |

#### 输入信号

### **External forces** — `FExt` 输入端口 `off` (default) | `on`

指定以创建输入端口 `FExt`。

### **External moments** — `MExt` 输入端口 `off` (default) | `on`

指定以创建输入端口 `MExt`。

### **External front wheel moment** — `MWhlF` 输入端口 `off` (default) | `on`

指定以创建输入端口 `MWhlF`。可考虑使用
此端口输入外部力矩，例如轮毂电机和外部间歇性摩擦相关扰动。

### **External rear wheel moment** — `MWhlR` 输入端口 `off` (default) | `on`

指定以创建输入端口 `MWhlR`。可考虑使用
此端口输入外部力矩，例如轮毂电机和外部间歇性摩擦相关扰动。

### **Grade angle** — `Grade` 输入端口 `on` (default) | `off`

指定以创建输入端口 `Grade`。

### **Wind velocity** — `WindXYZ` 输入端口 `on` (default) | `off`

指定以创建输入端口 `WindXYZ`。

### **Ambient temperature** — `Temp` 输入端口 `off` (default) | `on`

指定以创建输入端口 `Temp`。

### 布局

摩托车车身示意图

使用此表中的参数指定摩托车的几何布局。

| 参数 | | | 图中变量 |
| --- | --- | --- | --- |
| **Initial conditions** | **Position** | **Rear contact patch longitudinal coordinate, CpRrX0** | *OCpR* 相对于道路固定坐标系，沿 `x` |
| **Rear contact patch vertical coordinate, CpRrZ0** | *OCpR* 相对于道路固定坐标系，沿 `z` |
| **Pitch angle of rear arm, ArmRrAng0** | *θra* |
| **Pitch angle of main frame, FrmAng0** | *θFrm* |
| **Fork length, FrkFrL0** | *df* |
| **Frame** | | **Center of mass location, FrmCmPxz** | *GFrm* 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| **Length, FrmLen** | *FrmLen* |
| **Rider** | | **Center of mass location, RdrCmPxz** | *GRdr* 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| **Front Fork** | **Upper** | **Position, FrkUpCmPxz** | *GFrkUp* 相对于 *OFrkUp*，分别沿 *iFrkUp* 和 *kFrkUp* |
| **Offset, FrkOfs** | *FrkOfs* |
| **Lower** | **Position, FrkLwCmPxz** | *GFrkLw* 相对于 *OFrkLw*，分别沿 *iFrkLw* 和 *kFrkLw* |
| **Rear Arm** | | **Position, ArmRrCmPxz** | *GArmRr* 相对于 *OArmRr*，分别沿 *iArmRr* 和 *kArmRr* |
| **Length, ArmRrLen** | *ArmRrLen* |
| **Wheels** | **Front** | **Radius, WhlFrR** | *WhlFrR* |
| **Rear** | **Radius, WhlRrR** | *WhlRrR* |
| **Suspension** | **Front** | **Equilibrium length, FrkLwL0** | *df* |
| **Rear** | **Equilibrium angle, ShkRrAng0** | *θFrm* |

#### 车架

### **Center of mass location, FrmCmPxz** — 车架位置 `[0.255, -0.02]` (default) | `vector`

车架质心位置，
*GFrm*。指定为相对于 *OFrm*，
分别沿 *iFrm* 和
*kFrm* 的向量。

### **Mass, FrmMass** — 车架质量 `223` (default) | `scalar`

车架质量，*FrmMass*，单位为 kg。

### **Mass moment of inertia, FrmIyy** — 车架转动惯量 `26.2` (default) | `scalar`

质量转动惯量，*FrmIyy*，单位为
kg·m2。

### **Length, FrmLen** — 车架长度 `0.730` (default) | `scalar`

车架长度，*FrmLen*，单位为 m。

#### 骑手

### **Center of mass location, RdrCmPxz** — 骑手位置 `[0.275, -0.61]` (default) | `vector`

骑手质心位置，
*GRdr*。指定为相对于 *OFrm*，
分别沿 *iFrm* 和
*kFrm* 的向量。

### **Mass, RdrMass** — 骑手质量 `78` (default) | `scalar`

骑手质量，*RdrMass*，单位为 kg。

### **Mass moment of inertia, RdrIyy** — 骑手转动惯量 `26.2` (default) | `scalar`

骑手质量转动惯量，*RdrIyy*，单位为
kg·m2。

#### 前叉 – 上

### **Position, FrkUpCmPxz** — 上叉位置 `[0.023, -0.098]` (default) | `vector`

上叉质心位置，
*GFrkUp*。指定为相对于 *OFrkUp*，
分别沿 *iFrkUp* 和
*kFrkUp* 的向量。

### **Mass, FrkUpMass** — 上叉质量 `8.8` (default) | `scalar`

上叉质量，*FrkUpMass*，单位为 kg。

### **Mass moment of inertia, FrkUpIyy** — 上叉转动惯量 `0.14` (default) | `scalar`

上叉质量转动惯量，*FrkUpIyy*，单位为
kg·m2。

### **Offset, FrkOfs** — 上叉偏移量 `0.034` (default) | `scalar`

上叉偏移量，*FrkOfs*，单位为 m。

#### 前叉 – 下

### **Position, FrkLwCmPxz** — 下叉位置 `[-0.029, -0.189]` (default) | `vector`

下叉质心位置，
*GFrkLw*。指定为相对于 *OFrkLw*，
分别沿 *iFrkLw* 和
*kFrkLw* 的向量。

### **Mass, FrkLwMass** — 下叉质量 `7.0` (default) | `scalar`

下叉质量，*FrkLwMass*，单位为 kg。

### **Mass moment of inertia, FrkLwIyy** — 下叉转动惯量 `0.18` (default) | `scalar`

下叉质量转动惯量，*FrkLwIyy*，单位为
kg·m2。

#### 后摇臂

### **Position, ArmRrCmPxz** — 后摇臂位置 `[0.275, -0.052]` (default) | `vector`

后摇臂质心位置，
*GArmRr*。指定为相对于 *OArmRr*，
分别沿 *iArmRr* 和
*kArmRr* 的向量。

### **Mass, ArmRrMass** — 后摇臂质量 `10` (default) | `scalar`

后摇臂质量，*ArmRrMass*，单位为 kg。

### **Mass moment of inertia, ArmRrIyy** — 后摇臂转动惯量 `0.8` (default) | `scalar`

后摇臂质量转动惯量，*ArmRrIyy*，单位为
kg·m2。

### **Length, ArmRrLen** — 后摇臂长度 `0.535` (default) | `scalar`

后摇臂长度，*ArmRrLen*，单位为 m。

#### 车轮 – 前

### **Mass, WhlFrMass** — 前轮质量 `12` (default) | `scalar`

前轮质量，*WhlFrMass*，单位为 kg。

### **Radius, WhlFrR** — 前轮半径 `0.3` (default) | `scalar`

前轮半径，*WhlFrR*，单位为 m。

#### 车轮 – 后

### **Mass, WhlRrMass** — 后轮质量 `16.2` (default) | `scalar`

后轮质量，*WhlRrMass*，单位为 kg。

### **Radius, WhlRrR** — 后轮半径 `0.33` (default) | `scalar`

后轮半径，*WhlRrR*，单位为 m。

#### 悬架 – 前

### **Stiffness, SuspFrK** — 前悬架刚度 `25e3` (default) | `scalar`

前悬架在
*OFrkUp* 处沿
*kFrkUp* 的刚度，单位为 N/m。

### **Damping, SuspFrC** — 前悬架阻尼 `1250` (default) | `scalar`

前悬架在
*OFrkUp* 处沿
*kFrkUp* 的阻尼，单位为
N·s/m。

### **Equilibrium length, FrkLwL0** — 前悬架平衡长度 `0.473` (default) | `scalar`

前悬架平衡长度，
*df*，单位为 m。

#### 悬架 – 后

### **Stiffness, SuspRrK** — 后摇臂悬架刚度 `1500` (default) | `scalar`

后摇臂悬架在
*OArmRr* 处绕
*jArmRr* 的刚度，单位为
N/rad。

### **Damping, SuspRrC** — 后摇臂悬架阻尼 `150` (default) | `scalar`

后摇臂悬架在
*OArmRr* 处绕
*jArmRr* 的阻尼，单位为
N·s/rad。

### **Equilibrium angle, ShkRrAng0** — 后悬架平衡角 `0` (default) | `scalar`

后悬架平衡角，
*θFrm*，单位为 rad。

### 空气动力学

### **Longitudinal drag area, Af** — 面积 `2` (default) | `scalar`

用于计算车辆空气阻力的有效车辆横截面积，
*Af*，单位为
m2。

### **Longitudinal drag coefficient, Cd** — 阻力 `.2` (default) | `scalar`

空气阻力系数，*Cd*，
无量纲。

### **Longitudinal lift coefficient, Cl** — 升力 `.1` (default) | `scalar`

空气升力系数，*Cl*，
无量纲。

### **Longitudinal drag pitch moment, Cpm** — 俯仰阻力 `.1` (default) | `scalar`

纵向阻力俯仰力矩系数，
*Cpm*，
无量纲。

### **Pitch moment length, Lcpm** — 俯仰阻力 `2` (default) | `scalar`

俯仰力矩长度，*Lcpm*，单位为 m。

### 环境

### **Gravitational acceleration, g** — 重力 `9.80665` (default) | `scalar`

重力加速度，*g*，单位为
m/s2。

### **Absolute air pressure, Pabs** — 压力 `101325` (default) | `scalar`

环境空气绝对压力，*Pabs*，
单位为 Pa。

### **Air temperature, Tair** — 环境空气温度 `273` (default) | `scalar`

环境空气温度，
*Tair*，单位为 K。

#### 依赖项

要启用此参数，请清除 **Ambient
temperature**。

### 初始条件

#### 位置

### **Rear contact patch longitudinal coordinate, CpRrX0** — 纵向坐标 `0` (default) | `scalar`

后轮接地点纵向坐标，
*OCpR*，相对于
道路固定坐标系，沿 `x`，单位为 m。

### **Rear contact patch vertical coordinate, CpRrZ0** — 垂向坐标 `0` (default) | `scalar`

后轮接地点垂向坐标，
*OCpR*，相对于
道路固定坐标系，沿 `z`，单位为 m。

### **Pitch angle of rear arm, ArmRrAng0** — 后摇臂角度 `0.0590379` (default) | `scalar`

后摇臂俯仰角，
*θra*，单位为 rad。

### **Pitch angle of main frame, FrmAng0** — 角度长度 `0.377024` (default) | `scalar`

主车架俯仰角，
*θFrm*，单位为 rad。

### **Fork length, FrkFrL0** — 前叉长度 `0.4262193` (default) | `scalar`

前叉长度，*df*，单位为
m。

#### 速度

### **Longitudinal velocity of rear contact patch** — 纵向速度 `0` (default) | `scalar`

后轮接地点纵向速度，O˙CpR，相对于道路固定坐标系，沿
`x`，单位为 m/s。

### **Vertical velocity of rear contact patch, CpRrVz0** — 垂向速度 `0` (default) | `scalar`

后轮接地点垂向速度，O˙CpR，相对于道路固定坐标系，沿
`z`，单位为 m/s。

### **Pitch rate of rear arm, ArmRrAngV0** — 俯仰速率 `0` (default) | `scalar`

后摇臂俯仰速率，θ˙ra，单位为 rad/s。

### **Pitch rate of main frame, FrmAngV0** — 俯仰速率 `0` (default) | `scalar`

主车架俯仰速率，θ˙Frm，单位为 rad/s。

### **Lower fork deformation velocity, FrkLwV0** — 变形速度 `0` (default) | `scalar`

下叉变形速度，d˙f，单位为 m/s。

### 坐标偏移

### **Longitudinal offset, longOff** — 纵向偏移 `0` (default) | `scalar`

车辆主车架沿地球固定
*X* 轴的偏移量，单位为 m。

### **Lateral offset, latOff** — 侧向偏移 `0` (default) | `scalar`

车辆主车架沿地球固定
*Y* 轴的偏移量，单位为 m。

### **Vertical offset, vertOff** — 垂向偏移 `0` (default) | `scalar`

车辆主车架沿地球固定
*Z* 轴的偏移量，单位为 m。

### **Roll offset, pitchOff** — 侧倾偏移 `0` (default) | `scalar`

车辆主车架绕地球固定
*X* 轴的偏移量，单位为 rad。

### **Pitch offset, pitchOff** — 俯仰偏移 `0` (default) | `scalar`

车辆主车架绕地球固定
*Y* 轴的偏移量，单位为 rad。

### **Yaw offset, pitchOff** — 横摆偏移 `0` (default) | `scalar`

车辆主车架绕地球固定
*Z* 轴的偏移量，单位为 rad。

## 所属库

Powertrain Blockset / Vehicle Dynamics Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 Generate C and C++ code using Simulink® Coder™.

## 版本历史

**在 R2021b 中引入**

## 描述

纵向平面内摩托车车辆运动

Motorcycle Body Longitudinal In-Plane 模块实现纵向平面内摩托车车身模型，用于计算纵向、垂向和俯仰运动。该模块考虑：

- 车架、后摇臂、前上叉、前下叉、前轮和后轮的质量
- 车架、前下叉、前轮、后轮、后悬架、前悬架、后轮阻尼器、后摇臂和链条的平面内动态效应
- 外部力、外部力矩和空气动力学阻力
- 道路坡度
- 由于加速度引起的轴间重量分布

在动力总成和燃油经济性研究中，例如在包含重度制动或加速，或包含较大垂向变化的道路剖面的研究中，可考虑使用此模块表示摩托车运动。

该模块使用刚体车辆运动、悬架系统力以及风和阻力，计算摩托车车架上的力。然后该模块确定摩托车在前轮和后轮接地点处的位置和速度。

### 布局

为确定刚体摩托车运动，该模块使用附着在摩托车上的右手 (RH) *Cartesian* 参考坐标系。*i*、*j* 和 *k* 是附着到这些坐标系的相互正交单位向量。

摩托车车身示意图

| 坐标系 | 图中变量 | 描述 |
| --- | --- | --- |
| Road | *x*, *z* | 道路固定坐标系。*x* 沿道路坡度，*z* 指向下方。 |
| Motorcycle main frame  - *iFrm* – 沿由 *θfrm* 给出的向量向前 - *kFrm* – 向下 - *jFrm* – 与摩托车平面正交 | *OFrm* | 主车架原点 |
| *GFrm* | 主车架质心 (CM) 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| *GRdr* | 骑手质心 (CM) 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| *ϴfrm* | 主车架绕 *jFrm* 的旋转 |
| Upper fork  - *iFrkUp* – 沿由 *θfrm* 给出的向量向前 - *kFrkUp* – 向下 - *jFrkUp* – 与摩托车平面正交 | *OFrkUp* | 上叉原点 |
| *GFrkUp* | 上叉质心 (CM) 相对于 *OFrkUp*，分别沿 *iFrkUp* 和 *kFrkUp* |
| Lower fork  - *iFrkLw* – 沿由 *θfrm* 给出的向量向前 - *kFrkLw* – 向下 - *jFrkLw* – 与摩托车平面正交 | *OFrkLw* | 下叉原点 |
| *GFrkLw* | 下叉质心 (CM) 相对于 *OFrkLw*，分别沿 *iFrkLw* 和 *kFrkLw* |
| Rear arm  - *iArmRr* – 沿由 *θra* 给出的向量向前 - *kArmRr* – 向下 - *jArmRr* – 与摩托车平面正交 | *OArmRr* | 后摇臂原点 |
| *GArmRr* | 后摇臂质心 (CM) 相对于 *OArmRr*，分别沿 *iArmRr* 和 *kArmRr* |
| *ϴra* | 后摇臂绕 *jArmRr* 的旋转 |
| Front wheel contact patch  - *iCpF* – 沿由道路固定 *x* 轴给出的向量向前 - *kCpF* – 沿由道路固定 *z* 轴给出的向量向下 - *jCpF* – 与摩托车平面正交 | *OCpF* | 前轮接地点原点 |
| Rear wheel contact patch  - *iCpR* – 沿由道路固定 *x* 轴给出的向量向前 - *kCpR* – 沿由道路固定 *z* 轴给出的向量向下 - *jCpR* – 与摩托车平面正交 | *OCpR* | 后轮接地点原点 |

使用此表中的参数指定摩托车的几何布局。

| 参数 | | | 图中变量 |
| --- | --- | --- | --- |
| **Initial conditions** | **Position** | **Rear contact patch longitudinal coordinate, CpRrX0** | *OCpR* 相对于道路固定坐标系，沿 `x` |
| **Rear contact patch vertical coordinate, CpRrZ0** | *OCpR* 相对于道路固定坐标系，沿 `z` |
| **Pitch angle of rear arm, ArmRrAng0** | *θra* |
| **Pitch angle of main frame, FrmAng0** | *θFrm* |
| **Fork length, FrkFrL0** | *df* |
| **Frame** | | **Center of mass location, FrmCmPxz** | *GFrm* 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| **Length, FrmLen** | *FrmLen* |
| **Rider** | | **Center of mass location, RdrCmPxz** | *GRdr* 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| **Front Fork** | **Upper** | **Position, FrkUpCmPxz** | *GFrkUp* 相对于 *OFrkUp*，分别沿 *iFrkUp* 和 *kFrkUp* |
| **Offset, FrkOfs** | *FrkOfs* |
| **Lower** | **Position, FrkLwCmPxz** | *GFrkLw* 相对于 *OFrkLw*，分别沿 *iFrkLw* 和 *kFrkLw* |
| **Rear Arm** | | **Position, ArmRrCmPxz** | *GArmRr* 相对于 *OArmRr*，分别沿 *iArmRr* 和 *kArmRr* |
| **Length, ArmRrLen** | *ArmRrLen* |
| **Wheels** | **Front** | **Radius, WhlFrR** | *WhlFrR* |
| **Rear** | **Radius, WhlRrR** | *WhlRrR* |
| **Suspension** | **Front** | **Equilibrium length, FrkLwL0** | *df* |
| **Rear** | **Equilibrium angle, ShkRrAng0** | *θFrm* |

### 输入信号

您可以使用这些模块参数创建额外输入端口。此表总结了这些设置。

| 输入信号窗格参数 | 输入端口 | 描述 |
| --- | --- | --- |
| **External forces** | `FExt` | 施加在等效骑手和摩托车质心 (CM) 处的外部纵向力和垂向力。 |
| **External moments** | `MExt` | 绕等效骑手和摩托车质心 (CM) 的外部力矩，例如由骑手身体运动引起的力矩。 |
| **External front wheel moment** | `MWhlF` | 前轮 *GWhlFr* 处的外部力矩，例如轮毂电机和外部间歇性摩擦相关扰动。 |
| **External rear wheel moment** | `MWhlR` | 后轮 *GWhlRr* 处的外部力矩，例如轮毂电机和外部间歇性摩擦相关扰动。 |
| **Grade angle** | `Grade` | 道路坡度角。 |
| **Wind velocity** | `WindXYZ` | 风速。 |
| **Ambient temperature** | `Temp` | 环境空气温度。如果你希望在运行时改变温度，可考虑此选项。 |

### 悬架系统

使用 **Suspension type** 参数指定悬架类型。

| 设置 | 描述 |
| --- | --- |
| `Simple` | 模块将悬架力和力矩建模为弹簧-阻尼系统：  - 上叉处的悬架力 - 后摇臂处的悬架力矩 |
| `User-defined` | 输入悬架力和力矩：  - `FSuspF` – 上叉处的悬架力 - `MSuspR` – 后摇臂处的悬架力矩 |

### 风和阻力

该模块从车辆速度分量中减去风速，以获得净相对空速。为计算作用在摩托车上的阻力和力矩，该模块使用净相对空速。

### 功率核算

该模块核算传递的功率、未传递的功率和存储的功率。

| 总线信号 | | | 描述 |
| --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrFxExt` | 来自纵向外部力的机械功率 |
| `PwrFzExt` | 来自垂向外部力的机械功率 |
| `PwrMyExt` | 来自外部俯仰力矩的机械功率 |
| `PwrNotTrnsfrd` — 穿越模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFxDrag` | 来自纵向阻力力的机械功率损失 |
| `PwrFzDrag` | 来自垂向升力的机械功率损失 |
| `PwrMyDrag` | 来自俯仰力矩阻力的机械功率损失 |
| `PwrStored` — 存储能量变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredGrvty` | 重力势能变化率 |
| `PwrStoredxdot` | 纵向动能变化率 |
| `PwrStoredzdot` | 垂向动能变化率 |
| `PwrStoredq` | 俯仰转动动能变化率 |
| `PwrStoredFsFzSprng` | 前悬架存储的弹簧能量 |
| `PwrStoredFsRzSprng` | 后悬架存储的弹簧能量 |
