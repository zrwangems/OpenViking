---
type: simulink-block
title: 'Motorcycle Body Longitudinal In-Plane'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'motorcyclebodylongitudinalinplane'
documentation_source_path: 'ref/motorcyclebodylongitudinalinplane.html'
language: zh-CN
chinese_source: worker-translation
---

# Motorcycle Body Longitudinal In-Plane

## 端口
```yaml
ports:
- name: FCpF
  summary: 前轮接地点纵向力和垂向力 vector
  direction: input
- name: FCpR
  summary: 后轮接地点纵向力和垂向力 vector
  direction: input
- name: MDrvArmR
  summary: 后摇臂上的传动链力矩 scalar
  direction: input
- name: MDrvFrm
  summary: 车架上的传动链力矩 scalar
  direction: input
- name: FExt
  summary: 车架上的外部纵向力和垂向力 vector
  direction: input
- name: MExt
  summary: 绕车架的外部力矩 scalar
  direction: input
- name: MBrkF
  summary: 前轮制动力矩 scalar
  direction: input
- name: MBrkR
  summary: 后轮制动力矩 scalar
  direction: input
- name: MWhlF
  summary: 前轮外部力矩 scalar
  direction: input
- name: MWhlR
  summary: 后轮外部力矩 scalar
  direction: input
- name: FSuspF
  summary: 上叉上的外部悬架力 scalar
  direction: input
- name: MSuspR
  summary: 后摇臂上的外部悬架力矩 scalar
  direction: input
- name: Grade
  summary: 道路坡度角 scalar
  direction: input
- name: WindXYZ
  summary: 风速 array
  direction: input
- name: Temp
  summary: 环境空气温度 scalar
  direction: input
- name: Info
  summary: 总线信号总线
  direction: output
- name: VCpF
  summary: 前轮接地点纵向、侧向和垂向速度 vector
  direction: output
- name: PCpF
  summary: 前轮接地点纵向、侧向和垂向位置 vector
  direction: output
- name: VCpR
  summary: 后轮接地点纵向、侧向和垂向速度 vector
  direction: output
- name: PCpR
  summary: 后轮接地点纵向、侧向和垂向位置 vector
  direction: output
- name: ThetaFrm
  summary: 主车架俯仰角 scalar
  direction: output
- name: ThetaArmR
  summary: 后摇臂俯仰角 scalar
  direction: output
```

### 输入

### **FCpF** — 前轮接地点纵向力和垂向力 `vector`

前轮接地点沿 *iCpF* 和 *kCpF* 方向的纵向力和垂向力 *OCpF*，单位为 N。信号向量维度为 `[1x2]` 或 `[2x1]`。

### **FCpR** — 后轮接地点纵向力和垂向力 `vector`

后轮接地点沿 *iCpR* 和 *kCpR* 方向的纵向力和垂向力 *OCpR*，单位为 N。信号向量维度为 `[1x2]` 或 `[2x1]`。

### **MDrvArmR** — 后摇臂上的传动链力矩 `scalar`

后摇臂 *OArmRr* 上绕 *jArmRr* 的传动链力矩，单位为 N·m。

### **MDrvFrm** — 车架上的传动链力矩 `scalar`

车架 *OFrm* 上绕 *jFrm* 的传动链力矩，单位为 N·m。

### **FExt** — 车架上的外部纵向力和垂向力 `vector`

施加在等效骑手和摩托车质心（CM）处、沿 *iFrm* 和 *kFrm* 方向的外部纵向力和垂向力，单位为 N。信号向量维度为 `[1x2]` 或 `[2x1]`。

#### 依赖

要创建此端口，请选择 **External forces**。

### **MExt** — 绕车架的外部力矩 `scalar`

绕等效骑手和摩托车质心 *jFrm* 的外部力矩，例如由骑手身体运动引起的力矩，单位为 N·m。

#### 依赖

要创建此端口，请选择 **External moments**。

### **MBrkF** — 前轮制动力矩 `scalar`

前轮 *GWhlFr* 上绕 *jWhlFr* 的制动力矩，单位为 N·m。

### **MBrkR** — 后轮制动力矩 `scalar`

后轮 *GWhlRr* 上绕 *jWhlRr* 的制动力矩，单位为 N·m。

### **MWhlF** — 前轮外部力矩 `scalar`

前轮 *GWhlFr* 上的外部力矩，单位为 N·m。

#### 依赖

要创建此端口，请选择 **External front wheel moment**。

### **MWhlR** — 后轮外部力矩 `scalar`

后轮 *GWhlRr* 上的外部力矩，单位为 N·m。

#### 依赖

要创建此端口，请选择 **External rear wheel moment**。

### **FSuspF** — 上叉上的外部悬架力 `scalar`

上叉 *OFrkUp* 上沿 *kFrkUp* 方向的外部悬架力，单位为 N。

#### 依赖

要创建此端口，请将 **Suspension type** 设置为 `User-defined`。

### **MSuspR** — 后摇臂上的外部悬架力矩 `scalar`

上叉 *OArmRr* 上绕 *jArmRr* 的外部悬架力，单位为 N·m。

#### 依赖

要创建此端口，请将 **Suspension type** 设置为 `User-defined`。

### **Grade** — 道路坡度角 `scalar`

道路坡度角 γ，单位为 deg。

#### 依赖

要创建此端口，请选择 **Grade angle**。

### **WindXYZ** — 风速 `array`

沿地球固定 *X*、*Y* 和 *Z* 轴的风速 *WX*、*WY*、*WZ*，单位为 m/s。信号向量维度为 `[1x3]` 或 `[3x1]`。

#### 依赖

要创建此端口，请选择 **Wind velocity**。

### **Temp** — 环境空气温度 `scalar`

环境空气温度 *Tair*，单位为 K。如果希望在运行时改变温度，请考虑此选项。

#### 依赖

要创建此端口，请选择 **Ambient temperature**。
### 输出

### **Info** — 总线信号总线

包含这些模块计算的总线信号。

| 信号 | | | | | | 信号 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Geom` | | | | `PosOrgInert` | | 主车架沿地球固定轴的位置 | m |
| `PosFwBdy` | | 前轮中心相对于初始车辆固定车轮位置的位置，沿车辆 Z 向下 *X* 轴、*Y* 轴和 *Z* 轴 | m |
| `PosRwBdy` | | 后轮中心相对于初始车辆固定车轮位置的位置，沿车辆 Z 向下 *X* 轴、*Y* 轴和 *Z* 轴 | m |
| `AngOrgInert` | | 主车架绕地球固定轴的旋转 | rad |
| `Frame` | `Inert` | `Cg` | `Disp` | `X` | | 车辆质心沿地球固定 *X* 轴的位移 | m |
| `Y` | | 车辆质心沿地球固定 *Y* 轴的位移 | m |
| `Z` | | 车辆质心沿地球固定 *Z* 轴的位移 | m |
| `Vel` | `Xdot` | | 车辆质心沿地球固定 *X* 轴的速度 | m/s |
| `Ydot` | | 车辆质心沿地球固定 *Y* 轴的速度 | m/s |
| `Zdot` | | 车辆质心沿地球固定 *Z* 轴的速度 | m/s |
| `Ang` | `phi` | | 车辆固定坐标系绕地球固定 *X* 轴的旋转（横滚） | rad |
| `theta` | | 车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰） | rad |
| `psi` | | 车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆） | rad |
| `BdyFrm` | `Cg` | `Disp` | `x` | | 车辆质心沿道路固定 *x* 轴的位置 | m |
| `y` | | 车辆质心沿道路固定 *y* 轴的位置 | m |
| `z` | | 车辆质心沿道路固定 *z* 轴的位置 | m |
| `Vel` | `xdot` | | 车辆质心沿道路固定 *x* 轴的速度 | m/s |
| `ydot` | | 车辆质心沿道路固定 *y* 轴的速度 | m/s |
| `zdot` | | 车辆质心沿道路固定 *z* 轴的速度 | m/s |
| `AngVel` | `p` | | 车辆绕道路固定 *x* 轴的角速度（横滚角速率） | rad/s |
| `q` | | 车辆绕道路固定 *y* 轴的角速度（俯仰角速率） | rad/s |
| `r` | | 车辆绕道路固定 *z* 轴的角速度（横摆角速率） | rad/s |
| `Acc` | `ax` | | 车辆质心沿道路固定 *x* 轴的加速度 | m/s2 |
| `ay` | | 车辆质心沿道路固定 *y* 轴的加速度 | m/s2 |
| `az` | | 车辆质心沿道路固定 *z* 轴的加速度 | m/s2 |
| `xddot` | | 车辆质心沿道路固定 *x* 轴的加速度 | m/s2 |
| `yddot` | | 车辆质心沿道路固定 *y* 轴的加速度 | m/s2 |
| `zddot` | | 车辆质心沿道路固定 *z* 轴的加速度 | m/s2 |
| `AngAcc` | `pdot` | | 车辆绕道路固定 *x* 轴的角加速度 | rad/s2 |
| `qdot` | | 车辆绕道路固定 *y* 轴的角加速度 | rad/s2 |
| `rdot` | | 车辆绕道路固定 *z* 轴的角加速度 | rad/s2 |
| `Forces` | `Ext` | `Fx` | | 车辆质心沿道路固定 *x* 轴的外部力 | N |
| `Fy` | | 车辆质心沿道路固定 *x* 轴的外部力 | N |
| `Fz` | | 车辆质心沿道路固定 *x* 轴的外部力 | N |
| `Drag` | `Fx` | | 车辆质心沿道路固定 *x* 轴的阻力 | N |
| `Fy` | | 车辆质心沿道路固定 *y* 轴的阻力 | N |
| `Fz` | | 车辆质心沿道路固定 *z* 轴的阻力 | N |
| `Grvty` | `Fx` | | 车辆质心沿道路固定 *x* 轴的重力 | N |
| `Fy` | | 车辆质心沿道路固定 *y* 轴的重力 | N |
| `Fz` | | 车辆质心沿道路固定 *z* 轴的重力 | N |
| `Moments` | `Drag` | `Mx` | | 车辆质心绕道路固定 *x* 轴的阻力矩 | N·m |
| `My` | | 车辆质心绕道路固定 *z* 轴的阻力矩 | N·m |
| `Mz` | | 车辆质心绕道路固定 *z* 轴的阻力矩 | N·m |
| `Ext` | `Mx` | | 车辆质心绕道路固定 *x* 轴的外部力矩 | N·m |
| `My` | | 车辆质心绕道路固定 *y* 轴的外部力矩 | N·m |
| `Mz` | | 车辆质心绕道路固定 *z* 轴的外部力矩 | N·m |
| `Pwr` | `PwrExt` | | | 施加的外部功率 | W |
| `Drag` | | | 阻力导致的功率损失 | W |
| `PwrInfo` | `Pwr`  `Trnsfrd` | `PwrFxExt` | | | 来自纵向外部力的机械功率 | W |
| `PwrFzExt` | | | 来自垂向外部力的机械功率 | W |
| `PwrMyExt` | | | 来自外部俯仰力矩的机械功率 | W |
| `PwrNot`  `Trnsfrd` | `PwrFxDrag` | | | 来自纵向阻力的机械功率损失 | W |
| `PwrFzDrag` | | | 来自垂向升力的机械功率损失 | W |
| `PwrMyDrag` | | | 来自俯仰力矩阻力的机械功率损失 | W |
| `PwrStored` | `PwrStoredGrvty` | | | 重力势能的变化率 | W |
| `PwrStoredxdot` | | | 纵向动能的变化率 | W |
| `PwrStoredzdot` | | | 垂向动能的变化率 | W |
| `PwrStoredq` | | | 俯仰转动动能的变化率 | W |
| `Genrl` | `Vel` | `xdot` | | | 车辆质心沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | | | 车辆质心沿道路固定 *z* 轴的速度 | m/s |
| `Ang` | `thetafrm` | | | 主车架的俯仰角 | rad |
| `AngVel` | `thetafrmdot` | | | 主车架的旋转速度 | rad/s |
| `AngAcc` | `thetafrmddot` | | | 主车架的旋转加速度 | rad/s2 |
| `Whl` | `Genrl` | `Frnt` | `Cp` | `Disp` | `x` | 前轮接地点沿道路固定 *x* 轴的位置 | m |
| `z` | 前轮接地点沿道路固定 *z* 轴的位置 | m |
| `Vel` | `xdot` | 前轮接地点沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | 前轮接地点沿道路固定 *z* 轴的速度 | m/s |
| `Acc` | `xddot` | 前轮接地点沿道路固定 *x* 轴的加速度 | m/s2 |
| `zddot` | 前轮接地点沿道路固定 *z* 轴的加速度 | m/s2 |
| `Axl` | `Vel` | `xdot` | 前轮车轴沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | 前轮车轴沿道路固定 *z* 轴的速度 | m/s |
| `Rear` | `Cp` | `Disp` | `x` | 后轮接地点沿道路固定 *x* 轴的位置 | m |
| `z` | 后轮接地点沿道路固定 *z* 轴的位置 | m |
| `Vel` | `xdot` | 后轮接地点沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | 后轮接地点沿道路固定 *z* 轴的速度 | m/s |
| `Acc` | `xddot` | 后轮接地点沿道路固定 *x* 轴的加速度 | m/s2 |
| `zddot` | 后轮接地点沿道路固定 *z* 轴的加速度 | m/s2 |
| `Axl` | `Vel` | `xdot` | 后轮车轴沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | 后轮车轴沿道路固定 *z* 轴的速度 | m/s |
| `RearArm` | `Genrl` | `Vel` | `xdot` | | | 后摆臂沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | | | 后摆臂沿道路固定 *z* 轴的速度 | m/s |
| `Ang` | `thetara` | | | 后摆臂的俯仰角 | rad |
| `AngVel` | `thetaradot` | | | 后摆臂的旋转速度 | rad/s |
| `AngAcc` | `thetaraddot` | | | 后摆臂的旋转加速度 | rad/s2 |
| `Fork` | `Genrl` | `Upr` | `Vel` | `xdot` | | 上前叉沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | | 上前叉沿道路固定 *z* 轴的速度 | m/s |
| `Lwr` | `Disp` | `df` | | 前叉长度 | m |
| `Vel` | `xdot` | | 下前叉沿道路固定 *x* 轴的速度 | m/s |
| `zdot` | | 下前叉沿道路固定 *z* 轴的速度 | m/s |
| `dfdot` | | 前叉长度速度 | m/s |
| `Acc` | `dfddot` | | 前叉长度加速度 | m/s2 |
| `Susp` | `Genrl` | `Rear` | `Moments` | `Mthetafrm` | | 车架处的后悬架力矩 | N·m |
| `Frnt` | `Forces` | `Fdf` | | 上前叉处的悬架力 | N |

### **VCpF** — 前轮接地点纵向、侧向和垂向速度 `vector`

前轮接地点 *OCpF* 处沿 *iCpF* 和 *kCpF* 的纵向、侧向和垂向速度，单位为 m/s。信号向量维度为 `[1x3]` 或 `[3x1]`。侧向分量设置为 0。

### **PCpF** — 前轮接地点纵向、侧向和垂向位置 `vector`

前轮接地点 *OCpF* 处沿 *iCpF* 和 *kCpF* 的纵向、侧向和垂向位置，单位为 m。信号向量维度为 `[1x3]` 或 `[3x1]`。侧向分量设置为 0。

### **VCpR** — 后轮接地点纵向、侧向和垂向速度 `vector`

后轮接地点 *OCpR* 处沿 *iCpR* 和 *kCpR* 的纵向、侧向和垂向速度，单位为 m/s。信号向量维度为 `[1x3]` 或 `[3x1]`。侧向分量设置为 0。

### **PCpR** — 后轮接地点纵向、侧向和垂向位置 `vector`

后轮接地点 *OCpR* 处沿 *iCpR* 和 *kCpR* 的纵向、侧向和垂向位置，单位为 m。信号向量维度为 `[1x3]` 或 `[3x1]`。侧向分量设置为 0。

### **ThetaFrm** — 主车架俯仰角 `scalar`

主车架俯仰角，*ϴfrm*，单位为 rad。

### **ThetaArmR** — 后摇臂俯仰角 `scalar`

后摇臂俯仰角，*ϴra*，单位为 rad。
## 参数
```yaml
parameters:
- name: Suspension type
  summary: 悬架类型 Simple（默认）| User-defined
  group: 选项
- name: External forces
  summary: FExt 输入端口 off（默认）| on
  group: 选项
- name: External moments
  summary: MExt 输入端口 off（默认）| on
  group: 选项
- name: External front wheel moment
  summary: MWhlF 输入端口 off（默认）| on
  group: 选项
- name: External rear wheel moment
  summary: MWhlR 输入端口 off（默认）| on
  group: 选项
- name: Grade angle
  summary: Grade 输入端口 on（默认）| off
  group: 选项
- name: Wind velocity
  summary: WindXYZ 输入端口 on（默认）| off
  group: 选项
- name: Ambient temperature
  summary: Temp 输入端口 off（默认）| on
  group: 选项
- name: 质心位置，FrmCmPxz
  summary: 车架位置 [0.255, -0.02]（默认）| vector
  group: Layout
- name: 质量，FrmMass
  summary: 车架质量 223（默认）| scalar
  group: Layout
- name: 质量转动惯量，FrmIyy
  summary: 车架转动惯量 26.2（默认）| scalar
  group: Layout
- name: 长度，FrmLen
  summary: 车架长度 0.730（默认）| scalar
  group: Layout
- name: 质心位置，RdrCmPxz
  summary: 骑手位置 [0.275, -0.61]（默认）| vector
  group: Layout
- name: 质量，RdrMass
  summary: 骑手质量 78（默认）| scalar
  group: Layout
- name: 质量转动惯量，RdrIyy
  summary: 骑手转动惯量 26.2（默认）| scalar
  group: Layout
- name: 位置，FrkUpCmPxz
  summary: 上部前叉位置 [0.023, -0.098]（默认）| vector
  group: Layout
- name: 质量，FrkUpMass
  summary: 上部前叉质量 8.8（默认）| scalar
  group: Layout
- name: 质量转动惯量，FrkUpIyy
  summary: 上部前叉转动惯量 0.14（默认）| scalar
  group: Layout
- name: 偏移量，FrkOfs
  summary: 上部前叉偏移量 0.034（默认）| scalar
  group: Layout
- name: 位置，FrkLwCmPxz
  summary: 下部前叉位置 [-0.029, -0.189]（默认）| vector
  group: Layout
- name: 质量，FrkLwMass
  summary: 下部前叉质量 7.0（默认）| scalar
  group: Layout
- name: 质量转动惯量，FrkLwIyy
  summary: 下部前叉转动惯量 0.18（默认）| scalar
  group: Layout
- name: Position, ArmRrCmPxz
  summary: 后臂位置 [0.275, -0.052]（默认）| vector
  group: Layout
- name: Mass, ArmRrMass
  summary: 后臂质量 10（默认）| scalar
  group: Layout
- name: Mass moment of inertia, ArmRrIyy
  summary: 后臂转动惯量 0.8（默认）| scalar
  group: Layout
- name: Length, ArmRrLen
  summary: 后臂长度 0.535（默认）| scalar
  group: Layout
- name: Mass, WhlFrMass
  summary: 前轮质量 12（默认）| scalar
  group: Layout
- name: Radius, WhlFrR
  summary: 前轮半径 0.3（默认）| scalar
  group: Layout
- name: Mass, WhlRrMass
  summary: 后轮质量 16.2（默认）| scalar
  group: Layout
- name: Radius, WhlRrR
  summary: 后轮半径 0.33（默认）| scalar
  group: Layout
- name: Stiffness, SuspFrK
  summary: 前悬架刚度 25e3（默认）| scalar
  group: Layout
- name: Damping, SuspFrC
  summary: 前悬架阻尼 1250（默认）| scalar
  group: Layout
- name: Equilibrium length, FrkLwL0
  summary: 前悬架平衡长度 0.473（默认）| scalar
  group: Layout
- name: Stiffness, SuspRrK
  summary: 后臂悬架刚度 1500（默认）| scalar
  group: Layout
- name: Damping, SuspRrC
  summary: 后臂悬架阻尼 150（默认）| scalar
  group: Layout
- name: Equilibrium angle, ShkRrAng0
  summary: 后悬架平衡角 0（默认）| scalar
  group: Layout
- name: Longitudinal drag area, Af
  summary: 面积 2（默认）| scalar
  group: Aerodynamic
- name: Longitudinal drag coefficient, Cd
  summary: 阻力 .2（默认）| scalar
  group: Aerodynamic
- name: Longitudinal lift coefficient, Cl
  summary: 升力 .1（默认）| scalar
  group: Aerodynamic
- name: Longitudinal drag pitch moment, Cpm
  summary: 俯仰阻力 .1（默认）| scalar
  group: Aerodynamic
- name: Pitch moment length, Lcpm
  summary: 俯仰阻力 2（默认）| scalar
  group: Aerodynamic
- name: Gravitational acceleration, g
  summary: 重力 9.80665（默认）| scalar
  group: Environment
- name: Absolute air pressure, Pabs
  summary: 压力 101325（默认）| scalar
  group: Environment
- name: Air temperature, Tair
  summary: 环境空气温度 273（默认）| scalar
  group: Environment
- name: Rear contact patch longitudinal coordinate, CpRrX0
  summary: 纵向坐标 0（默认）| scalar
  group: Initial conditions
- name: Rear contact patch vertical coordinate, CpRrZ0
  summary: 垂直坐标 0（默认）| scalar
  group: Initial conditions
- name: Pitch angle of rear arm, ArmRrAng0
  summary: 后臂角度 0.0590379（默认）| scalar
  group: Initial conditions
- name: Pitch angle of main frame, FrmAng0
  summary: 角度长度 0.377024（默认）| scalar
  group: Initial conditions
- name: Fork length, FrkFrL0
  summary: 前叉长度 0.4262193（默认）| scalar
  group: Initial conditions
- name: 后接触印迹纵向速度
  summary: 纵向速度 0（默认）| scalar
  group: Initial conditions
- name: 后接触印迹垂直速度，CpRrVz0
  summary: 垂直速度 0（默认）| scalar
  group: Initial conditions
- name: 后摇臂俯仰角速度，ArmRrAngV0
  summary: 俯仰角速度 0（默认）| scalar
  group: Initial conditions
- name: 主车架俯仰角速度，FrmAngV0
  summary: 俯仰角速度 0（默认）| scalar
  group: Initial conditions
- name: 下前叉变形速度，FrkLwV0
  summary: 变形速度 0（默认）| scalar
  group: Initial conditions
- name: 纵向偏移，longOff
  summary: 纵向偏移 0（默认）| scalar
  group: 坐标偏移
- name: 横向偏移，latOff
  summary: 横向偏移 0（默认）| scalar
  group: 坐标偏移
- name: 垂直偏移，vertOff
  summary: 垂直偏移 0（默认）| scalar
  group: 坐标偏移
- name: 侧倾偏移，pitchOff
  summary: 侧倾偏移 0（默认）| scalar
  group: 坐标偏移
- name: 俯仰偏移，pitchOff
  summary: 俯仰偏移 0（默认）| scalar
  group: 坐标偏移
- name: 横摆偏移，pitchOff
  summary: 横摆偏移 0（默认）| scalar
  group: 坐标偏移
```

### 选项

### **Suspension type** — 悬架类型 `Simple`（默认）| `User-defined`

使用 **Suspension type** 参数指定悬架类型。

| 设置 | 描述 |
| --- | --- |
| `Simple` | 模块将悬架力和力矩建模为弹簧-阻尼系统：  - 前叉上的悬架力 - 后摇臂上的悬架力矩 |
| `User-defined` | 输入悬架力和力矩：  - `FSuspF` – 前叉上的悬架力 - `MSuspR` – 后摇臂上的悬架力矩 |

#### 输入信号

### **External forces** — `FExt` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `FExt`。

### **External moments** — `MExt` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `MExt`。

### **External front wheel moment** — `MWhlF` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `MWhlF`。可考虑使用此端口输入外部力矩，例如轮毂电机和外部间歇性摩擦相关扰动。

### **External rear wheel moment** — `MWhlR` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `MWhlR`。可考虑使用此端口输入外部力矩，例如轮毂电机和外部间歇性摩擦相关扰动。

### **Grade angle** — `Grade` 输入端口 `on`（默认）| `off`

指定是否创建输入端口 `Grade`。

### **Wind velocity** — `WindXYZ` 输入端口 `on`（默认）| `off`

指定是否创建输入端口 `WindXYZ`。

### **Ambient temperature** — `Temp` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `Temp`。

### Layout

摩托车车身示意图

使用此表中的参数指定摩托车的几何布局。

| 参数 | | | 图中变量 |
| --- | --- | --- | --- |
| **初始条件** | **位置** | **后接地点纵向坐标，CpRrX0** | *OCpR* 相对于道路固定坐标系，沿 `x` |
| **后接地点垂向坐标，CpRrZ0** | *OCpR* 相对于道路固定坐标系，沿 `z` |
| **后摇臂俯仰角，ArmRrAng0** | *θra* |
| **主车架俯仰角，FrmAng0** | *θFrm* |
| **前叉长度，FrkFrL0** | *df* |
| **车架** | | **质心位置，FrmCmPxz** | *GFrm* 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| **长度，FrmLen** | *FrmLen* |
| **骑手** | | **质心位置，RdrCmPxz** | *GRdr* 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| **前叉** | **上部** | **位置，FrkUpCmPxz** | *GFrkUp* 相对于 *OFrkUp*，分别沿 *iFrkUp* 和 *kFrkUp* |
| **偏移量，FrkOfs** | *FrkOfs* |
| **下部** | **位置，FrkLwCmPxz** | *GFrkLw* 相对于 *OFrkLw*，分别沿 *iFrkLw* 和 *kFrkLw* |
| **后摇臂** | | **位置，ArmRrCmPxz** | *GArmRr* 相对于 *OArmRr*，分别沿 *iArmRr* 和 *kArmRr* |
| **长度，ArmRrLen** | *ArmRrLen* |
| **车轮** | **前轮** | **半径，WhlFrR** | *WhlFrR* |
| **后轮** | **半径，WhlRrR** | *WhlRrR* |
| **悬架** | **前悬架** | **平衡长度，FrkLwL0** | *df* |
| **后悬架** | **平衡角，ShkRrAng0** | *θFrm* |

#### 车架

### **质心位置，FrmCmPxz** — 车架位置 `[0.255, -0.02]`（默认）| `vector`

车架的质心位置，*GFrm*。指定为相对于 *OFrm* 的向量，分别沿 *iFrm* 和 *kFrm*。

### **质量，FrmMass** — 车架质量 `223`（默认）| `scalar`

车架质量，*FrmMass*，单位为 kg。

### **质量转动惯量，FrmIyy** — 车架转动惯量 `26.2`（默认）| `scalar`

质量转动惯量，*FrmIyy*，单位为 kg·m2。

### **长度，FrmLen** — 车架长度 `0.730`（默认）| `scalar`

车架长度，*FrmLen*，单位为 m。

#### 骑手

### **质心位置，RdrCmPxz** — 骑手位置 `[0.275, -0.61]`（默认）| `vector`

骑手的质心位置，*GRdr*。指定为相对于 *OFrm* 的向量，分别沿 *iFrm* 和 *kFrm*。

### **质量，RdrMass** — 骑手质量 `78`（默认）| `scalar`

骑手质量，*RdrMass*，单位为 kg。

### **质量转动惯量，RdrIyy** — 骑手转动惯量 `26.2`（默认）| `scalar`

骑手质量转动惯量，*RdrIyy*，单位为 kg·m2。

#### 前叉 – 上部

### **位置，FrkUpCmPxz** — 上部前叉位置 `[0.023, -0.098]`（默认）| `vector`

上部前叉的质心位置，*GFrkUp*。指定为相对于 *OFrkUp* 的向量，分别沿 *iFrkUp* 和 *kFrkUp*。

### **质量，FrkUpMass** — 上部前叉质量 `8.8`（默认）| `scalar`

上部前叉质量，*FrkUpMass*，单位为 kg。

### **质量转动惯量，FrkUpIyy** — 上部前叉转动惯量 `0.14`（默认）| `scalar`

上部前叉质量转动惯量，*FrkUpIyy*，单位为 kg·m2。

### **偏移量，FrkOfs** — 上部前叉偏移量 `0.034`（默认）| `scalar`

上部前叉偏移量，*FrkOfs*，单位为 m。

#### 前叉 – 下部

### **位置，FrkLwCmPxz** — 下部前叉位置 `[-0.029, -0.189]`（默认）| `vector`

下部前叉的质心位置，*GFrkLw*。指定为相对于 *OFrkLw* 的向量，分别沿 *iFrkLw* 和 *kFrkLw*。

### **质量，FrkLwMass** — 下部前叉质量 `7.0`（默认）| `scalar`

下部前叉质量，*FrkLwMass*，单位为 kg。

### **质量转动惯量，FrkLwIyy** — 下部前叉转动惯量 `0.18`（默认）| `scalar`

下部前叉质量转动惯量，*FrkLwIyy*，单位为 kg·m2。

#### 后摇臂

### **Position, ArmRrCmPxz** — 后臂位置 `[0.275, -0.052]`（默认）| `vector`

后臂质心位置，
*GArmRr*。指定为相对于 *OArmRr* 的向量，
分别沿 *iArmRr* 和
*kArmRr*。

### **Mass, ArmRrMass** — 后臂质量 `10`（默认）| `scalar`

后臂质量，*ArmRrMass*，单位为 kg。

### **Mass moment of inertia, ArmRrIyy** — 后臂转动惯量 `0.8`（默认）| `scalar`

后臂质量转动惯量，*ArmRrIyy*，单位为
kg·m2。

### **Length, ArmRrLen** — 后臂长度 `0.535`（默认）| `scalar`

后臂长度，*ArmRrLen*，单位为 m。

#### Wheels – Front

### **Mass, WhlFrMass** — 前轮质量 `12`（默认）| `scalar`

前轮质量，*WhlFrMass*，单位为 kg。

### **Radius, WhlFrR** — 前轮半径 `0.3`（默认）| `scalar`

前轮半径，*WhlFrR*，单位为 m。

#### Wheels – Rear

### **Mass, WhlRrMass** — 后轮质量 `16.2`（默认）| `scalar`

后轮质量，*WhlRrMass*，单位为 kg。

### **Radius, WhlRrR** — 后轮半径 `0.33`（默认）| `scalar`

后轮半径，*WhlRrR*，单位为 m。

#### Suspension – Front

### **Stiffness, SuspFrK** — 前悬架刚度 `25e3`（默认）| `scalar`

前悬架在
*OFrkUp* 处、沿
*kFrkUp* 的刚度，单位为 N/m。

### **Damping, SuspFrC** — 前悬架阻尼 `1250`（默认）| `scalar`

前悬架在
*OFrkUp* 处、沿
*kFrkUp* 的阻尼，单位为
N·s/m。

### **Equilibrium length, FrkLwL0** — 前悬架平衡长度 `0.473`（默认）| `scalar`

前悬架平衡长度，
*df*，单位为 m。

#### Suspension – Rear

### **Stiffness, SuspRrK** — 后臂悬架刚度 `1500`（默认）| `scalar`

后臂悬架在
*OArmRr* 处、绕
*jArmRr* 的刚度，单位为
N/rad。

### **Damping, SuspRrC** — 后臂悬架阻尼 `150`（默认）| `scalar`

后臂悬架在
*OArmRr* 处、绕
*jArmRr* 的阻尼，单位为
N·s/rad。

### **Equilibrium angle, ShkRrAng0** — 后悬架平衡角 `0`（默认）| `scalar`

后悬架平衡角，
*θFrm*，单位为 rad。

### Aerodynamic

### **Longitudinal drag area, Af** — 面积 `2`（默认）| `scalar`

用于计算车辆气动阻力的有效车辆横截面积，
*Af*，单位为
m2。

### **Longitudinal drag coefficient, Cd** — 阻力 `.2`（默认）| `scalar`

空气阻力系数，*Cd*，
无量纲。

### **Longitudinal lift coefficient, Cl** — 升力 `.1`（默认）| `scalar`

空气升力系数，*Cl*，
无量纲。

### **Longitudinal drag pitch moment, Cpm** — 俯仰阻力 `.1`（默认）| `scalar`

纵向阻力俯仰力矩系数，
*Cpm*，
无量纲。

### **Pitch moment length, Lcpm** — 俯仰阻力 `2`（默认）| `scalar`

俯仰力矩长度，*Lcpm*，单位为 m。

### Environment

### **Gravitational acceleration, g** — 重力 `9.80665`（默认）| `scalar`

重力加速度，*g*，单位为
m/s2。

### **Absolute air pressure, Pabs** — 压力 `101325`（默认）| `scalar`

环境空气绝对压力，*Pabs*，
单位为 Pa。

### **Air temperature, Tair** — 环境空气温度 `273`（默认）| `scalar`

环境空气温度，
*Tair*，单位为 K。

#### 依赖关系

要启用此参数，请清除 **Ambient
temperature**。

### Initial conditions

#### Position

### **Rear contact patch longitudinal coordinate, CpRrX0** — 纵向坐标 `0`（默认）| `scalar`

后接地点纵向坐标，
*OCpR*，相对于道路固定坐标系，沿 `x`，单位为 m。

### **Rear contact patch vertical coordinate, CpRrZ0** — 垂直坐标 `0`（默认）| `scalar`

后接地点垂直坐标，
*OCpR*，相对于道路固定坐标系，沿 `z`，单位为 m。

### **Pitch angle of rear arm, ArmRrAng0** — 后臂角度 `0.0590379`（默认）| `scalar`

后臂俯仰角，
*θra*，单位为 rad。

### **Pitch angle of main frame, FrmAng0** — 角度长度 `0.377024`（默认）| `scalar`

主车架俯仰角，
*θFrm*，单位为 rad。

### **Fork length, FrkFrL0** — 前叉长度 `0.4262193`（默认）| `scalar`

前叉长度，*df*，单位为 m。

#### 速度

### **后接触印迹纵向速度** — 纵向速度 `0`（默认）| `scalar`

后接触印迹纵向坐标，O˙CpR，相对于道路固定坐标系，沿 `x` 方向，单位为 m/s。

### **后接触印迹垂直速度，CpRrVz0** — 垂直速度 `0`（默认）| `scalar`

后接触印迹垂直速度，O˙CpR，相对于道路固定坐标系，沿 `z` 方向，单位为 m/s。

### **后摇臂俯仰角速度，ArmRrAngV0** — 俯仰角速度 `0`（默认）| `scalar`

后摇臂俯仰角速度，θ˙ra，单位为 rad/s。

### **主车架俯仰角速度，FrmAngV0** — 俯仰角速度 `0`（默认）| `scalar`

主车架俯仰角速度，θ˙Frm，单位为 rad/s。

### **下前叉变形速度，FrkLwV0** — 变形速度 `0`（默认）| `scalar`

下前叉变形速度，d˙f，单位为 m/s。

### 坐标偏移

### **纵向偏移，longOff** — 纵向偏移 `0`（默认）| `scalar`

车辆主车架沿大地固定 *X* 轴的偏移，单位为 m。

### **横向偏移，latOff** — 横向偏移 `0`（默认）| `scalar`

车辆主车架沿大地固定 *Y* 轴的偏移，单位为 m。

### **垂直偏移，vertOff** — 垂直偏移 `0`（默认）| `scalar`

车辆主车架沿大地固定 *Z* 轴的偏移，单位为 m。

### **侧倾偏移，pitchOff** — 侧倾偏移 `0`（默认）| `scalar`

车辆主车架绕大地固定 *X* 轴的偏移，单位为 rad。

### **俯仰偏移，pitchOff** — 俯仰偏移 `0`（默认）| `scalar`

车辆主车架绕大地固定 *Y* 轴的偏移，单位为 rad。

### **横摆偏移，pitchOff** — 横摆偏移 `0`（默认）| `scalar`

车辆主车架绕大地固定 *Z* 轴的偏移，单位为 rad。
## 所属库

Powertrain Blockset / Vehicle Dynamics Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

摩托车纵向平面内车辆运动

Motorcycle Body Longitudinal In-Plane 模块实现摩托车车身纵向平面内模型，用于计算纵向、垂直和俯仰运动。该模块考虑：

- 车架、后摇臂、上前叉、下前叉、前轮和后轮的质量
- 车架、下前叉、前轮、后轮、后悬架、前悬架、后轮阻尼器、后摇臂和链条的平面内动态效应
- 外部力、外部力矩和气动阻力
- 道路坡度
- 由于加速度引起的轴间重量分布

考虑使用此模块来表示动力总成和燃油经济性研究中的摩托车运动，例如，在包含重制动或加速或包含较大垂直变化的道路剖面的研究中。

该模块使用刚体车辆运动、悬架系统力以及风力和阻力来计算摩托车车架上的力。然后该模块确定摩托车在前接触印迹和后接触印迹处的位置和速度。

### 布局

为确定刚体摩托车运动，该模块使用附着于摩托车的右手（RH）*笛卡尔*参考坐标系。*i*、*j* 和 *k* 是附着于坐标系的相互正交单位向量。

摩托车车身示意图

| 坐标系 | 图中变量 | 描述 |
| --- | --- | --- |
| 道路 | *x*、*z* | 道路固定坐标系。*x* 沿道路坡度方向，*z* 指向下方。 |
| 摩托车主车架  - *iFrm* – 沿由 *θfrm* 给出的向量向前 - *kFrm* – 向下 - *jFrm* – 正交于摩托车平面 | *OFrm* | 主车架原点 |
| *GFrm* | 主车架质心（CM）相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| *GRdr* | 骑手质心相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| *ϴfrm* | 主车架绕 *jFrm* 的旋转 |
| 上前叉  - *iFrkUp* – 沿由 *θfrm* 给出的向量向前 - *kFrkUp* – 向下 - *jFrkUp* – 正交于摩托车平面 | *OFrkUp* | 上前叉原点 |
| *GFrkUp* | 上前叉质心相对于 *OFrkUp*，分别沿 *iFrkUp* 和 *kFrkUp* |
| 下前叉  - *iFrkLw* – 沿由 *θfrm* 给出的向量向前 - *kFrkLw* – 向下 - *jFrkLw* – 正交于摩托车平面 | *OFrkLw* | 下前叉原点 |
| *GFrkLw* | 下前叉质心相对于 *OFrkLw*，分别沿 *iFrkLw* 和 *kFrkLw* |
| 后摇臂  - *iArmRr* – 沿由 *θra* 给出的向量向前 - *kArmRr* – 向下 - *jArmRr* – 正交于摩托车平面 | *OArmRr* | 后摇臂原点 |
| *GArmRr* | 后摇臂质心相对于 *OArmRr*，分别沿 *iArmRr* 和 *kArmRr* |
| *ϴra* | 后摇臂绕 *jArmRr* 的旋转 |
| 前轮接地点  - *iCpF* – 沿由道路固定 *x* 轴给出的向量向前 - *kCpF* – 沿由道路固定 *z* 轴给出的向量向下 - *jCpF* – 正交于摩托车平面 | *OCpF* | 前轮接地点原点 |
| 后轮接地点  - *iCpR* – 沿由道路固定 *x* 轴给出的向量向前 - *kCpR* – 沿由道路固定 *z* 轴给出的向量向下 - *jCpR* – 正交于摩托车平面 | *OCpR* | 后轮接地点原点 |

使用此表中的参数来指定摩托车的几何布局。

| 参数 | | | 图中变量 |
| --- | --- | --- | --- |
| **初始条件** | **位置** | **后接地点纵向坐标，CpRrX0** | *OCpR* 相对于道路固定坐标系，沿 `x` |
| **后接地点垂直坐标，CpRrZ0** | *OCpR* 相对于道路固定坐标系，沿 `z` |
| **后摇臂俯仰角，ArmRrAng0** | *θra* |
| **主车架俯仰角，FrmAng0** | *θFrm* |
| **前叉长度，FrkFrL0** | *df* |
| **车架** | | **质心位置，FrmCmPxz** | *GFrm* 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| **长度，FrmLen** | *FrmLen* |
| **骑手** | | **质心位置，RdrCmPxz** | *GRdr* 相对于 *OFrm*，分别沿 *iFrm* 和 *kFrm* |
| **前叉** | **上部** | **位置，FrkUpCmPxz** | *GFrkUp* 相对于 *OFrkUp*，分别沿 *iFrkUp* 和 *kFrkUp* |
| **偏移量，FrkOfs** | *FrkOfs* |
| **下部** | **位置，FrkLwCmPxz** | *GFrkLw* 相对于 *OFrkLw*，分别沿 *iFrkLw* 和 *kFrkLw* |
| **后摇臂** | | **位置，ArmRrCmPxz** | *GArmRr* 相对于 *OArmRr*，分别沿 *iArmRr* 和 *kArmRr* |
| **长度，ArmRrLen** | *ArmRrLen* |
| **车轮** | **前轮** | **半径，WhlFrR** | *WhlFrR* |
| **后轮** | **半径，WhlRrR** | *WhlRrR* |
| **悬架** | **前悬架** | **平衡长度，FrkLwL0** | *df* |
| **后悬架** | **平衡角，ShkRrAng0** | *θFrm* |

### 输入信号

您可以使用这些模块参数创建额外的输入端口。下表总结了相关设置。

| 输入信号窗格参数 | 输入端口 | 描述 |
| --- | --- | --- |
| **External forces** | `FExt` | 施加在等效骑手和摩托车质心（CM）处的纵向和垂向外力。 |
| **External moments** | `MExt` | 绕等效骑手和摩托车质心的外力矩，例如由骑手身体运动产生的力矩。 |
| **External front wheel moment** | `MWhlF` | 前轮 *GWhlFr* 处的外力矩，例如轮毂电机和外部间歇性摩擦相关扰动。 |
| **External rear wheel moment** | `MWhlR` | 后轮 *GWhlRr* 处的外力矩，例如轮毂电机和外部间歇性摩擦相关扰动。 |
| **Grade angle** | `Grade` | 道路坡度角。 |
| **Wind velocity** | `WindXYZ` | 风速。 |
| **Ambient temperature** | `Temp` | 环境空气温度。如果您希望在运行时改变温度，请考虑此选项。 |

### 悬架系统

使用 **Suspension type** 参数指定悬架类型。

| 设置 | 描述 |
| --- | --- |
| `Simple` | 模块将悬架力和力矩建模为弹簧-阻尼器系统：  - 上叉处的悬架力 - 后臂处的悬架力矩 |
| `User-defined` | 输入悬架力和力矩：  - `FSuspF` – 上叉处的悬架力 - `MSuspR` – 后臂处的悬架力矩 |

### 风力和阻力

模块从车辆速度分量中减去风速，以获得净相对空速。为了计算作用在摩托车上的阻力和力矩，模块使用净相对空速。

### 在 3D 环境中使用

要在 Unreal Engine® 中进行联合仿真，并为摩托车提供由 Motorcycle Body Longitudinal In-Plane 模块计算的运动：

1. 将 Simulation 3D Motorcycle 模块放入您的模型中。
2. 将这些 Info 总线端口信号连接到 Simulation 3D Motorcycle 输入端口 Translation 和 Rotation。

   - `PosOrgInert`
   - `PosFwBdy`
   - `PosRwBdy`
   - `AngOrgInert`

   图 Simulation 3D Motorcycle 模块输入

有关在 3D 环境中使用该模块的更多信息，请参阅 Longitudinal Motorcycle Braking Test。

### 功率核算

模块核算传输的、未传输的和存储的功率。

| 总线信号 | | | 描述 |
| --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrFxExt` | 来自纵向外力的机械功率 |
| `PwrFzExt` | 来自垂向外力的机械功率 |
| `PwrMyExt` | 来自外部俯仰力矩的机械功率 |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFxDrag` | 来自纵向阻力的机械功率损失 |
| `PwrFzDrag` | 来自垂直升力的机械功率损失 |
| `PwrMyDrag` | 来自俯仰力矩阻力的机械功率损失 |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredGrvty` | 重力势能的变化率 |
| `PwrStoredxdot` | 纵向动能的变化率 |
| `PwrStoredzdot` | 垂直动能的变化率 |
| `PwrStoredq` | 旋转俯仰动能的变化率 |
| `PwrStoredFsFzSprng` | 前悬架存储的弹簧能量 |
| `PwrStoredFsRzSprng` | 后悬架存储的弹簧能量 |
