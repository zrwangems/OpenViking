---
type: simulink-block
title: 'Bicycle Model'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'bicyclemodel'
documentation_source_path: 'ref/bicyclemodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Bicycle Model

## 端口
```yaml
ports:
- name: WhlAngF
  summary: 车轮转角 scalar
  direction: input
- name: FxF
  summary: 力输入：前轴总纵向力 scalar
  direction: input
- name: FxR
  summary: 力输入：后轴总纵向力 scalar
  direction: input
- name: xdotin
  summary: 速度输入：纵向速度 scalar
  direction: input
- name: Info
  summary: 总线信号总线
  direction: output
- name: xdot
  summary: 车身纵向速度 scalar
  direction: output
- name: ydot
  summary: 车身横向速度 scalar
  direction: output
- name: psi
  summary: 横摆 scalar
  direction: output
- name: r
  summary: 横摆角速度 scalar
  direction: output
```

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

### **Info** — 总线信号总线

包含这些模块值的总线信号。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆 CG 沿 earth-fixed *X* 轴的位移 | 计算所得 | m |
| `Y` | | | 车辆 CG 沿 earth-fixed *Y* 轴的位移 | 计算所得 | m |
| `Z` | | | 车辆 CG 沿 earth-fixed *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 车辆 CG 沿 earth-fixed *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | | 车辆 CG 沿 earth-fixed *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | | 车辆 CG 沿 earth-fixed *Z* 轴的速度 | `0` | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕 earth-fixed *X* 轴的旋转（横滚） | `0` | rad |
| `theta` | | | 车辆固定坐标系绕 earth-fixed *Y* 轴的旋转（俯仰） | `0` | rad |
| `psi` | | | 车辆固定坐标系绕 earth-fixed *Z* 轴的旋转（横摆） | 计算所得 | rad |
| `FrntAxl` | `Disp` | `X` | | | 前轮沿 earth-fixed *X* 轴的位移 | 计算所得 | m |
| `Y` | | | 前轮沿 earth-fixed *Y* 轴的位移 | 计算所得 | m |
| `Z` | | | 前轮沿 earth-fixed *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 前轮沿 earth-fixed *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | | 前轮沿 earth-fixed *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | | 前轮沿 earth-fixed *Z* 轴的速度 | `0` | m/s |
| `RearAxl` | `Disp` | `X` | | | 后轮沿 earth-fixed *X* 轴的位移 | 计算所得 | m |
| `Y` | | | 后轮沿 earth-fixed *Y* 轴的位移 | 计算所得 | m |
| `Z` | | | 后轮沿 earth-fixed *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 后轮沿 earth-fixed *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | | 后轮沿 earth-fixed *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | | 后轮沿 earth-fixed *Z* 轴的速度 | `0` | m/s |
| `Hitch` | `Disp` | `X` | | | 牵引装置从车轴平面沿 earth-fixed *X* 轴的偏移 | 计算所得 | m |
| `Y` | | | 牵引装置从中心平面沿 earth-fixed *Y* 轴的偏移 | 计算所得 | m |
| `Z` | | | 牵引装置从车轴平面沿 earth-fixed *Z* 轴的偏移 | 计算所得 | m |
| `Vel` | `Xdot` | | | 牵引装置从车轴平面沿 earth-fixed *X* 轴的偏移速度 | 计算所得 | m |
| `Ydot` | | | 牵引装置从中心平面沿 earth-fixed *Y* 轴的偏移速度 | 计算所得 | m |
| `Zdot` | | | 牵引装置从车轴平面沿 earth-fixed *Z* 轴的偏移速度 | 计算所得 | m |
| `Geom` | `Disp` | `X` | | | 车辆底盘从车轴平面沿 earth-fixed *X* 轴的偏移 | 计算所得 | m |
| `Y` | | | 车辆底盘从中心平面沿 earth-fixed *Y* 轴的偏移 | 计算所得 | m |
| `Z` | | | 车辆底盘从车轴平面沿 earth-fixed *Z* 轴的偏移 | 计算所得 | m |
| `Vel` | `Xdot` | | | 车辆底盘沿 earth-fixed *X* 轴的偏移速度 | 计算所得 | m/s |
| `Ydot` | | | 车辆底盘沿 earth-fixed *Y* 轴的偏移速度 | 计算所得 | m/s |
| `Zdot` | | | 车辆底盘沿 earth-fixed *Z* 轴的偏移速度 | 计算所得 | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | 车辆 CG 沿 vehicle-fixed *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | | 车辆 CG 沿 vehicle-fixed *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | | 车辆 CG 沿 vehicle-fixed *z* 轴的速度 | `0` | m/s |
| `Ang` | `Beta` | | | 车身侧偏角，*β*    β=VyVx | 计算所得 | rad |
| `AngVel` | `p` | | | 车辆绕 vehicle-fixed *x* 轴的角速度（横滚角速度） | `0` | rad/s |
| `q` | | | 车辆绕 vehicle-fixed *y* 轴的角速度（俯仰角速度） | `0` | rad/s |
| `r` | | | 车辆绕 vehicle-fixed *z* 轴的角速度（横摆角速度） | 计算所得 | rad/s |
| `Acc` | `ax` | | | 车辆 CG 沿 vehicle-fixed *x* 轴的加速度 | 计算所得 | gn |
| `ay` | | | 车辆 CG 沿 vehicle-fixed *y* 轴的加速度 | 计算所得 | gn |
| `az` | | | 车辆 CG 沿 vehicle-fixed *z* 轴的加速度 | `0` | gn |
| `xddot` | | | 车辆 CG 沿 vehicle-fixed *x* 轴的加速度 | 计算所得 | m/s^2 |
| `yddot` | | | 车辆 CG 沿 vehicle-fixed *y* 轴的加速度 | 计算所得 | m/s^2 |
| `zddot` | | | 车辆 CG 沿 vehicle-fixed *z* 轴的加速度 | `0` | m/s^2 |
| `AngAcc` | `pdot` | | | 车辆绕 vehicle-fixed *x* 轴的角加速度 | `0` | rad/s |
| `qdot` | | | 车辆绕 vehicle-fixed *y* 轴的角加速度 | `0` | rad/s |
| `rdot` | | | 车辆绕 vehicle-fixed *z* 轴的角加速度 | 计算所得 | rad/s |
| `DCM` | 方向余弦矩阵 | | | | 计算所得 | rad |
| `Forces` | `Body` | `Fx` | | | 车辆 CG 上沿 vehicle-fixed *x* 轴的合力 | 计算所得 | N |
| `Fy` | | | 车辆 CG 上沿 vehicle-fixed *y* 轴的合力 | 计算所得 | N |
| `Fz` | | | 车辆 CG 上沿 vehicle-fixed *z* 轴的合力 | `0` | N |
| `Ext` | `Fx` | | | 车辆 CG 上沿 vehicle-fixed *x* 轴的外力 | 计算所得 | N |
| `Fy` | | | 车辆 CG 上沿 vehicle-fixed *y* 轴的外力 | 计算所得 | N |
| `Fz` | | | 车辆 CG 上沿 vehicle-fixed *z* 轴的外力 | `0` | N |
| `Hitch` | `Fx` | | | 在牵引装置位置施加到车身上的沿 vehicle-fixed *x* 轴的牵引力 | 输入 | N |
| `Fy` | | | 在牵引装置位置施加到车身上的沿 vehicle-fixed *y* 轴的牵引力 | 输入 | N |
| `Fz` | | | 在牵引装置位置施加到车身上的沿 vehicle-fixed *z* 轴的牵引力 | 输入 | N |
| `FrntAxl` | `Fx` | | | 前轮上的纵向力，沿 vehicle-fixed *x* 轴 | 计算所得 | N |
| `Fy` | | | 前轮上的侧向力，沿 vehicle-fixed *y* 轴 | 计算所得 | N |
| `Fz` | | | 前轮上的法向力，沿 vehicle-fixed *z* 轴 | 计算所得 | N |
| `RearAxl` | `Fx` | | | 后轮上的纵向力，沿 vehicle-fixed *x* 轴 | 计算所得 | N |
| `Fy` | | | 后轮上的侧向力，沿 vehicle-fixed *y* 轴 | 计算所得 | N |
| `Fz` | | | 后轮上的法向力，沿 vehicle-fixed *z* 轴 | 计算所得 | N |
| `Tires` | `FrntTire` | `Fx` | | 前轮胎力，沿 vehicle-fixed *x* 轴 | 计算所得 | N |
| `Fy` | | 前轮胎力，沿 vehicle-fixed *y* 轴 | 计算所得 | N |
| `Fz` | | 前轮胎力，沿 vehicle-fixed *z* 轴 | 计算所得 | N |
| `RearTire` | `Fx``Fx` | | 后轮胎力，沿 vehicle-fixed *x* 轴 | 计算所得 | N |
| `Fy` | | 后轮胎力，沿 vehicle-fixed *y* 轴 | 计算所得 | N |
| `Fz` | | 后轮胎力，沿 vehicle-fixed *z* 轴 | 计算所得 | N |
| `Drag` | `Fx` | | | 车辆 CG 上沿 vehicle-fixed *x* 轴的阻力 | 计算所得 | N |
| `Fy` | | | 车辆 CG 上沿 vehicle-fixed *y* 轴的阻力 | 计算所得 | N |
| `Fz` | | | 车辆 CG 上沿 vehicle-fixed *z* 轴的阻力 | 计算所得 | N |
| `Grvty` | `Fx` | | | 车辆 CG 上沿 vehicle-fixed *x* 轴的重力 | 计算所得 | N |
| `Fy` | | | 车辆 CG 上沿 vehicle-fixed *y* 轴的重力 | 计算所得 | N |
| `Fz` | | | 车辆 CG 上沿 vehicle-fixed *z* 轴的重力 | 计算所得 | N |
| `Moments` | `Body` | `Mx` | | | 车辆 CG 上绕 vehicle-fixed *x* 轴的车身力矩 | `0` | N·m |
| `My` | | | 车辆 CG 上绕 vehicle-fixed *y* 轴的车身力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆 CG 上绕 vehicle-fixed *z* 轴的车身力矩 | `0` | N·m |
| `Drag` | `Mx` | | | 车辆 CG 上绕 vehicle-fixed *x* 轴的阻力力矩 | `0` | N·m |
| `My` | | | 车辆 CG 上绕 vehicle-fixed *y* 轴的阻力力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆 CG 上绕 vehicle-fixed *z* 轴的阻力力矩 | `0` | N·m |
| `Ext` | `Mx` | | | 车辆 CG 上绕 vehicle-fixed *x* 轴的外力矩 | `0` | N·m |
| `My` | | | 车辆 CG 上绕 vehicle-fixed *y* 轴的外力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆 CG 上绕 vehicle-fixed *z* 轴的外力矩 | `0` | N·m |
| `Hitch` | `Mx` | | | 牵引装置位置处绕 vehicle-fixed *x* 轴的牵引力矩 | `0` | N·m |
| `My` | | | 牵引装置位置处绕 vehicle-fixed *y* 轴的牵引力矩 | 计算所得 | N·m |
| `Mz` | | | 牵引装置位置处绕 vehicle-fixed *z* 轴的牵引力矩 | `0` | N·m |
| `FrntAxl` | `Disp` | `x` | | | 前轮沿 vehicle-fixed *x* 轴的位移 | 计算所得 | m |
| `y` | | | 前轮沿 vehicle-fixed *y* 轴的位移 | 计算所得 | m |
| `z` | | | 前轮沿 vehicle-fixed *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | | 前轮沿 vehicle-fixed *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | | 前轮沿 vehicle-fixed *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | | 前轮沿 vehicle-fixed *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngFL` | | | 前左轮转向角 | 计算所得 | rad |
| `WhlAngFR` | | | 前右轮转向角 | 计算所得 | rad |
| `RearAxl` | `Disp` | `x` | | | 后轮沿 vehicle-fixed *x* 轴的位移 | 计算所得 | m |
| `y` | | | 后轮沿 vehicle-fixed *y* 轴的位移 | 计算所得 | m |
| `z` | | | 后轮沿 vehicle-fixed *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | | 后轮沿 vehicle-fixed *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | | 后轮沿 vehicle-fixed *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | | 后轮沿 vehicle-fixed *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 后左轮转向角 | 计算所得 | rad |
| `WhlAngRR` | | | 后右轮转向角 | 计算所得 | rad |
| `Hitch` | `Disp` | | `x` | | 牵引装置从车轴平面沿 vehicle-fixed *x* 轴的偏移 | 输入 | m |
| `y` | | 牵引装置从中心平面沿 vehicle-fixed *y* 轴的偏移 | 输入 | m |
| `z` | | 牵引装置从车轴平面沿 earth-fixed *z* 轴的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 牵引装置沿 vehicle-fixed *x* 轴的偏移速度 | 计算所得 | m/s |
| `ydot` | | 牵引装置沿 vehicle-fixed *y* 轴的偏移速度 | 计算所得 | m/s |
| `zdot` | | 牵引装置沿 vehicle-fixed *z* 轴的偏移速度 | 计算所得 | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | 计算所得 | W |
| `Hitch` | | | | 牵引装置导致的功率损失 | 计算所得 | W |
| `Drag` | | | | 阻力导致的功率损失 | 计算所得 | W |
| `Geom` | `Disp` | | `x` | | 车辆底盘从车轴平面沿 vehicle-fixed *x* 轴的偏移 | 输入 | m |
| `y` | | 车辆底盘从中心平面沿 vehicle-fixed *y* 轴的偏移 | 输入 | m |
| `z` | | 车辆底盘从车轴平面沿 earth-fixed *z* 轴的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 车辆底盘沿 vehicle-fixed *x* 轴的偏移速度 | 计算所得 | m/s |
| `ydot` | | 车辆底盘沿 vehicle-fixed *y* 轴的偏移速度 | 计算所得 | m/s |
| `zdot` | | 车辆底盘沿 vehicle-fixed *z* 轴的偏移速度 | `0` | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | 计算所得 | rad |

| 信号 | | | 描述 | | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | 外部施加的纵向力功率 | | 计算值 | W |
| `PwrFyExt` | 外部施加的横向力功率 | | 计算值 | W |
| `PwrMzExt` | 外部施加的横摆力矩功率 | | 计算值 | W |
| `PwrFwFx` | 施加在前轴上的纵向力功率 | | 计算值 | W |
| `PwrFwFy` | 施加在前轴上的横向力功率 | | 计算值 | W |
| `PwrFwRx` | 施加在后轴上的纵向力功率 | | 计算值 | W |
| `PwrFwRy` | 施加在后轴上的横向力功率 | | 计算值 | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | 纵向阻力功率 | | 计算值 | W |
| `PwrFyDrag` | 横向阻力功率 | | 计算值 | W |
| `PwrMzDrag` | 阻力俯仰力矩功率 | | 计算值 | W |
| `PwrStored` | `PwrStoredGrvty` | 重力势能变化率 | | 计算值 | W |
| `PwrStoredxdot` | 纵向动能变化率 | | 计算值 | W |
| `PwrStoredydot` | 横向动能变化率 | | 计算值 | W |
| `PwrStoredr` | 横摆旋转动能变化率 | | 计算值 | W |

### **xdot** — 车身纵向速度 `scalar`

车辆质心沿车辆固定 `x` 轴的速度，单位为 m/s。

### **ydot** — 车身横向速度 `scalar`

车辆质心沿车辆固定 `y` 轴的速度，单位为 m/s。

### **psi** — 横摆 `scalar`

车辆固定坐标系绕大地固定 `Z` 轴的旋转（横摆），单位为 rad。

### **r** — 横摆角速度 `scalar`

车辆绕车辆固定 `z` 轴的角速度 `r`（横摆角速度），单位为 rad/s。
## 参数
```yaml
parameters:
- name: Number of wheels on front axle, NF
  summary: 前轮数量 2（默认）| scalar
  group: ''
- name: Number of wheels on rear axle, NR
  summary: 后轮数量 2（默认）| scalar
  group: ''
- name: Vehicle mass, m
  summary: 车辆质量 2000（默认）| scalar
  group: ''
- name: Longitudinal distance from center of mass to front axle, a
  summary: 前轴距离 1.4（默认）| scalar
  group: ''
- name: Longitudinal distance from center of mass to rear axle, b
  summary: 后轴距离 1.6（默认）| scalar
  group: ''
- name: Vertical distance from center of mass to axle plane, h
  summary: 高度 0.35（默认）| scalar
  group: ''
- name: Initial inertial frame longitudinal position, X_o
  summary: 位置 0（默认）| scalar
  group: ''
- name: Initial longitudinal velocity, xdot_o
  summary: 速度 0（默认）| scalar
  group: ''
- name: Front tire corner stiffness, Cy_f
  summary: 刚度 12e3（默认）| scalar
  group: ''
- name: Rear tire corner stiffness, Cy_r
  summary: 刚度 11e3（默认）| scalar
  group: ''
- name: Initial inertial frame lateral displacement, Y_o
  summary: 位置 0（默认）| scalar
  group: ''
- name: Initial lateral velocity, ydot_o
  summary: 速度 0（默认）| scalar
  group: ''
- name: Yaw polar inertia, Izz
  summary: 惯性 4000（默认）| scalar
  group: ''
- name: Initial yaw angle, psi_o
  summary: Psi 旋转 0（默认）| scalar
  group: ''
- name: Initial yaw rate, r_o
  summary: 横摆角速度 0（默认）| scalar
  group: ''
- name: 纵向阻力面积，Af
  summary: 有效车辆横截面积 2（默认）| 标量
  group: ''
- name: 纵向阻力系数，Cd
  summary: 空气阻力系数 .3（默认）| 标量
  group: ''
- name: 纵向升力系数，Cl
  summary: 空气升力系数 .1（默认）| 标量
  group: ''
- name: 纵向阻力俯仰力矩，Cpm
  summary: 俯仰阻力 .1（默认）| 标量
  group: ''
- name: 相对风向角向量，beta_w
  summary: 风向角 [0:0.01:0.3]（默认）| 向量
  group: ''
- name: 侧向力系数向量，Cs
  summary: 侧向力系数 [0:0.03:0.9]（默认）| 向量
  group: ''
- name: 横摆力矩系数向量，Cym
  summary: 横摆力矩阻力 [0:0.01:0.3]（默认）| 向量
  group: ''
- name: 绝对压力，Pabs
  summary: 压力 101325（默认）| 标量 | 标量
  group: ''
- name: 空气温度，Tair
  summary: 温度 273（默认）| 标量
  group: ''
- name: 重力加速度，g
  summary: 重力 9.81（默认）| 标量
  group: ''
- name: 标称摩擦比例因子，mu
  summary: 摩擦比例因子 1（默认）| 标量
  group: ''
- name: 纵向速度容差，xdot_tol
  summary: 容差 .01（默认）| 标量
  group: ''
- name: 标称法向力，Fznom
  summary: 法向力 5000（默认）| 标量
  group: ''
- name: 距轴平面的几何纵向偏移，longOff
  summary: 纵向偏移 0（默认）| 标量
  group: ''
- name: 距中心平面的几何侧向偏移，latOff
  summary: 侧向偏移 0（默认）| 标量
  group: ''
- name: 距轴平面的几何垂向偏移，vertOff
  summary: 垂向偏移 0（默认）| 标量
  group: ''
```

#### 纵向

### **Number of wheels on front axle, NF** — 前轮数量 `2`（默认）| `scalar`

前轴上的车轮数量，*NF*。该值无量纲。

### **Number of wheels on rear axle, NR** — 后轮数量 `2`（默认）| `scalar`

后轴上的车轮数量，*NR*。该值无量纲。

### **Vehicle mass, m** — 车辆质量 `2000`（默认）| `scalar`

车辆质量 *m*，单位为 kg。

### **Longitudinal distance from center of mass to front axle, a** — 前轴距离 `1.4`（默认）| `scalar`

从车辆质心到前轮轴的水平距离 *a*，单位为 m。

### **Longitudinal distance from center of mass to rear axle, b** — 后轴距离 `1.6`（默认）| `scalar`

从车辆质心到后轮轴的水平距离 *b*，单位为 m。

### **Vertical distance from center of mass to axle plane, h** — 高度 `0.35`（默认）| `scalar`

车辆质心高于车轴的高度 *h*，单位为 m。

### **Initial inertial frame longitudinal position, X\_o** — 位置 `0`（默认）| `scalar`

车辆质心沿大地固定 *X* 轴的初始位移，单位为 m。

### **Initial longitudinal velocity, xdot\_o** — 速度 `0`（默认）| `scalar`

车辆质心沿车辆固定 *x* 轴的初始速度，单位为 m/s。

#### 横向

### **Front tire corner stiffness, Cy\_f** — 刚度 `12e3`（默认）| `scalar`

前轮胎侧偏刚度 *Cyf*，单位为 N/rad。

### **Rear tire corner stiffness, Cy\_r** — 刚度 `11e3`（默认）| `scalar`

后轮胎侧偏刚度 *Cyr*，单位为 N/rad。

### **Initial inertial frame lateral displacement, Y\_o** — 位置 `0`（默认）| `scalar`

车辆质心沿大地固定 *Y* 轴的初始位移，单位为 m。

### **Initial lateral velocity, ydot\_o** — 速度 `0`（默认）| `scalar`

车辆质心沿车辆固定 *y* 轴的初始速度，单位为 m/s。

#### 横摆

### **Yaw polar inertia, Izz** — 惯性 `4000`（默认）| `scalar`

横摆极惯性，单位为 kg\*m^2。

### **Initial yaw angle, psi\_o** — Psi 旋转 `0`（默认）| `scalar`

车辆固定坐标系绕大地固定 *Z* 轴的旋转（横摆），单位为 rad。

### **Initial yaw rate, r\_o** — 横摆角速度 `0`（默认）| `scalar`

车辆绕车辆固定 *z* 轴的角速度（横摆角速度），单位为 rad/s。

#### 空气动力学

### **纵向阻力面积，Af** — 有效车辆横截面积 `2`（默认）| `标量`

有效车辆横截面积，
*Af*，用于计算车辆所受气动阻力，
单位为 m2。

### **纵向阻力系数，Cd** — 空气阻力系数 `.3`（默认）| `标量`

空气阻力系数，*Cd*。该值
无量纲。

### **纵向升力系数，Cl** — 空气升力系数 `.1`（默认）| `标量`

空气升力系数，*Cl*。该值
无量纲。

### **纵向阻力俯仰力矩，Cpm** — 俯仰阻力 `.1`（默认）| `标量`

纵向阻力俯仰力矩系数，
*Cpm*。该值
无量纲。

### **相对风向角向量，beta\_w** — 风向角 `[0:0.01:0.3]`（默认）| `向量`

相对风向角向量，*βw*，单位为
rad。

### **侧向力系数向量，Cs** — 侧向力系数 `[0:0.03:0.9]`（默认）| `向量`

侧向力系数向量系数，
*Cs*。该值无量纲。

### **横摆力矩系数向量，Cym** — 横摆力矩阻力 `[0:0.01:0.3]`（默认）| `向量`

横摆力矩系数向量，*Cym*。该
值无量纲。

#### 环境

### **绝对压力，Pabs** — 压力 `101325`（默认）| `标量` | `标量`

环境绝对压力，
*Pabs*，单位为 Pa。

### **空气温度，Tair** — 温度 `273`（默认）| `标量`

环境绝对温度，*T*，单位为 K。

### **重力加速度，g** — 重力 `9.81`（默认）| `标量`

重力加速度，*g*，单位为 m/s^2。

### **标称摩擦比例因子，mu** — 摩擦比例因子 `1`（默认）| `标量`

标称摩擦比例因子，*μ*。该值
无量纲。

#### 仿真

### **纵向速度容差，xdot\_tol** — 容差 `.01`（默认）| `标量`

纵向速度容差，单位为 m/s。

### **标称法向力，Fznom** — 法向力 `5000`（默认）| `标量`

标称法向力，单位为 N。

### **距轴平面的几何纵向偏移，longOff** — 纵向偏移 `0`（默认）| `标量`

车辆底盘沿车身固定
*x* 轴距轴平面的偏移，单位为 m。当您使用 3D 可视化
引擎时，可考虑使用该偏移来定位底盘，使其独立于
车辆 CG。

### **距中心平面的几何侧向偏移，latOff** — 侧向偏移 `0`（默认）| `标量`

车辆底盘沿车身固定
*y* 轴距中心平面的偏移，单位为 m。当您使用 3D 可视化
引擎时，可考虑使用该偏移来定位底盘，使其独立于
车辆 CG。

### **距轴平面的几何垂向偏移，vertOff** — 垂向偏移 `0`（默认）| `标量`

车辆底盘沿车身固定
*z* 轴距轴平面的偏移，单位为 m。当您使用 3D 可视化
引擎时，可考虑使用该偏移来定位底盘，使其独立于
车辆 CG。
## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Bicycle Model 模块仿真模型需要
Simulink
3D Animation。

## 描述

实现单轨三自由度刚性车身模型，用于计算纵向、横向和横摆运动

**注意**

使用 Bicycle Model 模块仿真模型需要
Simulink®
3D Animation™。

Bicycle Model 模块实现刚性双轴单轨车身模型，用于计算纵向、横向和横摆运动。该模块考虑了车身质量、气动阻力以及由于加速度和转向引起的前后轴之间的重量分配。Bicycle Model 模块有两种类型。

| 模块 | 实现 |
| --- | --- |
| Bicycle Model - Velocity Input带速度输入端口 WhlAngF 和 xdotin 的自行车模型模块。 | - 模块假设外部纵向速度为准稳态，因此纵向加速度近似为零。 - 由于运动为准稳态，模块仅使用轮胎侧偏角和线性侧偏刚度计算横向力。 |
| Bicycle Model - Force Input带力输入端口 WhlAngF、FxF 和 FxR 的自行车模型模块。 | - 模块使用外部纵向力使车辆加速或制动。 - 模块使用轮胎侧偏角和线性侧偏刚度计算横向力。 |

为计算前轴和后轴上的法向力，该模块使用刚体车辆运动、悬架系统力以及风力和阻力。该模块在刚性车身坐标系上求解力和力矩分量。
