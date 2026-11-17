---
type: simulink-block
title: '6-Phase Inverse VSD Transform'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: '6phaseinversevsdtransform'
documentation_source_path: '../mcb/ref/6phaseinversevsdtransform.html'
language: zh-CN
chinese_source: worker-translation
---

# 6-Phase Inverse VSD Transform

## 端口

### 输入

### **αβxyz+z-** — 三个不同子空间中的六轴正交分量 标量

以下三个子空间中的六轴正交输入分量（*α*、
*β*、*x*、*y*、
*z+* 和
*z-*）：

- *α*-*β* 子空间（包含
  *α* 和 *β* 分量）
- *x*-*y* 子空间（包含
  *x* 和 *y* 分量）
- 零序子空间（包含
  *z+* 和
  *z-* 分量）

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **a1b1c1** — 第一组三相输出 标量

第一组三相输出，使得相位 *a1* 轴
与 *α* 轴对齐。对于六相 PMSM，此端口
输出属于第一个三相绕组组的三相定子电压或电流。

**数据类型：** `single` | `double` | `fixed point`

### **a2b2c2** — 第二组三相输出 标量

第二组三相输出。对于六相 PMSM，此端口输出
属于第二个三相绕组组的三相定子电压或电流。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Power invariant** — 启用功率不变变换的选项 `off`（默认）| on

选择此参数以使模块能够使用功率不变
变换。如果清除此参数，模块将使用幅值不变
变换。

### **Motor type** — 六相 PMSM 的类型 `Asymmetric (30 degree offset)`（默认）| `Symmetric (60 degree offset)`

选择要为其计算逆 VSD
变换的六相 PMSM 类型。

## 所属库

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现
和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024b 中引入**

## 描述

对正交输入计算基于矢量空间分解 (VSD) 的逆变换

6-Phase Inverse VSD Transform 模块对正交输入（*α*、*β*、*x*、*y*、*z+* 和 *z-*）应用逆矢量空间分解 (VSD) 变换，以计算六相输出（*a1*、*b1*、*c1*、*a2*、*b2* 和 *c2*）。

六个正交输入分量属于以下三个子空间：

- *α*-*β* 子空间（包含 *α* 和 *β* 分量）
- *x*-*y* 子空间（包含 *x* 和 *y* 分量）
- 零序子空间（包含 *z+* 和 *z-* 分量）

该模块将六个信号输出为两组三相信号。

您可以使用该模块，通过六个正交输入分量来确定非对称或对称六相永磁同步电机 (PMSM) 的六相定子电压或电流。例如，您可以使用该模块，根据电流 PI 控制器生成的 *α*、*β*、*x* 和 *y* 参考电压分量来确定参考六相定子电压。因此，您可以使用该模块来实现非对称六相 PMSM 的磁场定向控制 (FOC)。有关详细信息，请参阅 Field-Oriented Control of Six-Phase PMSM。

六相电机根据两组三相绕组之间的空间角度（或空间位移）具有不同的配置。非对称六相 PMSM 使用 30 电角度的空间角度，而对称六相 PMSM 使用 60 电角度的空间角度。

下图显示了输入信号 *α* 和 *β* 与输出信号 *a1* 和 *b1* 之间的比较。

有关该模块算法的详细信息，请参阅算法。
