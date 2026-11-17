---
type: simulink-block
title: 'Relative Ratio'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'relativeratio'
documentation_source_path: 'relativeratio.html'
language: zh-CN
chinese_source: worker-translation
---

# Relative Ratio

## 端口
```yaml
ports:
- name: Mach
  summary: 马赫数标量
  direction: input
  data_types: double
- name: γ
  summary: 比值标量
  direction: input
  data_types: double
- name: To
  summary: 静温标量
  direction: input
  data_types: double
- name: Po
  summary: 静压标量
  direction: input
  data_types: double
- name: ρo
  summary: 静密度标量
  direction: input
  data_types: double
- name: θ
  summary: 相对温度比标量
  direction: output
  data_types: double
- name: sqrt(θ)
  summary: 相对温度比的平方根标量
  direction: output
  data_types: double
- name: δ
  summary: 相对压力比标量
  direction: output
  data_types: double
- name: σ
  summary: 相对密度比标量
  direction: output
  data_types: double
```

### 输入

### **Mach** — 马赫数标量

马赫数，指定为标量。

**数据类型：** `double`

### **γ** — 比值标量

定压比热（*Cp*）与定容比热（*Cv*）之间的比值，指定为标量。例如，（*γ* = *Cp*/*Cv*）。

**数据类型：** `double`

### **To** — 静温标量

静温，指定为标量。

**数据类型：** `double`

### **Po** — 静压标量

静压，指定为标量。

**数据类型：** `double`

### **ρo** — 静密度标量

静密度，指定为标量。

**数据类型：** `double`
### 输出

### **θ** — 相对温度比标量

相对温度比（*θ*），以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Theta**。

**数据类型：** `double`

### **sqrt(θ)** — 相对温度比的平方根标量

相对温度比的平方根（θ），以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Square root of theta**。

**数据类型：** `double`

### **δ** — 相对压力比标量

相对压力比（*δ*），以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Delta**。

**数据类型：** `double`

### **σ** — 相对密度比标量

相对密度比（*σ*），以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Sigma**。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 单位 Metric (MKS)（默认）| English
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English'''
- name: Theta
  summary: 相对温度比 on（默认）| off
  group: ''
  block_parameter: theta
  type: 字符向量
  values: '''on'' | ''off'''
- name: Square root of theta
  summary: 相对温度比的平方根 on（默认）| off
  group: ''
  block_parameter: sq_theta
  type: 字符向量
  values: '''on'' | ''off'''
- name: Delta
  summary: 相对压力比 on（默认）| off
  group: ''
  block_parameter: delta
  type: 字符向量
  values: '''on'' | ''off'''
- name: Sigma
  summary: 相对密度比 on（默认）| off
  group: ''
  block_parameter: sigma
  type: 字符向量
  values: '''on'' | ''off'''
```

### **Units** — 单位 `Metric (MKS)`（默认）| `English`

输入单位，指定为：

| 单位 | Tstatic | Pstatic | rho\_static |
| --- | --- | --- | --- |
| `Metric (MKS)` | Kelvin | Pascal | Kilograms per cubic meter |
| `English` | Degrees Rankine | Pound force per square inch | Slug per cubic foot |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认**：`'Metric (MKS)'` |

### **Theta** — 相对温度比 `on`（默认）| `off`

选中时，模块计算相对温度比（*θ*），并且静温为必需输入。

#### 程序化使用

|  |
| --- |
| **模块参数**：`theta` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'on'` |

### **Square root of theta** — 相对温度比的平方根 `on`（默认）| `off`

选中时，模块计算相对温度比的平方根（θ），并且静温为必需输入。

#### 依赖关系

选中此复选框将启用 sqrt(θ) 输出端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`sq_theta` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'on'` |

### **Delta** — 相对压力比 `on`（默认）| `off`

选中时，模块计算相对压力比（*δ*），并且静压为必需输入。

#### 程序化使用

|  |
| --- |
| **模块参数**：`delta` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'on'` |

### **Sigma** — 相对密度比 `on`（默认）| `off`

选中时，模块计算相对密度比（*σ*），并且静密度为必需输入。

#### 程序化使用

|  |
| --- |
| **模块参数**：`sigma` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认**：`'on'` |
## 所属库

Aerospace Blockset / Flight Parameters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算相对大气比值

Relative Ratio 模块计算相对大气比值，包括相对温度比（*θ*）、θ、相对压力比（*δ*）和相对密度比（*σ*）。

*θ* 表示选定参考站处的气流温度相对于海平面标准大气条件的比值：

θ=TT0。

*δ* 表示选定参考站处的气流压力相对于海平面标准大气条件的比值：

δ=PP0。

*σ* 表示选定参考站处的气流密度相对于海平面标准大气条件的比值：

σ=ρρ0。

Relative Ratio 模块图标显示从 **Units** 参数中选择的输入单位。
