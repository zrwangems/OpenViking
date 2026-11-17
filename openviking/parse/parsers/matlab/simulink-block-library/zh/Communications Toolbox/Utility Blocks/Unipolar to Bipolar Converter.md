---
type: simulink-block
title: 'Unipolar to Bipolar Converter'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'unipolartobipolarconverter'
documentation_source_path: 'ref/unipolartobipolarconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Unipolar to Bipolar Converter

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32
- name: Out
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
```

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。该模块期望输入整数在范围 [0, (*M* – 1)] 内，其中 *M* 是 **M-ary number** 参数。

输入信号在模块掩码上未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32`
### 输出

### **Out** — 输出信号 标量 | 向量 | 矩阵

输出信号，返回为整数信号，范围为 [–(*M* – 1), (*M* – 1)]，其维度与输入信号 **In** 相同。*M* 是 **M-ary number** 参数值。**Output data type** 参数指定所需的数据类型。

- 当将 *M* 设置为偶数整数时，该模块输出奇数整数值。
- 当将 *M* 设置为奇数整数时，该模块输出偶数整数值。

输出信号在模块掩码上未命名。

**注意**

对于无符号整数输入值、非整数输入值或超出范围 [0, (*M* – 1)] 的整数输入值，输出可能无效。
## 参数
```yaml
parameters:
- name: M-ary number
  summary: 符号数量 4（默认）| 正整数
  group: ''
- name: Polarity
  summary: 符号的相对顺序 Positive（默认）| Negative
  group: ''
- name: Output data type
  summary: 双极性信号的输出数据类型 Inherit via internal rule（默认）| Same as input | double | int8 | int16 | int32
  group: ''
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **M-ary number** — 符号数量 `4`（默认）| 正整数

双极性或单极性字母表中的符号数量，指定为正整数。

### **Polarity** — 符号的相对顺序 `Positive`（默认）| `Negative`

符号的相对顺序，指定为 `Positive` 或 `Negative`。

- `Positive` 使模块保持字母表中符号的相对顺序。
- `Negative` 使模块反转字母表中符号的相对顺序。

此参数的值决定了输入值 *k* 和 **M-ary number** 参数值 *M* 的输出。

|  | 输出 |
| --- | --- |
| `Positive` | 2*k* – (*M* – 1) |
| `Negative` | –2*k* + (*M* – 1) |

### **Output data type** — 双极性信号的输出数据类型 `Inherit via internal rule`（默认）| `Same as input` | `double` | `int8` | `int16` | `int32`

双极性信号的输出数据类型，指定为 `Inherit via internal rule`、`Same as input`、`double`、`int8`、`int16` 或 `int32`。

当将此参数设置为 `Inherit via internal rule` 时，该模块根据输入数据类型确定输出数据类型，如下所示：

- 如果输入数据类型为 `single` 或 `double`，则输出数据类型与输入数据类型相同。
- 如果输入数据类型不是 `single` 或 `double`：

  - 对于 **M-ary number** 参数值 *M*，该模块计算包含范围 [–(*M* – 1), (*M* – 1)] 所需的理想有符号整数输出字长 *ideal\_word\_length*，如下所示：

    `ideal_word_length = ceil(log2(M)) + 1`，其中 `+ 1` 满足符号位的需要。
  - 该模块根据能最好地适应所计算理想字长的最小字长（以位为单位），将输出数据类型设置为有符号整数。

**注意**

Hardware Implementation Pane (Simulink) 中约束字长的选择不会影响此模块确定输出数据类型的方式。
## 所属库

Communications Toolbox / Utility Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将范围 [0, M – 1] 内的单极性信号映射为双极性信号

Unipolar to Bipolar Converter 模块将单极性输入信号映射为双极性输出信号。
