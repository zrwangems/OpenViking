---
type: simulink-block
title: 'Quaternion Interpolation'
family: 'utilities'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaternioninterpolation'
documentation_source_path: 'quaternioninterpolation.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternion Interpolation

## 端口

### 输入

### **q0** — 第一个归一化四元数 4-by-1 向量 | 1-by-4 向量

用于计算插值的第一个归一化四元数。
此四元数必须是归一化四元数

**数据类型：** `double`

### **q1** — 第二个归一化四元数 4-by-1 向量 | 1-by-4 向量

用于计算插值的第二个归一化四元数，
指定为 4-by-1 向量或 1-by-4 向量。此四元数必须是
归一化四元数。

**数据类型：** `double`

### **f** — 区间分数标量

用于计算四元数插值的区间分数。此值在
0 和 1 之间变化。它表示要计算的
四元数的中间旋转。此分数影响插值
方法的旋转速度。

#### 依赖关系

区间分数会影响 **方法** 参数中插值方法的旋转速度。
有关区间分数的更多信息，请参阅 [1]。

**数据类型：** `double`
### 输出

### **qf** — 自然对数向量

四元数的自然对数，以向量形式返回。

**数据类型：** `double`

## 参数

### **方法** — 四元数插值方法 `SLERP`（默认） | `LERP` | `NLERP`

用于计算四元数插值的四元数插值方法，
指定为：

- `SLERP`

  四元数 slerp。球面线性四元数插值
  方法。
- `LERP`

  四元数 lerp。线性四元数插值方法。
- `NLERP`

  归一化四元数线性插值方法。

#### 依赖关系

这些方法具有不同的旋转速度，具体取决于
来自输入端口 f 的区间分数。有关区间
分数的更多信息，请参阅 [1]。

#### 编程用法

|  |
| --- |
| **模块参数**：`method` |
| **类型**：character vector |
| **取值**：`'SLERP'` | `'LERP'` | `'NLERP'` |
| **默认值**：`'SLERP'` |

### **超出范围输入的操作** — 超出范围模块行为 `None`（默认） | `Warning` | `Error`

超出范围模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在 Diagnostic Viewer 中发出警告，模型仿真继续。 |
| `Error`（默认） | 在 Diagnostic Viewer 中报错，模型仿真停止。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **取值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

## 所属库

Aerospace Blockset / Utilities / Math Operations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

两个四元数之间的四元数插值

Quaternion Interpolation 模块按区间分数计算
两个归一化四元数之间的四元数插值。Aerospace Blockset™ 使用采用 scalar-first 约定的四元数。
从 SLERP、LERP 或 NLERP 中选择插值方法。有关
插值方法使用的方程，请参阅 Algorithms。

这两个归一化四元数是该模块计算四元数时所介于的两个端点。
