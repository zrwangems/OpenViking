---
type: simulink-block
title: 'Vehicle Body 3DOF Three Axles'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Motion'
documentation_page: 'vehiclebody3dofthreeaxles'
documentation_source_path: 'ref/vehiclebody3dofthreeaxles.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Body 3DOF Three Axles

## 端口

### 输入

### **WhlAngF** — 前轮转向角 `scalar` | `array`

前轮转向角，*δF*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | *δF* | Scalar – `1` |
| `Dual` | δF=[δflδfr] 或 [δflδfr] | Array – `[1x2]` 或 `[2x1]` |

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **Front wheel steering**。

### **WhlAngM** — 中间轮转向角 `scalar` | `array`

中间轮转向角，*δM*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | *δM* | Scalar – `1` |
| `Dual` | δM=[δmlδmr] 或 [δmlδmr] | Array – `[1x2]` 或 `[2x1]` |

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **Middle wheel steering**。

### **WhlAngR** — 后轮转向角 `scalar` | `array`

后轮转向角，*δR*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | *δR* | Scalar – `1` |
| `Dual` | δR=[δrlδrr] 或 [δrlδrr] | Array – `[1x2]` 或 `[2x1]` |

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **Rear wheel steering**。

### **xdotin** — 纵向速度 `scalar`

车辆 CG 沿车辆固定 *x* 轴的速度，单位为 m/s。

#### 依赖关系

要启用此端口，请将 **Axle forces** 设置为 `External longitudinal velocity`。

### **FwF** — 前轮上的总力 `scalar` | `array`

前轮上的力，*FwF*，沿车辆固定轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | 前轮上的纵向力 | FwF=Fxf | Scalar – `1` |
| `External forces` | 前轮上的纵向力和侧向力 | FwF=[FxfFyf] 或 [FxfFyf] | Array – `[1x2]` 或 `[2x1]` |
| `Dual` | `External longitudinal forces` | 前轮上的纵向力 | FwF=[FxflFxfr] 或 [FxflFxfr] | Array – `[1x2]` 或 `[2x1]` |
| `External forces` | 前轮上的纵向力和侧向力 | FwF=[FxflFyflFxfrFyfr] | Array – `[2x2]` |

#### 依赖关系

要启用此端口，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FwM** — 中间轮上的总力 `scalar` | `array`

中间轮上的力，*FwM*，沿车辆固定轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | 中间轮上的纵向力 | FwM=Fxr | Scalar – `1` |
| `External forces` | 中间轮上的纵向力和侧向力 | FwM=[FxmFym] 或 [FxmFym] | Array – `[1x2]` 或 `[2x1]` |
| `Dual` | `External longitudinal forces` | 中间轮上的纵向力 | FwM=[FxmlFxmr] 或 [FxmlFxmr] | Array – `[1x2]` 或 `[2x1]` |
| `External forces` | 中间轮上的纵向力和侧向力 | FwM=[FxmlFxmrFymlFymr] | Array – `[2x2]` |

#### 依赖关系

要启用此端口，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FwR** — 后轮上的总力 `scalar` | `array`

后轮上的力，*FwR*，沿车辆固定轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | 后轮上的纵向力 | FwR=Fxr | Scalar – `1` |
| `External forces` | 后轮上的纵向力和侧向力 | FwR=[FxrFyr] 或 [FxrFyr] | Array – `[1x2]` 或 `[2x1]` |
| `Dual` | `External longitudinal forces` | 后轮上的纵向力 | FwR=[FxrlFxrr] 或 [FxrlFxrr] | Array – `[1x2]` 或 `[2x1]` |
| `External forces` | 后轮上的纵向力和侧向力 | FwR=[FxrlFyrlFxrrFyrr] | Array – `[2x2]` |

#### 依赖关系

要启用此端口，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FExt** — 车辆 CG 上的外部力 `array`

施加到车辆 CG 的外部力，*Fxext*、*Fyext*、*Fzext*，在车辆固定坐标系中，单位为 N。信号数组维度为 `[1x3]` 或 `[3x1]`。

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **External forces**。

### **MExt** — 绕车辆 CG 的外部力矩 `array`

绕车辆 CG 的外部力矩，*Mx*、*My*、*Mz*，在车辆固定坐标系中，单位为 N·m。信号数组维度为 `[1x3]` 或 `[3x1]`。

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **External moments**。

### **Fh** — 作用在车体上的挂钩力 `array`

在挂钩位置施加到车体上的挂钩力，*Fhx*、*Fhy*、*Fhz*，在车辆固定坐标系中，单位为 N，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Hitch forces**。

### **Mh** — 绕车体的挂钩力矩 `array`

在挂钩位置相对于车辆固定坐标系的挂钩力矩，*Mhx*、*Mhy*、*Mhz*，单位为 N·m，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Hitch moments**。

### **WindXYZ** — 风速 `array`

风速，*Wx*、*Wy*、*Wz*，沿惯性 *X*、*Y* 和 *Z* 轴，单位为 m/s。信号数组维度为 `[1x3]` 或 `[3x1]`。

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **External wind**。

### **Mu** — 轮胎摩擦系数 `array`

轮胎摩擦系数，*μ*，无量纲。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | Mu=[μfμmμr] 或 [μfμmμr] | Array – `[1x3]` 或 `[3x1]` |
| `Dual` | Mu=[μflμfrμmlμmrμrlμrr] | Array – `[3x2]` |

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **External friction**。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，单位为 K。

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **Air temperature**。

### **X\_o** — 初始纵向位置 `scalar`

初始车辆 CG 沿大地固定 *X* 轴的位移，单位为 m。

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **Initial longitudinal position**。

### **Y\_o** — 初始侧向位置 `scalar`

初始车辆 CG 沿大地固定 *Y* 轴的位移，单位为 m。

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **Initial lateral position**。

### **xdot\_o** — 初始纵向位置 `scalar`

初始车辆 CG 沿车辆固定 *x* 轴的速度，单位为 m/s。

#### 依赖关系

要启用此端口：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal forces`
   - `External forces`
2. 在 **Input signals** 窗格上，选择 **Initial longitudinal velocity**

### **ydot\_o** — 初始侧向位置 `scalar`

初始车辆 CG 沿车辆固定 *y* 轴的速度，单位为 m/s。

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **Initial lateral velocity**。

### **psi\_o** — 初始偏航角 `scalar`

车辆固定坐标系绕大地固定 *Z* 轴的旋转（偏航），单位为 rad。

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **Initial yaw angle**。

### **r\_o** — 初始偏航率 `scalar`

车辆绕车辆固定 *z* 轴的角速度（偏航率），单位为 rad/s。

#### 依赖关系

要启用此端口，请在 **Input signals** 窗格上选择 **Initial yaw rate**。

### 输出

### **Info** — 车辆数据总线

车辆数据，作为包含这些模块值的总线信号返回。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆质心沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | | 车辆质心沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | | 车辆质心沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 车辆质心沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | | 车辆质心沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | | 车辆质心沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕地球固定 *X* 轴的旋转（横滚） | `0` | rad |
| `theta` | | | 车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰） | `0` | rad |
| `psi` | | | 车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆） | 计算所得 | rad |
| `FrntAxl` | `Lft` | `Disp` | `X` | | 前左车轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 前左车轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 前左车轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前左车轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 前左车轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 前左车轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 前右车轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 前右车轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 前右车轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前右车轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 前右车轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 前右车轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `MidlAxl` | `Lft` | `Disp` | `X` | | 中左车轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 中左车轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 中左车轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 中左车轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 中左车轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 中左车轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 中右车轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 中右车轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 中右车轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 中右车轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 中右车轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 中右车轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `RearAxl` | `Lft` | `Disp` | `X` | | 后左车轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 后左车轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 后左车轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后左车轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 后左车轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 后左车轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 后右车轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 后右车轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 后右车轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后右车轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 后右车轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 后右车轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Hitch` | `Disp` | `X` | | | 拖车挂钩沿地球固定 *X* 轴距车轴平面的偏移 | 计算所得 | m |
| `Y` | | | 拖车挂钩沿地球固定 *Y* 轴距中心平面的偏移 | 计算所得 | m |
| `Z` | | | 拖车挂钩沿地球固定 *Z* 轴距车轴平面的偏移 | 计算所得 | m |
| `Vel` | `Xdot` | | | 拖车挂钩沿地球固定 *X* 轴的偏移速度 | 计算所得 | m/s |
| `Ydot` | | | 拖车挂钩沿地球固定 *Y* 轴的偏移速度 | 计算所得 | m/s |
| `Zdot` | | | 拖车挂钩沿地球固定 *Z* 轴的偏移速度 | 计算所得 | m/s |
| `Geom` | `Disp` | `X` | | | 车辆底盘沿地球固定 *X* 轴距车轴平面的偏移 | 计算所得 | m |
| `Y` | | | 车辆底盘沿地球固定 *Y* 轴距中心平面的偏移 | 计算所得 | m |
| `Z` | | | 车辆底盘沿地球固定 *Z* 轴距车轴平面的偏移 | 计算所得 | m |
| `Vel` | `Xdot` | | | 车辆底盘沿地球固定 *X* 轴的偏移速度 | 计算所得 | m/s |
| `Ydot` | | | 车辆底盘沿地球固定 *Y* 轴的偏移速度 | 计算所得 | m/s |
| `Zdot` | | | 车辆底盘沿地球固定 *Z* 轴的偏移速度 | 计算所得 | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | 车辆质心沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | | 车辆质心沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | | 车辆质心沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Ang` | `Beta` | | | 车身侧偏角，*β*    β=VyVx | 计算所得 | rad |
| `AngVel` | `p` | | | 车辆绕车辆固定 *x* 轴的角速度（横滚角速率） | `0` | rad/s |
| `q` | | | 车辆绕车辆固定 *y* 轴的角速度（俯仰角速率） | `0` | rad/s |
| `r` | | | 车辆绕车辆固定 *z* 轴的角速度（横摆角速率） | 计算所得 | rad/s |
| `Acc` | `ax` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | 计算所得 | gn |
| `ay` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | 计算所得 | gn |
| `az` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | gn |
| `xddot` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | 计算所得 | m/s^2 |
| `yddot` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | 计算所得 | m/s^2 |
| `zddot` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | m/s^2 |
| `AngAcc` | `pdot` | | | 车辆绕车辆固定 *x* 轴的角加速度 | `0` | rad/s |
| `qdot` | | | 车辆绕车辆固定 *y* 轴的角加速度 | `0` | rad/s |
| `rdot` | | | 车辆绕车辆固定 *z* 轴的角加速度 | 计算所得 | rad/s |
| `Forces` | `Body` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴的净力 | 计算所得 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴的净力 | 计算所得 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴的净力 | `0` | N |
| `Ext` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴的外力 | 计算所得 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴的外力 | 计算所得 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴的外力 | `0` | N |
| `Hitch` | `Fx` | | | 在挂钩位置沿车辆固定 *x* 轴施加到车体的挂钩力 | 计算所得 | N |
| `Fy` | | | 在挂钩位置沿车辆固定 *y* 轴施加到车体的挂钩力 | 计算所得 | N |
| `Fz` | | | 在挂钩位置沿车辆固定 *z* 轴施加到车体的挂钩力 | 计算所得 | N |
| `FrntAxl` | `Lft` | `Fx` | | 前左车轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 前左车轮沿车辆固定 *y* 轴的横向力 | 计算所得 | N |
| `Fz` | | 前左车轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Rght` | `Fx` | | 前右车轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 前右车轮沿车辆固定 *y* 轴的横向力 | 计算所得 | N |
| `Fz` | | 前右车轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `MidlAxl` | `Lft` | `Fx` | | 中左车轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 中左车轮沿车辆固定 *y* 轴的横向力 | 计算所得 | N |
| `Fz` | | 中左车轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Rght` | `Fx` | | 中右车轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 中右车轮沿车辆固定 *y* 轴的横向力 | 计算所得 | N |
| `Fz` | | 中右车轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `RearAxl` | `Lft` | `Fx` | | 后左车轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 后左车轮沿车辆固定 *y* 轴的横向力 | 计算所得 | N |
| `Fz` | | 后左车轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Rght` | `Fx` | | 后右车轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 后右车轮沿车辆固定 *y* 轴的横向力 | 计算所得 | N |
| `Fz` | | 后右车轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Tires` | `FrntTires` | `Lft` | `Fx` | 前左轮胎力沿车辆固定 *x* 轴 | 计算所得 | N |
| `Fy` | 前左轮胎力沿车辆固定 *y* 轴 | 计算所得 | N |
| `Fz` | 前左轮胎力沿车辆固定 *z* 轴 | 计算所得 | N |
| `Rght` | `Fx` | 前右轮胎力沿车辆固定 *x* 轴 | 计算所得 | N |
| `Fy` | 前右轮胎力沿车辆固定 *y* 轴 | 计算所得 | N |
| `Fz` | 前右轮胎力沿车辆固定 *z* 轴 | 计算所得 | N |
| `RearTires` | `Lft` | `Fx` | 后左轮胎力沿车辆固定 *x* 轴 | 计算所得 | N |
| `Fy` | 后左轮胎力沿车辆固定 *y* 轴 | 计算所得 | N |
| `Fz` | 后左轮胎力沿车辆固定 *z* 轴 | 计算所得 | N |
| `Rght` | `Fx` | 后右轮胎力沿车辆固定 *x* 轴 | 计算所得 | N |
| `Fy` | 后右轮胎力沿车辆固定 *y* 轴 | 计算所得 | N |
| `Fz` | 后右轮胎力沿车辆固定 *z* 轴 | 计算所得 |  |
| `Drag` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴的阻力 | 计算所得 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴的阻力 | 计算所得 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴的阻力 | 计算所得 | N |
| `Grvty` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴的重力 | 计算所得 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴的重力 | 计算所得 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴的重力 | 计算所得 | N |
| `Moments` | `Body` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴的车体力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴的车体力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴的车体力矩 | `0` | N·m |
| `Drag` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴的阻力力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴的阻力力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴的阻力力矩 | `0` | N·m |
| `Ext` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴的外力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴的外力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴的外力矩 | `0` | N·m |
| `Hitch` | `Mx` | | | 挂钩位置绕车辆固定 *x* 轴的挂钩力矩 | `0` | N·m |
| `My` | | | 挂钩位置绕车辆固定 *y* 轴的挂钩力矩 | 计算所得 | N·m |
| `Mz` | | | 挂钩位置绕车辆固定 *z* 轴的挂钩力矩 | `0` | N·m |
| `FrntAxl` | `Lft` | `Disp` | `x` | | 前左车轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 前左车轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 前左车轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 前左车轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 前左车轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 前左车轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 前右车轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 前右车轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 前右车轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 前右车轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 前右车轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 前右车轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngFL` | | | 前左车轮转向角 | 计算所得 | rad |
| `WhlAngFR` | | | 前右车轮转向角 | 计算所得 | rad |
| `MidlAxl` | `Lft` | `Disp` | `x` | | 中左车轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 中左车轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 中左车轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 中左车轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 中左车轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 中左车轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 中右车轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 中右车轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 中右车轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 中右车轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 中右车轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 中右车轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 中左车轮转向角 | 计算所得 | rad |
| `WhlAngRR` | | | 中右车轮转向角 | 计算所得 | rad |
| `RearAxl` | `Lft` | `Disp` | `x` | | 后左车轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 后左车轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 后左车轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 后左车轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 后左车轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 后左车轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 后右车轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 后右车轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 后右车轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 右后轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 右后轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 右后轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 左后轮转向角 | Computed | rad |
| `WhlAngRR` | | | 右后轮转向角 | Computed | rad |
| `Hitch` | `Disp` | | `x` | | 挂钩沿车辆固定 *x* 轴相对车轴平面的偏移 | Input | m |
| `y` | | 挂钩沿车辆固定 *y* 轴相对中心平面的偏移 | Input | m |
| `z` | | 挂钩沿大地固定 *z* 轴相对车轴平面的偏移 | Input | m |
| `Vel` | | `xdot` | | 挂钩偏移沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 挂钩偏移沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 挂钩偏移沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | Computed | W |
| `Hitch` | | | | 挂钩导致的功率损失 | Computed | W |
| `Drag` | | | | 阻力导致的功率损失 | Computed | W |
| `Geom` | `Disp` | | `x` | | 车辆底盘沿车辆固定 *x* 轴相对车轴平面的偏移 | Input | m |
| `y` | | 车辆底盘沿车辆固定 *y* 轴相对中心平面的偏移 | Input | m |
| `z` | | 车辆底盘沿大地固定 *z* 轴相对车轴平面的偏移 | Input | m |
| `Vel` | | `xdot` | | 车辆底盘偏移沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 车辆底盘偏移沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 车辆底盘偏移沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | Computed | rad |

lacement 沿车辆固定 *z* 轴 | Computed | m |
| `Vel` | `xdot` | | 后右轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 后右轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 后右轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 后左轮转向角 | Computed | rad |
| `WhlAngRR` | | | 后右轮转向角 | Computed | rad |
| `Hitch` | `Disp` | | `x` | | 挂接点沿车辆固定 *x* 轴距车轴平面的偏移 | Input | m |
| `y` | | 挂接点沿车辆固定 *y* 轴距中心平面的偏移 | Input | m |
| `z` | | 挂接点沿地球固定 *z* 轴距车轴平面的偏移 | Input | m |
| `Vel` | | `xdot` | | 挂接点沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 挂接点沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 挂接点沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | Computed | W |
| `Hitch` | | | | 由挂接点引起的功率损失 | Computed | W |
| `Drag` | | | | 由阻力引起的功率损失 | Computed | W |
| `Geom` | `Disp` | | `x` | | 车辆底盘沿车辆固定 *x* 轴距车轴平面的偏移 | Input | m |
| `y` | | 车辆底盘沿车辆固定 *y* 轴距中心平面的偏移 | Input | m |
| `z` | | 车辆底盘沿地球固定 *z* 轴距车轴平面的偏移 | Input | m |
| `Vel` | | `xdot` | | 车辆底盘沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 车辆底盘沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 车辆底盘沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | Computed | rad |

| 信号 | | | 描述 | | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | 外部施加的纵向力功率 | | Computed | W |
| `PwrFyExt` | 外部施加的侧向力功率 | | Computed | W |
| `PwrMzExt` | 外部施加的横摆力矩功率 | | Computed | W |
| `PwrFwFLx` | 施加在前左轴处的纵向力功率 | | Computed | W |
| `PwrFwFLy` | 施加在前左轴处的侧向力功率 | | Computed | W |
| `PwrFwFRx` | 施加在前右轴处的纵向力功率 | | Computed | W |
| `PwrFwFRy` | 施加在前右轴处的侧向力功率 | | Computed | W |
| `PwrFwMLx` | 施加在中左轴处的纵向力功率 | | Computed | W |
| `PwrFwMLy` | 施加在中左轴处的侧向力功率 | | Computed | W |
| `PwrFwMRx` | 施加在中右轴处的纵向力功率 | | Computed | W |
| `PwrFwMRy` | 施加在中右轴处的侧向力功率 | | Computed | W |
| `PwrFwRLx` | 施加在后左轴处的纵向力功率 | | Computed | W |
| `PwrFwRLy` | 施加在后左轴处的侧向力功率 | | Computed | W |
| `PwrFwRRx` | 施加在后右轴处的纵向力功率 | | Computed | W |
| `PwrFwRRy` | 施加在后右轴处的侧向力功率 | | Computed | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | 纵向阻力功率 | | Computed | W |
| `PwrFyDrag` | 侧向阻力功率 | | Computed | W |
| `PwrMzDrag` | 阻力俯仰力矩功率 | | Computed | W |
| `PwrStored` | `PwrStoredGrvty` | 重力势能变化率 | | Computed | W |
| `PwrStoredxdot` | 纵向动能变化率 | | Computed | W |
| `PwrStoredydot` | 侧向动能变化率 | | Computed | W |
| `PwrStoredr` | 横摆旋转动能变化率 | | Computed | W |

### **xdot** — 车辆纵向速度 `scalar`

车辆质心沿车辆固定
*x* 轴的速度，单位为 m/s。

### **ydot** — 车辆侧向速度 `scalar`

车辆质心沿车辆固定
*y* 轴的速度，单位为 m/s。

### **psi** — 横摆 `scalar`

车辆固定坐标系绕地球固定
*Z* 轴的旋转（横摆），单位为 rad。

### **r** — 横摆角速度 `scalar`

车辆绕车辆固定 *z* 轴的角速度，`r`（横摆角速度），单位为 rad/s。

### **FzF** — 前轮法向力 `scalar` | `array`

前轮沿车辆固定 *z* 轴的法向力，
*FzF*，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single (bicycle)` | 前轴上的法向力 | FzF=Fzf | Scalar – `1` |
| `Dual` | 右前轮和左前轮的法向力 | FzF=[FzflFzfr] | Array – `[1x2]` |

### **FzM** — 中间轮法向力 `scalar` | `array`

中间轮沿车辆固定 *z* 轴的法向力，
*FzM*，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single (bicycle)` | 中轴上的法向力 | FzM=Fzm | Scalar – `1` |
| `Dual` | 右中轮和左中轮的法向力 | FzM=[FzmlFzrl] | Array – `[1x2]` |

### **FzR** — 后轮法向力 `scalar` | `array`

后轮沿车辆固定 *z* 轴的法向力，
*FzR*，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single (bicycle)` | 后轮上的法向力 | FzR=Fzr | Scalar – `1` |
| `Dual` | 右后轮和左后轮的法向力 | FzR=[FzrlFzrr] | Array – `[1x2]` |

## 参数

#### 选项

### **Vehicle track** — 车辆车轮数量 `Dual` (默认) | `Single (bicycle)`

使用 **Vehicle track** 参数指定车轮数量。

| Vehicle Track 设置 | 实现 |
| --- | --- |
| `Single (bicycle)` | - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual` | 力作用在车轴硬点位置。 |

### **Axle forces** — 车轴力类型 `External longitudinal velocity` (默认) | `External longitudinal forces` | `External forces`

使用 **Axle forces** 参数指定力类型。

| Axle Forces 设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 该模块假设外部纵向速度处于准稳态，因此纵向加速度近似为零。 - 由于运动为准稳态，模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 在以下情况下考虑此设置：  - 生成虚拟传感器信号数据。   - 执行不受动力传动系统或非线性轮胎响应影响的高层软件研究。 |
| `External longitudinal forces` | - 该模块使用外部纵向力使车辆加速或制动。 - 模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 在以下情况下考虑此设置：  - 考虑纵向速度变化对侧向运动和横摆运动的影响。   - 通过力而不是外部纵向速度来指定外部纵向运动。   - 将该模块连接到牵引执行器、车轮、制动器和挂接点。 |
| `External forces` | - 该模块使用外部侧向力和纵向力来使车辆转向、加速或制动。 - 模块不使用转向输入来计算车辆运动。 - 当您需要具有更准确的非线性组合侧向和纵向滑移的轮胎模型时，考虑此设置。 |

#### 输入信号

### **Front wheel steering** — `WhlAngF` 输入端口 `on` (默认) | `off`

选择以创建输入端口 `WhlAngF`。

### **Middle wheel steering** — `WhlAngM` 输入端口 `off` (默认) | `on`

选择以创建输入端口 `WhlAngM`。

### **Rear wheel steering** — `WhlAngR` 输入端口 `off` (默认) | `on`

选择以创建输入端口 `WhlAngR`。

### **External wind** — `WindXYZ` 输入端口 `off` (默认) | `on`

选择以创建输入端口 `WindXYZ`。

### **External friction** — `Mu` 输入端口 `off` (默认) | `on`

选择以创建输入端口 `Mu`。

#### 依赖项

要启用此参数，请将 **Axle forces** 设置为 `External longitudinal forces` 或 `External forces`。

### **External forces** — `FExt` 输入端口 `off` (默认) | `on`

选择以创建输入端口 `FExt`。

### **External moments** — `MExt` 输入端口 `off` (默认) | `on`

选择以创建输入端口 `MExt`。

### **Hitch forces** — `Fh` 输入端口 `on` (默认) | `off`

选择以创建输入端口 `Fh`。

### **Hitch moments** — `Mh` 输入端口 `on` (默认) | `off`

指定以创建输入端口 `Mh`。

### **Initial longitudinal position** — `X_o` 输入端口 `off` (默认) | `on`

指定以创建输入端口 `X_o`。

### **Initial yaw angle** — `psi_o` 输入端口 `off` (默认) | `on`

指定以创建输入端口 `psi_o`。

### **Initial longitudinal velocity** — `xdot_o` 输入端口 `off` (默认) | `on`

指定以创建输入端口 `xdot_o`。

#### 依赖项

要启用此参数，请将 **Axle forces** 设置为 `External longitudinal forces` 或 `External forces`。

### **Initial yaw rate** — `r_o` 输入端口 `off` (默认) | `on`

指定以创建输入端口 `r_o`。

### **Initial lateral position** — `Y_o` 输入端口 `off` (默认) | `on`

指定以创建输入端口 `Y_o`。

### **Air temperature** — `AirTemp` 输入端口 `off` (默认) | `on`

指定以创建输入端口 `AirTemp`。

### **Initial lateral velocity** — `ydot_o` 输入端口 `off` (默认) | `on`

指定以创建输入端口 `ydot_o`。

#### 纵向

### **Number of wheels on front axle, NF** — 前轮数量 `2` (默认) | `scalar`

前轴上的车轮数量，
*NF*，无量纲。

### **Number of wheels on middle axle, NM** — 中间轮数量 `2` (默认) | `scalar`

中轴上的车轮数量，
*NM*，无量纲。

### **Number of wheels on rear axle, NR** — 后轮数量 `2` (默认) | `scalar`

后轴上的车轮数量，
*NR*，无量纲。

### **Vehicle mass, m** — 车辆质量 `47000` (默认) | `scalar`

车辆质量，*m*，单位为 kg。

### **Longitudinal distance from center of mass to front axle, a** — 从质心到前轴的距离 `0.5` (默认) | `scalar`

从车辆质心到前轴的距离，*a*，单位为 m。

拖拉机侧视图，显示挂接点和各轴到质心的距离

### **Longitudinal distance from center of mass to middle axle, b** — 从质心到中轴的距离 `4.5` (默认) | `scalar`

从车辆质心到中轴的距离，*b*，单位为 m。

拖拉机侧视图，显示挂接点和各轴到质心的距离

### **Longitudinal distance from center of mass to rear axle, c** — 从质心到后轴的距离 `5.7` (默认) | `scalar`

从车辆质心到后轴的距离，*c*，单位为 m。

拖拉机侧视图，显示挂接点和各轴到质心的距离

### **Vertical distance from center of mass to axle plane, h** — 从质心到车轴平面的距离 `0.3` (默认) | `scalar`

从车辆质心到车轴平面的垂直距离，*h*，单位为 m。

拖拉机侧视图，显示挂接点和各轴到质心的距离

### **Vertical distance from hitch to axle plane, hh** — 从挂接点到车轴平面的距离 `0.5` (默认) | `scalar`

从挂接点到车轴平面的垂直距离，*hh*，单位为 m。

拖拉机侧视图，显示挂接点和各轴到质心的距离

#### 依赖项

要启用此参数，请在 **Input signals** 窗格上选择 **Hitch forces** 或 **Hitch moments**。

### **Longitudinal distance from center of mass to hitch, dh** — 从质心到挂接点的距离 `5` (默认) | `scalar`

从质心到挂接点的纵向距离，*dh*，
单位为 m。

拖拉机侧视图，显示挂接点和各轴到质心的距离

#### 依赖项

要启用此参数，请在 **Input signals** 窗格上选择 **Hitch forces** 或 **Hitch moments**。

### **Initial inertial frame longitudinal position, X_o** — 初始纵向位移 `0` (默认) | `scalar`

车辆质心沿地球固定
*X* 轴的初始位移，单位为 m。

### **Initial longitudinal velocity, xdot_o** — 初始纵向速度 `0` (默认) | `scalar`

车辆质心沿车辆固定
*x* 轴的初始速度，单位为 m/s。

#### 依赖项

要启用此参数，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal
  forces`
- `External forces`

#### 侧向

### **Mapped corner stiffness** — 启用映射侧偏刚度 `off` (默认) | `on`

启用映射侧偏刚度计算。

#### 依赖项

要启用此参数，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal
  velocity`
- `External longitudinal
  forces`

### **Include relaxation length dynamics** — 启用松弛长度动力学 `on` (默认) | `off`

启用松弛长度动力学。

#### 依赖项

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Lateral distance from geometric centerline to center of mass, d** — 从中心线到质心的距离 `0` (默认) | `scalar`

从几何中心线到质心的侧向距离，
*d*，单位为 m，沿车辆固定
*y* 轴。正值表示车辆
质心位于几何中心线右侧。负值表示
车辆质心位于几何中心线左侧。

俯视图，显示轮距和质心距中心线的偏移

### **Track width, w** — 前、中、后轮距 `[1.82,1.82,1.82]` (默认) | `vector`

前、中、后轮距分别为 *wf*、
*wm* 和 *wr*，单位为 m。
维度为 `1-by-3`。

俯视图，显示轮距和质心距中心线的偏移

#### 依赖项

要启用此参数，请将 **Vehicle track** 设置为
`Dual`。

### **Front axle tire corner stiffness, Cy_f** — 前轮胎侧偏刚度 `12e3` | `scalar`

前轮胎侧偏刚度，
*Cyf*，单位为 N/rad。

#### 依赖项

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Middle axle tire corner stiffness, Cy_m** — 中间轮胎侧偏刚度 `11e3` | `scalar`

中轴轮胎侧偏刚度，
*Cym*，单位为 N/rad。

#### 依赖项

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Rear axle tire corner stiffness, Cy_r** — 后轮胎侧偏刚度 `11e3` | `scalar`

后轴轮胎侧偏刚度，
*Cyr*，单位为 N/rad。

#### 依赖项

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Front tire(s) relaxation length, sigma_f** — 前轮胎松弛长度 `.1` (默认) | `scalar`

前轮胎松弛长度，
*σf*，单位为 m。

#### 依赖项

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

### **Middle tire(s) relaxation length, sigma_m** — 中间轮胎松弛长度 `.1` (默认) | `scalar`

中间轮胎松弛长度，
*σm*，单位为 m。

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

### **Rear tire(s) relaxation length, sigma\_r** — 后轮胎松弛长度 `.1`（默认） | `scalar`

后轮胎松弛长度，*σr*，单位为 m。

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

前轴侧偏角断点，*αfbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Front axle tire corner data, Cy\_f\_data** — 前轴轮胎侧偏数据 `[-9e3 9e3]`（默认） | `vector`

前轴轮胎侧偏数据，*Cyfdata*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Middle axle slip angle breakpoints, alpha\_m\_brk** — 断点 `[-.1 .1]`（默认） | `vector`

中轴侧偏角断点，*αmbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Middle axle tire corner data, Cy\_m\_data** — 中轴轮胎侧偏数据 `[-9e3 9e3]`（默认） | `vector`

中轴轮胎侧偏数据，*Cymdata*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Rear axle slip angle breakpoints, alpha\_r\_brk** — 断点 `[-.1 .1]`（默认） | `vector`

后轴侧偏角断点，*αrbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Rear axle tire corner data, Cy\_r\_data** — 后轴轮胎侧偏数据 `[-9e3 9e3]`（默认） | `vector`

后轴轮胎侧偏数据，*Cyrdata*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Initial inertial frame lateral displacement, Y\_o** — 初始横向位移 `0`（默认） | `scalar`

车辆 CG 沿地球固定 *Y* 轴的初始位移，单位为 m。

### **Initial lateral velocity, ydot\_o** — 初始横向速度 `0`（默认） | `scalar`

车辆 CG 沿车辆固定 *y* 轴的初始速度，单位为 m/s。

#### 横摆

### **Yaw polar inertia, Izz** — 转动惯量 `4000`（默认） | `scalar`

横摆极转动惯量，单位为 kg\*m^2。

### **Initial yaw angle, psi\_o** — Psi 旋转 `0`（默认） | `scalar`

车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆），单位为 rad。

### **Initial yaw rate, r\_o** — 横摆角速度 `0`（默认） | `scalar`

车辆绕车辆固定 *z* 轴的角速度（横摆角速度），单位为 rad/s。

#### 空气动力学

### **Longitudinal drag area, Af** — 有效车辆横截面积 `2`（默认） | `scalar`

有效车辆横截面积，*Af*，用于计算车辆上的空气阻力，单位为 m2。

### **Longitudinal drag coefficient, Cd** — 空气阻力系数 `.3`（默认） | `scalar`

空气阻力系数，*Cd*。该值无量纲。

### **Longitudinal lift coefficient, Cl** — 空气升力系数 `.1`（默认） | `scalar`

空气升力系数，*Cl*。该值无量纲。

### **Longitudinal drag pitch moment, Cpm** — 俯仰阻力 `.1`（默认） | `scalar`

纵向阻力俯仰力矩系数，*Cpm*。该值无量纲。

### **Relative wind angle vector, beta\_w** — 风角 `[0:0.01:0.3]`（默认） | `vector`

相对风角向量，*βw*，单位为 rad。

### **Side force coefficient vector, Cs** — 侧向力系数 `[0:0.03:0.9]`（默认） | `vector`

侧向力系数向量系数，*Cs*。该值无量纲。

### **Yaw moment coefficient vector, Cym** — 横摆力矩阻力 `[0:0.01:0.3]`（默认） | `vector`

横摆力矩系数向量，*Cym*。该值无量纲。

#### 环境

### **Absolute air pressure, Pabs** — 压力 `101325`（默认） | `scalar`

环境绝对压力，*Pabs*，单位为 Pa。

### **Air temperature, Tair** — 温度 `273`（默认） | `scalar`

环境绝对温度，*T*，单位为 K。

#### 依赖关系

要启用此参数，请清除 **Air temperature**。

### **Gravitational acceleration, g** — 重力 `9.81`（默认） | `scalar`

重力加速度，*g*，单位为 m/s^2。

### **Nominal friction scaling factor, mu** — 摩擦缩放因子 `1`（默认） | `scalar`

标称摩擦缩放因子，*μ*。该值无量纲。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **External Friction**。

#### 仿真

### **Longitudinal velocity tolerance, xdot\_tol** — 容差 `.01`（默认） | `scalar`

纵向速度容差，单位为 m/s。

### **Nominal normal force, Fznom** — 法向力 `5000`（默认） | `scalar`

标称法向力，单位为 N。

#### 依赖关系

要启用此参数，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal velocity`
- `External longitudinal forces`

### **Geometric longitudinal offset from axle plane, longOff** — 纵向偏移 `0`（默认） | `scalar`

车辆底盘沿车辆固定 *x* 轴相对于车轴平面的偏移，单位为 m。使用 3D 可视化引擎时，可考虑使用该偏移来独立于车辆 CG 定位底盘。

### **Geometric lateral offset from center plane, latOff** — 横向偏移 `0`（默认） | `scalar`

车辆底盘沿车辆固定 *y* 轴相对于中心平面的偏移，单位为 m。使用 3D 可视化引擎时，可考虑使用该偏移来独立于车辆 CG 定位底盘。

### **Geometric vertical offset from axle plane, vertOff** — 垂向偏移 `0`（默认） | `scalar`

车辆底盘沿车辆固定 *z* 轴相对于车轴平面的偏移，单位为 m。使用 3D 可视化引擎时，可考虑使用该偏移来独立于车辆 CG 定位底盘。

### **Wrap Euler angles, wrapAng** — 将欧拉角包裹到区间 `[-pi, pi]` `off`（默认） | `on`

将欧拉角包裹到区间 `[-pi, pi]`。对于可能经历超出此区间的车辆横摆旋转的车辆机动，如果希望执行以下操作，请考虑清除此参数：

- 跟踪车辆总横摆旋转。
- 避免车辆状态估计器中出现不连续。

## 所属库

Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有纵向、横向和横摆运动的三轴车体

Vehicle Body 3DOF Three Axles 模块实现一个刚性三轴车体模型，用于计算纵向、横向和横摆运动。该模块考虑由车体质量加速度、空气阻力和转向引起的车轴和挂钩反作用力。

在车辆动力学和自动驾驶研究中，当车辆俯仰、侧倾和垂向运动不显著时，使用此模块对非完整车辆运动进行建模。

使用 **Vehicle track** 参数指定车轮数量。

| Vehicle track 设置 | 实现 |
| --- | --- |
| `Single (bicycle)` | - 力沿车轴中心线作用。 - 无横向载荷转移。 |
| `Dual` | 力作用在车轴硬点位置。 |

使用 **Axle forces** 参数指定力的类型。

| Axle forces 设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 该模块假设外部纵向速度处于准稳态，因此纵向加速度约为零。 - 由于运动是准稳态的，该模块使用轮胎侧偏角和线性侧偏刚度计算横向力。 - 当您希望执行以下操作时，请考虑此设置：  - 生成虚拟传感器信号数据。   - 进行不受动力传动系统或非线性轮胎响应影响的高级软件研究。 |
| `External longitudinal forces` | - 该模块使用外部纵向力来加速或制动车辆。 - 该模块使用轮胎侧偏角和线性侧偏刚度计算横向力。 - 当您希望执行以下操作时，请考虑此设置：  - 考虑纵向速度变化对横向和横摆运动的影响。   - 通过力而不是外部纵向速度来指定外部纵向运动。   - 将模块连接到牵引执行器、车轮、制动器和挂钩。 |
| `External forces` | - 该模块使用外部横向和纵向力来转向、加速或制动车辆。 - 该模块不使用转向输入来计算车辆运动。 - 当您需要具有更精确非线性组合横向和纵向滑移的轮胎模型时，请考虑此设置。 |

要创建额外的输入端口，请在 **Input signals** 下选择以下模块参数。

| 输入信号窗格参数 | 输入端口 | 描述 |
| --- | --- | --- |
| **Front wheel steering** | `WhlAngF` | 前轮转角，*δF* |
| **Middle wheel steering** | `WhlAngM` | 中轮转角，*δM* |
| **Rear wheel steering** | `WhlAngR` | 后轮转角，*δR* |
| **External wind** | `WindXYZ` | 风速，*WX*、*WY* 和 *WZ*，在惯性参考系中 |
| **External friction** | `Mu` | 摩擦系数 |
| **External forces** | `FExt` | 作用在车辆重心 (CG) 上的外部力，*Fx*、*Fy* 和 *Fz*，在车辆固定坐标系中 |
| **External moments** | `MExt` | 绕车辆 CG 的外部力矩，*Mx*、*My* 和 *Mz*，在车辆固定坐标系中 |
| **Front hitch forces** | `FhF` | 在前挂钩位置施加到车体的挂钩力，*FhFx*、*FhFy* 和 *FhFz*，在车辆固定坐标系中 |
| **Front hitch moments** | `MhF` | 前挂钩位置处的挂钩力矩，*MhFx*、*MhFy* 和 *MhFz*，绕车辆固定坐标系 |
| **Rear hitch forces** | `FhR` | 在后挂钩位置施加到车体的挂钩力，*FhRx*、*FhRy* 和 *FhRz*，在车辆固定坐标系中 |
| **Rear hitch moments** | `MhR` | 后挂钩位置处的挂钩力矩，*MhRx*、*MhRy* 和 *MhRz*，绕车辆固定坐标系 |
| **Initial longitudinal position** | `X_o` | 车辆 CG 沿地球固定 *X* 轴的初始位移 |
| **Initial yaw angle** | `psi_o` | 车辆固定坐标系绕地球固定 *Z* 轴的初始旋转（横摆） |
| **Initial longitudinal velocity** | `xdot_o` | 车辆 CG 沿车辆固定 *x* 轴的初始速度 |
| **Initial yaw rate** | `r_o` | 车辆绕车辆固定 *z* 轴的初始角速度（横摆角速度） |
| **Initial lateral position** | `Y_o` | 车辆 CG 沿地球固定 *Y* 轴的初始位移 |
| **Air temperature** | `AirTemp` | 环境空气温度。如果您希望在运行期间改变温度，请考虑此选项。 |
| **Initial lateral velocity** | `ydot_o` | 车辆 CG 沿车辆固定 *y* 轴的初始速度 |

### 理论

为确定车辆运动，该模块求解刚体平面动力学运动方程。

| 计算 | 描述 |
| --- | --- |
| *动力学* | 该模块求解刚体平面动力学方程以确定车辆纵向运动。如果将**车轴力**设置为 `External longitudinal velocity`，该模块假设纵向加速度为准稳态。 |
| *外力* | 外力包括阻力和外部力输入。这些力作用在车辆质心上。该模块将法向力除以标称法向载荷，以在重量和载荷转移期间改变有效摩擦参数。该模块保持俯仰和侧倾平衡。 |
| *轮胎力* | 该模块使用局部纵向速度和横向速度的比值来确定侧偏角。该模块使用转向角将轮胎力变换到车辆固定坐标系。如果将**车轴力**设置为 `External forces`，该模块假设外部提供的力位于车轴-车轮位置的车辆固定坐标系中。 |

**单轨**

在单轨悬架位置处作用的垂向、纵向和横向力的等轴测视图

**双轨**

在双轨悬架位置处作用的垂向、纵向和横向力的等轴测视图

这些图示使用以下变量。

|  |  |
| --- | --- |
| *a*, *b*, *c* | 前轴、中轴和后轴分别距车辆质心在公共车轴平面上的正投影点的纵向距离 |
| *h* | 车辆质心沿车辆固定 *z* 轴高出车轴平面的高度 |
| *d* | 沿车辆固定 *y* 轴从几何中心线到质心的横向距离 |
| *hh* | 挂钩沿车辆固定 *z* 轴高出车轴平面的高度 |
| *dh* | 挂钩距车辆质心在公共车轴平面上的正投影点的纵向距离 |
| *hl* | 沿车辆固定 *y* 轴从质心到挂钩的横向距离。 |
| *wf*, *wm*, *wr* | 前轮距、中轮距和后轮距 |

**阻力**

下表总结了该模块对阻力计算的实现。

| 计算 | 描述 |
| --- | --- |
| *坐标变换* | 该模块将风速从惯性坐标系变换到车辆固定坐标系。 |
| *阻力* | 为了确定相对空速，该模块从车辆质心速度中减去风速。该模块使用相对空速确定阻力。 |
| *阻力矩* | 该模块使用相对空速确定阻力矩。 |

**横向侧偏刚度和松弛动态**

要启用映射侧偏刚度和松弛长度动态参数，请将**车轴力**设置为 `External longitudinal force` 或 `External longitudinal velocity`。

| 参数设置 | | 描述 |
| --- | --- | --- |
| 映射侧偏刚度 | 包含松弛长度动态 |
| `Off` (默认) | `On` (默认) | 该模块使用恒定侧偏刚度值。 侧偏角包括松弛长度动态设置。松弛长度近似于一个作为车轮行程函数的有效侧偏刚度力。 |
| `On` | `On` (默认) | 该模块使用查找表，这些查找表是侧偏刚度数据和侧偏角的函数。 侧偏角包括松弛长度动态设置。松弛长度近似于一个作为车轮行程函数的有效侧偏刚度力。 |
| `Off` (默认) | `Off` | 该模块使用恒定侧偏刚度值。 |
