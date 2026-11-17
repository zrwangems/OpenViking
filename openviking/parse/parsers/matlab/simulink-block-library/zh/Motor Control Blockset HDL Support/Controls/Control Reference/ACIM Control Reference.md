---
type: simulink-block
title: 'ACIM Control Reference'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'acimcontrolreference'
documentation_source_path: '../mcb/ref/acimcontrolreference.html'
language: zh-CN
chinese_source: worker-translation
---

# ACIM Control Reference

## 端口

### 输入

### **Tref** — 参考转矩值 标量

该模块用于计算参考电流的参考转矩输入值。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m** — 机械转速 标量

该模块用于计算参考电流的参考机械转速值。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Isdref** — 参考 *d* 轴定子电流 标量

参考 *d* 轴定子电流值。

**数据类型：** `single` | `double` | `fixed point`

### **Isqref** — 参考 *q* 轴定子电流 标量

参考 *q* 轴定子电流值。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Number of pole pairs** — 电机中可用的极对数 `2`（默认）| 标量

感应电机中可用的极对数。

### **Rotor leakage inductance (H)** — 转子绕组的漏电感 `6.81e-3`（默认）| 标量

与转子绕组交链的漏磁通所产生的电感（单位：亨利）。

### **Magnetizing Inductance (H)** — 感应电机的励磁电感 `30e-3`（默认）| 标量

励磁磁通所产生的电感（单位：亨利）。

### **Rated Flux (Wb)** — 电机额定磁通 `38.2e-3`（默认）| 标量

感应电机的额定磁通（单位：韦伯）。

### **Rated Speed (rpm)** — 电机额定转速 `1150`（默认）| 标量

根据电机数据表得到的感应电机额定转速（单位：rpm）。

### **Synchronous Speed (rpm)** — 电机同步转速 `1500`（默认）| 标量

感应电机的同步转速（单位：rpm）。

### **Max current (A)** — 电机最大相电流限值（安培） `3`（默认）| 标量

感应电机的最大相电流限值（安培）。

### **Input units** — 输入值的单位 `Per-Unit (PU)`（默认）| `SI Units`

输入值的单位。

### **Base Current (A)** — 标幺系统的基准电流 `5.3611`（默认）| 标量

标幺系统的基准电流（单位：安培）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。

### **Base torque (Nm)** — 标幺系统的基准转矩 `0.50072`（默认）| 标量

标幺系统的基准转矩（单位：Nm）。有关更多详细信息，请参阅 Per-Unit System 页面。

此参数不可配置，其值由其他参数在内部计算得出。

#### 依赖关系

要显示此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。

## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除 ACIM Control Reference 模块层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

### 使用 Fixed-Point Designer™ 进行定点转换设计与仿真定点系统。

## 版本历史

**在 R2020b 中引入**

## 描述

计算感应电机磁场定向控制的参考电流

ACIM Control Reference 模块计算磁场定向控制（以及弱磁）操作所需的 *d* 轴和 *q* 轴参考电流。

该模块接受参考转矩和反馈机械转速，并输出相应的 *d* 轴和 *q* 轴参考电流。

该模块通过求解数学关系来计算参考电流值。计算使用 SI 单位制。当使用标幺（PU）制时（将 **Input units** 参数设置为 `Per-Unit (PU)`），该模块会将 PU 输入信号转换为 SI 单位以执行计算，并在输出端将其转换回 PU 值。

以下方程描述了该模块如何计算参考 *d* 轴和 *q* 轴电流值。

### 感应电机的数学模型

以下模型方程描述了感应电机在转子磁链参考坐标系中的动态特性：

电机电感表示为：

Ls= Lls+ Lm

Lr= Llr+ Lm

σ=1−(Lm2Ls⋅Lr)

定子电压表示为：

vsd= Rsisd+σLsdisddt+LmLrdλrddt−ωeσLsisq

vsq= Rsisq+σLsdisqdt+LmLrωeλrd+ωeσLsisd

在上述方程中，磁链可以表示为：

λsd= LmLrλrd+σLsisd

λsq= σLsisq

τrdλrddt+ λrd=Lmisd

如果我们将转子磁链保持恒定，并且 *d* 轴与转子磁链参考坐标系对齐，则可以得出：

λrd=Lmisd

λrq=0

以下方程描述了机械动态特性：

Te=32p(LmLr)λrdisq

Te− TL=Jdωmdt +Bωm

以下方程描述了转差速度：

τr= (LrRr)

ωe\_slip= (Lm⋅isqrefτr⋅λrd)

ωe= ωr+ωe\_slip

θe= ∫ωe⋅ dt=∫(ωr+ωe\_slip)⋅dt=θr+θslip

### Reference Current Computation

这些方程展示了参考电流的计算，

isd\_0=λrdLm

isq\_req= Tref32p(LmLr)λrd

参考电流在基速以下运行和弱磁区域的计算方式不同，

如果 ωm≤ ωrated：

isd\_sat=min(isd\_0,imax)

如果 ωm> ωrated：

isd\_fw=isd\_0(ωratedωm)

isd\_sat=min(isd\_fw,imax)

这些方程表示 *q* 轴电流的计算，

isq\_lim= imax2− isd\_sat2

isq\_sat=sat(isq\_lim,isq\_req)

该模块输出以下值，

isdref=isd\_sat

isqref=isq\_sat

其中：

- p 是电机的极对数。
- Rs 是定子相绕组电阻（欧姆）。
- Rr 是折算到定子的转子电阻（欧姆）。
- Lls 是定子漏电感（亨利）。
- Llr 是转子漏电感（亨利）。
- Ls 是定子电感（亨利）。
- Lm 是励磁电感（亨利）。
- Lr 是折算到定子的转子电感（亨利）。
- σ 是感应电机的总漏磁系数。
- τr 是转子时间常数（秒）。
- vsd 和 vsq 是定子 *d* 轴和 *q* 轴电压（伏特）。
- isd 和 isq 是定子 *d* 轴和 *q* 轴电流（安培）。
- isd\_0 是定子的额定 *d* 轴电流，也称为励磁电流（安培）。
- imax 是电机的最大相电流（峰值）（安培）。
- λsd 是定子的 *d* 轴磁链（韦伯）。
- λsq 是定子的 *q* 轴磁链（韦伯）。
- λrd 是转子的 *d* 轴磁链（韦伯）。
- λrq 是转子的 *q* 轴磁链（韦伯）。
- ωe\_slip 是转子的电转差速度（弧度/秒）。
- ωslip 是转子的机械转差速度（弧度/秒）。
- ωe 是对应于定子电压频率的电速度（弧度/秒）。
- ωm 是转子机械速度（弧度/秒）。
- ωr 是转子电速度（弧度/秒）。
- ωrated 是电机的额定机械速度（弧度/秒）。
- Te 是电机产生的机电转矩（Nm）。
