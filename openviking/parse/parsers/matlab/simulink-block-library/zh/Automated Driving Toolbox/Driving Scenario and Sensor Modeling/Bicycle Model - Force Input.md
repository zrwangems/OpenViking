---
type: simulink-block
title: 'Bicycle Model'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'bicyclemodel'
documentation_source_path: 'ref/bicyclemodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Bicycle Model

## 端口

### 输入

### **WhlAngF** — 车轮转角 `scalar`

前轮转角，单位为 rad。

### **FxF** — 力输入：前轴总纵向力 `scalar`

前轴上的纵向力，
*FxF*，沿
车辆固定 `x` 轴方向，单位为 N。

Bicycle Model - Force Input 模块输入端口。

### **FxR** — 力输入：后轴总纵向力 `scalar`

后轴上的纵向力，
*FxR*，沿
车辆固定 `x` 轴方向，单位为 N。

Bicycle Model - Force Input 模块输入端口。

### **xdotin** — 速度输入：纵向速度 `scalar`

车辆质心沿车辆固定 *x* 轴方向的速度，
单位为 m/s。

Bicycle Model - Velocity Input 模块输入端口。
### 输出

### **Info** — 总线信号 bus

包含以下模块值的总线信号。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆质心沿地面固定 *X* 轴的位移 | 计算值 | m |
| `Y` | | | 车辆质心沿地面固定 *Y* 轴的位移 | 计算值 | m |
| `Z` | | | 车辆质心沿地面固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 车辆质心沿地面固定 *X* 轴的速度 | 计算值 | m/s |
| `Ydot` | | | 车辆质心沿地面固定 *Y* 轴的速度 | 计算值 | m/s |
| `Zdot` | | | 车辆质心沿地面固定 *Z* 轴的速度 | `0` | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕地面固定 *X* 轴的旋转（侧倾） | `0` | rad |
| `theta` | | | 车辆固定坐标系绕地面固定 *Y* 轴的旋转（俯仰） | `0` | rad |
| `psi` | | | 车辆固定坐标系绕地面固定 *Z* 轴的旋转（横摆） | 计算值 | rad |
| `FrntAxl` | `Disp` | `X` | | | 前轮沿地面固定 *X* 轴的位移 | 计算值 | m |
| `Y` | | | 前轮沿地面固定 *Y* 轴的位移 | 计算值 | m |
| `Z` | | | 前轮沿地面固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 前轮沿地面固定 *X* 轴的速度 | 计算值 | m/s |
| `Ydot` | | | 前轮沿地面固定 *Y* 轴的速度 | 计算值 | m/s |
| `Zdot` | | | 前轮沿地面固定 *Z* 轴的速度 | `0` | m/s |
| `RearAxl` | `Disp` | `X` | | | 后轮沿地面固定 *X* 轴的位移 | 计算值 | m |
| `Y` | | | 后轮沿地面固定 *Y* 轴的位移 | 计算值 | m |
| `Z` | | | 后轮沿地面固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 后轮沿地面固定 *X* 轴的速度 | 计算值 | m/s |
| `Ydot` | | | 后轮沿地面固定 *Y* 轴的速度 | 计算值 | m/s |
| `Zdot` | | | 后轮沿地面固定 *Z* 轴的速度 | `0` | m/s |
| `Hitch` | `Disp` | `X` | | | 牵引点沿地面固定 *X* 轴方向相对车轴平面的偏移 | 计算值 | m |
| `Y` | | | 牵引点沿地面固定 *Y* 轴方向相对中心平面的偏移 | 计算值 | m |
| `Z` | | | 牵引点沿地面固定 *Z* 轴方向相对车轴平面的偏移 | 计算值 | m |
| `Vel` | `Xdot` | | | 牵引点沿地面固定 *X* 轴方向相对车轴平面的偏移速度 | 计算值 | m |
| `Ydot` | | | 牵引点沿地面固定 *Y* 轴方向相对中心平面的偏移速度 | 计算值 | m |
| `Zdot` | | | 牵引点沿地面固定 *Z* 轴方向相对车轴平面的偏移速度 | 计算值 | m |
| `Geom` | `Disp` | `X` | | | 车辆底盘沿地面固定 *X* 轴方向相对车轴平面的偏移 | 计算值 | m |
| `Y` | | | 车辆底盘沿地面固定 *Y* 轴方向相对中心平面的偏移 | 计算值 | m |
| `Z` | | | 车辆底盘沿地面固定 *Z* 轴方向相对车轴平面的偏移 | 计算值 | m |
| `Vel` | `Xdot` | | | 车辆底盘沿地面固定 *X* 轴方向的偏移速度 | 计算值 | m/s |
| `Ydot` | | | 车辆底盘沿地面固定 *Y* 轴方向的偏移速度 | 计算值 | m/s |
| `Zdot` | | | 车辆底盘沿地面固定 *Z* 轴方向的偏移速度 | 计算值 | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | 车辆质心沿车辆固定 *x* 轴方向的速度 | 计算值 | m/s |
| `ydot` | | | 车辆质心沿车辆固定 *y* 轴方向的速度 | 计算值 | m/s |
| `zdot` | | | 车辆质心沿车辆固定 *z* 轴方向的速度 | `0` | m/s |
| `Ang` | `Beta` | | | 车身侧偏角，*β*    β=VyVx | 计算值 | rad |
| `AngVel` | `p` | | | 车辆绕车辆固定 *x* 轴的角速度（侧倾角速度） | `0` | rad/s |
| `q` | | | 车辆绕车辆固定 *y* 轴的角速度（俯仰角速度） | `0` | rad/s |
| `r` | | | 车辆绕车辆固定 *z* 轴的角速度（横摆角速度） | 计算值 | rad/s |
| `Acc` | `ax` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | 计算值 | gn |
| `ay` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | 计算值 | gn |
| `az` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | gn |
| `xddot` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | 计算值 | m/s^2 |
| `yddot` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | 计算值 | m/s^2 |
| `zddot` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | m/s^2 |
| `AngAcc` | `pdot` | | | 车辆绕车辆固定 *x* 轴的角加速度 | `0` | rad/s |
| `qdot` | | | 车辆绕车辆固定 *y* 轴的角加速度 | `0` | rad/s |
| `rdot` | | | 车辆绕车辆固定 *z* 轴的角加速度 | 计算值 | rad/s |
| `DCM` | 方向余弦矩阵 | | | | 计算值 | rad |
| `Forces` | `Body` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴方向的合力 | 计算值 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴方向的合力 | 计算值 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴方向的合力 | `0` | N |
| `Ext` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴方向的外力 | 计算值 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴方向的外力 | 计算值 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴方向的外力 | `0` | N |
| `Hitch` | `Fx` | | | 在牵引点位置施加到车身上的牵引力，沿车辆固定 *x* 轴方向 | 输入 | N |
| `Fy` | | | 在牵引点位置施加到车身上的牵引力，沿车辆固定 *y* 轴方向 | 输入 | N |
| `Fz` | | | 在牵引点位置施加到车身上的牵引力，沿车辆固定 *z* 轴方向 | 输入 | N |
| `FrntAxl` | `Fx` | | | 前轮上的纵向力，沿车辆固定 *x* 轴方向 | 计算值 | N |
| `Fy` | | | 前轮上的侧向力，沿车辆固定 *y* 轴方向 | 计算值 | N |
| `Fz` | | | 前轮上的法向力，沿车辆固定 *z* 轴方向 | 计算值 | N |
| `RearAxl` | `Fx` | | | 后轮上的纵向力，沿车辆固定 *x* 轴方向 | 计算值 | N |
| `Fy` | | | 后轮上的侧向力，沿车辆固定 *y* 轴方向 | 计算值 | N |
| `Fz` | | | 后轮上的法向力，沿车辆固定 *z* 轴方向 | 计算值 | N |
| `Tires` | `FrntTire` | `Fx` | | 前轮胎力，沿车辆固定 *x* 轴方向 | 计算值 | N |
| `Fy` | | 前轮胎力，沿车辆固定 *y* 轴方向 | 计算值 | N |
| `Fz` | | 前轮胎力，沿车辆固定 *z* 轴方向 | 计算值 | N |
| `RearTire` | `Fx``Fx` | | 后轮胎力，沿车辆固定 *x* 轴方向 | 计算值 | N |
| `Fy` | | 后轮胎力，沿车辆固定 *y* 轴方向 | 计算值 | N |
| `Fz` | | 后轮胎力，沿车辆固定 *z* 轴方向 | 计算值 | N |
| `Drag` | `Fx` | | | 车辆质心上的阻力，沿车辆固定 *x* 轴方向 | 计算值 | N |
| `Fy` | | | 车辆质心上的阻力，沿车辆固定 *y* 轴方向 | 计算值 | N |
| `Fz` | | | 车辆质心上的阻力，沿车辆固定 *z* 轴方向 | 计算值 | N |
| `Grvty` | `Fx` | | | 车辆质心上的重力，沿车辆固定 *x* 轴方向 | 计算值 | N |
| `Fy` | | | 车辆质心上的重力，沿车辆固定 *y* 轴方向 | 计算值 | N |
| `Fz` | | | 车辆质心上的重力，沿车辆固定 *z* 轴方向 | 计算值 | N |
| `Moments` | `Body` | `Mx` | | | 车辆质心上绕车辆固定 *x* 轴的车身力矩 | `0` | N·m |
| `My` | | | 车辆质心上绕车辆固定 *y* 轴的车身力矩 | 计算值 | N·m |
| `Mz` | | | 车辆质心上绕车辆固定 *z* 轴的车身力矩 | `0` | N·m |
| `Drag` | `Mx` | | | 车辆质心上绕车辆固定 *x* 轴的阻力力矩 | `0` | N·m |
| `My` | | | 车辆质心上绕车辆固定 *y* 轴的阻力力矩 | 计算值 | N·m |
| `Mz` | | | 车辆质心上绕车辆固定 *z* 轴的阻力力矩 | `0` | N·m |
| `Ext` | `Mx` | | | 车辆质心上绕车辆固定 *x* 轴的外力矩 | `0` | N·m |
| `My` | | | 车辆质心上绕车辆固定 *y* 轴的外力矩 | 计算值 | N·m |
| `Mz` | | | 车辆质心上绕车辆固定 *z* 轴的外力矩 | `0` | N·m |
| `Hitch` | `Mx` | | | 牵引点处绕车辆固定 *x* 轴的牵引力矩 | `0` | N·m |
| `My` | | | 牵引点处绕车辆固定 *y* 轴的牵引力矩 | 计算值 | N·m |
| `Mz` | | | 牵引点处绕车辆固定 *z* 轴的牵引力矩 | `0` | N·m |
| `FrntAxl` | `Disp` | `x` | | | 前轮沿车辆固定 *x* 轴的位移 | 计算值 | m |
| `y` | | | 前轮沿车辆固定 *y* 轴的位移 | 计算值 | m |
| `z` | | | 前轮沿车辆固定 *z* 轴的位移 | 计算值 | m |
| `Vel` | `xdot` | | | 前轮沿车辆固定 *x* 轴的速度 | 计算值 | m/s |
| `ydot` | | | 前轮沿车辆固定 *y* 轴的速度 | 计算值 | m/s |
| `zdot` | | | 前轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngFL` | | | 前左轮转向角 | 计算值 | rad |
| `WhlAngFR` | | | 前右轮转向角 | 计算值 | rad |
| `RearAxl` | `Disp` | `x` | | | 后轮沿车辆固定 *x* 轴的位移 | 计算值 | m |
| `y` | | | 后轮沿车辆固定 *y* 轴的位移 | 计算值 | m |
| `z` | | | 后轮沿车辆固定 *z* 轴的位移 | 计算值 | m |
| `Vel` | `xdot` | | | 后轮沿车辆固定 *x* 轴的速度 | 计算值 | m/s |
| `ydot` | | | 后轮沿车辆固定 *y* 轴的速度 | 计算值 | m/s |
| `zdot` | | | 后轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 后左轮转向角 | 计算值 | rad |
| `WhlAngRR` | | | 后右轮转向角 | 计算值 | rad |
| `Hitch` | `Disp` | | `x` | | 牵引点沿车辆固定 *x* 轴方向相对车轴平面的偏移 | 输入 | m |
| `y` | | 牵引点沿车辆固定 *y* 轴方向相对中心平面的偏移 | 输入 | m |
| `z` | | 牵引点沿地面固定 *z* 轴方向相对车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 牵引点沿车辆固定 *x* 轴方向的偏移速度 | 计算值 | m/s |
| `ydot` | | 牵引点沿车辆固定 *y* 轴方向的偏移速度 | 计算值 | m/s |
| `zdot` | | 牵引点沿车辆固定 *z* 轴方向的偏移速度 | 计算值 | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | 计算值 | W |
| `Hitch` | | | | 牵引引起的功率损失 | 计算值 | W |
| `Drag` | | | | 阻力引起的功率损失 | 计算值 | W |
| `Geom` | `Disp` | | `x` | | 车辆底盘沿车辆固定 *x* 轴方向相对车轴平面的偏移 | 输入 | m |
| `y` | | 车辆底盘沿车辆固定 *y* 轴方向相对中心平面的偏移 | 输入 | m |
| `z` | | 车辆底盘沿地面固定 *z* 轴方向相对车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 车辆底盘沿车辆固定 *x* 轴方向的偏移速度 | 计算值 | m/s |
| `ydot` | | 车辆底盘沿车辆固定 *y* 轴方向的偏移速度 | 计算值 | m/s |
| `zdot` | | 车辆底盘沿车辆固定 *z* 轴方向的偏移速度 | `0` | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | 计算值 | rad |

| 信号 | | | 描述 | | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | 外部施加的纵向力功率 | | 计算值 | W |
| `PwrFyExt` | 外部施加的侧向力功率 | | 计算值 | W |
| `PwrMzExt` | 外部施加的侧倾力矩功率 | | 计算值 | W |
| `PwrFwFx` | 施加在前轴上的纵向力功率 | | 计算值 | W |
| `PwrFwFy` | 施加在前轴上的侧向力功率 | | 计算值 | W |
| `PwrFwRx` | 施加在后轴上的纵向力功率 | | 计算值 | W |
| `PwrFwRy` | 施加在后轴上的侧向力功率 | | 计算值 | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | 纵向阻力功率 | | 计算值 | W |
| `PwrFyDrag` | 侧向阻力功率 | | 计算值 | W |
| `PwrMzDrag` | 阻力俯仰力矩功率 | | 计算值 | W |
| `PwrStored` | `PwrStoredGrvty` | 重力势能变化率 | | 计算值 | W |
| `PwrStoredxdot` | 纵向动能变化率 | | 计算值 | W |
| `PwrStoredydot` | 侧向动能变化率 | | 计算值 | W |
| `PwrStoredr` | 横摆转动动能变化率 | | 计算值 | W |

### **xdot** — 车身纵向速度 `scalar`

车辆质心沿车辆固定 `x` 轴方向的速度，单位为
m/s。

### **ydot** — 车身侧向速度 `scalar`

车辆质心沿车辆固定 `y` 轴方向的速度，单位为
m/s。

### **psi** — 横摆 `scalar`

车辆固定坐标系绕地面固定
`Z` 轴的旋转（横摆），单位为 rad。

### **r** — 横摆角速度 `scalar`

车辆绕车辆固定 `z` 轴的角速度 `r`（横摆角速度），单位为 rad/s。

## 参数

#### 纵向

### **Number of wheels on front axle, NF** — 前轮数量 `2` (default) | `scalar`

前轴上的车轮数量，
*NF*。该值
无量纲。

### **Number of wheels on rear axle, NR** — 后轮数量 `2` (default) | `scalar`

后轴上的车轮数量，
*NR*。该值
无量纲。

### **Vehicle mass, m** — 车辆质量 `2000` (default) | `scalar`

车辆质量，*m*，单位为 kg。

### **Longitudinal distance from center of mass to front axle, a** — 前轴距离 `1.4` (default) | `scalar`

从车辆质心到前轮轴的水平距离 *a*，单位为 m。

### **Longitudinal distance from center of mass to rear axle, b** — 后轴距离 `1.6` (default) | `scalar`

从车辆质心到后轮轴的水平距离 *b*，单位为 m。

### **Vertical distance from center of mass to axle plane, h** — 高度 `0.35` (default) | `scalar`

车辆质心高于车轴的高度，*h*，单位为 m。

### **Initial inertial frame longitudinal position, X\_o** — 位置 `0` (default) | `scalar`

车辆质心沿地面固定
*X* 轴的初始位移，单位为 m。

### **Initial longitudinal velocity, xdot\_o** — 速度 `0` (default) | `scalar`

车辆质心沿车辆固定
*x* 轴的初始速度，单位为 m/s。

#### 侧向

### **Front tire corner stiffness, Cy\_f** — 刚度 `12e3` (default) | `scalar`

前轮胎侧偏刚度，
*Cyf*，单位为 N/rad。

### **Rear tire corner stiffness, Cy\_r** — 刚度 `11e3` (default) | `scalar`

后轮胎侧偏刚度，*Cyr*，
单位为 N/rad。

### **Initial inertial frame lateral displacement, Y\_o** — 位置 `0` (default) | `scalar`

车辆质心沿地面固定
*Y* 轴的初始位移，单位为 m。

### **Initial lateral velocity, ydot\_o** — 速度 `0` (default) | `scalar`

车辆质心沿车辆固定
*y* 轴的初始速度，单位为 m/s。

#### 横摆

### **Yaw polar inertia, Izz** — 惯量 `4000` (default) | `scalar`

横摆极惯量，单位为 kg\*m^2。

### **Initial yaw angle, psi\_o** — Psi 旋转 `0` (default) | `scalar`

车辆固定坐标系绕地面固定 *Z* 轴的旋转
（横摆），单位为 rad。

### **Initial yaw rate, r\_o** — 横摆角速度 `0`（默认）| `scalar`

车辆绕车辆固定 *z* 轴的角速度（横摆角速度），单位为 rad/s。

#### 空气动力学

### **Longitudinal drag area, Af** — 有效车辆迎风面积 `2`（默认）| `scalar`

有效车辆迎风面积 *Af*，用于计算车辆所受气动阻力，单位为 m2。

### **Longitudinal drag coefficient, Cd** — 空气阻力系数 `.3`（默认）| `scalar`

空气阻力系数 *Cd*。该值无量纲。

### **Longitudinal lift coefficient, Cl** — 空气升力系数 `.1`（默认）| `scalar`

空气升力系数 *Cl*。该值无量纲。

### **Longitudinal drag pitch moment, Cpm** — 俯仰阻力 `.1`（默认）| `scalar`

纵向阻力俯仰力矩系数 *Cpm*。该值无量纲。

### **Relative wind angle vector, beta\_w** — 风角 `[0:0.01:0.3]`（默认）| `vector`

相对风角向量 *βw*，单位为 rad。

### **Side force coefficient vector, Cs** — 侧向力系数 `[0:0.03:0.9]`（默认）| `vector`

侧向力系数向量系数 *Cs*。该值无量纲。

### **Yaw moment coefficient vector, Cym** — 横摆力矩阻力 `[0:0.01:0.3]`（默认）| `vector`

横摆力矩系数向量 *Cym*。该值无量纲。

#### 环境

### **Absolute pressure, Pabs** — 压力 `101325`（默认）| `scalar` | `scalar`

环境绝对压力 *Pabs*，单位为 Pa。

### **Air temperature, Tair** — 温度 `273`（默认）| `scalar`

环境绝对温度 *T*，单位为 K。

### **Gravitational acceleration, g** — 重力 `9.81`（默认）| `scalar`

重力加速度 *g*，单位为 m/s^2。

### **Nominal friction scaling factor, mu** — 摩擦比例因子 `1`（默认）| `scalar`

标称摩擦比例因子 *μ*。该值无量纲。

#### 仿真

### **Longitudinal velocity tolerance, xdot\_tol** — 容差 `.01`（默认）| `scalar`

纵向速度容差，单位为 m/s。

### **Nominal normal force, Fznom** — 法向力 `5000`（默认）| `scalar`

标称法向力，单位为 N。

### **Geometric longitudinal offset from axle plane, longOff** — 纵向偏移 `0`（默认）| `scalar`

车辆底盘沿车身固定 *x* 轴距车轴平面的偏移，单位为 m。使用 3D 可视化引擎时，可考虑使用该偏移将底盘定位为独立于车辆 CG。

### **Geometric lateral offset from center plane, latOff** — 侧向偏移 `0`（默认）| `scalar`

车辆底盘沿车身固定 *y* 轴距中心平面的偏移，单位为 m。使用 3D 可视化引擎时，可考虑使用该偏移将底盘定位为独立于车辆 CG。

### **Geometric vertical offset from axle plane, vertOff** — 垂直偏移 `0`（默认）| `scalar`

车辆底盘沿车身固定 *z* 轴距车轴平面的偏移，单位为 m。使用 3D 可视化引擎时，可考虑使用该偏移将底盘定位为独立于车辆 CG。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Bicycle Model 模块仿真模型需要 Simulink 3D Animation。

## 描述

实现单轨 3DOF 刚体车辆车身，以计算纵向、侧向和横摆运动

**注意**

使用 Bicycle Model 模块仿真模型需要 Simulink® 3D Animation™。

Bicycle Model 模块实现刚性双轴单轨车辆车身模型，以计算纵向、侧向和横摆运动。该模块考虑车身质量、气动阻力以及由于加速度和转向引起的轴间重量分布。Bicycle Model 模块有两种类型。

| 模块 | 实现 |
| --- | --- |
| Bicycle Model - Velocity Input带速度输入端口 WhlAngF 和 xdotin 的 Bicycle model 模块。 | - 模块假设外部纵向速度为准稳态，因此纵向加速度近似为零。 - 由于运动为准稳态，模块仅使用轮胎侧偏角和线性侧偏刚度计算侧向力。 |
| Bicycle Model - Force Input带力输入端口 WhlAngF、FxF 和 FxR 的 Bicycle model 模块。 | - 模块使用外部纵向力使车辆加速或制动。 - 模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 |

为计算前轴和后轴上的法向力，该模块使用刚体车辆运动、悬架系统力以及风力和阻力。该模块在刚性车辆车身坐标系上求解力和力矩分量。
