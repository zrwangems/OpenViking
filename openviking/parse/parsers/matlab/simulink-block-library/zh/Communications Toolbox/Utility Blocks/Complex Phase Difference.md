---
type: simulink-block
title: 'Complex Phase Difference'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'complexphasedifference'
documentation_source_path: 'ref/complexphasedifference.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Phase Difference

## 端口
```yaml
ports:
- name: In1
  summary: 第一个输入信号 标量 | 列向量 | 矩阵
  direction: input
  data_types: double | single
- name: In2
  summary: 第二个输入信号 标量 | 列向量 | 矩阵
  direction: input
  data_types: double | single
- name: Out1
  summary: 相位差 标量 | 列向量 | 矩阵
  direction: output
```

### 输入

### **In1** — 第一个输入信号 标量 | 列向量 | 矩阵

第一个输入信号，指定为标量、列向量或矩阵。
如果两个输入信号均为非标量，则它们必须具有相同的维度。

**注意**

此模块处理复信号。输入端口的实数值会被类型转换为具有
`+j0` 复数分量的复数值。

**数据类型：** `double` | `single`
**复数支持：** 是

### **In2** — 第二个输入信号 标量 | 列向量 | 矩阵

第二个输入信号，指定为标量、列向量或矩阵。
如果两个输入信号均为非标量，则它们必须具有相同的维度。
**In2** 必须与 **In1** 具有相同的数据类型。

**注意**

此模块处理复信号。输入端口的实数值会被类型转换为具有
`+j0` 复数分量的复数值。

**数据类型：** `double` | `single`
### 输出

### **Out1** — 相位差 标量 | 列向量 | 矩阵

以弧度表示的相位差，返回为标量、列向量或矩阵。如果任一输入信号为非标量，则输出
信号的维度与非标量输入信号的维度匹配。
输出是第二个输入信号与第一个输入信号之间的相位差。输出信号的元素介于 -π
和 π 之间，并且与输入信号具有相同的数据类型。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Communications Toolbox / Utility Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

两个复信号之间的相位差

Complex Phase Difference 模块计算第二个输入信号与第一个输入信号之间以弧度表示的相位差。输出的元素介于 -π 和
π 之间。此模块独立处理每一对对应的元素。
