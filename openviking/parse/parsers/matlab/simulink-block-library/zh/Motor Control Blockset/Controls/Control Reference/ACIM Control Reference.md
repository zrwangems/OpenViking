---
type: simulink-block
title: 'ACIM Control Reference'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'acimcontrolreference'
documentation_source_path: 'ref/acimcontrolreference.html'
language: zh-CN
chinese_source: official
---

# ACIM Control Reference

## 端口

### 输入

### **Tref** — 参考转矩值 标量

模块为其计算参考电流的参考转矩输入值。

**数据类型:** `single` | `double` | `fixed point`

### **⍵m** — 机械转速 标量

模块为其计算参考电流的参考机械转速值。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **Isdref** — 参考 *d* 轴定子电流 标量

参考 *d* 轴定子电流值。

**数据类型:** `single` | `double` | `fixed point`

### **Isqref** — 参考 *q* 轴定子电流 标量

参考 *q* 轴定子电流值。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **极对数** — 电机中可用的极对数 `2` (默认) | 标量

感应电机中可用的极对数。

### **转子泄漏电感(H)** — 转子绕组的漏感 `6.81e-3` (默认) | 标量

与转子绕组相关的泄漏磁通产生的电感（以亨为单位）。

### **磁化电感(H)** — 感应电机的磁化电感 `30e-3` (默认) | 标量

由磁化磁通产生的电感（以亨为单位）。

### **额定磁通(Wb)** — 电机的额定磁通 `38.2e-3` (默认) | 标量

感应电机的额定磁通（以韦伯为单位）。

### **额定转速(rpm)** — 电机的额定转速 `1150` (默认) | 标量

基于电机数据表的感应电机的额定转速（以 rpm 为单位）。

### **同步转速(rpm)** — 电机同步转速 `1500` (默认) | 标量

感应电机的同步转速（以 rpm 为单位）。

### **最大电流(A)** — 电机的相电流最大限值（安培） `3` (默认) | 标量

感应电机的相电流最大限值（安培）。

### **输入单位** — 输入值的单位 **标幺(PU)** (默认) | **SI 单位**

输入值的单位。

### **基电流(A)** — 标幺制的基电流 `5.3611` (默认) | 标量

标幺制的基电流（以安培为单位）。

#### 依赖关系

要启用此参数，请将**输入单位**设置为**标幺(PU)**。

### **基转矩(Nm)** — 标幺制的基转矩 `0.50072` (默认) | 标量

标幺制的基转矩（以 Nm 为单位）。有关详细信息，请参阅标幺制页。

此参数不可配置，它使用的值是使用其他参数内部计算获得的。

#### 依赖关系

要显示此参数，请将**输入单位**设置为**标幺(PU)**。

## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 要通过移动设计中的现有延迟来放置在输出端的寄存器的数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中删除 ACIM Control Reference 模块层次结构。默认值为**继承**。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020b 中推出**

## 描述

计算感应电机磁场定向控制的参考电流

ACIM Control Reference 模块为磁场定向控制（和弱磁）操作计算 *d* 轴和 *q* 轴的参考电流。

该模块接受参考转矩和反馈机械转速，并输出对应的 *d* 和 *q* 轴参考电流。

该模块通过求解数学关系来计算参考电流值。计算使用 SI 单位制。使用标幺 (PU) 制时（将**输入单位**参数设置为**标幺 (PU)**），该模块将 PU 输入信号转换为 SI 单位以执行计算，并在输出端将其转换回 PU 值。

这些方程描述该模块如何计算参考 *d* 轴和 *q* 轴的电流值。

### 感应电机的数学模型

这些模型方程描述转子磁通参考系中感应电机的动态特性：

感应电机的电感表示为，

Ls= Lls+ Lm

Lr= Llr+ Lm

σ=1−(Lm2Ls⋅Lr)

定子电压表示为，

vsd= Rsisd+σLsdisddt+LmLrdλrddt−ωeσLsisq

vsq= Rsisq+σLsdisqdt+LmLrωeλrd+ωeσLsisd

在前面的方程中，磁链可以表示为，

λsd= LmLrλrd+σLsisd

λsq= σLsisq

τrdλrddt+ λrd=Lmisd

如果我们保持转子磁通不变，并且 *d* 轴与转子磁通参考系对齐，则我们可以推断：

λrd=Lmisd

λrq=0

下列方程描述机械动态特性，

Te=32p(LmLr)λrdisq

Te− TL=Jdωmdt +Bωm

下列方程描述转差速度，

τr= (LrRr)

ωe\_slip= (Lm⋅isqrefτr⋅λrd)

ωe= ωr+ωe\_slip

θe= ∫ωe⋅ dt=∫(ωr+ωe\_slip)⋅dt=θr+θslip

### 参考电流计算

下列方程显示参考电流的计算，

isd\_0=λrdLm

isq\_req= Tref32p(LmLr)λrd

在低于基转速和弱磁区域运行时，参考电流的计算方法有所不同，

如果 ωm≤ ωrated，则：

isd\_sat=min(isd\_0,imax)

如果 ωm> ωrated，则：

isd\_fw=isd\_0(ωratedωm)

isd\_sat=min(isd\_fw,imax)

下列方程指示 *q* 轴电流计算，

isq\_lim= imax2− isd\_sat2

isq\_sat=sat(isq\_lim,isq\_req)

该模块输出以下值，

isdref=isd\_sat

isqref=isq\_sat

其中：

- p 是电机的极对数。
- Rs 是定子相绕组电阻 (ohm)。
- Rr 是转子相对于定子的电阻 (ohm)。
- Lls 是定子漏感（亨）。
- Llr 是转子泄漏电感（亨）。
- Ls 是定子电感（亨）。
- Lm 是磁化电感（亨）。
- Lr 是转子相对于定子的电感（亨）。
- σ 是感应电机的总漏磁因子。
- τr 是转子时间常量（秒）。
- vsd 和 vsq 是定子的 *d* 轴和 *q* 轴电压（伏）。
- isd 和 isq 是定子的 *d* 轴和 *q* 轴电流（安培）。
- isd\_0 是定子的额定 *d* 轴电流，也称为磁化电流（安培）。
- imax 是电机的最大相电流（峰值）（安培）。
- λsd 是定子的 *d* 轴磁链（韦伯）。
- λsq 是定子的 *q* 轴磁链（韦伯）。
- λrd 是转子的 *d* 轴磁链（韦伯）。
- λrq 是转子的 *q* 轴磁链（韦伯）。
- ωe\_slip 是转子的电气转差速度（弧度/秒）。
- ωslip 是转子的机械转差速度（弧度/秒）。
- ωe 是对应于定子电压频率的电角速度（弧度/秒）。
- ωm 是转子机械转速（弧度/秒）。
- ωr 是转子电角速度（弧度/秒）。
- ωrated 是电机的额定机械转速（弧度/秒）。
- Te 是电机产生的机电转矩 (Nm)。
