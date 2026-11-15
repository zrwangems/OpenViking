---
type: simulink-block
title: 'Set Parameter'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS Network Access / ROS Network Connection and Exploration'
documentation_page: 'setparameter'
documentation_source_path: 'ref/setparameter.html'
language: zh-CN
chinese_source: worker-translation
---

# Set Parameter

## 端口

### 输入

### **Value** — 参数值 scalar | logical | uint8 array

来自 ROS 网络的参数值。该值取决于 **Data type** 参数。

### **Length** — 字符串参数长度 integer

字符串参数的长度，指定为 integer。此长度是 `uint8` 数组的元素数量，或者转换为 `uint8` 的字符串中的字符数。

**注意**

当将字符串参数转换为 `uint8` 时，ASCII 值 0–31（控制字符）会因其字符类型不兼容而返回错误。

#### 依赖关系

要启用此端口，请将 **Data type** 设置为 `uint8[] (string)`。

## 参数

### **Source** — 用于指定参数名的来源 `Select from ROS network` | `Specify your own`

用于指定参数名的来源，为以下之一：

- `Select from ROS network`
  — 使用 **Select** 选择参数名。**Data type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own`
  — 在 **Name** 中输入参数名，并在 **Data type** 中指定其数据类型。您必须完全匹配参数名。

### **Name** — 参数名 string

要从 ROS 网络获取的参数名，指定为 string。当 **Source** 设置为 `Select from ROS network` 时，使用 **Select** 选择现有参数。您必须连接到 ROS 网络才能获取参数列表。否则，请指定参数和数据类型。

参数字符串必须遵循 ROS 图名称的规则。有效名称具有以下特征：

- 第一个字符是字母字符 ([a-z|A-Z])、波浪号 (~) 或正斜杠 (/)。
- 后续字符是字母数字 ([0-9|a-z|A-Z])、下划线(\_) 或正斜杠 (/)。

### **Data type** — 您的参数的数据类型 double | int32 | boolean | uint8[] (string)

您的参数的数据类型，指定为 string。

**注意**

`uint8[] (string)` 数据类型是 ASCII 值的数组，对应于字符串中的字符。获取字符串参数时，您可以创建一个 MATLAB Function (Simulink) 模块，将字符串与所需的参数值进行比较。有关详细信息，请参阅 ROS Parameters in Simulink。

**数据类型：** `double` | `int32` | `Boolean` | `uint8`

## 所属库

ROS Toolbox / ROS

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

在 ROS 参数服务器上设置值

Set Parameter 模块将 **Value** 输入设置到 ROS 参数服务器上的指定名称。该模块使用 Simulink® 模型的 ROS 节点连接到 ROS 网络。此节点在运行模型时创建，并在模型终止时删除。如果模型没有节点，则该模块会创建一个节点。
