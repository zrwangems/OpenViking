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

### 输入

### **vRef** — 参考 DC 电压标量

被控对象所需的 DC 输出电压。

**数据类型：** `single` | `double`

### **v** — 测量 DC 电压标量

被控对象的测量 DC 输出电压。

**数据类型：** `single` | `double`

### **FF** — 前馈标量

前馈项。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`

### 输出

### **Control** — 控制信号标量

控制信号，*control*，表示为占空比或电流。

**数据类型：** `single` | `double`

## 参数

### **比例增益** — 比例增益，*Kp* `0.1`（默认）| 正标量

控制器的比例增益 *Kp*。

### **积分增益** — 积分增益，*Ki* `50`（默认）| 正标量

控制器的积分增益 *Ki*。

### **抗饱和增益** — 抗饱和增益，*Kaw* `1`（默认）| 正标量

控制器的抗饱和增益 *Kaw*。

### **控制作用上限** — 控制信号的上限，*controlmax* `1`（默认）| 正标量

**Control** 输出信号的上限。该值必须大于 **控制作用下限** 参数的值。

### **控制作用下限** — 控制信号的下限，*controlmin* `0`（默认）| 非负标量

**Control** 输出信号的下限。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块生成输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

### **电压滤波器时间常数** — DC 电压滤波器时间常数，*τ* `0.001`（默认）| 正标量

DC 电压滤波器的时间常数 *τ*。

#### 依赖项

仅当选中 **滤波 DC 电压** 复选框时，**电压滤波器时间常数** 参数才可见。

### **滤波 DC 电压** — DC 电压滤波选项 on（默认）| off

要在电压测量路径上启用滤波器，请选中该复选框。要禁用滤波器，请清除该复选框。

#### 依赖项

仅当选中 **滤波 DC 电压** 复选框时，**电压滤波器时间常数** 参数才可见。

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

DC-DC Voltage Controller 模块实现带前馈 *FF* 的离散时间比例积分 (PI) DC-DC 电压控制。前馈输入优化瞬态响应。该模块可输出占空比或电流控制信号。为避免积分增益饱和，该模块可实现抗饱和增益。

### 方程

DC-DC Voltage Controller 模块用于计算控制信号的方程为

control=(Kp+KiTszz−1)(vref−v)+FF,

其中：

- *control* 是控制信号，表示为占空比或电流。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Ts* 是采样时间。
- *vref* 是参考电压。
- *v* 是测量电压。
- *FF* 是前馈输入。

为避免积分器输出饱和，该模块使用抗饱和机制。积分器增益随后等于

Ki+Kaw(controlsat−controlunsat),

其中：

- *Kaw* 是抗饱和增益。
- *controlsat* 是饱和控制信号，模块将其计算为 controlsat=min(max(controlunsat,controlmin),controlmax),

  其中：

  - *controlunsat* 是未饱和控制信号。
  - *controlmin* 是控制信号的下限。
  - *controlmax* 是控制信号的上限。
