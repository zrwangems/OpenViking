---
type: simulink-block
title: 'Vehicle Body 6DOF Three Axles'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'vehiclebody6dofthreeaxles'
documentation_source_path: 'ref/vehiclebody6dofthreeaxles.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Body 6DOF Three Axles

## 端口
```yaml
ports:
- name: FSusp
  summary: 作用在车辆上的悬架力 3-by-6 数组
  direction: input
- name: MSusp
  summary: 作用在车辆上的悬架力矩 3-by-6 数组
  direction: input
- name: FExt
  summary: 作用在车辆上的外部力 vector
  direction: input
- name: MExt
  summary: 作用在车辆上的外部力矩 vector
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
- name: AirTemp
  summary: 环境空气温度 scalar
  direction: input
- name: Info
  summary: 车身信息总线
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

### **FSusp** — 作用在车辆上的悬架力 `3-by-6` 数组

作用在车辆硬点位置处的悬架纵向、横向和垂向悬架力，单位为 N，指定为 `3-by-6` 数组。

FSusp=[FFLxFFRxFMLxFMRxFRLxFRRxFFLyFFRyFMLyFMRyFRLyFRRyFFLzFFRzFMLzFMRzFRLzFRRz]

| 数组元素 | 车轴 | 轮距 | 力轴 |
| --- | --- | --- | --- |
| `FSusp(1,1)` | 前 | 左 | 车辆固定 *x* 轴（纵向） |
| `FSusp(1,2)` | 前 | 右 |
| `FSusp(1,3)` | 中 | 左 |
| `FSusp(1,4)` | 中 | 右 |
| `FSusp(1,5)` | 后 | 左 |
| `FSusp(1,6)` | 后 | 右 |
| `FSusp(2,1)` | 前 | 左 | 车辆固定 *y* 轴（横向） |
| `FSusp(2,2)` | 前 | 右 |
| `FSusp(2,3)` | 中 | 左 |
| `FSusp(2,4)` | 中 | 右 |
| `FSusp(2,5)` | 后 | 左 |
| `FSusp(2,6)` | 后 | 右 |
| `FSusp(3,1)` | 前 | 左 | 车辆固定 *z* 轴（垂向） |
| `FSusp(3,2)` | 前 | 右 |
| `FSusp(3,3)` | 中 | 左 |
| `FSusp(3,4)` | 中 | 右 |
| `FSusp(3,5)` | 后 | 左 |
| `FSusp(3,6)` | 后 | 右 |

### **MSusp** — 作用在车辆上的悬架力矩 `3-by-6` 数组

作用在车辆硬点位置处、绕车辆的悬架纵向、横向和垂向悬架力矩，单位为 N，指定为 `3-by-6` 数组。

MSusp=[MFLxMFRxMMLxMMRxMRLxMRRxMFLyMFRzMMLyMMRyMRLyMRRyMFLzMFRzMMLzMMRzMRLzMRRz]

| 数组元素 | 车轴 | 轮距 | 力矩轴 |
| --- | --- | --- | --- |
| `MSusp(1,1)` | 前 | 左 | 车辆固定 *x* 轴（纵向） |
| `MSusp(1,2)` | 前 | 右 |
| `MSusp(1,3)` | 中 | 左 |
| `MSusp(1,4)` | 中 | 右 |
| `MSusp(1,5)` | 后 | 左 |
| `MSusp(1,6)` | 后 | 右 |
| `MSusp(2,1)` | 前 | 左 | 车辆固定 *y* 轴（横向） |
| `MSusp(2,2)` | 前 | 右 |
| `MSusp(2,3)` | 中 | 左 |
| `MSusp(2,4)` | 中 | 右 |
| `MSusp(2,5)` | 后 | 左 |
| `MSusp(2,6)` | 后 | 右 |
| `MSusp(3,1)` | 前 | 左 | 车辆固定 *z* 轴（垂向） |
| `MSusp(3,2)` | 前 | 右 |
| `MSusp(3,3)` | 中 | 左 |
| `MSusp(3,4)` | 中 | 右 |
| `MSusp(3,5)` | 后 | 左 |
| `MSusp(3,6)` | 后 | 右 |

### **FExt** — 作用在车辆上的外部力 `vector`

作用在车辆上的外部力，单位为 N，指定为 `1-by-3` 或 `3-by-1` 向量。

FExt=Fext=[FextxFextyFextz]or[FextxFextyFextz]

| 数组元素 | 力轴 |
| --- | --- |
| `FExt(1,1)` | 车辆固定 *x* 轴（纵向） |
| `FExt(1,2)` 或 `FExt(2,1)` | 车辆固定 *y* 轴（横向） |
| `FExt(1,3)` 或 `FExt(3,1)` | 车辆固定 *z* 轴（垂向） |

### **MExt** — 作用在车辆上的外部力矩 `vector`

作用在车辆上的外部力矩，单位为 N·m，指定为 `1-by-3` 或 `3-by-1` 向量。

MExt=Mext=[MextxMextyMextz]or[MextxMextyMextz]

| 数组元素 | 力轴 |
| --- | --- |
| `MExt(1,1)` | 车辆固定 *x* 轴（纵向） |
| `MExt(1,2)` 或 `MExt(2,1)` | 车辆固定 *y* 轴（横向） |
| `MExt(1,3)` 或 `MExt(3,1)` | 车辆固定 *z* 轴（垂向） |

### **Fh** — 作用在车体上的牵引力 `array`

作用在车体牵引点位置处的牵引力，*Fhx*、*Fhy*、*Fhz*，位于车辆固定坐标系中，单位为 N，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Hitch forces**。

### **Mh** — 绕车体的牵引力矩 `array`

牵引点位置处的牵引力矩，*Mhx*、*Mhy*、*Mhz*，绕车辆固定坐标系，单位为 N·m，指定为 `1-by-3` 或 `3-by-1` 数组。

#### 依赖关系

要启用此端口，请在 **Input signals** 下选择 **Hitch moments**。

### **WindXYZ** — 风速 `array`

沿惯性 *X*、*Y* 和 *Z* 轴的风速，*Wx*、*Wy*、*Wz*，单位为 m/s，指定为 `1-by-3` 或 `3-by-1` 数组。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，*Tair*，单位为 K，指定为标量。

#### 依赖关系

要启用此端口，请在 **Environment** 下选择 **Air temperature**。
### 输出

### **Info** — 车身信息总线

车辆车身信息，以包含以下值的总线信号形式返回。

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
| `FrntAxl` | `Lft` | `Disp` | `X` | | 前左车轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 前左车轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 前左车轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 前左车轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 前左车轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 前左车轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `X` | | 前右车轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 前右车轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 前右车轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 前右车轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 前右车轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 前右车轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `MidlAxl` | `Lft` | `Disp` | `X` | | 中左车轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 中左车轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 中左车轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 中左车轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 中左车轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 中左车轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `X` | | 中右车轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 中右车轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 中右车轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 中右车轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 中右车轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 中右车轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `RearAxl` | `Lft` | `Disp` | `X` | | 后左车轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 后左车轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 后左车轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 后左车轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 后左车轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 后左车轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `X` | | 后右车轴沿地球固定 *X* 轴的位移 | 计算得出 | m |
| `Y` | | 后右车轴沿地球固定 *Y* 轴的位移 | 计算得出 | m |
| `Z` | | 后右车轴沿地球固定 *Z* 轴的位移 | 计算得出 | m |
| `Vel` | `Xdot` | | 后右车轴沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | 后右车轴沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | 后右车轴沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `Hitch` | `Disp` | `X` | | | 牵引装置沿地球固定 *X* 轴相对于车轴平面的偏移 | 计算得出 | m |
| `Y` | | | 牵引装置沿地球固定 *Y* 轴相对于车轴平面的偏移 | 计算得出 | m |
| `Z` | | | 牵引装置沿地球固定 *Z* 轴相对于车轴平面的偏移 | 计算得出 | m |
| `Vel` | `Xdot` | | | 牵引装置沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | | 牵引装置沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | | 牵引装置沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
| `Geom` | `Disp` | `X` | | | 车辆底盘沿地球固定 *X* 轴相对于车轴平面的偏移 | 计算得出 | m |
| `Y` | | | 车辆底盘沿地球固定 *Y* 轴相对于中心平面的偏移 | 计算得出 | m |
| `Z` | | | 车辆底盘沿地球固定 *Z* 轴相对于车轴平面的偏移 | 计算得出 | m |
| `Vel` | `Xdot` | | | 车辆底盘偏移沿地球固定 *X* 轴的速度 | 计算得出 | m/s |
| `Ydot` | | | 车辆底盘偏移沿地球固定 *Y* 轴的速度 | 计算得出 | m/s |
| `Zdot` | | | 车辆底盘偏移沿地球固定 *Z* 轴的速度 | 计算得出 | m/s |
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
| `Ext` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的外部力 | 输入 | N |
| `Fy` | | | 车辆质心沿车辆固定 *x* 轴所受的外部力 | 输入 | N |
| `Fz` | | | 车辆质心沿车辆固定 *x* 轴所受的外部力 | 输入 | N |
| `FrntAxl` | `Lft` | `Fx` | | 前左车轴沿地球固定 *Y* 轴的速度 | 计算得出 | N |
| `Fy` | | 前左车轴左侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 前左车轴左侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `Rght` | `Fx` | | 前右车轴右侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 前右车轴左侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 前右车轴右侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `MidlAxl` | `Lft` | `Fx` | | 中左车轴左侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 中左车轴左侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fz` | | 中左车轴左侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `Rght` | `Fx` | | 中右车轴右侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 中右车轴左侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 中右车轴右侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `RearAxl` | `Lft` | `Fx` | | 后左车轴左侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 后左车轴左侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 后左车轴左侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `Rght` | `Fx` | | 后右车轴右侧沿车辆固定 *x* 轴所受的纵向力 | 计算得出 | N |
| `Fy` | | 后右车轴左侧沿车辆固定 *y* 轴所受的侧向力 | 计算得出 | N |
| `Fz` | | 后右车轴右侧沿车辆固定 *z* 轴所受的法向力 | 计算得出 | N |
| `Hitch` | `Fx` | | | 牵引装置位置处施加在车身上的牵引力沿车辆固定 *x* 轴的分量 | 计算得出 | N |
| `Fy` | | | 牵引装置位置处施加在车身上的牵引力沿车辆固定 *y* 轴的分量 | 计算得出 | N |
| `Fz` | | | 牵引装置位置处施加在车身上的牵引力沿车辆固定 *z* 轴的分量 | 计算得出 | N |
| `Tires` | `FrntTires` | `Lft` | `Fx` | 前左轮胎沿车辆固定 *x* 轴的力 | 计算得出 | N |
| `Fy` | 前左轮胎沿车辆固定 *y* 轴的力 | 计算得出 | N |
| `Fz` | 前左轮胎沿车辆固定 *z* 轴的力 | 计算得出 | N |
| `Rght` | `Fx` | 前右轮胎沿车辆固定 *x* 轴的力 | 计算得出 | N |
| `Fy` | 前右轮胎沿车辆固定 *y* 轴的力 | 计算得出 | N |
| `Fz` | 前右轮胎沿车辆固定 *z* 轴的力 | 计算得出 | N |
| `MidlTires` | `Lft` | `Fx` | 中左轮胎沿车辆固定 *x* 轴的力 | 计算得出 | N |
| `Fy` | 中左轮胎沿车辆固定 *y* 轴的力 | 计算得出 | N |
| `Fz` | 中左轮胎沿车辆固定 *z* 轴的力 | 计算得出 | N |
| `Rght` | `Fx` | 中右轮胎沿车辆固定 *x* 轴的力 | 计算得出 | N |
| `Fy` | 中右轮胎沿车辆固定 *y* 轴的力 | 计算得出 | N |
| `Fz` | 中右轮胎沿车辆固定 *z* 轴的力 | 计算得出 | N |
| `RearTires` | `Lft` | `Fx` | 后左轮胎沿车辆固定 *x* 轴的力 | 计算得出 | N |
| `Fy` | 后左轮胎沿车辆固定 *y* 轴的力 | 计算得出 | N |
| `Fz` | 后左轮胎沿车辆固定 *z* 轴的力 | 计算得出 | N |
| `Rght` | `Fx` | 后右轮胎沿车辆固定 *x* 轴的力 | 计算得出 | N |
| `Fy` | 后右轮胎沿车辆固定 *y* 轴的力 | 计算得出 | N |
| `Fz` | 后右轮胎沿车辆固定 *z* 轴的力 | 计算得出 | N |
| `Drag` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的阻力 | 计算得出 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴所受的阻力 | 计算得出 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴所受的阻力 | 计算得出 | N |
| `Grvty` | `Fx` | | | 车辆质心沿车辆固定 *x* 轴所受的重力 | 计算得出 | N |
| `Fy` | | | 车辆质心沿车辆固定 *y* 轴所受的重力 | 计算得出 | N |
| `Fz` | | | 车辆质心沿车辆固定 *z* 轴所受的重力 | 计算得出 | N |
| `Moments` | `Body` | `Mx` | | | 车身绕车辆固定 *x* 轴作用于车辆质心的力矩 | 计算得出 | N·m |
| `My` | | | 车身绕车辆固定 *y* 轴作用于车辆质心的力矩 | 计算得出 | N·m |
| `Mz` | | | 车身绕车辆固定 *z* 轴作用于车辆质心的力矩 | 计算得出 | N·m |
| `Drag` | `Mx` | | | 阻力绕车辆固定 *x* 轴作用于车辆质心的力矩 | 计算得出 | N·m |
| `My` | | | 阻力绕车辆固定 *y* 轴作用于车辆质心的力矩 | 计算得出 | N·m |
| `Mz` | | | 阻力绕车辆固定 *z* 轴作用于车辆质心的力矩 | 计算得出 | N·m |
| `Ext` | `Mx` | | | 外部力矩绕车辆固定 *x* 轴作用于车辆质心的力矩 | 计算得出 | N·m |
| `My` | | | 外部力矩绕车辆固定 *y* 轴作用于车辆质心的力矩 | 计算得出 | N·m |
| `Mz` | | | 外部力矩绕车辆固定 *z* 轴作用于车辆质心的力矩 | 计算得出 | N·m |
| `Hitch` | `Mx` | | | 牵引装置位置处绕车辆固定 *x* 轴的力矩 | 计算得出 | N·m |
| `My` | | | 牵引装置位置处绕车辆固定 *y* 轴的力矩 | 计算得出 | N·m |
| `Mz` | | | 牵引装置位置处绕车辆固定 *z* 轴的力矩 | 计算得出 | N·m |
| `FrntAxl` | `Lft` | `Disp` | `x` | | 前左车轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 前左车轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 前左车轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 前左车轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 前左车轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 前左车轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `x` | | 前右车轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 前右车轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 前右车轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 前右车轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 前右车轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 前右车轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `MidlAxl` | `Lft` | `Disp` | `x` | | 中左车轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 中左车轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 中左车轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 中左车轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 中左车轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 中左车轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `x` | | 中右车轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 中右车轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 中右车轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 中右车轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 中右车轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 中右车轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `RearAxl` | `Lft` | `Disp` | `x` | | 后左车轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 后左车轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 后左车轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 后左车轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 后左车轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 后左车轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `Rght` | `Disp` | `x` | | 后右车轴沿车辆固定 *x* 轴的位移 | 计算得出 | m |
| `y` | | 后右车轴沿车辆固定 *y* 轴的位移 | 计算得出 | m |
| `z` | | 后右车轴沿车辆固定 *z* 轴的位移 | 计算得出 | m |
| `Vel` | `xdot` | | 后右车轴沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 后右车轴沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 后右车轴沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `Hitch` | `Disp` | | `x` | | 牵引装置沿车辆固定 *x* 轴相对于车轴平面的偏移 | 输入 | m |
| `y` | | 牵引装置沿车辆固定 *y* 轴相对于中心平面的偏移 | 输入 | m |
| `z` | | 牵引装置沿车辆固定 *z* 轴相对于车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 牵引装置偏移沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 牵引装置偏移沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 牵引装置偏移沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
| `Pwr` | `PwrExt` | | | | 施加的外部功率 | 计算得出 | W |
| `Drag` | | | | 阻力导致的功率损失 | 计算得出 | W |
| `Geom` | `Disp` | | `x` | | 车辆底盘沿车辆固定 *x* 轴相对于车轴平面的偏移 | 输入 | m |
| `y` | | 车辆底盘沿车辆固定 *y* 轴相对于中心平面的偏移 | 输入 | m |
| `z` | | 车辆底盘沿车辆固定 *z* 轴相对于车轴平面的偏移 | 输入 | m |
| `Vel` | | `xdot` | | 车辆底盘偏移沿车辆固定 *x* 轴的速度 | 计算得出 | m/s |
| `ydot` | | 车辆底盘偏移沿车辆固定 *y* 轴的速度 | 计算得出 | m/s |
| `zdot` | | 车辆底盘偏移沿车辆固定 *z* 轴的速度 | 计算得出 | m/s |
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
- name: Hitch forces
  summary: 创建牵引力输入端口 off（默认）| on
  group: 模块选项
- name: Hitch moments
  summary: 创建牵引力矩输入端口 off（默认）| on
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
  summary: 质心到后轴的距离 1.8（默认）| scalar
  group: 底盘
- name: Lateral distance from geometric centerline to center of mass, d
  summary: 几何中心线到质心的横向距离 0（默认）| scalar
  group: 底盘
- name: Vertical distance from center of mass to axle plane, h
  summary: 距离 .35（默认）| scalar
  group: 底盘
- name: Longitudinal distance from center of mass to hitch, dh
  summary: 从质心到牵引点的纵向距离 1（默认）| scalar
  group: 底盘
- name: Longitudinal distance from center of mass to hitch, hl
  summary: 从质心到牵引点的横向距离 0（默认）| scalar
  group: 底盘
- name: Vertical distance from hitch to axle plane, hh
  summary: 从牵引点到轴平面的距离 0.1（默认）| scalar
  group: 底盘
- name: Initial position in the inertial frame [Xeo,Yeo,Zeo], Xe_o
  summary: 初始位置 [0,0,0]（默认）| vector
  group: 底盘
- name: Initial velocity in body axes [xdot_o,ydot_o,zdot_o], xbdot_o
  summary: 初始速度 [0,0,0]（默认）| vector
  group: 底盘
- name: Initial Euler orientation [roll, pitch, yaw], eul_o
  summary: 初始欧拉旋转 [0,0,0]（默认）| vector
  group: 底盘
- name: Initial body rotation rates [p,q,r], p_o
  summary: 初始旋转速率 [0,0,0]（默认）| vector
  group: 底盘
- name: Chassis inertia tensor, Iveh
  summary: 惯性 [430 0 0; 0 1900 0; 0 0 2100]（默认）| array
  group: 底盘
- name: Track widths [front,rear], w
  summary: 宽度 [1.9,1.9,1.9]（默认）| vector
  group: 底盘
- name: Mass, z1m
  summary: 拖拉机前部质量 0（默认）| scalar
  group: 惯性载荷
- name: Distance vector from front axle, z1R
  summary: 拖拉机前部距前轴的距离 [-.25,.125,.15]（默认）| vector
  group: 惯性载荷
- name: Inertia tensor, z1I
  summary: 拖拉机前部惯性 [1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0（默认）| array
  group: 惯性载荷
- name: Mass, z2m
  summary: 驾驶室顶部质量 0（默认）| scalar
  group: 惯性载荷
- name: Distance vector from front axle, z2R
  summary: 驾驶室顶部距前轴的距离 [1.4,0,.8]（默认）| vector
  group: 惯性载荷
- name: 惯性张量，z2I
  summary: 驾驶室顶部惯性 [1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0（默认）| array
  group: 惯性载荷
- name: 质量，z3m
  summary: 拖拉机车架左侧质量 0（默认）| scalar
  group: 惯性载荷
- name: 距前轴的距离矢量，z3R
  summary: 拖拉机车架左侧距前轴的距离 [.75,-.5,.4]（默认）| vector
  group: 惯性载荷
- name: 惯性张量，z3I
  summary: 拖拉机车架左侧惯性 [5,-.1,-2;-2,9,.1;-.1,.1,6].*0（默认）| array
  group: 惯性载荷
- name: 质量，z4m
  summary: 拖拉机车架右侧质量 0（默认）| scalar
  group: 惯性载荷
- name: 距前轴的距离矢量，z4R
  summary: 拖拉机车架右侧距前轴的距离 [.75,.5,.4]（默认）| vector
  group: 惯性载荷
- name: 惯性张量，z4I
  summary: 拖拉机车架右侧惯性 [5,-.1,-2;-2,9,.1;-.1,.1,6].*0（默认）| array
  group: 惯性载荷
- name: 质量，z5m
  summary: 驾驶室左侧质量 0（默认）| scalar
  group: 惯性载荷
- name: 距前轴的距离矢量，z5R
  summary: 驾驶室左侧距前轴的距离 [1.25,-.5,.4]（默认）| vector
  group: 惯性载荷
- name: Inertia tensor, z5I
  summary: Cab left inertia [5,-.1,-2;-2,9,.1;-.1,.1,6].*0（默认）| array
  group: 惯性载荷
- name: Mass, z6m
  summary: Cab right mass 0（默认）| scalar
  group: 惯性载荷
- name: Distance vector from front axle, z6R
  summary: Cab right distance from front axle [1.25,-.5,.4]（默认）| vector
  group: 惯性载荷
- name: Inertia tensor, z6I
  summary: Cab right inertia [5,-.1,-2;-2,9,.1;-.1,.1,6].*0（默认）| array
  group: 惯性载荷
- name: Mass, z7m
  summary: Tractor rear mass 0（默认）| scalar
  group: 惯性载荷
- name: Distance vector from front axle, z7R
  summary: Tractor rear mass distance from front axle [2,0,.25]（默认）| vector
  group: 惯性载荷
- name: Inertia tensor, z7I
  summary: Tractor rear inertia [1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0（默认）| array
  group: 惯性载荷
- name: Longitudinal drag area, Af
  summary: Vehicle cross-sectional area 2（默认）| scalar
  group: Aerodynamic
- name: Longitudinal drag coefficient, Cd
  summary: Air drag coefficient .3（默认）| scalar
  group: Aerodynamic
- name: Longitudinal lift coefficient, Cl
  summary: Air lift coefficient .1（默认）| scalar
  group: Aerodynamic
- name: Longitudinal drag pitch moment, Cpm
  summary: Pitch drag .1（默认）| scalar
  group: Aerodynamic
- name: Relative wind angle vector, beta_w
  summary: Wind angle [0:0.001:0.01]（默认）| vector
  group: Aerodynamic
- name: Side force coefficient vector, Cs
  summary: Side force drag [0:0.01:0.1]（默认）| vector
  group: Aerodynamic
- name: 横摆力矩系数向量，Cym
  summary: 横摆力矩阻力 [0:0.001:0.01]（默认）| vector
  group: Aerodynamic
- name: 绝对空气压力，Pabs
  summary: 压力 101325（默认）| scalar
  group: 环境
- name: 空气温度，Tair
  summary: 环境空气温度 273（默认）| scalar
  group: 环境
- name: 重力加速度，g
  summary: 重力 9.81（默认）| scalar
  group: 环境
- name: 纵向速度容差，xdot_tol
  summary: 容差 .1（默认）| scalar
  group: 仿真
- name: 距轴平面的几何纵向偏移，longOff
  summary: 纵向偏移 0（默认）| scalar
  group: 仿真
- name: 距中心平面的几何横向偏移，latOff
  summary: 横向偏移 0（默认）| scalar
  group: 仿真
- name: 距轴平面的几何垂向偏移，vertOff
  summary: 垂向偏移 0（默认）| scalar
  group: 仿真
- name: 包裹欧拉角，wrapAng
  summary: 选择 on（默认）| off
  group: 仿真
```

### 模块选项

#### 输入信号

### **Hitch forces** — 创建牵引力输入端口 `off`（默认）| `on`

选择此项可创建牵引力的输入端口 `Fh`。

### **Hitch moments** — 创建牵引力矩输入端口 `off`（默认）| `on`

选择此项可创建牵引力矩的输入端口 `Mh`。

### 底盘

### **Vehicle mass, m** — 质量 `2000`（默认）| `scalar`

车辆质量 *m*，单位为 kg。该质量通常对应于簧上质量。

### **Longitudinal distance from center of mass to front axle, a** — 质心到前轴的距离 `1.4`（默认）| `scalar`

车辆质心到前轴的距离 *a*，单位为 m。

车辆俯视图和侧视图，显示载荷位置

### **Longitudinal distance from center of mass to middle axle, b** — 质心到中轴的距离 `1.6`（默认）| `scalar`

车辆质心到中轴的距离 *b*，单位为 m。

车辆俯视图和侧视图，显示载荷位置

### **Longitudinal distance from center of mass to rear axle, c** — 质心到后轴的距离 `1.8`（默认）| `scalar`

车辆质心到后轴的距离 *c*，单位为 m。

车辆俯视图和侧视图，显示载荷位置

### **Lateral distance from geometric centerline to center of mass, d** — 几何中心线到质心的横向距离 `0`（默认）| `scalar`

沿车辆固定 *y* 方向，从几何中心线到质心的横向距离 *d*，单位为 m。正值表示车辆质心位于几何中心线右侧。负值表示车辆质心位于几何中心线左侧。

### **Vertical distance from center of mass to axle plane, h** — 距离 `.35`（默认）| `scalar`

从车辆质心到轴平面的垂直距离 *h*，单位为 m。

车辆俯视图和侧视图，显示载荷位置

### **Longitudinal distance from center of mass to hitch, dh** — 从质心到牵引点的纵向距离 `1`（默认）| `scalar`

从质心到牵引点的纵向距离 *dh*，单位为 m。

车辆俯视图和侧视图，显示载荷位置

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择 **Hitch forces** 或 **Hitch moments**。

### **Longitudinal distance from center of mass to hitch, hl** — 从质心到牵引点的横向距离 `0`（默认）| `scalar`

从质心到牵引点的横向距离 *hl*，单位为 m。

车辆俯视图和侧视图，显示载荷位置

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择 **Hitch forces** 或 **Hitch moments**。

### **Vertical distance from hitch to axle plane, hh** — 从牵引点到轴平面的距离 `0.1`（默认）| `scalar`

从牵引点到轴平面的垂直距离 *hh*，单位为 m。

车辆俯视图和侧视图，显示载荷位置

#### 依赖关系

要启用此参数，请在 **Input signals** 窗格中，选择 **Hitch forces** 或 **Hitch moments**。

### **Initial position in the inertial frame [Xeo,Yeo,Zeo], Xe\_o** — 初始位置 `[0,0,0]`（默认）| `vector`

车辆在惯性坐标系中的初始位置，*Xeo*，单位为 m。

### **Initial velocity in body axes [xdot\_o,ydot\_o,zdot\_o], xbdot\_o** — 初始速度 `[0,0,0]`（默认）| `vector`

车辆质心分别沿车辆固定 *x* 轴、*y* 轴和 *z* 轴的初始速度，单位为 m/s。

### **Initial Euler orientation [roll, pitch, yaw], eul\_o** — 初始欧拉旋转 `[0,0,0]`（默认）| `vector`

车辆固定坐标系分别绕地球固定 *X* 轴（滚转）、*Y* 轴（俯仰）、*Z* 轴（偏航）的初始欧拉旋转，单位为 rad。

### **Initial body rotation rates [p,q,r], p\_o** — 初始旋转速率 `[0,0,0]`（默认）| `vector`

车辆质心分别绕车辆固定 *x* 轴（滚转速率）、*y* 轴（俯仰速率）、*z* 轴（偏航速率）的初始角速度，单位为 rad/s。

### **Chassis inertia tensor, Iveh** — 惯性 `[430 0 0; 0 1900 0; 0 0 2100]`（默认）| `array`

车辆惯性张量，*Iveh*，单位为 kg\*m^2。维度为 `3-by-3`。

### **Track widths [front,rear], w** — 宽度 `[1.9,1.9,1.9]`（默认）| `vector`

前轮距、中轮距和后轮距，分别为 *wf*、*wm* 和 *wr*，单位为 m。维度为 `1-by-3`。

轮距和质心偏离中心线的俯视图。

### 惯性载荷

#### 拖拉机前部

### **Mass, z1m** — 拖拉机前部质量 `0`（默认）| `scalar`

质量，*z1m*，单位为 kg。

### **Distance vector from front axle, z1R** — 拖拉机前部距前轴的距离 `[-.25,.125,.15]`（默认）| `vector`

从前轴到载荷的距离向量，*z1R*，单位为 m。维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z1R(1,1)` | 从前悬架硬点到载荷，沿车辆固定 *x* 轴 |
| `z1R(1,2)` | 从车辆中心线到载荷，沿车辆固定 *y* 轴 |
| `z1R(1,3)` | 从前悬架硬点到载荷，沿车辆固定 *z* 轴 |

例如，下表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 在前轴前方 - 在车辆中心线右侧 - 在前轴悬架硬点上方 | - `z1R(1,1)` < 0 - `z1R(1,2)` > 0 - `z1R(1,3)` > 0 |

### **Inertia tensor, z1I** — 拖拉机前部惯性 `[1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0`（默认）| `array`

惯性张量，*z1I*，单位为 kg·m^2。维度为 `3-by-3`。

z1I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定 *x* 轴
- *y* 轴沿车辆固定 *y* 轴
- *z* 轴沿车辆固定 *z* 轴

#### 驾驶室顶部

### **Mass, z2m** — 驾驶室顶部质量 `0`（默认）| `scalar`

质量，*z2m*，单位为 kg。

### **Distance vector from front axle, z2R** — 驾驶室顶部距前轴的距离 `[1.4,0,.8]`（默认）| `vector`

从前轴到载荷的距离向量，*z2R*，单位为 m。维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z2R(1,1)` | 从前悬架硬点到载荷，沿车辆固定 *x* 轴 |
| `z2R(1,2)` | 从车辆中心线到载荷，沿车辆固定 *y* 轴 |
| `z2R(1,3)` | 从前悬架硬点到载荷，沿车辆固定 *z* 轴 |

例如，下表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 在前轴后方 - 在车辆中心线左侧 - 在前轴悬架硬点上方 | - `z2R(1,1)` > 0 - `z2R(1,2)` < 0 - `z2R(1,3)` > 0 |

### **惯性张量，z2I** — 驾驶室顶部惯性 `[1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0`（默认）| `array`

惯性张量，*z2I*，单位为 kg·m^2。维度为
`3-by-3`。

z2I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

#### 拖拉机车架左侧

### **质量，z3m** — 拖拉机车架左侧质量 `0`（默认）| `scalar`

质量，*z3m*，单位为 kg。

### **距前轴的距离矢量，z3R** — 拖拉机车架左侧距前轴的距离 `[.75,-.5,.4]`（默认）| `vector`

从前轴到载荷的距离矢量，*z3R*，单位为 m。
维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z3R(1,1)` | 从前悬架硬点至载荷，沿车辆固定 *x* 轴 |
| `z3R(1,2)` | 从车辆中心线至载荷，沿车辆固定 *y* 轴 |
| `z3R(1,3)` | 从前悬架硬点至载荷，沿车辆固定 *z* 轴 |

例如，下表总结了用于指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线左侧 - 前轴悬架硬点上方 | - `z3R(1,1)` > 0 - `z3R(1,2)` < 0 - `z3R(1,3)` > 0 |

### **惯性张量，z3I** — 拖拉机车架左侧惯性 `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0`（默认）| `array`

惯性张量，*z3I*，单位为 kg·m^2。维度为
`3-by-3`。

z3I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

#### 拖拉机车架右侧

### **质量，z4m** — 拖拉机车架右侧质量 `0`（默认）| `scalar`

质量，*z4m*，单位为 kg。

### **距前轴的距离矢量，z4R** — 拖拉机车架右侧距前轴的距离 `[.75,.5,.4]`（默认）| `vector`

从前轴到载荷的距离矢量，*z4R*，单位为 m。
维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z4R(1,1)` | 从前悬架硬点至载荷，沿车辆固定 *x* 轴 |
| `z4R(1,2)` | 从车辆中心线至载荷，沿车辆固定 *y* 轴 |
| `z4R(1,3)` | 从前悬架硬点至载荷，沿车辆固定 *z* 轴 |

例如，下表总结了用于指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线右侧 - 前轴悬架硬点上方 | - `z4R(1,1)` > 0 - `z4R(1,2)` > 0 - `z4R(1,3)` > 0 |

### **惯性张量，z4I** — 拖拉机车架右侧惯性 `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0`（默认）| `array`

惯性张量，*z4I*，单位为 kg·m^2。维度为
`3-by-3`。

z4I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

#### 驾驶室左侧

### **质量，z5m** — 驾驶室左侧质量 `0`（默认）| `scalar`

质量，z5m，单位为 kg。

### **距前轴的距离矢量，z5R** — 驾驶室左侧距前轴的距离 `[1.25,-.5,.4]`（默认）| `vector`

从前轴到载荷的距离矢量，*z5R*，单位为 m。
维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z5R(1,1)` | 从前悬架硬点至载荷，沿车辆固定 *x* 轴 |
| `z5R(1,2)` | 从车辆中心线至载荷，沿车辆固定 *y* 轴 |
| `z5R(1,3)` | 从前悬架硬点至载荷，沿车辆固定 *z* 轴 |

例如，下表总结了用于指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线左侧 - 前轴悬架硬点上方 | - `z5R(1,1)` > 0 - `z5R(1,2)` < 0 - `z5R(1,3)` > 0 |

### **Inertia tensor, z5I** — Cab left inertia `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0`（默认）| `array`

惯性张量，*z5I*，单位为 kg·m^2。维度为
`3-by-3`。

z5I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

#### Cab Right

### **Mass, z6m** — Cab right mass `0`（默认）| `scalar`

质量，*z6m*，单位为 kg。

### **Distance vector from front axle, z6R** — Cab right distance from front axle `[1.25,-.5,.4]`（默认）| `vector`

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

### **Inertia tensor, z6I** — Cab right inertia `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0`（默认）| `array`

惯性张量，*z6I*，单位为 kg·m^2。维度为
`3-by-3`。

z6I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

#### Tractor Rear

### **Mass, z7m** — Tractor rear mass `0`（默认）| `scalar`

质量，*z7m*，单位为 kg。

### **Distance vector from front axle, z7R** — Tractor rear mass distance from front axle `[2,0,.25]`（默认）| `vector`

从前轴到载荷的距离向量，*z7R*，单位为 m。
维度为 `1-by-3`。

| 数组元素 | 描述 |
| --- | --- |
| `z7R(1,1)` | 从前悬架硬点至载荷，沿车辆固定 *x* 轴 |
| `z7R(1,2)` | 从车辆中心线至载荷，沿车辆固定 *y* 轴 |
| `z7R(1,3)` | 从前悬架硬点至载荷，沿车辆固定 *z* 轴 |

例如，下表总结了指定载荷位置的参数设置。

| 示例位置 | 符号 |
| --- | --- |
| - 前轴后方 - 车辆中心线右侧 - 前轴悬架硬点上方 | - `z7R(1,1)` > 0 - `z7R(1,2)` > 0 - `z7R(1,3)` > 0 |

### **Inertia tensor, z7I** — Tractor rear inertia `[1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0`（默认）| `array`

惯性张量，*z7I*，单位为 kg·m^2。维度为
`3-by-3`。

z7I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

该张量使用的坐标系原点位于载荷质心。

- *x* 轴沿车辆固定
  *x* 轴
- *y* 轴沿车辆固定
  *y* 轴
- *z* 轴沿车辆固定
  *z* 轴

### Aerodynamic

### **Longitudinal drag area, Af** — Vehicle cross-sectional area `2`（默认）| `scalar`

用于计算车辆气动阻力的有效车辆横截面积，
*Af*，单位为 m^2。

### **Longitudinal drag coefficient, Cd** — Air drag coefficient `.3`（默认）| `scalar`

空气阻力系数，*Cd*，
无量纲。

### **Longitudinal lift coefficient, Cl** — Air lift coefficient `.1`（默认）| `scalar`

空气升力系数，*Cl*，
无量纲。

### **Longitudinal drag pitch moment, Cpm** — Pitch drag `.1`（默认）| `scalar`

纵向阻力俯仰力矩系数，
*Cpm*，
无量纲。

### **Relative wind angle vector, beta\_w** — Wind angle `[0:0.001:0.01]`（默认）| `vector`

相对风角向量，
*βw*，单位为 rad。

### **Side force coefficient vector, Cs** — Side force drag `[0:0.01:0.1]`（默认）| `vector`

侧向力系数向量系数，
*Cs*，
无量纲。

### **横摆力矩系数向量，Cym** — 横摆力矩阻力 `[0:0.001:0.01]`（默认）| `vector`

横摆力矩系数向量系数，
*Cym*，
无量纲。

### 环境

### **绝对空气压力，Pabs** — 压力 `101325`（默认）| `scalar`

环境空气绝对压力，*Pabs*，
单位为 Pa。

### **空气温度，Tair** — 环境空气温度 `273`（默认）| `scalar`

环境空气温度，*Tair*，单位为 K。

#### 依赖关系

要启用此参数，请清除 **空气温度**。

### **重力加速度，g** — 重力 `9.81`（默认）| `scalar`

重力加速度，*g*，单位为 m/s^2。

### 仿真

### **纵向速度容差，xdot\_tol** — 容差 `.1`（默认）| `scalar`

纵向速度容差，
*xdottol*，单位为
m/s。

当模块计算车身侧偏角 *β* 时，使用此参数来避免除以零。

### **距轴平面的几何纵向偏移，longOff** — 纵向偏移 `0`（默认）| `scalar`

车辆底盘沿车身固定
*x* 轴距轴平面的偏移，单位为 m。当您使用 3D 可视化
引擎时，可考虑使用该偏移来独立于车辆 CG 定位底盘。

### **距中心平面的几何横向偏移，latOff** — 横向偏移 `0`（默认）| `scalar`

车辆底盘沿车身固定
*y* 轴距中心平面的偏移，单位为 m。当您使用 3D 可视化
引擎时，可考虑使用该偏移来独立于车辆 CG 定位底盘。

### **距轴平面的几何垂向偏移，vertOff** — 垂向偏移 `0`（默认）| `scalar`

车辆底盘沿车身固定
*z* 轴距轴平面的偏移，单位为 m。当您使用 3D 可视化
引擎时，可考虑使用该偏移来独立于车辆 CG 定位底盘。

### **包裹欧拉角，wrapAng** — 选择 `on`（默认）| `off`

将欧拉角包裹到区间 `[-pi, pi]`。
对于可能经历超出该区间的车辆横摆旋转的车辆机动，如果您希望：

- 跟踪总车辆横摆旋转。
- 避免车辆状态
  估计器中的不连续性。

可考虑清除该参数。
## 所属库

Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

三轴车辆牵引车车身，具有平移和旋转运动

Vehicle Body 6DOF Three Axles 模块实现了一个六自由度（DOF）刚性三轴车辆车身模型，用于计算纵向、横向、垂向、俯仰、侧倾和横摆运动。使用该模块对三轴车辆（如牵引车）进行建模。该模块考虑了车身质量、惯性、气动阻力、道路坡度以及由于悬架和外部力与力矩在车轴硬点位置之间的重量分配。使用 **Inertial Loads** 参数来分析不同载荷条件下的车辆动力学。

将该模块连接到虚拟传感器、悬架系统或外部系统（如车身控制执行器）。在平顺性和操纵性研究中使用 Vehicle Body 6DOF Three Axles 模块，以对阻力、乘客载荷和悬架硬点位置的影响进行建模。

要创建额外的输入端口，请在 **Input signals** 下选择以下模块参数。

| 参数 | 输入端口 | 描述 |
| --- | --- | --- |
| **Front hitch forces** | `FhF` | 施加在车身前挂钩位置的挂钩力，*FhFx*、*FhFy* 和 *FhFz*，在车辆固定坐标系中 |
| **Front hitch moments** | `MhF` | 前挂钩位置的挂钩力矩，*MhFx*、*MhFy* 和 *MhFz*，关于车辆固定坐标系 |
| **Rear hitch forces** | `FhR` | 施加在车身后挂钩位置的挂钩力，*FhRx*、*FhRy* 和 *FhRz*，在车辆固定坐标系中 |
| **Rear hitch moments** | `MhR` | 后挂钩位置的挂钩力矩，*MhRx*、*MhRy* 和 *MhRz*，关于车辆固定坐标系 |

### 惯性载荷

为了分析不同加载条件下的车辆动力学，请使用 **Inertial Loads** 参数。您可以指定以下载荷：

- 拖拉机前部
- 驾驶室顶部
- 拖拉机车架左侧和车架右侧
- 驾驶室左侧和驾驶室右侧
- 拖拉机后部

对于每个载荷，您可以指定质量、位置和惯性。

这些图示给出了载荷位置和车辆参数尺寸。该表给出了相应的位置参数符号设置。

显示载荷位置的车辆俯视图和侧视图

此表总结了用于指定由点表示的载荷位置的参数设置。对于位置，该模块使用以下距离向量：

- 从前轴到载荷，沿车辆固定的 *x* 轴
- 从车辆中心线到载荷，沿车辆固定的 *y* 轴
- 从前轴到载荷，沿车辆固定的 *z* 轴

| 载荷 | 参数 | 示例位置 |
| --- | --- | --- |
| 拖拉机前部 | **Distance vector from front axle, z1R** | - `z1R(1,1)<0` — 前轴前方 - `z1R(1,2)>0` — 车辆中心线右侧 - `z1R(1,3)>0` — 前轴悬架硬点上方 |
| 驾驶室顶部 | **Distance vector from front axle, z2R** | - `z2R(1,1)>0` — 前轴后方 - `z2R(1,2)<0` — 车辆中心线左侧 - `z2R(1,3)>0` — 前轴悬架硬点上方 |
| 拖拉机车架左侧 | **Distance vector from front axle, z3R** | - `z3R(1,1)>0` — 前轴后方 - `z3R(1,2)<0` — 车辆中心线左侧 - `z3R(1,3)>0` — 前轴悬架硬点上方 |
| 拖拉机车架右侧 | **Distance vector from front axle, z4R** | - `z4R(1,1)>0` — 前轴后方 - `z4R(1,2)>0` — 车辆中心线右侧 - `z4R(1,3)>0` — 前轴悬架硬点上方 |
| 驾驶室左侧 | **Distance vector from front axle, z5R** | - `z5R(1,1)>0` — 前轴后方 - `z5R(1,2)<0` — 车辆中心线左侧 - `z5R(1,3)>0` — 前轴悬架硬点上方 |
| 驾驶室右侧 | **Distance vector from front axle, z6R** | - `z6R(1,1)>0` — 前轴后方 - `z6R(1,2)>0` — 车辆中心线右侧 - `z6R(1,3)>0` — 前轴悬架硬点上方 |
| 拖拉机后部 | **Distance vector from front axle, z7R** | - `z7R(1,1)>0` — 前轴后方 - `z7R(1,2)>0` — 车辆中心线右侧 - `z7R(1,3)>0` — 前轴悬架硬点上方 |

### 运动方程

为确定车辆运动，该模块实现了刚体车辆动力学、风阻、惯性载荷和坐标变换的计算。体坐标系与车辆坐标系相同。

该模块考虑体坐标系相对于平坦大地固定惯性参考系的旋转。体坐标系的原点是车身的车辆重心。

该模块使用此方程计算体坐标系的平移运动，其中施加的力 [*Fx Fy Fz*]T 位于体坐标系中，且假设车身质量 *m* 为常数。

F¯b=[FxFyFz]=m(V¯˙b+ω¯×V¯b)M¯b=[LMN]=Iω¯˙+ω¯×(Iω¯)I=[Ixx−Ixy−Ixz−IyxIyy−Iyz−Izx−IzyIzz]

为确定体坐标系角速度矢量 [*p q r*]T 与欧拉角变化率 [ϕ˙  θ˙   ψ˙]T 之间的关系，该模块将欧拉角速率分解到体坐标系中。

[pqr]=[ϕ˙00]+[1000cosϕsinϕ0−sinϕcosϕ][0θ˙0]+[1000cosϕsinϕ0−sinϕcosϕ][cosθ0−sinθ010sinθ0cosθ][00ψ˙]≡J−1[ϕ˙θ˙ψ˙]

对 *J* 求逆可得到确定欧拉角速率矢量所需的关系。

[ϕ˙θ˙ψ˙]=J[pqr] =[1(sinϕtanθ)(cosϕtanθ)0cosϕ−sinϕ0sinϕcosθcosϕcosθ][pqr]

施加的力和力矩是阻力、重力、外力和悬架力之和。

F¯b=[FxFyFz]=[FdxFdyFdz]+[FgxFgyFgz]+[FextxFextyFextz]+[FFLxFFLyFFLz]+[FFRxFFRyFFRz]+[FMLxFMLyFMLz]+[FMRxFMRyFMRz]+[FRLxFRLyFRLz]+[FRRxFRRyFRRz]M¯b=[MxMyMz]=[MdxMdyMdz]+[MextxMextyMextz]+[MFLxMFLyMFLz]+[MFRxMFRyMFRz]+[MMLxMMLyMMLz]+[MMRxMMRyMMRz]+[MRLxMRLyMRLz]+[MRRxMRRyMRRz]+M¯F

| 计算 | 实现 |
| --- | --- |
| 载荷质量和惯量 | 该模块使用平行轴定理，将各个载荷的质量和惯量与车辆质量和惯量进行合成。  Jij=Iij+m(|R|2δij−RiRj) |
| 重力，*Fg* | 该模块使用方向余弦矩阵 (DCM) 将惯性固定坐标系中的重力矢量变换到体坐标系。 |
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
| *FFLx*, *FFLy*, *FFLz* | 施加在前左硬点上的悬架力沿车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *FFRx*, *FFRy*, *FFRz* | 施加在前右硬点上的悬架力沿车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *FMLx*, *FMLy*, *FMLz* | 施加在中左硬点上的悬架力沿车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *FMRx*, *FMRy*, *FMRz* | 施加在中右硬点上的悬架力沿车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *FRLx*, *FRLy*, *FRLz* | 施加在后左硬点上的悬架力沿车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *FRRx*, *FRRy*, *FRRz* | 施加在后右硬点上的悬架力沿车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *MFLx*, *MFLy*, *MFLz* | 施加在前左硬点上的悬架力矩绕车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *MFRx*, *MFRy*, *MFRz* | 施加在前右硬点上的悬架力矩绕车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *MMLx*, *MMLy*, *MMLz* | 施加在中左硬点上的悬架力矩绕车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *MMRx*, *MMRy*, *MMRz* | 施加在中右硬点上的悬架力矩绕车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *MRLx*, *MRLy*, *MRLz* | 施加在后左硬点上的悬架力矩绕车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *MRRx*, *MRRy*, *MRRz* | 施加在后右硬点上的悬架力矩绕车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *Fextx*, *Fexty*, *Fextz* | 施加在车辆质心上的外力沿车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *Fdx*, *Fdy*, *Fdz* | 施加在车辆质心上的阻力沿车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *Mextx*, *Mexty*, *Mextz* | 绕车辆质心的外力矩绕车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *Mdx*, *Mdy*, *Mdz* | 绕车辆质心的阻力矩绕车辆固定 *x*、*y* 和 *z* 轴的分量 |
| *I* | 车体转动惯量 |
| *a*, *b*, *c* | 前轴、中轴和后轴分别距车辆质心在公共轴平面上的法向投影点的距离 |
| *h* | 车辆质心在轴平面上方的高度 |
| *d* | 沿车辆固定 *y* 轴从几何中心线到质心的横向距离 |
| *hh\_f*, *hh\_r* | 前挂钩和后挂钩分别沿车辆固定 *z* 轴在轴平面上方的高度 |
| *dh\_f*, *dh\_r* | 前挂钩和后挂钩分别距车辆质心在公共轴平面上的法向投影点的纵向距离 |
| *hl\_f*, *hl\_r* | 分别沿车辆固定 *y* 轴从质心到前挂钩和后挂钩的横向距离 |
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
