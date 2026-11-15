---
type: simulink-block
title: 'Argument Inport'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Simulink Functions'
documentation_page: 'argumentinport'
documentation_source_path: 'slref/argumentinport.html'
language: zh-CN
chinese_source: official
---

# Argument Inport

## 端口

### 输入

### **u** — 参量输入 标量 | 向量 | 矩阵

Argument Inport 模块接受 Simulink® 支持的任何数据类型的复信号或实信号，包括定点和枚举数据类型。Argument Inport 模块还接受将总线对象作为数据类型。

模块输出的复/实性和数据类型与参量输入相同。您可以使用**信号类型**和**数据类型**参数为 Argument Inport 模块指定输入参量的信号类型和数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **out** — 模块输出 标量 | 向量 | 矩阵

来自该模块的模块输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **端口号** — 指定模块的端口号 `1` (默认) | 整数

指定与模块对应的端口在父级子系统或 Model 模块中的显示顺序。

`1`
:   指定此模块的第一个端口位置。

整数
:   指定端口的位置。

#### 编程用法

|  |
| --- |
| **模块参数：**`Port` |
| **类型：**字符向量 |
| **值：**`'1'` | `'<integer>'` |
| **默认值：**`'1'` |

### **参量名称** — 指定输入参量名称 `u` (默认) | 字符向量

为 Simulink Function 模块表面显示的函数原型指定输入参量名称。

`u`
:   输入参量的默认名称。

字符向量
:   输入参量的名称。

#### 编程用法

|  |
| --- |
| **模块参数：**`ArgumentName` |
| **类型：**字符向量 |
| **值：**`'u'` | `'<character vector>'` |
| **默认值：**`'u'` |

### **最小** — 指定模块输出的最小值 `[]` (默认) | 数字

指定模块输出信号的最小值。

**注意**

如果您指定总线对象作为此模块的数据类型，请不要为模块上的总线数据设置最小值。因为 Simulink 会忽略此设置。但请为指定作为数据类型的总线对象的总线元素设置最小值。有关总线元素的“最小值”属性的信息，请参阅 `Simulink.BusElement`。

Simulink 使用此值执行仿真范围检查和定点数据类型的自动定标。

`[]`
:   未指定最小值。

数字
:   有限双精度实数标量值。

#### 编程用法

|  |
| --- |
| **模块参数：**`OutMin` |
| **类型：**字符向量 |
| **值：**`'[]'` | `'<number>'` |
| **默认值：**`'[]'` |

### **最大** — 指定模块输出的最大值 `[]` (默认) | 数字

指定模块输出信号的最大值。

**注意**

如果您指定总线对象作为此模块的数据类型，请不要为模块的总线数据设置最大值。因为 Simulink 会忽略此设置。但请为指定作为数据类型的总线对象的总线元素设置最大值。有关总线元素的“最大值”属性的信息，请参阅 `Simulink.BusElement`。

Simulink 使用此值执行仿真范围检查和定点数据类型的自动定标。

`[]`
:   未指定最大值。

数字
:   有限双精度实数标量值。

#### 编程用法

|  |
| --- |
| **模块参数：**`OutMax` |
| **类型：**字符向量 |
| **值：**`'[]'` | `'<number>'` |
| **默认值：**`'[]'` |

### **数据类型** — 指定模块输出数据类型 **double** (默认) | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **boolean** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^,0)** | **Enum: <class name>** | **Bus: <object name>** | **<数据类型表达式>**

指定模块输出数据类型。

**double**
:   数据类型为 `double`。

**single**
:   数据类型为 `single`。

**int8**
:   数据类型为 `int8`。

**uint8**
:   数据类型为 `uint8`。

**int16**
:   数据类型为 `int16`。

**uint16**
:   数据类型为 `uint16`。

**int32**
:   数据类型为 `int32`。

**uint32**
:   数据类型为 `uint32`。

**int64**
:   数据类型为 `int64`。

**uint64**
:   数据类型为 `uint64`。

**boolean**
:   数据类型为 `boolean`。

**fixdt(1,16,0)**
:   数据类型为定点 `fixdt(1,16,0)`。

**fixdt(1,16,2^0,0)**
:   数据类型为定点 `fixdt(1,16,2^0,0)`。

**Enum: <class name>**
:   数据类型为枚举，例如 `Enum: Basic Colors`。

**Bus: <object name>**
:   数据类型是 `Simulink.Bus` 对象。

**<数据类型表达式>**
:   数据类型对象的名称，例如 **Simulink.NumericType**

#### 提示

您不能以数据类型表达式的形式输入 `Simulink.Bus` 对象的名称。要使用 `Bus` 对象为模块指定**数据类型**，请选择 **Bus: <object name>** 选项，并用 `Bus` 对象的名称替换 `<object name>`。

#### 编程用法

|  |
| --- |
| **模块参数：**`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值：**`'double'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 off (默认) | on

控制定点工具和定点顾问对数据类型设置的更改。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

On
:   锁定此模块的所有数据类型设置。

Off
:   允许定点工具和定点顾问更改此模块的数据类型设置。

#### 编程用法

|  |
| --- |
| **模块参数：**`LockScale` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

### **端口维度** — 指定端口维度 `1` (默认) | `n` | `[m n]`

指定模块的参量输入信号的维度。有关详细信息，请参阅 Outport。

`1`
:   继承端口维度。

`n`
:   宽度为 `n` 的向量信号。

`[m n]`
:   具有 `m` 行和 `n` 列的矩阵信号。

#### 编程用法

|  |
| --- |
| **模块参数：**`PortDimensions` |
| **类型：**字符向量 |
| **值**：`'1'` | `'n'` | `'[m n]'` |
| **默认值：**`'1'` |

### **信号类型** — 选择实信号或复信号 **实部** (默认) | **复**

选择实信号或复信号。

**实部**
:   将信号类型指定为实数。

**复**
:   将信号类型指定为复数。

#### 编程用法

|  |
| --- |
| **模块参数：**`SignalType` |
| **类型：**字符向量 |
| **值：**`'real'` | `'complex'` |
| **默认值：**`'real'` |

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2014b 中推出**

## 描述

Simulink Function 模块的参量输入端口

该模块是您在 Simulink Function 模块中定义的函数的参量输入端口。
