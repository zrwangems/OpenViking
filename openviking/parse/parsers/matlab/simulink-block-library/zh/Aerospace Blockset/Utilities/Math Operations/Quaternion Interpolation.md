---
type: simulink-block
title: 'Quaternion Interpolation'
family: 'aeroblks'
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

### **q0** — 第一个归一化四元数 4×1 向量 | 1×4 向量

用于计算插值的第一个归一化四元数。
该四元数必须是归一化四元数

**数据类型：** `double`

### **q1** — 第二个归一化四元数 4×1 向量 | 1×4 向量

用于计算插值的第二个归一化四元数，
指定为 4×1 向量或 1×4 向量。该四元数必须是
归一化四元数。

**数据类型：** `double`

### **f** — 区间分数 标量

用于计算四元数插值的区间分数。该值在
0 和 1 之间变化。它表示待计算四元数的
中间旋转。该分数影响插值
方法的旋转速度。

#### 依赖关系

区间分数影响 **Methods** 参数的插值方法的
旋转速度。有关区间分数的更多信息，
请参阅 [1]。

**数据类型：** `double`
### 输出

### **qf** — 自然对数 向量

四元数的自然对数，以向量形式返回。

**数据类型：** `double`

## 参数

### **Methods** — 四元数插值方法 `SLERP`（默认）| `LERP` | `NLERP`

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
输入端口 f 的区间分数。有关区间
分数的更多信息，请参阅 [1]。

#### 编程用法

|  |
| --- |
| **模块参数**：`method` |
| **类型**：字符向量 |
| **值**：`'SLERP'` | `'LERP'` | `'NLERP'` |
| **默认值**：`'SLERP'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `None`（默认）| `Warning` | `Error`

超出范围时的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 不执行任何操作。 |
| `Warning` | 在诊断查看器中显示警告，模型仿真继续。 |
| `Error`（默认） | 在诊断查看器中显示错误，模型仿真停止。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`action` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

## 所属库

Aerospace Blockset / Utilities / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

两个四元数之间的四元数插值

Quaternion Interpolation 模块通过区间分数计算两个归一化四元数之间的
四元数插值。Aerospace Blockset™ 使用采用标量优先约定的
四元数。从 SLERP、LERP 或 NLERP 中选择插值方法。有关
插值方法所使用的方程，请参阅算法。

两个归一化四元数是该模块计算四元数插值的
两个端点。
