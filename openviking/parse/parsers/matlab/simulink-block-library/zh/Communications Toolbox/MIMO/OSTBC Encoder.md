---
type: simulink-block
title: 'OSTBC Encoder'
family: 'mimo'
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

### 输入

### **In** — 输入数据列向量 | 矩阵

输入数据，指定为斜率是 2 的幂且偏置为零的列向量或矩阵。有关详细信息，请参阅输入到输出维度。

此端口在模块图标上未命名。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes
### 输出

### **Out** — 输出数据矩阵 | 三维数组

输出数据，以矩阵或三维数组形式返回。有关详细信息，请参阅输入到输出维度。

输出信号继承输入信号的数据类型。对于定点信号，**整数溢出时饱和**参数指定模块如何处理因复共轭导致的整数溢出。

此端口在模块图标上未命名。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

#### 主要

### **发射天线数量** — 发射天线数量 `2`（默认）| `3` | `4`

发射天线数量，指定为 `2`、`3` 或 `4`。

### **速率** — 符号速率 `3/4`（默认）| `1/2`

码的符号速率，指定为 `3/4` 或 `1/2`。当将 **发射天线数量** 设置为 `2` 时，符号速率为 `1`。

#### 依赖项

要启用此参数，请将 **发射天线数量** 设置为 `3` 或 `4`。

#### 数据类型

### **整数溢出时饱和** — 在整数溢出时饱和的选项 off（默认）| on

对于定点计算，如果定点计算结果的幅值超出存储结果的数据类型和定标的范围，请使用此参数指定要使用的方法。

- 要在整数溢出时饱和，请选择此参数。
- 要在整数溢出时环绕，请勿选择此参数。

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

OSTBC Encoder 模块使用正交空时分组码 (OSTBC) 对输入符号序列进行编码。该模块以块方式映射输入符号，并在时域中串联输出码字矩阵。有关详细信息，请参阅 OSTBC 编码算法。
