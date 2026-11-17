---
type: simulink-block
title: 'ACIM Slip Speed Estimator'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'acimslipspeedestimator'
documentation_source_path: '../mcb/ref/acimslipspeedestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# ACIM Slip Speed Estimator

## 端口
```yaml
ports:
- name: Isdref
  summary: 参考 *d* 轴定子电流标量
  direction: input
  data_types: single | double | fixed point
- name: Isqref
  summary: 参考 *q* 轴定子电流标量
  direction: input
  data_types: single | double | fixed point
- name: ⍵mslip
  summary: 感应电机转差速度标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **Isdref** — 参考 *d* 轴定子电流标量

参考 *d* 轴定子电流。

**数据类型：** `single` | `double` | `fixed point`

### **Isqref** — 参考 *q* 轴定子电流标量

参考 *q* 轴定子电流。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **⍵mslip** — 感应电机转差速度标量

该模块计算的转子机械转差速度。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of pole pairs
  summary: 电机中可用的极对数 2（默认）| 标量
  group: ''
- name: Rotor resistance (Ohm)
  summary: 电机转子电阻 1.05（默认）| 标量
  group: ''
- name: Rotor leakage inductance (H)
  summary: 转子绕组漏电感 6.81e-3（默认）| 标量
  group: ''
- name: Magnetizing inductance (H)
  summary: 感应电机励磁电感 30e-3（默认）| 标量
  group: ''
- name: Output saturation (rpm)
  summary: 模块输出的饱和值 150（默认）| 标量
  group: ''
- name: Input units
  summary: 输入值的单位 Per-Unit (PU)（默认）| SI Units
  group: ''
- name: Base speed (rpm)
  summary: 标幺制系统的基速 1500（默认）| 标量
  group: ''
```

### **Number of pole pairs** — 电机中可用的极对数 `2`（默认）| 标量

感应电机中可用的极对数。

### **Rotor resistance (Ohm)** — 电机转子电阻 `1.05`（默认）| 标量

感应电机的转子电阻，单位为欧姆。

### **Rotor leakage inductance (H)** — 转子绕组漏电感 `6.81e-3`（默认）| 标量

与转子绕组交链的漏磁通引起的电感（单位为亨利）。

### **Magnetizing inductance (H)** — 感应电机励磁电感 `30e-3`（默认）| 标量

励磁磁通引起的电感（单位为亨利）。

### **Output saturation (rpm)** — 模块输出的饱和值 `150`（默认）| 标量

模块输出的饱和值（单位为 rpm）。

### **Input units** — 输入值的单位 `Per-Unit (PU)`（默认）| SI Units

输入值的单位。

### **Base speed (rpm)** — 标幺制系统的基速 `1500`（默认）| 标量

标幺制系统的基速（单位为 rpm）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。
## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020b 中引入**

## 描述

计算交流感应电机的转差速度

ACIM Slip Speed Estimator 模块计算感应电机的机械转差速度
（同步速度与转子速度之差）。

该模块接受 *d* 轴和
*q* 轴电流的参考值，并输出感应电机
的计算转差速度。

### 方程

这些方程描述了感应电机磁场定向控制 (FOC) 中滑差速度值的利用：

τr= (LrRr)

ωe\_slip= (Lm⋅isqrefτr⋅λrd)

ωe= ωr+ωe\_slip

θe= ∫ωe⋅ dt=∫(ωr+ωe\_slip)⋅dt=θr+θslip

如果我们保持转子磁链恒定，并且 *d* 轴与转子磁链参考坐标系对齐，那么可以推导出：

λrd=Lmisd

该模块将上述计算实现为：

ωslip= (1p)(1τr)(isqrefisdref)

有关详细的方程组和假设，请参见感应电机的数学模型。

其中：

- ωe\_slip 是转子的电滑差速度（弧度/秒）。
- ωslip 是转子的机械滑差速度（弧度/秒）。
- ωe 是对应于定子电压频率的电速度（弧度/秒）。
- ωm 是转子机械速度（弧度/秒）。
- ωr 是转子电速度（弧度/秒）。
- Lm 是电机的励磁电感（亨利）。
- Rr 是折算到定子的转子电阻（欧姆）。
- isdref 和 isqref 是参考定子 *d* 轴和 *q* 轴电流（安培）。
- τr 是转子时间常数（秒）。
- λrd 是转子的 *d* 轴磁链（韦伯）。
