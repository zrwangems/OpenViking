---
type: simulink-block
title: 'Trailer Body 6DOF'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'trailerbody6dof'
documentation_source_path: 'ref/trailerbody6dof.html'
language: zh-CN
chinese_source: worker-translation
---

# Trailer Body 6DOF

## 端口
```yaml
ports:
- name: FSusp
  summary: 作用在挂车上的悬架力 3-by-4 数组（默认）| 3-by-2 数组 | 3-by-6 数组
  direction: input
- name: MSusp
  summary: 作用在挂车上的悬架力矩 3-by-4 array（默认）| 3-by-2 array | 3-by-6 array
  direction: input
- name: FExt
  summary: 作用在车辆上的外部力 vector
  direction: input
- name: MExt
  summary: 作用在车辆上的外部力矩 vector
  direction: input
- name: FhF
  summary: 作用在车身上的前挂钩力 array
  direction: input
- name: MhF
  summary: 绕车体的前挂钩力矩 array
  direction: input
- name: FhR
  summary: 作用在车身上的后挂钩力 array
  direction: input
- name: MhR
  summary: 绕车体的后挂钩力矩 array
  direction: input
- name: WindXYZ
  summary: 风速 array
  direction: input
- name: AirTemp
  summary: 环境空气温度 scalar
  direction: input
- name: Info
  summary: 挂车车身信息总线
  direction: output
- name: Vb
  summary: 车辆固定坐标系下的车辆速度 vector
  direction: output
- name: pqr
  summary: 车辆固定坐标系下的车辆角速度 vector
  direction: output
- name: DCM
  summary: 方向余弦矩阵 array
  direction: output
- name: Euler
  summary: 欧拉角 array
  direction: output
- name: Xe
  summary: 惯性参考坐标系下的车辆位置 vector
  direction: output
- name: Ve
  summary: 惯性参考坐标系下的车辆速度 vector
  direction: output
```

### 输入

### **FSusp** — 作用在挂车上的悬架力 `3-by-4` 数组（默认）| `3-by-2` 数组 | `3-by-6` 数组

施加在挂车硬点位置上的悬架纵向、横向和垂向悬架力，
`FSusp`，单位为 N，指定为 `3-by-2`、
`3-by-4` 或 `3-by-6` 数组，
具体取决于 **Number of axles** 参数。

| **Number of axles** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `1` | FSusp=[FFLxFFRxFFLyFFRyFFLzFFRz] | 数组 – `3-by-2` |
| `2` | FSusp=[FFLxFFRxFRLxFRRxFFLyFFRyFRLyFRRyFFLzFFRzFRLzFRRz] | 数组 – `3-by-4` |
| `3` | FSusp=[FFLxFFRxFMLxFMRxFRLxFRRxFFLyFFRyFMLyFMRyFRLyFRRyFFLzFFRzFMLzFMRzFRLzFRRz] | 数组 – `3-by-6` |

这些数组使用以下变量。

|  |  |
| --- | --- |
| *FFLx*、*FFLy*、*FFLz* | 沿车辆固定 *x*、*y* 和 *z* 轴施加到前左硬点的悬架力 |
| *FFRx*、*FFRy*、*FFRz* | 沿车辆固定 *x*、*y* 和 *z* 轴施加到前右硬点的悬架力 |
| *FMLx*、*FMLy*、*FMLz* | 沿车辆固定 *x*、*y* 和 *z* 轴施加到中左硬点的悬架力 |
| *FMRx*、*FMRy*、*FMRz* | 沿车辆固定 *x*、*y* 和 *z* 轴施加到中右硬点的悬架力 |
| *FRLx*、*FRLy*、*FRLz* | 沿车辆固定 *x*、*y* 和 *z* 轴施加到后左硬点的悬架力 |
| *FRRx*、*FRRy*、*FRRz* | 沿车辆固定 *x*、*y* 和 *z* 轴施加到后右硬点的悬架力 |

### **MSusp** — 作用在挂车上的悬架力矩 `3-by-4 array`（默认）| `3-by-2 array` | `3-by-6 array`

围绕车辆在硬点位置处施加的悬架纵向、横向和垂向悬架力矩，
`MSusp`，单位为 N·m，指定为 `3-by-2`、
`3-by-4` 或 `3-by-6` 数组，
具体取决于 **Number of axles** 参数。

| **Number of axles** 设置 | 变量 | 信号维度 |
| --- | --- | --- |
| `1` | MSusp=[MFLxMFRxMFLyMFRyMFLzMFRz] | 数组 – `3-by-2` |
| `2` | MSusp=[MFLxMFRxMRLxMRRxMFLyMFRyMRLyMRRyMFLzMFRzMRLzMRRz] | 数组 – `3-by-4` |
| `3` | MSusp=[MFLxMFRxMMLxMMRxMRLxMRRxMFLyMFRzMMLyMMRyMRLyMRRyMFLzMFRzMMLzMMRzMRLzMRRz] | 数组 – `3-by-6` |

这些数组使用以下变量。

|  |  |
| --- | --- |
| *MFLx*、*MFLy*、*MFLz* | 围绕车辆固定 *x*、*y* 和 *z* 轴施加到前左硬点的悬架力矩 |
| *MFRx*、*MFRy*、*MFRz* | 围绕车辆固定 *x*、*y* 和 *z* 轴施加到前右硬点的悬架力矩 |
| *MMLx*、*MMLy*、*MMLz* | 围绕车辆固定 *x*、*y* 和 *z* 轴施加到中左硬点的悬架力矩 |
| *MMRx*、*MMRy*、*MMRz* | 围绕车辆固定 *x*、*y* 和 *z* 轴施加到中右硬点的悬架力矩 |
| *MRLx*、*MRLy*、*MRLz* | 围绕车辆固定 *x*、*y* 和 *z* 轴施加到后左硬点的悬架力矩 |
| *MRRx*、*MRRy*、*MRRz* | 围绕车辆固定 *x*、*y* 和 *z* 轴施加到后右硬点的悬架力矩 |

### **FExt** — 作用在车辆上的外部力 `vector`

作用在车辆上的外部力，单位为 N，指定为 `1-by-3` 或
`3-by-1` 向量。

FExt=Fext=[FextxFextyFextz]or[FextxFextyFextz]

| 数组元素 | 力轴 |
| --- | --- |
| `FExt(1,1)` | 车辆固定 *x* 轴（纵向） |
| `FExt(1,2)` 或 `FExt(2,1)` | 车辆固定 *y* 轴（横向） |
| `FExt(1,3)` 或 `FExt(3,1)` | 车辆固定 *z* 轴（垂向） |

### **MExt** — 作用在车辆上的外部力矩 `vector`

作用在车辆上的外部力矩，单位为 N·m，指定为
`1-by-3` 或 `3-by-1` 向量。

MExt=Mext=[MextxMextyMextz]or[MextxMextyMextz]

| 数组元素 | 力轴 |
| --- | --- |
| `MExt(1,1)` | 车辆固定 *x* 轴（纵向） |
| `MExt(1,2)` 或 `MExt(2,1)` | 车辆固定 *y* 轴（横向） |
| `MExt(1,3)` 或 `MExt(3,1)` | 车辆固定 *z* 轴（垂向） |

### **FhF** — 作用在车身上的前挂钩力 `array`

在前挂钩位置施加到车身上的挂钩力，
*FhFx*、
*FhFy*、
*FhFz*，位于车辆固定坐标系中，单位为
N，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖

要启用此端口，请在 **Input signals** 下选择
**Front hitch forces**。

### **MhF** — 绕车体的前挂钩力矩 `array`

前挂钩位置处的挂钩力矩，
*MhFx*、
*MhFy*、
*MhFz*，绕
车辆固定坐标系，单位为 N·m，指定为 `1-by-3` 或
`3-by-1` 数组。

#### 依赖

要启用此端口，请在 **Input signals** 下选择
**Front hitch moments**。

### **FhR** — 作用在车身上的后挂钩力 `array`

在后挂钩位置施加到车身上的挂钩力，
*FhRx*、
*FhRy*、
*FhRz*，位于车辆固定坐标系中，单位为
N，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖

要启用此端口，请在 **Input signals** 下选择
**Rear hitch forces**。

### **MhR** — 绕车体的后挂钩力矩 `array`

后挂钩位置处的挂钩力矩，
*MhRx*、
*MhRy*、
*MhRz*，绕
车辆固定坐标系，单位为 N·m，指定为 `1-by-3` 或
`3-by-1` 数组。

#### 依赖

要启用此端口，请在 **Input signals** 下选择
**Rear hitch moments**。

### **WindXYZ** — 风速 `array`

风速，*Wx*、
*Wy*、
*Wz*，沿惯性 *X* 轴、
*Y* 轴和 *Z* 轴，单位为 m/s，指定为
`1-by-3` 或 `3-by-1` 数组。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，*Tair*，单位为 K，指定为
标量。

#### 依赖

要启用此端口，请在 **Environment** 下选择 **Air
temperature**。
### 输出

### **Info** — 挂车车身信息总线

挂车车身信息，以包含以下值的 bug 信号形式返回。

| 信号 | | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | 车辆质心沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | | 车辆质心沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | | 车辆质心沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | | 车辆质心沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | | 车辆质心沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | | 车辆质心沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `Ang` | `phi` | | | 车辆固定坐标系绕地球固定 *X* 轴的旋转（横滚） | 计算得出 | rad |
| `theta` | | | 车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰） | 计算得出 | rad |
| `psi` | | | 车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆） | 计算得出 | rad |
| `FrntAxl` | `Lft` | `Disp` | `X` | | 前左轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 前左轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 前左轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 前左轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 前左轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 前左轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `X` | | 前右轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 前右轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 前右轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 前右轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 前右轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 前右轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `MidlAxl` | `Lft` | `Disp` | `X` | | 中左轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 中左轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 中左轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 中左轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 中左轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 中左轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `X` | | 中右轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 中右轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 中右轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 中右轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 中右轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 中右轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `RearAxl` | `Lft` | `Disp` | `X` | | 后左轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 后左轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 后左轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 后左轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 后左轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 后左轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `X` | | 后右轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 后右轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 后右轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 后右轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 后右轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 后右轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `HitchF` | `Disp` | `X` | | | 挂车前牵引座相对于轴平面的偏移沿地球固定 *X* 轴的分量 | 计算得出 | m |
| `Y` | | | 挂车前牵引座相对于中心平面的偏移沿地球固定 *Y* 轴的分量 | 计算得出 | m |
| `Z` | | | 挂车前牵引座相对于轴平面的偏移沿地球固定 *Z* 轴的分量 | 计算得出 | m |
| `Vel` | `Xdot` | | | 挂车前牵引座偏移速度沿地球固定 *X* 轴的分量 | 计算得出 | m/s |
| `Ydot` | | | 挂车前牵引座偏移速度沿地球固定 *Y* 轴的分量 | 计算得出 | m/s |
| `Zdot` | | | 挂车前牵引座偏移速度沿地球固定 *Z* 轴的分量 | 计算得出 | m/s |
| `HitchR` | `Disp` | `X` | | | 挂车后牵引座相对于轴平面的偏移沿地球固定 *X* 轴的分量 | 计算得出 | m |
| `Y` | | | 挂车后牵引座相对于中心平面的偏移沿地球固定 *Y* 轴的分量 | 计算得出 | m |
| `Z` | | | 挂车后牵引座相对于轴平面的偏移沿地球固定 *Z* 轴的分量 | 计算得出 | m |
| `Vel` | `Xdot` | | | 牵引座速度沿地球固定 *X* 轴的分量 | 计算得出 | m/s |
| `Ydot` | | | 牵引座速度沿地球固定 *Y* 轴的分量 | 计算得出 | m/s |
| `Zdot` | | | 牵引座速度沿地球固定 *Z* 轴的分量 | 计算得出 | m/s |
| `Geom` | `Disp` | `X` | | | 挂车相对于轴平面的偏移沿地球固定 *X* 轴的分量 | 计算得出 | m |
| `Y` | | | 挂车相对于中心平面的偏移沿地球固定 *Y* 轴的分量 | 计算得出 | m |
| `Z` | | | 挂车相对于轴平面的偏移沿地球固定 *Z* 轴的分量 | 计算得出 | m |
| `Vel` | `Xdot` | | | 挂车偏移速度沿地球固定 *X* 轴的分量 | 计算得出 | m/s |
| `Ydot` | | | 挂车偏移速度沿地球固定 *Y* 轴的分量 | 计算得出 | m/s |
| `Zdot` | | | 挂车偏移速度沿地球固定 *Z* 轴的分量 | 计算得出 | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | 车辆质心沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | | 车辆质心沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | | 车辆质心沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `AngVel` | `p` | | | 车辆绕车辆固定 *x* 轴的角速度（横滚角速率） | 计算得出 | rad/s |
| `q` | | | 车辆绕车辆固定 *y* 轴的角速度（俯仰角速率） | 计算得出 | rad/s |
| `r` | | | 车辆绕车辆固定 *z* 轴的角速度（横摆角速率） | 计算得出 | rad/s |
| `Acc` | `ax` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | 计算得出 | gn |
| `ay` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | 计算得出 | gn |
| `az` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | 计算得出 | gn |
| `xddot` | | | 车辆质心沿车辆固定 *x* 轴的加速度 | 计算得出 | m/s^2 |
| `yddot` | | | 车辆质心沿车辆固定 *y* 轴的加速度 | 计算得出 | m/s^2 |
| `zddot` | | | 车辆质心沿车辆固定 *z* 轴的加速度 | 计算得出 | m/s^2 |
| `DCM` | 方向余弦矩阵 | | | | 计算得出 | rad |
| `Forces` | `Body` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的合力 | 计算得出 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴所受的合力 | 计算得出 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴所受的合力 | 计算得出 | N |
| `Ext` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的外力 | 输入 | N |
| `Fy` | | | 车辆质心沿车辆固定 *x* 轴所受的外力 | 输入 | N |
| `Fz` | | | 车辆质心沿车辆固定 *x* 轴所受的外力 | 输入 | N |
| `FrntAxl` | `Lft` | `Fx` | | 前左轴沿地球固定 *Y* 轴的速度 | 计算得出 | N |
| `Fy` | | 前轴左侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 前轴左侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `Rght` | `Fx` | | 前轴右侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 前轴右侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 前轴右侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `MidlAxl` | `Lft` | `Fx` | | 中轴左侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 中轴左侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fz` | | 中轴左侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `Rght` | `Fx` | | 中轴右侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 中轴右侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 中轴右侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `RearAxl` | `Lft` | `Fx` | | 后轴左侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 后轴左侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 后轴左侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `Rght` | `Fx` | | 后轴右侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 后轴右侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 后轴右侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `HitchF` | `Fx` | | | 在牵引座位置施加于车身的前牵引座力沿车辆固定 *x* 轴的分量 | 计算得出 | N |
| `Fy` | | | 在牵引座位置施加于车身的前牵引座力沿车辆固定 *y* 轴的分量 | 计算得出 | N |
| `Fz` | | | 在牵引座位置施加于车身的前牵引座力沿车辆固定 *z* 轴的分量 | 计算得出 | N |
| `HitchR` | `Fx` | | | 在牵引座位置施加于车身的后牵引座力沿车辆固定 *x* 轴的分量 | 计算得出 | N |
| `Fy` | | | 在牵引座位置施加于车身的后牵引座力沿车辆固定 *y* 轴的分量 | 计算得出 | N |
| `Fz` | | | 在牵引座位置施加于车身的后牵引座力沿车辆固定 *z* 轴的分量 | 计算得出 | N |
| `Tires` | `FrntTires` | `Lft` | `Fx` | 前左轮胎力沿车辆固定 *x* 轴的分量 | 计算得出 | N |
| `Fy` | 前左轮胎力沿车辆固定 *y* 轴的分量 | 计算得出 | N |
| `Fz` | 前左轮胎力沿车辆固定 *z* 轴的分量 | 计算得出 | N |
| `Rght` | `Fx` | 前右轮胎力沿车辆固定 *x* 轴的分量 | 计算得出 | N |
| `Fy` | 前右轮胎力沿车辆固定 *y* 轴的分量 | 计算得出 | N |
| `Fz` | 前右轮胎力沿车辆固定 *z* 轴的分量 | 计算得出 | N |
| `MidlTires` | `Lft` | `Fx` | 中左轮胎力沿车辆固定 *x* 轴的分量 | 计算得出 | N |
| `Fy` | 中左轮胎力沿车辆固定 *y* 轴的分量 | 计算得出 | N |
| `Fz` | 中左轮胎力沿车辆固定 *z* 轴的分量 | 计算得出 | N |
| `Rght` | `Fx` | 中右轮胎力沿车辆固定 *x* 轴的分量 | 计算得出 | N |
| `Fy` | 中右轮胎力沿车辆固定 *y* 轴的分量 | 计算得出 | N |
| `Fz` | 中右轮胎力沿车辆固定 *z* 轴的分量 | 计算得出 | N |
| `RearTires` | `Lft` | `Fx` | 后左轮胎力沿车辆固定 *x* 轴的分量 | 计算得出 | N |
| `Fy` | 后左轮胎力沿车辆固定 *y* 轴的分量 | 计算得出 | N |
| `Fz` | 后左轮胎力沿车辆固定 *z* 轴的分量 | 计算得出 | N |
| `Rght` | `Fx` | 后右轮胎力沿车辆固定 *x* 轴的分量 | 计算得出 | N |
| `Fy` | 后右轮胎力沿车辆固定 *y* 轴的分量 | 计算得出 | N |
| `Fz` | 后右轮胎力沿车辆固定 *z* 轴的分量 | 计算得出 | N |
| `Drag` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的阻力 | 计算得出 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴所受的阻力 | 计算得出 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴所受的阻力 | 计算得出 | N |
| `Grvty` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的重力 | 计算得出 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴所受的重力 | 计算得出 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴所受的重力 | 计算得出 | N |
| `Moments` | `Body` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴所受的车身力矩 | 计算得出 | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴所受的车身力矩 | 计算得出 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴所受的车身力矩 | 计算得出 | N·m |
| `Drag` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴所受的阻力力矩 | 计算得出 | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴所受的阻力力矩 | 计算得出 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴所受的阻力力矩 | 计算得出 | N·m |
| `Ext` | `Mx` | | | 车辆质心绕车辆固定 *x* 轴所受的外力矩 | 计算得出 | N·m |
| `My` | | | 车辆质心绕车辆固定 *y* 轴所受的外力矩 | 计算得出 | N·m |
| `Mz` | | | 车辆质心绕车辆固定 *z* 轴所受的外力矩 | 计算得出 | N·m |
| `HitchF` | `Mx` | | | 前牵引座位置处绕车辆固定 *x* 轴的牵引座力矩 | 计算得出 | N·m |
| `My` | | | 前牵引座位置处绕车辆固定 *y* 轴的牵引座力矩 | 计算得出 | N·m |
| `Mz` | | | 前牵引座位置处绕车辆固定 *z* 轴的牵引座力矩 | 计算得出 | N·m |
| `HitchR` | `Mx` | | | 后牵引座位置处绕车辆固定 *x* 轴的牵引座力矩 | 计算得出 | N·m |
| `My` | | | 后牵引座位置处绕车辆固定 *y* 轴的牵引座力矩 | 计算得出 | N·m |
| `Mz` | | | 后牵引座位置处绕车辆固定 *z* 轴的牵引座力矩 | 计算得出 | N·m |
| `FrntAxl` | `Lft` | `Disp` | `x` | | 前左轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 前左轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 前左轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 前左轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 前左轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 前左轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `x` | | 前右轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 前右轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 前右轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 前右轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 前右轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 前右轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `MidlAxl` | `Lft` | `Disp` | `x` | | 中左轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 中左轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 中左轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 中左轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 中左轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 中左轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `x` | | 中右轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 中右轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 中右轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 中右轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 中右轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 中右轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `RearAxl` | `Lft` | `Disp` | `x` | | 后左轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 后左轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 后左轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 后左轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 后左轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 后左轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `x` | | 后右轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 后右轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 后右轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 后右轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 后右轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 后右轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `HitchF` | `Disp` | | `x` | | 前牵引座相对于轴平面的偏移沿车辆固定 *x* 轴的分量 | 输入 |  |
| `y` | | 前牵引座相对于中心平面的偏移沿车辆固定 *y* 轴的分量 | 输入 |  |
| `z` | | 前牵引座相对于轴平面的偏移沿地球固定 *z* 轴的分量 | 输入 |  |
| `Vel` | | `xdot` | | 前牵引座偏移速度沿车辆固定 *x* 轴的分量 | 计算得出 |  |
| `ydot` | | 前牵引座偏移速度沿车辆固定 *y* 轴的分量 | 计算得出 |  |
| `zdot` | | 前牵引座偏移速度沿车辆固定 *z* 轴的分量 | `0` |  |
| `HitchR` | `Disp` | | `x` | | 后牵引座相对于轴平面的偏移沿车辆固定 *x* 轴的分量 | 输入 | m |
| `y` | | 后牵引座相对于中心平面的偏移沿车辆固定 *y* 轴的分量 | 输入 | m |
| `z` | | 后牵引座相对于轴平面的偏移沿地球固定 *z* 轴的分量 | 输入 | m |
| `Vel` | | `xdot` | | 后牵引座偏移速度沿车辆固定 *x* 轴的分量 | 计算得出 | m/s |
| `ydot` | | 后牵引座偏移速度沿车辆固定 *y* 轴的分量 | 计算得出 | m/s |
| `zdot` | | 后牵引座偏移速度沿车辆固定 *z* 轴的分量 | `0` | m/s |
| `Pwr` | `PwrExt` | | | | 施加的外部功率 | 计算得出 | W |
| `Drag` | | | | 阻力导致的功率损失 | 计算得出 | W |
| `Geom` | `Disp` | | `x` | | 挂车相对于轴平面的偏移沿车辆固定 *x* 轴的分量 | 输入 | m |
| `y` | | 挂车相对于中心平面的偏移沿车辆固定 *y* 轴的分量 | 输入 | m |
| `z` | | 挂车相对于轴平面的偏移沿车辆固定 *z* 轴的分量 | 输入 | m |
| `Vel` | | `xdot` | | 挂车底盘偏移速度沿车辆固定 *x* 轴的分量 | 计算得出 | m/s |
| `ydot` | | 挂车底盘偏移速度沿车辆固定 *y* 轴的分量 | 计算得出 | m/s |
| `zdot` | | 挂车底盘偏移速度沿车辆固定 *z* 轴的分量 | 计算得出 | m/s |
| `Ang` | | `Beta` | | 车身侧偏角，*β*    β=VyVx | 计算得出 | rad |

### **Vb** — 车辆固定坐标系下的车辆速度 `vector`

车辆质心分别沿车辆固定 *x*、*y*、*z* 轴的速度，单位为 m/s，以向量形式返回。

### **pqr** — 车辆固定坐标系下的车辆角速度 `vector`

车辆质心分别绕车辆固定 *x* 轴（滚转角速率）、*y* 轴（俯仰角速率）、*z* 轴（偏航角速率）的角速度，单位为 rad/s，以向量形式返回。

### **DCM** — 方向余弦矩阵 `array`

方向余弦矩阵，单位为 rad，以数组形式返回。

### **Euler** — 欧拉角 `array`

欧拉角 *φ*、*θ* 和 *ψ*，单位分别为 rad，以数组形式返回。

### **Xe** — 惯性参考坐标系下的车辆位置 `vector`

车辆质心分别沿惯性固定 *X*、*Y*、*Z* 轴的位置，单位为 m，以向量形式返回。

### **Ve** — 惯性参考坐标系下的车辆速度 `vector`

车辆质心分别沿惯性固定 *X*、*Y*、*Z* 轴的速度，单位为 m/s，以向量形式返回。
## 参数
```yaml
parameters:
- name: Number of axles
  summary: 创建牵引力输入端口 2（默认）| 1 | 3
  group: 模块选项
- name: Front hitch forces
  summary: FhF 输入端口 on（默认）| off
  group: 模块选项
- name: Front hitch moments
  summary: MhF 输入端口 on（默认）| off
  group: 模块选项
- name: Rear hitch forces
  summary: FhR 输入端口 off（默认）| on
  group: 模块选项
- name: Rear hitch moments
  summary: MhR 输入端口 off（默认）| on
  group: 模块选项
- name: Vehicle mass, m
  summary: 质量 2000（默认）| scalar
  group: 底盘
- name: Longitudinal distance from center of mass to front axle, a
  summary: 质心到前轴的距离 1.4（默认）| scalar
  group: 底盘
- name: Longitudinal distance from center of mass to middle axle, b
  summary: 质心到中轴的距离 1.6（默认）| scalar
  group: 底盘
- name: Longitudinal distance from center of mass to rear axle, c
  summary: 质心到后轴的距离 1.9（默认）| scalar
  group: 底盘
- name: Lateral distance from geometric centerline to center of mass, d
  summary: 几何中心线到质心的横向距离 0（默认）| scalar
  group: 底盘
- name: Vertical distance from center of mass to axle plane, h
  summary: 质心到车轴平面的垂直距离 .35（默认）| scalar
  group: 底盘
- name: Longitudinal distance from center of mass to front hitch, dh_f
  summary: 质心到牵引装置的纵向距离 1（默认）| scalar
  group: 底盘
- name: 几何中心线到前挂钩的横向距离，hl_f
  summary: 从中心线到前挂钩的距离 0（默认）| scalar
  group: 底盘
- name: 前挂钩到车轴平面的垂直距离，hh_f
  summary: 从前挂钩到车轴平面的距离 0.1（默认）| scalar
  group: 底盘
- name: 从质心到后挂钩的纵向距离，dh_r
  summary: 到前挂钩的距离 1（默认）| scalar
  group: 底盘
- name: 几何中心线到后挂钩的横向距离，hl_r
  summary: 从中心线到后挂钩的距离 0（默认）| scalar
  group: 底盘
- name: 后挂钩到车轴平面的垂直距离，hh_r
  summary: 从后挂钩到车轴平面的距离 0.1（默认）| scalar
  group: 底盘
- name: 惯性坐标系中的初始位置 [Xeo,Yeo,Zeo]，Xe_o
  summary: 初始位置 [0,0,0]（默认）| vector
  group: 底盘
- name: 车体坐标系中的初始速度 [xdot_o,ydot_o,zdot_o]，xbdot_o
  summary: 初始速度 [0,0,0]（默认）| vector
  group: 底盘
- name: 初始欧拉姿态 [roll, pitch, yaw]，eul_o
  summary: 旋转 [0,0,0]（默认）| vector
  group: 底盘
- name: 初始车体旋转速率 [p,q,r]，p_o
  summary: 初始旋转速率 [0,0,0]（默认）| vector
  group: 底盘
- name: 底盘惯性张量，Iveh
  summary: 惯性 [430 0 0; 0 1900 0; 0 0 2100]（默认）| array
  group: 底盘
- name: 前轮距，w_f
  summary: 前轮距 1.9（默认）| scalar
  group: 底盘
- name: 中轮距，w_m
  summary: 中轮距 1.9（默认）| scalar
  group: 底盘
- name: 后轮距，w_r
  summary: 后轮距 1.9（默认）| scalar
  group: 底盘
- name: 质量，z1m
  summary: 质量 0（默认）| scalar
  group: 惯性载荷
- name: 距前轴的距离向量，z1R
  summary: 距离 [-.25,.125,.15]（默认）| vector
  group: 惯性载荷
- name: 惯性张量，z1I
  summary: 惯性 [1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0（默认）| array
  group: 惯性载荷
- name: 质量，z2m
  summary: 质量 0（默认）| scalar
  group: 惯性载荷
- name: 距前轴的距离向量，z2R
  summary: 距离 [1.4,0,.8]（默认）| vector
  group: 惯性载荷
- name: 惯性张量，z2I
  summary: 惯性 [1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0（默认）| array
  group: 惯性载荷
- name: 质量，z3m
  summary: 质量 0（默认）| scalar
  group: 惯性载荷
- name: 距前轴的距离向量，z3R
  summary: 距离 [.75,-.5,.4]（默认）| vector
  group: 惯性载荷
- name: 惯性张量，z3I
  summary: 惯性 [5,-.1,-2;-2,9,.1;-.1,.1,6].*0（默认）| array
  group: 惯性载荷
- name: Mass, z4m
  summary: 质量 0（默认）| scalar
  group: 惯性载荷
- name: Distance vector from front axle, z4R
  summary: 距离 [.75,.5,.4]（默认）| vector
  group: 惯性载荷
- name: Inertia tensor, z4I
  summary: 惯性 [5,-.1,-2;-2,9,.1;-.1,.1,6].*0（默认）| array
  group: 惯性载荷
- name: Mass, z5m
  summary: 质量 0（默认）| scalar
  group: 惯性载荷
- name: Distance vector from front axle, z5R
  summary: 距离 [1.25,-.5,.4]（默认）| vector
  group: 惯性载荷
- name: Inertia tensor, z5I
  summary: 惯性 [5,-.1,-2;-2,9,.1;-.1,.1,6].*0（默认）| array
  group: 惯性载荷
- name: Mass, z6m
  summary: 质量 0（默认）| scalar
  group: 惯性载荷
- name: Distance vector from front axle, z6R
  summary: 距离 [1.25,-.5,.4]（默认）| vector
  group: 惯性载荷
- name: Inertia tensor, z6I
  summary: 惯性 [5,-.1,-2;-2,9,.1;-.1,.1,6].*0（默认）| array
  group: 惯性载荷
- name: Mass, z7m
  summary: 质量 0（默认）| scalar
  group: 惯性载荷
- name: Distance vector from front axle, z7R
  summary: 距离 [2,0,.25]（默认）| vector
  group: 惯性载荷
- name: Inertia tensor, z7I
  summary: 惯性 [1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0（默认）| array
  group: 惯性载荷
- name: Longitudinal drag area, Af
  summary: 阻力面积 2（默认）| scalar
  group: Aerodynamic
- name: Longitudinal drag coefficient, Cd
  summary: 阻力系数 .3（默认）| scalar
  group: Aerodynamic
- name: Longitudinal lift coefficient, Cl
  summary: 升力 .1（默认）| scalar
  group: Aerodynamic
- name: Longitudinal drag pitch moment, Cpm
  summary: 俯仰阻力 .1（默认）| scalar
  group: Aerodynamic
- name: Relative wind angle vector, beta_w
  summary: 风角 [0:0.001:0.01]（默认）| vector
  group: Aerodynamic
- name: Side force coefficient vector, Cs
  summary: 侧向力阻力 [0:0.01:0.1]（默认）| vector
  group: Aerodynamic
- name: Yaw moment coefficient vector, Cym
  summary: 横摆力矩阻力 [0:0.001:0.01]（默认）| vector
  group: Aerodynamic
- name: Absolute air pressure, Pabs
  summary: 压力 101325（默认）| scalar
  group: Environment
- name: Air temperature, Tair
  summary: 环境空气温度 273（默认）| scalar
  group: Environment
- name: Gravitational acceleration, g
  summary: 重力 9.81（默认）| scalar
  group: Environment
- name: Longitudinal velocity tolerance, xdot_tol
  summary: 容差 .1（默认）| scalar
  group: 仿真
- name: Geometric longitudinal offset from axle plane, longOff
  summary: 纵向偏移 0（默认）| scalar
  group: 仿真
- name: Geometric lateral offset from center plane, latOff
  summary: 横向偏移 0（默认）| scalar
  group: 仿真
- name: Geometric vertical offset from axle plane, vertOff
  summary: 垂直偏移 0（默认）| scalar
  group: 仿真
- name: Wrap Euler angles, wrapAng
  summary: Selection on (default) | off
  group: 仿真
```

### 模块选项

### **Number of axles** — 创建牵引力输入端口 `2`（默认）| `1` | `3`

指定挂车的车轴数量。

#### 输入信号

### **Front hitch forces** — `FhF` 输入端口 `on`（默认）| `off`

选择以创建输入端口 `Fh`。

### **Front hitch moments** — `MhF` 输入端口 `on`（默认）| `off`

选择以创建输入端口 `Mh`。

### **Rear hitch forces** — `FhR` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `Fh`。

### **Rear hitch moments** — `MhR` 输入端口 `off`（默认）| `on`

选择以创建输入端口 `Mh`。

### 底盘

### **Vehicle mass, m** — 质量 `2000`（默认）| `scalar`

车辆质量 *m*，单位为 kg。该质量通常对应于簧载质量。

### **Longitudinal distance from center of mass to front axle, a** — 质心到前轴的距离 `1.4`（默认）| `scalar`

从车辆质心到前轴的距离 *a*，单位为 m。

挂车侧视图，显示从质心到车轴和牵引装置的纵向距离

### **Longitudinal distance from center of mass to middle axle, b** — 质心到中轴的距离 `1.6`（默认）| `scalar`

从车辆质心到中轴的距离 *b*，单位为 m。

挂车侧视图，显示从质心到车轴和牵引装置的纵向距离

#### 依赖关系

要启用此参数，请将 **Number of axles** 设置为 `3`。

### **Longitudinal distance from center of mass to rear axle, c** — 质心到后轴的距离 `1.9`（默认）| `scalar`

从车辆质心到后轴的距离 *c*，单位为 m。

挂车侧视图，显示从质心到车轴和牵引装置的纵向距离

#### 依赖关系

要启用此参数，请将 **Number of axles** 设置为 `2` 或 `3`。

### **Lateral distance from geometric centerline to center of mass, d** — 几何中心线到质心的横向距离 `0`（默认）| `scalar`

从几何中心线到质心的横向距离 *d*，单位为 m，沿车辆固定 *y* 轴方向。正值表示车辆质心位于几何中心线右侧。负值表示车辆质心位于几何中心线左侧。

轮距和质心偏离中心线的俯视图。

### **Vertical distance from center of mass to axle plane, h** — 质心到车轴平面的垂直距离 `.35`（默认）| `scalar`

从车辆质心到车轴平面的垂直距离 *h*，单位为 m。

挂车侧视图，显示从质心到车轴和牵引装置的纵向距离

### **Longitudinal distance from center of mass to front hitch, dh\_f** — 质心到牵引装置的纵向距离 `1`（默认）| `scalar`

从质心到前牵引装置的纵向距离 *dh\_f*，单位为 m。

挂车侧视图，显示从质心到车轴和牵引装置的纵向距离

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中选择 **Front hitch forces** 或 **Front hitch moments**。

### **几何中心线到前挂钩的横向距离，hl\_f** — 从中心线到前挂钩的距离 `0`（默认）| `scalar`

从几何中心线到前挂钩的横向距离，
*hl\_f*，单位为 m，沿车辆固定 *y* 轴方向。
正值表示挂车挂钩位于几何中心线右侧。负值表示挂车挂钩位于几何中心线左侧。

车轴宽度和质心相对中心线偏移的俯视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Front hitch forces** 或 **Front hitch
moments**。

### **前挂钩到车轴平面的垂直距离，hh\_f** — 从前挂钩到车轴平面的距离 `0.1`（默认）| `scalar`

从前挂钩到车轴平面的垂直距离，
*hh\_f*，单位为 m。

显示纵向车轴和挂钩到质心距离的挂车侧视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Front hitch forces** 或 **Front hitch
moments**。

### **从质心到后挂钩的纵向距离，dh\_r** — 到前挂钩的距离 `1`（默认）| `scalar`

从质心到后挂钩的纵向距离，
*dh\_r*，单位为 m。

显示纵向车轴和挂钩到质心距离的挂车侧视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Rear hitch forces** 或 **Rear hitch
moments**。

### **几何中心线到后挂钩的横向距离，hl\_r** — 从中心线到后挂钩的距离 `0`（默认）| `scalar`

从几何中心线到后挂钩的横向距离，
*hl\_r*，单位为 m，沿车辆固定 *y* 轴方向。
正值表示挂车挂钩位于几何中心线右侧。负值表示挂车挂钩位于几何中心线左侧。

车轴宽度和质心相对中心线偏移的俯视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Rear hitch forces** 或 **Rear hitch
moments**。

### **后挂钩到车轴平面的垂直距离，hh\_r** — 从后挂钩到车轴平面的距离 `0.1`（默认）| `scalar`

从后挂钩到车轴平面的垂直距离，
*hh\_r*，单位为 m。

显示纵向车轴和挂钩到质心距离的挂车侧视图

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择
**Rear hitch forces** 或 **Rear hitch
moments**。

### **惯性坐标系中的初始位置 [Xeo,Yeo,Zeo]，Xe\_o** — 初始位置 `[0,0,0]`（默认）| `vector`

车辆在惯性坐标系中的初始位置，
*Xeo*，单位为 m。

### **车体坐标系中的初始速度 [xdot\_o,ydot\_o,zdot\_o]，xbdot\_o** — 初始速度 `[0,0,0]`（默认）| `vector`

车辆质心分别沿车辆固定
*x*、*y* 和
*z* 轴的初始速度，单位为 m/s。

### **初始欧拉姿态 [roll, pitch, yaw]，eul\_o** — 旋转 `[0,0,0]`（默认）| `vector`

车辆固定坐标系分别绕地球固定 *X* 轴（roll）、*Y* 轴
（pitch）、*Z* 轴（yaw）的初始欧拉旋转，单位为 rad。

### **初始车体旋转速率 [p,q,r]，p\_o** — 初始旋转速率 `[0,0,0]`（默认）| `vector`

车辆质心分别绕车辆固定
*x* 轴（roll rate）、*y* 轴（pitch
rate）、*z* 轴（yaw rate）的初始角速度，单位为
rad/s。

### **底盘惯性张量，Iveh** — 惯性 `[430 0 0; 0 1900 0; 0 0 2100]`（默认）| `array`

车辆惯性张量，
*Iveh*，单位为 kg\*m^2。维度
为 `[3-by-3]`。

### **前轮距，w\_f** — 前轮距 `1.9`（默认）| `scalar`

前轮距，单位为 m。

轮距和质心相对中心线偏移的俯视图。

### **中轮距，w\_m** — 中轮距 `1.9`（默认）| `scalar`

中轮距，单位为 m。

轮距和质心相对中心线偏移的俯视图。

#### 依赖关系

要启用此参数，请将 **Number of axles**
设置为 `3`。

### **后轮距，w\_r** — 后轮距 `1.9`（默认）| `scalar`

后轮距，单位为 m。

轮距和质心相对中心线偏移的俯视图。

#### 依赖

要启用此参数，请将 **Number of axles** 设置为 `2` 或 `3`。

### 惯性载荷

#### 前端

### **质量，z1m** — 质量 `0`（默认）| `scalar`

质量，*z1m*，单位为 kg。

### **距前轴的距离向量，z1R** — 距离 `[-.25,.125,.15]`（默认）| `vector`

从前轴到载荷的距离向量，*z1R*，单位为 m。维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z1R(1,1)` | 从前悬架硬点到载荷，沿车辆固定 *x* 轴 |
| `z1R(1,2)` | 从车辆中心线到载荷，沿车辆固定 *y* 轴 |
| `z1R(1,3)` | 从前悬架硬点到载荷，沿车辆固定 *z* 轴 |

例如，此表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴前方 - 车辆中心线右侧 - 前轴悬架硬点上方 | - `z1R(1,1)` < 0 - `z1R(1,2)` > 0 - `z1R(1,3)` > 0 |

### **惯性张量，z1I** — 惯性 `[1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0`（默认）| `array`

惯性张量，*z1I*，单位为 kg·m^2。维度为 `[3-by-3]`。

z1I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定 *x* 轴
- *y* 轴沿车辆固定 *y* 轴
- *z* 轴沿车辆固定 *z* 轴

#### 顶部

### **质量，z2m** — 质量 `0`（默认）| `scalar`

质量，*z2m*，单位为 kg。

### **距前轴的距离向量，z2R** — 距离 `[1.4,0,.8]`（默认）| `vector`

从前轴到载荷的距离向量，*z2R*，单位为 m。维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z2R(1,1)` | 从前悬架硬点到载荷，沿车辆固定 *x* 轴 |
| `z2R(1,2)` | 从车辆中心线到载荷，沿车辆固定 *y* 轴 |
| `z2R(1,3)` | 从前悬架硬点到载荷，沿车辆固定 *z* 轴 |

例如，此表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线左侧 - 前轴悬架硬点上方 | - `z2R(1,1)` > 0 - `z2R(1,2)` < 0 - `z2R(1,3)` > 0 |

### **惯性张量，z2I** — 惯性 `[1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0`（默认）| `array`

惯性张量，*z2I*，单位为 kg·m^2。维度为 `[3-by-3]`。

z2I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定 *x* 轴
- *y* 轴沿车辆固定 *y* 轴
- *z* 轴沿车辆固定 *z* 轴

#### 左前

### **质量，z3m** — 质量 `0`（默认）| `scalar`

质量，*z3m*，单位为 kg。

### **距前轴的距离向量，z3R** — 距离 `[.75,-.5,.4]`（默认）| `vector`

从前轴到载荷的距离向量，*z3R*，单位为 m。维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z3R(1,1)` | 从前悬架硬点到载荷，沿车辆固定 *x* 轴 |
| `z3R(1,2)` | 从车辆中心线到载荷，沿车辆固定 *y* 轴 |
| `z3R(1,3)` | 从前悬架硬点到载荷，沿车辆固定 *z* 轴 |

例如，此表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线左侧 - 前轴悬架硬点上方 | - `z3R(1,1)` > 0 - `z3R(1,2)` < 0 - `z3R(1,3)` > 0 |

### **惯性张量，z3I** — 惯性 `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0`（默认）| `array`

惯性张量，*z3I*，单位为 kg·m^2。维度为 `[3-by-3]`。

z3I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定 *x* 轴
- *y* 轴沿车辆固定 *y* 轴
- *z* 轴沿车辆固定 *z* 轴

#### Front Right

### **Mass, z4m** — 质量 `0`（默认）| `scalar`

质量，*z4m*，单位为 kg。

### **Distance vector from front axle, z4R** — 距离 `[.75,.5,.4]`（默认）| `vector`

从前轴到载荷的距离向量，*z4R*，单位为 m。
维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z4R(1,1)` | 从前悬架硬点至载荷，沿车辆固定 *x* 轴 |
| `z4R(1,2)` | 从车辆中心线至载荷，沿车辆固定 *y* 轴 |
| `z4R(1,3)` | 从前悬架硬点至载荷，沿车辆固定 *z* 轴 |

例如，下表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线右侧 - 前轴悬架硬点上方 | - `z4R(1,1)` > 0 - `z4R(1,2)` > 0 - `z4R(1,3)` > 0 |

### **Inertia tensor, z4I** — 惯性 `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0`（默认）| `array`

惯性张量，*z4I*，单位为 kg·m^2。维度为
`[3-by-3]`。

z4I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

#### Rear Left

### **Mass, z5m** — 质量 `0`（默认）| `scalar`

质量，z5m，单位为 kg。

### **Distance vector from front axle, z5R** — 距离 `[1.25,-.5,.4]`（默认）| `vector`

从前轴到载荷的距离向量，*z5R*，单位为 m。
维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z5R(1,1)` | 从前悬架硬点至载荷，沿车辆固定 *x* 轴 |
| `z5R(1,2)` | 从车辆中心线至载荷，沿车辆固定 *y* 轴 |
| `z5R(1,3)` | 从前悬架硬点至载荷，沿车辆固定 *z* 轴 |

例如，下表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线左侧 - 前轴悬架硬点上方 | - `z5R(1,1)` > 0 - `z5R(1,2)` < 0 - `z5R(1,3)` > 0 |

### **Inertia tensor, z5I** — 惯性 `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0`（默认）| `array`

惯性张量，*z5I*，单位为 kg·m^2。维度为
`[3-by-3]`。

z5I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

#### Rear Right

### **Mass, z6m** — 质量 `0`（默认）| `scalar`

质量，*z6m*，单位为 kg。

### **Distance vector from front axle, z6R** — 距离 `[1.25,-.5,.4]`（默认）| `vector`

从前轴到载荷的距离向量，*z6R*，单位为 m。
维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z6R(1,1)` | 从前悬架硬点至载荷，沿车辆固定 *x* 轴 |
| `z6R(1,2)` | 从车辆中心线至载荷，沿车辆固定 *y* 轴 |
| `z6R(1,3)` | 从前悬架硬点至载荷，沿车辆固定 *z* 轴 |

例如，下表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线右侧 - 前轴悬架硬点上方 | - `z6R(1,1)` > 0 - `z6R(1,2)` > 0 - `z6R(1,3)` > 0 |

### **Inertia tensor, z6I** — 惯性 `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0`（默认）| `array`

惯性张量，*z6I*，单位为 kg·m^2。维度为
`[3-by-3]`。

z6I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

#### Rear End

### **Mass, z7m** — 质量 `0`（默认）| `scalar`

质量，*z7m*，单位为 kg。

### **Distance vector from front axle, z7R** — 距离 `[2,0,.25]`（默认）| `vector`

从前轴到载荷的距离向量，*z7R*，单位为 m。
维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z7R(1,1)` | 前悬架硬点至载荷，沿车辆固定 *x* 轴 |
| `z7R(1,2)` | 车辆中心线至载荷，沿车辆固定 *y* 轴 |
| `z7R(1,3)` | 前悬架硬点至载荷，沿车辆固定 *z* 轴 |

例如，下表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线右侧 - 前轴悬架硬点上方 | - `z7R(1,1)` > 0 - `z7R(1,2)` > 0 - `z7R(1,3)` > 0 |

### **Inertia tensor, z7I** — 惯性 `[1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0`（默认）| `array`

惯性张量，*z7I*，单位为 kg·m^2。维度为
`[3-by-3]`。

z7I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

### Aerodynamic

### **Longitudinal drag area, Af** — 阻力面积 `2`（默认）| `scalar`

用于计算车辆气动阻力的有效车辆横截面积，
*Af*，单位为 m^2。

### **Longitudinal drag coefficient, Cd** — 阻力系数 `.3`（默认）| `scalar`

空气阻力系数，*Cd*，
无量纲。

### **Longitudinal lift coefficient, Cl** — 升力 `.1`（默认）| `scalar`

空气升力系数，*Cl*，
无量纲。

### **Longitudinal drag pitch moment, Cpm** — 俯仰阻力 `.1`（默认）| `scalar`

纵向阻力俯仰力矩系数，
*Cpm*，
无量纲。

### **Relative wind angle vector, beta\_w** — 风角 `[0:0.001:0.01]`（默认）| `vector`

相对风角向量，
*βw*，单位为 rad。

### **Side force coefficient vector, Cs** — 侧向力阻力 `[0:0.01:0.1]`（默认）| `vector`

侧向力系数向量系数，
*Cs*，
无量纲。

### **Yaw moment coefficient vector, Cym** — 横摆力矩阻力 `[0:0.001:0.01]`（默认）| `vector`

横摆力矩系数向量系数，
*Cym*，
无量纲。

### Environment

### **Absolute air pressure, Pabs** — 压力 `101325`（默认）| `scalar`

环境空气绝对压力，*Pabs*，
单位为 Pa。

### **Air temperature, Tair** — 环境空气温度 `273`（默认）| `scalar`

环境空气温度，*Tair*，单位为 K。

#### 依赖关系

要启用此参数，请清除 **Air temperature**。

### **Gravitational acceleration, g** — 重力 `9.81`（默认）| `scalar`

重力加速度，*g*，单位为 m/s^2。

### 仿真

### **Longitudinal velocity tolerance, xdot\_tol** — 容差 `.1`（默认）| `scalar`

纵向速度容差，
*xdottol*，单位为
m/s。

该模块使用此参数来避免在计算车身侧偏角 *β* 时发生除零。

### **Geometric longitudinal offset from axle plane, longOff** — 纵向偏移 `0`（默认）| `scalar`

拖车沿车身固定
*x* 轴相对于轴平面的偏移，单位为 m。当您使用 3D 可视化
引擎时，可考虑使用该偏移来独立于车辆质心定位底盘。

### **Geometric lateral offset from center plane, latOff** — 横向偏移 `0`（默认）| `scalar`

拖车沿车身固定
*y* 轴相对于中心平面的偏移，单位为 m。当您使用 3D 可视化
引擎时，可考虑使用该偏移来独立于车辆质心定位底盘。

### **Geometric vertical offset from axle plane, vertOff** — 垂直偏移 `0`（默认）| `scalar`

拖车沿车身固定
*z* 轴相对于轴平面的偏移，单位为 m。当您使用 3D 可视化
引擎时，可考虑使用该偏移来独立于车辆质心定位底盘。

### **Wrap Euler angles, wrapAng** — Selection `on` (default) | `off`

将欧拉角包裹到区间 `[-pi, pi]`。
对于可能经历超出该区间的车辆横摆旋转的车辆机动，如果您希望：

- 跟踪车辆总横摆旋转。
- 避免车辆状态估计器中的不连续性。

请考虑清除该参数。
## 所属库

Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

具有平移和旋转运动的挂车车身

Trailer Body 6DOF 模块实现了一个刚性单轴、双轴或三轴挂车车身模型，用于计算纵向、横向、垂向、俯仰、侧倾和横摆运动。该模块考虑了车身质量、惯性、气动阻力、道路坡度，以及由于悬架和外力及力矩在车轴硬点位置之间的重量分布。

使用 **Inertial Loads** 参数来分析不同载荷条件下的挂车动力学。要指定挂车车轴数量，请使用 **Number of axles** 参数。

要创建额外的输入端口，请在 **Input signals** 下选择这些模块参数。

| 参数 | 输入端口 | 描述 |
| --- | --- | --- |
| **Front hitch forces** | `FhF` | 施加在车身前部牵引点位置的牵引力，*FhFx*、*FhFy* 和 *FhFz*，位于车辆固定坐标系中 |
| **Front hitch moments** | `MhF` | 前部牵引点位置的牵引力矩，*MhFx*、*MhFy* 和 *MhFz*，关于车辆固定坐标系 |
| **Rear hitch forces** | `FhR` | 施加在车身后部牵引点位置的牵引力，*FhRx*、*FhRy* 和 *FhRz*，位于车辆固定坐标系中 |
| **Rear hitch moments** | `MhR` | 后部牵引点位置的牵引力矩，*MhRx*、*MhRy* 和 *MhRz*，关于车辆固定坐标系 |

### Inertial Loads

要分析不同载荷条件下的车辆动力学，请使用 **Inertial Loads** 参数。您可以指定以下载荷：

- 前端
- 顶部
- 左前和右前
- 左后和右后
- 后端

对于每种载荷，您可以指定质量、位置和惯量。

插图提供了载荷位置和车辆参数尺寸。表格提供了相应的位置参数符号设置。

显示载荷位置的挂车俯视图和侧视图

下表汇总了用于指定由圆点表示的载荷位置的参数设置。对于位置，模块使用以下距离向量：

- 前轴到载荷，沿车辆固定 *x* 轴
- 车辆中心线到载荷，沿车辆固定 *y* 轴
- 前轴到载荷，沿车辆固定 *z* 轴

| 载荷 | 参数 | 示例位置 |
| --- | --- | --- |
| 前端 | **Distance vector from front axle, z1R** | - `z1R(1,1)<0` — 前轴前方 - `z1R(1,2)>0` — 车辆中心线右侧 - `z1R(1,3)>0` — 前轴悬架硬点上方 |
| 顶部 | **Distance vector from front axle, z2R** | - `z2R(1,1)>0` — 前轴后方 - `z2R(1,2)<0` — 车辆中心线左侧 - `z2R(1,3)>0` — 前轴悬架硬点上方 |
| 左前 | **Distance vector from front axle, z3R** | - `z3R(1,1)>0` — 前轴后方 - `z3R(1,2)<0` — 车辆中心线左侧 - `z3R(1,3)>0` — 前轴悬架硬点上方 |
| 右前 | **Distance vector from front axle, z4R** | - `z4R(1,1)>0` — 前轴后方 - `z4R(1,2)>0` — 车辆中心线右侧 - `z4R(1,3)>0` — 前轴悬架硬点上方 |
| 左后 | **Distance vector from front axle, z5R** | - `z5R(1,1)>0` — 前轴后方 - `z5R(1,2)<0` — 车辆中心线左侧 - `z5R(1,3)>0` — 前轴悬架硬点上方 |
| 右后 | **Distance vector from front axle, z6R** | - `z6R(1,1)>0` — 前轴后方 - `z6R(1,2)>0` — 车辆中心线右侧 - `z6R(1,3)>0` — 前轴悬架硬点上方 |
| 后端 | **Distance vector from front axle, z7R** | - `z7R(1,1)>0` — 前轴后方 - `z7R(1,2)>0` — 车辆中心线右侧 - `z7R(1,3)>0` — 前轴悬架硬点上方 |

### 运动方程

为确定车辆运动，该模块实现了刚体车辆动力学、风阻、惯性载荷和坐标变换的计算。体坐标系和车辆坐标系相同。

该模块考虑体坐标系相对于平坦大地固定惯性参考系的旋转。体坐标系的原点是车身的车辆重心。

该模块使用此方程计算体坐标系的平移运动，其中施加的力 [*Fx
Fy Fz*]T
位于体坐标系中，且假设刚体质量 *m* 为常数。

F¯b=[FxFyFz]=m(V¯˙b+ω¯×V¯b)M¯b=[LMN]=Iω¯˙+ω¯×(Iω¯)I=[Ixx−Ixy−Ixz−IyxIyy−Iyz−Izx−IzyIzz]

为确定体坐标系角速度向量 [*p q r*]T 与欧拉角变化率 [ϕ˙  θ˙   ψ˙]T 之间的关系，该模块将欧拉角速率分解到体坐标系中。

[pqr]=[ϕ˙00]+[1000cosϕsinϕ0−sinϕcosϕ][0θ˙0]+[1000cosϕsinϕ0−sinϕcosϕ][cosθ0−sinθ010sinθ0cosθ][00ψ˙]≡J−1[ϕ˙θ˙ψ˙]

对 *J* 求逆可得到用于确定欧拉角速率向量所需的关系。

[ϕ˙θ˙ψ˙]=J[pqr] =[1(sinϕtanθ)(cosϕtanθ)0cosϕ−sinϕ0sinϕcosθcosϕcosθ][pqr]

施加的力和力矩是阻力、重力、外力和悬架力之和。

F¯b=[FxFyFz]=[FdxFdyFdz]+[FgxFgyFgz]+[FextxFextyFextz]+[FFLxFFLyFFLz]+[FFRxFFRyFFRz]+[FMLxFMLyFMLz]+[FMRxFMRyFMRz]+[FRLxFRLyFRLz]+[FRRxFRRyFRRz]M¯b=[MxMyMz]=[MdxMdyMdz]+[MextxMextyMextz]+[MFLxMFLyMFLz]+[MFRxMFRyMFRz]+[MMLxMMLyMMLz]+[MMRxMMRyMMRz]+[MRLxMRLyMRLz]+[MRRxMRRyMRRz]+M¯F

| 计算 | 实现 |
| --- | --- |
| 载荷质量和惯量 | 该模块使用平行轴定理，将各个载荷的质量和惯量与车辆质量和惯量进行合成。  Jij=Iij+m(|R|2δij−RiRj) |
| 重力，*Fg* | 该模块使用方向余弦矩阵 (DCM) 将惯性固定坐标系中的重力向量变换到体坐标系。 |
| 阻力，*Fd*，以及力矩，*Md* | 为确定相对空速，该模块从车辆质心 (CM) 速度中减去风速。使用相对空速，该模块确定阻力。  w¯=(x˙−wx)2+(y˙−wy)2+(wz)2Fdx=−12TRCdAfPabs(w¯)2Fdy=−12TRCsAfPabs(w¯)2Fdz=−12TRClAfPabs(w¯)2    使用相对空速，该模块确定阻力矩。  Mdr=−12TRCrmAfPabs(w¯)2(a+c)Mdp=−12TRCpmAfPabs(w¯)2(a+c)Mdy=−12TRCymAfPabs(w¯)2(a+c) |
| 外力，*Fin*，以及力矩，*Min* | 外力和力矩通过端口 **FExt** 和 **MExt** 输入。 |
| 悬架力和力矩 | 该模块假设悬架力和力矩作用在这些硬点位置：  - *FFL*，   *MFL* — 左前 - *FFR*，   *MFR* — 右前 - *FML*，   *MML* — 左中 - *FMR*，   *MMR* — 右中 - *FRL*，   *MRL* — 左后 - *FRR*，   *MRR* — 右后 |

这些方程使用以下变量。

|  |  |
| --- | --- |
| x,x˙,x¨ | 车辆质心沿车辆固定 *x* 轴的位移、速度和加速度 |
| y,y˙,y¨ | 车辆质心沿车辆固定 *y* 轴的位移、速度和加速度 |
| z,z˙,z¨ | 车辆质心沿车辆固定 *z* 轴的位移、速度和加速度 |
| *φ* | 车辆固定坐标系绕大地固定 *X* 轴的旋转（横滚） |
| *θ* | 车辆固定坐标系绕大地固定 *Y* 轴的旋转（俯仰） |
| *ψ* | 车辆固定坐标系绕大地固定 *Z* 轴的旋转（横摆） |
| *FFLx*, *FFLy*, *FFLz* | 施加在前左硬点上的悬架力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *FFRx*, *FFRy*, *FFRz* | 施加在前右硬点上的悬架力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *FMLx*, *FMLy*, *FMLz* | 施加在中左硬点上的悬架力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *FMRx*, *FMRy*, *FMRz* | 施加在中右硬点上的悬架力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *FRLx*, *FRLy*, *FRLz* | 施加在后左硬点上的悬架力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *FRRx*, *FRRy*, *FRRz* | 施加在后右硬点上的悬架力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *MFLx*, *MFLy*, *MFLz* | 施加在前左硬点上的悬架力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *MFRx*, *MFRy*, *MFRz* | 施加在前右硬点上的悬架力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *MMLx*, *MMLy*, *MMLz* | 施加在中左硬点上的悬架力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *MMRx*, *MMRy*, *MMRz* | 施加在中右硬点上的悬架力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *MRLx*, *MRLy*, *MRLz* | 施加在后左硬点上的悬架力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *MRRx*, *MRRy*, *MRRz* | 施加在后右硬点上的悬架力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *Fextx*, *Fexty*, *Fextz* | 施加在车辆质心上的外力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *Fdx*, *Fdy*, *Fdz* | 施加在车辆质心上的阻力，沿车辆固定 *x*、*y* 和 *z* 轴 |
| *Mextx*, *Mexty*, *Mextz* | 绕车辆质心的外力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *Mdx*, *Mdy*, *Mdz* | 绕车辆质心的阻力矩，绕车辆固定 *x*、*y* 和 *z* 轴 |
| *I* | 车体转动惯量 |
| *a*, *b*, *c* | 前轴、中轴和后轴分别距车辆质心在公共轴平面上的法向投影点的距离 |
| *h* | 车辆质心在轴平面上方的高度 |
| *d* | 沿车辆固定 *y* 轴从几何中心线到质心的横向距离 |
| *hh\_f*, *hh\_r* | 前挂钩和后挂钩分别沿车辆固定 *z* 轴在轴平面上方的高度 |
| *dh\_f*, *dh\_r* | 前挂钩和后挂钩分别距车辆质心在公共轴平面上的法向投影点的纵向距离 |
| *hl\_f*, *hl\_r* | 沿车辆固定 *y* 轴从质心到前挂钩和后挂钩的横向距离 |
| *wF*, *wM*, *wR* | 前轮距、中轮距和后轮距 |
| *Cd* | 沿车辆固定 *x* 轴作用的空气阻力系数 |
| *Cs* | 沿车辆固定 *y* 轴作用的空气阻力系数 |
| *Cl* | 沿车辆固定 *z* 轴作用的空气阻力系数 |
| *Crm* | 绕车辆固定 *x* 轴作用的空气阻力横滚力矩 |
| *Cpm* | 绕车辆固定 *y* 轴作用的空气阻力俯仰力矩 |
| *Cym* | 绕车辆固定 *z* 轴作用的空气阻力横摆力矩 |
| *Af* | 迎风面积 |
| *R* | 大气比气体常数 |
| *T* | 环境空气温度 |
| *Pabs* | 环境绝对压力 |
| *wx*, *wy*, *wz* | 沿车辆固定 *x*、*y* 和 *z* 轴的风速 |
| *Wx*, *Wy*, *Wz* | 沿惯性 *X*、*Y* 和 *Z* 轴的风速 |
