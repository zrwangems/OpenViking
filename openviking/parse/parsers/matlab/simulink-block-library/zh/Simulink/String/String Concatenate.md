---
type: simulink-block
title: 'String Concatenate'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringconcatenate'
documentation_source_path: 'slref/stringconcatenate.html'
language: zh-CN
chinese_source: worker-translation
---

# String Concatenate

## 端口
```yaml
ports:
- name: Port_1
  summary: 第一个输入字符串标量
  direction: input
  data_types: string
- name: Port_2
  summary: 第二个输入字符串标量
  direction: input
  data_types: string
- name: Port_1
  summary: 拼接后的字符串标量
  direction: output
  data_types: string
```

### 输入

### **Port\_1** — 第一个输入字符串标量

第一个输入字符串，指定为标量。

**数据类型：** `string`

### **Port\_2** — 第二个输入字符串标量

第二个输入字符串，指定为标量。

**数据类型：** `string`
### 输出

### **Port\_1** — 拼接后的字符串标量

拼接后的字符串，指定为标量。

**数据类型：** `string`
## 参数
```yaml
parameters:
- name: Number of Inputs
  summary: 输入字符串的数量 标量
  group: ''
  block_parameter: Inputs
  type: 字符向量
  values: 从 2 到 512 的标量
  default: '''2'''
- name: Output data type
  summary: 输出数据类型 string（默认） | <data type expression> | 标量
  group: ''
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''string'' | *<data type expression>*'
  default: '''string'''
- name: Mode
  summary: 数据类别 stringtype(128)（默认） | scalar
  group: ''
```

### **Number of Inputs** — 输入字符串的数量 标量

要拼接的输入字符串的数量，指定为标量。您可以指定 2 到 512 个输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Inputs` |
| **类型：** 字符向量 |
| **值：** 从 `2` 到 `512` 的标量 |
| **默认值：** `'2'` |

### **Output data type** — 输出数据类型 `string`（默认） | `<data type expression>` | 标量

输出数据类型，使用 string 数据类型指定，以表示没有最大长度的字符串。

要指定具有最大长度的字符串数据类型，请指定
`stringtype(N)`。例如，`stringtype(128)` 创建一个最大长度为 128 个字符的字符串数据类型。

点击 **Show data type assistant** 按钮
以显示 **Data Type
Assistant**，它可以帮助您设置数据类型属性。有关更多信息，请参阅
使用数据类型助手指定数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'string'` | *`<data type expression>`* |
| **默认值：** `'string'` |

### **Mode** — 数据类别 `stringtype(128)`（默认） | `scalar`

使用 `stringtype` 函数，例如，
`stringtype(128)`。

#### 依赖关系

点击 **Show data type assistant** 按钮
会启用此参数。
## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

将输入字符串拼接成一个输出字符串

String Concatenate 模块按照输入顺序拼接多个输入字符串，形成一个输出字符串。如果您想将多个字符串合并为一个字符串，请使用此模块。
