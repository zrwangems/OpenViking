---
type: simulink-block
title: '2-D IDCT'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Filters, Transforms, and Enhancements'
documentation_page: '2didct'
documentation_source_path: 'ref/2didct.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D IDCT

## 端口

### 输入

### **Port\_1** — 输入数据矩阵 | 向量

将输入数据指定为强度值的向量或矩阵。输入数据中的元素数必须为 2 的幂。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### 输出

### **Port\_1** — 输出数据矩阵 | 向量

输出数据包含输入的 2-D IDCT，以矩阵或向量形式返回。输出的大小和数据类型与输入相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

**主要**

### **正弦和余弦计算** — 模块如何计算正弦和余弦项 `Table lookup`（默认） | `Trigonometric fcn`

指定模块如何计算正弦和余弦项以求得 2-D IDCT。

- `Table lookup` — 模块在仿真开始前计算并存储三角函数值。此选项比 `Trigonometric fcn` 选项需要更多内存。
- `Trigonometric fcn` — 模块在仿真期间计算正弦和余弦值。

**数据类型**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **锁定数据类型设置，防止定点工具更改** — 数据类型覆盖 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

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

计算 2-D 离散余弦逆变换 (IDCT)

2-D IDCT 模块计算输入信号的二维离散余弦逆变换。输入信号的二维 IDCT 方程为：

f(x,y)=2MN∑m=0M−1∑n=0N−1C(m)C(n)F(m,n)cos(2x+1)mπ2Mcos(2y+1)nπ2N,

其中 *F*(*m*,*n*) 是信号 *f*(*x*,*y*) 的离散余弦变换 (DCT)。如果 m=n=0，则 C(m)=C(n)=1/2。否则 C(m)=C(n)=1。
