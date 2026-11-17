---
type: simulink-block
title: 'Centrifugal Effect Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'centrifugaleffectmodel'
documentation_source_path: 'centrifugaleffectmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Centrifugal Effect Model

## 端口
```yaml
ports:
- name: Xecef
  summary: 行星中心行星固定坐标 m×3 矩阵
  direction: input
  data_types: double
- name: ω
  summary: 行星自转速率 标量
  direction: input
  data_types: double
- name: Output 1
  summary: 重力值 m×3 数组
  direction: output
  data_types: double
```

### 输入

### **Xecef** — 行星中心行星固定坐标 m×3 矩阵

从行星中心出发的行星中心行星固定坐标，指定为标量。如果 **Planet model** 的值为 `Earth`，则该矩阵包含地心地球固定（ECEF）坐标。该模块不使用显式单位。

**数据类型：** `double`

### **ω** — 行星自转速率 标量

行星自转速率，指定为标量，单位为 rad/sec。

#### 依赖关系

要启用此参数，请将 **Planetary rotational rate (rad/sec)** 设置为 `Custom`。

**数据类型：** `double`
### 输出

### **Output 1** — 重力值 m×3 数组

重力值，以 m×3 数组形式返回，分别位于行星中心行星固定坐标的 *x* 轴、*y* 轴和 *z* 轴上，单位为输入距离单位每秒平方。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Planet model
  summary: 行星模型 Earth（默认）| Venus | Mercury | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Custom
  group: ''
  block_parameter: ptype
  type: character vector
  values: '''Mercury'' | ''Venus'' | ''Earth'' | ''Moon'' | ''Mars'' | ''Jupiter'' | ''Saturn'' | ''Uranus'' | ''Neptune''
    | ''Custom'''
  default: '''Earth'''
- name: Planetary rotational rate (rad/sec)
  summary: 行星自转速率 7.2921150e-05（默认）| 标量
  group: ''
  block_parameter: omega
  type: character vector
  values: '''7.2921150e-05'' | scalar'
  default: '''7.2921150e-05'''
- name: Input planetary rotation rate
  summary: 行星自转速率端口 off（默认）| on
  group: ''
  block_parameter: rate_loc
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### **Planet model** — 行星模型 `Earth`（默认）| `Venus` | `Mercury` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Custom`

行星模型，指定为 `Mercury`、`Venus`、`Earth`、`Moon`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune` 或 `Custom`。该模块使用所选行星的自转来实现离心效应的数学表示。

#### 依赖关系

选择 `Custom` 会启用 **Planetary rotational rate (rad/sec)** 和 **Input planetary rotation rate** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`ptype` |
| **类型**：character vector |
| **值**：`'Mercury'` | `'Venus'` | `'Earth'` | `'Moon'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Custom'` |
| **默认值**：`'Earth'` |

### **Planetary rotational rate (rad/sec)** — 行星自转速率 `7.2921150e-05`（默认）| 标量

行星自转速率，单位为弧度每秒。

如果要将行星自转速率指定为模块的输入，请参阅 **Input planetary rotation rate** 参数。

#### 依赖关系

选中 **Input planetary rotation rate** 复选框会禁用 **Planetary rotational rate (rad/sec)** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`omega` |
| **类型**：character vector |
| **值**：`'7.2921150e-05'` | scalar |
| **默认值**：`'7.2921150e-05'` |

### **Input planetary rotation rate** — 行星自转速率端口 `off`（默认）| `on`

选中此复选框以启用 ω 输入端口。然后可以将行星自转速率作为模块输入。

#### 依赖关系

选中此复选框会启用 ω 并禁用 **Planetary rotational rate (rad/sec)** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`rate_loc` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |
## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

实现行星重力的离心效应数学表示

Centrifugal Effect Model 模块实现行星重力的离心效应数学表示。重力离心效应是由于行星自转产生的离心力效应中的加速度部分。该模块使用行星自转速率来实现此表示。您在旋转或非惯性坐标系中使用离心力值。
