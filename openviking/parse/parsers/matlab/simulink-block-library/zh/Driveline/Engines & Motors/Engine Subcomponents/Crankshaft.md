---
type: simulink-block
title: 'Crankshaft'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'crankshaft'
documentation_source_path: 'ref/crankshaft.html'
language: zh-CN
chinese_source: worker-translation
---

# Crankshaft

## 端口
```yaml
ports:
- name: CylPwr
  summary: 气缸功率数组物理信号
  direction: input
- name: CylPwr1
  summary: 气缸 1 功率物理信号
  direction: input
- name: CylPwr2
  summary: 气缸 2 功率物理信号
  direction: input
- name: CylPwr3
  summary: 气缸 3 功率物理信号
  direction: input
- name: CylPwr4
  summary: 气缸 4 功率物理信号
  direction: input
- name: CrkPos
  summary: 曲柄位置，deg 物理信号
  direction: output
- name: Spd
  summary: 发动机转速，rad/s 物理信号
  direction: output
- name: AvrSpd
  summary: 循环平均曲柄转速，rad/s 物理信号
  direction: output
- name: AvrTrq
  summary: 循环平均净指示曲柄扭矩，N\*m 物理信号
  direction: output
- name: Trq
  summary: 瞬时净指示曲柄扭矩，N\*m 物理信号
  direction: output
- name: F
  summary: 曲轴机械旋转
  direction: output
```

### 输入

### **CylPwr** — 气缸功率数组物理信号

当模块作为子组件运行时，与气缸功率相关联的物理信号输入。

#### 依赖关系

要启用此端口，请清除 **Input power separately**。

### **CylPwr1** — 气缸 1 功率物理信号

与来自气缸 1 的功率相关联的物理信号输入。

#### 依赖关系

要启用此端口，请选择 **Input power separately**。

### **CylPwr2** — 气缸 2 功率物理信号

与来自气缸 2 的功率相关联的物理信号输入。

#### 依赖关系

要启用此端口，请将 **Number of cylinders** 设置为 `Two
Cylinders`、`Three
Cylinders` 或 `Four
Cylinders`，并选择 **Input power
separately**。

### **CylPwr3** — 气缸 3 功率物理信号

与来自气缸 3 的功率相关联的物理信号输入。

#### 依赖关系

要启用此端口，请将 **Number of cylinders** 设置为 `Three
Cylinders` 或 `Four
Cylinders`，并选择 **Input power
separately**。

### **CylPwr4** — 气缸 4 功率物理信号

与来自气缸 4 的功率相关联的物理信号输入。

#### 依赖关系

要启用此端口，请将 **Number of cylinders** 设置为 `Four
Cylinders`，并选择 **Input power
separately**。
### 输出

### **CrkPos** — 曲柄位置，deg 物理信号

与曲柄位置相关联的物理信号输出，以度为单位。

### **Spd** — 发动机转速，rad/s 物理信号

与发动机转速相关联的物理信号输出，以 rad/s 为单位。

### **AvrSpd** — 循环平均曲柄转速，rad/s 物理信号

与循环平均曲柄转速相关联的物理信号输出，以 rad/s 为单位。

### **AvrTrq** — 循环平均净指示曲柄扭矩，N\*m 物理信号

与循环平均净指示曲柄扭矩相关联的物理信号输出，以
Nm 为单位。

### **Trq** — 瞬时净指示曲柄扭矩，N\*m 物理信号

与瞬时净指示曲柄扭矩相关联的物理信号输出，以
Nm 为单位。
### 守恒

### **F** — 曲轴机械旋转

与曲轴从动端相关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Initial crank position, ca0 (0-720 CAdeg)
  summary: 仿真开始时的曲柄位置 0 deg（默认）| 范围 [0,720) 内的非负标量
  group: 机械
- name: Number of cylinders
  summary: 气缸总数 Single Cylinder（默认）| Two Cylinders | Three Cylinders | Four Cylinders
  group: 机械
- name: Input power separately
  summary: 功率输入选项 on（默认）| off
  group: 机械
- name: Spark angle difference
  summary: 双缸发动机火花角相位 270 deg（默认）| 正标量
  group: 机械
- name: Firing order
  summary: 四缸发动机的点火顺序 1-3-4-2（默认）| 1-3-2-4
  group: 机械
- name: Threshold to avoid divide-by-zero
  summary: 发动机转速阈值 0.1 rad/s（默认）
  group: 仿真
- name: Cycle-average speed
  summary: 输出循环平均转速的选项 on（默认）| off
  group: 输出
- name: Cycle-average net indicated torque
  summary: 输出循环平均净指示扭矩的选项 on（默认）| off
  group: 输出
- name: Instantaneous net indicated torque
  summary: 输出瞬时净指示扭矩的选项 on（默认）| off
  group: 输出
```

### 机械

### **Initial crank position, ca0 (0-720 CAdeg)** — 仿真开始时的曲柄位置 `0` `deg`（默认）| 范围 [0,720) 内的非负标量

初始曲柄位置。

### **Number of cylinders** — 气缸总数 `Single Cylinder`（默认）| `Two Cylinders` | `Three Cylinders` | `Four Cylinders`

火花点火气缸的数量。

### **Input power separately** — 功率输入选项 `on`（默认）| `off`

是将功率作为数组输入，还是为每个燃烧气缸分配各自的端口。

### **Spark angle difference** — 双缸发动机火花角相位 `270` `deg`（默认）| 正标量

双缸发动机的火花角差值。此值因发动机而异。

#### 依赖关系

要启用此参数，请将 **Number of
cylinders** 设置为 `Two
Cylinders`。

### **Firing order** — 四缸发动机的点火顺序 `1-3-4-2`（默认）| `1-3-2-4`

四缸发动机的点火顺序。点火顺序因发动机而异，但您对此参数的选择不会影响模块性能。您可以将点火顺序信息用于控制器开发。

#### 依赖关系

要启用此参数，请将 **Number of
cylinders** 设置为 `Four
Cylinders`。

### 仿真

### **Threshold to avoid divide-by-zero** — 发动机转速阈值 `0.1` `rad/s`（默认）

模块应用线性化以避免在 *ω* = 0 处出现不连续的发动机转速。

### 输出

### **Cycle-average speed** — 输出循环平均转速的选项 `on`（默认）| `off`

是否输出循环平均转速。

### **Cycle-average net indicated torque** — 输出循环平均净指示扭矩的选项 `on`（默认）| `off`

是否输出循环平均净指示扭矩。

### **Instantaneous net indicated torque** — 输出瞬时净指示扭矩的选项 `on`（默认）| `off`

是否输出瞬时净指示扭矩。
## 所属库

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

### R2025a：枚举更新

这些参数现在使用复选框。

- **Input power separately**
- **Cycle-average speed**
- **Cycle-average net indicated torque**
- **Instantaneous net indicated torque**

这些参数在之前的版本中使用下拉菜单。

## 描述

连接到一个或多个活塞的内燃机曲轴

Crankshaft 模块表示抽象内燃机的曲轴组件。将此模块连接到一个或多个
SI Combustion
Cylinder 模块，以计算曲柄角解析的瞬时扭矩。

### 方程

该模块遵循通用的扭矩-转速-功率关系，即

τ⋅ω=P，

其中

- *τ* 是扭矩。
- *ω* 是转速，模块假定其为非负值。
- *P* 是功率。

模块按如下方式计算功率

P=∑i=1NPi，

其中 *N* 是 **Number
of cylinders** 参数的值。模块将 *ω* 计算为曲柄位置 *θ* 的时间导数，即

ddtθ=ω。

常数 *ωc* 是
**Threshold to avoid divide-by-zero** 参数。当 *ω* <
*ωc* 时，模块应用 1/*ω* 线性化。

τ={PωP⋅(2ω−ωωc2)ω≥ωcω<ωc

**曲柄位置**

模块计算每个燃烧气缸相对于上止点位置的曲柄位置，其中 0 ≤ *θi* ≤
720 度。模块执行此计算的方式取决于
*N*。对于所有 *N* 值，*θ1* =
*θ*。对于 *N* = 2，*θ2* =
*θ1*+*Δ*，其中 *Δ* 是 **Spark angle
difference** 参数。此参数值特定于您要建模的发动机。它可能是 270° 或 360° 之类的值。当 *N* = 3 时，模块假定气缸均匀相位，使得

θ2=θ1+(1⋅7203)θ3=θ1+(2⋅7203)

当 *N* = 4 时，模块假定气缸以
180° 均匀相位，并启用 **Firing order** 参数。
