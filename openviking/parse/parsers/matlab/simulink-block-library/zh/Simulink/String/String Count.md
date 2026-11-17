---
type: simulink-block
title: 'String Count'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringcount'
documentation_source_path: 'slref/stringcount.html'
language: zh-CN
chinese_source: worker-translation
---

# String Count

## 端口
```yaml
ports:
- name: str
  summary: 要搜索的字符串 标量
  direction: input
  data_types: string
- name: sub
  summary: 要搜索的字符串模式 标量
  direction: input
  data_types: string
- name: n
  summary: 在字符串中找到模式的次数 标量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32
```

### 输入

### **str** — 要搜索的字符串 标量

要在其中搜索模式的字符串，指定为标量。

**数据类型：** `string`

### **sub** — 要搜索的字符串模式 标量

要在字符串中搜索的字符串模式，指定为标量。

**数据类型：** `string`
### 输出

### **n** — 在字符串中找到模式的次数 标量

在字符串 `str` 中找到字符串模式的次数，以标量形式返回。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
## 参数
```yaml
parameters:
- name: Case sensitive
  summary: 区分大小写 开启（默认） | 关闭
  group: ''
  block_parameter: CaseSensitive
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Output data type
  summary: '输出数据类型 Inherit: Inherit via internal rule（默认） | Inherit: Inherit via back propagation | int8 | uint8 | int16 |
    uint16 | int32 | uint32 | <data type expression>'
  group: ''
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Inherit via back propagation'' | ''int8'' | ''uint8'' | ''int16''
    | ''uint16'' | ''int32'' | ''uint32'' | *<data type expression>*'
  default: '''Inherit: Inherit via internal rule'''
- name: Mode
  summary: 数据类型类别 Inherit（默认） | Built in | Expression
  group: ''
```

### **Case sensitive** — 区分大小写 开启（默认） | 关闭

字符串计数的区分大小写：

开启
:   在计数找到的字符串时考虑字符串大小写。

关闭
:   在计数找到的字符串时不考虑字符串大小写。

#### 编程使用

|  |
| --- |
| **模块参数**：`CaseSensitive` |
| **类型**：字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **Output data type** — 输出数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Inherit via back propagation` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `<data type expression>`

输出数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择继承选项时，模块表现出以下行为：

- `Inherit: Inherit via internal rule` — Simulink® 选择一种数据类型以平衡数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。

单击“显示数据类型助手”按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | *`<data type expression>`* |
| **默认值：** `'Inherit: Inherit via internal rule'` |

### **Mode** — 数据类型类别 `Inherit`（默认） | `Built in` | `Expression`

数据类型类别，指定为 `Inherit`、`Built in` 或 `Expression`。有关使用此参数的更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

单击 **Show data type assistant** 按钮可启用此参数。
## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

统计字符串中模式的出现次数

String Count 模块统计字符串（**str**）中模式（**sub**）的出现次数。如果 **sub** 处的输入匹配 **str** 处的输入的部分或全部，则该模块将该次出现计为 1。
