---
type: simulink-block
title: 'RrL Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / ACIM Parameter Estimation'
documentation_page: 'rrlestimator'
documentation_source_path: 'ref/rrlestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# RrL Estimator

## 端口

### 输入

### **Iabc** — 三相电流响应标量

由电流传感器测量的电机三相电流响应。

**注意**

提供 phase-*c* 电流输入是可选的。如果不提供 phase-*c* 电流输入，模块功能不受影响。

**数据类型：** `single`

### **Vdc** — 直流母线电压标量

您提供给逆变器的直流母线电压。

**数据类型：** `single`

### **StartStop** — 用于 *Ld* 估计的逻辑控制信号

用于启动或停止估计过程的信号：

- `1`（脉冲上升沿）— 此信号启动估计过程。
- `0`（脉冲下降沿）— 此信号立即停止估计过程。如果在完成前突然中断估计过程，模块不会计算或输出 *Rr*、*Lm*、*Lls* 和 *Llr* 值。

**数据类型：** `Boolean`

### **Config** — 总线信号输入总线

此表汇总了总线信号输入中的预期配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 用于电机和逆变器硬件的元素 | Number of pole pairs | | | - |
| Rated frequency | | | Hz |
| Nominal motor current | | | A |
| Nominal voltage | | | V |
| Maximum measurable inverter current | | | A |
| Board resistance | | | ohm |
| Current sense gain | | | A/ADC Count |
| Voltage sense gain | | | V/ADC Count |
| 用于估计励磁电流 *Id0* 的元素 | Measurement time | | | seconds |
| Open-loop ramp time | | | seconds |
| 用于估计电机电阻 (*Rs*) 的元素 | Estimation time | | | seconds |
| *Vd* reference voltage 1 | | | PU voltage |
| *Vd* reference voltage 2 | | | PU voltage |
| 用于估计转子电阻 (*Rr*)、励磁电感 (*Lm*)、定子漏电感 (*Lls*) 和转子漏电感 (*Llr*) 的元素 | Frequency 1 as a ratio of rated frequency | | | PU frequency |
| Frequency 2 as a ratio of rated frequency | | | PU frequency |
| High frequency for *Lm* | | | Hz |
| Start voltage for voltage sweep | | | PU voltage |
| Voltage step for voltage sweep | | | PU voltage |
| High-frequency injection voltage | | | PU voltage |
| 用于估计电机惯量 (*J*) 和摩擦常数 (*B*) 的元素 | Closed-loop speed duration | | | seconds |
| Closed-loop speed | | | RPM |
| *Iq* Reference current for FOC | | | PU current |
| Proportional gain | | | - |
| Integral gain | | | - |
| Lower speed limit for inertia estimation | | | RPM |
| - | Parameter estimation sample time | | | seconds |

您可以将此输入端口连接到 ACIM Parameter Estimation Configurator 模块的 `Config` 输出端口。

**数据类型：** `single`

### 输出

### **Vabc** — *a*、*b* 和 *c* 轴定子参考电压分量标量

沿 *abc* 参考坐标系的 *a*、*b* 和 *c* 轴的定子参考电压分量。

**数据类型：** `single`

### **Rr** — 估计的转子电阻标量

感应电机的估计转子电阻（以 Ohms 为单位）。

**数据类型：** `single`

### **Lm** — 估计的励磁电感标量

感应电机的估计励磁电感（以 Henry 为单位）。

**数据类型：** `single`

### **Lls** — 估计的定子漏电感标量

感应电机的估计定子漏电感（以 Henry 为单位）。

**数据类型：** `single`

### **Llr** — 估计的转子漏电感标量

感应电机的估计转子漏电感（以 Henry 为单位）。

**数据类型：** `single`

### **Log** — 调试信号总线

模块提供用于检查的调试信号。该总线包含以下调试信号。

| 调试信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| *Id* | | | *D* 轴电流 | Amperes |
| *InjFreq* | | | 模块当前注入的频率 | Hertz |
| *status* | | `0` | 未完成估计 | - |
| `1` | 估计成功完成 | - |
| *Vd* | | | *D* 轴电压 | Volts |

**数据类型：** `single`

## 参数

未在 R2025b 中记录。

## 所属库

Motor Control Blockset / Parameter Estimation / ACIM Parameter Estimation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

估计交流感应电机 (ACIM) 的转子电阻 (*Rr*)、励磁电感 (*Lm*)、定子漏电感 (*Lls*) 和转子漏电感 (*Llr*)。

RrL Estimator 模块使用相电流、电机两端直流电压以及测试配置元素，计算交流感应电机的转子电阻 (*Rr*)、励磁电感 (*Lm*)、定子漏电感 (*Lls*) 和转子漏电感 (*Llr*)。

为估计这些值，模块在电机各相上注入以下三种信号：

- 第一低频信号（电压变化）
- 第二低频信号（电压变化）
- 高频信号（电压固定）

使用给定的初始电压和步长，模块对第一和第二低频信号执行电压扫描，直到产生的电机相电流等于电机额定电流的 50%。此时，模块测量注入电压（低频信号）与产生的电流响应之间的相位差，以估计 *Rr*、*Lm*、*Lls* 和 *Llr*。
