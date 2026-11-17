---
type: simulink-block
title: 'Induction Machine Direct Torque Control (Single-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinedirecttorquecontrolsinglephase'
documentation_source_path: 'ref/inductionmachinedirecttorquecontrolsinglephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Direct Torque Control (Single-Phase)

## 端口
```yaml
ports:
- name: Reference
  summary: 转矩或角速度参考标量
  direction: input
  data_types: single | double
- name: iab
  summary: 定子电流标量
  direction: input
  data_types: single | double
- name: vab
  summary: 定子电压标量
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
  summary: 用于可视化的内部信号 Reference | Rotor velocity | TqRef | FluxRef | Torque | Flux
  direction: output
  data_types: single | double | bus
```

### 输入

### **Reference** — 转矩或角速度参考标量

以 rad/s 为单位指定角速度参考，或以 Nm 为单位指定转矩参考。

**数据类型：** `single` | `double`

### **iab** — 定子电流标量

主绕组和辅助绕组的定子电流。

**数据类型：** `single` | `double`

### **vab** — 定子电压标量

主绕组和辅助绕组的定子电压。

**数据类型：** `single` | `double`

### **wr** — 转子角速度标量

以 rad/s 为单位测量转子角速度。

**数据类型：** `single` | `double`
### 输出

### **G** — 逆变器门极脉冲 `0` | `1`

逆变器门极脉冲，指定为布尔值。不考虑死区时间。

**数据类型：** `single` | `double`

### **Visualization** — 用于可视化的内部信号 `Reference` | `Rotor velocity` | `TqRef` | `FluxRef` | `Torque` | `Flux`

包含用于可视化的内部信号的总线。信号包括：

- 参考转矩或速度
- 转子速度，单位为 rad/s
- 转矩参考，单位为 Nm
- 磁链参考，单位为 Wb
- 转矩，单位为 Nm
- 磁链，单位为 Wb

**数据类型：** `single` | `double` | `bus`
## 参数
```yaml
parameters:
- name: Control mode
  summary: 指定控制模式 Speed control（默认）| Torque control
  group: 常规
- name: Rated electrical frequency (Hz)
  summary: 指定额定电频率 60（默认）| 正标量
  group: 常规
- name: Number of pole pairs
  summary: 指定极对数 2（默认）| 正标量
  group: 常规
- name: Main winding stator resistance, Ras (Ohm)
  summary: 指定主绕组定子电阻 1.8180（默认）| 正标量
  group: 常规
- name: Auxiliary winding stator resistance, Rbs (Ohm)
  summary: 指定辅助绕组定子电阻 6.4260（默认）| 正标量
  group: 常规
- name: Auxiliary/main windings turn ratio
  summary: 指定辅助绕组与主绕组的匝数比 1.1（默认）| 正标量
  group: 常规
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 正标量
  group: 常规
- name: Speed controller proportional gain
  summary: 指定速度控制器比例增益 1（默认）| 正标量
  group: 外环
- name: Speed controller integral gain
  summary: 指定速度控制器积分增益 10（默认）| 正标量
  group: 外环
- name: Speed controller integral anti-windup gain
  summary: 指定速度控制器积分抗饱和增益 1000（默认）| 正标量
  group: 外环
- name: Maximum torque (Nm)
  summary: 指定最大转矩 5（默认）| 正标量
  group: 外环
- name: Minimum torque (Nm)
  summary: 指定最小转矩 -5（默认）| 标量
  group: 外环
- name: Rated flux (Wb)
  summary: 指定额定磁链 0.5（默认）| 正标量
  group: 外环
- name: Flux hysteresis band (Wb)
  summary: 指定磁链滞环带宽 0.02（默认）| 正标量
  group: 内环
- name: Torque hysteresis band (Nm)
  summary: 指定转矩滞环带宽 0.1（默认）| 正标量
  group: 内环
```

### 常规

### **Control mode** — 指定控制模式 `Speed control`（默认）| `Torque control`

指定控制模式。对于 `Speed control`，参考输入被视为角速度，单位为 rad/s；对于 `Torque control`，参考输入被视为转矩，单位为 Nm。

### **Rated electrical frequency (Hz)** — 指定额定电频率 `60`（默认）| 正标量

额定电频率，单位为 Hz。

### **Number of pole pairs** — 指定极对数 `2`（默认）| 正标量

极对数。

### **Main winding stator resistance, Ras (Ohm)** — 指定主绕组定子电阻 `1.8180`（默认）| 正标量

主绕组定子电阻，单位为欧姆。

### **Auxiliary winding stator resistance, Rbs (Ohm)** — 指定辅助绕组定子电阻 `6.4260`（默认）| 正标量

辅助绕组定子电阻，单位为欧姆。

### **Auxiliary/main windings turn ratio** — 指定辅助绕组与主绕组的匝数比 `1.1`（默认）| 正标量

辅助绕组与主绕组的匝数比。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

### 外环

此表显示了 **Outer Loop** 选项卡中某些参数的可见性如何取决于 **General** 选项卡中 **Control mode** 参数所选的选项。

| 控制模式 | 可用参数 |
| --- | --- |
| Speed control | Speed controller proportional gain |
| Speed controller integral gain |
| Speed controller integral anti-windup gain |
| Maximum torque (Nm) |
| Minimum torque (Nm) |
| Rated flux (Wb) |
| Torque control | Rated flux (Wb) |

### **Speed controller proportional gain** — 指定速度控制器比例增益 `1`（默认）| 正标量

PI 速度控制器的比例增益。

### **Speed controller integral gain** — 指定速度控制器积分增益 `10`（默认）| 正标量

PI 速度控制器的积分增益。

### **Speed controller integral anti-windup gain** — 指定速度控制器积分抗饱和增益 `1000`（默认）| 正标量

积分抗饱和增益。

### **Maximum torque (Nm)** — 指定最大转矩 `5`（默认）| 正标量

速度控制器饱和中使用的最大转矩，单位为 Nm。

### **Minimum torque (Nm)** — 指定最小转矩 `-5`（默认）| 标量

速度控制器饱和中使用的最小转矩，单位为 Nm。

### **Rated flux (Wb)** — 指定额定磁链 `0.5`（默认）| 正标量

额定磁链，单位为 Wb。额定磁链用于计算磁链参考。

### 内环

### **Flux hysteresis band (Wb)** — 指定磁链滞环带宽 `0.02`（默认）| 正标量

控制器的磁链滞环带宽，单位为 Wb。

### **Torque hysteresis band (Nm)** — 指定转矩滞环带宽 `0.1`（默认）| 正标量

控制器的转矩滞环带宽，单位为 Nm。
## 所属库

Simscape / Electrical / Control / Induction Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

单相感应电机直接转矩控制

Induction Machine Direct Torque Control (Single-Phase) 模块实现单相感应电机直接转矩控制结构。

### 方程

此图显示了单相电机的直接转矩控制架构

转矩和磁链估计基于电机电压方程。使用后向欧拉离散化方法的离散时间电压方程为：

ψa=(va−iaRas)Tszz−1

ψb=(vb−ibRbs)Tszz−1

其中：

- *Ras* 和 *Rbs* 分别为主绕组电阻和辅助绕组电阻。
- *ia* 和 *ib* 分别为主绕组电流和辅助绕组电流。
- *va* 和 *vb* 分别为主绕组电压和辅助绕组电压。
- *ψa* 和 *ψb* 分别为主绕组磁链和辅助绕组磁链。

转矩和磁链由下式获得：

T=−p(aψaib−1aψbia)

ψs=ψa2+ψb2

其中：

- `p` 为极对数。
- `a` 为辅助绕组与主绕组的匝数比。

采用简单的滞环比较器检测磁链和转矩误差的状态。下图说明了滞环比较器和开关扇区。

该表显示了最优开关表（逆变器高侧）。

| *cψ*, *cT*, *S(θ)* | | *S0* | *S1* | *S2* | *S3* |
| --- | --- | --- | --- | --- | --- |
| `cψ` = 1 | `cT` = 1 | 1, 0 | 1, 1 | 0, 1 | 0, 0 |
| `cT` = 0 | 1, 1 | 0, 1 | 0, 0 | 1, 0 |
| `cψ` = 0 | `cT` = 1 | 0, 0 | 1, 0 | 1, 1 | 0, 1 |
| `cT` = 0 | 0, 1 | 0, 0 | 1, 0 | 1, 1 |

转矩参考可以作为输入提供，或者在速度控制的情况下，使用 PI 速度控制器内部生成。

磁链参考使用下式内部生成：

ψs\*=2πfnψnpmin(|ωr|,2πfnp)

其中，

- *ωr* 为转子角机械速度，单位为 rad/s。
- *fn* 为额定频率。
- *ψn* 为额定磁链。

### 限制

- 此模块不考虑功率逆变器死区时间。对于硬件实现，请在外部添加死区时间。
