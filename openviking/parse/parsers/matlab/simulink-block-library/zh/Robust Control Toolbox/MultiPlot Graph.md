---
type: simulink-block
title: 'MultiPlot Graph'
family: 'robust'
product_id: 'robust'
product_name: 'Robust Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'multiplotgraph'
documentation_source_path: 'ref/multiplotgraph.html'
language: zh-CN
chinese_source: worker-translation
---

# MultiPlot Graph

## 端口

### 输入

### **Port\_1(y)** — 要绘制的信号 scalar | vector

提供 scalar 信号会创建一个绘图。要创建多个子图，请使用如下模块将要绘制的信号合并为 vector 信号：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)

## 参数

### **t-min** — X 轴下限 0（默认）| scalar | vector

**t-min** 和 **t-max** 参数设置 *x* 轴范围。要为每个子图设置不同的下限，请将 **t-min** 设置为与输入信号维度相同的 vector。

#### 编程用法

|  |
| --- |
| **模块参数：** `tmin` |
| **类型：** scalar, vector |
| **默认值：** 0 |

### **t-max** — X 轴上限 20（默认）| scalar | vector

**t-min** 和 **t-max** 参数设置 *x* 轴范围。要为每个子图设置不同的上限，请将 **t-max** 设置为与输入信号维度相同的 vector。

#### 编程用法

|  |
| --- |
| **模块参数：** `tmax` |
| **类型：** scalar, vector |
| **默认值：** 20 |

### **y-min** — Y 轴下限 –1（默认）| scalar | vector

**y-min** 和 **y-max** 参数设置 *y* 轴范围。要为每个子图设置不同的下限，请将 **y-min** 设置为与输入信号维度相同的 vector。

#### 编程用法

|  |
| --- |
| **模块参数：** `ymin` |
| **类型：** scalar, vector |
| **默认值：** –1 |

### **y-max** — Y 轴上限 1（默认）| scalar | vector

**y-min** 和 **y-max** 参数设置 *y* 轴范围。要为每个子图设置不同的上限，请将 **y-max** 设置为与输入信号维度相同的 vector。

#### 编程用法

|  |
| --- |
| **模块参数：** `ymax` |
| **类型：** scalar, vector |
| **默认值：** 1 |

### **绘图标题** — 图标题 空（默认）| character vector

指定该模块生成的 MATLAB 图形的标题。

#### 编程用法

|  |
| --- |
| **模块参数：** `titleString` |
| **类型：** character vector |
| **默认值：** `''` |

### **用于导出的工作区变量** — 用于保存绘图数据的变量名 `multisimout`（默认）| character vector

要将绘图数据导出到 MATLAB 工作区，请在图形窗口中点击导出图标。该模块将数据导出到变量中，变量名称由您在此参数中指定。数据保存在具有以下字段的 `struct` 数组中：

- `time` — 记录输入值时的仿真时间列向量。
- `signals` — 包含样本值并具有以下字段的结构体：

  - `values` — 样本值数组。
  - `dimensions` — 样本维度。
  - `label` — 模型中信号线的名称。
- `blockName` — MultiPlot Graph 模块的名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `vnamesave` |
| **类型：** character vector |
| **默认值：** `''` |

## 所属库

Robust Control Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2007a 中引入**

### R2023a：模块继承上游采样时间

**采样时间** 参数已删除。该模块现在使用其输入信号的采样时间。以前，该模块按指定的采样时间对输入信号进行重采样，或者当 **采样时间** 设置为 –1 时使用上游采样时间。

### R2023a：参数名称已更改

- **标题** 现在称为 **绘图标题**。
- **用于导出到工作区的变量** 现在称为 **用于导出的工作区变量**。

## 描述

绘制多次仿真的结果

MultiPlot Graph 模块在您仿真模型时生成的 MATLAB® 图形窗口中显示信号。在每次后续仿真中，该模块向图形添加一条新线，并循环使用七种颜色。该模块允许您在单个 MATLAB 图形中查看多次仿真的结果。例如，您可以将该模块与 Uncertain State Space 模块一起使用，以可视化蒙特卡洛和最坏情况仿真时间响应。

输入信号可以是 scalar 或 vector。如果输入信号是 vector，则该模块在单独的坐标轴中绘制 vector 的每个分量。

要将可见绘图数据导出到 MATLAB 工作区，请在图形窗口中点击导出图标。该模块将数据导出到变量中，变量名称由您在用于导出的工作区变量参数中指定。

要清除所有坐标轴中的数据，请在图形窗口中点击橡皮擦图标。
