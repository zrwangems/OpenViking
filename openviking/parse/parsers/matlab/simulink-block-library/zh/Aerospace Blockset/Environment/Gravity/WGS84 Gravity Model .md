---
type: simulink-block
title: 'WGS84 Gravity Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'wgs84gravitymodel'
documentation_source_path: 'wgs84gravitymodel.html'
language: zh-CN
chinese_source: worker-translation
---

# WGS84 Gravity Model

## 端口
```yaml
ports:
- name: μ l h
  summary: 大地纬度、经度和高度位置 三元素向量 | *M*×3 数组
  direction: input
  data_types: double
- name: JD
  summary: 儒略日 标量 | 大于 2451545 的值
  direction: input
  data_types: double
- name: Output 1
  summary: 重力 三元素向量 | *M*×3 数组
  direction: output
  data_types: double
```

### 输入

### **μ l h** — 大地纬度、经度和高度位置 三元素向量 | *M*×3 数组

以选定单位指定的大地纬度、经度和高度位置，指定为三元素向量或 *M*×3 数组。高度必须小于 20,000 m（约 65,620 英尺）。

对于超出限制（0 到 20000 m）的输入，如果动作输入指定为 'None' 或 'warning'，则实现会被扩展。但是，不建议对这些限制之外的输入使用该模块。

**数据类型：** `double`

### **JD** — 儒略日 标量 | 大于 2451545 的值

儒略日，指定为标量。年份必须晚于 2000 年 1 月 1 日（2451545）。

#### 依赖关系

要启用此端口，请选择 **Input Julian date**。

**数据类型：** `double`
### 输出

### **Output 1** — 重力 三元素向量 | *M*×3 数组

北-东-地（NED）坐标系中的重力。

| 重力模型方法 | 输出 |
| --- | --- |
| Taylor Series 和 Close Approximation | 仅输出正常重力（NED 坐标系中向下）。 |
| Exact | 同时输出正常重力和切向重力（NED 坐标系中向下和向北）。 |

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Type of gravity model
  summary: 重力模型方法 WGS84 Taylor Series（默认）| WGS84 Close Approximation | WGS84 Exact
  group: ''
  block_parameter: model
  type: 字符向量
  values: '''WGS84 Taylor Series'' | ''WGS84 Close Approximation'' | ''WGS84 Exact'''
  default: '''WGS84 Taylor Series'''
- name: Units
  summary: 单位 Metric (MKS)（默认）| English
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Exclude Earth's atmosphere
  summary: 地球大气 on（默认）| off
  group: ''
  block_parameter: no_atmos
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Precessing reference frame
  summary: 进动参考系 on（默认）| off
  group: ''
  block_parameter: precessing
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Input Julian date
  summary: 儒略日 off（默认）| on
  group: ''
  block_parameter: jd_loc
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Month
  summary: 月 January（默认）| February | March | April | May | June | July | August | September | October | November | December
  group: ''
  block_parameter: month
  type: 字符向量
  values: '''January'' | ''February'' | ''March'' | ''April'' | ''May'' | ''June'' | ''July'' | ''August'' | ''September''
    | ''October'' | ''November'' | ''December'''
  default: '''January'''
- name: Day
  summary: 日 10（默认）| 1 到 31
  group: ''
  block_parameter: day
  type: 字符向量
  values: '''1'' 到 ''31'''
  default: '''10'''
- name: Year
  summary: 年 2004（默认）| 任意年份
  group: ''
  block_parameter: year
  type: 字符向量
  values: 任意年份
  default: '''2004'''
- name: No centrifugal effects
  summary: 离心效应 on（默认）| off
  group: ''
  block_parameter: no_centrifugal
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Action for out-of-range input
  summary: 超出范围时的模块行为 Warning（默认）| Error | None
  group: ''
  block_parameter: action
  type: 字符向量
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
```

### **Type of gravity model** — 重力模型方法 `WGS84 Taylor Series`（默认）| `WGS84 Close Approximation` | `WGS84 Exact`

用于计算重力的方法，指定为：

| 重力模型方法 | 输出 |
| --- | --- |
| `WGS84 Taylor Series` 和 `WGS84 Close Approximation` | 仅输出正常重力（NED 坐标系中向下）。 |
| `WGS84 Exact` | 同时输出正常重力和切向重力（NED 坐标系中向下和向北）。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`model` |
| **类型**：字符向量 |
| **值**：`'WGS84 Taylor Series'` | `'WGS84 Close Approximation'` | `'WGS84 Exact'` |
| **默认值**：`'WGS84 Taylor Series'` |

### **Units** — 单位 `Metric (MKS)`（默认）| `English`

输入和输出单位，指定为：

| 单位 | 高度 | 重力 |
| --- | --- | --- |
| `Metric (MKS)` | 米 | 米每二次方秒 |
| `English` | 英尺 | 英尺每二次方秒 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **Exclude Earth's atmosphere** — 地球大气 `on`（默认）| `off`

- 要排除地球引力场中的大气质量，请选中此复选框。
- 要包含地球引力场中的大气质量，请清除此复选框。

#### 依赖关系

要启用此复选框，请将 **Type of gravity model** 设置为 `Type of gravity model WGS84 Close Approximation` 或 `WGS84 Exact`。

#### 编程使用

|  |
| --- |
| **模块参数**：`no_atmos` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Precessing reference frame** — 进动参考系 `on`（默认）| `off`

- 要使用国际天文学联合会（IAU）地球角速度值和赤经进动率计算地球速度，请选中此复选框。
- 要使用以恒定角速度旋转的标准地球的角速度计算地球速度，请清除此复选框。

为获得赤经进动率，该模块使用 **Month**、**Day** 和 **Year** 从 J2000.0 历元计算儒略世纪。

#### 依赖关系

- 要启用此复选框，请将 **Type of gravity model** 设置为 `Type of gravity model WGS84 Close Approximation` 或 `WGS84 Exact`。
- 清除此复选框会禁用 **Input Julian date** 参数和 **JD** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`precessing` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Input Julian date** — 儒略日 `off`（默认）| `on`

- 要通过输入端口为该模块指定儒略日，请选中此复选框。
- 要使用 **Month**、**Day** 和 **Year** 的值计算儒略日，请清除此复选框。年份必须晚于 2000 年 1 月 1 日（2451545）。

#### 依赖关系

- 要启用 **JD** 端口，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`jd_loc` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Month** — 月 `January`（默认）| `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

用于从 J2000.0 历元计算儒略世纪的月份。

#### 依赖关系

要启用此参数：

- 将 **Type of gravity model** 设置为 `WGS84 Close Approximation` 或 `WGS84 Exact`。
- 选择 **Precessing reference frame**。

要禁用此参数，请选择 **Input Julian date**。

#### 编程使用

|  |
| --- |
| **模块参数**：`month` |
| **类型**：字符向量 |
| **值**：`'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认值**：`'January'` |

### **Day** — 日 10（默认）| `1` 到 `31`

用于从 J2000.0 历元计算儒略世纪的日期。

#### 依赖关系

要启用此参数：

- 将 **Type of gravity model** 设置为 `WGS84 Close Approximation` 或 `WGS84 Exact`。
- 选择 **Precessing reference frame**。

要禁用此参数，请选择 **Input Julian date**。

#### 编程使用

|  |
| --- |
| **模块参数**：`day` |
| **类型**：字符向量 |
| **值**：`'1'` 到 `'31'` |
| **默认值**：`'10'` |

### **Year** — 年 2004（默认）| 任意年份

用于从 J2000.0 历元计算儒略世纪的年份。年份必须为 2000 或更大。

#### 依赖关系

要启用此参数：

- 将 **Type of gravity model** 设置为 `WGS84 Close Approximation` 或 `WGS84 Exact`。
- 选择 **Precessing reference frame**。
- 要禁用此参数，请选择 **Input Julian date**。

#### 编程使用

|  |
| --- |
| **模块参数**：`year` |
| **类型**：字符向量 |
| **值**：任意年份 |
| **默认值**：`'2004'` |

### **No centrifugal effects** — 离心效应 `on`（默认）| `off`

- 要使计算的重力基于由正常引力势产生的纯吸引力，请选中此复选框。
- 要使计算的重力包含由地球角速度产生的离心力，请清除此复选框。

此选项仅在 **Type of gravity model WGS84 Close Approximation** 或 **WGS84 Exact** 时可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`no_centrifugal` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `Warning`（默认）| `Error` | `None`

超出范围时的模块行为，指定如下。

| 值 | 描述 |
| --- | --- |
| `None` | 无动作。该模块对输入信号施加上限和下限。对于超出限制的输入，实现会被扩展。 |
| `Warning` | 在 Diagnostic Viewer 中发出警告，模型仿真继续。对于 Accelerator 和 Rapid Accelerator 模式，将动作设置为 `Warning` 没有效果，模型的行为如同该动作设置为 `None`。 |
| `Error` | MATLAB® 返回异常，模型仿真停止。对于 Accelerator 和 Rapid Accelerator 模式，将动作设置为 `Error` 没有效果，模型的行为如同该动作设置为 `None`。 |

不建议对超出限制的输入使用 WGS84 Gravity Model。

#### 编程使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |
## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现 1984 世界大地测量系统（WGS84）对地球重力的表示

WGS84 Gravity Model 模块实现世界大地测量系统（WGS84）地心等势椭球的数学表示。该模块输出为特定位置处的地球重力。要控制重力精度，请使用 **Type of gravity model** 参数。

模块图标显示从 **Units** 列表中选择的输入和输出单位。
