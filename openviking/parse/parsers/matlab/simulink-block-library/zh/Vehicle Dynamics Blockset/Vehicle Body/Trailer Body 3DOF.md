---
type: simulink-block
title: 'Trailer Body 3DOF'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'trailerbody3dof'
documentation_source_path: 'ref/trailerbody3dof.html'
language: zh-CN
chinese_source: worker-translation
---

# Trailer Body 3DOF

## 端口

### 输入

### **WhlAngF** — 前轮转向角 `scalar` | `array`

前轮转向角，*δF*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single 1-axle`  `Single 2-axle`  `Single 3-axle` | *δF* | Scalar – `1` |
| `Dual 1-axle`  `Dual 2-axle`  `Dual 3-axle` | δF=[δflδfr]  或  [δflδfr] | Array – `[1x2]` 或 `[2x1]` |

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Front wheel steering**。

### **WhlAngM** — 中间车轮转向角 `scalar` | `array`

中间车轮转向角，*δM*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single 3-axle` | *δM* | Scalar – `1` |
| `Dual 3-axle` | δM=[δmlδmr]  或  [δmlδmr] | Array – `[1x2]` 或 `[2x1]` |

#### 依赖项

要启用此端口：

- 将 **Vehicle track** 设置为 `Single 3-axle` 或 `Dual 3-axle`。
- 要启用此端口，在 **Input signals** 下，选择 **Middle wheel steering**。

### **WhlAngR** — 后轮转向角 `scalar` | `array`

后轮转向角，*δR*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single 1-axle`  `Single 2-axle`  `Single 3-axle` | *δR* | Scalar – `1` |
| `Dual 1-axle`  `Dual 2-axle`  `Dual 3-axle` | δR=[δrlδrr]  或  [δrlδrr] | Array – `[1x2]` 或 `[2x1]` |

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Rear wheel steering**。

### **xdotin** — 纵向速度 `scalar`

车辆质心沿车辆固定 *x* 轴的速度，单位为 m/s。

#### 依赖项

要启用此端口，将 **Axle forces** 设置为 `External longitudinal velocity`。

### **FwF** — 前轮上的总力 `scalar` | `array`

前轮上的力，*FwF*，沿车辆固定轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single 1-axle`  `Single 2-axle`  `Single 3-axle` | `External longitudinal forces` | 前轮的纵向力 | FwF=Fxf | Scalar – `1` |
| `External forces` | 前轮的纵向力和横向力 | FwF=[FxfFyf]  或 [FxfFyf] | Array – `[1x2]` 或 `[2x1]` |
| `Dual 1-axle`  `Dual 2-axle`  `Dual 3-axle` | `External longitudinal forces` | 前轮的纵向力 | FwF=[FxflFxfr] 或 [FxflFxfr] | Array – `[1x2]` 或 `[2x1]` |
| `External forces` | 前轮的纵向力和横向力 | FwF=[FxflFyflFxfrFyfr] | Array – `[2x2]` |

#### 依赖项

要启用此端口，将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FwM** — 中间车轮上的总力 `scalar` | `array`

中间车轮上的力，*FwM*，沿车辆固定轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single 3-axle` | `External longitudinal forces` | 中间车轮的纵向力 | FwM=Fxr | Scalar – `1` |
| `External forces` | 中间车轮的纵向力和横向力 | FwM=[FxmFym]  或 [FxmFym] | Array – `[1x2]` 或 `[2x1]` |
| `Dual 3-axle` | `External longitudinal forces` | 中间车轮的纵向力 | FwM=[FxmlFxmr] 或 [FxmlFxmr] | Array – `[1x2]` 或 `[2x1]` |
| `External forces` | 中间车轮的纵向力和横向力 | FwM=[FxmlFxmrFymlFymr] | Array – `[2x2]` |

#### 依赖项

要启用此端口，设置：

- 将 **Vehicle track** 设置为
  `Single 3-axle` 或
  `Dual 3-axle`。
- 将 **Axle forces** 设置为
  `External longitudinal
  forces` 或 `External
  forces`。

### **FwR** — 后轮上的总力 `scalar` | `array`

后轮上的力，*FwR*，沿车辆固定轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single 2-axle`  `Single 3-axle` | `External longitudinal forces` | 后轮的纵向力 | FwR=Fxr | Scalar – `1` |
| `External forces` | 后轮的纵向力和横向力 | FwR=[FxrFyr]  或 [FxrFyr] | Array – `[1x2]` 或 `[2x1]` |
| `Dual 2-axle`  `Dual 3-axle` | `External longitudinal forces` | 后轮的纵向力 | FwR=[FxrlFxrr] 或 [FxrlFxrr] | Array – `[1x2]` 或 `[2x1]` |
| `External forces` | 后轮的纵向力和横向力 | FwR=[FxrlFyrlFxrrFyrr] | Array – `[2x2]` |

#### 依赖项

要启用此端口，设置：

- 将 **Vehicle track** 设置为
  `Single 3-axle`、
  `Single 2-axle`、
  `Dual 3-axle` 或
  `Dual 2-axle`。
- 将 **Axle forces** 设置为
  `External longitudinal
  forces` 或 `External
  forces`。

### **FExt** — 车辆质心上的外部力 `array`

施加到车辆质心的外部力，*Fxext*、*Fyext*、*Fzext*，在车辆固定坐标系中，单位为 N。信号向量维度为 `[1x3]` 或 `[3x1]`。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **External forces**。

### **MExt** — 绕车辆质心的外部力矩 `array`

绕车辆质心的外部力矩，*Mx*、*My*、*Mz*，在车辆固定坐标系中，单位为 N·m。信号向量维度为 `[1x3]` 或 `[3x1]`。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **External moments**。

### **FhF** — 车体上的前挂接点力 `array`

施加在车体前挂接点位置的挂接力，*FhFx*、*FhFy*、*FhFz*，在车辆固定坐标系中，单位为 N，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Front hitch forces**。

### **MhF** — 绕车体的前挂接力矩 `array`

前挂接点位置的挂接力矩，*MhFx*、*MhFy*、*MhFz*，相对于车辆固定坐标系，单位为 N·m，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Front hitch moments**。

### **FhR** — 车体上的后挂接点力 `array`

施加在车体后挂接点位置的挂接力，*FhRx*、*FhRy*、*FhRz*，在车辆固定坐标系中，单位为 N，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Rear hitch forces**。

### **MhR** — 绕车体的后挂接力矩 `array`

后挂接点位置的挂接力矩，*MhRx*、*MhRy*、*MhRz*，相对于车辆固定坐标系，单位为 N·m，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Rear hitch moments**。

### **WindXYZ** — 风速 `array`

风速，*Wx*、*Wy*、*Wz*，沿惯性 *X*、*Y* 和 *Z* 轴，单位为 m/s。信号向量维度为 `1-by-3` 或 `3-by-1`。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **External wind**。

### **Mu** — 轮胎摩擦系数 `array`

轮胎摩擦系数，*μ*。该值无量纲。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single 1-axle` | 车轮上的摩擦系数 | Mu=μf | Array – `[1x1]` |
| `Dual 1-axle` | 车轮上的摩擦系数 | Mu=[μflμfr] 或 [μflμfr] | Array – `[1x2]` 或 `[2x1]` |
| `Single 2-axle` | 车轮上的摩擦系数 | Mu=[μfμr] 或 [μfμr] | Array – `[1x2]` 或 `[2x1]` |
| `Dual 2-axle` | 车轮上的摩擦系数 | Mu=[μflμfrμrlμrr] | Array – `[2x2]` |
| `Single 3-axle` | 车轮上的摩擦系数 | Mu=[μfμmμr] 或 [μfμmμr] | Array – `[1x3]` 或 `[3x1]` |
| `Dual 3-axle` | 车轮上的摩擦系数 | Mu=[μflμfrμmlμmrμrlμrr] | Array – `[3x2]` |

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **External friction**。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，单位为 K。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Air temperature**。

### **X\_o** — 初始纵向位置 `scalar`

车辆质心沿地球固定 *X* 轴的初始位移，单位为 m。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Initial longitudinal position**。

### **Y\_o** — 初始横向位置 `scalar`

车辆质心沿地球固定 *Y* 轴的初始位移，单位为 m。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Initial lateral position**。

### **xdot\_o** — 初始纵向位置 `scalar`

车辆质心沿车辆固定 *x* 轴的初始速度，单位为 m/s。

#### 依赖项

要启用此端口：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     forces`
   - `External
     forces`
2. 在 **Input signals** 下，选择
   **Initial longitudinal
   velocity**

### **ydot\_o** — 初始横向位置 `scalar`

车辆质心沿车辆固定 *y* 轴的初始速度，单位为 m/s。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Initial lateral velocity**。

### **psi\_o** — 初始横摆角 `scalar`

车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆），单位为 rad。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Initial yaw angle**。

### **r\_o** — 初始横摆角速度 `scalar`

车辆绕车辆固定 *z* 轴的角速度（横摆角速度），单位为 rad/s。

#### 依赖项

要启用此端口，在 **Input signals** 下，选择 **Initial yaw rate**。
### 输出

### **Info** — 拖车数据总线

拖车数据，作为包含以下模块值的总线信号返回。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆质心沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | | 车辆质心沿地球固定 *Y* 轴的位移 | Computed | m |
| `Z` | | | 车辆质心沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 车辆质心沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | | 车辆质心沿地球固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | | 车辆质心沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕地球固定 *X* 轴的旋转（横滚） | `0` | rad |
| `theta` | | | 车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰） | `0` | rad |
| `psi` | | | 车辆固定坐标系绕地球固定 *Z* 轴的旋转（偏航） | Computed | rad |
| `FrntAxl` | `Lft` | `Disp` | `X` | | 前左轮沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | 前左轮沿地球固定 *Y* 轴的位移 | Computed | m |
| `Z` | | 前左轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前左轮沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | 前左轮沿地球固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | 前左轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 前右轮沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | 前右轮沿地球固定 *Y* 轴的位移 | Computed | m |
| `Z` | | 前右轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前右轮沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | 前右轮沿地球固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | 前右轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `MidlAxl` | `Lft` | `Disp` | `X` | | 中间左轮沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | 中间左轮沿地球固定 *Y* 轴的位移 | Computed | m |
| `Z` | | 中间左轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 中间左轮沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | 中间左轮沿地球固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | 中间左轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 中间右轮沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | 中间右轮沿地球固定 *Y* 轴的位移 | Computed | m |
| `Z` | | 中间右轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 中间右轮沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | 中间右轮沿地球固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | 中间右轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `RearAxl` | `Lft` | `Disp` | `X` | | 后左轮沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | 后左轮沿地球固定 *Y* 轴的位移 | Computed | m |
| `Z` | | 后左轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后左轮沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | 后左轮沿地球固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | 后左轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 后右轮沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | 后右轮沿地球固定 *Y* 轴的位移 | Computed | m |
| `Z` | | 后右轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后右轮沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | 后右轮沿地球固定 *Y* 轴的速度 | Computed | m/s |
| `Zdot` | | 后右轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Geom` | `Disp` | `X` | | | 拖车车身沿地球固定 *X* 轴距车轴平面的偏移 | Computed | m |
| `Y` | | | 拖车车身沿地球固定 *Y* 轴距中心平面的偏移 | Computed | m |
| `Z` | | | 拖车车身沿地球固定 *Z* 轴距车轴平面的偏移 | Computed | m |
| `Vel` | `Xdot` | | | 拖车车身沿地球固定 *X* 轴的偏移速度 | Computed | m/s |
| `Ydot` | | | 拖车车身沿地球固定 *Y* 轴的偏移速度 | Computed | m/s |
| `Zdot` | | | 拖车车身沿地球固定 *Z* 轴的偏移速度 | Computed | m/s |
| `HitchF` | `Disp` | `X` | | | 拖车前挂接点沿地球固定 *X* 轴距车轴平面的偏移 | Computed | m |
| `Y` | | | 拖车前挂接点沿地球固定 *Y* 轴距中心平面的偏移 | Computed | m |
| `Z` | | | 拖车前挂接点沿地球固定 *Z* 轴距车轴平面的偏移 | Computed | m |
| `Vel` | `Xdot` | | | 拖车前挂接点沿地球固定 *X* 轴的偏移速度 | Computed | m/s |
| `Ydot` | | | 拖车前挂接点沿地球固定 *Y* 轴的偏移速度 | Computed | m/s |
| `Zdot` | | | 拖车前挂接点沿地球固定 *Z* 轴的偏移速度 | Computed | m/s |
| `HitchR` | `Disp` | `X` | | | 拖车后挂接点沿地球固定 *X* 轴距车轴平面的偏移 | Computed | m |
| `Y` | | | 拖车后挂接点沿地球固定 *Y* 轴距中心平面的偏移 | Computed | m |
| `Z` | | | 拖车后挂接点沿地球固定 *Z* 轴距车轴平面的偏移 | Computed | m |
| `Vel` | `Xdot` | | | 拖车后挂接点沿地球固定 *X* 轴的偏移速度 | Computed | m/s |
| `Ydot` | | | 拖车后挂接点沿地球固定 *Y* 轴的偏移速度 | Computed | m/s |
| `Zdot` | | | 拖车后挂接点沿地球固定 *Z* 轴的偏移速度 | Computed | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | 车辆质心沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | | 车辆质心沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | | 车辆质心沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Ang` | `Beta` | | | 车身侧偏角，*β*    β=VyVx | Computed | rad |
| `AngVel` | `p` | | | 车辆绕车辆固定 *x* 轴的角速度（横滚角速率） | `0` | rad/s |
| `q` | | | 车辆绕车辆固定 *y* 轴的角速度（俯仰角速率） | `0` | rad/s |
| `r` | | | 车辆绕车辆固定 *z* 轴的角速度（偏航角速率） | Computed | rad/s |
| `Acc` | `ax` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | Computed | gn |
| `ay` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | Computed | gn |
| `az` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | gn |
| `xddot` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | Computed | m/s^2 |
| `yddot` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | Computed | m/s^2 |
| `zddot` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | `0` | m/s^2 |
| `AngAcc` | `pdot` | | | 车辆绕车辆固定 *x* 轴的角加速度 | `0` | rad/s |
| `qdot` | | | 车辆绕车辆固定 *y* 轴的角加速度 | `0` | rad/s |
| `rdot` | | | 车辆绕车辆固定 *z* 轴的角加速度 | Computed | rad/s |
| `Forces` | `Body` | `Fx` | | | 沿车辆固定 *x* 轴作用于车辆质心的净力 | Computed | N |
| `Fy` | | | 沿车辆固定 *y* 轴作用于车辆质心的净力 | Computed | N |
| `Fz` | | | 沿车辆固定 *z* 轴作用于车辆质心的净力 | `0` | N |
| `Ext` | `Fx` | | | 沿车辆固定 *x* 轴作用于车辆质心的外力 | Computed | N |
| `Fy` | | | 沿车辆固定 *y* 轴作用于车辆质心的外力 | Computed | N |
| `Fz` | | | 沿车辆固定 *z* 轴作用于车辆质心的外力 | `0` | N |
| `HitchF` | `Fx` | | | 在挂接位置施加到车身上的前挂接力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | | 在挂接位置施加到车身上的前挂接力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | | 在挂接位置施加到车身上的前挂接力沿车辆固定 *z* 轴 | Computed | N |
| `HitchR` | `Fx` | | | 在挂接位置施加到车身上的后挂接力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | | | 在挂接位置施加到车身上的后挂接力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | | | 在挂接位置施加到车身上的后挂接力沿车辆固定 *z* 轴 | Computed | N |
| `FrntAxl` | `Lft` | `Fx` | | 左前轮沿车辆固定 *x* 轴的纵向力 | Computed | N |
| `Fy` | | 左前轮沿车辆固定 *y* 轴的侧向力 | Computed | N |
| `Fz` | | 左前轮沿车辆固定 *z* 轴的法向力 | Computed | N |
| `Rght` | `Fx` | | 右前轮沿车辆固定 *x* 轴的纵向力 | Computed | N |
| `Fy` | | 右前轮沿车辆固定 *y* 轴的侧向力 | Computed | N |
| `Fz` | | 右前轮沿车辆固定 *z* 轴的法向力 | Computed | N |
| `MidlAxl` | `Lft` | `Fx` | | 左中轮沿车辆固定 *x* 轴的纵向力 | Computed | N |
| `Fy` | | 左中轮沿车辆固定 *y* 轴的侧向力 | Computed | N |
| `Fz` | | 左中轮沿车辆固定 *z* 轴的法向力 | Computed | N |
| `Rght` | `Fx` | | 右中轮沿车辆固定 *x* 轴的纵向力 | Computed | N |
| `Fy` | | 右中轮沿车辆固定 *y* 轴的侧向力 | Computed | N |
| `Fz` | | 右中轮沿车辆固定 *z* 轴的法向力 | Computed | N |
| `RearAxl` | `Lft` | `Fx` | | 左后轮沿车辆固定 *x* 轴的纵向力 | Computed | N |
| `Fy` | | 左后轮沿车辆固定 *y* 轴的侧向力 | Computed | N |
| `Fz` | | 左后轮沿车辆固定 *z* 轴的法向力 | Computed | N |
| `Rght` | `Fx` | | 右后轮沿车辆固定 *x* 轴的纵向力 | Computed | N |
| `Fy` | | 右后轮沿车辆固定 *y* 轴的侧向力 | Computed | N |
| `Fz` | | 右后轮沿车辆固定 *z* 轴的法向力 | Computed | N |
| `Tires` | `FrntTires` | `Lft` | `Fx` | 前左轮胎力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | 前左轮胎力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | 前左轮胎力沿车辆固定 *z* 轴 | Computed | N |
| `Rght` | `Fx` | 前右轮胎力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | 前右轮胎力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | 前右轮胎力沿车辆固定 *z* 轴 | Computed | N |
| `RearTires` | `Lft` | `Fx` | 后左轮胎力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | 后左轮胎力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | 后左轮胎力沿车辆固定 *z* 轴 | Computed | N |
| `Rght` | `Fx` | 后右轮胎力沿车辆固定 *x* 轴 | Computed | N |
| `Fy` | 后右轮胎力沿车辆固定 *y* 轴 | Computed | N |
| `Fz` | 后右轮胎力沿车辆固定 *z* 轴 | Computed |  |
| `Drag` | `Fx` | | | 沿车辆固定 *x* 轴作用于车辆质心的阻力 | Computed | N |
| `Fy` | | | 沿车辆固定 *y* 轴作用于车辆质心的阻力 | Computed | N |
| `Fz` | | | 沿车辆固定 *z* 轴作用于车辆质心的阻力 | Computed | N |
| `Grvty` | `Fx` | | | 沿车辆固定 *x* 轴作用于车辆质心的重力 | Computed | N |
| `Fy` | | | 沿车辆固定 *y* 轴作用于车辆质心的重力 | Computed | N |
| `Fz` | | | 沿车辆固定 *z* 轴作用于车辆质心的重力 | Computed | N |
| `Moments` | `Body` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴的车身力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴的车身力矩 | Computed | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴的车身力矩 | `0` | N·m |
| `Drag` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴的阻力力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴的阻力力矩 | Computed | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴的阻力力矩 | `0` | N·m |
| `Ext` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴的外力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴的外力矩 | Computed | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴的外力矩 | `0` | N·m |
| `HitchF` | `Mx` | | | 前挂接位置处绕车辆固定 *x* 轴的挂接力矩 | `0` | N·m |
| `My` | | | 前挂接位置处绕车辆固定 *y* 轴的挂接力矩 | Computed | N·m |
| `Mz` | | | 前挂接位置处绕车辆固定 *z* 轴的挂接力矩 | `0` | N·m |
| `HitchR` | `Mx` | | | 后挂接位置处绕车辆固定 *x* 轴的挂接力矩 | `0` | N·m |
| `My` | | | 后挂接位置处绕车辆固定 *y* 轴的挂接力矩 | Computed | N·m |
| `Mz` | | | 后挂接位置处绕车辆固定 *z* 轴的挂接力矩 | `0` | N·m |
| `FrntAxl` | `Lft` | `Disp` | `x` | | 前左轮沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | 前左轮沿车辆固定 *y* 轴的位移 | Computed | m |
| `z` | | 前左轮沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | 前左轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 前左轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 前左轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 前右轮沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | 前右轮沿车辆固定 *y* 轴的位移 | Computed | m |
| `z` | | 前右轮沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | 前右轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 前右轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 前右轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngFL` | | | 前左轮转向角 | Computed | rad |
| `WhlAngFR` | | | 前右轮转向角 | Computed | rad |
| `MidlAxl` | `Lft` | `Disp` | `x` | | 中间左轮沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | 中间左轮沿车辆固定 *y* 轴的位移 | Computed | m |
| `z` | | 中间左轮沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | 中间左轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 中间左轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 中间左轮沿车辆固定 *z* 轴的速度 | Computed | m/s |
| `Rght` | `Disp` | `x` | | 中右轮沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | 中右轮沿车辆固定 *y* 轴的位移 | Computed | m |
| `z` | | 中右轮沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | 中右轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 中右轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 中右轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 中左轮转向角 | Computed | rad |
| `WhlAngRR` | | | 中右轮转向角 | Computed | rad |
| `RearAxl` | `Lft` | `Disp` | `x` | | 后左轮沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | 后左轮沿车辆固定 *y* 轴的位移 | Computed | m |
| `z` | | 后左轮沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | 后左轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 后左轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 后左轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 后右轮沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | 后右轮沿车辆固定 *y* 轴的位移 | Computed | m |
| `z` | | 后右轮沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | 后右轮沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 后右轮沿车辆固定 *y* 轴的速度 | Computed | m/s |
| `zdot` | | 后右轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 后左轮转向角 | Computed | rad |
| `WhlAngRR` | | | 后右轮转向角 | Computed | rad |
| `HitchF` | `Disp` | | `x` | | 前挂钩沿车辆固定 *x* 轴相对轴平面的偏移 | Input | m |
| `y` | | 前挂钩沿车辆固定 *y* 轴相对中心平面的偏移 | Input | m |
| `z` | | 前挂钩沿地球固定 *z* 轴相对轴平面的偏移 | Input | m |
| `Vel` | | `xdot` | | 前挂钩沿车辆固定 *x* 轴的偏移速度 | Computed | m/s |
| `ydot` | | 前挂钩沿车辆固定 *y* 轴的偏移速度 | Computed | m/s |
| `zdot` | | 前挂钩沿车辆固定 *z* 轴的偏移速度 | `0` | m/s |
| `HitchR` | `Disp` | | `x` | | 后挂钩沿车辆固定 *x* 轴相对轴平面的偏移 | Input | m |
| `y` | | 后挂钩沿车辆固定 *y* 轴相对中心平面的偏移 | Input | m |
| `z` | | 后挂钩沿地球固定 *z* 轴相对轴平面的偏移 | Input | m |
| `Vel` | | `xdot` | | 后挂钩沿车辆固定 *x* 轴的偏移速度 | Computed | m/s |
| `ydot` | | 后挂钩沿车辆固定 *y* 轴的偏移速度 | Computed | m/s |
| `zdot` | | 后挂钩沿车辆固定 *z* 轴的偏移速度 | `0` | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | Computed | W |
| `HitchF` | | | | 前挂钩功率 | Computed | W |
| `HitchR` | | | | 后挂钩功率 | Computed | W |
| `Drag` | | | | 阻力引起的功率损失 | Computed | W |
| `Geom` | `Disp` | | `x` | | 挂车沿车辆固定 *x* 轴相对轴平面的偏移 | Input | m |
| `y` | | 挂车沿车辆固定 *y* 轴相对中心平面的偏移 | Input | m |
| `z` | | 挂车沿车辆固定 *z* 轴相对轴平面的偏移 | Input | m |
| `Vel` | | `xdot` | | 挂车沿车辆固定 *x* 轴的偏移速度 | Computed | m/s |
| `ydot` | | 挂车沿车辆固定 *y* 轴的偏移速度 | Computed | m/s |
| `zdot` | | 挂车沿车辆固定 *z* 轴的偏移速度 | `0` | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | Computed | rad |

e 车辆固定 *z* 轴 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 右中轮沿车辆固定 *x* 轴的位移 | 计算 | m |
| `y` | | 右中轮沿车辆固定 *y* 轴的位移 | 计算 | m |
| `z` | | 右中轮沿车辆固定 *z* 轴的位移 | 计算 | m |
| `Vel` | `xdot` | | 右中轮沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 右中轮沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 右中轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 左中轮转向角 | 计算 | rad |
| `WhlAngRR` | | | 右中轮转向角 | 计算 | rad |
| `RearAxl` | `Lft` | `Disp` | `x` | | 左后轮沿车辆固定 *x* 轴的位移 | 计算 | m |
| `y` | | 左后轮沿车辆固定 *y* 轴的位移 | 计算 | m |
| `z` | | 左后轮沿车辆固定 *z* 轴的位移 | 计算 | m |
| `Vel` | `xdot` | | 左后轮沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 左后轮沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 左后轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 右后轮沿车辆固定 *x* 轴的位移 | 计算 | m |
| `y` | | 右后轮沿车辆固定 *y* 轴的位移 | 计算 | m |
| `z` | | 右后轮沿车辆固定 *z* 轴的位移 | 计算 | m |
| `Vel` | `xdot` | | 右后轮沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 右后轮沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 右后轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 左后轮转向角 | 计算 | rad |
| `WhlAngRR` | | | 右后轮转向角 | 计算 | rad |
| `HitchF` | `Disp` | | `x` | | 沿车辆固定 *x* 轴，前牵引点距车轴平面的偏移 | 输入 | m |
| `y` | | 沿车辆固定 *y* 轴，前牵引点距中心平面的偏移 | 输入 | m |
| `z` | | 沿地球固定 *z* 轴，前牵引点距车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 前牵引点偏移沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 前牵引点偏移沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 前牵引点偏移沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `HitchR` | `Disp` | | `x` | | 沿车辆固定 *x* 轴，后牵引点距车轴平面的偏移 | 输入 | m |
| `y` | | 沿车辆固定 *y* 轴，后牵引点距中心平面的偏移 | 输入 | m |
| `z` | | 沿地球固定 *z* 轴，后牵引点距车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 后牵引点偏移沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 后牵引点偏移沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 后牵引点偏移沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | 计算 | W |
| `HitchF` | | | | 前牵引点功率 | 计算 | W |
| `HitchR` | | | | 后牵引点功率 | 计算 | W |
| `Drag` | | | | 阻力导致的功率损失 | 计算 | W |
| `Geom` | `Disp` | | `x` | | 沿车辆固定 *x* 轴，挂车距车轴平面的偏移 | 输入 | m |
| `y` | | 沿车辆固定 *y* 轴，挂车距中心平面的偏移 | 输入 | m |
| `z` | | 沿车辆固定 *z* 轴，挂车距车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 挂车偏移沿车辆固定 *x* 轴的速度 | 计算 | m/s |
| `ydot` | | 挂车偏移沿车辆固定 *y* 轴的速度 | 计算 | m/s |
| `zdot` | | 挂车偏移沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | 计算 | rad |

| 信号 | | | 描述 | | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | 外部施加的纵向力功率 | | 计算 | W |
| `PwrFyExt` | 外部施加的横向力功率 | | 计算 | W |
| `PwrMzExt` | 外部施加的横摆力矩功率 | | 计算 | W |
| `PwrFwFLx` | 施加在左前轴上的纵向力功率 | | 计算 | W |
| `PwrFwFLy` | 施加在左前轴上的横向力功率 | | 计算 | W |
| `PwrFwFRx` | 施加在右前轴上的纵向力功率 | | 计算 | W |
| `PwrFwFRy` | 施加在右前轴上的横向力功率 | | 计算 | W |
| `PwrFwMLx` | 施加在左中轴上的纵向力功率 | | 计算 | W |
| `PwrFwMLy` | 施加在左中轴上的横向力功率 | | 计算 | W |
| `PwrFwMRx` | 施加在右中轴上的纵向力功率 | | 计算 | W |
| `PwrFwMRy` | 施加在右中轴上的横向力功率 | | 计算 | W |
| `PwrFwRLx` | 施加在左后轴上的纵向力功率 | | 计算 | W |
| `PwrFwRLy` | 施加在左后轴上的横向力功率 | | 计算 | W |
| `PwrFwRRx` | 施加在右后轴上的纵向力功率 | | 计算 | W |
| `PwrFwRRy` | 施加在右后轴上的横向力功率 | | 计算 | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | 纵向阻力功率 | | 计算 | W |
| `PwrFyDrag` | 横向阻力功率 | | 计算 | W |
| `PwrMzDrag` | 阻力俯仰力矩功率 | | 计算 | W |
| `PwrStored` | `PwrStoredGrvty` | 重力势能变化率 | | 计算 | W |
| `PwrStoredxdot` | 纵向动能变化率 | | 计算 | W |
| `PwrStoredydot` | 横向动能变化率 | | 计算 | W |
| `PwrStoredr` | 横摆转动动能变化率 | | 计算 | W |

### **xdot** — 挂车纵向速度 `scalar`

挂车 CG 速度沿车辆固定 *x* 轴，单位为 m/s。

### **ydot** — 挂车横向速度 `scalar`

挂车 CG 速度沿车辆固定 *y* 轴，单位为 m/s。

### **psi** — 横摆角 `scalar`

车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆），单位为 rad。

### **r** — 横摆角速度 `scalar`

车辆角速度 *r*，绕车辆固定 *z* 轴（横摆角速度），单位为 rad/s。

### **FzF** — 前轮法向力 `scalar` | `array`

前轮法向力 *FzF*，沿车辆固定 *z* 轴，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single 2-axle`  `Single 3-axle` | 前轴法向力 | FzF=Fzf | Scalar – `1` |
| `Dual 2-axle`  `Dual 3-axle` | 前轮法向力 | FzF=[FzflFzfr] | Array – `[1x2]` |

### **FzM** — 中轮法向力 `scalar` | `array`

中轮法向力 *FzM*，沿车辆固定 *z* 轴，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single 3-axle` | 中轴法向力 | FzM=Fzm | Scalar – `1` |
| `Dual 3-axle` | 右中轮和左中轮的法向力 | FzM=[FzmlFzrl] | Array – `[1x2]` |

#### 依赖项

要启用此端口，请将 **Vehicle track** 设置为 `Single 3-axle` 或 `Dual 3-axle`。

### **FzR** — 后轮法向力 `scalar` | `array`

后轮法向力 *FzR*，沿车辆固定 *z* 轴，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single 2-axle`  `Single 3-axle` | 后轮法向力 | FzR=Fzr | Scalar – `1` |
| `Dual 2-axle`  `Dual 3-axle` | 后轮法向力 | FzR=[FzrlFzrr] | Array – `[1x2]` |

### **Fhz** — 作用在车体上的牵引力法向分量 `scalar`

在牵引点位置施加到车体上的法向牵引力 *Fhz*，在车辆固定坐标系 *z* 轴方向，单位为 N。

如果启用 **Hitch forces** 参数，模块使用 *Fh* 输入端口沿车辆固定 *z* 轴的分量值来抵消法向牵引力 *Fhz*。

## 参数

#### 选项

### **Vehicle track** — 车辆轨迹类型 `Dual 2-axle`（默认）| `Single 1-axle` | `Dual 1-axle` | `Single 2-axle` | `Dual 3-axle`

使用 **Vehicle track** 参数指定车轮数量。

| Vehicle Track 设置 | 实现 |
| --- | --- |
| `Single 1-axle` | 单轮迹单轴挂车。  - 力沿车轴中心线作用。 - 无横向载荷转移。 |
| `Dual 1-axle` | 双轮迹单轴挂车。力作用在车轴硬点位置。 |
| `Single 2-axle` | 单轮迹双轴挂车。  - 力沿车轴中心线作用。 - 无横向载荷转移。 |
| `Dual 2-axle`（默认） | 双轮迹双轴挂车。力作用在车轴硬点位置。 |
| `Single 3-axle` | 单轮迹三轴挂车。  - 力沿车轴中心线作用。 - 无横向载荷转移。 |
| `Dual 3-axle` | 双轮迹三轴挂车。力作用在车轴硬点位置。 |

### **Axle forces** — 车轴力类型 `External forces`（默认）| `External longitudinal velocity` | `External longitudinal forces`

使用 **Axle forces** 参数指定力类型。

| Axle Forces 设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 模块假设外部纵向速度处于准稳态，且纵向加速度近似为零。 - 由于运动为准稳态，模块使用轮胎侧偏角和线性侧偏刚度计算横向力。 - 当您希望以下情况时，请考虑此设置：  - 生成虚拟传感器信号数据。   - 执行不受动力传动系或非线性轮胎响应影响的高层软件研究。 |
| `External longitudinal forces` | - 模块使用外部纵向力使车辆加速或制动。 - 模块使用轮胎侧偏角和线性侧偏刚度计算横向力。 - 当您希望以下情况时，请考虑此设置：  - 考虑纵向速度变化对横向和横摆运动的影响。   - 通过力而不是外部纵向速度来指定外部纵向运动。   - 将模块连接到牵引执行器、车轮、制动器和牵引点。 |
| `External forces` | - 模块使用外部横向和纵向力来转向、加速或制动车辆。 - 模块不使用转向输入来计算车辆运动。 - 当您需要具有更准确的非线性组合横向和纵向滑移的轮胎模型时，请考虑此设置。 |

#### 输入信号

### **Front wheel steering** — `WhlAngF` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WhlAngF`。

### **Middle wheel steering** — `WhlAngM` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WhlAngM`。

#### 依赖项

要启用此参数，请将 **Vehicle track** 设置为 `Single 3-axle` 或 `Dual 3-axle`。

### **Rear wheel steering** — `WhlAngR` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WhlAngR`。

#### 依赖项

要启用此参数，请将 **Vehicle track** 设置为 `Single 2-axle`、`Dual 2-axle`、`Single 3-axle` 或 `Dual 3-axle`。

### **External wind** — `WindXYZ` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WindXYZ`。

### **External friction** — `Mu` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `Mu`。

#### 依赖项

要启用此参数，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal
  forces`
- `External forces`

### **External forces** — `FExt` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `FExt`。

### **External moments** — `MExt` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `MExt`。

### **Front hitch forces** — `FhF` 输入端口 `on`（默认）| `off`

选择以创建输入端口 `Fh`。

### **Front hitch moments** — `MhF` 输入端口 `on`（默认）| `off`

选择以创建输入端口 `Mh`。

### **Rear hitch forces** — `FhR` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `Fh`。

### **Rear hitch moments** — `MhR` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `Mh`。

### **Initial longitudinal position** — `X_o` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `X_o`。

### **Initial yaw angle** — `psi_o` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `psi_o`。

### **Initial longitudinal velocity** — `xdot_o` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `xdot_o`。

#### 依赖项

要启用此参数，请将 **Axle forces** 设置为 `External longitudinal forces` 或 `External forces`。

### **Initial yaw rate** — `r_o` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `r_o`。

### **Initial lateral position** — `Y_o` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `Y_o`。

### **Air temperature** — `AirTemp` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `AirTemp`。

### **Initial lateral velocity** — `ydot_o` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `ydot_o`。

#### 纵向

### **Number of wheels on front axle, NF** — 前轮数量 `2`（默认）| `scalar`

前轴上的车轮数量 *NF*。该值无量纲。

### **Number of wheels on middle axle, NM** — 中轮数量 `2`（默认）| `scalar`

中轴上的车轮数量 *NM*。该值无量纲。

#### 依赖项

要启用此参数，请将 **Vehicle track** 设置为 `Single 3-axle` 或 `Dual 3-axle`。

### **Number of wheels on rear axle, NR** — 后轮数量 `2`（默认）| `scalar`

后轴上的车轮数量 *NR*。该值无量纲。

要启用此参数，请将 **Vehicle track** 设置为 `Single 2-axle`、`Single 3-axle`、`Dual 2-axle` 或 `Dual 3-axle`。

### **Vehicle mass, m** — 车辆质量 `26000`（默认）| `scalar`

车辆质量 *m*，单位为 kg。

### **Longitudinal distance from center of mass to front axle, a** — 从 CM 到前轴的距离 `4`（默认）| `scalar`

从车辆 CM 到前轴的距离 *a*，单位为 m。

挂车侧视图，显示从 CM 到车轴和牵引点的纵向距离

### **Longitudinal distance from center of mass to middle axle, b** — 从 CM 到中轴的距离 `4.5`（默认）| `scalar`

从车辆 CM 到中轴的距离 *b*，单位为 m。

挂车侧视图，显示从 CM 到车轴和牵引点的纵向距离

#### 依赖项

要启用此参数，请将 **Vehicle track** 设置为 `Single 3-axle` 或 `Dual 3-axle`。

### **Longitudinal distance from center of mass to rear axle, c** — 从 CM 到后轴的距离 `5`（默认）| `scalar`

从车辆 CM 到前轴的距离 *c*，单位为 m。

挂车侧视图，显示从 CM 到车轴和牵引点的纵向距离

#### 依赖项

要启用此参数，请将 **Vehicle track** 设置为 `Single 2-axle`、`Single 3-axle`、`Single 3-axle` 或 `Dual 3-axle`。

### **Vertical distance from center of mass to axle plane, h** — 从 CM 到车轴平面的距离 `2`（默认）| `scalar`

从车辆 CM 到车轴平面的垂直距离 *h*，单位为 m。

挂车侧视图，显示从 CM 到车轴和牵引点的纵向距离

### **Longitudinal distance from center of mass to front hitch, dh\_f** — 到前牵引点的距离 `7.5`（默认）| `scalar`

从质心到前牵引点的纵向距离 *dh\_f*，单位为 m。

挂车侧视图，显示从 CM 到车轴和牵引点的纵向距离

#### 依赖项

要启用此参数，请在 **Input signals** 窗格上选择 **Front hitch forces** 或 **Front hitch moments**。

### **Vertical distance from front hitch to axle plane, hh\_f** — Distance from front hitch to axle plane `0.6` (default) | `scalar`

从前牵引装置到车轴平面的垂直距离，
*hh\_f*，单位为 m。

挂车侧视图，显示从质心到车轴的纵向距离和牵引装置距离

#### 依赖关系

要启用此参数，在 **Input signals** 窗格中，选择
**Front hitch forces** 或 **Front hitch
moments**。

### **Longitudinal distance from center of mass to rear hitch, dh\_r** — Distance to front hitch `7.5` (default) | `scalar`

从质心到后牵引装置的纵向距离，
*dh\_r*，单位为 m。

挂车侧视图，显示从质心到车轴的纵向距离和牵引装置距离

#### 依赖关系

要启用此参数，在 **Input signals** 窗格中，选择
**Rear hitch forces** 或 **Rear hitch
moments**。

### **Vertical distance from front hitch to axle plane, hh\_r** — Distance from rear hitch to axle plane `0.6` (default) | `scalar`

从后牵引装置到车轴平面的垂直距离，
*hh\_r*，单位为 m。

挂车侧视图，显示从质心到车轴的纵向距离和牵引装置距离

#### 依赖关系

要启用此参数，在 **Input signals** 窗格中，选择
**Rear hitch forces** 或 **Rear hitch
moments**。

### **Initial inertial frame longitudinal position, X\_o** — Initial inertial X location `0` (default) | `scalar`

车辆质心沿地球固定
*X* 轴的初始位移，单位为 m。

### **Initial longitudinal velocity, xdot\_o** — Initial velocity `0` (default) | `scalar`

车辆质心沿车辆固定
*x* 轴的初始速度，单位为 m/s。

#### 依赖关系

要启用此参数，将 **Axle forces** 设置为以下选项之一：

- `External longitudinal
  forces`
- `External forces`

#### 横向

### **Mapped corner stiffness** — Selection `off` (default) | `on`

启用映射侧偏刚度计算。

#### 依赖关系

要启用此参数，将 **Axle forces** 设置为以下选项之一：

- `External longitudinal
  velocity`
- `External longitudinal
  forces`

### **Include relaxation length dynamics** — Enable relaxation length dynamics `on` (default) | `off`

启用松弛长度动力学。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Lateral distance from geometric centerline to center of mass, d** — Distance from centerline to CM `0` (default) | `scalar`

从几何中心线到质心的横向距离，
*d*，单位为 m，沿车辆固定
*y* 方向。正值表示挂车质心位于几何中心线右侧。负值表示
挂车质心位于几何中心线左侧。

俯视图，显示轮距宽度和质心相对中心线的偏移

### **Lateral distance from geometric centerline to front hitch, hl\_f** — Distance from centerline to front hitch `0` (default) | `scalar`

从几何中心线到前牵引装置的横向距离，
*hl\_f*，单位为 m，沿车辆固定 *y* 方向。
正值表示挂车牵引装置位于几何
中心线右侧。负值表示挂车牵引装置位于几何中心线左侧。

俯视图，显示车轴宽度和质心相对中心线的偏移

#### 依赖关系

要启用此参数，在 **Input signals** 窗格中，选择
**Front hitch forces** 或 **Front hitch
moments**。

### **Lateral distance from geometric centerline to rear hitch, hl\_r** — Distance from centerline to rear hitch `0` (default) | `scalar`

从几何中心线到后牵引装置的横向距离，
*hl\_r*，单位为 m，沿车辆固定 *y* 方向。
正值表示挂车牵引装置位于几何
中心线右侧。负值表示挂车牵引装置位于几何中心线左侧。

俯视图，显示车轴宽度和质心相对中心线的偏移

#### 依赖关系

要启用此参数，在 **Input signals** 窗格中，选择
**Rear hitch forces** 或 **Rear hitch
moments**。

### **Front track width, w\_f** — Front track width `1.82` (default) | `scalar`

前轮距宽度，*wf*，单位为 m。

俯视图，显示轮距宽度和质心相对中心线的偏移

#### 依赖关系

要启用此参数，将 **Vehicle track** 设置为
`Dual 2-axle`、`Dual
2-axle` 或 `Dual
3-axle`。

### **Middle track width, w\_m** — Middle track width `1.82` (default) | `scalar`

中轮距宽度，*wm*，单位为 m。

俯视图，显示轮距宽度和质心相对中心线的偏移

#### 依赖关系

要启用此参数，将 **Vehicle track** 设置为
`Dual 3-axle`。

### **Rear track width, w\_r** — Rear track width `1.82` (default) | `scalar`

后轮距宽度，*wr*，单位为 m。

俯视图，显示轮距宽度和质心相对中心线的偏移

#### 依赖关系

要启用此参数，将 **Vehicle track** 设置为
`Dual 2-axle` 或 `Dual
3-axle`。

### **Front axle tire corner stiffness, Cy\_f** — Front axle tire stiffness `12.3` (default) | `scalar`

前轮胎侧偏刚度，
*Cyf*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Middle axle tire corner stiffness, Cy\_m** — Middle axle tire stiffness `11.3` (default) | `scalar`

中轮胎侧偏刚度，
*Cym*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Vehicle track** 设置为以下选项之一：

   - `Single
     3-axle`
   - `Dual 3-axle`
2. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
3. 清除 **Mapped corner stiffness**。

### **Rear axle tire corner stiffness, Cy\_r** — Rear axle tire stiffness `11.3` (default) | `scalar`

后轮胎侧偏刚度，*Cyr*，
单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Vehicle track** 设置为以下选项之一：

   - `Single
     2-axle`
   - `Dual 2-axle`
   - `Single
     3-axle`
   - `Dual 3-axle`
2. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
3. 清除 **Mapped corner stiffness**。

### **Front tire(s) relaxation length, sigma\_f** — Relaxation length `.1` (default) | `scalar`

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

### **Middle tire(s) relaxation length, sigma\_m** — Relaxation length `.1` (default) | `scalar`

中轮胎松弛长度，
*σm*，单位为 m。

#### 依赖关系

要启用此参数：

1. 将 **Vehicle track** 设置为以下选项之一：

   - `Single
     3-axle`
   - `Dual 3-axle`
2. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
3. 执行以下任一操作：

   - 选择 **Mapped corner
     stiffness**。
   - 清除 **Mapped corner
     stiffness** 并选择 **Include
     relaxation length dynamics**。

### **Rear tire(s) relaxation length, sigma\_r** — Relaxation length `.1` (default) | `scalar`

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

### **Front axle slip angle breakpoints, alpha\_f\_brk** — Breakpoints `[-.1 .1]` (default) | `vector`

前轴侧偏角断点，
*αfbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Front axle corner data, Cy\_f\_data** — Breakpoints `[-9e3 9e3]` (default) | `vector`

前轴侧偏数据，*Cyfdata*，
单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Middle axle slip angle breakpoints, alpha\_m\_brk** — Breakpoints `[-.1 .1]` (default) | `vector`

中轴侧偏角断点，
*αmbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Middle axle corner data, Cy\_m\_data** — Breakpoints `[-9e3 9e3]` (default) | `vector`

中轴侧偏数据，
*Cymdata*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Rear axle slip angle breakpoints, alpha\_r\_brk** — Breakpoints `[-.1 .1]` (default) | `vector`

后轴侧偏角断点，
*αrbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Rear axle corner data, Cy\_r\_data** — Data `[-9e3 9e3]` (default) | `vector`

后轴侧偏数据，*Cyrdata*，
单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Initial inertial frame lateral displacement, Y\_o** — Position `0` (default) | `scalar`

车辆质心沿地球固定
*Y* 轴的初始位移，单位为 m。

### **Initial lateral velocity, ydot\_o** — Velocity `0` (default) | `scalar`

车辆质心沿车辆固定
*y* 轴的初始速度，单位为 m/s。

#### 横摆

### **Yaw polar inertia, Izz** — Inertia `4000` (default) | `scalar`

横摆极惯性，单位为 kg\*m^2。

### **Initial yaw angle, psi\_o** — Psi rotation `0` (default) | `scalar`

车辆固定坐标系绕地球固定 *Z* 轴的
旋转（横摆），单位为 rad。

### **Initial yaw rate, r\_o** — Yaw rate `0` (default) | `scalar`

车辆绕车辆固定 *z* 轴的角速度（横摆
角速度），单位为 rad/s。

#### 空气动力学

### **Longitudinal drag area, Af** — Effective vehicle cross-sectional area `2` (default) | `scalar`

有效车辆横截面积，
*Af*，用于计算车辆上的空气阻力，
单位为 m2。

### **Longitudinal drag coefficient, Cd** — Air drag coefficient `.3` (default) | `scalar`

空气阻力系数，*Cd*。该值
无量纲。

### **Longitudinal lift coefficient, Cl** — Air lift coefficient `.1` (default) | `scalar`

空气升力系数，*Cl*。该值
无量纲。

### **Longitudinal drag pitch moment, Cpm** — Pitch drag `.1` (default) | `scalar`

纵向阻力俯仰力矩系数，
*Cpm*。该值
无量纲。

### **Relative wind angle vector, beta\_w** — Wind angle `[0:0.01:0.3]` (default) | `vector`

相对风角向量，*βw*，单位为
rad。

### **Side force coefficient vector, Cs** — Side force coefficient `[0:0.03:0.9]` (default) | `vector`

侧向力系数向量系数，
*Cs*。该值无量纲。

### **Yaw moment coefficient vector, Cym** — Yaw moment drag `[0:0.01:0.3]` (default) | `vector`

横摆力矩系数向量，*Cym*。该
值无量纲。

#### 环境

### **Absolute air pressure, Pabs** — Pressure `101325` (default) | `scalar`

环境绝对压力，*Pabs*，
单位为 Pa。

### **Air temperature, Tair** — Temperature `273` (default) | `scalar`

环境绝对温度，*T*，单位为 K。

#### 依赖关系

要启用此参数，清除 **Air temperature**。

### **Gravitational acceleration, g** — Gravity `9.81` (default) | `scalar`

重力加速度，*g*，单位为 m/s^2。

### **Nominal friction scaling factor, mu** — Friction scale factor `1` (default) | `scalar`

标称摩擦比例因子，*μ*。该值
无量纲。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **External Friction**。

#### 仿真

### **Longitudinal velocity tolerance, xdot\_tol** — Tolerance `.01` (default) | `scalar`

纵向速度容差，单位为 m/s。

### **Nominal normal force, Fznom** — Normal force `5000` (default) | `scalar`

标称法向力，单位为 N。

#### 依赖关系

要启用此参数，将 **Axle forces** 设置为以下选项之一：

- `External longitudinal velocity`
- `External longitudinal forces`

### **Geometric longitudinal offset from axle plane, longOff** — Longitudinal offset `0` (default) | `scalar`

车辆底盘沿车辆固定
*x* 轴相对于车轴平面的偏移，单位为 m。使用 3D 可视化引擎时，
可考虑使用该偏移独立于车辆
质心来定位底盘。

### **Geometric lateral offset from center plane, latOff** — Lateral offset `0` (default) | `scalar`

车辆底盘沿车辆固定
*y* 轴相对于中心平面的偏移，单位为 m。使用 3D 可视化引擎时，
可考虑使用该偏移独立于车辆
质心来定位底盘。

### **Geometric vertical offset from axle plane, vertOff** — Vertical offset `0` (default) | `scalar`

车辆底盘沿车辆固定
*z* 轴相对于车轴平面的偏移，单位为 m。使用 3D 可视化引擎时，
可考虑使用该偏移独立于车辆
质心来定位底盘。

### **Wrap Euler angles, wrapAng** — Wrap the Euler angles to the interval `[-pi, pi]` `off` (default) | `on`

将欧拉角包裹到区间 `[-pi, pi]`。对于可能经历超出此区间的车辆横摆
旋转的车辆机动，如果要执行以下操作，可考虑清除该参数：

- 跟踪总车辆横摆旋转。
- 避免车辆状态估计器中的不连续性。

## 所属库

Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有纵向、横向和横摆运动的挂车车身

Trailer Body 3DOF 模块实现刚性单轴、双轴或三轴挂车车身模型，以计算纵向、横向和横摆运动。将模块配置为单轨或双轨。该模块考虑因挂车加速、空气阻力和转向产生的车轴和挂钩反作用力。

在车辆动力学和自动驾驶研究中，当车辆俯仰、侧倾和垂向运动不显著时，使用此模块对非完整车辆运动进行建模。

使用 **Vehicle track** 参数指定车轮数量。

| Vehicle Track 设置 | 实现 |
| --- | --- |
| `Single 1-axle` | 具有单轨和单轴的挂车。  - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual 1-axle` | 具有双轨和单轴的挂车。力作用在车轴硬点位置。 |
| `Single 2-axle` | 具有单轨和双轴的挂车。  - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual 2-axle`(default) | 具有双轨和双轴的挂车。力作用在车轴硬点位置。 |
| `Single 3-axle` | 具有单轨和三轴的挂车。  - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual 3-axle` | 具有双轨和三轴的挂车。力作用在车轴硬点位置。 |

使用 **Axle forces** 参数指定力的类型。

| Axle Forces 设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 模块假设外部纵向速度处于准稳态，且纵向加速度近似为零。 - 由于运动为准稳态，模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 当您希望执行以下操作时，请考虑此设置：  - 生成虚拟传感器信号数据。   - 开展不受动力传动系统或非线性轮胎响应影响的高层级软件研究。 |
| `External longitudinal forces` | - 模块使用外部纵向力使车辆加速或制动。 - 模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 当您希望执行以下操作时，请考虑此设置：  - 考虑纵向速度变化对侧向和横摆运动的影响。   - 通过力而不是外部纵向速度来指定外部纵向运动。   - 将模块连接到牵引执行器、车轮、制动器和挂钩。 |
| `External forces` | - 模块使用外部侧向力和纵向力来转向、加速或制动车辆。 - 模块不使用转向输入来计算车辆运动。 - 当您需要具有更准确的非线性组合侧向和纵向滑移的轮胎模型时，请考虑此设置。 |

要创建附加输入端口，请在 **Input signals** 下选择这些模块参数。

| 输入信号窗格参数 | 输入端口 | 描述 |
| --- | --- | --- |
| **Front wheel steering** | `WhlAngF` | 前轮转角，*δF* |
| **Middle wheel steering** | `WhlAngM` | 中轮转角，*δM* |
| **Rear wheel steering** | `WhlAngR` | 后轮转角，*δR* |
| **External wind** | `WindXYZ` | 风速，*WX*、*WY* 和 *WZ*，在惯性参考系中 |
| **External friction** | `Mu` | 摩擦系数 |
| **External forces** | `FExt` | 作用在车辆重心 (CG) 上的外部力，*Fx*、*Fy* 和 *Fz*，在车辆固定坐标系中 |
| **External moments** | `MExt` | 关于车辆 CG 的外部力矩，*Mx*、*My* 和 *Mz*，在车辆固定坐标系中 |
| **Front hitch forces** | `FhF` | 前挂钩位置处施加到车身上的挂钩力，*FhFx*、*FhFy* 和 *FhFz*，在车辆固定坐标系中 |
| **Front hitch moments** | `MhF` | 前挂钩位置处的挂钩力矩，*MhFx*、*MhFy* 和 *MhFz*，关于车辆固定坐标系 |
| **Rear hitch forces** | `FhR` | 后挂钩位置处施加到车身上的挂钩力，*FhRx*、*FhRy* 和 *FhRz*，在车辆固定坐标系中 |
| **Rear hitch moments** | `MhR` | 后挂钩位置处的挂钩力矩，*MhRx*、*MhRy* 和 *MhRz*，关于车辆固定坐标系 |
| **Initial longitudinal position** | `X_o` | 车辆 CG 沿地球固定 *X* 轴的初始位移 |
| **Initial yaw angle** | `psi_o` | 车辆固定坐标系绕地球固定 *Z* 轴的初始旋转（横摆） |
| **Initial longitudinal velocity** | `xdot_o` | 车辆 CG 沿车辆固定 *x* 轴的初始速度 |
| **Initial yaw rate** | `r_o` | 车辆绕车辆固定 *z* 轴的初始角速度（横摆角速度） |
| **Initial lateral position** | `Y_o` | 车辆 CG 沿地球固定 *Y* 轴的初始位移 |
| **Air temperature** | `AirTemp` | 环境空气温度。如果您希望在运行期间改变温度，请考虑此选项。 |
| **Initial lateral velocity** | `ydot_o` | 车辆 CG 沿车辆固定 *y* 轴的初始速度 |

### 理论

为确定车辆运动，该模块求解刚体平面动力学运动方程。

**Signal Track**

| 计算 | 描述 |
| --- | --- |
| *动力学* | 该模块使用这些方程计算刚体平面动力学。  y¨=−x˙r+Fyf+Fym+Fyr+Fyext+Fhyf+Fhyrmr˙=−aFyf−bFym−cFyr+dhfFhyf−dhrFhyr+Mzext+Mhzf+MhzrIzzr=ψ˙  如果将 **Axle forces** 设为 `External longitudinal forces` 或 `External forces`，该模块使用此方程计算纵向加速度。  x¨=y˙r+Fxf+Fxm+Fxr−gsin(γ)+Fxext+Fhxf+Fhxrm  如果将 **Axle forces** 设为 `External longitudinal velocity`，该模块假定纵向加速度为准稳态。  x¨=0 |
| *外力* | 外力包括阻力和外部力输入。这些力作用在车辆 CG 上。  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    如果将 **Axle forces** 设为 `External longitudinal forces`，该模块使用这些方程。  Fxft=FxfinputFyft=−CyfαfμfFzfFznomFxmt=FxminputFymt=−CymαmμmFzmFznomFxrt=FxrinputFyrt=−CyrαrμrFzrFznom    如果将 **Axle forces** 设为 `External longitudinal velocity`，该模块使用这些方程。  Fxft=0Fyft=−CyfαfμfFzfFznomFxmt=0Fymt=−CymαmμmFzmFznomFxrt=0Fyrt=−CyrαrμrFzrFznom    该模块将法向力除以标称法向载荷，以在重量和载荷转移期间改变有效摩擦参数。该模块保持俯仰和侧倾平衡。  Fzf=bmgcos(γ)−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amgcos(γ)+(x¨−y˙r)mh−hFxext+aFzext+Myexta+b |
| *轮胎力* | 该模块使用局部纵向和侧向速度之比确定侧偏角。  αf=atan(y˙−arx˙)−δfαm=atan(y˙−brx˙)−δmαr=atan(y˙−crx˙)−δr    该模块使用转向角将轮胎力变换到车辆固定坐标系。  Fxf=Fxftcos(δf)−Fyftsin(δf)Fyf=−Fxftsin(δf)+Fyftcos(δf)Fxm=Fxmtcos(δm)−Fymtsin(δm)Fym=−Fxmtsin(δm)+Fymtcos(δm)Fxr=Fxrtcos(δr)−Fyrtsin(δr)Fyr=−Fxrtsin(δr)+Fyrtcos(δr)    如果将 **Axle forces** 设为 `External forces`，该模块假定外部提供的力位于车轴-车轮位置处的车辆固定坐标系中。  Fxf=Fxft=FxfinputFyf=Fyft=FyfinputFxm=Fxmt=FxminputFym=Fymt=FyminputFxr=Fxrt=FxrinputFyr=Fyrt=Fyrinput |

**单轨 — 三轴**

在三个车轴位置作用的垂向、纵向和侧向力的等轴测视图

**单轨 — 两轴**

在两个车轴位置作用的垂向、纵向和侧向力的等轴测视图

**单轨 — 一轴**

在一个车轴位置作用的垂向、纵向和侧向力的等轴测视图

**双轨**

| 计算 | 描述 |
| --- | --- |
| *动力学* | 该模块使用这些方程计算刚体平面动力学。  x¨=y˙r+Fxfl+Fxfr+Fxml+Fxmr+Fxrl+Fxrr−gsin(γ)+Fxext+Fhxf+Fhxrmy¨=−x˙r+Fyfl+Fyfr+Fyml+Fymr+Fyrl+Fyrr+Fyext+Fhyf+Fhyrmr˙=−a(Fyfl+Fyfr)−b(Fyml+Fymr)−c(Fyrl+Fyrr)+dhfFhyf−dhrFhyr+Fxfl(wf2+d)−Fxfr(wf2−d)+Fxml(wm2+d)−Fxmr(wm2−d)+Fxrl(wr2+d)−Fxrr(wr2−d)+Mzext+Mhfz+Mhrz−Fhxfhlf−FhxrhlrIzzr=ψ˙  如果将 **Axle forces** 设为 `External longitudinal velocity`，该模块假定纵向加速度为准稳态。  x¨=0 |
| *外力* | 外力包括阻力和外部力输入。这些力作用在车辆 CG 上。  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    如果将 **Axle forces** 设为 `External longitudinal forces`，该模块使用这些方程。  Fxflt=FxflinputFyflt=−CyflαflμflFzfl2FznomFxfrt=FxfrinputFyfrt=−CyfrαfrμfrFzfr2FznomFxmlt=FxmlinputFymlt=−CymlαmlμmlFzml2FznomFxmrt=FxmrinputFymrt=−CymrαmrμmrFzmr2FznomFxrlt=FxrlinputFyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=FxrrinputFyrrt=−CyrrαrrμrrFzrr2Fznom    如果将 **Axle forces** 设为 `External longitudinal velocity`，该模块使用这些方程。  Fxflt=0Fyflt=−CyflαflμflFzfl2FznomFxfrt=0Fyfrt=−CyfrαfrμfrFzfr2FznomFxmlt=0Fymlt=−CymlαmlμmlFzml2FznomFxmrt=0Fymrt=−CymrαmrμmrFzmr2FznomFxrlt=0Fyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=0Fyrrt=−CyrrαrrμrrFzrr2Fznom    该模块将法向力除以标称法向载荷，以在重量和载荷转移期间改变有效摩擦参数。该模块保持俯仰和侧倾平衡。  Fzf=bmgcos(γ)−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amgcos(γ)+(x¨−y˙r)mh−hFxext+aFzext+Myext(a+b)Fzfl=Fzf+(mh(y¨+x˙r)−hFyext−Mxext)2wfFzfr=Fzf+(−mh(y¨+x˙r)+hFyext+Mxext)2wfFzrl=Fzr+(mh(y¨+x˙r)−hFyext−Mxext)2wrFzrr=Fzr+(−mh(y¨+x˙r)+hFyext+Mxext)2wr |
| *轮胎力* | 该模块使用局部纵向和侧向速度之比确定侧偏角。  αfl=atan(y˙−arx˙+rwf2)−δflαfr=atan(y˙−arx˙−rwf2)−δfrαml=atan(y˙−brx˙+rwm2)−δmlαmr=atan(y˙−brx˙−rwm2)−δmrαrl=atan(y˙−crx˙+rwr2)−δrlαrr=atan(y˙−crx˙−rwr2)−δrr    该模块使用转向角将轮胎力变换到车辆固定坐标系。  Fxfl=Fxfltcos(δfl)−Fyfltsin(δfl)Fxfr=Fxfrtcos(δfr)−Fyfrtsin(δfr)Fxml=Fxmltcos(δml)−Fymltsin(δml)Fxmr=Fxmrtcos(δmr)−Fymrtsin(δmr)Fyfl=−Fxfltsin(δfl)+Fyfltcos(δfl)Fyfr=−Fxfrtsin(δfr)+Fyfrtcos(δfr)Fyml=−Fxmltsin(δml)+Fymltcos(δml)Fymr=−Fxmrtsin(δmr)+Fymrtcos(δmr)Fxrl=Fxrltcos(δrl)−Fyrltsin(δrl)Fxrr=Fxrrtcos(δrr)−Fyrrtsin(δrr)Fyrl=−Fxrltsin(δrl)+Fyrltcos(δrl)Fyrr=−Fxrrtsin(δrr)+Fyrrtcos(δrr)    如果将 **Axle forces** 设为 `External forces`，该模块假定外部提供的力位于车轴-车轮位置处的车辆固定坐标系中。  Fxfl=Fxflt=FxflinputFxfr=Fxfrt=FxfrinputFxml=Fxmlt=FxmlinputFxmr=Fxmrt=FxmrinputFyfl=Fyflt=FyflinputFyfr=Fyfrt=FyfrinputFyml=Fymlt=FymlinputFymr=Fymrt=FymrinputFxrl=Fxrlt=FxrlinputFxrr=Fxrrt=FxrrinputFyrl=Fyrlt=FyrlinputFyrr=Fyrrt=Fyrrinput |

**双轨 — 三轴**

在双轨三轴位置作用的垂向、纵向和侧向力的等轴测视图

**双轨 — 两轴**

在双轨两轴位置作用的垂向、纵向和侧向力的等轴测视图

**双轨 — 一轴**

在双轨一轴位置作用的垂向、纵向和侧向力的等轴测视图

插图使用以下变量。

|  |  |
| --- | --- |
| *a*, *b*, *c* | 前轴、中轴和后轴分别距车辆 CG 在公共车轴平面上的法向投影点的纵向距离 |
| *h* | 牵引车 CG 沿车辆固定 *z* 轴在车轴平面上方的高度 |
| *d* | 沿车辆固定 *y* 轴，从几何中心线到质心的侧向距离 |
| *hh\_f*, *hh\_r* | 前挂接点和后挂接点分别沿车辆固定 *z* 轴在车轴平面上方的高度 |
| *dh\_f*, *dh\_r* | 前挂接点和后挂接点分别距牵引车 CG 在公共车轴平面上的法向投影点的纵向距离 |
| *wf*, *wm*, *wr* | 前轮距、中轮距和后轮距分别 |

**阻力**

此表总结该模块的阻力计算实现。

| 计算 | 描述 |
| --- | --- |
| *坐标变换* | 该模块将风速从惯性坐标系变换到车辆固定坐标系。  wx=Wxcos(ψ)+Wysin(ψ)wy=Wycos(ψ)−Wxsin(ψ)wz=Wz |
| *阻力* | 为确定相对空速，该模块从 CG 车辆速度中减去风速。使用相对空速，该模块确定阻力。  w¯=(x˙−wx)2+(y˙−wy)2+(wz)2Fdx=−12TRCdAfPabs(w¯)2Fdy=−12TRCsAfPabs(w¯)2Fdz=−12TRClAfPabs(w¯)2 |
| *阻力矩* | 使用相对空速，该模块确定阻力矩。  Mdr=−12TRCrmAfPabs(w¯)2(dh+c)Mdp=−12TRCpmAfPabs(w¯)2(dh+c)Mdy=−12TRCymAfPabs(w¯)2(dh+c) |

**侧向侧偏刚度和松弛动力学**

要启用映射侧偏刚度和松弛长度动态参数，将 **Axle forces** 设为 `External longitudinal forces` 或 `External longitudinal velocity`。

| 参数设置 | | 描述 |
| --- | --- | --- |
| Mapped Corner Stiffness | Include Relaxation Length Dynamics |
| `Off`（默认） | `On`（默认） | 该模块对 *Cyf*、*Cym* 和 *Cyr* 使用恒定侧偏刚度值。侧偏角包括松弛长度动态设置。松弛长度近似为作为车轮行程函数的有效侧偏刚度力。 |
| `On` | `On`（默认） | 该模块使用作为侧偏刚度数据和侧偏角函数的查找表。  Cyf=f(αfσ,Cyfdata)Cym=f(αmσ,Cymdata)Cyr=f(αrσ,Cyrdata)αfσ=1s[(αf−αfσ)vwfαf]αmσ=1s[(αm−αmσ)vmfαm]αrσ=1s[(αr−αrσ)vwrαr]    侧偏角包括松弛长度动态设置。松弛长度近似为作为车轮行程函数的有效侧偏刚度力。 |
| `Off`（默认） | `Off` | 该模块使用恒定侧偏刚度值 *Cyf*、*Cym* 和 *Cyr*。 |

这些方程使用以下变量。

|  |  |
| --- | --- |
| x,x˙,x¨ | 车辆 CG 沿车辆固定 *x* 轴的位移、速度和加速度 |
| y,y˙,y¨ | 车辆 CG 沿车辆固定 *y* 轴的位移、速度和加速度 |
| *ψ* | 车辆固定坐标系绕地面固定 *Z* 轴的旋转（横摆） |
| *r*,Ψ˙ | 车辆绕车辆固定 *z* 轴的角速度（横摆角速度） |
| *Fxf*, *Fxm*, *Fxr* | 沿车辆固定 *x* 轴施加到前轮、中轮和后轮的纵向力 |
| *Fyf*, *Fym*, *Fyr* | 沿车辆固定 *y* 轴施加到前轮、中轮和后轮的侧向力 |
| *Fxext*, *Fyext*, *Fzext* | 沿车辆固定 *x*、*y* 和 *z* 轴施加到车辆 CG 的外力 |
| *Fdx*, *Fdy*, *Fdz* | 沿车辆固定 *x*、*y* 和 *z* 轴施加到车辆 CG 的阻力 |
| *Fxinput*, *Fyinput*, *Fzinput* | 沿车辆固定 *x*、*y* 和 *z* 轴施加到车辆 CG 的输入力 |
| *Mxext*, *Myext*, *Mzext* | 绕车辆 CG、绕车辆固定 *x*、*y* 和 *z* 轴的外力矩 |
| *Mdx*, *Mdy*, *Mdz* | 绕车辆 CG、绕车辆固定 *x*、*y* 和 *z* 轴的阻力矩 |
| *Mxinput*, *Myinput*, *Mzinput* | 绕车辆 CG、绕车辆固定 *x*、*y* 和 *z* 轴的输入力矩 |
| *Izz* | 车辆车身绕车辆固定 *z* 轴的转动惯量 |
| *Fxft*, *Fxmt*, *Fxrt* | 沿车辆固定 *x* 轴施加到前轮、中轮和后轮的纵向轮胎力 |
| *Fyft*, *Fymt*, *Fyrt* | 沿车辆固定 *y* 轴施加到前轮、中轮和后轮的侧向轮胎力 |
| *Fxfl*, *Fxfr* | 沿车辆固定 *x* 轴施加到左前轮和右前轮的纵向力 |
| *Fyfl*, *Fyfr* | 沿车辆固定 *y* 轴施加到左前轮和右前轮的侧向力 |
| *Fxrl*, *Fxrr* | 沿车辆固定 *x* 轴施加到左后轮和右后轮的纵向力 |
| *Fyrl*, *Fyrr* | 沿车辆固定 *y* 轴施加到左后轮和右后轮的侧向力 |
| *Fxflt*, *Fxfrt* | 沿车辆固定 *x* 轴施加到左前轮和右前轮的纵向轮胎力 |
| *Fxmlt*, *Fxmrt* | 沿车辆固定 *x* 轴施加到左中轮和右中轮的纵向轮胎力 |
| *Fxrlt*, *Fxrrt* | 沿车辆固定 *x* 轴施加到左后轮和右后轮的纵向轮胎力 |
| *Fyflt*, *Fyfrt* | 沿车辆固定 *y* 轴施加到左前轮和右前轮的侧向轮胎力 |
| *Fymlt*, *Fymrt* | 沿车辆固定 *y* 轴施加到左中轮和右中轮的侧向轮胎力 |
| *Fyrlt*, *Fyrrt* | 沿车辆固定 *y* 轴施加到左后轮和右后轮的侧向力 |
| *Fzf*,*Fzr* | 沿车辆固定 *z* 轴施加到前轮和后轮的法向力 |
| *Fznom* | 沿车辆固定 *z* 轴施加到车轴的标称法向力 |
| *Fzfl*,*Fzfr* | 沿车辆固定 *z* 轴施加到左前轮和右前轮的法向力 |
| *Fzrl*,*Fzrr* | 沿车辆固定 *z* 轴施加到左后轮和右后轮的法向力 |
| *m* | 车辆车身质量 |
| *a*, *b* | 前轮和后轮分别距车辆 CG 在公共车轴平面上的法向投影点的距离 |
| *h* | 车辆 CG 在车轴平面上方的高度 |
| *d* | 沿车辆固定 *y* 轴，从几何中心线到质心的侧向距离 |
| *hh* | 挂接点沿车辆固定 *z* 轴在车轴平面上方的高度 |
| *dh* | 挂接点距牵引车 CG 在公共车轴平面上的法向投影点的纵向距离 |
| *hl* | 沿车辆固定 *y* 轴，从质心到挂接点的侧向距离。 |
| *αf*, *αr* | 前轮和后轮侧偏角 |
| *αfl*, *αfr* | 左前轮和右前轮侧偏角 |
| *αrl*, *αrr* | 左后轮和右后轮侧偏角 |
| *δf*, *δr* | 前轮和后轮转向角 |
| *δrl*, *δrr* | 左后轮和右后轮转向角 |
| *δfl*, *δfr* | 左前轮和右前轮转向角 |
| *wf*, *wr* | 前轮距和后轮距 |
| *Cyf*, *Cyr* | 前轮和后轮侧偏刚度 |
| *Cyfdata*, *Cyrdata* | 前轮和后轮侧偏刚度数据 |
| *σf*, *σr* | 前轮和后轮松弛长度 |
| *αfσ*, *αrσ* | 包括松弛长度的前轮和后轮侧偏角 |
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
