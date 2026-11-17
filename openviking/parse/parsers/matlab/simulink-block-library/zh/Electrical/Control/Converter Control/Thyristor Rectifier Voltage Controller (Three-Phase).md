---
type: simulink-block
title: 'Thyristor Rectifier Voltage Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Converter Control'
documentation_page: 'thyristorrectifiervoltagecontrollerthreephase'
documentation_source_path: 'ref/thyristorrectifiervoltagecontrollerthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Thyristor Rectifier Voltage Controller (Three-Phase)

## 端口
```yaml
ports:
- name: VdcRef
  summary: 参考直流电压，V 标量
  direction: input
  data_types: single | double
- name: Vdc
  summary: 直流母线电压，V 标量
  direction: input
  data_types: single | double
- name: Reset
  summary: 外部复位标量
  direction: input
  data_types: single | double
- name: Vabc
  summary: 三相电压，V 向量
  direction: input
  data_types: single | double
- name: P
  summary: 脉冲向量
  direction: output
  data_types: single | double
```

### 输入

### **VdcRef** — 参考直流电压，V 标量

期望的直流母线电压。

**数据类型：** `single` | `double`

### **Vdc** — 直流母线电压，V 标量

测量的直流母线电压。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`

### **Vabc** — 三相电压，V 向量

三相电压，指定为包含 *a* 相、*b* 相和 *c* 相电压的向量。

**数据类型：** `single` | `double`
### 输出

### **P** — 脉冲向量

脉冲控制信号。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Loop filter proportional gain
  summary: 环路滤波器 *Kp* 2（默认）| 正标量
  group: ''
- name: Loop filter integral gain
  summary: 环路滤波器 *Ki* 20（默认）| 正标量
  group: ''
- name: Proportional gain
  summary: 控制器 *Kp* 1（默认）| 正标量
  group: ''
- name: Integral gain
  summary: 控制器 *Ki* 1（默认）| 正标量
  group: ''
- name: Thyristor pulse width (rad)
  summary: 脉冲宽度 5*pi/6（默认）| 正标量
  group: ''
- name: Pulse ordering
  summary: 脉冲排序规则 Sequential device order（默认）| Natural order of commutation
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 正标量
  group: ''
- name: Time constant voltage filter
  summary: 直流电压滤波器 *τ* 0.001（默认）| 正标量
  group: ''
- name: Filter DC voltage
  summary: 直流电压滤波器选项 on（默认）| off
  group: ''
```

### **Loop filter proportional gain** — 环路滤波器 *Kp* `2`（默认）| 正标量

锁相环（PLL）的环路滤波器比例增益。

### **Loop filter integral gain** — 环路滤波器 *Ki* `20`（默认）| 正标量

锁相环（PLL）的环路滤波器积分增益。

### **Proportional gain** — 控制器 *Kp* `1`（默认）| 正标量

生成参考相电压的 PI 控制器的比例增益。

### **Integral gain** — 控制器 *Ki* `1`（默认）| 正标量

生成参考相电压的 PI 控制器的积分增益。

### **Thyristor pulse width (rad)** — 脉冲宽度 `5*pi/6`（默认）| 正标量

脉冲的角宽度。

### **Pulse ordering** — 脉冲排序规则 `Sequential device order`（默认）| `Natural order of commutation`

生成脉冲的排序模型。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

### **Time constant voltage filter** — 直流电压滤波器 *τ* `0.001`（默认）| 正标量

直流电压滤波器的时间常数。

#### 依赖关系

仅当选中 **Filter DC voltage** 复选框时，**Time constant voltage filter** 参数才可见。

### **Filter DC voltage** — 直流电压滤波器选项 on（默认）| off

当该复选框：

- 选中 — 模块对直流电压信号进行滤波。
- 清除 — 模块不对直流电压信号进行滤波。

#### 依赖关系

仅当选中 **Filter DC voltage** 复选框时，**Time constant voltage filter** 参数才可见。
## 所属库

Simscape / Electrical / Control / Converter Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

用于晶闸管整流器的离散时间直流母线电压 PI 控制

Thyristor Rectifier Voltage Controller (Three-Phase) 模块为晶闸管整流器实现基于离散时间比例积分（PI）的直流母线电压控制器。

### 模型

为调节晶闸管整流器的输出直流母线电压，Thyristor Rectifier Voltage Controller (Three-Phase) 模块使用余弦波交叉法确定触发角。该图显示了控制结构，其中包括三相锁相环（PLL）。
