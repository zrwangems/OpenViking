---
type: simulink-block
title: 'Complex to Magnitude-Angle'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'complextomagnitudeangle'
documentation_source_path: 'slref/complextomagnitudeangle.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex to Magnitude-Angle

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Port_1
  summary: 幅值 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_2
  summary: 弧度相位角 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

模块计算并输出其幅值和/或相位角的复数输入信号。

#### 限制

仅当将**近似方法**设置为 `CORDIC` 时，才支持定点数据类型。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 幅值 标量 | 向量 | 矩阵

输出信号，为输入信号的幅值和/或相位角。要选择输出，请设置**输出**参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — 弧度相位角 标量 | 向量 | 矩阵

弧度相位角，以实值标量、向量或矩阵形式返回。

#### 依赖关系

- 要启用此端口，请将**输出**设置为 `Magnitude and angle` 或 `Angle`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Output
  summary: 幅值和/或相位角输出设定 Magnitude and angle（默认）| Magnitude | Angle
  group: ''
  block_parameter: Output
  type: 字符向量
  values: '''Magnitude and angle'' | ''Magnitude'' | ''Angle'''
  default: '''Magnitude and angle'''
- name: Approximation method
  summary: 近似方法 None（默认）| CORDIC
  group: ''
  block_parameter: ApproximationMethod
  type: 字符向量
  values: '''None'' | ''CORDIC'''
  default: '''None'''
- name: Number of iterations
  summary: CORDIC 算法的迭代次数 11（默认）| 小于或等于定点输入字长的正整数
  group: ''
  block_parameter: NumberOfIterations
  type: 字符向量
  values: 小于或等于定点输入字长的正整数
  default: '''11'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
```

### **Output** — 幅值和/或相位角输出设定 `Magnitude and angle`（默认）| `Magnitude` | `Angle`

指定输出是输入信号的幅值和/或弧度相位角。

#### 编程用法

|  |
| --- |
| **参数：** `Output` |
| **类型：** 字符向量 |
| **值：** `'Magnitude and angle'` | `'Magnitude'` | `'Angle'` |
| **默认值：** `'Magnitude and angle'` |

### **Approximation method** — 近似方法 `None`（默认）| `CORDIC`

指定用于计算输出的近似类型。

| 近似方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `None`（默认） | 浮点 | 您希望使用默认的泰勒级数算法。 |
| `CORDIC` | 浮点和定点 | 您希望进行快速、近似的计算。 |

模块使用以下数据类型传播规则。

| 复数输入的数据类型 | 近似方法 | 幅值输出的数据类型 | 角度输出的数据类型 |
| --- | --- | --- | --- |
| 浮点 | `None` 或 `CORDIC` | 与输入相同 | 与输入相同 |
| 有符号定点 | `CORDIC` | `fixdt`(1, *`WL`* + 2, *`FL`*)  其中：  - *`WL`* = 幅值的输入字长 + 2 + 1 - *`FL`* = 幅值的输入小数长度 | `fixdt`(1, *`WL`* + 2, *`FL`*)  其中：  - *`WL`* = 幅值的输入字长 -3，以获得 [`-pi, pi`) 的最佳精度 - *`FL`* = 角度的输入小数长度 |
| 无符号定点 | `CORDIC` | `fixdt`(1, *`WL`* + 3, *`FL`*)  其中：  - *`WL`* = 幅值的输入字长 + 2 - *`FL`* = 幅值的输入小数长度 | `fixdt`(1, *`WL`* + 3, *`FL`*)  其中：  - *`WL`* = 角度的输入字长 - 2，以获得范围 [0, pi/2] 的最佳精度小数长度 - *`FL`* = 角度的小数长度 |

#### 编程用法

|  |
| --- |
| **模块参数：** `ApproximationMethod` |
| **类型：** 字符向量 |
| **值：** `'None' | 'CORDIC'` |
| **默认值：** `'None'` |

### **Number of iterations** — CORDIC 算法的迭代次数 `11`（默认）| 小于或等于定点输入字长的正整数

CORDIC 算法执行的迭代次数，指定为正整数值标量。增加迭代次数可以产生更精确的结果，但也会增加计算开销并增加延迟。

| 模块输入的数据类型 | 可以指定的值 |
| --- | --- |
| 浮点 | 正整数。最大值为 double 类型 52 或 single 类型 23。 |
| 定点 | 不超过幅值输入字长或相位角输入字长的正整数，取两者中较小的值。 |

#### 依赖关系

要启用此参数，请将**近似方法**设置为 `CORDIC`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumberOfIterations` |
| **类型：** 字符向量 |
| **值：** 小于或等于定点输入字长的正整数 |
| **默认值：** `'11'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |
## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

### R2024b: Complex to Magnitude-Angle 模块支持定点输入

Complex to Magnitude-Angle 模块现在支持 CORDIC 近似方法。此方法允许在输入 **Port\_1** 处使用定点输入。要选择 CORDIC 方法，请将新增的**近似方法**参数设置为 `CORDIC`。

当您选择 CORDIC 方法时，模块图标会更新。新增的参数 Number of iterations 允许您定义 CORDIC 算法的迭代次数。

使用 CORDIC 近似方法输入的 Complex to Magnitude-Angle 模块图标

## 描述

计算复数信号的幅值和/或相位角

Complex to Magnitude-Angle 模块根据**输出**参数的设置，输出输入信号的幅值和/或相位角。输出为与模块输入具有相同数据类型的实值。输入可以是复数信号数组，在这种情况下，输出信号也是数组。幅值信号数组包含对应复数输入元素的幅值。角度输出同样包含输入元素的角度。
