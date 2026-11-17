---
type: simulink-block
title: 'DC-DC Voltage Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Converter Control'
documentation_page: 'dcdcvoltagecontroller'
documentation_source_path: 'ref/dcdcvoltagecontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# DC-DC Voltage Controller

## 端口
```yaml
ports:
- name: vRef
  summary: 参考直流电压标量
  direction: input
  data_types: single | double
- name: v
  summary: 测量的直流电压标量
  direction: input
  data_types: single | double
- name: FF
  summary: 前馈标量
  direction: input
  data_types: single | double
- name: Reset
  summary: 外部复位标量
  direction: input
  data_types: single | double
- name: Control
  summary: 控制信号标量
  direction: output
  data_types: single | double
```

### 输入

### **vRef** — 参考直流电压标量

被控对象的期望直流输出电压。

**数据类型：** `single` | `double`

### **v** — 测量的直流电压标量

被控对象的测量直流输出电压。

**数据类型：** `single` | `double`

### **FF** — 前馈标量

前馈项。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`
### 输出

### **Control** — 控制信号标量

控制信号 *control*，表示为占空比或电流。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Proportional gain
  summary: 比例增益，*Kp* 0.1（默认）| 正标量
  group: ''
- name: Integral gain
  summary: 积分增益，*Ki* 50（默认）| 正标量
  group: ''
- name: Anti-windup gain
  summary: 抗积分饱和增益，*Kaw* 1（默认）| 正标量
  group: ''
- name: Control action upper limit
  summary: 控制信号上限，*controlmax* 1（默认）| 正标量
  group: ''
- name: Control action lower limit
  summary: 控制信号下限，*controlmin* 0（默认）| 非负标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 正标量
  group: ''
- name: Time constant voltage filter
  summary: 直流电压滤波器时间常数，*τ* 0.001（默认）| 正标量
  group: ''
- name: Filter DC voltage
  summary: 直流电压滤波器选项 开（默认）| 关
  group: ''
```

### **Proportional gain** — 比例增益，*Kp* `0.1`（默认）| 正标量

控制器的比例增益 *Kp*。

### **Integral gain** — 积分增益，*Ki* `50`（默认）| 正标量

控制器的积分增益 *Ki*。

### **Anti-windup gain** — 抗积分饱和增益，*Kaw* `1`（默认）| 正标量

控制器的抗积分饱和增益 *Kaw*。

### **Control action upper limit** — 控制信号上限，*controlmax* `1`（默认）| 正标量

**Control** 输出信号的上限。该值必须大于 **Control action lower limit** 参数的值。

### **Control action lower limit** — 控制信号下限，*controlmin* `0`（默认）| 非负标量

**Control** 输出信号的下限。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

### **Time constant voltage filter** — 直流电压滤波器时间常数，*τ* `0.001`（默认）| 正标量

直流电压滤波器的时间常数 *τ*。

#### 依赖关系

**Time constant voltage filter** 参数仅在选中 **Filter DC voltage** 复选框时可见。

### **Filter DC voltage** — 直流电压滤波器选项 开（默认）| 关

要启用电压测量路径上的滤波器，请选中该复选框。要禁用滤波器，请清除该复选框。

#### 依赖关系

**Time constant voltage filter** 参数仅在选中 **Filter DC voltage** 复选框时可见。
## 所属库

Simscape / Electrical / Control / General Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

带前馈和可选积分抗饱和的离散时间 DC-DC 电压 PI 控制

DC-DC Voltage Controller 模块实现带前馈 *FF* 的离散时间比例积分（PI）DC-DC 电压控制。前馈输入优化瞬态响应。该模块可以输出占空比或电流控制信号。为避免积分增益饱和，该模块可以实现抗积分饱和增益。

### 方程

DC-DC Voltage Controller 模块用于计算控制信号的方程为

control=(Kp+KiTszz−1)(vref−v)+FF，

其中：

- *control* 是控制信号，表示为占空比或电流。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Ts* 是采样时间。
- *vref* 是参考电压。
- *v* 是测量电压。
- *FF* 是前馈输入。

为避免积分器输出饱和，该模块使用抗积分饱和机制。积分器增益则等于

Ki+Kaw(controlsat−controlunsat)，

其中：

- *Kaw* 是抗积分饱和增益。
- *controlsat* 是饱和控制信号，模块将其计算为 controlsat=min(max(controlunsat,controlmin),controlmax)，

  其中：

  - *controlunsat* 是未饱和控制信号。
  - *controlmin* 是控制信号的下限。
  - *controlmax* 是控制信号的上限。
