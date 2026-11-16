---
type: simulink-block
title: 'Vehicle Body 3DOF'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Motion'
documentation_page: 'vehiclebody3dof'
documentation_source_path: 'ref/vehiclebody3dof.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Body 3DOF

## 端口

### 输入

### **WhlAngF** — 前轮转向角 `scalar` | `array`

前轮转向角 *δF*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | *δF* | Scalar – `1` |
| `Dual` | δF=[δflδfr]  or  [δflδfr] | Array – `[1x2]` or `[2x1]` |

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **Front wheel steering**。

### **WhlAngR** — 后轮转向角 `scalar` | `array`

后轮转向角 *δR*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | *δR* | Scalar – `1` |
| `Dual` | δR=[δrlδrr]  or  [δrlδrr] | Array – `[1x2]` or `[2x1]` |

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **Rear wheel steering**。

### **xdotin** — 纵向速度 `scalar`

车辆 CG 沿车辆固定 *x* 轴的速度，单位为 m/s。

#### 依赖项

要启用此端口，请将 **Axle forces** 设置为 `External longitudinal velocity`。

### **FwF** — 前轮上的总力 `scalar` | `array`

前轮上的力 *FwF*，沿车辆固定轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | 前轮上的纵向力 | FwF=Fxf | Scalar – `1` |
| `External forces` | 前轮上的纵向力和横向力 | FwF=[FxfFyf]  or [FxfFyf] | Array – `[1x2]` or `[2x1]` |
| `Dual` | `External longitudinal forces` | 前轮上的纵向力 | FwF=[FxflFxfr] or [FxflFxfr] | Array – `[1x2]` or `[2x1]` |
| `External forces` | 前轮上的纵向力和横向力 | FwF=[FxflFyflFxfrFyfr] | Array – `[2x2]` |

#### 依赖项

要启用此端口，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FwR** — 后轮上的总力 `scalar` | `array`

后轮上的力 *FwR*，沿车辆固定轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | 后轮上的纵向力 | FwR=Fxr | Scalar – `1` |
| `External forces` | 后轮上的纵向力和横向力 | FwR=[FxrFyr]  or [FxrFyr] | Array – `[1x2]` or `[2x1]` |
| `Dual` | `External longitudinal forces` | 后轮上的纵向力 | FwR=[FxrlFxrr] or [FxrlFxrr] | Array – `[1x2]` or `[2x1]` |
| `External forces` | 后轮上的纵向力和横向力 | FwR=[FxrlFyrlFxrrFyrr] | Array – `[2x2]` |

#### 依赖项

要启用此端口，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FExt** — 车辆 CG 上的外力 `array`

施加到车辆 CG 上的外力 *Fxext*、*Fyext*、*Fzext*，在车辆固定坐标系中，单位为 N。信号向量维度为 `[1x3]` 或 `[3x1]`。

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **External forces**。

### **MExt** — 绕车辆 CG 的外力矩 `array`

绕车辆 CG 的外力矩 *Mx*、*My*、*Mz*，在车辆固定坐标系中，单位为 N·m。信号向量维度为 `[1x3]` 或 `[3x1]`。

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **External moments**。

### **Fh** — 作用在车体上的挂钩力 `array`

在挂钩位置施加到车体上的挂钩力 *Fhx*、*Fhy*、*Fhz*，在车辆固定坐标系中，单位为 N，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖项

要启用此端口，请在 **Input signals** 下选择 **Hitch forces**。

### **Mh** — 绕车体的挂钩力矩 `array`

在挂钩位置处绕车辆固定坐标系的挂钩力矩 *Mhx*、*Mhy*、*Mhz*，单位为 N·m，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖项

要启用此端口，请在 **Input signals** 下选择 **Hitch moments**。

### **WindXYZ** — 风速 `array`

风速 *Wx*、*Wy*、*Wz*，沿惯性 *X*、*Y* 和 *Z* 轴，单位为 m/s。信号向量维度为 `[1x3]` 或 `[3x1]`。

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **External wind**。

### **Mu** — 轮胎摩擦系数 `scalar`

轮胎摩擦系数 *μ*。该值无量纲。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single (bicycle)` | 前轮上的纵向力 | Mu=[μfμr] or [μfμr] | Array – `[1x2]` or `[2x1]` |
| `Dual` | 前轮上的纵向力 | Mu=[μflμfrμrlμrr] | Array – `[2x2]` |

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **External friction**。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，单位为 K。

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **Air temperature**。

### **X\_o** — 初始纵向位置 `scalar`

车辆 CG 沿地球固定 *X* 轴的初始位移，单位为 m。

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **Initial longitudinal position**。

### **Y\_o** — 初始横向位置 `scalar`

车辆 CG 沿地球固定 *Y* 轴的初始位移，单位为 m。

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **Initial lateral position**。

### **xdot\_o** — 初始纵向速度 `scalar`

车辆 CG 沿车辆固定 *x* 轴的初始速度，单位为 m/s。

#### 依赖项

要启用此端口：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     forces`
   - `External
     forces`
2. 在 **Input signals** 窗格上，选择
   **Initial longitudinal
   velocity**

### **ydot\_o** — 初始横向速度 `scalar`

车辆 CG 沿车辆固定 *y* 轴的初始速度，单位为 m/s。

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **Initial lateral velocity**。

### **psi\_o** — 初始横摆角 `scalar`

车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆），单位为 rad。

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **Initial yaw angle**。

### **r\_o** — 初始横摆角速度 `scalar`

车辆绕车辆固定 *z* 轴的初始角速度（横摆角速度），单位为 rad/s。

#### 依赖项

要启用此端口，请在 **Input signals** 窗格上选择 **Initial yaw rate**。
### 输出

### **Info** — 总线信号总线

总线信号，包含这些模块值。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆质心沿大地固定 *X* 轴的位移 | 相对于道路坡度计算。 | m |
| `Y` | | | 车辆质心沿大地固定 *Y* 轴的位移 | 相对于道路坡度计算。 | m |
| `Z` | | | 车辆质心沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 车辆质心沿大地固定 *X* 轴的速度 | 相对于道路坡度计算。 | m/s |
| `Ydot` | | | 车辆质心沿大地固定 *Y* 轴的速度 | 相对于道路坡度计算。 | m/s |
| `Zdot` | | | 车辆质心沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕大地固定 *X* 轴的旋转（侧倾） | `0` | rad |
| `theta` | | | 车辆固定坐标系绕大地固定 *Y* 轴的旋转（俯仰） | `0` | rad |
| `psi` | | | 车辆固定坐标系绕大地固定 *Z* 轴的旋转（横摆） | 相对于坡度角计算。 | rad |
| `FrntAxl` | `Lft` | `Disp` | `X` | | 前左车轮沿大地固定 *X* 轴的位移 | 计算 | m |
| `Y` | | 前左车轮沿大地固定 *Y* 轴的位移 | 计算 | m |
| `Z` | | 前左车轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前左车轮沿大地固定 *X* 轴的速度 | 计算 | m/s |
| `Ydot` | | 前左车轮沿大地固定 *Y* 轴的速度 | 计算 | m/s |
| `Zdot` | | 前左车轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 前右车轮沿大地固定 *X* 轴的位移 | 计算 | m |
| `Y` | | 前右车轮沿大地固定 *Y* 轴的位移 | 计算 | m |
| `Z` | | 前右车轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前右车轮沿大地固定 *X* 轴的速度 | 计算 | m/s |
| `Ydot` | | 前右车轮沿大地固定 *Y* 轴的速度 | 计算 | m/s |
| `Zdot` | | 前右车轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `RearAxl` | `Lft` | `Disp` | `X` | | 后左车轮沿大地固定 *X* 轴的位移 | 计算 | m |
| `Y` | | 后左车轮沿大地固定 *Y* 轴的位移 | 计算 | m |
| `Z` | | 后左车轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后左车轮沿大地固定 *X* 轴的速度 | 计算 | m/s |
| `Ydot` | | 后左车轮沿大地固定 *Y* 轴的速度 | 计算 | m/s |
| `Zdot` | | 后左车轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 后右车轮沿大地固定 *X* 轴的位移 | 计算 | m |
| `Y` | | 后右车轮沿大地固定 *Y* 轴的位移 | 计算 | m |
| `Z` | | 后右车轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后右车轮沿大地固定 *X* 轴的速度 | 计算 | m/s |
| `Ydot` | | 后右车轮沿大地固定 *Y* 轴的速度 | 计算 | m/s |
| `Zdot` | | 后右车轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Hitch` | `Disp` | `X` | | | 牵引点沿大地固定 *X* 轴距轴平面的偏移 | 计算 | m |
| `Y` | | | 牵引点沿大地固定 *Y* 轴距中心平面的偏移 | 计算 | m |
| `Z` | | | 牵引点沿大地固定 *Z* 轴距轴平面的偏移 | 计算 | m |
| `Vel` | `Xdot` | | | 牵引点沿大地固定 *X* 轴距轴平面的偏移速度 | 计算 | m/s |
| `Ydot` | | | 牵引点沿大地固定 *Y* 轴距中心平面的偏移速度 | 计算 | m/s |
| `Zdot` | | | 牵引点沿大地固定 *Z* 轴距轴平面的偏移速度 | 计算 | m/s |
| `Geom` | `Disp` | `X` | | | 车辆底盘沿大地固定 *X* 轴距轴平面的偏移 | 计算 | m |
| `Y` | | | 车辆底盘沿大地固定 *Y* 轴距中心平面的偏移 | 计算 | m |
| `Z` | | | 车辆底盘沿大地固定 *Z* 轴距轴平面的偏移 | 计算 | m |
| `Vel` | `Xdot` | | | 车辆底盘沿大地固定 *X* 轴的偏移速度 | 计算 | m/s |
| `Ydot` | | | 车辆底盘沿大地固定 *Y* 轴的偏移速度 | 计算 | m/s |
| `Zdot` | | | 车辆底盘沿大地固定 *Z* 轴的偏移速度 | 计算 | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | 车辆质心沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | | 车辆质心沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | | 车辆质心沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Ang` | `Beta` | | | 车身侧偏角，*β*    β=VyVx | 计算 | rad |
| `AngVel` | `p` | | | 车辆绕车辆固定 *x* 轴的角速度（侧倾角速度） | `0` | rad/s |
| `q` | | | 车辆绕车辆固定 *y* 轴的角速度（俯仰角速度） | `0` | rad/s |
| `r` | | | 车辆绕车辆固定 *z* 轴的角速度（横摆角速度） | 计算 | rad/s |
| `Acc` | `ax` | | | 车辆质心沿车辆固定 *x* 轴的惯性加速度 | 计算 | gn |
| `ay` | | | 车辆质心沿车辆固定 *y* 轴的惯性加速度 | 计算 | gn |
| `az` | | | 车辆质心沿车辆固定 *z* 轴的惯性加速度 | `0` | gn |
| `xddot` | | | 车辆质心沿车辆固定 *x* 轴的加速度，不包括离心分量 | 计算 | m/s^2 |
| `yddot` | | | 车辆质心沿车辆固定 *y* 轴的加速度，不包括离心分量 | 计算 | m/s^2 |
| `zddot` | | | 车辆质心沿车辆固定 *z* 轴的加速度，不包括离心分量 | `0` | m/s^2 |
| `AngAcc` | `pdot` | | | 车辆绕车辆固定 *x* 轴的角加速度 | `0` | rad/s |
| `qdot` | | | 车辆绕车辆固定 *y* 轴的角加速度 | `0` | rad/s |
| `rdot` | | | 车辆绕车辆固定 *z* 轴的角加速度 | 计算 | rad/s |
| `DCM` | 方向余弦矩阵 | | | | 计算 | rad |
| `Forces` | `Body` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴的净力 | 计算 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴的净力 | 计算 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴的净力 | `0` | N |
| `Ext` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴的外部力 | 计算 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴的外部力 | 计算 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴的外部力 | `0` | N |
| `Hitch` | `Fx` | | | 在牵引点位置沿车辆固定 *x* 轴施加到车体的牵引力 | 输入 | N |
| `Fy` | | | 在牵引点位置沿车辆固定 *y* 轴施加到车体的牵引力 | 输入 | N |
| `Fz` | | | 在牵引点位置沿车辆固定 *z* 轴施加到车体的牵引力 | 输入 | N |
| `FrntAxl` | `Lft` | `Fx` | | 左前轮沿车辆固定 *x* 轴的纵向力 | 计算 | N |
| `Fy` | | 左前轮沿车辆固定 *y* 轴的侧向力 | 计算 | N |
| `Fz` | | 左前轮沿车辆固定 *z* 轴的法向力 | 计算 | N |
| `Rght` | `Fx` | | 右前轮沿车辆固定 *x* 轴的纵向力 | 计算 | N |
| `Fy` | | 右前轮沿车辆固定 *y* 轴的侧向力 | 计算 | N |
| `Fz` | | 右前轮沿车辆固定 *z* 轴的法向力 | 计算 | N |
| `RearAxl` | `Lft` | `Fx` | | 左后轮沿车辆固定 *x* 轴的纵向力 | 计算 | N |
| `Fy` | | 左后轮沿车辆固定 *y* 轴的侧向力 | 计算 | N |
| `Fz` | | 左后轮沿车辆固定 *z* 轴的法向力 | 计算 | N |
| `Rght` | `Fx` | | 右后轮沿车辆固定 *x* 轴的纵向力 | 计算 | N |
| `Fy` | | 右后轮沿车辆固定 *y* 轴的侧向力 | 计算 | N |
| `Fz` | | 右后轮沿车辆固定 *z* 轴的法向力 | 计算 | N |
| `Tires` | `FrntTires` | `Lft` | `Fx` | 左前轮胎力，沿车辆固定 *x* 轴 | 计算 | N |
| `Fy` | 左前轮胎力，沿车辆固定 *y* 轴 | 计算 | N |
| `Fz` | 左前轮胎力，沿车辆固定 *z* 轴 | 计算 | N |
| `Rght` | `Fx` | 右前轮胎力，沿车辆固定 *x* 轴 | 计算 | N |
| `Fy` | 右前轮胎力，沿车辆固定 *y* 轴 | 计算 | N |
| `Fz` | 右前轮胎力，沿车辆固定 *z* 轴 | 计算 | N |
| `RearTires` | `Lft` | `Fx` | 左后轮胎力，沿车辆固定 *x* 轴 | 计算 | N |
| `Fy` | 左后轮胎力，沿车辆固定 *y* 轴 | 计算 | N |
| `Fz` | 左后轮胎力，沿车辆固定 *z* 轴 | 计算 | N |
| `Rght` | `Fx` | 右后轮胎力，沿车辆固定 *x* 轴 | 计算 | N |
| `Fy` | 右后轮胎力，沿车辆固定 *y* 轴 | 计算 | N |
| `Fz` | 右后轮胎力，沿车辆固定 *z* 轴 | 计算 |  |
| `Drag` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴的阻力 | 计算 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴的阻力 | 计算 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴的阻力 | 计算 | N |
| `Grvty` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴的重力 | 计算 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴的重力 | 计算 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴的重力 | 计算 | N |
| `Moments` | `Body` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴的车体力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴的车体力矩 | 计算 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴的车体力矩 | `0` | N·m |
| `Drag` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴的阻力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴的阻力矩 | 计算 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴的阻力矩 | `0` | N·m |
| `Ext` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴的外部力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴的外部力矩 | 计算 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴的外部力矩 | `0` | N·m |
| `Hitch` | `Mx` | | | 牵引点位置绕车辆固定 *x* 轴的牵引力矩 | `0` | N·m |
| `My` | | | 牵引点位置绕车辆固定 *y* 轴的牵引力矩 | 计算 | N·m |
| `Mz` | | | 牵引点位置绕车辆固定 *z* 轴的牵引力矩 | `0` | N·m |
| `FrntAxl` | `Lft` | `Disp` | `x` | | 前左车轮沿车辆固定 *x* 轴的位移 | 计算 | m |
| `y` | | 前左车轮沿车辆固定 *y* 轴的位移 | 计算 | m |
| `z` | | 前左车轮沿车辆固定 *z* 轴的位移 | 计算 | m |
| `Vel` | `xdot` | | 前左车轮沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 前左车轮沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 前左车轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 前右车轮沿车辆固定 *x* 轴的位移 | 计算 | m |
| `y` | | 前右车轮沿车辆固定 *y* 轴的位移 | 计算 | m |
| `z` | | 前右车轮沿车辆固定 *z* 轴的位移 | 计算 | m |
| `Vel` | `xdot` | | 前右车轮沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 前右车轮沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 前右车轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngFL` | | | 前左车轮转向角 | 计算 | rad |
| `WhlAngFR` | | | 前右车轮转向角 | 计算 | rad |
| `RearAxl` | `Lft` | `Disp` | `x` | | 后左车轮沿车辆固定 *x* 轴的位移 | 计算 | m |
| `y` | | 后左车轮沿车辆固定 *y* 轴的位移 | 计算 | m |
| `z` | | 后左车轮沿车辆固定 *z* 轴的位移 | 计算 | m |
| `Vel` | `xdot` | | 后左车轮沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 后左车轮沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 后左车轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 后右车轮沿车辆固定 *x* 轴的位移 | 计算 | m |
| `y` | | 后右车轮沿车辆固定 *y* 轴的位移 | 计算 | m |
| `z` | | 后右车轮沿车辆固定 *z* 轴的位移 | 计算 | m |
| `Vel` | `xdot` | | 后右车轮沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 后右车轮沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 后右车轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 后左车轮转向角 | 计算 | rad |
| `WhlAngRR` | | | 后右车轮转向角 | 计算 | rad |
| `Hitch` | `Disp` | | `x` | | 牵引点沿车辆固定 *x* 轴距轴平面的偏移 | 输入 | m |
| `y` | | 牵引点沿车辆固定 *y* 轴距中心平面的偏移 | 输入 | m |
| `z` | | 牵引点沿车辆固定 *z* 轴距轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 牵引点沿车辆固定 *x* 轴的偏移速度 | 计算 | m/s |
| `ydot` | | 牵引点沿车辆固定 *y* 轴的偏移速度 | 计算 | m/s |
| `zdot` | | 牵引点沿车辆固定 *z* 轴的偏移速度 | 计算 | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | 计算 | W |
| `Hitch` | | | | 牵引点导致的功率损耗 | 计算 | W |
| `Drag` | | | | 阻力导致的功率损耗 | 计算 | W |
| `Geom` | `Disp` | | `x` | | 车辆底盘沿车辆固定 *x* 轴距轴平面的偏移 | 输入 | m |
| `y` | | 车辆底盘沿车辆固定 *y* 轴距中心平面的偏移 | 输入 | m |
| `z` | | 车辆底盘沿大地固定 *z* 轴距轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 车辆底盘沿车辆固定 *x* 轴的偏移速度 | 计算 | m/s |
| `ydot` | | 车辆底盘沿车辆固定 *y* 轴的偏移速度 | 计算 | m/s |
| `zdot` | | 车辆底盘沿车辆固定 *z* 轴的偏移速度 | `0` | m/s |
| `Beta` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | 计算 | rad |

| 信号 | | | 描述 | | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | 外部施加的纵向力功率 | | 计算值 | W |
| `PwrFyExt` | 外部施加的横向力功率 | | 计算值 | W |
| `PwrMzExt` | 外部施加的侧倾力矩功率 | | 计算值 | W |
| `PwrFwFLx` | 施加在前左轴上的纵向力功率 | | 计算值 | W |
| `PwrFwFLy` | 施加在前左轴上的横向力功率 | | 计算值 | W |
| `PwrFwFRx` | 施加在前右轴上的纵向力功率 | | 计算值 | W |
| `PwrFwFRy` | 施加在前右轴上的横向力功率 | | 计算值 | W |
| `PwrFwRLx` | 施加在后左轴上的纵向力功率 | | 计算值 | W |
| `PwrFwRLy` | 施加在后左轴上的横向力功率 | | 计算值 | W |
| `PwrFwRRx` | 施加在后右轴上的纵向力功率 | | 计算值 | W |
| `PwrFwRRy` | 施加在后右轴上的横向力功率 | | 计算值 | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | 纵向阻力功率 | | 计算值 | W |
| `PwrFyDrag` | 横向阻力功率 | | 计算值 | W |
| `PwrMzDrag` | 阻力俯仰力矩功率 | | 计算值 | W |
| `PwrStored` | `PwrStoredGrvty` | 重力势能变化率 | | 计算值 | W |
| `PwrStoredxdot` | 纵向动能变化率 | | 计算值 | W |
| `PwrStoredydot` | 横向动能变化率 | | 计算值 | W |
| `PwrStoredr` | 旋转横摆动能变化率 | | 计算值 | W |

### **xdot** — 车辆纵向速度 `scalar`

车辆质心沿车辆固定 *x* 轴的速度，
单位为 m/s。

### **ydot** — 车辆横向速度 `scalar`

车辆质心沿车辆固定 *y* 轴的速度，
单位为 m/s。

### **psi** — 横摆 `scalar`

车辆固定坐标系绕地球固定
*Z* 轴的旋转（横摆），单位为 rad。

### **r** — 横摆角速度 `scalar`

车辆角速度 `r`，绕
车辆固定 *z* 轴（横摆角速度），单位为 rad/s。

### **FzF** — 前轮上的法向力 `scalar` | `array`

前轮上的法向力，
*FzF*，沿车辆固定
*z* 轴，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single (bicycle)` | 前轴上的法向力 | FzF=Fzf | Scalar – `1` |
| `Dual` | 前轮上的法向力 | FzF=[FzflFzfr] | Array – `[1x2]` |

### **FzR** — 后轮上的法向力 `scalar` | `array`

后轮上的法向力，
*FzR*，沿车辆固定
*z* 轴，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single (bicycle)` | 后轮上的法向力 | FzR=Fzr | Scalar – `1` |
| `Dual` | 后轮上的法向力 | FzR=[FzrlFzrr] | Array – `[1x2]` |

## 参数

#### 选项

### **Vehicle track** — 车轮数量 `Single (bicycle)` | `Dual`

在 Vehicle Dynamics Blockset 库中，有两种类型的 Vehicle Body 3DOF 模块，用于建模
纵向、横向和横摆运动。

| 模块 | Vehicle Track 设置 | 实现 |
| --- | --- | --- |
| Vehicle Body 3DOF Single TrackVehicle Body 3DOF block single track | `Single (bicycle)` | - 力沿前轴和后轴的中心线作用。 - 无横向载荷转移。 |
| Vehicle Body 3DOF Dual TrackVehicle Body 3DOF block | `Dual` | 力作用在车辆四个角或 *硬点*。 |

### **Axle forces** — 轴力类型 `External longitudinal velocity` | `External longitudinal forces` | `External forces`

使用 **Axle forces** 参数指定
力的类型。

| Axle Forces 设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 模块假设外部纵向速度为准稳态，因此纵向加速度近似为零。 - 由于运动为准稳态，模块使用轮胎侧偏角和线性侧偏刚度计算横向力。 - 在以下情况下考虑此设置：  - 生成虚拟传感器信号数据。   - 进行不受传动系或非线性轮胎响应影响的高级软件研究。 |
| `External longitudinal forces` | - 模块使用外部纵向力来加速或制动车辆。 - 模块使用轮胎侧偏角和线性侧偏刚度计算横向力。 - 在以下情况下考虑此设置：  - 考虑纵向速度变化对横向和横摆运动的影响。   - 通过力而不是外部纵向速度来指定外部纵向运动。   - 将模块连接到牵引执行器、车轮、制动器和牵引装置。 |
| `External forces` | - 模块使用外部横向力和纵向力来转向、加速或制动车辆。 - 模块不使用转向输入来计算车辆运动。 - 当您需要具有更准确的非线性组合横向和纵向滑移的轮胎模型时，考虑此设置。 |

#### 输入信号

### **Front wheel steering** — `WhlAngF` 输入端口 `on`（默认） | `off`

指定以创建输入端口 `WhlAngF`。

### **External wind** — `WindXYZ` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `WindXYZ`。

### **External forces** — `FExt` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `FExt`。

### **External moments** — `MExt` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `MExt`。

### **Rear wheel steering** — `WhlAngR` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `WhlAngR`。

### **External friction** — `Mu` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `Mu`。

### **Hitch forces** — `Fh` 输入端口 `off`（默认） | `on`

选择以创建输入端口 `Fh`。

### **Hitch moments** — `Mh` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `Mh`。

### **Initial longitudinal position** — `X_o` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `X_o`。

### **Initial lateral position** — `Y_o` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `Y_o`。

### **Initial longitudinal velocity** — `xdot_o` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `xdot_o`。

### **Initial lateral velocity** — `ydot_o` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `ydot_o`。

### **Initial yaw angle** — `psi_o` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `psi_o`。

### **Initial yaw rate** — `r_o` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `r_o`。

### **Air temperature** — `AirTemp` 输入端口 `off`（默认） | `on`

指定以创建输入端口 `AirTemp`。

#### 纵向

### **Number of wheels on front axle, NF** — 前轮数量 `2`（默认） | `scalar`

前轴上的车轮数量，*NF*。该
值无量纲。

### **Number of wheels on rear axle, NR** — 后轮数量 `2`（默认） | `scalar`

后轴上的车轮数量，*NR*。该
值无量纲。

### **Vehicle mass, m** — 车辆质量 `2000`（默认） | `scalar`

车辆质量，*m*，单位为 kg。

### **Longitudinal distance from center of mass to front axle, a** — 前轴距离 `1.4`（默认） | `scalar`

从车辆质心到前轮
轴的水平距离 *a*，单位为 m。

### **Longitudinal distance from center of mass to rear axle, b** — 后轴距离 `1.6`（默认） | `scalar`

从车辆质心到后轮
轴的水平距离 *b*，单位为 m。

### **Vertical distance from center of mass to axle plane, h** — 高度 `0.35`（默认） | `scalar`

车辆质心高于车轴的高度，*h*，单位为 m。

### **Longitudinal distance from center of mass to hitch, dh** — 从质心到牵引装置的距离 `1`（默认） | `scalar`

从质心到牵引装置的纵向距离，*dh*，单位为
m。

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，
选择 **Hitch forces** 或 **Hitch
moments**。

### **Vertical distance from hitch to axle plane, hh** — 从牵引装置到车轴平面的距离 `0.2`（默认） | `scalar`

从牵引装置到车轴平面的垂直距离，*hh*，单位为 m。

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，
选择 **Hitch forces** 或 **Hitch
moments**。

### **Initial inertial frame longitudinal position, X\_o** — 位置 `0`（默认） | `scalar`

车辆质心沿地球固定 *X* 轴的初始位移，单位为
m。

### **Initial longitudinal velocity, xdot\_o** — 速度 `0`（默认） | `scalar`

车辆质心沿车辆固定 *x* 轴的初始速度，单位为
m/s。

#### 依赖关系

对于 Vehicle Body 3DOF Single Track 或 Vehicle Body
3DOF Dual Track 模块，要启用此参数，请将 **Axle
forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

#### 横向

### **Front tire corner stiffness, Cy\_f** — 刚度 `12e3`（默认） | `scalar`

前轮胎侧偏刚度，*Cyf*，单位为
N/rad。

#### 依赖关系

对于 Vehicle Body 3DOF Single Track 或 Vehicle Body 3DOF Dual
Track 模块，要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 清除 **Mapped corner stiffness**。

### **Rear tire corner stiffness, Cy\_r** — 刚度 `11e3`（默认） | `scalar`

后轮胎侧偏刚度，*Cyr*，单位为
N/rad。

#### 依赖关系

对于 Vehicle Body 3DOF Single Track 或 Vehicle Body 3DOF Dual
Track 模块，要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 清除 **Mapped corner stiffness**。

### **Initial inertial frame lateral displacement, Y\_o** — 位置 `0`（默认） | `scalar`

车辆质心沿地球固定 *Y* 轴的初始位移，单位为
m。

### **Initial lateral velocity, ydot\_o** — 速度 `0`（默认） | `scalar`

车辆质心沿车辆固定 *y* 轴的初始速度，单位为
m/s。

### **Mapped corner stiffness** — 选择 `off`（默认） | `on`

启用映射侧偏刚度计算。

#### 依赖关系

要启用此参数，请将 **Axle forces** 设置为以下选项
之一：

- `External longitudinal
  velocity`
- `External longitudinal
  forces`

### **Include relaxation length dynamics** — 启用松弛长度动力学 `on`（默认） | `off`

启用松弛长度动力学。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Lateral distance from geometric centerline to center of mass, d** — 距离 `0`（默认） | `scalar`

沿车辆固定
*y* 从几何中心线到质心的横向距离，
*d*，单位为 m。正值表示车辆质心
位于几何中心线的右侧。负值表示
车辆质心位于几何中心线的左侧。

### **Lateral distance from geometric centerline to hitch, hl** — 距离 `0`（默认） | `scalar`

沿车辆固定
*y* 从几何中心线到牵引装置的横向距离，
*hl*，单位为 m。正值表示牵引装置
位于几何中心线的右侧。负值表示
牵引装置位于几何中心线的左侧。

#### 依赖关系

要启用此参数，请在 **Input signals**
窗格中，选择 **Hitch forces** 或 **Hitch
moments**。

### **Track width** — 宽度 `[1.4,1.4]`（默认） | `1`-by-`2` `vector`

轮距，*w*，单位为 m。

#### 依赖关系

要启用此参数，请将 **Vehicle track** 设置为
`Dual`。

### **Front tire(s) relaxation length, sigma\_f** — 松弛长度 `.1`（默认） | `scalar`

前轮胎松弛长度，
*σf*，单位为 m。

#### 依赖关系

要启用此参数：

1. 将 **Vehicle track** 设置为以下选项之一：

   - `Single 2-axle`
   - `Dual 2-axle`
   - `Single 3-axle`
   - `Dual 3-axle`
2. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
3. 执行以下任一操作：

   - 选择 **Mapped corner stiffness**。
   - 清除 **Mapped corner stiffness** 并选择
     **Include relaxation length dynamics**。

### **Rear tire(s) relaxation length, sigma\_r** — 松弛长度 `.1`（默认） | `scalar`

后轮胎松弛长度，*σr*，
单位为 m。

#### 依赖关系

要启用此参数：

1. 将 **Vehicle track** 设置为以下选项之一：

   - `Single 2-axle`
   - `Dual 2-axle`
   - `Single 3-axle`
   - `Dual 3-axle`
2. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
3. 执行以下任一操作：

   - 选择 **Mapped corner stiffness**。
   - 清除 **Mapped corner stiffness** 并选择
     **Include relaxation length dynamics**。

### **Front axle slip angle breakpoints, alpha\_f\_brk** — 断点 `[-.1 .1]`（默认） | `vector`

前轴侧偏角断点，
*αfbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Front axle corner data, Cy\_f\_data** — 断点 `[-9e3 9e3]`（默认） | `vector`

前轴侧偏数据，*Cyfdata*，
单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Rear axle slip angle breakpoints, alpha\_r\_brk** — 断点 `[-.1 .1]`（默认） | `vector`

后轴侧偏角断点，
*αrbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Rear axle corner data, Cy\_r\_data** — 数据 `[-9e3 9e3]`（默认） | `vector`

后轴侧偏数据，*Cyrdata*，
单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

#### 横摆

### **Yaw polar inertia, Izz** — 惯性 `4000`（默认） | `scalar`

横摆极惯性，单位为 kg\*m^2。

### **Initial yaw angle, psi\_o** — Psi 旋转 `0`（默认） | `scalar`

车辆固定坐标系绕地球固定 *Z* 轴的旋转
（横摆），单位为 rad。

### **Initial yaw rate, r\_o** — 横摆角速度 `0`（默认） | `scalar`

车辆绕车辆固定 *z* 轴的角速度（横摆
角速度），单位为 rad/s。

#### 空气动力学

### **Longitudinal drag area, Af** — 车辆有效横截面积 `2`（默认） | `scalar`

车辆有效横截面积，
*Af*，用于计算
车辆上的空气阻力，单位为
m2。

### **Longitudinal drag coefficient, Cd** — 空气阻力系数 `.3`（默认） | `scalar`

空气阻力系数，*Cd*。该
值无量纲。

### **Longitudinal lift coefficient, Cl** — 空气升力系数 `.1`（默认） | `scalar`

空气升力系数，*Cl*。该
值无量纲。

### **Longitudinal drag pitch moment, Cpm** — 俯仰阻力 `.1`（默认） | `scalar`

纵向阻力俯仰力矩系数，
*Cpm*。该值
无量纲。

### **Relative wind angle vector, beta\_w** — 风角 `[0:0.01:0.3]`（默认） | `vector`

相对风角向量，*βw*，
单位为 rad。

### **Side force coefficient vector, Cs** — 侧向力系数 `[0 0.01:0.01:0.3]`（默认） | `vector`

侧向力系数向量系数，
*Cs*。该值
无量纲。

### **Yaw moment coefficient vector, Cym** — 横摆力矩阻力 `[0 1e-6:0.01:0.3]`（默认） | `vector`

横摆力矩系数向量，
*Cym*。该值
无量纲。

#### 环境

### **绝对压力, Pabs** — 压力 `101325`（默认） | `scalar` | `scalar`

环境绝对压力，*Pabs*，单位为 Pa。

### **空气温度, Tair** — 温度 `273`（默认） | `scalar`

环境绝对温度，*T*，单位为 K。

#### 依赖项

要启用此参数，请清除 **空气温度**。

### **重力加速度, g** — 重力 `9.81`（默认） | `scalar`

重力加速度，*g*，单位为 m/s^2。

### **标称摩擦缩放因子, mu** — 摩擦缩放因子 `1`（默认） | `scalar`

标称摩擦缩放因子，*μ*。该值无量纲。

#### 依赖项

对于 Vehicle Body 3DOF Single Track 或 Vehicle Body 3DOF Dual Track 模块，要启用此参数：

1. 将 **车轴力** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **外部摩擦**。

#### 仿真

### **纵向速度容差, xdot\_tol** — 容差 `.01`（默认） | `scalar`

纵向速度容差，单位为 m/s。

### **标称法向力, Fznom** — 法向力 `5000`（默认） | `scalar`

标称法向力，单位为 N。

#### 依赖项

对于 Vehicle Body 3DOF Single Track 或 Vehicle Body 3DOF Dual Track 模块，要启用此参数，请将 **车轴力** 设置为以下选项之一：

- `External longitudinal velocity`
- `External longitudinal forces`

### **从车轴平面的几何纵向偏移, longOff** — 纵向偏移 `0`（默认） | `scalar`

车辆底盘沿车身固定 *x* 轴相对于车轴平面的偏移，单位为 m。使用 3D 可视化引擎时，请考虑使用该偏移量来定位底盘，使其独立于车辆 CG。

### **从中心平面的几何横向偏移, latOff** — 横向偏移 `0`（默认） | `scalar`

车辆底盘沿车身固定 *y* 轴相对于中心平面的偏移，单位为 m。使用 3D 可视化引擎时，请考虑使用该偏移量来定位底盘，使其独立于车辆 CG。

### **从车轴平面的几何垂直偏移, vertOff** — 垂直偏移 `0`（默认） | `scalar`

车辆底盘沿车身固定 *z* 轴相对于车轴平面的偏移，单位为 m。使用 3D 可视化引擎时，请考虑使用该偏移量来定位底盘，使其独立于车辆 CG。

### **环绕欧拉角, wrapAng** — 选择 `off`（默认） | `on`

将欧拉角环绕到区间 `[-pi, pi]`。对于可能经历超出该区间的车辆横摆旋转的车辆机动，如果希望执行以下操作，请考虑取消选择此参数：

- 跟踪车辆总横摆旋转。
- 避免车辆状态估计器中出现不连续。

## 所属库

Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

用于计算纵向、横向和横摆运动的 3DOF 刚性车体

Vehicle Body 3DOF 模块实现刚性双轴车体模型，以计算纵向、横向和横摆运动。该模块考虑了车身质量以及因加速和转向在车轴之间产生的空气动力阻力。

在车辆动力学和自动驾驶研究中，当车辆俯仰、侧倾和垂直运动不显著时，可使用此模块对非完整车辆运动进行建模。

在 Vehicle Dynamics Blockset™ 库中，有两种类型的 Vehicle Body 3DOF 模块，用于对纵向、横向和横摆运动进行建模。

| 模块 | 车辆轨迹设置 | 实现 |
| --- | --- | --- |
| Vehicle Body 3DOF Single TrackVehicle Body 3DOF block single track | `Single (bicycle)` | - 力沿前轴和后轴的中心线作用。 - 无侧向载荷转移。 |
| Vehicle Body 3DOF Dual TrackVehicle Body 3DOF block | `Dual` | 力作用在四个车辆角点或 *硬点*。 |

使用 **车轴力** 参数指定力的类型。

| 车轴力设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 该模块假设外部纵向速度处于准稳态，因此纵向加速度近似为零。 - 由于运动是准稳态的，该模块使用轮胎滑移角和线性侧偏刚度计算侧向力。 - 当您希望执行以下操作时，请考虑此设置：  - 生成虚拟传感器信号数据。   - 开展不受动力传动系统或非线性轮胎响应影响的高级软件研究。 |
| `External longitudinal forces` | - 该模块使用外部纵向力使车辆加速或制动。 - 该模块使用轮胎滑移角和线性侧偏刚度计算侧向力。 - 当您希望执行以下操作时，请考虑此设置：  - 考虑纵向速度变化对侧向和横摆运动的影响。   - 通过力而不是外部纵向速度来指定外部纵向运动。   - 将该模块连接到牵引执行器、车轮、制动器和挂钩。 |
| `External forces` | - 该模块使用外部侧向和纵向力来转向、加速或制动车辆。 - 该模块不使用转向输入来计算车辆运动。 - 当您需要具有更准确的非线性组合侧向和纵向滑移的轮胎模型时，请考虑此设置。 |

您可以使用这些模块参数创建附加输入端口。下表汇总了这些设置。

| 输入信号窗格参数 | 输入端口 | 描述 |
| --- | --- | --- |
| **前轮转向** | `WhlAngF` | 前轮角度，*δF* |
| **外部风** | `WindXYZ` | 惯性参考系中的风速，*WX*、*WY*、*WZ* |
| **外部力** | `FExt` | 车辆固定坐标系中作用在车辆重心 (CG) 上的外部力，*Fx*、*Fy*、*Fz* |
| **后轮转向** | `WhlAngR` | 后轮角度，*δR* |
| **外部摩擦** | `Mu` | 摩擦系数 |
| **外部力矩** | `MExt` | 车辆固定坐标系中绕车辆 CG 的外部力矩，*Mx*、*My*、*Mz* |
| **挂钩力** | `Fh` | 在车辆固定坐标系中，施加到挂钩位置车体上的挂钩力，*Fhx*、*Fhy* 和 *Fhz* |
| **挂钩力矩** | `Mh` | 在车辆固定坐标系中，挂钩位置处的挂钩力矩，*Mhx*、*Mhy* 和 *Mhz* |
| **初始纵向位置** | `X_o` | 沿地球固定 *X* 轴的初始车辆 CG 位移，单位为 m |
| **初始横向位置** | `Y_o` | 沿地球固定 *Y* 轴的初始车辆 CG 位移，单位为 m |
| **初始纵向速度** | `xdot_o` | 沿车辆固定 *x* 轴的初始车辆 CG 速度，单位为 m/s |
| **初始横向速度** | `ydot_o` | 沿车辆固定 *y* 轴的初始车辆 CG 速度，单位为 m/s |
| **初始横摆角** | `psi_o` | 车辆固定坐标系绕地球固定 *Z* 轴的初始旋转（横摆），单位为 rad |
| **初始横摆角速度** | `r_o` | 绕车辆固定 *z* 轴的初始车辆角速度（横摆角速度），单位为 rad/s |
| **空气温度** | `AirTemp` | 环境空气温度。如果您希望在运行期间改变温度，请考虑此选项。 |

### 理论

Vehicle Body 3DOF 模块实现刚性双轴车身模型，以计算纵向、横向和横摆运动。该模块考虑车身质量、空气动力阻力以及由于加速和转向引起的车轴间重量分配。为确定车辆运动，该模块针对单轨、双轨和阻力计算实现这些方程。

**单轨**

| 计算 | 描述 |
| --- | --- |
| *动力学* | 该模块使用这些方程计算刚体平面动力学。  y¨=−x˙r+Fyf+Fyr+Fyextmr˙=aFyf−bFyr+MzextIzzr=ψ˙  如果将 **Axle forces** 设置为 `External longitudinal forces` 或 `External forces`，该模块使用此方程计算纵向加速度。  x¨=y˙r+Fxf+Fxr+Fxextm  如果将 **Axle forces** 设置为 `External longitudinal velocity`，该模块假设纵向加速度为准稳态。  x¨=0 |
| *外力* | 外力包括阻力和外部力输入。这些力作用在车辆 CG 上。  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    如果将 **Axle forces** 设置为 `External longitudinal forces`，该模块使用这些方程。  Fxft=FxfinputFyft=−CyfαfμfFzfFznomFxrt=FxrinputFyrt=−CyrαrμrFzrFznom    如果将 **Axle forces** 设置为 `External longitudinal velocity`，该模块使用这些方程。  Fxft=0Fyft=−CyfαfμfFzfFznomFxrt=0Fyrt=−CyrαrμrFzrFznom    该模块将法向力除以标称法向载荷，以在重量和载荷转移期间改变有效摩擦参数。该模块使用这些方程来保持俯仰和侧倾平衡。  Fzf=bmg−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amg+(x¨−y˙r)mh−hFxext+aFzext+Myexta+b |
| *轮胎力* | 该模块使用局部纵向速度和横向速度的比值确定侧滑角。  αf=atan(y˙+arx˙)−δfαr=atan(y˙−brx˙)−δr    为确定轮胎力，该模块使用侧滑角。  Fxf=Fxftcos(δf)−Fyftsin(δf)Fyf=−Fxftsin(δf)+Fyftcos(δf)Fxr=Fxrtcos(δr)−Fyrtsin(δr)Fyr=−Fxrtsin(δr)+Fyrtcos(δr)    如果将 **Axle forces** 设置为 `External forces`，该模块将轮胎力设置为等于外部输入力。  Fxf=Fxft=FxfinputFyf=Fyft=FyfinputFxr=Fxrt=FxrinputFyr=Fyrt=Fyrinput |

**双轨**

作用在悬架位置处的垂向、纵向和横向力的等轴测视图

| 计算 | 描述 |
| --- | --- |
| *动力学* | 该模块使用这些方程计算刚体平面动力学。  x¨=y˙r+Fxfl+Fxfr+Fxrl+Fxrr+Fxextmy¨=−x˙r+Fyfl+Fyfr+Fyrl+Fyrr+Fyextmr˙=a(Fyfl+Fyfr)−b(Fyrl+Fyrr)+wf(Fxfl−Fxfr)2+wr(Fxrl−Fxrr)2+MzextIzzr=ψ˙  如果将 **Axle forces** 设置为 `External longitudinal velocity`，该模块假设纵向加速度为准稳态。  x¨=0 |
| *外力* | 外力包括阻力和外部力输入。这些力作用在车辆 CG 上。  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    如果将 **Axle forces** 设置为 `External longitudinal forces`，该模块使用这些方程。  Fxflt=FxflinputFyflt=−CyflαflμflFzfl2FznomFxfrt=FxlrinputFyfrt=−CyfrαfrμfrFzfr2FznomFxrlt=FxrlinputFyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=FxrrinputFyrrt=−CyrrαrrμrrFzrr2Fznom    如果将 **Axle forces** 设置为 `External longitudinal velocity`，该模块使用这些方程。  Fxflt=0Fyflt=−CyflαflμflFzfl2FznomFxfrt=0Fyfrt=−CyfrαfrμfrFzfr2FznomFxrlt=0Fyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=0Fyrrt=−CyrrαrrμrrFzrr2Fznom    该模块将法向力除以标称法向载荷，以在重量和载荷转移期间改变有效摩擦参数。该模块使用这些方程来保持俯仰和侧倾平衡。  Fzf=bmg−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amg+(x¨−y˙r)mh−hFxext+aFzext+Myext(a+b)Fzfl=Fzf+(mh(y¨+x˙r)−hFyext−Mxext)2wfFzfr=Fzf+(−mh(y¨+x˙r)+hFyext+Mxext)2wfFzrl=Fzr+(mh(y¨+x˙r)−hFyext−Mxext)2wrFzrr=Fzr+(−mh(y¨+x˙r)+hFyext+Mxext)2wr |
| *轮胎力* | 该模块使用局部纵向速度和横向速度的比值确定侧滑角。  αfl=atan(y˙+arx˙+rwf2)−δflαfr=atan(y˙+arx˙−rwf2)−δfrαrl=atan(y˙−arx˙+rwr2)−δrlαrr=atan(y˙−arx˙−rwr2)−δrr    该模块使用转向角将轮胎力变换到车辆固定坐标系。  Fxfl=Fxfltcos(δfl)−Fyfltsin(δfl)Fxfr=Fxfrtcos(δfr)−Fyfrtsin(δfr)Fyfl=−Fxfltsin(δfl)+Fyfltcos(δfl)Fyfr=−Fxfrtsin(δfr)+Fyfrtcos(δfr)Fxrl=Fxrltcos(δrl)−Fyrltsin(δrl)Fxrr=Fxrrtcos(δrr)−Fyrrtsin(δrr)Fyrl=−Fxrltsin(δrl)+Fyrltcos(δrl)Fyrr=−Fxrrtsin(δrr)+Fyrrtcos(δrr)    如果将 **Axle forces** 设置为 `External forces`，该模块使用这些方程。该模块假设外部提供的力位于车轴-车轮位置处的车辆固定坐标系中。  Fxfl=Fxflt=FxflinputFxfr=Fxfrt=FxfrinputFyfl=Fyflt=FyflinputFyfr=Fyfrt=FyfrinputFxrl=Fxrlt=FxrlinputFyrr=Fyrrt=Fyrrinput |

**阻力**

| 计算 | 描述 |
| --- | --- |
| *坐标变换* | 该模块将风速从惯性坐标系变换到车辆固定坐标系。  wx=Wxcos(ψ)+Wysin(ψ)wy=Wycos(ψ)−Wxsin(ψ)wz=Wz |
| *阻力* | 为确定相对空速，该模块从 CG 车辆速度中减去风速。使用相对空速，该模块确定阻力。  w¯=(x˙−wx)2+(y˙−wy)2+(wz)2Fdx=−12TRCdAfPabs(w¯)2Fdy=−12TRCsAfPabs(w¯)2Fdz=−12TRClAfPabs(w¯)2 |
| *阻力矩* | 使用相对空速，该模块确定阻力矩。  Mdr=−12TRCrmAfPabs(w¯)2(a+b)Mdp=−12TRCpmAfPabs(w¯)2(a+b)Mdy=−12TRCymAfPabs(w¯)2(a+b) |

**侧偏刚度和松弛动力学**

| 描述 | 实现 |
| --- | --- |
| *常量值。* | 该模块对 *Cyf* 和 *Cyr* 使用常量刚度值。 |
| *作为侧偏刚度数据和侧滑角函数的查找表。* | 该模块使用作为侧偏刚度数据和侧滑角函数的查找表。  Cyf=f(αf,Cyfdata)Cyr=f(αr,Cyrdata) |
| *作为侧偏刚度数据和侧滑角函数的查找表。*  *侧滑角包括松弛长度动态设置。* | 该模块使用作为侧偏刚度数据和侧滑角函数的查找表。侧滑角包括松弛长度动态设置。松弛长度近似表示作为车轮行程函数的有效侧偏刚度力。  Cyf=f(αfσ,Cyfdata)Cyr=f(αrσ,Cyrdata)αfσ=1s[(αf−αfσ)vwfαf]αrσ=1s[(αr−αrσ)vwrαr] |

这些方程使用以下变量。

|  |  |
| --- | --- |
| x,x˙,x¨ | 车辆 CG 沿车辆固定 *x* 轴的位移、速度和加速度 |
| y,y˙,y¨ | 车辆 CG 沿车辆固定 *y* 轴的位移、速度和加速度 |
| *ψ* | 车辆固定坐标系绕大地固定 *Z* 轴的旋转（横摆） |
| *r*,Ψ˙ | 车辆绕车辆固定 *z* 轴的角速度（横摆角速度） |
| *Fxf*, *Fxr* | 施加到前轮和后轮的、沿车辆固定 *x* 轴的纵向力 |
| *Fyf*, *Fyr* | 施加到前轮和后轮的、沿车辆固定 *y* 轴的横向力 |
| *Fxext*, *Fyext*, *Fzext* | 施加到车辆 CG 的、沿车辆固定 *x*、*y* 和 *z* 轴的外力 |
| *Fdx*, *Fdy*, *Fdz* | 施加到车辆 CG 的、沿车辆固定 *x*、*y* 和 *z* 轴的阻力 |
| *Fxinput*, *Fyinput*, *Fzinput* | 施加到车辆 CG 的、沿车辆固定 *x*、*y* 和 *z* 轴的输入力 |
| *Mxext*, *Myext*, *Mzext* | 绕车辆 CG 的、绕车辆固定 *x*、*y* 和 *z* 轴的外力矩 |
| *Mdx*, *Mdy*, *Mdz* | 绕车辆 CG 的、绕车辆固定 *x*、*y* 和 *z* 轴的阻力矩 |
| *Mxinput*, *Myinput*, *Mzinput* | 绕车辆 CG 的、绕车辆固定 *x*、*y* 和 *z* 轴的输入力矩 |
| *Izz* | 车辆车身绕车辆固定 *z* 轴的转动惯量 |
| *Fxft*, *Fxrt* | 施加到前轮和后轮的、沿车辆固定 *x* 轴的纵向轮胎力 |
| *Fyft*, *Fyft* | 施加到前轮和后轮的、沿车辆固定 *y* 轴的横向轮胎力 |
| *Fxfl*, *Fxfr* | 施加到左前轮和右前轮的、沿车辆固定 *x* 轴的纵向力 |
| *Fyfl*, *Fyfr* | 施加到左前轮和右前轮的、沿车辆固定 *y* 轴的横向力 |
| *Fxrl*, *Fxrr* | 施加到左后轮和右后轮的、沿车辆固定 *x* 轴的纵向力 |
| *Fyrl*, *Fyrr* | 施加到左后轮和右后轮的、沿车辆固定 *y* 轴的横向力 |
| *Fxflt*, *Fxfrt* | 施加到左前轮和右前轮的、沿车辆固定 *x* 轴的纵向轮胎力 |
| *Fyflt*, *Fyfrt* | 施加到左前轮和右前轮的、沿车辆固定 *y* 轴的横向轮胎力 |
| *Fxrlt*, *Fxrrt* | 施加到左后轮和右后轮的、沿车辆固定 *x* 轴的纵向轮胎力 |
| *Fyrlt*, *Fyrrt* | 施加到左后轮和右后轮的、沿车辆固定 *y* 轴的横向力 |
| *Fzf*,*Fzr* | 施加到前轮和后轮的、沿车辆固定 *z* 轴的法向力 |
| *Fznom* | 施加到车轴的、沿车辆固定 *z* 轴的标称法向力 |
| *Fzfl*,*Fzfr* | 施加到左前轮和右前轮的、沿车辆固定 *z* 轴的法向力 |
| *Fzrl*,*Fzrr* | 施加到左后轮和右后轮的、沿车辆固定 *z* 轴的法向力 |
| *m* | 车辆车身质量 |
| *a*, *b* | 前轮和后轮分别距车辆 CG 在公共车轴平面上的法向投影点的距离 |
| *h* | 车辆 CG 高于车轴平面的高度 |
| *d* | 沿车辆固定 *y* 轴从几何中心线到质心的横向距离 |
| *hh* | 沿车辆固定 *z* 轴，牵引点高于车轴平面的高度 |
| *dh* | 牵引点距牵引车 CG 在公共车轴平面上的法向投影点的纵向距离 |
| *hl* | 沿车辆固定 *y* 轴从质心到牵引点的横向距离。 |
| *αf*, *αr* | 前轮和后轮侧滑角 |
| *αfl*, *αfr* | 左前轮和右前轮侧滑角 |
| *αrl*, *αrr* | 左后轮和右后轮侧滑角 |
| *δf*, *δr* | 前轮和后轮转向角 |
| *δrl*, *δrr* | 左后轮和右后轮转向角 |
| *δfl*, *δfr* | 左前轮和右前轮转向角 |
| *wf*, *wr* | 前轮距和后轮距 |
| *Cyf*, *Cyr* | 前轮和后轮侧偏刚度 |
| *Cyfdata*, *Cyrdata* | 前轮和后轮侧偏刚度数据 |
| *σf*, *σr* | 前轮和后轮松弛长度 |
| *αfσ*, *αrσ* | 包含松弛长度的前轮和后轮侧滑角 |
| *vwf*, *vwr* | 前轮和后轮硬点速度的大小 |
| *μf*, *μr* | 前轮和后轮摩擦系数 |
| *μfl*, *μfr* | 左前轮和右前轮摩擦系数 |
| *μrl*, *μrr* | 左后轮和右后轮摩擦系数 |
| *Cd* | 沿车辆固定 *x* 轴作用的空气阻力系数 |
| *Cs* | 沿车辆固定 *y* 轴作用的空气阻力系数 |
| *Cl* | 沿车辆固定 *z* 轴作用的空气阻力系数 |
| *Crm* | 绕车辆固定 *x* 轴作用的空气阻力侧倾力矩 |
| *Cpm* | 绕车辆固定 *y* 轴作用的空气阻力俯仰力矩 |
| *Cym* | 绕车辆固定 *z* 轴作用的空气阻力横摆力矩 |
| *Af* | 迎风面积 |
| *R* | 大气比气体常数 |
| *T* | 环境空气温度 |
| *Pabs* | 环境绝对压力 |
| *wx*, *wy*, *wz* | 沿车辆固定 *x*、*y* 和 *z* 轴的风速 |
| *Wx*, *Wy*, *Wz* | 沿惯性 *X*、*Y* 和 *Z* 轴的风速 |
