---
type: simulink-block
title: 'Piecewise Linear Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'piecewiselinearcurrentsource'
documentation_source_path: 'ref/piecewiselinearcurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Piecewise Linear Current Source

## 端口
```yaml
ports:
- name: +
  summary: 正极端子 electrical
  direction: conserving
- name: '-'
  summary: 负极端子 electrical
  direction: conserving
```

### 守恒端口

### **+** — 正极端子 electrical

与分段线性电流源正极端子关联的电气守恒端口。

### **-** — 负极端子 electrical

与分段线性电流源负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Time specification
  summary: 时间值向量 [0, 1, 2, 3, 4] s（默认）
  group: ''
- name: Current at specified time
  summary: 电流值向量 [0, 0, 0, 0, 0] A（默认）
  group: ''
- name: Interpolation method
  summary: 插值方法 Linear（默认）| Smooth
  group: ''
- name: Extrapolation method
  summary: 外推方法 Nearest（默认）| Linear
  group: ''
- name: Include parallel conductance, GMIN
  summary: 是否包含并联电导 Yes（默认）| No
  group: ''
```

### **Time specification** — 时间值向量 `[0, 1, 2, 3, 4]` `s`（默认）

以制表 1×*n* 数组形式表示的时间值向量。时间值向量必须严格单调递增。

### **Current at specified time** — 电流值向量 `[0, 0, 0, 0, 0]` `A`（默认）

以制表 1×*n* 数组形式表示的电流值向量。电流值向量的大小必须与时间值向量相同。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

选择模块用于确定前述向量中未指定的中间时间点处输出电流值的方法：

- `Linear` — 通过使用线性函数优先考虑性能。
- `Smooth` — 通过生成具有连续一阶导数的连续曲线优先考虑精度。

### **Extrapolation method** — 外推方法 `Nearest`（默认）| `Linear`

选择模块用于确定前述向量中指定的时间范围之外的时间点处输出电流值的方法：

- `Nearest` — 选择此选项以使用最近的输入值进行外推。
- `Linear` — 选择此选项以使用线性函数。

### **Include parallel conductance, GMIN** — 是否包含并联电导 `Yes`（默认）| `No`

指定电流源是否包含并联电导。并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

下表显示了并联电导 *GMIN* 的可能值：

**并联电导 GMIN 的值**

| Include parallel conductance, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **模型包含 Environment Parameters 模块** | **模型不包含 Environment Parameters 模块** | 不包含并联电导 *GMIN*，且它不影响电流源。 | | |
| *GMIN* 等于 Environment Parameters 模块中 **GMIN** 参数的值。 | *GMIN* = `1e-12` `Ohm` |
## 所属库

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

使用查找表的时变电流源

Piecewise Linear Current Source 模块表示以查找表形式指定的电流源，使用时间值向量和相应的电流值向量进行指定。您必须至少指定两对时间-电流值。该模块使用选定的插值方法和外推方法，基于这些时间-电流值生成时变电流。您可以选择两种插值方法和外推方法。输出电流与源端子两端的电压无关。

该模块内部使用一个小电导来防止数值仿真问题。该电导连接器件的 **+** 和 **-** 端口，其电导为 *GMIN*：

- 默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 `1e–12``1/Ohm`。
- 要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型中，并将 **GMIN** 参数设置为所需的值。
