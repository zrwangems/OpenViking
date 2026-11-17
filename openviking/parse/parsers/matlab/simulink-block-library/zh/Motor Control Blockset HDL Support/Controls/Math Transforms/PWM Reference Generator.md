---
type: simulink-block
title: 'PWM Reference Generator'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'pwmreferencegenerator'
documentation_source_path: '../mcb/ref/pwmreferencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Reference Generator

## 端口

### 输入

### **Vα** — *α* 轴定子参考电压分量标量

*αβ* 参考坐标系中沿 *α* 轴的定子参考电压分量。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为
`Valphabeta`。

**数据类型：** `single` | `double` | `fixed point`

### **Vβ** — *β* 轴定子参考电压分量标量

*αβ* 参考坐标系中沿 *β* 轴的定子参考电压分量。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为
`Valphabeta`。

**数据类型：** `single` | `double` | `fixed point`

### **Va** — 相分量标量

*abc* 参考坐标系中三相系统的分量。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为
`Vabc`。

**数据类型：** `single` | `double` | `fixed point`

### **Vb** — 相分量标量

*abc* 参考坐标系中三相系统的分量。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为
`Vabc`。

**数据类型：** `single` | `double` | `fixed point`

### **Vc** — 相分量标量

*abc* 参考坐标系中三相系统的分量。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为
`Vabc`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Vao** — *a* 轴定子参考电压分量标量

*abc* 参考坐标系中沿 *a* 轴的定子参考电压分量。

**数据类型：** `single` | `double` | `fixed point`

### **Vbo** — *b* 轴定子参考电压分量标量

*abc* 参考坐标系中沿 *b* 轴的定子参考电压分量。

**数据类型：** `single` | `double` | `fixed point`

### **Vco** — *c* 轴定子参考电压分量标量

*abc* 参考坐标系中沿 *c* 轴的定子参考电压分量。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Input type** — 模块输入类型 `Valphabeta`（默认）| `Vabc` | `Degrees`

模块用作输入的三相定子电压表示类型。
选择 *abc* 或 *αβ* 参考坐标系。

### **Modulation method** — 脉宽调制 (PWM) 方法 `SVM: space vector modulation`（默认）| `SPWM: sinusoidal PWM` | `60 DPWM:60 degree discontinuous PWM` | `60 DPWM (+30 degree shift):+30 degree shift from 60 DPWM` | `60 DPWM (-30 degree shift):-30 degree shift from 60 DPWM` | `30 DPWM: 30 degree discontinuous PWM` | `120 DPWM: positive DC component` | `120 DPWM: negative DC component`

模块用于调制输入定子相电压或参考电压的脉宽调制 (PWM) 方法。

## 所属库

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**支持的模块参数**

对于 PWM Reference Generator 模块的 HDL 代码生成，将 **Modulation method** 设置为 `SVM: space vector modulation` 或 `SPWM: sinusoidal PWM`。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除 PWM Reference Generator 模块层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

从相电压生成调制信号

PWM Reference Generator 模块从定子相电压或参考电压生成调制电压信号。

该模块接受由 *α-β* 电压分量描述的相电压（*Vabc*）或定子参考电压（*Vαβ*）。

使用此模块执行正弦 PWM (SPWM) 和空间矢量调制 (SVM)，以及以下减少开关损耗的离散脉宽调制 (DPWM) 方法：

**注意**

对于以下 DPWM 方法，该模块仅支持标幺 (PU) 输入信号。有关标幺系统的更多信息，请参阅 Per-Unit System。

- 60 DPWM — 60 度不连续 PWM
- 60 DPWM (+30 degree shift) — 从 60 DPWM 偏移 +30 度
- 60 DPWM (-30 degree shift) — 从 60 DPWM 偏移 -30 度
- 30 DPWM — 30 度不连续 PWM
- 120 DPWM — 正直流分量
- 120 DPWM — 负直流分量

对于不连续 PWM (DPWM)，该模块在每个基波周期内每相将调制波钳位到正或负直流母线总计 120 度。在每个钳位区间内，调制不连续。

该图显示了正弦 PWM (SPWM) 波形。

该图显示了空间矢量调制 (SVM) 波形。

该图显示了每个基波周期具有两个 60 度钳位区间的 60 度 DPWM 波形。

该图显示了具有正 30 度相移的 60 度 DPWM 波形。

该图显示了具有负 30 度相移的 60 度 DPWM 波形。

该图显示了每个基波周期具有四个 30 度钳位区间的 30 度 DPWM 波形。

该图显示了具有正直流钳位的 120 度 DPWM 波形。

该图显示了具有负直流钳位的 120 度 DPWM 波形。
