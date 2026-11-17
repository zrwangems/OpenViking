---
type: simulink-block
title: 'Get Parameter'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'getparameter'
documentation_source_path: 'ref/getparameter.html'
language: zh-CN
chinese_source: worker-translation
---

# Get Parameter

## 端口
```yaml
ports:
- name: Value
  summary: 参数值 标量 | 逻辑值 | uint8 数组
  direction: output
- name: ErrorCode
  summary: ROS 参数的状态 0 | 1 | 2 | 3
  direction: output
- name: Length
  summary: 字符串参数的长度 整数
  direction: output
```

### 输出

### **Value** — 参数值 标量 | 逻辑值 | uint8 数组

来自 ROS 网络的参数值。该值取决于 **Data type** 参数。

### **ErrorCode** — ROS 参数的状态 0 | 1 | 2 | 3

ROS 参数的状态，指定为以下之一：

- **0 —** ROS 参数成功获取。获取的值在 **Value** 端口输出。
- **1 —** 未找到具有指定名称的 ROS 参数。如果没有已知值，**Value** 设置为最后接收的值或 **Initial value**。
- **2 —** ROS 参数已获取，但其类型与指定的 **Data type** 不同。如果没有已知值，Value 设置为最后接收的值或 **Initial value**。
- **3 —** 对于字符串参数，传入的字符串已根据指定的长度被截断。

### **Length** — 字符串参数的长度 整数

字符串参数的长度，以整数形式返回。该长度是 `uint8` 数组的元素个数或转换为 `uint8` 的字符串中的字符数。

**注意**

从 ROS 网络获取字符串参数时，ASCII 值 13 会因其不兼容的字符类型而返回错误。

#### 依赖关系

要启用此端口，请将 **Data type** 设置为 `uint8[] (string)`。
## 参数
```yaml
parameters:
- name: Source
  summary: 用于指定参数名称的来源 Select from ROS network | Specify your own
  group: ''
- name: Name
  summary: 参数名称 字符串
  group: ''
- name: Data type
  summary: 参数的数据类型 double | int32 | boolean | uint8[] (string)
  group: ''
- name: Maximum length
  summary: uint8 数组的最大长度 标量
  group: ''
- name: Initial value
  summary: 默认参数值输出 double | int32 | boolean | uint8
  group: ''
- name: Sample time
  summary: 输出之间的间隔 inf（默认）| 标量
  group: ''
- name: Show ErrorCode output port
  summary: 显示错误代码输出 on | off
  group: ''
```

### **Source** — 用于指定参数名称的来源 `Select from ROS network` | `Specify your own`

用于指定参数名称的来源，为以下之一：

- `Select from ROS network`
  — 使用 **Select** 选择参数名称。**Data type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own`
  — 在 **Name** 中输入参数名称，并在 **Data type** 中指定其数据类型。您必须精确匹配参数名称。

### **Name** — 参数名称 字符串

要从 ROS 网络获取的参数名称，指定为字符串。当 **Source** 设置为 `Select from ROS network` 时，使用 **Select** 选择现有参数。您必须连接到 ROS 网络才能获取参数列表。否则，请指定参数和数据类型。

参数名称字符串必须遵循 ROS 图名称的规则。有效名称具有以下特征：

- 第一个字符是字母字符（[a-z|A-Z]）、波浪号（~）或正斜杠（/）。
- 后续字符是字母数字（[0-9|a-z|A-Z]）、下划线（\_）或正斜杠（/）。

### **Data type** — 参数的数据类型 double | int32 | boolean | uint8[] (string)

参数的数据类型，指定为字符串。`uint8[] (string)` 会启用 **Maximum length** 参数。

**注意**

`uint8[] (string)` 数据类型是与字符串中字符对应的 ASCII 值数组。获取字符串参数时，您可以创建一个 MATLAB Function (Simulink) 模块来将字符串与所需的参数值进行比较。有关详细信息，请参阅 Simulink 中的 ROS 参数。

**数据类型：** `double` | `int32` | `Boolean` | `uint8`

### **Maximum length** — `uint8` 数组的最大长度 标量

`uint8` 数组的最大长度，指定为标量。如果参数字符串的长度大于 **Maximum length**，则 **ErrorCode** 输出设置为 3。

#### 依赖关系

要启用此端口，请将 **Data type** 设置为 `uint8[] (string)`。

### **Initial value** — 默认参数值输出 double | int32 | boolean | uint8

当发生错误且未从参数服务器接收到有效值时输出的默认参数值。数据类型必须与指定的 **Data type** 匹配。

### **Sample time** — 输出之间的间隔 `inf`（默认）| 标量

输出之间的间隔，指定为标量。此默认值表示模块输出永不改变。使用此值可消除重新计算模块输出的需要，从而加速仿真和代码生成。否则，模块在每个 `Sample time` 间隔输出一条新的空白消息。

有关详细信息，请参阅 Specify Sample Time (Simulink)。

### **Show ErrorCode output port** — 显示错误代码输出 on | off

要启用错误代码输出，请选择此参数。清除此参数后，**ErrorCode** 输出端口将从模块中移除。状态选项包括：

- **0 —** ROS 参数检索成功。检索到的值在 **Value** 端口输出。
- **1 —** 未找到具有指定名称的 ROS 参数。如果没有已知值，**Value** 将设置为最后接收的值或 **Initial value**。
- **2 —** ROS 参数已检索，但其类型与指定的 **Data type** 不同。如果没有已知值，Value 将设置为最后接收的值或 **Initial value**。
- **3 —** 对于字符串参数，传入字符串已根据指定长度被截断。
## 所属库

ROS Toolbox / ROS

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

从 ROS 参数服务器获取值

Get Parameter 模块输出指定 ROS 参数的值。该模块使用 Simulink® 模型的 ROS 节点连接到 ROS 网络。此节点在运行模型时创建，并在模型终止时删除。如果模型没有节点，该模块将创建一个。

在每个采样命中时，该模块检查 ROS 参数服务器以获取指定的 ROS 参数并输出其值。
