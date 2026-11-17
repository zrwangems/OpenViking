---
type: simulink-block
title: 'Get Parameter'
family: 'ros-2'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'getparameterros2'
documentation_source_path: 'ref/getparameterros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Get Parameter

## 端口

### 输出

### **Value** — 参数值 标量 | 数组

来自 ROS 2 网络的参数值，以标量或数组形式返回。此输出的类型和大小取决于 **Data type** 参数。

**数据类型：** `double` | `int64` | `Boolean` | `uint8[]`

### **Length** — 数组参数的长度 标量

数组参数的长度，以整数标量形式返回。此长度是数组的元素数，或者强制转换为 `uint8` 的字符串中的字符数。

**注意**

从 ROS 2 网络获取字符串参数时，ASCII 值 13 会因其字符类型不兼容而返回错误。

#### 依赖项

要启用此端口，请将 **Data type** 参数设置为 `uint8[]`、`double[]`、`int64[]` 或 `boolean[]`。

## 参数

### **Name** — 参数名称 `mynamespace.param`（默认）| 字符串

要从 ROS 2 网络获取的参数名称，指定为字符串。有效的参数名称具有以下特征：

- 第一个字符是字母字符（[a-z|A-Z]）、波浪号（~）或正斜杠（/）。
- 后续字符是字母数字（[0-9|a-z|A-Z]）、下划线（\_）或正斜杠（/）。

### **Data type** — 参数的数据类型 `double`（默认）| `int64` | `boolean` | `uint8[]` | `double[]` | `int64[]` | `boolean[]`

参数的数据类型，指定为字符串。诸如 `uint8[]`、`double[]`、`int64[]` 和 `boolean[]` 等数组数据类型会启用 **Maximum length** 参数。如果数据类型在运行时发生更改，该模块会发出警告。

**注意**

`uint8[]` 数据类型是一个 ASCII 值数组，对应于字符串中的字符。获取字符串参数时，可以创建一个 MATLAB Function (Simulink) 模块来将该字符串与所需的参数值进行比较。

### **Maximum length** — 数组的最大长度 16（默认）| 数值标量

数组的最大长度，指定为标量。如果数组的长度大于 **Maximum length**，该模块会返回警告。

#### 依赖项

要启用此参数，请将 **Data type** 参数设置为 `uint8[]`、`double[]`、`int64[]` 或 `boolean[]`。

### **Initial value** — 默认参数值输出 `0.0`（默认）| 数值标量 | 向量

当发生错误且未从参数接收到有效值时，输出的默认参数值。指定的值必须是指定 **Data type** 的有效值。

### **Sample time** — 输出之间的间隔 `-1`（默认）| 数值标量

输出之间的间隔，指定为数值标量。默认值 `-1` 表示该模块从模型继承输出采样时间。否则，该模块在 `Sample time` 的每个间隔输出一条新的空白消息。

有关详细信息，请参阅 Specify Sample Time (Simulink)。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

获取 ROS 2 参数值

Get Parameter 模块输出与 Simulink® 模型的节点关联的指定 ROS 2 参数的值。Simulink 在运行模型时创建此节点，并在模型终止时删除它。如果模型没有参数，则该模块会创建一个参数。

在仿真开始时，该模块使用指定的初始值初始化 ROS 2 参数。在每个采样命中时，该模块检查 ROS 2 参数并输出其值。
