---
type: simulink-block
title: 'Divide by Constant HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'dividebyconstanthdloptimized'
documentation_source_path: '../fixedpoint/ref/dividebyconstanthdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Divide by Constant HDL Optimized

## 端口
```yaml
ports:
- name: X
  summary: 被除数实数标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: validIn
  summary: 输入是否有效布尔标量
  direction: input
  data_types: Boolean
- name: Y
  summary: 除法和舍入运算的结果标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: validOut
  summary: 输出数据是否有效布尔标量
  direction: output
  data_types: Boolean
```

### 输入

### **X** — 被除数实数标量

被除数，指定为实数标量。

定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **validIn** — 输入是否有效布尔标量

输入是否有效，指定为布尔标量。此控制信号指示来自 **X** 输入端口的数据何时有效。当此值为 `1`（`true`）时，模块采集 **X** 输入端口上的值。当此值为 `0`（`false`）时，模块忽略输入采样。

**数据类型：** `Boolean`
### 输出

### **Y** — 除法和舍入运算的结果标量

除法和舍入运算的结果，以标量形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **validOut** — 输出数据是否有效布尔标量

输出数据是否有效，以布尔标量形式返回。当此控制信号的值为 `1`（`true`）时，模块已成功计算输出 **Y**。当此值为 `0`（`false`）时，输出数据无效。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Denominator for rational division
  summary: 除数 10 （默认） | 标量
  group: ''
  block_parameter: Denominator
  type: character vector
  values: MATLAB® expression that evaluates to a positive, real-valued, finite fixed point or numeric value
  default: '''10'''
- name: Rounding Method
  summary: 要使用的舍入方法 Floor （默认） | Ceiling | Nearest | Zero | Convergent
  group: ''
  block_parameter: RndMeth
  type: character vector
  values: '''Floor'' | ''Ceiling'' | ''Nearest'' | ''Zero'' | ''Convergent'''
  default: '''Floor'''
```

### **Denominator for rational division** — 除数 10 （默认） | 标量

除数，指定为正的实值有限标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`Denominator` |
| **类型**：character vector |
| **值**：MATLAB® expression that evaluates to a positive, real-valued, finite fixed point or numeric value |
| **Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **默认值**：`'10'` |

### **Rounding Method** — 要使用的舍入方法 `Floor` （默认） | `Ceiling` | `Nearest` | `Zero` | `Convergent`

要使用的舍入方法，指定为以下值之一：

- `Floor` — 向负无穷方向舍入到最接近的整数。
- `Ceiling` — 向正无穷方向舍入到最接近的整数。
- `Nearest` — 舍入到最接近的整数。出现结值时，向正无穷方向舍入到最接近的整数。
- `Zero` — 向零方向舍入到最接近的整数。
- `Convergent` — 舍入到最接近的整数。出现结值时，舍入到最接近的偶数整数。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`'Floor'` | `'Ceiling'` | `'Nearest'` | `'Zero'` | `'Convergent'` |
| **默认值**：`'Floor'` |
## 所属库

Fixed-Point Designer HDL Support / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟而在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

定点数据类型不支持斜率-偏置表示。

## 版本历史

**在 R2021a 中引入**

## 描述

将输入除以常数并舍入为整数，同时生成优化的 HDL 代码

Divide by Constant HDL Optimized 模块使用 HDL 优化架构以周期精确的延迟输出输入除以常数的结果，并使用指定的舍入方法将结果舍入为整数。

Divide by Constant HDL Optimized 模块使用的算法在功能上类似于 Granlund-Montgomery-Warren 方法。除法运算通过乘以倒数来计算，这通常可在嵌入式系统上获得更好的性能。
