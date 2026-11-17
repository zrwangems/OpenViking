---
type: simulink-block
title: 'Induction Machine Field-Oriented Control (Single-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinefieldorientedcontrolsinglephase'
documentation_source_path: 'ref/inductionmachinefieldorientedcontrolsinglephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Field-Oriented Control (Single-Phase)

## 端口
```yaml
ports:
- name: Reference
  summary: 转矩或角速度参考值标量
  direction: input
  data_types: single | double
- name: iab
  summary: 定子电流标量
  direction: input
  data_types: single | double
- name: wr
  summary: 转子角速度标量
  direction: input
  data_types: single | double
- name: G
  summary: 逆变器门极脉冲 0 | 1
  direction: output
  data_types: single | double
- name: Visualization
  summary: 用于可视化的内部信号 Reference | Rotor velocity | θ | iab | iabRef | TqRef | FluxRef
  direction: output
  data_types: single | double | bus
```

### 输入

### **Reference** — 转矩或角速度参考值标量

指定角速度参考值，单位为 rad/s，或转矩参考值，单位为 Nm。

**数据类型：** `single` | `double`

### **iab** — 定子电流标量

主绕组和辅助绕组的定子电流。

**数据类型：** `single` | `double`

### **wr** — 转子角速度标量

测得的转子角速度，单位为 rad/s。

**数据类型：** `single` | `double`
### 输出

### **G** — 逆变器门极脉冲 `0` | `1`

逆变器门极脉冲，指定为布尔值。不考虑死区时间。

**数据类型：** `single` | `double`

### **Visualization** — 用于可视化的内部信号 `Reference` | `Rotor velocity` | `θ` | `iab` | `iabRef` | `TqRef` | `FluxRef`

包含用于可视化的内部信号的总线。信号包括：

- 参考转矩或速度
- 转子速度，单位为 rad/s
- *θ*，单位为弧度
- 定子电流（*iab*），单位为 A
- 定子电流参考值（*iabRef*），单位为 A
- 转矩参考值（*TqRef*），单位为 Nm
- 磁链参考值（*FluxRef*），单位为 Wb

**数据类型：** `single` | `double` | `bus`
## 参数
```yaml
parameters:
- name: Control mode
  summary: 指定控制模式 Speed control（默认） | Torque control
  group: 常规
- name: Rated electrical frequency (Hz)
  summary: 指定额定电频率 60（默认） | 正标量
  group: 常规
- name: Number of pole pairs
  summary: 指定极对数 2（默认） | 正标量
  group: 常规
- name: Main winding rotor resistance, Rar' (Ohm)
  summary: 指定主绕组转子电阻 3.7080（默认） | 正标量
  group: 常规
- name: Main winding rotor leakage inductance, Llar' (H)
  summary: 指定主绕组转子漏电感 0.0050（默认） | 正标量
  group: 常规
- name: Main winding mutual inductance, Lms (H)
  summary: 指定主绕组互感 0.1595（默认） | 正标量
  group: 常规
- name: Auxiliary/main windings turn ratio
  summary: 指定辅助绕组与主绕组的匝数比 1.1（默认） | 正标量
  group: 常规
- name: Fundamental sample time (s)
  summary: 指定模块采样时间 5e-6（默认） | 正标量
  group: 常规
- name: Control sample time (s)
  summary: 指定控制采样时间 5e-5（默认） | 正标量
  group: 常规
- name: Speed controller proportional gain
  summary: 指定速度控制器比例增益 1（默认） | 正标量
  group: 外环
- name: Speed controller integral gain
  summary: 指定速度控制器积分增益 10（默认） | 正标量
  group: 外环
- name: Speed controller integral anti-windup gain
  summary: 指定速度控制器积分抗饱和增益 1000（默认） | 正标量
  group: 外环
- name: Maximum torque (Nm)
  summary: 指定最大转矩 5（默认） | 正标量
  group: 外环
- name: Minimum torque (Nm)
  summary: 指定最小转矩 -5（默认） | 标量
  group: 外环
- name: Rated flux (Wb)
  summary: 指定额定磁链 0.5（默认） | 正标量
  group: 外环
- name: Control type
  summary: 指定控制类型 Hysteresis control（默认） | PI control
  group: 内环
- name: Current hysteresis band (A)
  summary: 指定电流滞环带宽 0.5（默认） | 正标量
  group: 内环
- name: A-phase current proportional gain
  summary: 主绕组电流比例增益 1（默认） | 正标量
  group: 内环
- name: A-phase current integral gain
  summary: 主绕组电流积分增益 500（默认）
  group: 内环
- name: A-phase current anti-windup gain
  summary: 主绕组电流抗饱和增益 1000（默认）
  group: 内环
- name: B-phase current proportional gain
  summary: 辅助绕组电流比例增益 1（默认）
  group: 内环
- name: B-phase current integral gain
  summary: 辅助绕组电流积分增益 500（默认）
  group: 内环
- name: B-phase current anti-windup gain
  summary: 辅助绕组电流抗饱和增益 1000（默认）
  group: 内环
```

### 常规

### **Control mode** — 指定控制模式 `Speed control`（默认） | `Torque control`

指定控制模式。对于 `Speed control`，参考输入为角速度，单位为 rad/s；对于 `Torque control`，参考输入为转矩，单位为 Nm。

### **Rated electrical frequency (Hz)** — 指定额定电频率 `60`（默认） | 正标量

额定电频率，单位为 Hz。

### **Number of pole pairs** — 指定极对数 `2`（默认） | 正标量

极对数。

### **Main winding rotor resistance, Rar' (Ohm)** — 指定主绕组转子电阻 `3.7080`（默认） | 正标量

主绕组转子电阻，单位为欧姆。

### **Main winding rotor leakage inductance, Llar' (H)** — 指定主绕组转子漏电感 `0.0050`（默认） | 正标量

主绕组转子漏电感，单位为 H。

### **Main winding mutual inductance, Lms (H)** — 指定主绕组互感 `0.1595`（默认） | 正标量

主绕组互感，单位为 H。

### **Auxiliary/main windings turn ratio** — 指定辅助绕组与主绕组的匝数比 `1.1`（默认） | 正标量

辅助绕组与主绕组的匝数比。

### **Fundamental sample time (s)** — 指定模块采样时间 `5e-6`（默认） | 正标量

模块的采样时间，单位为 s。

### **Control sample time (s)** — 指定控制采样时间 `5e-5`（默认） | 正标量

控制采样时间，单位为 s。

### 外环

下表显示了 **Outer Loop** 选项卡中某些参数的可见性如何取决于 **General** 选项卡中 **Control mode** 参数所选的选项。

| 控制模式 | 可用参数 |
| --- | --- |
| Speed control | Speed controller proportional gain |
| Speed controller integral gain |
| Speed controller integral anti-windup gain |
| Maximum torque (Nm) |
| Minimum torque (Nm) |
| Rated flux (Wb) |
| Torque control | Rated flux (Wb) |

### **Speed controller proportional gain** — 指定速度控制器比例增益 `1`（默认） | 正标量

PI 速度控制器的比例增益。

### **Speed controller integral gain** — 指定速度控制器积分增益 `10`（默认） | 正标量

PI 速度控制器的积分增益。

### **Speed controller integral anti-windup gain** — 指定速度控制器积分抗饱和增益 `1000`（默认） | 正标量

积分抗饱和增益。

### **Maximum torque (Nm)** — 指定最大转矩 `5`（默认） | 正标量

速度控制器饱和中使用的最大转矩，单位为 Nm。

### **Minimum torque (Nm)** — 指定最小转矩 `-5`（默认） | 标量

速度控制器饱和中使用的最小转矩，单位为 Nm。

### **Rated flux (Wb)** — 指定额定磁链 `0.5`（默认） | 正标量

额定磁链，单位为 Wb。额定磁链用于计算磁链参考值。

### 内环

下表显示了 **Inner Loop** 选项卡中某些参数的可见性如何取决于 **Control type** 参数所选的选项。

| 控制类型 | 可用参数 |
| --- | --- |
| Hysteresis control | Current hysteresis band (A) |
| PI control | A-phase current proportional gain |
| A-phase current integral gain |
| A-phase current anti-windup gain |
| B-phase current proportional gain |
| B-phase current integral gain |
| B-phase current anti-windup gain |

### **Control type** — 指定控制类型 `Hysteresis control`（默认） | `PI control`

电流控制环的控制类型。

### **Current hysteresis band (A)** — 指定电流滞环带宽 `0.5`（默认） | 正标量

控制器的电流滞环带宽，单位为 A。

### **A-phase current proportional gain** — 主绕组电流比例增益 `1`（默认） | 正标量

A 相（主绕组）控制器电流的比例增益。

### **A-phase current integral gain** — 主绕组电流积分增益 `500`（默认）

A 相（主绕组）控制器电流的积分增益。

### **A-phase current anti-windup gain** — 主绕组电流抗饱和增益 `1000`（默认）

A 相（主绕组）控制器电流的抗饱和增益。

### **B-phase current proportional gain** — 辅助绕组电流比例增益 `1`（默认）

B 相（辅助绕组）控制器电流的比例增益。

### **B-phase current integral gain** — 辅助绕组电流积分增益 `500`（默认）

B 相（辅助绕组）控制器电流的积分增益。

### **B-phase current anti-windup gain** — 辅助绕组电流抗饱和增益 `1000`（默认）

B 相（辅助绕组）控制器电流的抗饱和增益。
## 所属库

Simscape / Electrical / Control / Induction Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

标幺值离散时间单相感应电机磁场定向控制

Induction Machine Field-Oriented Control (Single-Phase) 模块实现单相感应电机磁场定向控制结构。

### 方程

单相感应电机的磁场定向控制架构为：

您可以将转矩参考值作为输入提供，或者在速度控制的情况下，使用 PI 速度控制器内部生成参考值。由 PI 速度控制器导出的转矩参考值为：

T\*=(Kp\_ω+Ki\_ωTszz−1)(ωref−ωr)

其中 *ωr* 是转子角机械速度，单位为 rad/s。

该模块生成磁链参考值为

ψ\*=2πfnψnpmin(|ωr|,2πfnp)

其中：

- *p* 是极对数。
- *fn* 是额定频率。
- *ψn* 是额定磁链。

电流参考值由电机参数获得：

iq\*=(Lms+Llar)T\*paLmsψ\*

id\*=ψ\*a2Lms

其中：

- *Lms* 是主绕组互感。
- *Llar* 是主绕组转子漏电感。
- *a* 是辅助绕组与主绕组的匝数比。

角度通过求解以下方程计算：

dθdt=pωr+a3LmsRarψ\*(Lms+Llar)

到静止参考坐标系的变换通过使用以下公式完成：

(iaib)=(a2sin(θ)a2cos(θ)cos(θ)−sin(θ))(idiq)

### 限制

- 该控制结构以单一采样率实现。
