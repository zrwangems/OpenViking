---
type: simulink-block
title: 'atan2'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'atan2'
documentation_source_path: 'ref/atan2.html'
language: zh-CN
chinese_source: official
---

# atan2

## 端口

### 输入

### **A** — y 坐标值（实数） 标量

作为模块的输入提供的 y 轴上的实数。

**数据类型:** `single` | `double` | `fixed point`

### **B** — x 坐标值（实数） 标量

作为模块的输入提供的 x 轴上的实数。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **θ** — 反正切表示的角度 标量

反正切表示的角度。这是一个从原点到指定点 (x,y) 的矢量与正 x 轴所形成的夹角。

**数据类型:** `single` | `double` | `fixed point`

下图显示了输入值 A、B 和反正切在 x-y 坐标平面上的表示。

## 参数

### **逼近方法** — 用于 atan2 计算的逼近类型 **无** (默认) | **CORDIC** | **查找**

模块用于 atan2 计算的逼近类型：

- **无** - 模块不使用任何逼近。
- **CORDIC** - 模块使用基于坐标旋转数字计算 (CORDIC) 算法的逼近。
- **查找** - 模块使用基于查找表的逼近。

**注意**

使用模块生成代码时：

- **无** 选项更适合单精度数据类型。
- **CORDIC** 选项更适合 FPGA 部署。
- **查找** 选项更适合定点数据类型。

### **输出单位** — 输出值的单位 **弧度** (默认) | **标幺**

输出值的单位。

## 所属库

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

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

**限制**

如果您运行第三方 (3p) 仿真，则由于内部三角函数使用浮点数据类型，该模块可能会在仿真结果中显示微小的不匹配（`1e-7` 数量级）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

计算四象限反正切

atan2 模块对两个实数执行四象限反正切运算。

### 方程

此方程描述该模块如何计算四象限反正切值 (`θ`)。

Theta=atan2(A,B)={arctan(AB)                 if B>0,arctan(AB)+π           if B<0 and A≥0,arctan(AB)−π           if B<0 and A<0,+π2                            if B=0 and A>0, −π2                            if B=0 and A<0,undefined                 if B=0 and A=0.

其中：

−π<Theta≤π    (Radians)
