---
type: simulink-block
title: 'Induction Machine Direct Torque Control (Single-Phase)'
family: 'control'
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

## Ports

### Input

### **Reference** — 转矩或角速度参考标量

以 rad/s 指定角速度参考，或以 Nm 指定转矩参考。

**数据类型：** `single` | `double`

### **iab** — 定子电流标量

主绕组和辅助绕组的定子电流。

**数据类型：** `single` | `double`

### **vab** — 定子电压标量

主绕组和辅助绕组的定子电压。

**数据类型：** `single` | `double`

### **wr** — 转子角速度标量

以 rad/s 测量转子角速度。

**数据类型：** `single` | `double`
### Output

### **G** — 逆变器门极脉冲 `0` | `1`

逆变器门极脉冲，指定为布尔值。不考虑死区。

**数据类型：** `single` | `double`

### **Visualization** — 用于可视化的内部信号 `Reference` | `Rotor velocity` | `TqRef` | `FluxRef` | `Torque` | `Flux`

包含用于可视化的内部信号的 Bus。信号为：

- 参考转矩或速度
- Rotor velocity，单位为 rad/s
- Torque Reference，单位为 Nm
- Flux Reference，单位为 Wb
- Torque，单位为 Nm
- Flux，单位为 Wb

**数据类型：** `single` | `double` | `bus`

## Parameters

### General

### **控制模式** — 指定控制模式 `Speed control` (默认) | `Torque control`

指定控制模式。对于 `Speed control`，参考输入取为角速度，单位为 rad/s；对于 `Torque control`，参考输入取为转矩，单位为 Nm。

### **额定电气频率 (Hz)** — 指定额定电气频率 `60` (默认) | 正标量

额定电气频率，单位为 Hz。

### **极对数** — 指定极对数 `2` (默认) | 正标量

极对数。

### **主绕组定子电阻, Ras (Ohm)** — 指定主绕组定子电阻 `1.8180` (默认) | 正标量

主绕组定子的电阻，单位为 Ohm。

### **辅助绕组定子电阻, Rbs (Ohm)** — 指定辅助绕组定子电阻 `6.4260` (默认) | 正标量

辅助绕组定子的电阻，单位为 Ohm。

### **辅助/主绕组匝数比** — 指定辅助绕组与主绕组的匝数比 `1.1` (默认) | 正标量

辅助绕组与主绕组的匝数比。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1` (默认) | 正标量

连续模块执行之间的时间，单位为 s。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

### Outer Loop

此表显示 **外环** 选项卡中某些参数的可见性如何取决于你在 **常规** 选项卡中为 **控制模式** 参数选择的选项。

| 控制模式 | 可用参数 |
| --- | --- |
| Speed control | 速度控制器比例增益 |
| 速度控制器积分增益 |
| 速度控制器积分抗饱和增益 |
| 最大转矩 (Nm) |
| 最小转矩 (Nm) |
| 额定磁通 (Wb) |
| Torque control | 额定磁通 (Wb) |

### **速度控制器比例增益** — 指定速度控制器比例增益 `1` (默认) | 正标量

PI 速度控制器的比例增益。

### **速度控制器积分增益** — 指定速度控制器积分增益 `10` (默认) | 正标量

PI 速度控制器的积分增益。

### **速度控制器积分抗饱和增益** — 指定速度控制器积分抗饱和增益 `1000` (默认) | 正标量

积分抗饱和增益。

### **最大转矩 (Nm)** — 指定最大转矩 `5` (默认) | 正标量

速度控制器饱和中使用的最大转矩，单位为 Nm。

### **最小转矩 (Nm)** — 指定最小转矩 `-5` (默认) | 标量

速度控制器饱和中使用的最小转矩，单位为 Nm。

### **额定磁通 (Wb)** — 指定额定磁通 `0.5` (默认) | 正标量

额定磁通，单位为 Wb。额定磁通用于计算磁通参考。

### Inner Loop

### **磁通滞环带宽 (Wb)** — 指定磁通滞环带宽 `0.02` (默认) | 正标量

控制器的磁通滞环带宽，单位为 Wb。

### **转矩滞环带宽 (Nm)** — 指定转矩滞环带宽 `0.1` (默认) | 正标量

控制器的转矩滞环带宽，单位为 Nm。

## Libraries

Simscape / Electrical / Control / Induction Machine Control

## Block Characteristics

未在 R2025b 中记录。

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

单相感应电机直接转矩控制

Induction Machine Direct Torque Control (Single-Phase) 模块实现单相感应电机直接转矩控制结构。

### Equations

此图展示了单相电机的直接转矩控制架构

转矩和磁通估计基于电机电压方程。使用后向欧拉离散化方法的离散时间电压方程为：

ψa=(va−iaRas)Tszz−1

ψb=(vb−ibRbs)Tszz−1

其中：

- *Ras* 和
  *Rbs* 分别为主绕组电阻和辅助绕组电阻。
- *ia* 和
  *ib* 分别为主绕组电流和辅助绕组电流。
- *va* 和
  *vb* 分别为主绕组电压和辅助绕组电压。
- *ψa* 和
  *ψb* 分别为主绕组磁通和辅助绕组磁通。

转矩和磁通由下式得到：

T=−p(aψaib−1aψbia)

ψs=ψa2+ψb2

其中：

- `p` 为极对数。
- `a` 为辅助绕组与主绕组的匝数比。

采用简单的滞环比较器检测磁通和转矩误差的状态。以下各图展示了滞环比较器和开关扇区。

下表显示了最优开关表（逆变器高侧）。

| *cψ*, *cT*, *S(θ)* | | *S0* | *S1* | *S2* | *S3* |
| --- | --- | --- | --- | --- | --- |
| `cψ` = 1 | `cT` = 1 | 1, 0 | 1, 1 | 0, 1 | 0, 0 |
| `cT` = 0 | 1, 1 | 0, 1 | 0, 0 | 1, 0 |
| `cψ` = 0 | `cT` = 1 | 0, 0 | 1, 0 | 1, 1 | 0, 1 |
| `cT` = 0 | 0, 1 | 0, 0 | 1, 0 | 1, 1 |

转矩参考可作为输入提供，或者在速度控制的情况下，使用 PI 速度控制器内部生成。

磁通参考使用下式内部生成：

ψs\*=2πfnψnpmin(|ωr|,2πfnp)

其中，

- *ωr* 为转子机械角速度，单位为 rad/s。
- *fn* 为额定频率。
- *ψn* 为额定磁通。

### Limitations

- 此模块不考虑功率逆变器死区。对于硬件实现，请在外部添加死区。
