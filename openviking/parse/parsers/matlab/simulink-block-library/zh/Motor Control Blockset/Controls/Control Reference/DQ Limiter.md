---
type: simulink-block
title: 'DQ Limiter'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'dqlimiter'
documentation_source_path: '../mcb/ref/dqlimiter.html'
language: zh-CN
chinese_source: official
---

# DQ Limiter

## 端口

### 输入

### **dref** — 参考 *d* 轴电压（或电流） 标量

沿旋转 *dq* 参考系的 *d* 轴的参考电压（或电流）值。

**数据类型:** `single` | `double` | `fixed point`

### **qref** — 参考 *q* 轴电压（或电流） 标量

沿旋转 *dq* 参考系的 *q* 轴的参考电压（或电流）值。

**数据类型:** `single` | `double` | `fixed point`

### **satMethod** — 饱和方法 标量

模块用于启动饱和的饱和方法。端口接受以下整数值之一：

- 1 - D 轴优先
- 2 - Q 轴优先
- 任何其他正整数 - D-Q 等效方法

#### 依赖关系

要启用此端口，请为**饱和方法**参数选择**输入端口**。

**数据类型:** `uint16`

### **satLim** — 饱和界限 标量

模块用于启动饱和的饱和限值。端口接受大于或等于 0 的值。

#### 依赖关系

要启用此端口，请为**饱和界限**参数选择**输入端口**。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **dsat** — 饱和 *d* 轴电压（或电流） 标量

沿旋转 *dq* 参考系的 *d* 轴的饱和电压（或电流）值。

**数据类型:** `single` | `double` | `fixed point`

### **qsat** — 饱和 *q* 轴电压（或电流） 标量

沿旋转 *dq* 参考系的 *q* 轴的饱和电压（或电流）值。

**数据类型:** `single` | `double` | `fixed point`

### **magref** — 模块输入的非饱和峰值 标量

输入电压（或电流）的非饱和峰值。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **饱和方法** — 饱和方法选择方式 `Specify via dialog` (默认) | `Input port`

选择模块应使用对话框还是输入端口来指定饱和方法。

#### 编程用法

```
satMethodInputType
```

### **选定的饱和方法** — 模块使用的饱和方法 `D-Q equivalence` (默认) | `Prioritize D axis` | `Prioritize Q axis`

选择模块应使用的饱和方法。

#### 依赖关系

要启用此参数，请将**饱和方法**设置为**通过对话框指定**。

#### 编程用法

```
satMethodSelected
```

### **饱和界限** — 饱和界限选择方式 `Specify via dialog` (默认) | `Input port`

选择模块应使用对话框还是输入端口来指定饱和界限。

#### 编程用法

```
satLimitInputType
```

### **饱和限值** — 相电压（或电流）峰值限值 `1` (默认) | 标量

电压（或电流）的最大幅值，超出该值时模块输出将受限。

D−Q saturation limit (current) 通常是电机的额定电流。当您使用标幺制 (PU) 时，您应将电机的额定电流转换为关于基电流的标幺值。

D−Q saturation limit (voltage) 通常是逆变器提供的最大相电压。通常，对于空间矢量 PWM，该值为 Vdc3；对于正弦 PWM，该值为 Vdc2，其中 Vdc 是逆变器的 DC 母线电压。

**注意**

您可以在此参数中输入标幺单位或 SI 单位电压（或电流）值（输入值的单位应与 *dref* 和 *qref* 输入的单位相同）。为了获得最优性能，我们建议您提供标幺单位值。

#### 依赖关系

要启用此参数，请将**饱和界限**设置为**通过对话框指定**。

#### 编程用法

```
Vmax
```

## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**支持的模块参数**

对于涉及 DQ Limiter 模块的 HDL 代码生成，请设置以下参数：

- 将**饱和方法**设置为**通过对话框指定**
- 将**选定的饱和方法**设置为  **D-Q 等效**
- 将**饱和界限**设置为**通过对话框指定**

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 要通过移动设计中的现有延迟来放置在输出端的寄存器的数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中删除 DQ Limiter 模块层次结构。默认值为**继承**。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

dq 参考系中的饱和电压（或电流）

DQ Limiter 模块根据指定的饱和界限与所选饱和方法，在 *dq* 参考系中生成输入电压（或电流）的饱和值。

该模块接受 *d* 轴和 *q* 轴电压（或电流）的参考值，并输出对应的饱和值。该模块还提供参考 *dq* 电压（或电流）的非饱和峰值，可用于启用弱磁控制。

**注意**

该模块支持最大 128 位的定点数据类型。

### 方程

下列方程描述模块对饱和 *dq* 电压（或电流）值的计算。

**对于 DQ 等效性：**

magref=(dref)2+(qref)2

当 magref>xmax 时。

- dsat=drefmagref×xmax
- qsat=qrefmagref×xmax

当 magref≤xmax 时。

- dsat=dref
- qsat=qref

其中，*xmax* 是饱和界限。

**当 D 轴优先时：**

magref=(dref)2+(qref)2

dsat=min(max(dref,−xmax),xmax)qsat=sign(qref)×min(|qref|,|xmax2−(dsat)2|)

其中，*xmax* 是饱和界限。

**当 Q 轴优先时：**

magref=(dref)2+(qref)2

qsat=min(max(qref,−xmax),xmax)dsat=sign(dref)×min(|dref|,|xmax2−(qsat)2|)

其中，*xmax* 是饱和界限。
