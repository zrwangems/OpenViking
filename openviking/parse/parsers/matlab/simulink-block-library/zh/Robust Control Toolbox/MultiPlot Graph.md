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
```yaml
ports:
- name: Port_1(y)
  summary: 要绘制的信号 标量 | 向量
  direction: input
```

### 输入

### **Port\_1(y)** — 要绘制的信号 标量 | 向量

提供标量信号将创建一个绘图。要创建多个子图，请将要绘制的信号合并为向量信号，使用如下模块：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
## 参数
```yaml
parameters:
- name: t-min
  summary: X 轴下限 0（默认）| 标量 | 向量
  group: ''
  block_parameter: tmin
  type: scalar, vector
  default: '0'
- name: t-max
  summary: X 轴上限 20（默认）| 标量 | 向量
  group: ''
  block_parameter: tmax
  type: scalar, vector
  default: '20'
- name: y-min
  summary: Y 轴下限 –1（默认）| 标量 | 向量
  group: ''
  block_parameter: ymin
  type: scalar, vector
  default: –1
- name: y-max
  summary: Y 轴上限 1（默认）| 标量 | 向量
  group: ''
  block_parameter: ymax
  type: scalar, vector
  default: '1'
- name: Plot title
  summary: 图窗标题 空（默认）| 字符向量
  group: ''
  block_parameter: titleString
  type: character vector
  default: ''''''
- name: Workspace variable for export
  summary: 用于保存绘图数据的变量名 multisimout（默认）| 字符向量
  group: ''
  block_parameter: vnamesave
  type: character vector
  default: ''''''
```

### **t-min** — X 轴下限 0（默认）| 标量 | 向量

**t-min** 和 **t-max** 参数用于设置 *x* 轴范围。要为每个子图设置不同的下限，请将 **t-min** 设置为与输入信号维度相同的向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`tmin` |
| **类型**：scalar, vector |
| **默认值**：0 |

### **t-max** — X 轴上限 20（默认）| 标量 | 向量

**t-min** 和 **t-max** 参数用于设置 *x* 轴范围。要为每个子图设置不同的上限，请将 **t-max** 设置为与输入信号维度相同的向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`tmax` |
| **类型**：scalar, vector |
| **默认值**：20 |

### **y-min** — Y 轴下限 –1（默认）| 标量 | 向量

**y-min** 和 **y-max** 参数用于设置 *y* 轴范围。要为每个子图设置不同的下限，请将 **y-min** 设置为与输入信号维度相同的向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`ymin` |
| **类型**：scalar, vector |
| **默认值**：–1 |

### **y-max** — Y 轴上限 1（默认）| 标量 | 向量

**y-min** 和 **y-max** 参数用于设置 *y* 轴范围。要为每个子图设置不同的上限，请将 **y-max** 设置为与输入信号维度相同的向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`ymax` |
| **类型**：scalar, vector |
| **默认值**：1 |

### **Plot title** — 图窗标题 空（默认）| 字符向量

指定该模块生成的 MATLAB 图窗的标题。

#### 编程使用

|  |
| --- |
| **模块参数**：`titleString` |
| **类型**：character vector |
| **默认值**：`''` |

### **Workspace variable for export** — 用于保存绘图数据的变量名 `multisimout`（默认）| 字符向量

要将绘图数据导出到 MATLAB 工作区，请在图窗窗口中点击导出图标。该模块会将数据导出到您在此参数中指定的变量名。数据保存在一个 `struct` 数组中，包含以下字段：

- `time` — 记录输入值时的仿真时间列向量。
- `signals` — 包含样本值的结构体，包含以下字段：

  - `values` — 样本值数组。
  - `dimensions` — 样本维度。
  - `label` — 模型中信号线的名称。
- `blockName` — MultiPlot Graph 模块的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`vnamesave` |
| **类型**：character vector |
| **默认值**：`''` |
## 所属库

Robust Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2007a 中引入**

### R2023a：模块继承上游采样时间

**Sample time** 参数已被移除。该模块现在使用其输入信号的采样时间。此前，该模块会按指定的采样时间对输入信号进行重采样，或者当 **Sample time** 设置为 –1 时使用上游采样时间。

### R2023a：参数名称已更改

- **Title** 现在称为 **Plot title**。
- **Variable for Export to Workspace** 现在称为 **Workspace variable for export**。

## 描述

绘制多次仿真的结果

MultiPlot Graph 模块显示在您对模型进行仿真时生成的 MATLAB® 图窗中的信号。在随后的每次仿真中，该模块会向图窗添加一条新线，并循环使用七种颜色。该模块允许您在单个 MATLAB 图窗上查看多次仿真的结果。例如，您可以将该模块与 Uncertain State Space 模块一起使用，以可视化蒙特卡洛和最坏情况仿真时间响应。

输入信号可以是标量或向量。如果输入信号是向量，则该模块会在单独的坐标轴中绘制向量的每个分量。

要将可见的绘图数据导出到 MATLAB 工作区，请在图窗中点击导出图标。该模块会将数据导出到具有您在 Workspace variable for export 参数中指定的名称的变量中。

要清除所有坐标轴中的数据，请在图窗中点击橡皮擦图标。
