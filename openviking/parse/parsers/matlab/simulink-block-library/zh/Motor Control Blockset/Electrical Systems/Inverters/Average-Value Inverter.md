---
type: simulink-block
title: 'Average Value Inverter'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Electrical Systems / Inverters'
documentation_page: 'averagevalueinverter'
documentation_source_path: 'ref/averagevalueinverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Average Value Inverter

## 端口
```yaml
ports:
- name: Dabc
  summary: 三相电压的占空比 1×3 数组
  direction: input
  data_types: single | double | fixed point
- name: Vdc
  summary: 逆变器直流电压 标量
  direction: input
  data_types: single | double | fixed point | uint8 | uint16 | uint32
- name: Vabc
  summary: 三相电压输出 1×3 数组
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **Dabc** — 三相电压的占空比 `1`×`3` 数组

用于生成驱动电机电压的三相调制指数，范围为 [0,1]。

**数据类型：** `single` | `double` | `fixed point`

### **Vdc** — 逆变器直流电压 标量

逆变器的直流母线电压输入。

**数据类型：** `single` | `double` | `fixed point` | `uint8` | `uint16` | `uint32`

### 输出

### **Vabc** — 三相电压输出 `1`×`3` 数组

与驱动电机的输入占空比对应的三相电压（伏特）。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Motor Control Blockset / Electrical Systems / Inverters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

根据逆变器直流电压计算三相交流电压

Average-Value Inverter 模块对平均值和全波逆变器进行建模。它通过使用占空比信息，根据逆变器直流电压计算三相交流电压输出。

### 方程

以下方程描述了该模块如何计算三相交流电压。

D0=(Da+Db+Dc)3

Va=Vdc×(Da−D0)

Vb=Vdc×(Db−D0)

Vc=Vdc×(Dc−D0)

其中：

- Da、Db 和 Dc 是范围在 0 到 1 之间的调制指数。
- Vdc 是逆变器的直流母线电压（伏特）。
- Va、Vb 和 Vc 是输出的三相电压（伏特）。
