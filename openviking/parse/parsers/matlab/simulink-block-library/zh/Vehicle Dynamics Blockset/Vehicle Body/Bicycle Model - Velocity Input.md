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

### 输入

### **WhlAngF** — 前轮转角 `scalar`

前轮转角，单位为 rad。

### **FxF** — 力输入：前轴总纵向力 `scalar`

前轴上的纵向力，*FxF*，沿车辆固定 `x` 轴，单位为 N。

Bicycle Model - Force Input 模块输入端口。

### **FxR** — 力输入：后轴总纵向力 `scalar`

后轴上的纵向力，*FxR*，沿车辆固定 `x` 轴，单位为 N。

Bicycle Model - Force Input 模块输入端口。

### **xdotin** — 速度输入：纵向速度 `scalar`

车辆质心沿车辆固定 *x* 轴的速度，单位为 m/s。

Bicycle Model - Velocity Input 模块输入端口。
### 输出

### **Info** — 总线信号 bus

包含这些模块值的总线信号。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆质心沿大地固定 *X* 轴的位移 | Computed | m |
| `Y` | | | 车辆质心沿大地固定 *Y* 轴的位移 | Computed | m |
| `Z` | | | 车辆质心沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 车辆质心沿大地固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | | 车辆质心沿大地固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | | 车辆质心沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕大地固定 *X* 轴的旋转（侧倾） | `0` | rad |
| `theta` | | | 车辆固定坐标系绕大地固定 *Y* 轴的旋转（俯仰） | `0` | rad |
| `psi` | | | 车辆固定坐标系绕大地固定 *Z* 轴的旋转（偏航） | Computed | rad |
| `FrntAxl` | `Disp` | `X` | | | 前轮沿大地固定 *X* 轴的位移 | Computed | m |
| `Y` | | | 前轮沿大地固定 *Y* 轴的位移 | Computed | m |
| `Z` | | | 前轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 前轮沿大地固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | | 前轮沿大地固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | | 前轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `RearAxl` | `Disp` | `X` | | | 后轮沿大地固定 *X* 轴的位移 | Computed | m |
| `Y` | | | 后轮沿大地固定 *Y* 轴的位移 | Computed | m |
| `Z` | | | 后轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 后轮沿大地固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | | 后轮沿大地固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | | 后轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Hitch` | `Disp` | `X` | | | 牵引点沿大地固定 *X* 轴偏离轴平面的偏移 | Computed | m |
| `Y` | | | 牵引点沿大地固定 *Y* 轴偏离中心平面的偏移 | Computed | m |
| `Z` | | | 牵引点沿大地固定 *Z* 轴偏离轴平面的偏移 | Computed | m |
| `Vel` | `Xdot` | | | 牵引点偏移速度沿大地固定 *X* 轴，从轴平面起算 | Computed | m |
| `Ydot` | | | 牵引点沿大地固定 *Y* 轴从中心平面起算的偏移速度 | Computed | m |
| `Zdot` | | | 牵引点沿大地固定 *Z* 轴从轴平面起算的偏移速度 | Computed | m |
| `Geom` | `Disp` | `X` | | | 车辆底盘沿大地固定 *X* 轴偏离轴平面的偏移 | Computed | m |
| `Y` | | | 车辆底盘沿大地固定 *Y* 轴偏离中心平面的偏移 | Computed | m |
| `Z` | | | 车辆底盘沿大地固定 *Z* 轴偏离轴平面的偏移 | Computed | m |
| `Vel` | `Xdot` | | | 车辆底盘偏移速度沿大地固定 *X* 轴 | Computed | m/s |
| `Ydot` | | | 车辆底盘偏移速度沿大地固定 *Y* 轴 | Computed | m/s |
| `Zdot` | | | 车辆底盘偏移速度沿大地固定 *Z* 轴 | Computed | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | 车辆质心沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | | 车辆质心沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | | 车辆质心沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Ang` | `Beta` | | | 车身侧偏角，*β*    β=VyVx | Computed | rad |
| `AngVel` | `p` | | | 车辆绕车辆固定 *x* 轴的角速度（侧倾角速度） | `0` | rad/s |
| `q` | | | 车辆绕车辆固定 *y* 轴的角速度（俯仰角速度） | `0` | rad/s |
| `r` | | | 车辆绕车辆固定 *z* 轴的角速度（偏航角速度） | Computed | rad/s |
| `Acc` | `ax` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | Computed | gn |
| `ay` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | Computed | gn |
| `az` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | gn |
| `xddot` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | Computed | m/s^2 |
| `yddot` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | Computed | m/s^2 |
| `zddot` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | m/s^2 |
| `AngAcc` | `pdot` | | | 车辆绕车辆固定 *x* 轴的角加速度 | `0` | rad/s |
| `qdot` | | | 车辆绕车辆固定 *y* 轴的角加速度 | `0` | rad/s |
| `rdot` | | | 车辆绕车辆固定 *z* 轴的角加速度 | Computed | rad/s |
| `DCM` | 方向余弦矩阵 | | | | Computed | rad |
| `Forces` | `Body` | `Fx` | | | 车辆质心上的合力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | | 车辆质心上的合力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | | 车辆质心上的合力沿车辆固定 *z* 轴 | `0` | N |
| `Ext` | `Fx` | | | 车辆质心上的外力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | | 车辆质心上的外力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | | 车辆质心上的外力沿车辆固定 *z* 轴 | `0` | N |
| `Hitch` | `Fx` | | | 在牵引点位置施加到车身上的牵引力沿车辆固定 *x* 轴 | Input | N |
| `Fy` | | | 在牵引点位置施加到车身上的牵引力沿车辆固定 *y* 轴 | Input | N |
| `Fz` | | | 在牵引点位置施加到车身上的牵引力沿车辆固定 *z* 轴 | Input | N |
| `FrntAxl` | `Fx` | | | 前轮上的纵向力，沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | | 前轮上的横向力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | | 前轮上的法向力，沿车辆固定 *z* 轴 | Computed | N |
| `RearAxl` | `Fx` | | | 后轮上的纵向力，沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | | 后轮上的横向力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | | 后轮上的法向力，沿车辆固定 *z* 轴 | Computed | N |
| `Tires` | `FrntTire` | `Fx` | | 前轮胎力，沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | 前轮胎力，沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | 前轮胎力，沿车辆固定 *z* 轴 | Computed | N |
| `RearTire` | `Fx``Fx` | | 后轮胎力，沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | 后轮胎力，沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | 后轮胎力，沿车辆固定 *z* 轴 | Computed | N |
| `Drag` | `Fx` | | | 车辆质心上的阻力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | | 车辆质心上的阻力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | | 车辆质心上的阻力沿车辆固定 *z* 轴 | Computed | N |
| `Grvty` | `Fx` | | | 车辆质心上的重力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | | 车辆质心上的重力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | | 车辆质心上的重力沿车辆固定 *z* 轴 | Computed | N |
| `Moments` | `Body` | `Mx` | | | 车辆质心上的车身力矩绕车辆固定 *x* 轴 | `0` | N·m |
| `My` | | | 车辆质心上的车身力矩绕车辆固定 *y* 轴 | Computed | N·m |
| `Mz` | | | 车辆质心上的车身力矩绕车辆固定 *z* 轴 | `0` | N·m |
| `Drag` | `Mx` | | | 车辆质心上的阻力力矩绕车辆固定 *x* 轴 | `0` | N·m |
| `My` | | | 车辆质心上的阻力力矩绕车辆固定 *y* 轴 | Computed | N·m |
| `Mz` | | | 车辆质心上的阻力力矩绕车辆固定 *z* 轴 | `0` | N·m |
| `Ext` | `Mx` | | | 车辆质心上的外力矩绕车辆固定 *x* 轴 | `0` | N·m |
| `My` | | | 车辆质心上的外力矩绕车辆固定 *y* 轴 | Computed | N·m |
| `Mz` | | | 车辆质心上的外力矩绕车辆固定 *z* 轴 | `0` | N·m |
| `Hitch` | `Mx` | | | 牵引点处的牵引力矩绕车辆固定 *x* 轴 | `0` | N·m |
| `My` | | | 牵引点处的牵引力矩绕车辆固定 *y* 轴 | Computed | N·m |
| `Mz` | | | 牵引点处的牵引力矩绕车辆固定 *z* 轴 | `0` | N·m |
| `FrntAxl` | `Disp` | `x` | | | 前轮沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | | 前轮沿车辆固定 *y* 轴的位移 | Computed | m |
| `z` | | | 前轮沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | | 前轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | | 前轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | | 前轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngFL` | | | 前左轮转向角 | Computed | rad |
| `WhlAngFR` | | | 前右轮转向角 | Computed | rad |
| `RearAxl` | `Disp` | `x` | | | 后轮沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | | 后轮沿车辆固定 *y* 轴的位移 | Computed | m |
| `z` | | | 后轮沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | | 后轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | | 后轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | | 后轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 后左轮转向角 | Computed | rad |
| `WhlAngRR` | | | 后右轮转向角 | Computed | rad |
| `Hitch` | `Disp` | | `x` | | 牵引点沿车辆固定 *x* 轴偏离轴平面的偏移 | Input | m |
| `y` | | 牵引点沿车辆固定 *y* 轴偏离中心平面的偏移 | Input | m |
| `z` | | 牵引点沿大地固定 *z* 轴偏离轴平面的偏移 | Input | m |
| `Vel` | | `xdot` | | 牵引点偏移速度沿车辆固定 *x* 轴 | Computed | m/s |
| `ydot` | | 牵引点偏移速度沿车辆固定 *y* 轴 | Computed | m/s |
| `zdot` | | 牵引点偏移速度沿车辆固定 *z* 轴 | Computed | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | Computed | W |
| `Hitch` | | | | 牵引点导致的功率损失 | Computed | W |
| `Drag` | | | | 阻力导致的功率损失 | Computed | W |
| `Geom` | `Disp` | | `x` | | 车辆底盘沿车辆固定 *x* 轴偏离轴平面的偏移 | Input | m |
| `y` | | 车辆底盘沿车辆固定 *y* 轴偏离中心平面的偏移 | Input | m |
| `z` | | 车辆底盘沿大地固定 *z* 轴偏离轴平面的偏移 | Input | m |
| `Vel` | | `xdot` | | 车辆底盘偏移速度沿车辆固定 *x* 轴 | Computed | m/s |
| `ydot` | | 车辆底盘偏移速度沿车辆固定 *y* 轴 | Computed | m/s |
| `zdot` | | 车辆底盘偏移速度沿车辆固定 *z* 轴 | `0` | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | Computed | rad |

| 信号 | | | 描述 | | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | 外部施加的纵向力功率 | | Computed | W |
| `PwrFyExt` | 外部施加的横向力功率 | | Computed | W |
| `PwrMzExt` | 外部施加的侧倾力矩功率 | | Computed | W |
| `PwrFwFx` | 施加在前轴的纵向力功率 | | Computed | W |
| `PwrFwFy` | 施加在前轴的横向力功率 | | Computed | W |
| `PwrFwRx` | 施加在后轴的纵向力功率 | | Computed | W |
| `PwrFwRy` | 施加在后轴的横向力功率 | | Computed | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | 纵向阻力功率 | | Computed | W |
| `PwrFyDrag` | 横向阻力功率 | | Computed | W |
| `PwrMzDrag` | 阻力俯仰力矩功率 | | Computed | W |
| `PwrStored` | `PwrStoredGrvty` | 重力势能变化率 | | Computed | W |
| `PwrStoredxdot` | 纵向动能变化率 | | Computed | W |
| `PwrStoredydot` | 横向动能变化率 | | Computed | W |
| `PwrStoredr` | 偏航旋转动能变化率 | | Computed | W |

### **xdot** — 车身纵向速度 `scalar`

车辆质心沿车辆固定 `x` 轴的速度，单位为 m/s。

### **ydot** — 车身横向速度 `scalar`

车辆质心沿车辆固定 `y` 轴的速度，单位为 m/s。

### **psi** — 偏航 `scalar`

车辆固定坐标系绕大地固定 `Z` 轴的旋转（偏航），单位为 rad。

### **r** — 偏航角速度 `scalar`

车辆绕车辆固定 `z` 轴的角速度 `r`（偏航角速度），单位为 rad/s。

## 参数

#### 纵向

### **前轴车轮数量，NF** — 前轮数量 `2` (默认) | `scalar`

前轴车轮数量，*NF*。该值无量纲。

### **后轴车轮数量，NR** — 后轮数量 `2` (默认) | `scalar`

后轴车轮数量，*NR*。该值无量纲。

### **车辆质量，m** — 车辆质量 `2000` (默认) | `scalar`

车辆质量，*m*，单位为 kg。

### **从质心到前轴的纵向距离，a** — 前轴距离 `1.4` (默认) | `scalar`

从车辆质心到前轮轴的水平距离 *a*，单位为 m。

### **从质心到后轴的纵向距离，b** — 后轴距离 `1.6` (默认) | `scalar`

从车辆质心到后轮轴的水平距离 *b*，单位为 m。

### **从质心到轴平面的垂直距离，h** — 高度 `0.35` (默认) | `scalar`

车辆质心高出车轴的高度 *h*，单位为 m。

### **初始惯性坐标系纵向位置，X\_o** — 位置 `0` (默认) | `scalar`

车辆质心沿大地固定 *X* 轴的初始位移，单位为 m。

### **初始纵向速度，xdot\_o** — 速度 `0` (默认) | `scalar`

车辆质心沿车辆固定 *x* 轴的初始速度，单位为 m/s。

#### 横向

### **前轮胎侧偏刚度，Cy\_f** — 刚度 `12e3` (默认) | `scalar`

前轮胎侧偏刚度，*Cyf*，单位为 N/rad。

### **后轮胎侧偏刚度，Cy\_r** — 刚度 `11e3` (默认) | `scalar`

后轮胎侧偏刚度，*Cyr*，单位为 N/rad。

### **初始惯性坐标系横向位移，Y\_o** — 位置 `0` (默认) | `scalar`

车辆质心沿大地固定 *Y* 轴的初始位移，单位为 m。

### **初始横向速度，ydot\_o** — 速度 `0` (默认) | `scalar`

车辆质心沿车辆固定 *y* 轴的初始速度，单位为 m/s。

#### 偏航

### **偏航极惯性，Izz** — 惯性 `4000` (默认) | `scalar`

偏航极惯性，单位为 kg\*m^2。

### **初始偏航角，psi\_o** — Psi 旋转 `0` (默认) | `scalar`

车辆固定坐标系绕大地固定 *Z* 轴的旋转（偏航），单位为 rad。

### **初始偏航角速度，r\_o** — 偏航角速度 `0` (默认) | `scalar`

车辆绕车体固定 *z* 轴的角速度（偏航角速度），以 rad/s 为单位。

#### 气动

### **纵向阻力面积，Af** — 有效车辆横截面积 `2` (默认) | `scalar`

用于计算车辆所受空气阻力的有效车辆横截面积 *Af*，以 m2 为单位。

### **纵向阻力系数，Cd** — 空气阻力系数 `.3` (默认) | `scalar`

空气阻力系数 *Cd*。该值无量纲。

### **纵向升力系数，Cl** — 空气升力系数 `.1` (默认) | `scalar`

空气升力系数 *Cl*。该值无量纲。

### **纵向阻力俯仰力矩，Cpm** — 俯仰阻力 `.1` (默认) | `scalar`

纵向阻力俯仰力矩系数 *Cpm*。该值无量纲。

### **相对风角向量，beta\_w** — 风角 `[0:0.01:0.3]` (默认) | `vector`

相对风角向量 *βw*，以 rad 为单位。

### **侧向力系数向量，Cs** — 侧向力系数 `[0:0.03:0.9]` (默认) | `vector`

侧向力系数向量系数 *Cs*。该值无量纲。

### **偏航力矩系数向量，Cym** — 偏航力矩阻力 `[0:0.01:0.3]` (默认) | `vector`

偏航力矩系数向量 *Cym*。该值无量纲。

#### 环境

### **绝对压力，Pabs** — 压力 `101325` (默认) | `scalar` | `scalar`

环境绝对压力 *Pabs*，以 Pa 为单位。

### **空气温度，Tair** — 温度 `273` (默认) | `scalar`

环境绝对温度 *T*，以 K 为单位。

### **重力加速度，g** — 重力 `9.81` (默认) | `scalar`

重力加速度 *g*，以 m/s^2 为单位。

### **标称摩擦缩放因子，mu** — 摩擦比例因子 `1` (默认) | `scalar`

标称摩擦比例因子 *μ*。该值无量纲。

#### 仿真

### **纵向速度容差，xdot\_tol** — 容差 `.01` (默认) | `scalar`

纵向速度容差，以 m/s 为单位。

### **标称法向力，Fznom** — 法向力 `5000` (默认) | `scalar`

标称法向力，以 N 为单位。

### **距车轴平面的几何纵向偏移，longOff** — 纵向偏移 `0` (默认) | `scalar`

车辆底盘沿车体固定 *x* 轴距车轴平面的偏移，以 m 为单位。使用 3D 可视化引擎时，可考虑使用该偏移来定位底盘，使其独立于车辆 CG。

### **距中心平面的几何横向偏移，latOff** — 横向偏移 `0` (默认) | `scalar`

车辆底盘沿车体固定 *y* 轴距中心平面的偏移，以 m 为单位。使用 3D 可视化引擎时，可考虑使用该偏移来定位底盘，使其独立于车辆 CG。

### **距车轴平面的几何垂直偏移，vertOff** — 垂直偏移 `0` (默认) | `scalar`

车辆底盘沿车体固定 *z* 轴距车轴平面的偏移，以 m 为单位。使用 3D 可视化引擎时，可考虑使用该偏移来定位底盘，使其独立于车辆 CG。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling
Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024a: 需要 Simulink 3D Animation

使用 Bicycle Model 模块仿真模型需要 Simulink 3D Animation。

## 描述

实现单轨 3DOF 刚性车体，以计算纵向、横向和偏航运动

**注意**

使用 Bicycle Model 模块仿真模型需要 Simulink® 3D Animation™。

Bicycle Model 模块实现刚性双轴单轨车体模型，以计算纵向、横向和偏航运动。该模块考虑车身质量、空气阻力以及因加速和转向引起的车轴间重量分布。Bicycle Model 模块有两种类型。

| 模块 | 实现 |
| --- | --- |
| Bicycle Model - Velocity Input Bicycle Model 模块具有速度输入端口 WhlAngF 和 xdotin。 | - 该模块假设外部纵向速度处于准稳态，因此纵向加速度近似为零。 - 由于运动为准稳态，该模块仅使用轮胎侧偏角和线性侧偏刚度计算侧向力。 |
| Bicycle Model - Force Input Bicycle Model 模块具有力输入端口 WhlAngF、FxF 和 FxR。 | - 该模块使用外部纵向力使车辆加速或制动。 - 该模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 |

为计算前轴和后轴上的法向力，该模块使用刚体车辆运动、悬架系统力以及风力和阻力。该模块在刚性车体坐标系上求解力和力矩分量。
