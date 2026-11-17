---
type: simulink-block
title: '3-Phase Sine Voltage Generator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: '3phasesinevoltagegenerator'
documentation_source_path: 'ref/3phasesinevoltagegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# 3-Phase Sine Voltage Generator

## 端口
```yaml
ports:
- name: A
  summary: 参考电压幅值标量
  direction: input
  data_types: single | double | fixed point
- name: θe
  summary: 参考电压位置标量
  direction: input
  data_types: single | double | fixed point
- name: Va
  summary: 平衡三相电压的 *a* 轴分量标量
  direction: output
  data_types: single | double | fixed point
- name: Vb
  summary: 平衡三相电压的 *b* 轴分量标量
  direction: output
  data_types: single | double | fixed point
- name: Vc
  summary: 平衡三相电压的 *c* 轴分量标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **A** — 参考电压幅值标量

参考电压信号的最大幅值。

**数据类型：** `single` | `double` | `fixed point`

### **θe** — 参考电压位置标量

参考电压信号的位置或相位值。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Va** — 平衡三相电压的 *a* 轴分量标量

平衡三相电压信号沿 *abc* 参考坐标系 *a* 轴的分量。

**数据类型：** `single` | `double` | `fixed point`

### **Vb** — 平衡三相电压的 *b* 轴分量标量

平衡三相电压信号沿 *abc* 参考坐标系 *b* 轴的分量。

**数据类型：** `single` | `double` | `fixed point`

### **Vc** — 平衡三相电压的 *c* 轴分量标量

平衡三相电压信号沿 *abc* 参考坐标系 *c* 轴的分量。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Theta units
  summary: θe 的单位 Per-unit（默认）| Radians | Degrees
  group: ''
- name: Number of data points for lookup table
  summary: 查找表的大小 1024（默认）| 标量
  group: ''
```

### **Theta units** — `θe` 的单位 `Per-unit`（默认）| `Radians` | `Degrees`

作为输入提供的参考电压位置的单位。

### **Number of data points for lookup table** — 查找表的大小 `1024`（默认）| 标量

查找表的大小。
## 所属库

Motor Control Blockset / Controls / Math Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

生成平衡三相正弦信号

3-Phase Sine Voltage Generator 模块使用信号幅值和位置输入生成平衡三相正弦信号。

该模块使用查找表方法。当与 Motor Control Blockset™ 中提供的示例所采用的模型设置和配置一起使用时，此方法可实现优化的代码执行。您可以在 **Number of data points for lookup table** 参数中指定查找表的点数。

下图显示了位置输入和三相正弦输出信号随时间变化的曲线图。

### 方程

以下方程描述了该模块如何计算平衡三相正弦信号。

- Va=A×sinωt
- Vb=A×sin(ωt−2π3)
- Vc=A×sin(ωt−4π3)

其中：

- A 是参考电压幅值（伏特）。
- ω 是参考电压位置输入信号（`θe`）的频率（弧度/秒）。
- t 是时间（秒）。
