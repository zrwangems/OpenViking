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
chinese_source: worker-translation
---

# DQ Limiter

## 端口

### 输入

### **dref** — 参考 *d* 轴电压（或电流）标量

沿旋转 *dq* 参考坐标系 *d* 轴的参考电压（或电流）值。

**数据类型：** `single` | `double` | `fixed point`

### **qref** — 参考 *q* 轴电压（或电流）标量

沿旋转 *dq* 参考坐标系 *q* 轴的参考电压（或电流）值。

**数据类型：** `single` | `double` | `fixed point`

### **satMethod** — 饱和技术标量

模块用于启动饱和的饱和方法。该端口接受以下整数值之一：

- 1 – 优先 D 轴
- 2 – 优先 Q 轴
- 任何其他正整数 – D-Q 等效方法

#### 依赖关系

要启用此端口，请为 **Saturation method** 参数选择 `Input port`。

**数据类型：** `uint16`

### **satLim** — 饱和限值标量

模块用于启动饱和的饱和限值。该端口接受大于或等于 0 的值。

#### 依赖关系

要启用此端口，请为 **Saturation limit** 参数选择 `Input port`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **dsat** — 饱和 *d* 轴电压（或电流）标量

沿旋转 *dq* 参考坐标系 *d* 轴的饱和电压（或电流）值。

**数据类型：** `single` | `double` | `fixed point`

### **qsat** — 饱和 *q* 轴电压（或电流）标量

沿旋转 *dq* 参考坐标系 *q* 轴的饱和电压（或电流）值。

**数据类型：** `single` | `double` | `fixed point`

### **magref** — 模块输入的非饱和峰值标量

输入电压（或电流）的非饱和峰值。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Saturation method** — 饱和方法选择技术 `Specify via dialog`（默认）| `Input port`

选择模块应使用对话框还是输入端口来指定饱和方法。

#### 编程使用

```
satMethodInputType
```

### **Saturation method selected** — 模块使用的饱和方法 `D-Q equivalence`（默认）| `Prioritize D axis` | `Prioritize Q axis`

选择模块应使用的饱和方法。

#### 依赖关系

要启用此参数，请将 **Saturation method** 设置为 `Specify via dialog`。

#### 编程使用

```
satMethodSelected
```

### **Saturation limit** — 饱和限值选择技术 `Specify via dialog`（默认）| `Input port`

选择模块应使用对话框还是输入端口来指定饱和限值。

#### 编程使用

```
satLimitInputType
```

### **Saturation limit value** — 相电压（或电流）峰值限值 `1`（默认）| 标量

模块输出受到限制的最大电压（或电流）幅值。

D−Q 饱和限值（电流）通常是电机的额定电流。当您使用标幺值系统（PU）时，应将电机额定电流转换为相对于基准电流的标幺值。

D−Q 饱和限值（电压）通常是逆变器提供的最大相电压。通常，对于空间矢量 PWM 为 Vdc3，对于正弦 PWM 为 Vdc2，其中 Vdc 是逆变器的直流母线电压。

**注意**

您可以在此参数中输入标幺值或 SI 单位电压（或电流）值（输入值的单位应与 *dref* 和 *qref* 输入的单位相同）。为获得最佳性能，我们建议您提供标幺值。

#### 依赖关系

要启用此参数，请将 **Saturation limit** 设置为 `Specify via dialog`。

#### 编程使用

```
Vmax
```

## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**支持的模块参数**

要使用 DQ Limiter 模块进行 HDL 代码生成，请设置以下参数：

- 将 **Saturation method** 设置为 `Specify via
  dialog`
- 将 **Saturation method selected** 设置为 `D-Q
  equivalence`
- 将 **Saturation limit** 设置为 `Specify via
  dialog`

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除 DQ Limiter 模块层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

在 dq 参考坐标系中饱和电压（或电流）

DQ Limiter 模块根据指定的饱和限值和选定的饱和方法，在 *dq* 参考坐标系中生成输入电压（或电流）的饱和值。

该模块接受 *d* 轴和 *q* 轴电压（或电流）的参考值，并输出相应的饱和值。该模块还提供参考 *dq* 电压（或电流）的未饱和峰值，您可以使用该值来启用弱磁控制。

**注意**

该模块支持最高 128 位的定点数据类型大小。

### 方程

这些方程描述了该模块对饱和 *dq* 电压（或电流）值的计算。

**对于 DQ 等效：**

magref=(dref)2+(qref)2

当 magref>xmax 时。

- dsat=drefmagref×xmax
- qsat=qrefmagref×xmax

当 magref≤xmax 时。

- dsat=dref
- qsat=qref

其中，*xmax* 是饱和限值。

**当优先考虑 D 轴时：**

magref=(dref)2+(qref)2

dsat=min(max(dref,−xmax),xmax)qsat=sign(qref)×min(|qref|,|xmax2−(dsat)2|)

其中，*xmax* 是饱和限值。

**当优先考虑 Q 轴时：**

magref=(dref)2+(qref)2

qsat=min(max(qref,−xmax),xmax)dsat=sign(dref)×min(|dref|,|xmax2−(qsat)2|)

其中，*xmax* 是饱和限值。
