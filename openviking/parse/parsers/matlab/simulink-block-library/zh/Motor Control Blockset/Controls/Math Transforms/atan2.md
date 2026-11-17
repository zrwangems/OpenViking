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
chinese_source: worker-translation
---

# atan2

## 端口
```yaml
ports:
- name: A
  summary: y 坐标值（实数）标量
  direction: input
  data_types: single | double | fixed point
- name: B
  summary: x 坐标值（实数）标量
  direction: input
  data_types: single | double | fixed point
- name: θ
  summary: 由反正切表示的角度 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **A** — y 坐标值（实数）标量

y 轴上的实数，作为模块的输入提供。

**数据类型：** `single` | `double` | `fixed point`

### **B** — x 坐标值（实数）标量

x 轴上的实数，作为模块的输入提供。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **θ** — 由反正切表示的角度 标量

由反正切表示的角度。这是从原点到指定点 (x,y) 的向量与 x 轴正方向所成的角度。

**数据类型：** `single` | `double` | `fixed point`

下图展示了输入值 A、B 以及反正切在 x-y 坐标平面上的表示。
## 参数
```yaml
parameters:
- name: Approximation method
  summary: 用于 atan2 计算的近似类型 None（默认）| CORDIC | Lookup
  group: ''
- name: Output unit
  summary: 输出值的单位 Radians（默认）| PerUnit
  group: ''
```

### **Approximation method** — 用于 atan2 计算的近似类型 `None`（默认）| `CORDIC` | `Lookup`

模块用于 atan2 计算的近似类型：

- `None` — 模块不使用任何近似。
- `CORDIC` — 模块使用基于坐标旋转数字计算机（CORDIC）算法的近似。
- `Lookup` — 模块使用基于查找表的近似。

**注意**

当您将模块用于代码生成时：

- `None` 选项更适合 single 数据类型。
- `CORDIC` 选项更适合 FPGA 部署。
- `Lookup` 选项更适合定点数据类型。

### **Output unit** — 输出值的单位 `Radians`（默认）| `PerUnit`

输出值的单位。
## 所属库

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

**限制**

如果运行第三方（3p）仿真，由于使用浮点数据类型的内部三角函数，模块可能会在仿真结果中显示轻微不匹配（约为 `1e-7` 量级）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

计算四象限反正切

atan2 模块对两个实数执行四象限反正切。

### 方程

此方程描述了模块如何计算四象限反正切（`θ`）。

Theta=atan2(A,B)={arctan(AB)                 if B>0,arctan(AB)+π           if B<0 and A≥0,arctan(AB)−π           if B<0 and A<0,+π2                            if B=0 and A>0, −π2                            if B=0 and A<0,undefined                 if B=0 and A=0.

其中：

−π<Theta≤π    (Radians)
