---
type: simulink-block
title: 'ACIM Slip Speed Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Control Reference'
documentation_page: 'acimslipspeedestimator'
documentation_source_path: 'ref/acimslipspeedestimator.html'
language: zh-CN
chinese_source: official
---

# ACIM Slip Speed Estimator

## 端口

### 输入

### **Isdref** — 参考 *d* 轴定子电流 标量

参考 *d* 轴定子电流。

**数据类型:** `single` | `double` | `fixed point`

### **Isqref** — 参考 *q* 轴定子电流 标量

参考 *q* 轴定子电流。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **⍵mslip** — 感应电机的转差转速 标量

模块计算的转子机械转差转速。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **极对数** — 电机中可用的极对数 `2` (默认) | 标量

感应电机中可用的极对数。

### **转子电阻(Ohm)** — 电机转子电阻 `1.05` (默认) | 标量

感应电机的转子电阻，以 ohm 为单位。

### **转子泄漏电感(H)** — 转子绕组的漏感 `6.81e-3` (默认) | 标量

与转子绕组相关的泄漏磁通产生的电感（以亨为单位）。

### **磁化电感(H)** — 感应电机的磁化电感 `30e-3` (默认) | 标量

由磁化磁通产生的电感（以亨为单位）。

### **输出饱和(rpm)** — 模块输出的饱和值 `150` (默认) | 标量

模块输出的饱和值（以 rpm 为单位）。

### **输入单位** — 输入值的单位 `Per-Unit (PU)` (默认) | SI 单位

输入值的单位。

### **基转速(rpm)** — 标幺制的基转速 `1500` (默认) | 标量

标幺制的基转速（以 rpm 为单位）。

#### 依赖关系

要启用此参数，请将**输入单位**设置为**标幺(PU)**。

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
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020b 中推出**

## 描述

计算 AC 感应电机的转差速度

ACIM Slip Speed Estimator 模块估计感应电机的机械转差速度（同步转速和转子转速之差）。

该模块接受 *d* 轴和 *q* 轴电流的参考值，并输出计算的感应电机转差速度。

### 方程

下列方程描述感应电机磁场定向控制 (FOC) 的转差速度值的利用：

τr= (LrRr)

ωe\_slip= (Lm⋅isqrefτr⋅λrd)

ωe= ωr+ωe\_slip

θe= ∫ωe⋅ dt=∫(ωr+ωe\_slip)⋅dt=θr+θslip

如果我们保持转子磁通不变，并且 *d* 轴与转子磁通参考系对齐，则我们可以推断：

λrd=Lmisd

此模块按照如下方式实现上述计算：

ωslip= (1p)(1τr)(isqrefisdref)

有关详细的方程组和假设，请参阅感应电机的数学模型。

其中：

- ωe\_slip 是转子的电气转差速度（弧度/秒）。
- ωslip 是转子的机械转差速度（弧度/秒）。
- ωe 是对应于定子电压频率的电角速度（弧度/秒）。
- ωm 是转子机械转速（弧度/秒）。
- ωr 是转子电角速度（弧度/秒）。
- Lm 是电机的磁化电感（亨）。
- Rr 是转子相对于定子的电阻 (ohm)。
- isdref 和 isqref 是参考定子 *d* 轴和 *q* 轴电流（安培）。
- τr 是转子时间常量（秒）。
- λrd 是转子的 *d* 轴磁链（韦伯）。
