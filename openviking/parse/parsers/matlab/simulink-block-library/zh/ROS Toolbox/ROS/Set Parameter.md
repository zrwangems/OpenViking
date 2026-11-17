---
type: simulink-block
title: 'Set Parameter'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'setparameter'
documentation_source_path: 'ref/setparameter.html'
language: zh-CN
chinese_source: worker-translation
---

# Set Parameter

## 端口
```yaml
ports:
- name: Value
  summary: 参数值 标量 | 逻辑值 | uint8 数组
  direction: input
- name: Length
  summary: 字符串参数的长度 整数
  direction: input
```

### 输入

### **Value** — 参数值 标量 | 逻辑值 | uint8 数组

来自 ROS 网络的参数值。该值取决于 **Data type** 参数。

### **Length** — 字符串参数的长度 整数

字符串参数的长度，指定为整数。该长度是 `uint8` 数组的元素个数，或者是转换为 `uint8` 的字符串中的字符个数。

**注意**

当将字符串参数转换为 `uint8` 时，ASCII 值 0–31（控制字符）会因其不兼容的字符类型而返回错误。

#### 依赖关系

要启用此端口，请将 **Data type** 设置为 `uint8[] (string)`。
## 参数
```yaml
parameters:
- name: Source
  summary: 用于指定参数名的来源 Select from ROS network | Specify your own
  group: ''
- name: Name
  summary: 参数名 字符串
  group: ''
- name: Data type
  summary: 参数的数据类型 double | int32 | boolean | uint8[] (string)
  group: ''
```

### **Source** — 用于指定参数名的来源 `Select from ROS network` | `Specify your own`

用于指定参数名的来源，为以下之一：

- `Select from ROS network`
  — 使用 **Select** 选择参数名。**Data type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own`
  — 在 **Name** 中输入参数名，并在 **Data type** 中指定其数据类型。参数名必须完全匹配。

### **Name** — 参数名 字符串

要从 ROS 网络获取的参数名，指定为字符串。当 **Source** 设置为 `Select from ROS network` 时，使用 **Select** 选择现有参数。您必须连接到 ROS 网络才能获取参数列表。否则，请指定参数和数据类型。

参数名字符串必须遵循 ROS 图名称的规则。有效名称具有以下特征：

- 第一个字符是字母字符（[a-z|A-Z]）、波浪号（~）或正斜杠（/）。
- 后续字符是字母数字（[0-9|a-z|A-Z]）、下划线（\_）或正斜杠（/）。

### **Data type** — 参数的数据类型 double | int32 | boolean | uint8[] (string)

参数的数据类型，指定为字符串。

**注意**

`uint8[] (string)` 数据类型是与字符串中字符对应的 ASCII 值数组。在获取字符串参数时，您可以创建一个 MATLAB Function (Simulink) 模块，将字符串与所需的参数值进行比较。有关详细信息，请参阅 Simulink 中的 ROS 参数。

**数据类型：** `double` | `int32` | `Boolean` | `uint8`
## 所属库

ROS Toolbox / ROS

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

在 ROS 参数服务器上设置值

Set Parameter 模块将 **Value** 输入设置为 ROS 参数服务器上指定的名称。该模块使用 Simulink® 模型的 ROS 节点连接到 ROS 网络。该节点在您运行模型时创建，并在模型终止时删除。如果模型没有节点，该模块会创建一个。
