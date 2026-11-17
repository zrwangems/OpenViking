---
type: simulink-block
title: 'Earth Orientation Parameters'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'earthorientationparameters'
documentation_source_path: 'earthorientationparameters.html'
language: zh-CN
chinese_source: worker-translation
---

# Earth Orientation Parameters

## 端口
```yaml
ports:
- name: UTCMJD
  summary: UTC 标量
  direction: input
  data_types: double
- name: ΔUT1
  summary: UT1 与 UTC 之差标量
  direction: output
  data_types: double
- name: '[xp,yp]'
  summary: 地球极移向量
  direction: output
  data_types: double
- name: '[dX,dY]'
  summary: 天球中间极（CIP）位置调整向量
  direction: output
  data_types: double
- name: ΔUT1err
  summary: 返回 IERS 数据中测量值和预测值的误差向量
  direction: output
- name: '[xp,yp]err'
  summary: 返回 IERS 数据中测量值和预测值的误差向量
  direction: output
- name: '[dX,dY]err'
  summary: 返回 IERS 数据中测量值和预测值的误差向量
  direction: output
```

### 输入

### **UTCMJD** — UTC 标量

UTC，指定为标量修正儒略日。使用 Julian Date Conversion 模块将 UTC 日期转换为修正儒略日。

**数据类型：** `double`
### 输出

### **ΔUT1** — UT1 与 UTC 之差标量

UT1 与 UTC 之差，指定为标量，单位为秒。

**数据类型：** `double`

### **[xp,yp]** — 地球极移向量

地球极移，[*xp*,*yp*]，指定为向量，单位为弧度，表示地壳运动沿 *x* 轴和 *y* 轴的分量。

**数据类型：** `double`

### **[dX,dY]** — 天球中间极（CIP）位置调整向量

天球中间极（CIP）位置调整，指定为向量，单位为弧度。该位置（[d*X*,d*Y*]）沿 *x* 轴和 *y* 轴方向。

**数据类型：** `double`

### **ΔUT1err** — 返回 IERS 数据中测量值和预测值的误差向量

返回 IERS 数据中 UT1 与 UTC 之差的测量值和预测值的误差，指定为向量，单位为秒。

#### 依赖关系

当选中 **Output parameter error** 时，此端口启用。

### **[xp,yp]err** — 返回 IERS 数据中测量值和预测值的误差向量

返回 IERS 数据中地球极移的测量值和预测值的误差，指定为向量，单位为弧度。

#### 依赖关系

当选中 **Output parameter error** 时，此端口启用。

### **[dX,dY]err** — 返回 IERS 数据中测量值和预测值的误差向量

返回 IERS 数据中天球中间极（CIP）位置调整的测量值和预测值的误差，指定为向量，单位为弧度。

#### 依赖关系

当选中 **Output parameter error** 时，此端口启用。
## 参数
```yaml
parameters:
- name: IERS data file
  summary: 地球定向数据 aeroiersdata.mat（默认）| MAT 文件
  group: ''
  block_parameter: FileName
  type: character vector
  values: scalar
  default: '''aeroiersdata.mat'''
- name: Output parameter error
  summary: 启用输出端口以返回误差 off（默认）| on
  group: ''
  block_parameter: OutputError
  type: character vector
  values: scalar
  default: '''off'''
- name: Action for out-of-range input
  summary: 超出范围时的模块行为 None（默认）| Warning | Error
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: IERS data URL
  summary: 网站或地球定向数据文件 http://maia.usno.navy.mil/ser7/finals2000A.data（默认）| 网站地址 | 文件名
  group: ''
  block_parameter: FileName
  type: character vector
  values: scalar
  default: '''aeroiersdata.mat'''
- name: Destination folder
  summary: IERS 数据文件的文件夹 当前文件夹（默认）
  group: ''
  block_parameter: FileName
  type: character vector
  values: scalar
  default: '''aeroiersdata.mat'''
```

### **IERS data file** — 地球定向数据 `aeroiersdata.mat`（默认）| MAT 文件

自定义地球定向数据列表，以 MAT 文件指定。

#### 编程使用

|  |
| --- |
| **模块参数**：`FileName` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'aeroiersdata.mat'` |

### **Output parameter error** — 启用输出端口以返回误差 `off`（默认）| `on`

选中此参数以启用输出端口，返回 IERS 数据文件中测量值和预测值的误差：

- UT1 与 UTC 之差
- 地球极移
- 天球中间极（CIP）位置调整

#### 依赖关系

选中此复选框将启用以下端口：

- ΔUT1err
- [xp,yp]err
- [dX,dY]err

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputError` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'off'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `None`（默认）| `Warning` | `Error`

超出范围时的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在诊断查看器中显示警告，模型仿真继续。 |
| `Error`（默认） | 在诊断查看器中显示错误，模型仿真停止。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

### **IERS data URL** — 网站或地球定向数据文件 `http://maia.usno.navy.mil/ser7/finals2000A.data`（默认）| 网站地址 | 文件名

包含根据 IAU 2000A 的地球定向数据的网站或地球定向数据文件，指定为网站地址或文件名。

**注意**

如果在访问默认站点时收到错误消息，请使用以下备用站点之一：

- `https://datacenter.iers.org/data/latestVersion/10_FINALS.DATA_IAU2000_V2013_0110.txt`
- `ftp://cddis.gsfc.nasa.gov/pub/products/iers/finals2000A.data`

#### 编程使用

|  |
| --- |
| **模块参数**：`FileName` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'aeroiersdata.mat'` |

### **Destination folder** — IERS 数据文件的文件夹 当前文件夹（默认）

IERS 数据文件的文件夹，指定为字符数组或字符串。在运行此函数之前，请创建具有写入权限的 *foldername*。

要在目标文件夹中创建 IERS 数据文件，请点击 **Create** 按钮。

#### 编程使用

|  |
| --- |
| **模块参数**：`FileName` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'aeroiersdata.mat'` |
## 所属库

Aerospace Blockset / Environment / Celestial Phenomena

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2020b：更新了 `aeroiersdata.mat` 文件

`aeroiersdata.mat` 文件的内容已更新。相应地，当使用默认值（`'aeroiersdata.mat'`）作为 **IERS data file** 参数的值时，此模块的输出将产生不同的结果。这些结果反映了来自国际地球自转和参考系统服务（IERS）的更准确的外部数据。

## 描述

计算地球定向参数（EOP）

Earth Orientation Parameters 模块计算以下参数：

- 协调世界时（UTC）与世界时（UT1）之差
- 旋转轴相对于地壳的运动
- 天球中间极（CIP）位置调整

默认情况下，此模块使用预填充的国际地球自转和参考系统服务（IERS）数据列表。此列表包含 IERS 提供的测量数据和计算（预测）数据。IERS 针对一组预定日期测量和计算此数据。对于预填充列表中列出的日期之后的日期，Earth Orientation Parameters 使用以下方程计算 ΔUT1，并将值限制在 +/- 0.9 秒：

```
UT1-UTC=0.5309-0.00123(MJD-57808)-(UT2-UT1)
```

当您的应用使用地心惯性到地心地球固定坐标变换时（例如高空应用），请使用此模块。
