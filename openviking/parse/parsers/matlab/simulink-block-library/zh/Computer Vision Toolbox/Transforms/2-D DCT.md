---
type: simulink-block
title: '2-D DCT'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: '2ddct'
documentation_source_path: 'ref/2ddct.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D DCT

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入数据矩阵 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出数据矩阵 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入数据矩阵 | 向量

输入数据，指定为数值矩阵或向量。输入数据的大小必须为 2 的幂。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出数据矩阵 | 向量

包含 DCT 系数的输出数据，以矩阵或向量形式返回。输出的大小和数据类型与输入相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Sine and cosine computation
  summary: 指定模块如何计算正弦和余弦项 Table lookup（默认）| Trigonometric fcn
  group: ''
- name: Rounding mode
  summary: 定点表示的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: ''
- name: Saturate on integer overflow
  summary: 指定溢出模式 关（默认）| 开
  group: ''
- name: Sine Table
  summary: '正弦表的数据类型 Inherit: Same word length as input（默认）| fixdt(1,16) | <data type expression>'
  group: ''
- name: Product output
  summary: '乘积输出的数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt(1,16,0) | <data type expression>'
  group: ''
- name: Accumulator
  summary: '累加器的数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt(1,16,0)
    | <data type expression>'
  group: ''
- name: Output
  summary: '输出的数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt(1,16,0) | <data type expression>'
  group: ''
- name: Lock data type settings against change by the fixed-point tools
  summary: 数据类型覆盖 关（默认）| 开
  group: ''
```

**主选项卡**

### **Sine and cosine computation** — 指定模块如何计算正弦和余弦项 `Table lookup`（默认）| `Trigonometric fcn`

使用此参数指定模块在 DCT 算法中如何计算正弦和余弦项。

- 如果选择 `Trigonometric fcn`，模块在仿真期间计算正弦和余弦值。
- 如果选择 `Table lookup`，模块在仿真开始前计算并存储三角函数值。在这种情况下，模块需要额外的内存。`Table lookup` 为默认值。

**数据类型选项卡**

#### 定点运算参数

### **Rounding mode** — 定点表示的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

使用此参数指定当指定的数据类型和定标无法精确表示定点计算结果时，模块所使用的舍入模式。有关可用值的详细信息，请参阅舍入模式。

**注意**

正弦表值不遵循此参数；它们始终舍入到 `Nearest`。

### **Saturate on integer overflow** — 指定溢出模式 关（默认）| 开

选中此参数时，模块对其定点运算的结果进行饱和处理。清除此参数时，模块对其定点运算的结果进行回绕处理。

有关饱和与回绕的详细信息，请参阅定点运算的溢出处理。

**注意**

正弦表值不遵循此参数；它们始终进行饱和处理。

#### 定点数据类型

### **Sine Table** — 正弦表的数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16)` | `<data type expression>`

使用此参数指定正弦表值的字长。正弦表值的小数长度始终等于字长减一。

正弦表值不遵循 **Rounding mode** 和 **Saturate on integer overflow** 参数；它们始终进行饱和处理并舍入到 `Nearest`。

### **Product output** — 乘积输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)` | `<data type expression>`

使用此参数指定乘积输出数据类型。有关说明此模块中乘积输出数据类型使用的图示，请参阅定点数据类型和乘法数据类型。

### **Accumulator** — 累加器的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)` | `<data type expression>`

使用此参数指定累加器数据类型。有关说明此模块中累加器数据类型使用的图示，请参阅定点数据类型。

### **Output** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)` | `<data type expression>`

使用此参数指定输出数据类型。有关说明此模块中输出数据类型使用的图示，请参阅定点数据类型。将此参数设置为

- `Inherit: Inherit via internal rule` 时，模块自动计算输出字长和小数长度。内部规则首先使用以下公式计算理想的输出字长和小数长度：

  WLideal output=WLinput+floor(log2(DCT length−1))+1

  FLideal output=FLinput

  使用这些理想结果，内部规则随后选择适合您硬件的字长和小数长度。有关详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 数据类型覆盖 关（默认）| 开

选中此参数可防止定点工具覆盖您在模块封装上指定的数据类型。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)，即定点工具参考页。
## 所属库

Computer Vision Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算二维离散余弦变换（DCT）

2-D DCT 模块计算图像的二维离散余弦变换。假设 *f*(*x*,*y*) 是维度为 *M*×*N* 的输入图像，二维 DCT 的公式为

F(m,n)=2MNC(m)C(n)∑x=0M−1∑y=0N−1f(x,y)cos(2x+1)mπ2Mcos(2y+1)nπ2N

其中当 m,n=0 时 C(m)=C(n)=1/2，否则 C(m),C(n)=1。

输入图像的行数和列数必须为 2 的幂。您也可以使用此模块计算向量的 1-D DCT。
