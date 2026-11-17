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
  summary: 后轮上的总力 scalar | array
  direction: input
- name: FExt
  summary: 车辆 CG 上的外力 array
  direction: input
- name: MExt
  summary: 绕车辆 CG 的外力矩 array
  direction: input
- name: FhF
  summary: 作用在车体上的前挂钩力 array
  direction: input
- name: MhF
  summary: 绕车体的前挂钩力矩 array
  direction: input
- name: FhR
  summary: 作用在车体上的后挂钩力 array
  direction: input
- name: MhR
  summary: 绕车体的后挂钩力矩 array
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
  summary: 初始横摆角 scalar
  direction: input
- name: r_o
  summary: 初始横摆角速度 scalar
  direction: input
- name: Info
  summary: 挂车数据总线
  direction: output
- name: xdot
  summary: 挂车纵向速度 scalar
  direction: output
- name: ydot
  summary: 挂车横向速度 scalar
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
- name: Fhz
  summary: 作用在车身上的牵引力的法向分量 scalar
  direction: output
```

### 输入

### **WhlAngF** — 前轮转向角 `scalar` | `array`

前轮转向角，
*δF*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single 1-axle`  `Single 2-axle`  `Single 3-axle` | *δF* | 标量 – `1` |
| `Dual 1-axle`  `Dual 2-axle`  `Dual 3-axle` | δF=[δflδfr]  or  [δflδfr] | 数组 – `[1x2]` 或 `[2x1]` |

#### 依赖

要启用此端口，请在 **Input signals** 下，
选择 **Front wheel steering**。

### **WhlAngM** — 中轮转向角 `scalar` | `array`

中轮转向角，
*δM*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single 3-axle` | *δM* | 标量 – `1` |
| `Dual 3-axle` | δM=[δmlδmr]  or  [δmlδmr] | 数组 – `[1x2]` 或 `[2x1]` |

#### 依赖

要启用此端口：

- 将 **Vehicle track** 设置为
  `Single 3-axle` 或
  `Dual 3-axle`。
- 要启用此端口，请在 **Input
  signals** 下，选择 **Middle wheel
  steering**。

### **WhlAngR** — 后轮转向角 `scalar` | `array`

后轮转向角，
*δR*，单位为 rad。

| **Vehicle Track** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `Single 1-axle`  `Single 2-axle`  `Single 3-axle` | *δR* | 标量 – `1` |
| `Dual 1-axle`  `Dual 2-axle`  `Dual 3-axle` | δR=[δrlδrr]  or  [δrlδrr] | 数组 – `[1x2]` 或 `[2x1]` |

#### 依赖

要启用此端口，请在 **Input signals** 下，
选择 **Rear wheel steering**。

### **xdotin** — 纵向速度 `scalar`

车辆 CG 沿车辆固定 *x* 轴的速度，
单位为 m/s。

#### 依赖

要启用此端口，请将 **Axle forces** 设置为
`External longitudinal
velocity`。

### **FwF** — 前轮上的总力 `scalar` | `array`

前轮上的力，
*FwF*，沿车辆固定
轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single 1-axle`  `Single 2-axle`  `Single 3-axle` | `External longitudinal forces` | 前轮上的纵向力 | FwF=Fxf | 标量 – `1` |
| `External forces` | 前轮上的纵向力和横向力 | FwF=[FxfFyf]  or [FxfFyf] | 数组 – `[1x2]` 或 `[2x1]` |
| `Dual 1-axle`  `Dual 2-axle`  `Dual 3-axle` | `External longitudinal forces` | 前轮上的纵向力 | FwF=[FxflFxfr] or [FxflFxfr] | 数组 – `[1x2]` 或 `[2x1]` |
| `External forces` | 前轮上的纵向力和横向力 | FwF=[FxflFyflFxfrFyfr] | 数组 – `[2x2]` |

#### 依赖

要启用此端口，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal forces`
- `External forces`

### **FwM** — 中轮上的总力 `scalar` | `array`

中轮上的力，
*FwM*，沿车辆固定
轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single 3-axle` | `External longitudinal forces` | 中轮上的纵向力 | FwM=Fxr | 标量 – `1` |
| `External forces` | 中轮上的纵向力和横向力 | FwM=[FxmFym]  or [FxmFym] | 数组 – `[1x2]` 或 `[2x1]` |
| `Dual 3-axle` | `External longitudinal forces` | 中轮上的纵向力 | FwM=[FxmlFxmr] or [FxmlFxmr] | 数组 – `[1x2]` 或 `[2x1]` |
| `External forces` | 中轮上的纵向力和横向力 | FwM=[FxmlFxmrFymlFymr] | 数组 – `[2x2]` |

#### 依赖

要启用此端口，请设置：

- **Vehicle track** 为
  `Single 3-axle` 或
  `Dual 3-axle`。
- **Axle forces** 为
  `External longitudinal
  forces` 或 `External
  forces`。

### **FwR** — 后轮上的总力 `scalar` | `array`

后轮上的力，
*FwR*，沿车辆固定
轴，单位为 N。

| **Vehicle Track** 设置 | **Axle Forces** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- | --- |
| `Single 2-axle`  `Single 3-axle` | `External longitudinal forces` | 后轮上的纵向力 | FwR=Fxr | 标量 – `1` |
| `External forces` | 后轮上的纵向力和横向力 | FwR=[FxrFyr]  or [FxrFyr] | 数组 – `[1x2]` 或 `[2x1]` |
| `Dual 2-axle`  `Dual 3-axle` | `External longitudinal forces` | 后轮上的纵向力 | FwR=[FxrlFxrr] or [FxrlFxrr] | 数组 – `[1x2]` 或 `[2x1]` |
| `External forces` | 后轮上的纵向力和横向力 | FwR=[FxrlFyrlFxrrFyrr] | 数组 – `[2x2]` |

#### 依赖关系

要启用此端口，请设置：

- **Vehicle track** 为
  `Single 3-axle`、
  `Single 2-axle`、
  `Dual 3-axle` 或
  `Dual 2-axle`。
- **Axle forces** 为
  `External longitudinal
  forces` 或 `External
  forces`。

### **FExt** — 车辆 CG 上的外力 `array`

施加到车辆 CG 上的外力，
*Fxext*、
*Fyext*、
*Fzext*，在
车辆固定坐标系中，单位为 N。信号向量维度为
`[1x3]` 或 `[3x1]`。

#### 依赖关系

要启用此端口，请在 **Input signals** 下，
选择 **External forces**。

### **MExt** — 绕车辆 CG 的外力矩 `array`

绕车辆 CG 的外力矩，
*Mx*、
*My*、
*Mz*，在
车辆固定坐标系中，单位为 N·m。信号向量维度为
`[1x3]` 或 `[3x1]`。

#### 依赖关系

要启用此端口，请在 **Input signals** 下，
选择 **External moments**。

### **FhF** — 作用在车体上的前挂钩力 `array`

施加到车体前挂钩位置的
挂钩力，
*FhFx*、
*FhFy*、
*FhFz*，在车辆固定坐标系中，单位为
N，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下，选择
**Front hitch forces**。

### **MhF** — 绕车体的前挂钩力矩 `array`

前挂钩位置处的
挂钩力矩，
*MhFx*、
*MhFy*、
*MhFz*，绕
车辆固定坐标系，单位为 N·m，指定为 `1-by-3` 或
`3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下，选择
**Front hitch moments**。

### **FhR** — 作用在车体上的后挂钩力 `array`

施加到车体后挂钩位置的
挂钩力，
*FhRx*、
*FhRy*、
*FhRz*，在车辆固定坐标系中，单位为
N，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下，选择
**Rear hitch forces**。

### **MhR** — 绕车体的后挂钩力矩 `array`

后挂钩位置处的
挂钩力矩，
*MhRx*、
*MhRy*、
*MhRz*，绕
车辆固定坐标系，单位为 N·m，指定为 `1-by-3` 或
`3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下，选择
**Rear hitch moments**。

### **WindXYZ** — 风速 `array`

风速，*Wx*、
*Wy*、
*Wz*，沿惯性
*X*、*Y* 和
*Z* 轴，单位为 m/s。信号向量维度
为 `1-by-3` 或 `3-by-1`。

#### 依赖关系

要启用此端口，请在 **Input signals** 下，
选择 **External wind**。

### **Mu** — 轮胎摩擦系数 `array`

轮胎摩擦系数，*μ*。该值
无量纲。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single 1-axle` | 车轮上的摩擦系数 | Mu=μf | 数组 – `[1x1]` |
| `Dual 1-axle` | 车轮上的摩擦系数 | Mu=[μflμfr] or [μflμfr] | 数组 – `[1x2]` 或 `[2x1]` |
| `Single 2-axle` | 车轮上的摩擦系数 | Mu=[μfμr] or [μfμr] | 数组 – `[1x2]` 或 `[2x1]` |
| `Dual 2-axle` | 车轮上的摩擦系数 | Mu=[μflμfrμrlμrr] | 数组 – `[2x2]` |
| `Single 3-axle` | 车轮上的摩擦系数 | Mu=[μfμmμr] or [μfμmμr] | 数组 – `[1x3]` 或 `[3x1]` |
| `Dual 3-axle` | 车轮上的摩擦系数 | Mu=[μflμfrμmlμmrμrlμrr] | 数组 – `[3x2]` |

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **External friction**。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，单位为 K。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Air temperature**。

### **X\_o** — 初始纵向位置 `scalar`

车辆质心沿大地坐标系 *X* 轴的初始位移，单位为 m。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Initial longitudinal position**。

### **Y\_o** — 初始横向位置 `scalar`

车辆质心沿大地坐标系 *Y* 轴的初始位移，单位为 m。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Initial lateral position**。

### **xdot\_o** — 初始纵向位置 `scalar`

车辆质心沿车辆坐标系 *x* 轴的初始速度，单位为 m/s。

#### 依赖关系

要启用此端口：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     forces`
   - `External
     forces`
2. 在 **Input signals** 下，选择 **Initial longitudinal
   velocity**

### **ydot\_o** — 初始横向位置 `scalar`

车辆质心沿车辆坐标系 *y* 轴的初始速度，单位为 m/s。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Initial lateral velocity**。

### **psi\_o** — 初始横摆角 `scalar`

车辆坐标系绕大地坐标系 *Z* 轴的旋转（横摆），单位为 rad。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Initial yaw angle**。

### **r\_o** — 初始横摆角速度 `scalar`

车辆绕车辆坐标系 *z* 轴的角速度（横摆角速度），单位为 rad/s。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Initial yaw rate**。
### 输出

### **Info** — 挂车数据总线

挂车数据，以总线信号形式返回，包含以下模块值。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆质心沿大地固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | | 车辆质心沿大地固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | | 车辆质心沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | | 车辆质心沿大地固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | | 车辆质心沿大地固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | | 车辆质心沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕大地固定 *X* 轴的旋转（横滚） | `0` | rad |
| `theta` | | | 车辆固定坐标系绕大地固定 *Y* 轴的旋转（俯仰） | `0` | rad |
| `psi` | | | 车辆固定坐标系绕大地固定 *Z* 轴的旋转（横摆） | 计算所得 | rad |
| `FrntAxl` | `Lft` | `Disp` | `X` | | 前左轮沿大地固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 前左轮沿大地固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 前左轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前左轮沿大地固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 前左轮沿大地固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 前左轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 前右轮沿大地固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 前右轮沿大地固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 前右轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 前右轮沿大地固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 前右轮沿大地固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 前右轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `MidlAxl` | `Lft` | `Disp` | `X` | | 中左轮沿大地固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 中左轮沿大地固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 中左轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 中左轮沿大地固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 中左轮沿大地固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 中左轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 中右轮沿大地固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 中右轮沿大地固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 中右轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 中右轮沿大地固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 中右轮沿大地固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 中右轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `RearAxl` | `Lft` | `Disp` | `X` | | 后左轮沿大地固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 后左轮沿大地固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 后左轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后左轮沿大地固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 后左轮沿大地固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 后左轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Rght` | `Disp` | `X` | | 后右轮沿大地固定 *X* 轴的位移 | 计算所得 | m |
| `Y` | | 后右轮沿大地固定 *Y* 轴的位移 | 计算所得 | m |
| `Z` | | 后右轮沿大地固定 *Z* 轴的位移 | `0` | m |
| `Vel` | `Xdot` | | 后右轮沿大地固定 *X* 轴的速度 | 计算所得 | m/s |
| `Ydot` | | 后右轮沿大地固定 *Y* 轴的速度 | 计算所得 | m/s |
| `Zdot` | | 后右轮沿大地固定 *Z* 轴的速度 | `0` | m/s |
| `Geom` | `Disp` | `X` | | | 挂车车身沿大地固定 *X* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Y` | | | 挂车车身沿大地固定 *Y* 轴相对于中心平面的偏移 | 计算所得 | m |
| `Z` | | | 挂车车身沿大地固定 *Z* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Vel` | `Xdot` | | | 挂车车身沿大地固定 *X* 轴的偏移速度 | 计算所得 | m/s |
| `Ydot` | | | 挂车车身沿大地固定 *Y* 轴的偏移速度 | 计算所得 | m/s |
| `Zdot` | | | 挂车车身沿大地固定 *Z* 轴的偏移速度 | 计算所得 | m/s |
| `HitchF` | `Disp` | `X` | | | 挂车前牵引座沿大地固定 *X* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Y` | | | 挂车前牵引座沿大地固定 *Y* 轴相对于中心平面的偏移 | 计算所得 | m |
| `Z` | | | 挂车前牵引座沿大地固定 *Z* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Vel` | `Xdot` | | | 挂车前牵引座沿大地固定 *X* 轴的偏移速度 | 计算所得 | m/s |
| `Ydot` | | | 挂车前牵引座沿大地固定 *Y* 轴的偏移速度 | 计算所得 | m/s |
| `Zdot` | | | 挂车前牵引座沿大地固定 *Z* 轴的偏移速度 | 计算所得 | m/s |
| `HitchR` | `Disp` | `X` | | | 挂车后牵引座沿大地固定 *X* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Y` | | | 挂车后牵引座沿大地固定 *Y* 轴相对于中心平面的偏移 | 计算所得 | m |
| `Z` | | | 挂车后牵引座沿大地固定 *Z* 轴相对于车轴平面的偏移 | 计算所得 | m |
| `Vel` | `Xdot` | | | 挂车后牵引座沿大地固定 *X* 轴的偏移速度 | 计算所得 | m/s |
| `Ydot` | | | 挂车后牵引座沿大地固定 *Y* 轴的偏移速度 | 计算所得 | m/s |
| `Zdot` | | | 挂车后牵引座沿大地固定 *Z* 轴的偏移速度 | 计算所得 | m/s |
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
| `Forces` | `Body` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的合力 | 计算所得 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴所受的合力 | 计算所得 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴所受的合力 | `0` | N |
| `Ext` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的外力 | 计算所得 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴所受的外力 | 计算所得 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴所受的外力 | `0` | N |
| `HitchF` | `Fx` | | | 在牵引座位置施加于车身的前牵引座力沿车辆固定 *x* 轴的分量 | 计算所得 | N |
| `Fy` | | | 在牵引座位置施加于车身的前牵引座力沿车辆固定 *y* 轴的分量 | 计算所得 | N |
| `Fz` | | | 在牵引座位置施加于车身的前牵引座力沿车辆固定 *z* 轴的分量 | 计算所得 | N |
| `HitchR` | `Fx` | | | 在牵引座位置施加于车身的后牵引座力沿车辆固定 *x* 轴的分量 | 计算所得 | N |
| `Fy` | | | 在牵引座位置施加于车身的后牵引座力沿车辆固定 *y* 轴的分量 | 计算所得 | N |
| `Fz` | | | 在牵引座位置施加于车身的后牵引座力沿车辆固定 *z* 轴的分量 | 计算所得 | N |
| `FrntAxl` | `Lft` | `Fx` | | 前左轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 前左轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 前左轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Rght` | `Fx` | | 前右轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 前右轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 前右轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `MidlAxl` | `Lft` | `Fx` | | 中左轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 中左轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 中左轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
| `Rght` | `Fx` | | 中右轮沿车辆固定 *x* 轴的纵向力 | 计算所得 | N |
| `Fy` | | 中右轮沿车辆固定 *y* 轴的侧向力 | 计算所得 | N |
| `Fz` | | 中右轮沿车辆固定 *z* 轴的法向力 | 计算所得 | N |
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
| `Drag` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的阻力 | 计算所得 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴所受的阻力 | 计算所得 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴所受的阻力 | 计算所得 | N |
| `Grvty` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的重力 | 计算所得 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴所受的重力 | 计算所得 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴所受的重力 | 计算所得 | N |
| `Moments` | `Body` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴所受的车身力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴所受的车身力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴所受的车身力矩 | `0` | N·m |
| `Drag` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴所受的阻力力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴所受的阻力力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴所受的阻力力矩 | `0` | N·m |
| `Ext` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴所受的外力矩 | `0` | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴所受的外力矩 | 计算所得 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴所受的外力矩 | `0` | N·m |
| `HitchF` | `Mx` | | | 前牵引座位置处绕车辆固定 *x* 轴的牵引座力矩 | `0` | N·m |
| `My` | | | 前牵引座位置处绕车辆固定 *y* 轴的牵引座力矩 | 计算所得 | N·m |
| `Mz` | | | 前牵引座位置处绕车辆固定 *z* 轴的牵引座力矩 | `0` | N·m |
| `HitchR` | `Mx` | | | 后牵引座位置处绕车辆固定 *x* 轴的牵引座力矩 | `0` | N·m |
| `My` | | | 后牵引座位置处绕车辆固定 *y* 轴的牵引座力矩 | 计算所得 | N·m |
| `Mz` | | | 后牵引座位置处绕车辆固定 *z* 轴的牵引座力矩 | `0` | N·m |
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
| `HitchF` | `Disp` | | `x` | | 前牵引座沿车辆固定 *x* 轴相对于车轴平面的偏移 | 输入 | m |
| `y` | | 前牵引座沿车辆固定 *y* 轴相对于中心平面的偏移 | 输入 | m |
| `z` | | 前牵引座沿大地固定 *z* 轴相对于车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 前牵引座沿车辆固定 *x* 轴的偏移速度 | 计算所得 | m/s |
| `ydot` | | 前牵引座沿车辆固定 *y* 轴的偏移速度 | 计算所得 | m/s |
| `zdot` | | 前牵引座沿车辆固定 *z* 轴的偏移速度 | `0` | m/s |
| `HitchR` | `Disp` | | `x` | | 后牵引座沿车辆固定 *x* 轴相对于车轴平面的偏移 | 输入 | m |
| `y` | | 后牵引座沿车辆固定 *y* 轴相对于中心平面的偏移 | 输入 | m |
| `z` | | 后牵引座沿大地固定 *z* 轴相对于车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 后牵引座沿车辆固定 *x* 轴的偏移速度 | 计算所得 | m/s |
| `ydot` | | 后牵引座沿车辆固定 *y* 轴的偏移速度 | 计算所得 | m/s |
| `zdot` | | 后牵引座沿车辆固定 *z* 轴的偏移速度 | `0` | m/s |
| `Pwr` | `Ext` | | | | 施加的外部功率 | 计算所得 | W |
| `HitchF` | | | | 前牵引座功率 | 计算所得 | W |
| `HitchR` | | | | 后牵引座功率 | 计算所得 | W |
| `Drag` | | | | 阻力导致的功率损失 | 计算所得 | W |
| `Geom` | `Disp` | | `x` | | 挂车沿车辆固定 *x* 轴相对于车轴平面的偏移 | 输入 | m |
| `y` | | 挂车沿车辆固定 *y* 轴相对于中心平面的偏移 | 输入 | m |
| `z` | | 挂车沿车辆固定 *z* 轴相对于车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 挂车沿车辆固定 *x* 轴的偏移速度 | 计算所得 | m/s |
| `ydot` | | 挂车沿车辆固定 *y* 轴的偏移速度 | 计算所得 | m/s |
| `zdot` | | 挂车沿车辆固定 *z* 轴的偏移速度 | `0` | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | 计算所得 | rad |

| 信号 | | | 描述 | | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | 外部施加的纵向力功率 | | 计算值 | W |
| `PwrFyExt` | 外部施加的横向力功率 | | 计算值 | W |
| `PwrMzExt` | 外部施加的横摆力矩功率 | | 计算值 | W |
| `PwrFwFLx` | 施加在前左轴上的纵向力功率 | | 计算值 | W |
| `PwrFwFLy` | 施加在前左轴上的横向力功率 | | 计算值 | W |
| `PwrFwFRx` | 施加在前右轴上的纵向力功率 | | 计算值 | W |
| `PwrFwFRy` | 施加在前右轴上的横向力功率 | | 计算值 | W |
| `PwrFwMLx` | 施加在中左轴上的纵向力功率 | | 计算值 | W |
| `PwrFwMLy` | 施加在中左轴上的横向力功率 | | 计算值 | W |
| `PwrFwMRx` | 施加在中右轴上的纵向力功率 | | 计算值 | W |
| `PwrFwMRy` | 施加在中右轴上的横向力功率 | | 计算值 | W |
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
| `PwrStoredr` | 横摆转动动能变化率 | | 计算值 | W |

### **xdot** — 挂车纵向速度 `scalar`

挂车质心沿车辆固定 *x* 轴的速度，单位为 m/s。

### **ydot** — 挂车横向速度 `scalar`

挂车质心沿车辆固定 *y* 轴的速度，单位为 m/s。

### **psi** — 横摆 `scalar`

车辆固定坐标系绕地面固定 *Z* 轴的旋转（横摆），单位为 rad。

### **r** — 横摆角速度 `scalar`

车辆绕车辆固定 *z* 轴的角速度 *r*（横摆角速度），单位为 rad/s。

### **FzF** — 前轮法向力 `scalar` | `array`

前轮沿车辆固定 *z* 轴的法向力 *FzF*，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single 2-axle`  `Single 3-axle` | 前轴法向力 | FzF=Fzf | 标量 – `1` |
| `Dual 2-axle`  `Dual 3-axle` | 前轮法向力 | FzF=[FzflFzfr] | 数组 – `[1x2]` |

### **FzM** — 中轮法向力 `scalar` | `array`

中轮沿车辆固定 *z* 轴的法向力 *FzM*，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single 3-axle` | 中轴法向力 | FzM=Fzm | 标量 – `1` |
| `Dual 3-axle` | 左、右中轮法向力 | FzM=[FzmlFzrl] | 数组 – `[1x2]` |

#### 依赖关系

要启用此端口，请将 **Vehicle track** 设置为 `Single 3-axle` 或 `Dual 3-axle`。

### **FzR** — 后轮法向力 `scalar` | `array`

后轮沿车辆固定 *z* 轴的法向力 *FzR*，单位为 N。

| **Vehicle Track** 设置 | 描述 | 变量 | 信号维度 |
| --- | --- | --- | --- |
| `Single 2-axle`  `Single 3-axle` | 后轮法向力 | FzR=Fzr | 标量 – `1` |
| `Dual 2-axle`  `Dual 3-axle` | 后轮法向力 | FzR=[FzrlFzrr] | 数组 – `[1x2]` |

### **Fhz** — 作用在车身上的牵引力的法向分量 `scalar`

在牵引点处施加到车身上的法向牵引力，
*Fhz*，在
车辆固定坐标系 *z* 轴方向，单位为 N。

如果启用 **Hitch forces** 参数，该
模块将法向牵引力
*Fhz* 与 *Fh* 输入端口沿车辆固定
*z* 轴的分量值进行偏置。
## 参数
```yaml
parameters:
- name: Vehicle track
  summary: 车辆轨迹类型 Dual 2-axle（默认）| Single 1-axle | Dual 1-axle | Single 2-axle | Dual 3-axle
  group: ''
- name: Axle forces
  summary: 车轴力类型 External forces（默认）| External longitudinal velocity | External longitudinal forces
  group: ''
- name: Front wheel steering
  summary: WhlAngF 输入端口 off（默认）| on
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
- name: Front hitch forces
  summary: FhF 输入端口 on（默认）| off
  group: ''
- name: Front hitch moments
  summary: MhF 输入端口 on（默认）| off
  group: ''
- name: Rear hitch forces
  summary: FhR 输入端口 off（默认）| on
  group: ''
- name: Rear hitch moments
  summary: MhR 输入端口 off（默认）| on
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
- name: Initial lateral velocity
  summary: ydot_o 输入端口 off（默认）| on
  group: ''
- name: Number of wheels on front axle, NF
  summary: 前轮数量 2（默认）| scalar
  group: ''
- name: Number of wheels on middle axle, NM
  summary: 中轮数量 2（默认）| scalar
  group: ''
- name: Number of wheels on rear axle, NR
  summary: 后轮数量 2（默认）| scalar
  group: ''
- name: Vehicle mass, m
  summary: 车辆质量 26000（默认）| scalar
  group: ''
- name: Longitudinal distance from center of mass to front axle, a
  summary: 从质心到前轴的距离 4（默认）| scalar
  group: ''
- name: Longitudinal distance from center of mass to middle axle, b
  summary: 从质心到中轴的距离 4.5（默认）| scalar
  group: ''
- name: Longitudinal distance from center of mass to rear axle, c
  summary: 从质心到后轴的距离 5（默认）| scalar
  group: ''
- name: Vertical distance from center of mass to axle plane, h
  summary: 从质心到车轴平面的距离 2（默认）| scalar
  group: ''
- name: 从质心到前挂钩的纵向距离，dh_f
  summary: 到前挂钩的距离 7.5（默认）| scalar
  group: ''
- name: 从前挂钩到车轴平面的垂直距离，hh_f
  summary: 从前挂钩到车轴平面的距离 0.6（默认）| scalar
  group: ''
- name: 从质心到后挂钩的纵向距离，dh_r
  summary: 到前挂钩的距离 7.5（默认）| scalar
  group: ''
- name: 从前挂钩到车轴平面的垂直距离，hh_r
  summary: 从后挂钩到车轴平面的距离 0.6（默认）| scalar
  group: ''
- name: 初始惯性坐标系纵向位置，X_o
  summary: 初始惯性 X 位置 0（默认）| scalar
  group: ''
- name: 初始纵向速度，xdot_o
  summary: 初始速度 0（默认）| scalar
  group: ''
- name: 映射侧偏刚度
  summary: 选择 off（默认）| on
  group: ''
- name: 包含松弛长度动力学
  summary: 启用松弛长度动力学 on（默认）| off
  group: ''
- name: 从几何中心线到质心的横向距离，d
  summary: 从中心线到质心的距离 0（默认）| scalar
  group: ''
- name: 从几何中心线到前挂钩的横向距离，hl_f
  summary: 从中心线到前挂钩的距离 0（默认）| scalar
  group: ''
- name: 从几何中心线到后牵引装置的距离，hl_r
  summary: 从中心线到后牵引装置的距离 0（默认）| scalar
  group: ''
- name: 前轮距，w_f
  summary: 前轮距 1.82（默认）| scalar
  group: ''
- name: 中轮距，w_m
  summary: 中轮距 1.82（默认）| scalar
  group: ''
- name: 后轮距，w_r
  summary: 后轮距 1.82（默认）| scalar
  group: ''
- name: 前轴轮胎侧偏刚度，Cy_f
  summary: 前轴轮胎刚度 12.3（默认）| scalar
  group: ''
- name: 中轴轮胎侧偏刚度，Cy_m
  summary: 中轴轮胎刚度 11.3（默认）| scalar
  group: ''
- name: 后轴轮胎侧偏刚度，Cy_r
  summary: 后轴轮胎刚度 11.3（默认）| scalar
  group: ''
- name: 前轮胎松弛长度，sigma_f
  summary: 松弛长度 .1（默认）| scalar
  group: ''
- name: 中轮胎松弛长度，sigma_m
  summary: 松弛长度 .1（默认）| scalar
  group: ''
- name: 后轮胎松弛长度，sigma_r
  summary: 松弛长度 .1（默认）| scalar
  group: ''
- name: 前轴侧偏角断点，alpha_f_brk
  summary: 断点 [-.1 .1]（默认）| vector
  group: ''
- name: 前轴侧偏数据，Cy_f_data
  summary: 断点 [-9e3 9e3]（默认）| vector
  group: ''
- name: 中轴侧偏角断点，alpha_m_brk
  summary: 断点 [-.1 .1]（默认）| vector
  group: ''
- name: 中轴侧偏数据，Cy_m_data
  summary: 断点 [-9e3 9e3]（默认）| vector
  group: ''
- name: 后轴侧偏角断点，alpha_r_brk
  summary: 断点 [-.1 .1]（默认）| vector
  group: ''
- name: 后轴侧偏数据，Cy_r_data
  summary: 数据 [-9e3 9e3]（默认）| vector
  group: ''
- name: 初始惯性坐标系横向位移，Y_o
  summary: 位置 0（默认）| scalar
  group: ''
- name: 初始横向速度，ydot_o
  summary: 速度 0（默认）| scalar
  group: ''
- name: 横摆极惯性，Izz
  summary: 惯性 4000（默认）| scalar
  group: ''
- name: 初始横摆角，psi_o
  summary: Psi 旋转 0（默认）| scalar
  group: ''
- name: 初始横摆角速度，r_o
  summary: 横摆角速度 0（默认）| scalar
  group: ''
- name: 纵向阻力面积，Af
  summary: 有效车辆迎风面积 2（默认）| scalar
  group: ''
- name: 纵向阻力系数，Cd
  summary: 空气阻力系数 .3（默认）| scalar
  group: ''
- name: 纵向升力系数，Cl
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
- name: Yaw moment coefficient vector, Cym
  summary: 横摆力矩阻力 [0:0.01:0.3]（默认）| vector
  group: ''
- name: Absolute air pressure, Pabs
  summary: 压力 101325（默认）| scalar
  group: ''
- name: Air temperature, Tair
  summary: 温度 273（默认）| scalar
  group: ''
- name: Gravitational acceleration, g
  summary: 重力 9.81（默认）| scalar
  group: ''
- name: Nominal friction scaling factor, mu
  summary: 摩擦比例因子 1（默认）| scalar
  group: ''
- name: Longitudinal velocity tolerance, xdot_tol
  summary: 容差 .01（默认）| scalar
  group: ''
- name: Nominal normal force, Fznom
  summary: 法向力 5000（默认）| scalar
  group: ''
- name: Geometric longitudinal offset from axle plane, longOff
  summary: 纵向偏移 0（默认）| scalar
  group: ''
- name: Geometric lateral offset from center plane, latOff
  summary: 侧向偏移 0（默认）| scalar
  group: ''
- name: Geometric vertical offset from axle plane, vertOff
  summary: 垂直偏移 0（默认）| scalar
  group: ''
- name: Wrap Euler angles, wrapAng
  summary: 将欧拉角包裹到区间 [-pi, pi] off（默认）| on
  group: ''
```

#### 选项

### **Vehicle track** — 车辆轨迹类型 `Dual 2-axle`（默认）| `Single 1-axle` | `Dual 1-axle` | `Single 2-axle` | `Dual 3-axle`

使用 **Vehicle track** 参数指定车轮数量。

| 车辆轨迹设置 | 实现 |
| --- | --- |
| `Single 1-axle` | 单轨迹单轴挂车。  - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual 1-axle` | 双轨迹单轴挂车。力作用在车轴硬点位置。 |
| `Single 2-axle` | 单轨迹双轴挂车。  - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual 2-axle`（默认） | 双轨迹双轴挂车。力作用在车轴硬点位置。 |
| `Single 3-axle` | 单轨迹三轴挂车。  - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual 3-axle` | 双轨迹三轴挂车。力作用在车轴硬点位置。 |

### **Axle forces** — 车轴力类型 `External forces`（默认）| `External longitudinal velocity` | `External longitudinal forces`

使用 **Axle forces** 参数指定力的类型。

| 车轴力设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 该模块假设外部纵向速度处于准稳态，且纵向加速度近似为零。 - 由于运动为准稳态，该模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 在以下情况下考虑此设置：  - 生成虚拟传感器信号数据。   - 进行不受传动系统或非线性轮胎响应影响的高层级软件研究。 |
| `External longitudinal forces` | - 该模块使用外部纵向力使车辆加速或制动。 - 该模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 在以下情况下考虑此设置：  - 考虑纵向速度变化对侧向和横摆运动的影响。   - 通过力而非外部纵向速度来指定外部纵向运动。   - 将该模块连接到牵引执行器、车轮、制动器和牵引装置。 |
| `External forces` | - 该模块使用外部侧向和纵向力来转向、加速或制动车辆。 - 该模块不使用转向输入来计算车辆运动。 - 当您需要具有更精确非线性组合侧向和纵向滑移的轮胎模型时，考虑此设置。 |

#### 输入信号

### **Front wheel steering** — `WhlAngF` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WhlAngF`。

### **Middle wheel steering** — `WhlAngM` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WhlAngM`。

#### 依赖关系

要启用此参数，请将 **Vehicle track** 设置为
`Single 3-axle` 或 `Dual
3-axle`。

### **Rear wheel steering** — `WhlAngR` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `WhlAngR`。

#### 依赖关系

要启用此参数，请将 **Vehicle track** 设置为
`Single 2-axle`、`Dual
2-axle`、`Single 3-axle` 或
`Dual 3-axle`。

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

要启用此参数，请将 **Axle forces** 设置为
`External longitudinal forces` 或
`External forces`。

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

前轴上的车轮数量，
*NF*。该值无量纲。

### **Number of wheels on middle axle, NM** — 中轮数量 `2`（默认）| `scalar`

中轴上的车轮数量，
*NM*。该值无量纲。

#### 依赖项

要启用此参数，请将 **Vehicle track** 设置为
`Single 3-axle` 或 `Dual
3-axle`。

### **Number of wheels on rear axle, NR** — 后轮数量 `2`（默认）| `scalar`

后轴上的车轮数量，
*NR*。该值无量纲。

要启用此参数，请将 **Vehicle track** 设置为
`Single 2-axle`、`Single
3-axle`、`Dual 2-axle` 或
`Dual 3-axle`。

### **Vehicle mass, m** — 车辆质量 `26000`（默认）| `scalar`

车辆质量，*m*，单位为 kg。

### **Longitudinal distance from center of mass to front axle, a** — 从质心到前轴的距离 `4`（默认）| `scalar`

从车辆质心到前轴的距离，*a*，单位为 m。

挂车侧视图，显示从质心到车轴的纵向距离和挂钩距离

### **Longitudinal distance from center of mass to middle axle, b** — 从质心到中轴的距离 `4.5`（默认）| `scalar`

从车辆质心到中轴的距离，*b*，单位为 m。

挂车侧视图，显示从质心到车轴的纵向距离和挂钩距离

#### 依赖项

要启用此参数，请将 **Vehicle track** 设置为
`Single 3-axle` 或 `Dual
3-axle`。

### **Longitudinal distance from center of mass to rear axle, c** — 从质心到后轴的距离 `5`（默认）| `scalar`

从车辆质心到前轴的距离，*c*，单位为 m。

挂车侧视图，显示从质心到车轴的纵向距离和挂钩距离

#### 依赖项

要启用此参数，请将 **Vehicle track** 设置为
`Single 2-axle`、`Single
3-axle`、`Single 3-axle` 或
`Dual 3-axle`。

### **Vertical distance from center of mass to axle plane, h** — 从质心到车轴平面的距离 `2`（默认）| `scalar`

从车辆质心到车轴平面的垂直距离，*h*，
单位为 m。

挂车侧视图，显示从质心到车轴的纵向距离和挂钩距离

### **从质心到前挂钩的纵向距离，dh\_f** — 到前挂钩的距离 `7.5`（默认）| `scalar`

从质心到前挂钩的纵向距离，
*dh\_f*，单位为 m。

显示纵向车轴和挂钩到质心距离的挂车侧视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Front hitch forces** 或 **Front hitch
moments**。

### **从前挂钩到车轴平面的垂直距离，hh\_f** — 从前挂钩到车轴平面的距离 `0.6`（默认）| `scalar`

从前挂钩到车轴平面的垂直距离，
*hh\_f*，单位为 m。

显示纵向车轴和挂钩到质心距离的挂车侧视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Front hitch forces** 或 **Front hitch
moments**。

### **从质心到后挂钩的纵向距离，dh\_r** — 到前挂钩的距离 `7.5`（默认）| `scalar`

从质心到后挂钩的纵向距离，
*dh\_r*，单位为 m。

显示纵向车轴和挂钩到质心距离的挂车侧视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Rear hitch forces** 或 **Rear hitch
moments**。

### **从前挂钩到车轴平面的垂直距离，hh\_r** — 从后挂钩到车轴平面的距离 `0.6`（默认）| `scalar`

从后挂钩到车轴平面的垂直距离，
*hh\_r*，单位为 m。

显示纵向车轴和挂钩到质心距离的挂车侧视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Rear hitch forces** 或 **Rear hitch
moments**。

### **初始惯性坐标系纵向位置，X\_o** — 初始惯性 X 位置 `0`（默认）| `scalar`

车辆质心沿地球固定
*X* 轴的初始位移，单位为 m。

### **初始纵向速度，xdot\_o** — 初始速度 `0`（默认）| `scalar`

车辆质心沿车辆固定
*x* 轴的初始速度，单位为 m/s。

#### 依赖关系

要启用此参数，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal
  forces`
- `External forces`

#### 横向

### **映射侧偏刚度** — 选择 `off`（默认）| `on`

启用映射侧偏刚度计算。

#### 依赖关系

要启用此参数，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal
  velocity`
- `External longitudinal
  forces`

### **包含松弛长度动力学** — 启用松弛长度动力学 `on`（默认）| `off`

启用松弛长度动力学。

#### 依赖关系

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. 清除 **Mapped corner stiffness**。

### **从几何中心线到质心的横向距离，d** — 从中心线到质心的距离 `0`（默认）| `scalar`

从几何中心线到质心的横向距离，
*d*，单位为 m，沿车辆固定
*y* 方向。正值表示挂车质心位于几何中心线右侧。负值表示
挂车质心位于几何中心线左侧。

显示轮距和质心偏离中心线的俯视图

### **从几何中心线到前挂钩的横向距离，hl\_f** — 从中心线到前挂钩的距离 `0`（默认）| `scalar`

从几何中心线到前挂钩的横向距离，
*hl\_f*，单位为 m，沿车辆固定 *y* 方向。
正值表示挂车挂钩位于几何中心线右侧。负值表示挂车挂钩位于几何
中心线左侧。

显示车轴宽度和质心偏离中心线的俯视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Front hitch forces** 或 **Front hitch
moments**。

### **从几何中心线到后牵引装置的距离，hl\_r** — 从中心线到后牵引装置的距离 `0`（默认）| `scalar`

从几何中心线到后牵引装置的横向距离，
*hl\_r*，单位为 m，沿车辆固定的 *y* 方向。
正值表示牵引装置位于几何中心线右侧。
负值表示牵引装置位于几何中心线左侧。

轴距宽度和质心相对中心线偏移的俯视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Rear hitch forces** 或 **Rear hitch
moments**。

### **前轮距，w\_f** — 前轮距 `1.82`（默认）| `scalar`

前轮距，*wf*，单位为 m。

轮距和质心相对中心线偏移的俯视图

#### 依赖关系

要启用此参数，请将 **Vehicle track** 设置为
`Dual 2-axle`、`Dual
2-axle` 或 `Dual
3-axle`。

### **中轮距，w\_m** — 中轮距 `1.82`（默认）| `scalar`

中轮距，*wm*，单位为 m。

轮距和质心相对中心线偏移的俯视图

#### 依赖关系

要启用此参数，请将 **Vehicle track** 设置为
`Dual 3-axle`。

### **后轮距，w\_r** — 后轮距 `1.82`（默认）| `scalar`

后轮距，*wr*，单位为 m。

轮距和质心相对中心线偏移的俯视图

#### 依赖关系

要启用此参数，请将 **Vehicle track** 设置为
`Dual 2-axle` 或 `Dual
3-axle`。

### **前轴轮胎侧偏刚度，Cy\_f** — 前轴轮胎刚度 `12.3`（默认）| `scalar`

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

### **中轴轮胎侧偏刚度，Cy\_m** — 中轴轮胎刚度 `11.3`（默认）| `scalar`

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

### **后轴轮胎侧偏刚度，Cy\_r** — 后轴轮胎刚度 `11.3`（默认）| `scalar`

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

### **前轮胎松弛长度，sigma\_f** — 松弛长度 `.1`（默认）| `scalar`

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

### **中轮胎松弛长度，sigma\_m** — 松弛长度 `.1`（默认）| `scalar`

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

### **后轮胎松弛长度，sigma\_r** — 松弛长度 `.1`（默认）| `scalar`

后轮胎松弛长度，*σr*，
单位为 m。

#### 依赖

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

### **前轴侧偏角断点，alpha\_f\_brk** — 断点 `[-.1 .1]`（默认）| `vector`

前轴侧偏角断点，
*αfbrk*，单位为 rad。

#### 依赖

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **前轴侧偏数据，Cy\_f\_data** — 断点 `[-9e3 9e3]`（默认）| `vector`

前轴侧偏数据，*Cyfdata*，
单位为 N/rad。

#### 依赖

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **中轴侧偏角断点，alpha\_m\_brk** — 断点 `[-.1 .1]`（默认）| `vector`

中轴侧偏角断点，
*αmbrk*，单位为 rad。

#### 依赖

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **中轴侧偏数据，Cy\_m\_data** — 断点 `[-9e3 9e3]`（默认）| `vector`

中轴侧偏数据，
*Cymdata*，单位为 N/rad。

#### 依赖

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **后轴侧偏角断点，alpha\_r\_brk** — 断点 `[-.1 .1]`（默认）| `vector`

后轴侧偏角断点，
*αrbrk*，单位为 rad。

#### 依赖

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **后轴侧偏数据，Cy\_r\_data** — 数据 `[-9e3 9e3]`（默认）| `vector`

后轴侧偏数据，*Cyrdata*，
单位为 N/rad。

#### 依赖

要启用此参数：

1. 将 **Axle forces** 设置为以下选项之一：

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. 选择 **Mapped corner stiffness**。

### **初始惯性坐标系横向位移，Y\_o** — 位置 `0`（默认）| `scalar`

车辆质心沿地球固定
*Y* 轴的初始位移，单位为 m。

### **初始横向速度，ydot\_o** — 速度 `0`（默认）| `scalar`

车辆质心沿车辆固定
*y* 轴的初始速度，单位为 m/s。

#### 横摆

### **横摆极惯性，Izz** — 惯性 `4000`（默认）| `scalar`

横摆极惯性，单位为 kg\*m^2。

### **初始横摆角，psi\_o** — Psi 旋转 `0`（默认）| `scalar`

车辆固定坐标系绕地球固定 *Z* 轴的旋转
（横摆），单位为 rad。

### **初始横摆角速度，r\_o** — 横摆角速度 `0`（默认）| `scalar`

车辆绕车辆固定 *z* 轴的角速度（横摆
角速度），单位为 rad/s。

#### 空气动力学

### **纵向阻力面积，Af** — 有效车辆迎风面积 `2`（默认）| `scalar`

有效车辆迎风面积，
*Af*，用于计算作用在车辆上的空气阻力
力，单位为 m2。

### **纵向阻力系数，Cd** — 空气阻力系数 `.3`（默认）| `scalar`

空气阻力系数，*Cd*。该值
无量纲。

### **纵向升力系数，Cl** — 空气升力系数 `.1`（默认）| `scalar`

空气升力系数，*Cl*。该值
无量纲。

### **Longitudinal drag pitch moment, Cpm** — 俯仰阻力 `.1`（默认）| `scalar`

纵向阻力俯仰力矩系数，
*Cpm*。该值无量纲。

### **Relative wind angle vector, beta\_w** — 风角 `[0:0.01:0.3]`（默认）| `vector`

相对风角向量，*βw*，单位为
rad。

### **Side force coefficient vector, Cs** — 侧向力系数 `[0:0.03:0.9]`（默认）| `vector`

侧向力系数向量系数，
*Cs*。该值无量纲。

### **Yaw moment coefficient vector, Cym** — 横摆力矩阻力 `[0:0.01:0.3]`（默认）| `vector`

横摆力矩系数向量，*Cym*。该
值无量纲。

#### 环境

### **Absolute air pressure, Pabs** — 压力 `101325`（默认）| `scalar`

环境绝对压力，*Pabs*，
单位为 Pa。

### **Air temperature, Tair** — 温度 `273`（默认）| `scalar`

环境绝对温度，*T*，单位为 K。

#### 依赖关系

要启用此参数，请清除 **Air temperature**。

### **Gravitational acceleration, g** — 重力 `9.81`（默认）| `scalar`

重力加速度，*g*，单位为 m/s^2。

### **Nominal friction scaling factor, mu** — 摩擦比例因子 `1`（默认）| `scalar`

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

### **Longitudinal velocity tolerance, xdot\_tol** — 容差 `.01`（默认）| `scalar`

纵向速度容差，单位为 m/s。

### **Nominal normal force, Fznom** — 法向力 `5000`（默认）| `scalar`

标称法向力，单位为 N。

#### 依赖关系

要启用此参数，请将 **Axle forces** 设置为以下选项之一：

- `External longitudinal velocity`
- `External longitudinal forces`

### **Geometric longitudinal offset from axle plane, longOff** — 纵向偏移 `0`（默认）| `scalar`

车辆底盘沿车辆固定
*x* 轴从车轴平面的偏移，单位为 m。当您使用 3D 可视化引擎时，
可考虑使用该偏移来独立于车辆 CG 定位底盘。

### **Geometric lateral offset from center plane, latOff** — 侧向偏移 `0`（默认）| `scalar`

车辆底盘沿车辆固定
*y* 轴从中心平面的偏移，单位为 m。当您使用 3D 可视化引擎时，
可考虑使用该偏移来独立于车辆 CG 定位底盘。

### **Geometric vertical offset from axle plane, vertOff** — 垂直偏移 `0`（默认）| `scalar`

车辆底盘沿车辆固定
*z* 轴从车轴平面的偏移，单位为 m。当您使用 3D 可视化引擎时，
可考虑使用该偏移来独立于车辆 CG 定位底盘。

### **Wrap Euler angles, wrapAng** — 将欧拉角包裹到区间 `[-pi, pi]` `off`（默认）| `on`

将欧拉角包裹到区间 `[-pi, pi]`。对于可能经历超出此区间的车辆横摆旋转的车辆机动，如果您希望：

- 跟踪车辆总横摆旋转。
- 避免车辆状态估计器中的不连续性。

可考虑清除该参数。
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

挂车车身 3DOF 模块实现刚性单轴、双轴或三轴挂车车身模型，以计算纵向、横向和横摆运动。将模块配置为单轨或双轨。该模块考虑由挂车加速度、空气阻力和转向引起的车轴和牵引座反作用力。

在车辆动力学和自动驾驶研究中，当车辆俯仰、侧倾和垂向运动不显著时，使用此模块对非完整车辆运动进行建模。

使用 **Vehicle track** 参数指定车轮数量。

| Vehicle Track 设置 | 实现 |
| --- | --- |
| `Single 1-axle` | 单轨单轴挂车。 - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual 1-axle` | 双轨单轴挂车。力作用在车轴硬点位置。 |
| `Single 2-axle` | 单轨双轴挂车。 - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual 2-axle`（默认） | 双轨双轴挂车。力作用在车轴硬点位置。 |
| `Single 3-axle` | 单轨三轴挂车。 - 力沿车轴中心线作用。 - 无侧向载荷转移。 |
| `Dual 3-axle` | 双轨三轴挂车。力作用在车轴硬点位置。 |

使用 **Axle forces** 参数指定力的类型。

| Axle Forces 设置 | 实现 |
| --- | --- |
| `External longitudinal velocity` | - 模块假设外部纵向速度处于准稳态，并且纵向加速度近似为零。 - 由于运动是准稳态的，模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 当您希望执行以下操作时，请考虑此设置： - 生成虚拟传感器信号数据。 - 进行不受动力传动系统或非线性轮胎响应影响的高层软件研究。 |
| `External longitudinal forces` | - 模块使用外部纵向力使车辆加速或制动。 - 模块使用轮胎侧偏角和线性侧偏刚度计算侧向力。 - 当您希望执行以下操作时，请考虑此设置： - 考虑纵向速度变化对侧向和横摆运动的影响。 - 通过力而不是外部纵向速度来指定外部纵向运动。 - 将模块连接到牵引执行器、车轮、制动器和牵引座。 |
| `External forces` | - 模块使用外部侧向力和纵向力来使车辆转向、加速或制动。 - 模块不使用转向输入来计算车辆运动。 - 当您需要具有更准确的非线性侧向和纵向组合滑移的轮胎模型时，请考虑此设置。 |

要创建额外的输入端口，请在 **Input signals** 下选择这些模块参数。

| 输入信号窗格参数 | 输入端口 | 描述 |
| --- | --- | --- |
| **前轮转向** | `WhlAngF` | 前轮转角，*δF* |
| **中轮转向** | `WhlAngM` | 中轮转角，*δM* |
| **后轮转向** | `WhlAngR` | 后轮转角，*δR* |
| **外部风** | `WindXYZ` | 风速，*WX*、*WY* 和 *WZ*，在惯性参考坐标系中 |
| **外部摩擦** | `Mu` | 摩擦系数 |
| **外部力** | `FExt` | 作用在车辆质心（CG）上的外部力，*Fx*、*Fy* 和 *Fz*，在车辆固定坐标系中 |
| **外部力矩** | `MExt` | 绕车辆质心的外部力矩，*Mx*、*My* 和 *Mz*，在车辆固定坐标系中 |
| **前牵引力** | `FhF` | 施加在车身前牵引点处的牵引力，*FhFx*、*FhFy* 和 *FhFz*，在车辆固定坐标系中 |
| **前牵引力矩** | `MhF` | 前牵引点处的牵引力矩，*MhFx*、*MhFy* 和 *MhFz*，绕车辆固定坐标系 |
| **后牵引力** | `FhR` | 施加在车身后牵引点处的牵引力，*FhRx*、*FhRy* 和 *FhRz*，在车辆固定坐标系中 |
| **后牵引力矩** | `MhR` | 后牵引点处的牵引力矩，*MhRx*、*MhRy* 和 *MhRz*，绕车辆固定坐标系 |
| **初始纵向位置** | `X_o` | 车辆质心沿大地固定 *X* 轴的初始位移 |
| **初始横摆角** | `psi_o` | 车辆固定坐标系绕大地固定 *Z* 轴的初始旋转（横摆） |
| **初始纵向速度** | `xdot_o` | 车辆质心沿车辆固定 *x* 轴的初始速度 |
| **初始横摆角速度** | `r_o` | 车辆绕车辆固定 *z* 轴的初始角速度（横摆角速度） |
| **初始横向位置** | `Y_o` | 车辆质心沿大地固定 *Y* 轴的初始位移 |
| **空气温度** | `AirTemp` | 环境空气温度。如果希望在运行时改变温度，请考虑此选项。 |
| **初始横向速度** | `ydot_o` | 车辆质心沿车辆固定 *y* 轴的初始速度 |

### 理论

为确定车辆运动，该模块求解刚体平面动力学运动方程。

**信号轨迹**

| 计算 | 描述 |
| --- | --- |
| *动力学* | 该模块使用这些方程计算刚体平面动力学。  y¨=−x˙r+Fyf+Fym+Fyr+Fyext+Fhyf+Fhyrmr˙=−aFyf−bFym−cFyr+dhfFhyf−dhrFhyr+Mzext+Mhzf+MhzrIzzr=ψ˙  如果将 **Axle forces** 设置为 `External longitudinal forces` 或 `External forces`，则该模块使用此方程计算纵向加速度。  x¨=y˙r+Fxf+Fxm+Fxr−gsin(γ)+Fxext+Fhxf+Fhxrm  如果将 **Axle forces** 设置为 `External longitudinal velocity`，则该模块假设纵向加速度为准稳态。  x¨=0 |
| *外力* | 外力包括阻力和外部力输入。这些力作用在车辆质心上。  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    如果将 **Axle forces** 设置为 `External longitudinal forces`，则该模块使用这些方程。  Fxft=FxfinputFyft=−CyfαfμfFzfFznomFxmt=FxminputFymt=−CymαmμmFzmFznomFxrt=FxrinputFyrt=−CyrαrμrFzrFznom    如果将 **Axle forces** 设置为 `External longitudinal velocity`，则该模块使用这些方程。  Fxft=0Fyft=−CyfαfμfFzfFznomFxmt=0Fymt=−CymαmμmFzmFznomFxrt=0Fyrt=−CyrαrμrFzrFznom    该模块将法向力除以标称法向载荷，以在重量和载荷转移期间改变有效摩擦参数。该模块保持俯仰和侧倾平衡。  Fzf=bmgcos(γ)−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amgcos(γ)+(x¨−y˙r)mh−hFxext+aFzext+Myexta+b |
| *轮胎力* | 该模块使用局部、纵向和横向速度的比值来确定侧偏角。  αf=atan(y˙−arx˙)−δfαm=atan(y˙−brx˙)−δmαr=atan(y˙−crx˙)−δr    该模块使用转向角将轮胎力变换到车辆固定坐标系。  Fxf=Fxftcos(δf)−Fyftsin(δf)Fyf=−Fxftsin(δf)+Fyftcos(δf)Fxm=Fxmtcos(δm)−Fymtsin(δm)Fym=−Fxmtsin(δm)+Fymtcos(δm)Fxr=Fxrtcos(δr)−Fyrtsin(δr)Fyr=−Fxrtsin(δr)+Fyrtcos(δr)    如果将 **Axle forces** 设置为 `External forces`，则该模块假设外部提供的力位于车轴-车轮位置的车辆固定坐标系中。  Fxf=Fxft=FxfinputFyf=Fyft=FyfinputFxm=Fxmt=FxminputFym=Fymt=FyminputFxr=Fxrt=FxrinputFyr=Fyrt=Fyrinput |

**单轨 — 三轴**

作用在三个车轴位置的垂向、纵向和横向力的等轴测视图

**单轨 — 两轴**

作用在两个车轴位置的垂向、纵向和横向力的等轴测视图

**单轨 — 单轴**

作用在一个车轴位置的垂向、纵向和横向力的等轴测视图

**双轨**

| 计算 | 描述 |
| --- | --- |
| *动力学* | 该模块使用这些方程计算刚体平面动力学。  x¨=y˙r+Fxfl+Fxfr+Fxml+Fxmr+Fxrl+Fxrr−gsin(γ)+Fxext+Fhxf+Fhxrmy¨=−x˙r+Fyfl+Fyfr+Fyml+Fymr+Fyrl+Fyrr+Fyext+Fhyf+Fhyrmr˙=−a(Fyfl+Fyfr)−b(Fyml+Fymr)−c(Fyrl+Fyrr)+dhfFhyf−dhrFhyr+Fxfl(wf2+d)−Fxfr(wf2−d)+Fxml(wm2+d)−Fxmr(wm2−d)+Fxrl(wr2+d)−Fxrr(wr2−d)+Mzext+Mhfz+Mhrz−Fhxfhlf−FhxrhlrIzzr=ψ˙  如果将 **Axle forces** 设置为 `External longitudinal velocity`，则该模块假设纵向加速度为准稳态。  x¨=0 |
| *外力* | 外力包括阻力和外部力输入。这些力作用在车辆 CG 上。  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    如果将 **Axle forces** 设置为 `External longitudinal forces`，则该模块使用这些方程。  Fxflt=FxflinputFyflt=−CyflαflμflFzfl2FznomFxfrt=FxfrinputFyfrt=−CyfrαfrμfrFzfr2FznomFxmlt=FxmlinputFymlt=−CymlαmlμmlFzml2FznomFxmrt=FxmrinputFymrt=−CymrαmrμmrFzmr2FznomFxrlt=FxrlinputFyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=FxrrinputFyrrt=−CyrrαrrμrrFzrr2Fznom    如果将 **Axle forces** 设置为 `External longitudinal velocity`，则该模块使用这些方程。  Fxflt=0Fyflt=−CyflαflμflFzfl2FznomFxfrt=0Fyfrt=−CyfrαfrμfrFzfr2FznomFxmlt=0Fymlt=−CymlαmlμmlFzml2FznomFxmrt=0Fymrt=−CymrαmrμmrFzmr2FznomFxrlt=0Fyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=0Fyrrt=−CyrrαrrμrrFzrr2Fznom    该模块将法向力除以标称法向载荷，以在重量和载荷转移期间改变有效摩擦参数。该模块保持俯仰和侧倾平衡。  Fzf=bmgcos(γ)−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amgcos(γ)+(x¨−y˙r)mh−hFxext+aFzext+Myext(a+b)Fzfl=Fzf+(mh(y¨+x˙r)−hFyext−Mxext)2wfFzfr=Fzf+(−mh(y¨+x˙r)+hFyext+Mxext)2wfFzrl=Fzr+(mh(y¨+x˙r)−hFyext−Mxext)2wrFzrr=Fzr+(−mh(y¨+x˙r)+hFyext+Mxext)2wr |
| *轮胎力* | 该模块使用局部速度、纵向速度和横向速度的比值来确定侧偏角。  αfl=atan(y˙−arx˙+rwf2)−δflαfr=atan(y˙−arx˙−rwf2)−δfrαml=atan(y˙−brx˙+rwm2)−δmlαmr=atan(y˙−brx˙−rwm2)−δmrαrl=atan(y˙−crx˙+rwr2)−δrlαrr=atan(y˙−crx˙−rwr2)−δrr    该模块使用转向角将轮胎力变换到车辆固定坐标系。  Fxfl=Fxfltcos(δfl)−Fyfltsin(δfl)Fxfr=Fxfrtcos(δfr)−Fyfrtsin(δfr)Fxml=Fxmltcos(δml)−Fymltsin(δml)Fxmr=Fxmrtcos(δmr)−Fymrtsin(δmr)Fyfl=−Fxfltsin(δfl)+Fyfltcos(δfl)Fyfr=−Fxfrtsin(δfr)+Fyfrtcos(δfr)Fyml=−Fxmltsin(δml)+Fymltcos(δml)Fymr=−Fxmrtsin(δmr)+Fymrtcos(δmr)Fxrl=Fxrltcos(δrl)−Fyrltsin(δrl)Fxrr=Fxrrtcos(δrr)−Fyrrtsin(δrr)Fyrl=−Fxrltsin(δrl)+Fyrltcos(δrl)Fyrr=−Fxrrtsin(δrr)+Fyrrtcos(δrr)    如果将 **Axle forces** 设置为 `External forces`，则该模块假设外部提供的力位于车轴-车轮位置处的车辆固定坐标系中。  Fxfl=Fxflt=FxflinputFxfr=Fxfrt=FxfrinputFxml=Fxmlt=FxmlinputFxmr=Fxmrt=FxmrinputFyfl=Fyflt=FyflinputFyfr=Fyfrt=FyfrinputFyml=Fymlt=FymlinputFymr=Fymrt=FymrinputFxrl=Fxrlt=FxrlinputFxrr=Fxrrt=FxrrinputFyrl=Fyrlt=FyrlinputFyrr=Fyrrt=Fyrrinput |

**Dual Track — Three Axles**

双履带三轴位置处作用的垂向、纵向和横向力的等轴测视图

**Dual Track — Two Axles**

双履带两轴位置处作用的垂向、纵向和横向力的等轴测视图

**Dual Track — One Axle**

双履带单轴位置处作用的垂向、纵向和横向力的等轴测视图

这些图示使用以下变量。

|  |  |
| --- | --- |
| *a*、*b*、*c* | 前轴、中轴和后轴分别距车辆 CG 在公共轴平面上的法向投影点的纵向距离 |
| *h* | 拖拉机 CG 沿车辆固定 *z* 轴在轴平面上方的高度 |
| *d* | 沿车辆固定 *y* 轴从几何中心线到质心的横向距离 |
| *hh\_f*、*hh\_r* | 前挂接点和后挂接点分别沿车辆固定 *z* 轴在轴平面上方的高度 |
| *dh\_f*、*dh\_r* | 前挂接点和后挂接点分别距拖拉机 CG 在公共轴平面上的法向投影点的纵向距离 |
| *wf*、*wm*、*wr* | 前轮距、中轮距和后轮距 |

**阻力**

此表总结了阻力计算的模块实现。

| 计算 | 描述 |
| --- | --- |
| *坐标变换* | 模块将风速从惯性坐标系变换到车辆固定坐标系。 wx=Wxcos(ψ)+Wysin(ψ)wy=Wycos(ψ)−Wxsin(ψ)wz=Wz |
| *阻力* | 为确定相对空速，模块从 CG 车辆速度中减去风速。使用相对空速，模块确定阻力。 w¯=(x˙−wx)2+(y˙−wy)2+(wz)2Fdx=−12TRCdAfPabs(w¯)2Fdy=−12TRCsAfPabs(w¯)2Fdz=−12TRClAfPabs(w¯)2 |
| *阻力矩* | 使用相对空速，模块确定阻力矩。 Mdr=−12TRCrmAfPabs(w¯)2(dh+c)Mdp=−12TRCpmAfPabs(w¯)2(dh+c)Mdy=−12TRCymAfPabs(w¯)2(dh+c) |

**侧偏刚度和松弛动力学**

要启用映射侧偏刚度和松弛长度动态参数，请将 **Axle forces** 设置为 `External
longitudinal forces` 或 `External longitudinal
velocity`。

| 参数设置 | | 描述 |
| --- | --- | --- |
| Mapped Corner Stiffness | Include Relaxation Length Dynamics |
| `Off`（默认） | `On`（默认） | 模块对 *Cyf*、*Cym* 和 *Cyr* 使用恒定侧偏刚度值。滑移角包括松弛长度动态设置。松弛长度近似为作为车轮行程函数的有效侧偏刚度力。 |
| `On` | `On`（默认） | 模块使用作为侧偏刚度数据和滑移角函数的查找表。 Cyf=f(αfσ,Cyfdata)Cym=f(αmσ,Cymdata)Cyr=f(αrσ,Cyrdata)αfσ=1s[(αf−αfσ)vwfαf]αmσ=1s[(αm−αmσ)vmfαm]αrσ=1s[(αr−αrσ)vwrαr]    滑移角包括松弛长度动态设置。松弛长度近似为作为车轮行程函数的有效侧偏刚度力。 |
| `Off`（默认） | `Off` | 模块使用恒定侧偏刚度值 *Cyf*、*Cym* 和 *Cyr*。 |

这些方程使用以下变量。

|  |  |
| --- | --- |
| x,x˙,x¨ | 车辆质心沿车辆固定 *x* 轴的位移、速度和加速度 |
| y,y˙,y¨ | 车辆质心沿车辆固定 *y* 轴的位移、速度和加速度 |
| *ψ* | 车辆固定坐标系绕大地固定 *Z* 轴的旋转（横摆） |
| *r*,Ψ˙ | 车辆绕车辆固定 *z* 轴的角速度（横摆角速度） |
| *Fxf*, *Fxm*, *Fxr* | 施加在前轮、中轮和后轮上的纵向力，沿车辆固定 *x* 轴 |
| *Fyf*, *Fym*, *Fyr* | 施加在前轮、中轮和后轮上的侧向力，沿车辆固定 *y* 轴 |
| *Fxext*, *Fyext*, *Fzext* | 施加在车辆质心上的外部力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *Fdx*, *Fdy*, *Fdz* | 施加在车辆质心上的阻力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *Fxinput*, *Fyinput*, *Fzinput* | 施加在车辆质心上的输入力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *Mxext*, *Myext*, *Mzext* | 绕车辆质心的外部力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *Mdx*, *Mdy*, *Mdz* | 绕车辆质心的阻力力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *Mxinput*, *Myinput*, *Mzinput* | 绕车辆质心的输入力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *Izz* | 车体绕车辆固定 *z* 轴的转动惯量 |
| *Fxft*, *Fxmt*, *Fxrt* | 施加在前轮、中轮和后轮上的纵向轮胎力，沿车辆固定 *x* 轴 |
| *Fyft*, *Fymt*, *Fyrt* | 施加在前轮、中轮和后轮上的侧向轮胎力，沿车辆固定 *y* 轴 |
| *Fxfl*, *Fxfr* | 施加在前左轮和前右轮上的纵向力，沿车辆固定 *x* 轴 |
| *Fyfl*, *Fyfr* | 施加在前左轮和前右轮上的侧向力，沿车辆固定 *y* 轴 |
| *Fxrl*, *Fxrr* | 施加在后左轮和后右轮上的纵向力，沿车辆固定 *x* 轴 |
| *Fyrl*, *Fyrr* | 施加在后左轮和后右轮上的侧向力，沿车辆固定 *y* 轴 |
| *Fxflt*, *Fxfrt* | 施加在前左轮和前右轮上的纵向轮胎力，沿车辆固定 *x* 轴 |
| *Fxmlt*, *Fxmrt* | 施加在中左轮和中右轮上的纵向轮胎力，沿车辆固定 *x* 轴 |
| *Fxrlt*, *Fxrrt* | 施加在后左轮和后右轮上的纵向轮胎力，沿车辆固定 *x* 轴 |
| *Fyflt*, *Fyfrt* | 施加在前左轮和前右轮上的侧向轮胎力，沿车辆固定 *y* 轴 |
| *Fymlt*, *Fymrt* | 施加在中左轮和中右轮上的侧向轮胎力，沿车辆固定 *y* 轴 |
| *Fyrlt*, *Fyrrt* | 施加在后左轮和后右轮上的侧向力，沿车辆固定 *y* 轴 |
| *Fzf*,*Fzr* | 施加在前轮和后轮上的法向力，沿车辆固定 *z* 轴 |
| *Fznom* | 施加在车轴上的标称法向力，沿车辆固定 *z* 轴 |
| *Fzfl*,*Fzfr* | 施加在前左轮和前右轮上的法向力，沿车辆固定 *z* 轴 |
| *Fzrl*,*Fzrr* | 施加在后左轮和后右轮上的法向力，沿车辆固定 *z* 轴 |
| *m* | 车体质量 |
| *a*, *b* | 前轮和后轮分别到车辆质心在公共车轴平面上的法向投影点的距离 |
| *h* | 车辆质心在车轴平面以上的高度 |
| *d* | 沿车辆固定 *y* 轴从几何中心线到质心的侧向距离 |
| *hh* | 沿车辆固定 *z* 轴从车轴平面到牵引装置的高度 |
| *dh* | 从牵引车质心在公共车轴平面上的法向投影点到牵引装置的纵向距离 |
| *hl* | 沿车辆固定 *y* 轴从质心到牵引装置的侧向距离。 |
| *αf*, *αr* | 前轮和后轮侧偏角 |
| *αfl*, *αfr* | 前左轮和前右轮侧偏角 |
| *αrl*, *αrr* | 后左轮和后右轮侧偏角 |
| *δf*, *δr* | 前轮和后轮转向角 |
| *δrl*, *δrr* | 后左轮和后右轮转向角 |
| *δfl*, *δfr* | 前左轮和前右轮转向角 |
| *wf*, *wr* | 前轮距和后轮距 |
| *Cyf*, *Cyr* | 前轮和后轮侧偏刚度 |
| *Cyfdata*, *Cyrdata* | 前轮和后轮侧偏刚度数据 |
| *σf*, *σr* | 前轮和后轮松弛长度 |
| *αfσ*, *αrσ* | 包含松弛长度的前轮和后轮侧偏角 |
| *vwf*, *vwr* | 前轮和后轮硬点速度的大小 |
| *μf*, *μr* | 前轮和后轮摩擦系数 |
| *μfl*, *μfr* | 前左轮和前右轮摩擦系数 |
| *μrl*, *μrr* | 后左轮和后右轮摩擦系数 |
| *Cd* | 沿车辆固定 *x* 轴作用的空气阻力系数 |
| *Cs* | 沿车辆固定 *y* 轴作用的空气阻力系数 |
| *Cl* | 沿车辆固定 *z* 轴作用的空气阻力系数 |
| *Crm* | 绕车辆固定 *x* 轴作用的空气阻力滚转力矩 |
| *Cpm* | 绕车辆固定 *y* 轴作用的空气阻力俯仰力矩 |
| *Cym* | 绕车辆固定 *z* 轴作用的空气阻力横摆力矩 |
| *Af* | 迎风面积 |
| *R* | 大气比气体常数 |
| *T* | 环境空气温度 |
| *Pabs* | 环境绝对压力 |
| *wx*, *wy*, *wz* | 风速，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *Wx*, *Wy*, *Wz* | 风速，沿惯性 *X*、*Y* 和 *Z* 轴 |
