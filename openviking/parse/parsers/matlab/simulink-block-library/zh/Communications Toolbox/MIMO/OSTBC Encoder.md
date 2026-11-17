---
type: simulink-block
title: 'OSTBC Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'MIMO'
documentation_page: 'ostbcencoder'
documentation_source_path: 'ref/ostbcencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# OSTBC Encoder

## 端口
```yaml
ports:
- name: In
  summary: 输入数据列向量 | 矩阵
  direction: input
  data_types: single | double | fixed point
- name: Out
  summary: 输出数据矩阵 | 三维数组
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **In** — 输入数据列向量 | 矩阵

输入数据，指定为具有二次幂斜率和零偏置的值的列向量或矩阵。有关详细信息，请参阅输入到输出维度。

此端口在模块图标上未命名。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是
### 输出

### **Out** — 输出数据矩阵 | 三维数组

输出数据，以矩阵或三维数组形式返回。有关详细信息，请参阅输入到输出维度。

输出信号从输入信号继承数据类型。对于定点信号，**Saturate on integer overflow** 参数指定模块如何处理由复共轭引起的整数溢出。

此端口在模块图标上未命名。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of transmit antennas
  summary: 发射天线数量 2（默认）| 3 | 4
  group: ''
- name: Rate
  summary: 符号速率 3/4（默认）| 1/2
  group: ''
- name: Saturate on integer overflow
  summary: 整数溢出时饱和的选项 关（默认）| 开
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

#### 主要

### **Number of transmit antennas** — 发射天线数量 `2`（默认）| `3` | `4`

发射天线数量，指定为 `2`、`3` 或 `4`。

### **Rate** — 符号速率 `3/4`（默认）| `1/2`

码的符号速率，指定为 `3/4` 或 `1/2`。当您将 **Number of transmit antennas** 设置为 `2` 时，符号速率为 `1`。

#### 依赖关系

要启用此参数，请将 **Number of transmit antennas** 设置为 `3` 或 `4`。

#### 数据类型

### **Saturate on integer overflow** — 整数溢出时饱和的选项 关（默认）| 开

对于定点计算，使用此参数指定当定点计算结果的幅值不适合存储结果的数据类型和定标范围时要使用的方法。

- 要在整数溢出时饱和，请选择此参数。
- 要在整数溢出时环绕，请不要选择此参数。

有关详细信息，请参阅精度和范围。

**数据类型：** `Boolean`
## 所属库

Communications Toolbox / MIMO

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 仅限有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

使用正交空时分组码对输入消息进行编码

OSTBC Encoder 模块使用正交空时分组码（OSTBC）对输入符号序列进行编码。该模块按块映射输入符号，并在时域中串联输出码字矩阵。有关详细信息，请参阅 OSTBC 编码算法。
