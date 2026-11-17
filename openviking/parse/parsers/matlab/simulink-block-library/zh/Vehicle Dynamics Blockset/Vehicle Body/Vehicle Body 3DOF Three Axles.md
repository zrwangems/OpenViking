---
type: simulink-block
title: 'Vehicle Body 3DOF Three Axles'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'vehiclebody3dofthreeaxles'
documentation_source_path: 'ref/vehiclebody3dofthreeaxles.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Body 3DOF Three Axles

## 端口
```yaml
ports:
- name: WhlAngF
  summary: 前轮转向角 scalar | array
  direction: input
- name: WhlAngM
  summary: 中轮转向角 scalar | array
  direction: input
- name: WhlAngR
  summary: 后轮转向角 scalar | array
  direction: input
- name: xdotin
  summary: 纵向速度 scalar
  direction: input
- name: FwF
  summary: 前轮上的总力 scalar | array
  direction: input
- name: FwM
  summary: 中轮上的总力 scalar | array
  direction: input
- name: FwR
  summary: 后轮总力 scalar | array
  direction: input
- name: FExt
  summary: 车辆 CG 上的外力 array
  direction: input
- name: MExt
  summary: 绕车辆 CG 的外力矩 array
  direction: input
- name: Fh
  summary: 作用在车体上的牵引力 array
  direction: input
- name: Mh
  summary: 绕车体的牵引力矩 array
  direction: input
- name: WindXYZ
  summary: 风速 array
  direction: input
- name: Mu
  summary: 轮胎摩擦系数 array
  direction: input
- name: AirTemp
  summary: 环境空气温度 scalar
  direction: input
- name: X_o
  summary: 初始纵向位置 scalar
  direction: input
- name: Y_o
  summary: 初始横向位置 scalar
  direction: input
- name: xdot_o
  summary: 初始纵向位置 scalar
  direction: input
- name: ydot_o
  summary: 初始横向位置 scalar
  direction: input
- name: psi_o
  summary: 初始偏航角 scalar
  direction: input
- name: r_o
  summary: 初始偏航角速率 scalar
  direction: input
- name: Info
  summary: 车辆数据总线
  direction: output
- name: xdot
  summary: 车辆纵向速度 scalar
  direction: output
- name: ydot
  summary: 车辆横向速度 scalar
  direction: output
- name: psi
  summary: 横摆 scalar
  direction: output
- name: r
  summary: 横摆角速度 scalar
  direction: output
- name: FzF
  summary: 前轮法向力 scalar | array
  direction: output
- name: FzM
  summary: 中轮法向力 scalar | array
  direction: output
- name: FzR
  summary: 后轮法向力 scalar | array
  direction: output
```

### 输入

### **WhlAngF** — 前轮转向角 `scalar` | `array`

前轮转向角，
*δF*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | *δF* | 标量 – `1` |
| `Dual` | δF=[δflδfr]  或  [δflδfr] | 数组 – `[1x2]` 或 `[2x1]` |

#### 依赖

要启用此端口，请在 **Input signals**
窗格中，选择 **Front wheel steering**。

### **WhlAngM** — 中轮转向角 `scalar` | `array`

中轮转向角，
*δM*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | *δM* | 标量 – `1` |
| `Dual` | δM=[δmlδmr]  或  [δmlδmr] | 数组 – `[1x2]` 或 `[2x1]` |

#### 依赖

要启用此端口，请在 **Input signals**
窗格中，选择 **Middle wheel steering**。

### **WhlAngR** — 后轮转向角 `scalar` | `array`

后轮转向角，
*δR*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | *δR* | 标量 – `1` |
| `Dual` | δR=[δrlδrr]  或  [δrlδrr] | 数组 – `[1x2]` 或 `[2x1]` |

#### 依赖

要启用此端口，请在 **Input signals**
窗格中，选择 **Rear wheel steering**。

### **xdotin** — 纵向速度 `scalar`

车辆质心沿车辆固定
*x* 轴的速度，单位为 m/s。

#### 依赖

要启用此端口，请将 **Axle forces** 设置为
`External longitudinal
velocity`。

### **FwF** — 前轮上的总力 `scalar` | `array`

前轮上的力，
*FwF*，沿
车辆固定轴方向，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | 前轮上的纵向力 | FwF=Fxf | 标量 – `1` |
| `External forces` | 前轮上的纵向力和横向力 | FwF=[FxfFyf]  或 [FxfFyf] | 数组 – `[1x2]` 或 `[2x1]` |
| `Dual` | `External longitudinal forces` | 前轮上的纵向力 | FwF=[FxflFxfr] 或 [FxflFxfr] | 数组 – `[1x2]` 或 `[2x1]` |
| `External forces` | 前轮上的纵向力和横向力 | FwF=[FxflFyflFxfrFyfr] | 数组 – `[2x2]` |

#### 依赖

要启用此端口，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FwM** — 中轮上的总力 `scalar` | `array`

中轮上的力，
*FwM*，沿
车辆固定轴方向，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | 中轮上的纵向力 | FwM=Fxr | 标量 – `1` |
| `External forces` | 中轮上的纵向力和横向力 | FwM=[FxmFym]  或 [FxmFym] | 数组 – `[1x2]` 或 `[2x1]` |
| `Dual` | `External longitudinal forces` | 中轮上的纵向力 | FwM=[FxmlFxmr] 或 [FxmlFxmr] | 数组 – `[1x2]` 或 `[2x1]` |
| `External forces` | 中轮上的纵向力和横向力 | FwM=[FxmlFxmrFymlFymr] | 数组 – `[2x2]` |

#### 依赖

要启用此端口，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FwR** — 后轮总力 `scalar` | `array`

后轮上的力，
*FwR*，沿
车辆固定轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | 后轮上的纵向力 | FwR=Fxr | 标量 – `1` |
| `External forces` | 后轮上的纵向力和横向力 | FwR=[FxrFyr]  or [FxrFyr] | 数组 – `[1x2]` 或 `[2x1]` |
| `Dual` | `External longitudinal forces` | 后轮上的纵向力 | FwR=[FxrlFxrr] or [FxrlFxrr] | 数组 – `[1x2]` 或 `[2x1]` |
| `External forces` | 后轮上的纵向力和横向力 | FwR=[FxrlFyrlFxrrFyrr] | 数组 – `[2x2]` |

#### 依赖关系

要启用此端口，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FExt** — 车辆 CG 上的外力 `array`

施加到车辆 CG 上的外力，
*Fxext*，
*Fyext*，
*Fzext*，在
车辆固定坐标系中，单位为 N。信号数组维度为
`[1x3]` 或 `[3x1]`。

#### 依赖关系

要启用此端口，请在 **Input signals**
窗格中，选择 **External forces**。

### **MExt** — 绕车辆 CG 的外力矩 `array`

绕车辆 CG 的外力矩，
*Mx*，
*My*，
*Mz*，在车辆固定
坐标系中，单位为 N·m。信号数组维度为 `[1x3]`
或 `[3x1]`。

#### 依赖关系

要启用此端口，请在 **Input signals**
窗格中，选择 **External moments**。

### **Fh** — 作用在车体上的牵引力 `array`

施加到车体牵引点处的牵引力，
*Fhx*，
*Fhy*，
*Fhz*，在车辆固定坐标系中，单位为 N，
指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下，选择
**Hitch forces**。

### **Mh** — 绕车体的牵引力矩 `array`

牵引点处的牵引力矩，*Mhx*，
*Mhy*，
*Mhz*，绕
车辆固定坐标系，单位为 N·m，指定为 `1-by-3` 或
`3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下，选择 **Hitch
moments**。

### **WindXYZ** — 风速 `array`

风速，*Wx*，
*Wy*，
*Wz* 沿惯性
*X* 轴、*Y* 轴和
*Z* 轴，单位为 m/s。信号数组维度为
`[1x3]` 或 `[3x1]`。

#### 依赖关系

要启用此端口，请在 **Input signals**
窗格中，选择 **External wind**。

### **Mu** — 轮胎摩擦系数 `array`

轮胎摩擦系数，*μ*，无量纲。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single (bicycle)` | Mu=[μfμmμr] or [μfμmμr] | 数组 – `[1x3]` 或 `[3x1]` |
| `Dual` | Mu=[μflμfrμmlμmrμrlμrr] | 数组 – `[3x2]` |

#### 依赖关系

要启用此端口，请在 **Input signals**
窗格中，选择 **External friction**。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，单位为 K。

#### 依赖关系

要启用此端口，请在 **Input signals**
窗格中，选择 **Air temperature**。

### **X\_o** — 初始纵向位置 `scalar`

车辆 CG 沿地球固定
*X* 轴的初始位移，单位为 m。

#### 依赖关系

要启用此端口，请在 **Input signals**
窗格中，选择 **Initial longitudinal
position**。

### **Y\_o** — 初始横向位置 `scalar`

车辆 CG 沿地球固定
*Y* 轴的初始位移，单位为 m。

#### 依赖关系

要启用此端口，请在 **Input signals**
窗格中，选择 **Initial lateral position**。

### **xdot\_o** — 初始纵向位置 `scalar`

车辆 CG 沿车辆固定
*x* 轴的初始速度，单位为 m/s。

#### 依赖关系

要启用此端口：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     forces`
   - `External
     forces`
2. 在 **Input signals** 窗格中，选择
   **Initial longitudinal
   velocity**

### **ydot\_o** — 初始横向位置 `scalar`

车辆 CG 沿车辆固定
*y* 轴的初始速度，单位为 m/s。

#### 依赖关系

要启用此端口，请在 **输入信号** 窗格中，选择 **初始横向速度**。

### **psi\_o** — 初始偏航角 `scalar`

车辆固定坐标系绕地球固定 *Z* 轴的旋转（偏航），单位为 rad。

#### 依赖关系

要启用此端口，请在 **输入信号** 窗格中，选择 **初始偏航角**。

### **r\_o** — 初始偏航角速率 `scalar`

车辆绕车辆固定 *z* 轴的角速度（偏航角速率），单位为 rad/s。

#### 依赖关系

要启用此端口，请在 **输入信号** 窗格中，选择 **初始偏航角速率**。
### 输出

### **Info** — 车辆数据总线

车辆数据，以包含以下模块值的总线信号形式返回。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆 CG 沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | | 车辆 CG 沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | | 车辆 CG 沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 车辆 CG 沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | | 车辆 CG 沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | | 车辆 CG 沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕地球固定 *X* 轴的旋转（横滚） | `0` | rad |
| `theta` | | | 车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰） | `0` | rad |
| `psi` | | | 车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆） | 计算所得 | rad |
| `FrntAxl` | `Lft` | `Disp` | `X` | | 前左轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 前左轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 前左轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前左轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 前左轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 前左轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 前右轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 前右轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 前右轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前右轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 前右轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 前右轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `MidlAxl` | `Lft` | `Disp` | `X` | | 中左轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 中左轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 中左轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 中左轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 中左轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 中左轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 中右轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 中右轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 中右轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 中右轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 中右轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 中右轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `RearAxl` | `Lft` | `Disp` | `X` | | 后左轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 后左轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 后左轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后左轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 后左轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 后左轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 后右轮沿地球固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 后右轮沿地球固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 后右轮沿地球固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后右轮沿地球固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 后右轮沿地球固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 后右轮沿地球固定 *Z* 轴的速度 | `0` | m/s |
| `Hitch` | `Disp` | `X` | | | 拖车挂钩沿地球固定 *X* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Y` | | | 拖车挂钩沿地球固定 *Y* 轴相对于中心平面的偏移 | 计算所得 | m |
| `Z` | | | 拖车挂钩沿地球固定 *Z* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Vel` | `Xdot` | | | 拖车挂钩沿地球固定 *X* 轴的偏移速度 | 计算所得 | m/s |
| `Ydot` | | | 拖车挂钩沿地球固定 *Y* 轴的偏移速度 | 计算所得 | m/s |
| `Zdot` | | | 拖车挂钩沿地球固定 *Z* 轴的偏移速度 | 计算所得 | m/s |
| `Geom` | `Disp` | `X` | | | 车辆底盘沿地球固定 *X* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Y` | | | 车辆底盘沿地球固定 *Y* 轴相对于中心平面的偏移 | 计算所得 | m |
| `Z` | | | 车辆底盘沿地球固定 *Z* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Vel` | `Xdot` | | | 车辆底盘沿地球固定 *X* 轴的偏移速度 | 计算所得 | m/s |
| `Ydot` | | | 车辆底盘沿地球固定 *Y* 轴的偏移速度 | 计算所得 | m/s |
| `Zdot` | | | 车辆底盘沿地球固定 *Z* 轴的偏移速度 | 计算所得 | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | 车辆 CG 沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | | 车辆 CG 沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | | 车辆 CG 沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Ang` | `Beta` | | | 车身侧偏角，*β*    β=VyVx | 计算所得 | rad |
| `AngVel` | `p` | | | 车辆绕车辆固定 *x* 轴的角速度（横滚角速率） | `0` | rad/s |
| `q` | | | 车辆绕车辆固定 *y* 轴的角速度（俯仰角速率） | `0` | rad/s |
| `r` | | | 车辆绕车辆固定 *z* 轴的角速度（横摆角速率） | 计算所得 | rad/s |
| `Acc` | `ax` | | | 车辆 CG 沿车辆固定 *x* 轴的加速度 | 计算所得 | gn |
| `ay` | | | 车辆 CG 沿车辆固定 *y* 轴的加速度 | 计算所得 | gn |
| `az` | | | 车辆 CG 沿车辆固定 *z* 轴的加速度 | `0` | gn |
| `xddot` | | | 车辆 CG 沿车辆固定 *x* 轴的加速度 | 计算所得 | m/s^2 |
| `yddot` | | | 车辆 CG 沿车辆固定 *y* 轴的加速度 | 计算所得 | m/s^2 |
| `zddot` | | | 车辆 CG 沿车辆固定 *z* 轴的加速度 | `0` | m/s^2 |
| `AngAcc` | `pdot` | | | 车辆绕车辆固定 *x* 轴的角加速度 | `0` | rad/s |
| `qdot` | | | 车辆绕车辆固定 *y* 轴的角加速度 | `0` | rad/s |
| `rdot` | | | 车辆绕车辆固定 *z* 轴的角加速度 | 计算所得 | rad/s |
| `Forces` | `Body` | `Fx` | | | 车辆 CG 上沿车辆固定 *x* 轴的合力 | 计算所得 | N |
| `Fy` | | | 车辆 CG 上沿车辆固定 *y* 轴的合力 | 计算所得 | N |
| `Fz` | | | 车辆 CG 上沿车辆固定 *z* 轴的合力 | `0` | N |
| `Ext` | `Fx` | | | 车辆 CG 上沿车辆固定 *x* 轴的外力 | 计算所得 | N |
| `Fy` | | | 车辆 CG 上沿车辆固定 *y* 轴的外力 | 计算所得 | N |
| `Fz` | | | 车辆 CG 上沿车辆固定 *z* 轴的外力 | `0` | N |
| `Hitch` | `Fx` | | | 在挂钩位置施加于车身的沿车辆固定 *x* 轴的挂钩力 | 计算所得 | N |
| `Fy` | | | 在挂钩位置施加于车身的沿车辆固定 *y* 轴的挂钩力 | 计算所得 | N |
| `Fz` | | | 在挂钩位置施加于车身的沿车辆固定 *z* 轴的挂钩力 | 计算所得 | N |
| `FrntAxl` | `Lft` | `Fx` | | 左前轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 左前轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 左前轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Rght` | `Fx` | | 右前轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 右前轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 右前轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `MidlAxl` | `Lft` | `Fx` | | 左中轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 左中轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 左中轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Rght` | `Fx` | | 右中轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 右中轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 右中轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `RearAxl` | `Lft` | `Fx` | | 后左轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 后左轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 后左轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Rght` | `Fx` | | 后右轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 后右轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 后右轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Tires` | `FrntTires` | `Lft` | `Fx` | 前左轮胎沿车辆固定 *x* 轴的力 | 计算所得 | N |
| `Fy` | 前左轮胎沿车辆固定 *y* 轴的力 | 计算所得 | N |
| `Fz` | 前左轮胎沿车辆固定 *z* 轴的力 | 计算所得 | N |
| `Rght` | `Fx` | 前右轮胎沿车辆固定 *x* 轴的力 | 计算所得 | N |
| `Fy` | 前右轮胎沿车辆固定 *y* 轴的力 | 计算所得 | N |
| `Fz` | 前右轮胎沿车辆固定 *z* 轴的力 | 计算所得 | N |
| `RearTires` | `Lft` | `Fx` | 后左轮胎沿车辆固定 *x* 轴的力 | 计算所得 | N |
| `Fy` | 后左轮胎沿车辆固定 *y* 轴的力 | 计算所得 | N |
| `Fz` | 后左轮胎沿车辆固定 *z* 轴的力 | 计算所得 | N |
| `Rght` | `Fx` | 后右轮胎沿车辆固定 *x* 轴的力 | 计算所得 | N |
| `Fy` | 后右轮胎沿车辆固定 *y* 轴的力 | 计算所得 | N |
| `Fz` | 后右轮胎沿车辆固定 *z* 轴的力 | 计算所得 |  |
| `Drag` | `Fx` | | | 车辆 CG 上沿车辆固定 *x* 轴的阻力 | 计算所得 | N |
| `Fy` | | | 车辆 CG 上沿车辆固定 *y* 轴的阻力 | 计算所得 | N |
| `Fz` | | | 车辆 CG 上沿车辆固定 *z* 轴的阻力 | 计算所得 | N |
| `Grvty` | `Fx` | | | 车辆 CG 上沿车辆固定 *x* 轴的重力 | 计算所得 | N |
| `Fy` | | | 车辆 CG 上沿车辆固定 *y* 轴的重力 | 计算所得 | N |
| `Fz` | | | 车辆 CG 上沿车辆固定 *z* 轴的重力 | 计算所得 | N |
| `Moments` | `Body` | `Mx` | | | 车辆 CG 上绕车辆固定 *x* 轴的车身力矩 | `0` | N·m |
| `My` | | | 车辆 CG 上绕车辆固定 *y* 轴的车身力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆 CG 上绕车辆固定 *z* 轴的车身力矩 | `0` | N·m |
| `Drag` | `Mx` | | | 车辆 CG 上绕车辆固定 *x* 轴的阻力力矩 | `0` | N·m |
| `My` | | | 车辆 CG 上绕车辆固定 *y* 轴的阻力力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆 CG 上绕车辆固定 *z* 轴的阻力力矩 | `0` | N·m |
| `Ext` | `Mx` | | | 车辆 CG 上绕车辆固定 *x* 轴的外力矩 | `0` | N·m |
| `My` | | | 车辆 CG 上绕车辆固定 *y* 轴的外力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆 CG 上绕车辆固定 *z* 轴的外力矩 | `0` | N·m |
| `Hitch` | `Mx` | | | 挂钩位置处绕车辆固定 *x* 轴的挂钩力矩 | `0` | N·m |
| `My` | | | 挂钩位置处绕车辆固定 *y* 轴的挂钩力矩 | 计算所得 | N·m |
| `Mz` | | | 挂钩位置处绕车辆固定 *z* 轴的挂钩力矩 | `0` | N·m |
| `FrntAxl` | `Lft` | `Disp` | `x` | | 前左轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 前左轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 前左轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 前左轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 前左轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 前左轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 前右轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 前右轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 前右轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 前右轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 前右轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 前右轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngFL` | | | 前左轮转向角 | 计算所得 | rad |
| `WhlAngFR` | | | 前右轮转向角 | 计算所得 | rad |
| `MidlAxl` | `Lft` | `Disp` | `x` | | 中左轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 中左轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 中左轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 中左轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 中左轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 中左轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 中右轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 中右轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 中右轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 中右轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 中右轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 中右轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 中左轮转向角 | 计算所得 | rad |
| `WhlAngRR` | | | 中右轮转向角 | 计算所得 | rad |
| `RearAxl` | `Lft` | `Disp` | `x` | | 后左轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 后左轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 后左轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 后左轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 后左轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 后左轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `x` | | 后右轮沿车辆固定 *x* 轴的位移 | 计算所得 | m |
| `y` | | 后右轮沿车辆固定 *y* 轴的位移 | 计算所得 | m |
| `z` | | 后右轮沿车辆固定 *z* 轴的位移 | 计算所得 | m |
| `Vel` | `xdot` | | 后右轮沿车辆固定 *x* 轴的速度 | 计算所得 | m/s |
| `ydot` | | 后右轮沿车辆固定 *y* 轴的速度 | 计算所得 | m/s |
| `zdot` | | 后右轮沿车辆固定 *z* 轴的速度 | `0` | m/s |
| `Steer` | `WhlAngRL` | | | 后左轮转向角 | 计算所得 | rad |
| `WhlAngRR` | | | 后右轮转向角 | 计算所得 | rad |
| `Hitch` | `Disp` | | `x` | | 挂钩沿车辆固定 *x* 轴相对于车轴平面的偏移 | 输入 | m |
| `y` | | 挂钩沿车辆固定 *y* 轴相对于中心平面的偏移 | 输入 | m |
| `z` | | 挂钩沿地球固定 *z* 轴相对于车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 挂钩沿车辆固定 *x* 轴的偏移速度 | 计算所得 | m/s |
| `ydot` | | 挂钩沿车辆固定 *y* 轴的偏移速度 | 计算所得 | m/s |
| `zdot` | | 挂钩沿车辆固定 *z* 轴的偏移速度 | `0` | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | 计算所得 | W |
| `Hitch` | | | | 挂钩导致的功率损耗 | 计算所得 | W |
| `Drag` | | | | 阻力导致的功率损耗 | 计算所得 | W |
| `Geom` | `Disp` | | `x` | | 车辆底盘沿车辆固定 *x* 轴相对于车轴平面的偏移 | 输入 | m |
| `y` | | 车辆底盘沿车辆固定 *y* 轴相对于中心平面的偏移 | 输入 | m |
| `z` | | 车辆底盘沿地球固定 *z* 轴相对于车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 车辆底盘沿车辆固定 *x* 轴的偏移速度 | 计算所得 | m/s |
| `ydot` | | 车辆底盘沿车辆固定 *y* 轴的偏移速度 | 计算所得 | m/s |
| `zdot` | | 车辆底盘沿车辆固定 *z* 轴的偏移速度 | `0` | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | 计算所得 | rad |

| 信号 | | | 描述 | | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | 外部施加的纵向力功率 | | 计算值 | W |
| `PwrFyExt` | 外部施加的横向力功率 | | 计算值 | W |
| `PwrMzExt` | 外部施加的横摆力矩功率 | | 计算值 | W |
| `PwrFwFLx` | 施加在前左轴的纵向力功率 | | 计算值 | W |
| `PwrFwFLy` | 施加在前左轴的横向力功率 | | 计算值 | W |
| `PwrFwFRx` | 施加在前右轴的纵向力功率 | | 计算值 | W |
| `PwrFwFRy` | 施加在前右轴的横向力功率 | | 计算值 | W |
| `PwrFwMLx` | 施加在中左轴的纵向力功率 | | 计算值 | W |
| `PwrFwMLy` | 施加在中左轴的横向力功率 | | 计算值 | W |
| `PwrFwMRx` | 施加在中右轴的纵向力功率 | | 计算值 | W |
| `PwrFwMRy` | 施加在中右轴的横向力功率 | | 计算值 | W |
| `PwrFwRLx` | 施加在后左轴的纵向力功率 | | 计算值 | W |
| `PwrFwRLy` | 施加在后左轴的横向力功率 | | 计算值 | W |
| `PwrFwRRx` | 施加在后右轴的纵向力功率 | | 计算值 | W |
| `PwrFwRRy` | 施加在后右轴的横向力功率 | | 计算值 | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | 纵向阻力功率 | | 计算值 | W |
| `PwrFyDrag` | 横向阻力功率 | | 计算值 | W |
| `PwrMzDrag` | 阻力俯仰力矩功率 | | 计算值 | W |
| `PwrStored` | `PwrStoredGrvty` | 重力势能变化率 | | 计算值 | W |
| `PwrStoredxdot` | 纵向动能变化率 | | 计算值 | W |
| `PwrStoredydot` | 横向动能变化率 | | 计算值 | W |
| `PwrStoredr` | 横摆转动动能变化率 | | 计算值 | W |

### **xdot** — 车辆纵向速度 `scalar`

车辆质心沿车辆固定 *x* 轴的速度，单位为 m/s。

### **ydot** — 车辆横向速度 `scalar`

车辆质心沿车辆固定 *y* 轴的速度，单位为 m/s。

### **psi** — 横摆 `scalar`

车辆固定坐标系绕大地固定 *Z* 轴的旋转（横摆），单位为 rad。

### **r** — 横摆角速度 `scalar`

车辆绕车辆固定 *z* 轴的角速度 `r`（横摆角速度），单位为 rad/s。

### **FzF** — 前轮法向力 `scalar` | `array`

前轮沿车辆固定 *z* 轴的法向力 *FzF*，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single (bicycle)` | 前轴法向力 | FzF=Fzf | 标量 – `1` |
| `Dual` | 右前轮和左前轮法向力 | FzF=[FzflFzfr] | 数组 – `[1x2]` |

### **FzM** — 中轮法向力 `scalar` | `array`

中轮沿车辆固定 *z* 轴的法向力 *FzM*，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single (bicycle)` | 中轴法向力 | FzM=Fzm | 标量 – `1` |
| `Dual` | 右中轮和左中轮法向力 | FzM=[FzmlFzrl] | 数组 – `[1x2]` |

### **FzR** — 后轮法向力 `scalar` | `array`

后轮沿车辆固定 *z* 轴的法向力 *FzR*，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single (bicycle)` | 后轮法向力 | FzR=Fzr | 标量 – `1` |
| `Dual` | 右后轮和左后轮法向力 | FzR=[FzrlFzrr] | 数组 – `[1x2]` |
## 参数
```yaml
parameters:
- name: Vehicle track
  summary: 车辆车轮数量 Dual（默认）| Single (bicycle)
  group: ''
- name: Axle forces
  summary: 车轴力类型 External longitudinal velocity（默认）| External longitudinal forces | External forces
  group: ''
- name: Front wheel steering
  summary: WhlAngF 输入端口 on（默认）| off
  group: ''
- name: Middle wheel steering
  summary: WhlAngM 输入端口 off（默认）| on
  group: ''
- name: Rear wheel steering
  summary: WhlAngR 输入端口 off（默认）| on
  group: ''
- name: External wind
  summary: WindXYZ 输入端口 off（默认）| on
  group: ''
- name: External friction
  summary: Mu 输入端口 off（默认）| on
  group: ''
- name: External forces
  summary: FExt 输入端口 off（默认）| on
  group: ''
- name: External moments
  summary: MExt 输入端口 off（默认）| on
  group: ''
- name: Hitch forces
  summary: Fh 输入端口 on（默认）| off
  group: ''
- name: Hitch moments
  summary: Mh 输入端口 on（默认）| off
  group: ''
- name: Initial longitudinal position
  summary: X_o 输入端口 off（默认）| on
  group: ''
- name: Initial yaw angle
  summary: psi_o 输入端口 off（默认）| on
  group: ''
- name: Initial longitudinal velocity
  summary: xdot_o 输入端口 off（默认）| on
  group: ''
- name: Initial yaw rate
  summary: r_o 输入端口 off（默认）| on
  group: ''
- name: Initial lateral position
  summary: Y_o 输入端口 off（默认）| on
  group: ''
- name: Air temperature
  summary: AirTemp 输入端口 off（默认）| on
  group: ''
- name: 初始横向速度
  summary: ydot_o 输入端口 off（默认）| on
  group: ''
- name: 前轴车轮数，NF
  summary: 前轮数量 2（默认）| scalar
  group: ''
- name: 中轴车轮数，NM
  summary: 中轮数量 2（默认）| scalar
  group: ''
- name: 后轴车轮数，NR
  summary: 后轮数量 2（默认）| scalar
  group: ''
- name: 车辆质量，m
  summary: 车辆质量 47000（默认）| scalar
  group: ''
- name: 从质心到前轴的纵向距离，a
  summary: 从质心到前轴的距离 0.5（默认）| scalar
  group: ''
- name: 从质心到中轴的纵向距离，b
  summary: 从质心到中轴的距离 4.5（默认）| scalar
  group: ''
- name: 从质心到后轴的纵向距离，c
  summary: 从质心到后轴的距离 5.7（默认）| scalar
  group: ''
- name: 从质心到车轴平面的垂直距离，h
  summary: 从质心到车轴平面的距离 0.3（默认）| scalar
  group: ''
- name: 从牵引座到车轴平面的垂直距离，hh
  summary: 从牵引座到车轴平面的距离 0.5（默认）| scalar
  group: ''
- name: 从质心到牵引座的纵向距离，dh
  summary: 从质心到牵引座的距离 5（默认）| scalar
  group: ''
- name: 初始惯性坐标系纵向位置，X_o
  summary: 初始纵向位移 0（默认）| scalar
  group: ''
- name: 初始纵向速度，xdot_o
  summary: 初始纵向速度 0（默认）| scalar
  group: ''
- name: 映射侧偏刚度
  summary: 启用映射侧偏刚度 off（默认）| on
  group: ''
- name: 包含松弛长度动力学
  summary: 启用松弛长度动力学 on（默认）| off
  group: ''
- name: Lateral distance from geometric centerline to center of mass, d
  summary: 从中心线到质心的距离 0（默认）| scalar
  group: ''
- name: Track width, w
  summary: 前、中、后轮距 [1.82,1.82,1.82]（默认）| vector
  group: ''
- name: Front axle tire corner stiffness, Cy_f
  summary: 前轮胎侧偏刚度 12e3 | scalar
  group: ''
- name: Middle axle tire corner stiffness, Cy_m
  summary: 中轮胎侧偏刚度 11e3 | scalar
  group: ''
- name: Rear axle tire corner stiffness, Cy_r
  summary: 后轮胎侧偏刚度 11e3 | scalar
  group: ''
- name: Front tire(s) relaxation length, sigma_f
  summary: 前轮胎松弛长度 .1（默认）| scalar
  group: ''
- name: Middle tire(s) relaxation length, sigma_m
  summary: 中轮胎松弛长度 .1（默认）| scalar
  group: ''
- name: Rear tire(s) relaxation length, sigma_r
  summary: 后轮胎松弛长度 .1（默认）| scalar
  group: ''
- name: Front axle slip angle breakpoints, alpha_f_brk
  summary: 断点 [-.1 .1]（默认）| vector
  group: ''
- name: Front axle tire corner data, Cy_f_data
  summary: 前轴轮胎侧偏数据 [-9e3 9e3]（默认）| vector
  group: ''
- name: Middle axle slip angle breakpoints, alpha_m_brk
  summary: 断点 [-.1 .1]（默认）| vector
  group: ''
- name: Middle axle tire corner data, Cy_m_data
  summary: 中轴轮胎侧偏数据 [-9e3 9e3]（默认）| vector
  group: ''
- name: Rear axle slip angle breakpoints, alpha_r_brk
  summary: 断点 [-.1 .1]（默认）| vector
  group: ''
- name: Rear axle tire corner data, Cy_r_data
  summary: 后轴轮胎侧偏数据 [-9e3 9e3]（默认）| vector
  group: ''
- name: Initial inertial frame lateral displacement, Y_o
  summary: 初始侧向位移 0（默认）| scalar
  group: ''
- name: Initial lateral velocity, ydot_o
  summary: 初始侧向速度 0（默认）| scalar
  group: ''
- name: Yaw polar inertia, Izz
  summary: 转动惯量 4000（默认）| scalar
  group: ''
- name: Initial yaw angle, psi_o
  summary: Psi 旋转 0（默认）| scalar
  group: ''
- name: Initial yaw rate, r_o
  summary: 横摆角速度 0（默认）| scalar
  group: ''
- name: Longitudinal drag area, Af
  summary: 有效车辆迎风面积 2（默认）| scalar
  group: ''
- name: Longitudinal drag coefficient, Cd
  summary: 空气阻力系数 .3（默认）| scalar
  group: ''
- name: Longitudinal lift coefficient, Cl
  summary: 空气升力系数 .1（默认）| scalar
  group: ''
- name: Longitudinal drag pitch moment, Cpm
  summary: 俯仰阻力 .1（默认）| scalar
  group: ''
- name: Relative wind angle vector, beta_w
  summary: 风角 [0:0.01:0.3]（默认）| vector
  group: ''
- name: Side force coefficient vector, Cs
  summary: 侧向力系数 [0:0.03:0.9]（默认）| vector
  group: ''
- name: 横摆力矩系数向量，Cym
  summary: 横摆力矩阻力 [0:0.01:0.3]（默认）| vector
  group: ''
- name: 绝对气压，Pabs
  summary: 压力 101325（默认）| scalar
  group: ''
- name: 空气温度，Tair
  summary: 温度 273（默认）| scalar
  group: ''
- name: 重力加速度，g
  summary: 重力 9.81（默认）| scalar
  group: ''
- name: 标称摩擦缩放因子，mu
  summary: 摩擦缩放因子 1（默认）| scalar
  group: ''
- name: 纵向速度容差，xdot_tol
  summary: 容差 .01（默认）| scalar
  group: ''
- name: 标称法向力，Fznom
  summary: 法向力 5000（默认）| scalar
  group: ''
- name: 距车轴平面的几何纵向偏移，longOff
  summary: 纵向偏移 0（默认）| scalar
  group: ''
- name: 距中心平面的几何横向偏移，latOff
  summary: 横向偏移 0（默认）| scalar
  group: ''
- name: 距车轴平面的几何垂直偏移，vertOff
  summary: 垂直偏移 0（默认）| scalar
  group: ''
- name: 包裹欧拉角，wrapAng
  summary: 将欧拉角包裹到区间 [-pi, pi] off（默认）| on
  group: ''
```

#### 选项

### **Vehicle track** — 车辆车轮数量 `Dual`（默认）| `Single (bicycle)`

使用 **Vehicle track** 参数指定车轮数量。

| 车辆轨迹设置 | 实现 |
| --- | --- |
| `Single (bicycle)` | - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual` | 力作用在车轴硬点位置。 |

### **Axle forces** — 车轴力类型 `External longitudinal velocity`（默认）| `External longitudinal forces` | `External forces`

使用 **Axle forces** 参数指定力的类型。

| 车轴力设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 该模块假设外部纵向速度处于准稳态，因此纵向加速度近似为零。 - 由于运动是准稳态的，该模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 当你需要执行以下操作时，请考虑此设置： - 生成虚拟传感器信号数据。 - 进行不受传动系统或非线性轮胎响应影响的高层软件研究。 |
| `External longitudinal forces` | - 该模块使用外部纵向力使车辆加速或制动。 - 该模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 当你需要执行以下操作时，请考虑此设置： - 考虑纵向速度变化对侧向和横摆运动的影响。 - 通过力而不是外部纵向速度来指定外部纵向运动。 - 将该模块连接到牵引执行器、车轮、制动器和挂钩。 |
| `External forces` | - 该模块使用外部侧向力和纵向力来使车辆转向、加速或制动。 - 该模块不使用转向输入来计算车辆运动。 - 当你需要具有更准确的非线性组合侧向和纵向滑移的轮胎模型时，请考虑此设置。 |

#### 输入信号

### **Front wheel steering** — `WhlAngF` 输入端口 `on`（默认）| `off`

选择以创建输入端口 `WhlAngF`。

### **Middle wheel steering** — `WhlAngM` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WhlAngM`。

### **Rear wheel steering** — `WhlAngR` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WhlAngR`。

### **External wind** — `WindXYZ` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WindXYZ`。

### **External friction** — `Mu` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `Mu`。

#### 依赖关系

要启用此参数，请将 **Axle forces** 设置为 `External longitudinal forces` 或 `External forces`。

### **External forces** — `FExt` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `FExt`。

### **External moments** — `MExt` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `MExt`。

### **Hitch forces** — `Fh` 输入端口 `on`（默认）| `off`

选择以创建输入端口 `Fh`。

### **Hitch moments** — `Mh` 输入端口 `on`（默认）| `off`

指定以创建输入端口 `Mh`。

### **Initial longitudinal position** — `X_o` 输入端口 `off`（默认）| `on`

指定以创建输入端口 `X_o`。

### **Initial yaw angle** — `psi_o` 输入端口 `off`（默认）| `on`

指定以创建输入端口 `psi_o`。

### **Initial longitudinal velocity** — `xdot_o` 输入端口 `off`（默认）| `on`

指定以创建输入端口 `xdot_o`。

#### 依赖关系

要启用此参数，请将 **Axle forces** 设置为 `External longitudinal forces` 或 `External forces`。

### **Initial yaw rate** — `r_o` 输入端口 `off`（默认）| `on`

指定以创建输入端口 `r_o`。

### **Initial lateral position** — `Y_o` 输入端口 `off`（默认）| `on`

指定以创建输入端口 `Y_o`。

### **Air temperature** — `AirTemp` 输入端口 `off`（默认）| `on`

指定以创建输入端口 `AirTemp`。

### **初始横向速度** — `ydot_o` 输入端口 `off`（默认）| `on`

指定是否创建输入端口 `ydot_o`。

#### 纵向

### **前轴车轮数，NF** — 前轮数量 `2`（默认）| `scalar`

前轴上的车轮数，
*NF*，无量纲。

### **中轴车轮数，NM** — 中轮数量 `2`（默认）| `scalar`

中轴上的车轮数，
*NM*，无量纲。

### **后轴车轮数，NR** — 后轮数量 `2`（默认）| `scalar`

后轴上的车轮数，
*NR*，无量纲。

### **车辆质量，m** — 车辆质量 `47000`（默认）| `scalar`

车辆质量，*m*，单位为 kg。

### **从质心到前轴的纵向距离，a** — 从质心到前轴的距离 `0.5`（默认）| `scalar`

从车辆质心到前轴的距离，*a*，单位为 m。

显示牵引车侧视图，其中标注了牵引座和各轴到质心的距离

### **从质心到中轴的纵向距离，b** — 从质心到中轴的距离 `4.5`（默认）| `scalar`

从车辆质心到中轴的距离，*b*，单位为 m。

显示牵引车侧视图，其中标注了牵引座和各轴到质心的距离

### **从质心到后轴的纵向距离，c** — 从质心到后轴的距离 `5.7`（默认）| `scalar`

从车辆质心到后轴的距离，*c*，单位为 m。

显示牵引车侧视图，其中标注了牵引座和各轴到质心的距离

### **从质心到车轴平面的垂直距离，h** — 从质心到车轴平面的距离 `0.3`（默认）| `scalar`

从车辆质心到车轴平面的垂直距离，*h*，单位为 m。

显示牵引车侧视图，其中标注了牵引座和各轴到质心的距离

### **从牵引座到车轴平面的垂直距离，hh** — 从牵引座到车轴平面的距离 `0.5`（默认）| `scalar`

从牵引座到车轴平面的垂直距离，*hh*，单位为 m。

显示牵引车侧视图，其中标注了牵引座和各轴到质心的距离

#### 依赖项

要启用此参数，请在 **Input signals**
窗格中，选择 **Hitch forces** 或 **Hitch
moments**。

### **从质心到牵引座的纵向距离，dh** — 从质心到牵引座的距离 `5`（默认）| `scalar`

从质心到牵引座的纵向距离，*dh*，
单位为 m。

显示牵引车侧视图，其中标注了牵引座和各轴到质心的距离

#### 依赖项

要启用此参数，请在 **Input signals**
窗格中，选择 **Hitch forces** 或 **Hitch
moments**。

### **初始惯性坐标系纵向位置，X\_o** — 初始纵向位移 `0`（默认）| `scalar`

车辆质心沿地球固定
*X* 轴的初始位移，单位为 m。

### **初始纵向速度，xdot\_o** — 初始纵向速度 `0`（默认）| `scalar`

车辆质心沿车辆固定
*x* 轴的初始速度，单位为 m/s。

#### 依赖项

要将此参数启用，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal
  forces`
- `External forces`

#### 横向

### **映射侧偏刚度** — 启用映射侧偏刚度 `off`（默认）| `on`

启用映射侧偏刚度计算。

#### 依赖项

要将此参数启用，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal
  velocity`
- `External longitudinal
  forces`

### **包含松弛长度动力学** — 启用松弛长度动力学 `on`（默认）| `off`

启用松弛长度动力学。

#### 依赖项

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Lateral distance from geometric centerline to center of mass, d** — 从中心线到质心的距离 `0`（默认）| `scalar`

从几何中心线到质心的横向距离，
*d*，单位为 m，沿车辆固定
*y* 轴方向。正值表示车辆
质心位于几何中心线右侧。负值表示
车辆质心位于几何中心线左侧。

轨道宽度和质心相对中心线偏移的俯视图

### **Track width, w** — 前、中、后轮距 `[1.82,1.82,1.82]`（默认）| `vector`

前、中、后轮距，分别为 *wf*、
*wm* 和 *wr*，单位为 m。
维度为 `1-by-3`。

轨道宽度和质心相对中心线偏移的俯视图

#### 依赖关系

要启用此参数，请将 **Vehicle track** 设置为
`Dual`。

### **Front axle tire corner stiffness, Cy\_f** — 前轮胎侧偏刚度 `12e3` | `scalar`

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

### **Middle axle tire corner stiffness, Cy\_m** — 中轮胎侧偏刚度 `11e3` | `scalar`

中轮胎侧偏刚度，
*Cym*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Rear axle tire corner stiffness, Cy\_r** — 后轮胎侧偏刚度 `11e3` | `scalar`

后轮胎侧偏刚度，
*Cyr*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **Front tire(s) relaxation length, sigma\_f** — 前轮胎松弛长度 `.1`（默认）| `scalar`

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

### **Middle tire(s) relaxation length, sigma\_m** — 中轮胎松弛长度 `.1`（默认）| `scalar`

中轮胎松弛长度，
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

### **Rear tire(s) relaxation length, sigma\_r** — 后轮胎松弛长度 `.1`（默认）| `scalar`

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

### **Front axle slip angle breakpoints, alpha\_f\_brk** — 断点 `[-.1 .1]`（默认）| `vector`

前轴侧偏角断点，
*αfbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Front axle tire corner data, Cy\_f\_data** — 前轴轮胎侧偏数据 `[-9e3 9e3]`（默认）| `vector`

前轴轮胎侧偏数据，
*Cyfdata*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Middle axle slip angle breakpoints, alpha\_m\_brk** — 断点 `[-.1 .1]`（默认）| `vector`

中轴侧偏角断点，
*αmbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Middle axle tire corner data, Cy\_m\_data** — 中轴轮胎侧偏数据 `[-9e3 9e3]`（默认）| `vector`

中轴轮胎侧偏数据，
*Cymdata*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Rear axle slip angle breakpoints, alpha\_r\_brk** — 断点 `[-.1 .1]`（默认）| `vector`

后轴侧偏角断点，
*αrbrk*，单位为 rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Rear axle tire corner data, Cy\_r\_data** — 后轴轮胎侧偏数据 `[-9e3 9e3]`（默认）| `vector`

后轴轮胎侧偏数据，
*Cyrdata*，单位为 N/rad。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **Initial inertial frame lateral displacement, Y\_o** — 初始侧向位移 `0`（默认）| `scalar`

车辆质心沿大地坐标系
*Y* 轴的初始位移，单位为 m。

### **Initial lateral velocity, ydot\_o** — 初始侧向速度 `0`（默认）| `scalar`

车辆质心沿车辆坐标系
*y* 轴的初始速度，单位为 m/s。

#### 横摆

### **Yaw polar inertia, Izz** — 转动惯量 `4000`（默认）| `scalar`

横摆极转动惯量，单位为 kg\*m^2。

### **Initial yaw angle, psi\_o** — Psi 旋转 `0`（默认）| `scalar`

车辆坐标系绕大地坐标系 *Z* 轴的旋转角
（横摆角），单位为 rad。

### **Initial yaw rate, r\_o** — 横摆角速度 `0`（默认）| `scalar`

车辆绕车辆坐标系 *z* 轴的角速度（横摆
角速度），单位为 rad/s。

#### 空气动力学

### **Longitudinal drag area, Af** — 有效车辆迎风面积 `2`（默认）| `scalar`

用于计算车辆空气阻力的有效车辆
迎风面积，
*Af*，单位为 m2。

### **Longitudinal drag coefficient, Cd** — 空气阻力系数 `.3`（默认）| `scalar`

空气阻力系数，*Cd*。该值为
无量纲量。

### **Longitudinal lift coefficient, Cl** — 空气升力系数 `.1`（默认）| `scalar`

空气升力系数，*Cl*。该值为
无量纲量。

### **Longitudinal drag pitch moment, Cpm** — 俯仰阻力 `.1`（默认）| `scalar`

纵向阻力俯仰力矩系数，
*Cpm*。该值为
无量纲量。

### **Relative wind angle vector, beta\_w** — 风角 `[0:0.01:0.3]`（默认）| `vector`

相对风角向量，*βw*，单位为
rad。

### **Side force coefficient vector, Cs** — 侧向力系数 `[0:0.03:0.9]`（默认）| `vector`

侧向力系数向量系数，
*Cs*。该值为无量纲量。

### **横摆力矩系数向量，Cym** — 横摆力矩阻力 `[0:0.01:0.3]`（默认）| `vector`

横摆力矩系数向量，*Cym*。该值无量纲。

#### 环境

### **绝对气压，Pabs** — 压力 `101325`（默认）| `scalar`

环境绝对压力，*Pabs*，单位为 Pa。

### **空气温度，Tair** — 温度 `273`（默认）| `scalar`

环境绝对温度，*T*，单位为 K。

#### 依赖关系

要启用此参数，请清除 **Air temperature**。

### **重力加速度，g** — 重力 `9.81`（默认）| `scalar`

重力加速度，*g*，单位为 m/s^2。

### **标称摩擦缩放因子，mu** — 摩擦缩放因子 `1`（默认）| `scalar`

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

### **纵向速度容差，xdot\_tol** — 容差 `.01`（默认）| `scalar`

纵向速度容差，单位为 m/s。

### **标称法向力，Fznom** — 法向力 `5000`（默认）| `scalar`

标称法向力，单位为 N。

#### 依赖关系

要启用此参数，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal velocity`
- `External longitudinal forces`

### **距车轴平面的几何纵向偏移，longOff** — 纵向偏移 `0`（默认）| `scalar`

车辆底盘沿车辆固定 *x* 轴距车轴平面的偏移，单位为 m。当您使用 3D 可视化引擎时，可考虑使用该偏移将底盘独立于车辆 CG 进行定位。

### **距中心平面的几何横向偏移，latOff** — 横向偏移 `0`（默认）| `scalar`

车辆底盘沿车辆固定 *y* 轴距中心平面的偏移，单位为 m。当您使用 3D 可视化引擎时，可考虑使用该偏移将底盘独立于车辆 CG 进行定位。

### **距车轴平面的几何垂直偏移，vertOff** — 垂直偏移 `0`（默认）| `scalar`

车辆底盘沿车辆固定 *z* 轴距车轴平面的偏移，单位为 m。当您使用 3D 可视化引擎时，可考虑使用该偏移将底盘独立于车辆 CG 进行定位。

### **包裹欧拉角，wrapAng** — 将欧拉角包裹到区间 `[-pi, pi]` `off`（默认）| `on`

将欧拉角包裹到区间 `[-pi, pi]`。对于可能经历超出此区间的车辆横摆旋转的车辆机动，如果您希望执行以下操作，请考虑清除该参数：

- 跟踪车辆总横摆旋转。
- 避免车辆状态估计器中出现不连续。
## 所属库

Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有纵向、横向和横摆运动的三轴车体

Vehicle Body 3DOF Three Axles 模块实现一个刚性三轴车体模型，用于计算纵向、横向和横摆运动。该模块考虑由车体质量加速度、空气阻力和转向引起的车轴和挂钩反作用力。

在车辆动力学和自动驾驶研究中，当车辆俯仰、侧倾和垂向运动不显著时，使用该模块对非完整车辆运动进行建模。

使用 **Vehicle track** 参数指定车轮数量。

| Vehicle Track 设置 | 实现 |
| --- | --- |
| `Single (bicycle)` | - 力沿车轴中心线作用。 - 无横向载荷转移。 |
| `Dual` | 力作用在车轴硬点位置。 |

使用 **Axle forces** 参数指定力的类型。

| Axle Forces 设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 该模块假设外部纵向速度处于准稳态，因此纵向加速度近似为零。 - 由于运动是准稳态的，该模块使用轮胎侧偏角和线性侧偏刚度计算横向力。 - 当你需要以下情况时，考虑此设置： - 生成虚拟传感器信号数据。 - 进行不受动力传动系统或非线性轮胎响应影响的高层级软件研究。 |
| `External longitudinal forces` | - 该模块使用外部纵向力使车辆加速或制动。 - 该模块使用轮胎侧偏角和线性侧偏刚度计算横向力。 - 当你需要以下情况时，考虑此设置： - 考虑纵向速度变化对横向和横摆运动的影响。 - 通过力而不是外部纵向速度来指定外部纵向运动。 - 将模块连接到牵引执行器、车轮、制动器和挂钩。 |
| `External forces` | - 该模块使用外部横向和纵向力来使车辆转向、加速或制动。 - 该模块不使用转向输入来计算车辆运动。 - 当你需要具有更准确非线性组合横向和纵向滑移的轮胎模型时，考虑此设置。 |

要创建额外的输入端口，请在 **Input signals** 下选择这些模块参数。

| 输入信号窗格参数 | 输入端口 | 描述 |
| --- | --- | --- |
| **前轮转向** | `WhlAngF` | 前轮转角，*δF* |
| **中轮转向** | `WhlAngM` | 中轮转角，*δM* |
| **后轮转向** | `WhlAngR` | 后轮转角，*δR* |
| **外部风** | `WindXYZ` | 惯性参考系中的风速，*WX*、*WY* 和 *WZ* |
| **外部摩擦** | `Mu` | 摩擦系数 |
| **外部力** | `FExt` | 车辆固定坐标系中作用在车辆重心（CG）上的外部力，*Fx*、*Fy* 和 *Fz* |
| **外部力矩** | `MExt` | 车辆固定坐标系中绕车辆重心的外部力矩，*Mx*、*My* 和 *Mz* |
| **前牵引力** | `FhF` | 车辆固定坐标系中施加在车身前牵引点处的牵引力，*FhFx*、*FhFy* 和 *FhFz* |
| **前牵引力矩** | `MhF` | 车辆固定坐标系中前牵引点处的牵引力矩，*MhFx*、*MhFy* 和 *MhFz* |
| **后牵引力** | `FhR` | 车辆固定坐标系中施加在车身后牵引点处的牵引力，*FhRx*、*FhRy* 和 *FhRz* |
| **后牵引力矩** | `MhR` | 车辆固定坐标系中后牵引点处的牵引力矩，*MhRx*、*MhRy* 和 *MhRz* |
| **初始纵向位置** | `X_o` | 车辆重心沿大地固定 *X* 轴的初始位移 |
| **初始横摆角** | `psi_o` | 车辆固定坐标系绕大地固定 *Z* 轴的初始旋转（横摆） |
| **初始纵向速度** | `xdot_o` | 车辆重心沿车辆固定 *x* 轴的初始速度 |
| **初始横摆角速度** | `r_o` | 车辆绕车辆固定 *z* 轴的初始角速度（横摆角速度） |
| **初始横向位置** | `Y_o` | 车辆重心沿大地固定 *Y* 轴的初始位移 |
| **空气温度** | `AirTemp` | 环境空气温度。如果希望在运行期间改变温度，请考虑此选项。 |
| **初始横向速度** | `ydot_o` | 车辆重心沿车辆固定 *y* 轴的初始速度 |

### 理论

为确定车辆运动，该模块求解刚体平面动力学运动方程。

| 计算 | 描述 |
| --- | --- |
| *动力学* | 该模块求解刚体平面动力学方程，以确定车辆纵向运动。如果将 **Axle forces** 设置为 `External longitudinal velocity`，则该模块对纵向加速度采用准稳态假设。 |
| *外力* | 外力包括阻力和外部力输入。这些力作用在车辆 CG 上。该模块将法向力除以标称法向载荷，以在重量和载荷转移期间改变有效摩擦参数。该模块保持俯仰和侧倾平衡。 |
| *轮胎力* | 该模块使用局部速度、纵向速度和侧向速度的比值来确定侧偏角。该模块使用转向角将轮胎力变换到车辆固定坐标系。如果将 **Axle forces** 设置为 `External forces`，则该模块假设外部提供的力位于车轴-车轮位置处的车辆固定坐标系中。 |

**单轨**

作用在单轨悬架位置处的垂向、纵向和侧向力的等轴测视图

**双轨**

作用在双轨悬架位置处的垂向、纵向和侧向力的等轴测视图

这些图示使用以下变量。

|  |  |
| --- | --- |
| *a*、*b*、*c* | 前轴、中轴和后轴分别距车辆 CG 在公共车轴平面上的法向投影点的纵向距离 |
| *h* | 车辆 CG 沿车辆固定 *z* 轴高于车轴平面的高度 |
| *d* | 沿车辆固定 *y* 轴从几何中心线到质心的侧向距离 |
| *hh* | 牵引装置沿车辆固定 *z* 轴高于车轴平面的高度 |
| *dh* | 牵引装置距车辆 CG 在公共车轴平面上的法向投影点的纵向距离 |
| *hl* | 沿车辆固定 *y* 轴从质心到牵引装置的侧向距离。 |
| *wf*、*wm*、*wr* | 前轮距、中轮距和后轮距 |

**阻力**

下表总结了该模块对阻力计算的实现。

| 计算 | 描述 |
| --- | --- |
| *坐标变换* | 该模块将风速从惯性坐标系变换到车辆固定坐标系。 |
| *阻力* | 为确定相对空速，该模块从 CG 车辆速度中减去风速。该模块使用相对空速确定阻力。 |
| *阻力矩* | 该模块使用相对空速确定阻力矩。 |

**侧偏刚度和松弛动力学**

要启用映射侧偏刚度和松弛长度动态参数，请将 **Axle forces** 设置为 `External longitudinal force` 或 `External longitudinal velocity`。

| 参数设置 | | 描述 |
| --- | --- | --- |
| Mapped Corner Stiffness | Include Relaxation Length Dynamics |
| `Off`（默认） | `On`（默认） | 该模块使用恒定侧偏刚度值。侧偏角包括松弛长度动态设置。松弛长度近似表示作为车轮行程函数的有效侧偏刚度力。 |
| `On` | `On`（默认） | 该模块使用作为侧偏刚度数据和侧偏角函数的查找表。侧偏角包括松弛长度动态设置。松弛长度近似表示作为车轮行程函数的有效侧偏刚度力。 |
| `Off`（默认） | `Off` | 该模块使用恒定侧偏刚度值。 |
