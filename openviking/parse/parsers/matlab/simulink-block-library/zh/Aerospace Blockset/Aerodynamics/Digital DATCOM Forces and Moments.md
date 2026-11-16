---
type: simulink-block
title: 'Digital DATCOM Forces and Moments'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Aerodynamics'
documentation_page: 'digitaldatcomforcesandmoments'
documentation_source_path: 'digitaldatcomforcesandmoments.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital DATCOM Forces and Moments

## 端口

### 输入

### **Port\_1** — 迎角标量

迎角，指定为标量。

**数据类型：** `double`

### **Port\_2** — 侧滑角标量

侧滑角，指定为标量，以弧度为单位。

**数据类型：** `double`

### **Port\_3** — 马赫数标量

马赫数，指定为标量。

**数据类型：** `double`

### **Port\_4** — 高度标量

高度，指定为标量，采用所选长度单位。

**数据类型：** `double`

### **Port\_5** — 动压标量

动压，指定为标量，采用所选压力单位。

**数据类型：** `double`

### **Port\_6** — 速度三元素向量

速度，指定为三元素向量，采用所选速度单位和所选力轴。

**数据类型：** `double`

### **Port\_7** — 迎角速率标量

迎角速率，指定为标量，以弧度每秒为单位。

#### 依赖关系

当 Digital DATCOM 的输入中使用 DAMP Control Card 时出现。

**数据类型：** `double`

### **Port\_8** — 机体角速率三元素向量

机体角速率，指定为三元素向量，以弧度每秒为单位。

#### 依赖关系

当 Digital DATCOM 的输入中使用 DAMP Control Card 时出现。

**数据类型：** `double`

### **Port\_9** — 地面高度标量

地面高度，指定为标量，采用所选长度单位。

#### 依赖关系

当 Digital DATCOM 的输入中使用 GRNDEF Namelist 时出现。

**数据类型：** `double`

### **Port\_10** — 操纵面偏转标量

操纵面偏转，指定为标量，以弧度为单位。

#### 依赖关系

当 Digital DATCOM 的输入中使用 ASYFLP 或 SYMFLP 和 GRNDEF namelists 时出现。

**数据类型：** `double`
### 输出

### **Port\_1** — 重心处的空气动力三元素向量

重心处的空气动力，返回为三元素向量，在所选坐标系中：Body（*F*、*F*yx 和 *F*z），或 Wind（*F*D、*F*y 和 *F*L）。

**数据类型：** `double`

### **Port\_2** — 重心处的空气动力力矩三元素向量

重心处的空气动力力矩，返回为三元素向量，在机体坐标系中（*M*x、*M*y 和 *M*z）。

**数据类型：** `double`

## 参数

### **单位** — 单位 `Metric (MKS)` (默认) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 力 | 力矩 | 长度 | 速度 | 压力 |
| --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-  meter | Meters | Meters per second | Pascal |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet | Feet per second | Pound per square inch |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet | Knots | Pound per square inch |

#### 编程用法

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Digital DATCOM 结构** — Digital DATCOM 数据结构 `factstruct{1}` (默认) | structure

MATLAB® 结构，包含 digital DATCOM 数据。此结构由 `datcomimport` 函数生成。要在生成的输出文件中包含动态导数，请使用 `damp` 关键字调用 `datomimport` 函数。

有关创建 digital DATCOM 结构的详细信息，请参阅 Import from USAF Digital DATCOM Files。此示例说明如何使用 Aerospace Toolbox 软件将美国空军 (USAF) Digital DATCOM 文件导入 MATLAB 环境。

#### 编程用法

|  |
| --- |
| **模块参数**：`dcase` |
| **类型**：character vector |
| **值**：`factstruct{1}` | structure |
| **默认值**：`factstruct{1}` |

### **力轴** — 空气动力的坐标系 `Body` (默认) | `Wind`

空气动力的坐标系，指定为 `Body` 或 `Wind`。

#### 编程用法

|  |
| --- |
| **模块参数**：`fmode` |
| **类型**：character vector |
| **值**：`'Body'` | `'Wind'` |
| **默认值**：`'Body'` |

### **插值方法** — 插值方法 `None - flat` (默认) | `Linear`

插值方法，指定为 `None (flat)` 或 `Linear`。该模块使用插值方法对 **Digital DATCOM 结构**中的静态和动态稳定系数进行插值。

#### 编程用法

|  |
| --- |
| **模块参数**：`imethod` |
| **类型**：character vector |
| **值**：`'None (flat)'` | `'Linear'` |
| **默认值**：`'None (flat)'` |

### **外推方法** — 外推方法 `None - clip` (默认) | `Linear`

外推方法，指定为 `None (clip)` 或 `Linear`。该模块使用外推方法对 **Digital DATCOM 结构**中的静态和动态稳定系数进行外推。

#### 编程用法

|  |
| --- |
| **模块参数**：`emethod` |
| **类型**：character vector |
| **值**：`'None (flat)'` | `'Linear'` |
| **默认值**：`'None (flat)'` |

### **处理超出范围的输入** — 处理超出范围的输入 `Clip to Range` (默认) | `Linear Extrapolation`

处理超出范围的输入操作，`Linear Extrapolation` 或 `Clip to Range`。

#### 编程用法

|  |
| --- |
| **模块参数**：`rmethod` |
| **类型**：character vector |
| **值**：`'Clip to Range'` | `'Linear Extrapolation'` |
| **默认值**：`'Clip to Range'` |

### **超出范围输入的操作** — 超出范围的模块行为 `None` (默认) | `Warning` | `Error`

超出范围的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在诊断查看器中显示警告，模型仿真继续。 |
| `Error` (默认) | 在诊断查看器中显示错误，模型仿真停止。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

## 所属库

Aerospace Blockset / Aerodynamics

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006b 中引入**

## 描述

使用 Digital DATCOM 静态和动态稳定性导数计算空气动力和力矩

Digital DATCOM Forces and Moments 模块使用来自 Digital DATCOM 的空气动力系数计算重心处的空气动力和力矩。

Digital DATCOM Forces and Moments 模块的端口标签会根据从 **单位** 列表中选择的输入和输出单位而变化。
