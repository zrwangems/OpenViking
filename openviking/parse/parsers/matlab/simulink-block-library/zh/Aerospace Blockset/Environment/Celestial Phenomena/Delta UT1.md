---
type: simulink-block
title: 'Delta UT1'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'deltaut1'
documentation_source_path: 'deltaut1.html'
language: zh-CN
chinese_source: worker-translation
---

# Delta UT1

## 端口

### 输入

### **UTC** — UTC 的 UT1 修正儒略日

UTC 的 UT1，指定为修正儒略日。使用 `mjuliandate` 函数将 UTC 日期转换为修正儒略日。

**数据类型：** `double`
### 输出参数

### **ΔUT1** — UT1 与 UTC 之间的差值 double

UT1 与 UTC 之间的差值。

**数据类型：** `double`

## 参数

### **IERS data file** — 地球定向数据 `aeroiersdata.mat`（默认）| MAT 文件

自定义的地球定向数据列表，以 MAT 文件指定。

#### 程序化使用

|  |
| --- |
| **模块参数**：`FileName` |
| **类型**：字符向量 |
| **值**：`'aeroiersdata.mat'` | MAT 文件 |
| **默认值**：`'aeroiersdata.mat'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `None`（默认）| `Warning` | `Error`

超出范围时的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 不执行任何操作。 |
| `Warning` | 在诊断查看器中显示警告，模型仿真继续。 |
| `Error`（默认） | 在诊断查看器中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

### **IERS data URL** — 网站或地球定向数据文件 `https://maia.usno.navy.mil/ser7/finals2000A.data`（默认）| 网站地址 | 文件名

包含 IAU 2000A 地球定向数据的网站或地球定向数据文件，指定为网站地址或文件名。

**注意**

如果在访问默认站点时收到错误消息，请使用以下备用站点之一：

- `https://datacenter.iers.org/data/latestVersion/10_FINALS.DATA_IAU2000_V2013_0110.txt`
- `ftp://cddis.gsfc.nasa.gov/pub/products/iers/finals2000A.data`

#### 程序化使用

|  |
| --- |
| **模块参数**：`iersurl` |
| **类型**：字符向量 |
| **值**：`'https://maia.usno.navy.mil/ser7/finals2000A.data'` | 网站地址 | 文件名 |
| **默认值**：`'https://maia.usno.navy.mil/ser7/finals2000A.data'` |

### **Destination folder** — IERS 数据文件的文件夹 Current Folder（默认）

IERS 数据文件的文件夹，指定为字符数组或字符串。
在运行此函数之前，请创建具有写入权限的 *foldername*。

要在目标文件夹中创建 IERS 数据文件，请点击 **Create** 按钮。

#### 程序化使用

|  |
| --- |
| **模块参数**：`folder` |
| **类型**：字符向量 |
| **值**：`'Current Folder'` | 文件夹名称 |
| **默认值**：`'Current Folder'` |

## 所属库

Aerospace Blockset / Environment / Celestial Phenomena Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2020b：更新了 `aeroiersdata.mat` 文件

`aeroiersdata.mat` 文件的内容已更新。
相应地，当使用默认值（`'aeroiersdata.mat'`）作为
**IERS data file** 参数的值时，此模块的输出将产生不同的结果。这些结果反映了来自国际地球自转和参考系统服务（IERS）更准确的外部数据。

## 描述

根据国际天文学联合会（IAU）2000A 参考系统计算主世界时（UT1）与协调世界时（UTC）之间的差值

Delta UT1 模块根据 IAU 2000A 参考系统和地球定向数据计算主 UT1 与 UTC 之间的差值。默认情况下，此模块使用预填充的国际地球自转和参考系统服务（IERS）数据列表。此列表包含 IERS 提供的测量数据和计算（预测）数据。IERS 为一组预定日期测量和计算此数据。对于预填充列表中列出的日期之后的日期，Delta UT1 使用以下方程计算数据，并将值限制在 +/- .9s 范围内：

```
UT1-UTC=0.5309-0.00123(MJD-57808)-(UT2-UT1)
```
