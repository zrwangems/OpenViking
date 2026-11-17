---
type: simulink-block
title: 'Transform Sensor'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Frames and Transforms'
documentation_page: 'transformsensor'
documentation_source_path: 'ref/transformsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Transform Sensor

## 端口
```yaml
ports:
- name: B
  summary: 基础坐标系 坐标系
  direction: output
- name: F
  summary: 从动坐标系 坐标系
  direction: output
- name: q
  summary: 旋转角度，rad 物理信号
  direction: output
- name: axs
  summary: 旋转轴，无量纲 物理信号
  direction: output
- name: Q
  summary: 四元数，无量纲 物理信号
  direction: output
- name: R
  summary: 旋转矩阵，无量纲 物理信号
  direction: output
- name: seq
  summary: 三次连续旋转的角度，rad 物理信号
  direction: output
- name: wx
  summary: 相对角速度的 *X* 分量，rad/s 物理信号
  direction: output
- name: wy
  summary: 相对角速度的 *Y* 分量，rad/s 物理信号
  direction: output
- name: wz
  summary: 相对角速度的 *Z* 分量，rad/s 物理信号
  direction: output
- name: w
  summary: 相对角速度，rad/s 物理信号
  direction: output
- name: Qd
  summary: 以四元数时间导数表示的相对角速度，无量纲物理信号
  direction: output
- name: Rd
  summary: 以旋转矩阵时间导数表示的相对角速度，无量纲物理信号
  direction: output
- name: seqd
  summary: 以旋转序列角时间导数表示的相对角速度，rad/s 物理信号
  direction: output
- name: bx
  summary: 相对角加速度的 *X* 分量，rad/s^2 物理信号
  direction: output
- name: by
  summary: 相对角加速度的 *Y* 分量，rad/s^2 物理信号
  direction: output
- name: bz
  summary: 相对角加速度的 *Z* 分量，rad/s^2 物理信号
  direction: output
- name: b
  summary: 相对角加速度，rad/s^2 物理信号
  direction: output
- name: Qdd
  summary: 以四元数二阶时间导数表示的相对角加速度，无量纲物理信号
  direction: output
- name: Rdd
  summary: 以旋转矩阵二阶时间导数表示的相对角加速度，无量纲物理信号
  direction: output
- name: x
  summary: 相对平移的 *X* 分量，m 物理信号
  direction: output
- name: y
  summary: 相对平移的 *Y* 分量，m 物理信号
  direction: output
- name: z
  summary: 相对平移的 *Z* 分量，m 物理信号
  direction: output
- name: p
  summary: 相对平移，m 物理信号
  direction: output
- name: rad
  summary: 相对平移的圆柱半径坐标，m 物理信号
  direction: output
- name: azm
  summary: 相对平移的方位角，rad 物理信号
  direction: output
- name: dst
  summary: 相对平移的球半径坐标，m 物理信号
  direction: output
- name: inc
  summary: 相对平移的倾角，rad 物理信号
  direction: output
- name: vx
  summary: 相对线速度的 *X* 坐标，m/s 物理信号
  direction: output
- name: vy
  summary: 相对线速度的 *Y* 坐标，m/s 物理信号
  direction: output
- name: vz
  summary: 相对线速度的 *Z* 坐标，m/s 物理信号
  direction: output
- name: v
  summary: 相对线速度，m/s 物理信号
  direction: output
- name: vrad
  summary: 相对线速度的柱坐标半径坐标，m/s 物理信号
  direction: output
- name: vazm
  summary: 相对线速度的方位角坐标，rad/s 物理信号
  direction: output
- name: vdst
  summary: 相对线速度的球坐标半径坐标，m/s 物理信号
  direction: output
- name: vinc
  summary: 相对线速度的倾角坐标，rad/s 物理信号
  direction: output
- name: ax
  summary: 相对线加速度的 *X* 分量，m/s^2 物理信号
  direction: output
- name: ay
  summary: 相对线加速度的 *Y* 分量，m/s^2 物理信号
  direction: output
- name: az
  summary: 相对线加速度的 *Z* 分量，m/s^2 物理信号
  direction: output
- name: a
  summary: 相对线加速度，m/s^2 物理信号
  direction: output
- name: arad
  summary: 相对线加速度的柱面半径坐标，m/s^2 物理信号
  direction: output
- name: aazm
  summary: 相对线加速度的方位角坐标，rad/s^2 物理信号
  direction: output
- name: adst
  summary: 相对线加速度的球面半径坐标，m/s^2 物理信号
  direction: output
- name: ainc
  summary: 相对线加速度的倾角坐标，rad/s^2 物理信号
  direction: output
```

### 坐标系

### **B** — 基础坐标系 坐标系

与基础坐标系关联的坐标系端口。

### **F** — 从动坐标系 坐标系

与从动坐标系关联的坐标系端口。
### 输出

### **q** — 旋转角度，rad 物理信号

旋转角度，以标量形式返回。该角度表示从动坐标系相对于基础坐标系绕端口 **axs** 输出的向量所指定轴的旋转。角度范围为 [0, π]。

使用端口 **q** 和 **axs** 以轴角参数化方式输出旋转信号。有关详细信息，请参阅 Rotational Measurements。**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Rotation** 下选择 **Angle**。

### **axs** — 旋转轴，无量纲 物理信号

旋转轴，以 3×1 单位向量形式返回。使用端口 **q** 和 **axs** 以轴角参数化方式输出旋转信号。

**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Rotation** 下选择 **Axis**。

### **Q** — 四元数，无量纲 物理信号

相对旋转，以四元数形式返回。有关四元数的详细信息，请参阅 Rotational Measurements。

**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Rotation** 下选择 **Quaternion**。

### **R** — 旋转矩阵，无量纲 物理信号

相对旋转，以 3×3 矩阵形式返回。有关旋转矩阵的详细信息，请参阅 Rotational Measurements。**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Rotation** 下选择 **Transform**。

### **seq** — 三次连续旋转的角度，rad 物理信号

相对旋转，以 3×1 向量形式返回。该向量包含表示从动坐标系相对于基础坐标系旋转的三次连续基本旋转的角度。

这三次旋转围绕一个中间坐标系进行，可以是 12 种不同旋转序列之一。有关旋转序列测量的详细信息，请参阅 Rotational Measurements。**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Rotation** 下选择 **Rotation Sequence**。

### **wx** — 相对角速度的 *X* 分量，rad/s 物理信号

两个坐标系之间相对角速度的 *X* 分量，以标量形式返回。**Measurement Frame** 参数的设置影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Velocity** 下选择 **Omega X**。

### **wy** — 相对角速度的 *Y* 分量，rad/s 物理信号

两个坐标系之间相对角速度的 *Y* 分量，以标量形式返回。**Measurement Frame** 参数的设置影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Velocity** 下选择 **Omega Y**。

### **wz** — 相对角速度的 *Z* 分量，rad/s 物理信号

两个坐标系之间相对角速度的 *Z* 分量，以标量形式返回。**Measurement Frame** 参数的设置影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Velocity** 下选择 **Omega Z**。

### **w** — 相对角速度，rad/s 物理信号

从动坐标系相对于基础坐标系的角速度，以 3×1 向量形式返回。**Measurement Frame** 参数的设置影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Velocity** 下选择 **Omega XYZ**。

### **Qd** — 以四元数时间导数表示的相对角速度，无量纲物理信号

相对角速度，返回为 4×1 向量，等于端口 **Q** 信号的时间导数。**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Velocity** 下选择 **Quaternion**。

### **Rd** — 以旋转矩阵时间导数表示的相对角速度，无量纲物理信号

相对角速度，返回为 3×3 矩阵。该矩阵等于端口 **R** 信号的时间导数。**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Velocity** 下选择 **Transform**。

### **seqd** — 以旋转序列角时间导数表示的相对角速度，rad/s 物理信号

相对角速度，返回为 3×1 向量。该向量等于端口 **seq** 输出的时间导数。**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Velocity** 下选择 **Rotation Sequence**。

### **bx** — 相对角加速度的 *X* 分量，rad/s^2 物理信号

两个坐标系之间相对角加速度的 *X* 分量，返回为标量。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Acceleration** 下选择 **Alpha X**。

### **by** — 相对角加速度的 *Y* 分量，rad/s^2 物理信号

两个坐标系之间相对角加速度的 *Y* 分量，返回为标量。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Acceleration** 下选择 **Alpha Y**。

### **bz** — 相对角加速度的 *Z* 分量，rad/s^2 物理信号

两个坐标系之间相对角加速度的 *Z* 分量，返回为标量。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Acceleration** 下选择 **Alpha Z**。

### **b** — 相对角加速度，rad/s^2 物理信号

从动坐标系相对于基础坐标系的角加速度，返回为 3×1 向量。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Acceleration** 下选择 **Alpha XYZ**。

### **Qdd** — 以四元数二阶时间导数表示的相对角加速度，无量纲物理信号

相对角加速度，返回为 4×1 向量。**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Acceleration** 下选择 **Quaternion**。

### **Rdd** — 以旋转矩阵二阶时间导数表示的相对角加速度，无量纲物理信号

相对角加速度，返回为 3×3 矩阵。**Measurement Frame** 参数的设置不影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Angular Acceleration** 下选择 **Transform**。

### **x** — 相对平移的 *X* 分量，m 物理信号

两个坐标系之间相对平移的 *X* 分量，返回为标量。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Translation** 下选择 **X**。

### **y** — 相对平移的 *Y* 分量，m 物理信号

两个坐标系之间相对平移的 *Y* 分量，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Translation** 下选择 **Y**。

### **z** — 相对平移的 *Z* 分量，m 物理信号

两个坐标系之间相对平移的 *Z* 分量，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达。

由于笛卡尔坐标系和圆柱坐标系都有 *z* 轴，Transform Sensor 模块对这两种坐标系只有一个输出端口。

#### 依赖关系

要启用此端口，请在 **Translation** 下选择 **Z**。

### **p** — 相对平移，m 物理信号

从动坐标系相对于基础坐标系的平移，以笛卡尔坐标系表示的 3×1 向量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Translation** 下选择 **XYZ**。

### **rad** — 相对平移的圆柱半径坐标，m 物理信号

相对平移向量的圆柱半径坐标，以非负标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Translation** 下选择 **Radius**。

### **azm** — 相对平移的方位角，rad 物理信号

相对平移向量的方位角，以标量形式返回。该角度落在 [-π, π) 范围内。如果基础坐标系和从动坐标系的原点重合，则方位角未定义。**Measurement Frame** 参数的设置会影响该信号的表达。

由于方位角同时存在于圆柱坐标系和球坐标系中，Transform Sensor 模块对这两种坐标系只有一个输出端口。

#### 依赖关系

要启用此端口，请在 **Translation** 下选择 **Azimuth**。

### **dst** — 相对平移的球半径坐标，m 物理信号

相对平移向量的球半径坐标，以标量形式返回。该值等于基础坐标系和从动坐标系原点之间的距离。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Translation** 下选择 **Distance**。

### **inc** — 相对平移的倾角，rad 物理信号

以球坐标系表示的相对平移向量的倾角，以标量形式返回。该角度落在 [-π/2, π/2] 范围内。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Translation** 下选择 **Inclination**。

### **vx** — 相对线速度的 *X* 坐标，m/s 物理信号

两个坐标系之间相对线速度的 *X* 分量，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Velocity** 下选择 **X**。

### **vy** — 相对线速度的 *Y* 坐标，m/s 物理信号

两个坐标系之间相对线速度的 *Y* 分量，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达。

#### 依赖关系

要启用此端口，请在 **Velocity** 下选择 **Y**。

### **vz** — 相对线速度的 *Z* 坐标，m/s 物理信号

两个坐标系之间相对线速度的 *Z* 分量，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

由于笛卡尔坐标系和柱坐标系都有 *z* 轴，Transform Sensor 模块对这两种坐标系只有一个输出端口。

#### 依赖关系

要启用此端口，请在 **Velocity** 下选择 **Z**。

### **v** — 相对线速度，m/s 物理信号

从动坐标系相对于基础坐标系的线速度，以笛卡尔坐标系表示的 3×1 向量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

#### 依赖关系

要启用此端口，请在 **Velocity** 下选择 **XYZ**。

### **vrad** — 相对线速度的柱坐标半径坐标，m/s 物理信号

相对线速度的柱坐标半径坐标，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

#### 依赖关系

要启用此端口，请在 **Velocity** 下选择 **Radius**。

### **vazm** — 相对线速度的方位角坐标，rad/s 物理信号

相对线速度的方位角坐标，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

由于方位角坐标同时存在于柱坐标系和球坐标系中，Transform Sensor 模块对这两种坐标系只有一个输出端口。

#### 依赖关系

要启用此端口，请在 **Velocity** 下选择 **Azimuth**。

### **vdst** — 相对线速度的球坐标半径坐标，m/s 物理信号

相对线速度的球坐标半径坐标，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

#### 依赖关系

要启用此端口，请在 **Velocity** 下选择 **Distance**。

### **vinc** — 相对线速度的倾角坐标，rad/s 物理信号

相对线速度的倾角坐标，以球坐标系表示，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

#### 依赖关系

要启用此端口，请在 **Velocity** 下选择 **Inclination**。

### **ax** — 相对线加速度的 *X* 分量，m/s^2 物理信号

两个坐标系之间相对线加速度的 *X* 分量，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

#### 依赖关系

要启用此端口，请在 **Acceleration** 下选择 **X**。

### **ay** — 相对线加速度的 *Y* 分量，m/s^2 物理信号

两个坐标系之间相对线加速度的 *Y* 分量，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

#### 依赖关系

要启用此端口，请在 **Acceleration** 下选择 **Y**。

### **az** — 相对线加速度的 *Z* 分量，m/s^2 物理信号

两个坐标系之间相对线加速度的 *Z* 分量，以标量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

由于笛卡尔坐标系和柱坐标系都有 *z* 轴，Transform Sensor 模块对这两种坐标系只有一个输出端口。

#### 依赖关系

要启用此端口，请在 **Acceleration** 下选择 **Z**。

### **a** — 相对线加速度，m/s^2 物理信号

从动坐标系相对于基础坐标系的线加速度，以笛卡尔坐标系表示的 3×1 向量形式返回。**Measurement Frame** 参数的设置会影响该信号的表达式。

#### 依赖关系

要启用此端口，请在 **Acceleration** 下选择
**XYZ**。

### **arad** — 相对线加速度的柱面半径坐标，m/s^2 物理信号

相对线加速度的柱面半径坐标，以标量形式返回。**Measurement Frame** 参数的设置会影响此信号的表达式。

#### 依赖关系

要启用此端口，请在 **Acceleration** 下选择
**Radius**。

### **aazm** — 相对线加速度的方位角坐标，rad/s^2 物理信号

相对线加速度的方位角坐标，以标量形式返回。**Measurement Frame** 参数的设置会影响此信号的表达式。

由于方位角坐标同时存在于柱面和球面坐标系中，Transform Sensor 模块对两种坐标系只有一个输出端口。

#### 依赖关系

要启用此端口，请在 **Acceleration** 下选择
**Azimuth**。

### **adst** — 相对线加速度的球面半径坐标，m/s^2 物理信号

相对线加速度的球面半径坐标，以标量形式返回。**Measurement Frame** 参数的设置会影响此信号的表达式。

#### 依赖关系

要启用此端口，请在 **Acceleration** 下选择
**Distance**。

### **ainc** — 相对线加速度的倾角坐标，rad/s^2 物理信号

相对线加速度的倾角坐标，以球面坐标系表示，指定为标量。**Measurement Frame** 参数的设置会影响此信号的表达式。

#### 依赖关系

要启用此端口，请在 **Acceleration** 下选择
**Inclination**。
## 参数
```yaml
parameters:
- name: Measurement Frame
  summary: 用于表达测量值的坐标系 World（默认）| Base | Follower | Non-Rotating Base | Non-Rotating Follower
  group: ''
- name: Sequence for Rotation Sequence
  summary: 旋转轴序列 X-Y-X（默认）| X-Y-Z | X-Z-X | X-Z-Y | Y-X-Y | Y-X-Z | Y-Z-X | Y-Z-Y | Z-X-Y | Z-X-Z | Z-Y-X | Z-Y-Z
  group: ''
```

### **Measurement Frame** — 用于表达测量值的坐标系 `World`（默认）| `Base` | `Follower` | `Non-Rotating Base` | `Non-Rotating Follower`

用于指定如何表达以及从何处观测所测量量的坐标系。此参数的设定不影响旋转量。

**测量坐标系类型**

| 测量坐标系 | 描述 |
| --- | --- |
| `World` | 世界坐标系是一个惯性坐标系。 |
| `Base` | Transform Sensor 模块的基础坐标系。它是一个非惯性坐标系。 |
| `Follower` | Transform Sensor 模块的从动坐标系。它是一个非惯性坐标系。 |
| `Non-Rotating Base` | 非旋转基础坐标系是一个惯性坐标系，始终与 Transform Sensor 模块的基础坐标系瞬时重合。 |
| `Non-Rotating Follower` | 非旋转从动坐标系是一个惯性坐标系，始终与 Transform Sensor 模块的从动坐标系瞬时重合。 |

非旋转基础坐标系和非旋转从动坐标系并非在空间中移动并随时间存在的实际坐标系。因此，在非旋转坐标系中表达的测量值不支持标准导数关系。如果模块使用非旋转坐标系作为测量坐标系，则所表达的加速度测量值通常不涉及向心项和科里奥利项。

### **Sequence for Rotation Sequence** — 旋转轴序列 `X-Y-X`（默认）| `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

三次连续基本旋转的旋转轴序列。有关更多信息，请参阅 Rotation Sequence Measurements。

#### 依赖关系

要启用此参数，请在 **Rotation** 下选择
**Rotation Sequence**。
## 所属库

Simscape / Multibody / Frames and Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

测量两个坐标系之间相对空间关系的传感器

Transform Sensor 模块测量连接到该模块端口 **F** 和 **B** 的坐标系之间的相对空间关系。所测量的量包括相对位姿、速度和加速度，这些是随时间变化的物理信号。

您可以通过将模块的坐标系端口 **F** 和 **B** 分别连接到该坐标系和模型的世界坐标系，来测量某个坐标系的绝对平移量或旋转量。

模块的默认单位是米-千克-秒或 MKS（SI）。您可以使用 Simulink-PS Converter 或 PS-Simulink Converter 模块分别指定输入或输出信号的单位。

### 测量坐标系

测量坐标系是：

- 用于表示所测量量的坐标系。
- 观测者观察所测量量如何随时间变化的位置。

测量坐标系的选择不影响旋转量。要查看某个特定量是否受影响，请参阅输出部分。

Transform Sensor 模块的 **Measurement Frame** 参数有五个不同选项。有关这些选项的详细信息，请参阅参数部分中的 **Measurement Frame** 参数。

### Rotational and Translational Measurements

该模块有四种参数化方式来表示测量到的旋转：角轴、四元数、旋转矩阵和旋转序列。要启用这些参数化方式，请在模块对话框中，在 **Rotation** 下选择相应的参数。
例如，选择 **Angle** 和 **Axis** 参数以使用角轴参数化，或选择 **Quaternion**、**Transform** 或 **Rotation Sequence** 参数以使用四元数、旋转矩阵或旋转序列参数化。

此外，该模块有多种参数化方式来表示旋转速度和加速度：*x-*、*y-* 和 *z-* 坐标；四元数或旋转序列的时间导数；或矩阵。要启用这些参数化方式，您可以在 **Angular Velocity** 或 **Angular Acceleration** 下选择相应的参数。有关详细信息，请参阅 Rotational Measurements。

该模块有三种坐标系来表示平移测量：笛卡尔、圆柱和球面。您可以同时选择其中一种或多种。有关详细信息，请参阅 Translational Measurements。

这些表格总结了三种坐标系的坐标，图像显示了这些坐标系的示意图。为简单起见，在图像中，将 **Measurement Frame** 参数指定为 `Base`。

**笛卡尔坐标**

| 坐标 | 描述 |
| --- | --- |
| **X** | 向量 `BF` 在测量坐标系 *x* 轴上的投影。 |
| **Y** | 向量 `BF` 在测量坐标系 *y* 轴上的投影。 |
| **Z** | 向量 `BF` 在测量坐标系 *z* 轴上的投影。 |

笛卡尔坐标系

**圆柱坐标**

| 坐标 | 描述 |
| --- | --- |
| **Radius** | 向量 `BF` 在测量坐标系 *x-y* 平面上的投影长度。 |
| **Azimuth** | `Radius` 相对于测量坐标系正 *x* 轴的角度。该角度落在 [-π, π) 范围内。 |
| **Z** | 向量 `BF` 在测量坐标系 *z* 轴上的投影。 |

圆柱坐标系

**球面坐标**

| 坐标 | 描述 |
| --- | --- |
| **Distance** | 基座坐标系与从动坐标系原点之间的距离。 |
| **Azimuth** | 向量 `BF` 在 *x-y* 平面上的投影相对于正 *x* 轴的角度。该角度在测量坐标系中解析，并落在 [-π, π) 范围内。 |
| **Inclination** | 向量 `BF` 相对于测量坐标系 *x-y* 平面的角度。该角度落在 [-π/2, π/2] 范围内。 |

球面坐标系

要使用特定坐标系，请选择相应的参数。例如，如果您想使用笛卡尔坐标系来表示测量到的从动坐标系相对线速度，请在 **Velocity** 下选择 **X**、**Y** 和 **Z** 参数。
