---
type: simulink-block
title: 'Julian Date Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'juliandateconversion'
documentation_source_path: 'juliandateconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Julian Date Conversion

## 端口

### 输入

### **day** — 时钟源 标量 | 数组

模型仿真的时钟源，指定为标量或数组。

#### 依赖关系

此端口的存在和标签取决于 **Time increment** 参数。

| 端口 | Time increment 设置 |
| --- | --- |
| day | `Day` |
| hour | `Hour` |
| min | `Min` |
| sec | `Sec` |
| 无输入端口 | `None` |

**数据类型：** `double`
### 输出

### **JD** — 儒略日 标量 | 数组

儒略日，以标量或数组形式返回。

#### 依赖关系

**数据类型：** `double`

## 参数

### **Year** — 年份 `2013`（默认）| double、整数、大于 1

年份，指定为标量，用于计算儒略日。

#### 编程用法

|  |
| --- |
| **模块参数**：`year` |
| **类型**：character vector |
| **取值**：double、大于 1 |
| **默认值**：`'2013'` |

### **Month** — 月份 `January`（默认）| `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

用于计算儒略日的月份。从列表中选择从 `January` 到 `December` 的月份。

#### 编程用法

|  |
| --- |
| **模块参数**：`month` |
| **类型**：character vector |
| **取值**：`'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认值**：`'January'` |

### **Day** — 日 `1`（默认）| `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

用于计算儒略日的日。从列表中选择从 `1` 到 `31` 的日。

#### 编程用法

|  |
| --- |
| **模块参数**：`day` |
| **类型**：character vector |
| **取值**：`'1'` | `'2'` | `'3'` | `'4'` | `'5'` | `'5'` | `'6'` | `'7'` | `'8'` | `'9'` | `'10'` | `'11'` | `'12'` | `'13'` | `'14'` | `'15'` | `'16'` | `'17'` | `'18'` | `'19'` | `'20'` | `'21'` | `'22'` | `'23'` | `'24'` | `'25'` | `'26'` | `'27'` | `'28'` | `'29'` | `'30'` | `'31'` |
| **默认值**：`'1'` |

### **Hour** — 小时 `0`（默认）| double、整数、`0` 到 `24`

用于计算儒略日的小时。输入从 `0` 到 `24` 的值。

#### 编程用法

|  |
| --- |
| **模块参数**：`hour` |
| **类型**：character vector |
| **取值**：double、整数、`0` 到 `24` |
| **默认值**：`'0'` |

### **Minutes** — 分钟 `0`（默认）| double、整数、`0` 到 `60`

用于计算儒略日的分钟。输入从 `0` 到 `60` 的数字。

#### 编程用法

|  |
| --- |
| **模块参数**：`min` |
| **类型**：character vector |
| **取值**：double、整数、`0` 到 `60` |
| **默认值**：`'0'` |

### **Seconds** — 秒 `0`（默认）| double、整数、`0` 到 `60`

指定用于计算儒略日的秒。输入从 `0` 到 `60` 的数字。

#### 编程用法

|  |
| --- |
| **模块参数**：`sec` |
| **类型**：character vector |
| **取值**：double、整数、`0` 到 `60` |
| **默认值**：`'0'` |

### **Calculate modified Julian date** — 修正儒略日 `off`（默认）| `on`

选中此复选框可计算年、月、日、小时、分钟和秒对应元素的修正儒略日 (MJD)。

#### 依赖关系

选中此复选框会将输出端口标签更改为 MJD。
清除此复选框会将输出端口标签更改为 JD。

#### 编程用法

|  |
| --- |
| **模块参数**：`modflag` |
| **类型**：character vector |
| **取值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Time increment** — 时间增量 `Day`（默认）| `Hour` | `Min` | `Sec` | `None`

指定日期与所需模型仿真时间之间的时间增量。该模块会调整计算出的儒略日，以考虑模型仿真的时间增量。例如，选择 `Day` 并将仿真计时器连接到端口，意味着每个时间增量单位是一天，模块会根据该仿真时间调整其计算。

如果选择 `None`，计算出的儒略日不会考虑模型仿真时间。选择此选项会移除第一个模块输入。

#### 依赖关系

此参数控制输出端口的存在和标签。

| Time increment 设置 | 端口 |
| --- | --- |
| `Day` | day |
| `Hour` | hour |
| `Min` | min |
| `Sec` | sec |
| `None` | 无输入端口 |

#### 编程用法

|  |
| --- |
| **模块参数**：`deltaT` |
| **类型**：character vector |
| **取值**：`'Day'` | `'Hour'` | `'Min'` | `'Sec'` | `'None'` |
| **默认值**：`'Day'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `None`（默认）| `Warning` | `Error`

超出范围的模块行为，指定如下。

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在 Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error`（默认） | 在 Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`errorflag` |
| **类型**：character vector |
| **取值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Error'` |

## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2013b 中引入**

## 描述

计算儒略日或修正儒略日

Julian Date Conversion 模块将指定日期转换为儒略日或修正儒略日。
