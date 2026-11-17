---
type: simulink-block
title: 'Hall-Effect Rotary Encoder'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'halleffectrotaryencoder'
documentation_source_path: 'ref/halleffectrotaryencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Hall-Effect Rotary Encoder

## 端口
```yaml
ports:
- name: Angle
  summary: 旋转角度物理信号
  direction: output
- name: R
  summary: 传感器正探头的旋转速度机械旋转
  direction: output
- name: C
  summary: 传感器负探头的旋转速度机械旋转
  direction: output
- name: yp
  summary: y 轴正霍尔场电气
  direction: output
- name: yn
  summary: y 轴负霍尔场电气
  direction: output
- name: xp
  summary: x 轴正霍尔场电气
  direction: output
- name: xn
  summary: x 轴负霍尔场电气
  direction: output
```

### 输出

### **Angle** — 旋转角度物理信号

解码位置的物理信号输出端口，以磁场在 x-y 平面中的旋转角度表示。

#### 依赖关系

要启用此端口，请将 **Output interface** 参数设置为 `Decoded angular
position`。
### 守恒

### **R** — 传感器正探头的旋转速度机械旋转

与传感器正探头关联的机械旋转守恒端口。

### **C** — 传感器负探头的旋转速度机械旋转

与传感器负（参考）探头关联的机械旋转守恒端口。

### **yp** — y 轴正霍尔场电气

与 y 轴正霍尔场关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Output interface** 参数设置为
`Electrical connections`。

### **yn** — y 轴负霍尔场电气

与 y 轴负霍尔场关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Output interface**
参数设置为 `Electrical
connections`。

### **xp** — x 轴正霍尔场电气

与 x 轴正霍尔场关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Output interface**
参数设置为 `Electrical
connections`。

### **xn** — x 轴负霍尔场电气

与 x 轴负霍尔场关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Output interface**
参数设置为 `Electrical
connections`。
## 参数
```yaml
parameters:
- name: X-axis voltage amplitude
  summary: x 轴电压 2.5 V（默认值）
  group: ''
- name: Y-axis voltage amplitude
  summary: y 轴电压 2.5 V（默认值）
  group: ''
- name: X-axis voltage offset
  summary: x 轴电压偏移 0 V（默认值）
  group: ''
- name: Y-axis voltage offset
  summary: Y 轴电压偏移 0 V（默认值）
  group: ''
- name: Quadrature error
  summary: 正交误差 0 deg（默认值）
  group: ''
- name: Output interface
  summary: 解码信息的接口 Electrical connections（默认值）| Decoded angular position
  group: ''
```

### **X-axis voltage amplitude** — x 轴电压 `2.5` `V`（默认值）

x 轴电压幅值，以伏特为单位。

### **Y-axis voltage amplitude** — y 轴电压 `2.5` `V`（默认值）

y 轴电压幅值，以伏特为单位。

### **X-axis voltage offset** — x 轴电压偏移 `0` `V`（默认值）

在 x 轴上无外部磁场时，电流通过电导体的电势差，以伏特为单位。

### **Y-axis voltage offset** — Y 轴电压偏移 `0` `V`（默认值）

在 y 轴上无外部磁场时，电流通过电导体的电势差，以伏特为单位。

### **Quadrature error** — 正交误差 `0` `deg`（默认值）

正交误差量。正交切换可以减小偏移误差。

### **Output interface** — 解码信息的接口 `Electrical connections`（默认值）| `Decoded angular position`

解码信息的端口接口。

将此参数设置为 `Electrical connections` 以在每个传感器处输出霍尔电压。选择此选项会启用 **yp**、**yn**、**xp** 和 **xn** 守恒端口。

将此参数设置为 `Decoded angular position` 以输出磁场在 x-y 平面中的旋转角度。选择此选项会启用 **Angle** 物理信号端口。
## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

四元件霍尔效应旋转编码器

Hall-Effect Rotary Encoder 模块使用磁化旋转磁体下方的四个等间距霍尔元件来建模 360° 旋转位置传感器。这些元件生成四个正弦波形。

下图显示了编码器的示意图。霍尔元件
*y*p、
*y*n、
*x*p 和
*x*n 保持固定位置，而磁体的北极和南极以角度 *θ* 旋转。

### 方程

这些方程描述了旋转编码器各元件之间的电压：

vx=Vx0+Axcos(θ)

vy=Vy0+Aycos(θ−π2+β),

其中：

- *vx* 是元件 *xp* 和
  *xn* 之间的电压；
- *vy* 是元件 *yp* 和
  *yn* 之间的电压；
- *Ax* 和 *Ay* 是 *x* 轴和 *y* 轴的电压幅值，反映灵敏度失配；
- *Vx0* 和 *Vy0* 是 *x* 轴和 *y* 轴的电压偏移；
- *β* 是正交误差。

该模块使用此方程解码角度：

θout=arctan(vyvx)。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
