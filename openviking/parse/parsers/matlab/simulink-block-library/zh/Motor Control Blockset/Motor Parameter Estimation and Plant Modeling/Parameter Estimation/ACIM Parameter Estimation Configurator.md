---
type: simulink-block
title: 'ACIM Parameter Estimation Configurator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Parameter Estimation'
documentation_page: 'acimparameterestimationconfigurator'
documentation_source_path: 'ref/acimparameterestimationconfigurator.html'
language: zh-CN
chinese_source: worker-translation
---

# ACIM Parameter Estimation Configurator

## 端口

### 输出

### **Config** — Bus signal bus

该总线信号包含以下配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 用于电机和逆变器硬件的元素 | Number of pole pairs | | | - |
|  | Rated frequency | | | Hz |
|  | Nominal motor current | | | A |
|  | Nominal voltage | | | V |
|  | Maximum measurable inverter current | | | A |
|  | Board resistance | | | ohm |
|  | Current sense gain | | | A/ADC Count |
|  | Voltage sense gain | | | V/ADC Count |
| 用于估计励磁电流 *Id0* 的元素 | Measurement time | | | seconds |
|  | Open-loop ramp time | | | seconds |
| 用于估计电机电阻 (*Rs*) 的元素 | Estimation time | | | seconds |
|  | *Vd* reference voltage 1 | | | PU voltage |
|  | *Vd* reference voltage 2 | | | PU voltage |
| 用于估计转子电阻 (*Rr*)、励磁电感 (*Lm*)、定子漏感 (*Lls*) 和转子漏感 (*Llr*) 的元素 | Frequency 1 as a ratio of rated frequency | | | PU frequency |
|  | Frequency 2 as a ratio of rated frequency | | | PU frequency |
|  | High frequency for *Lm* | | | Hz |
|  | Start voltage for voltage sweep | | | PU voltage |
|  | Voltage step for voltage sweep | | | PU voltage |
|  | High-frequency injection voltage | | | PU voltage |
| 用于估计电机惯量 (*J*) 和摩擦常数 (*B*) 的元素 | Closed-loop speed duration | | | seconds |
|  | Closed-loop speed | | | RPM |
|  | *Iq* Reference current for FOC | | | PU current |
|  | Proportional gain | | | - |
|  | Integral gain | | | - |
|  | Lower speed limit for inertia estimation | | | RPM |
| - | Parameter estimation sample time | | | seconds |

这些配置元素与模块参数类似。有关这些元素的更多信息，请参阅参数。

**数据类型：** `single`

## 参数

#### 电机和逆变器

### **Number of pole pairs** — Number of motor pole pairs `2` (默认) | `scalar`

感应电机中可用的极对数。

### **Rated frequency (Hz)** — Motor rated frequency `50` (默认) | `scalar`

感应电机的额定频率（单位：Hertz）。

### **Nominal motor current (A)** — Motor nominal current `2` (默认) | `scalar`

感应电机的额定电流（单位：Amperes）。

### **Nominal voltage (V)** — Motor nominal voltage `24` (默认) | `scalar`

感应电机的额定电压（单位：Volts）。

### **Maximum inverter current (A)** — Maximum measurable current `21` (默认) | `scalar`

系统（包括逆变器和控制器）可测量的最大电流（单位：Amperes）。

### **Board resistance (ohm)** — Inverter bridge resistance `0.0043` (默认) | `scalar`

相电流路径中的电阻（不包括电机电阻）。你可以从逆变器硬件的数据手册中获取该值。

### **Current sense gain (A/ADC Count)** — Current per ADC count `0.0105` (默认) | `scalar`

逆变器电流检测电路的增益。该值确定一个模数转换器 (ADC) count 对应的电流（单位：Amperes）（可测量电流范围的分辨率）。

### **Voltage sense gain (V/ADC Count)** — Voltage per ADC count `0.0098` (默认) | `scalar`

逆变器电压检测电路的增益。该值确定一个模数转换器 (ADC) count 对应的电压（单位：Volts）（可测量电压范围的分辨率）。

#### Id0 估计

### **Measurement time (sec)** — Time used to measure and average-out current `5` (默认) | `scalar`

用于测量并平均化消除感应电机开环运行时电流响应中峰值的时间。有关 *Id0* 估计的更多详细信息，请参阅 Id0 Estimator。

### **Open loop ramp time (sec)** — Time allotted to ramp up frequency `3` (默认) | `scalar`

你希望分配给电机运行频率斜坡上升并达到电机额定频率 90% 的时间。有关 *Id0* 估计的更多详细信息，请参阅 Id0 Estimator。

#### Rs 估计

### **Estimation time (sec)** — Time to run *Rs* estimation algorithm `2` (默认) | `scalar`

你希望分配给运行电机电阻 (*Rs*) 估计算法的时间。该值定义 ACIM Rs Estimator 模块注入每个电压以测量电机电阻的时间长度。有关 *Rs* 估计的更多详细信息，请参阅 ACIM Rs Estimator。

### **Vd reference voltage 1 (PU)** — First reference voltage for *Rs* estimation `0.1` (默认) | `scalar`

ACIM Rs Estimator 模块用于测量电机电阻 (*Rs*) 的第一个参考电机相电压（单位：per-unit）。默认情况下，该模块将此字段设置为逆变器 DC 电压的 10%。有关 *Rs* 估计的更多详细信息，请参阅 ACIM Rs Estimator。有关 per-unit 系统的更多详细信息，请参阅 Per-Unit System。

### **Vd reference voltage 2 (PU)** — Second reference voltage for *Rs* estimation `0.2` (默认) | `scalar`

ACIM Rs Estimator 模块用于测量电机电阻 (*Rs*) 的第二个参考电机相电压（单位：per-unit）。默认情况下，该模块将此字段设置为逆变器 DC 电压的 20%。有关 *Rs* 估计的更多详细信息，请参阅 ACIM Rs Estimator。有关 per-unit 系统的更多详细信息，请参阅 Per-Unit System。

#### Rr、Lm、Lls、Llr 估计

### **Frequency 1 as a ratio of rated frequency (PU)** — Ratio of first injected low frequency over rated frequency `0.1` (默认) | `scalar`

第一个注入低频与感应电机额定频率之比（单位：per-unit）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关 per-unit 系统的更多详细信息，请参阅 Per-Unit System。

### **Frequency 2 as a ratio of rated frequency (PU)** — Ratio of second injected low frequency over rated frequency `0.2` (默认) | `scalar`

第二个注入低频与感应电机额定频率之比（单位：per-unit）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关 per-unit 系统的更多详细信息，请参阅 Per-Unit System。

### **High Frequency for Lm (Hz)** — Frequency of third injected signal `200` (默认) | `scalar`

该模块为机械参数估计注入的第三个（高频）信号的频率（单位：Hertz）。有关估计过程的更多详细信息，请参阅 RrL Estimator。

### **Voltage sweep start value voltage (PU)** — Initial voltage at which voltage sweep begins `0.1` (默认) | `scalar`

电压扫描开始时的初始电压（模块注入的第一个和第二个低频信号的电压，单位：per-unit）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关 per-unit 系统的更多详细信息，请参阅 Per-Unit System。

### **Voltage sweep step value voltage (PU)** — Step size for voltage sweep `0.0125` (默认) | `scalar`

该模块用于对两个注入的低频信号执行电压扫描的步长（单位：per-unit）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关 per-unit 系统的更多详细信息，请参阅 Per-Unit System。

### **High frequency injection voltage (PU)** — Voltage of third injected signal `0.1` (默认) | `scalar`

该模块为机械参数估计注入的第三个（高频）信号的电压（单位：per-unit）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关 per-unit 系统的更多详细信息，请参阅 Per-Unit System。

### **Current measurement delay (s)** — Delay in current measurement `2 * 50e-6` (默认) | `scalar`

电流发生变化的时刻与微控制器中测量变化后电流的时刻之间的时间延迟。

#### J、B 估计

### **Closed loop duration (sec)** — Closed-loop motor run duration `5` (默认) | `scalar`

ACIM Mechanical Parameter Estimator 模块在启动自由滑行之前使用闭环控制运行电机的持续时间（单位：seconds）。有关估计过程的更多信息，请参阅 ACIM Mechanical Parameter Estimator。

### **Closed loop speed (RPM)** — Closed-loop motor speed `950` (默认) | `scalar`

ACIM Mechanical Parameter Estimator 模块使用闭环控制运行电机的速度（单位：RPM）。有关估计过程的更多信息，请参阅 ACIM Mechanical Parameter Estimator。

### **Iq reference current for FOC (PU)** — Reference current for FOC when estimating *J* and *B* `0.2` (默认) | `scalar`

参考电流 *Iq*（以电机额定电流为单位），用于达到 **Closed loop speed (RPM)** 参数中指定的参考速度。有关估计过程的更多信息，请参阅 ACIM Mechanical Parameter Estimator。

### **Specify current controller gains** — Specify PI current controller gains `off` (默认) | `on`

选择此参数以启用以下字段：

- **Proportional gain**
- **Integral gain**

你可以使用这些字段输入实现闭环控制以估计 *J* 和 *B* 的 PI 电流控制器的比例和积分增益。

如果清除此参数，该模块会自动计算比例和积分增益。

要了解有关估计过程的更多信息，请参阅 ACIM Mechanical Parameter Estimator。

### **Proportional gain** — Proportional gain of PI controller `1` (默认) | `scalar`

PI 电流控制器的比例增益 *kp*，该控制器实现磁场定向控制，以闭环控制运行电机并估计 *J* 和 *B*。

#### 依赖关系

要启用此参数，请选择 **Specify current controller gains** 参数。

### **Integral gain** — Integral gain of PI controller `1000` (默认) | `scalar`

PI 电流控制器的积分增益 *ki*，该控制器实现磁场定向控制，以闭环控制运行电机并估计 *J* 和 *B*。

#### 依赖关系

要启用此参数，请选择 **Specify current controller gains** 参数。

### **Speed lower limit for inertia estimation (RPM)** — Lower speed limit during coast-down `100` (默认) | `scalar`

自由滑行期间的速度下限，ACIM Mechanical Parameter Estimation 模块在该速度下记录用于估计电机惯量的时间戳。有关估计过程的更多详细信息，请参阅 ACIM Mechanical Parameter Estimation。

### **Parameter estimation sample time (sec)** — Sample time for parameter estimation `50e-6` (默认) | `scalar`

参数估计算法的采样时间。此参数定义以下用于交流感应电机的参数估计模块的采样时间：

- Id0 Estimator
- ACIM Rs Estimator
- Rr L Estimator
- ACIM Mechanical Parameter Estimator

## 所属库

Motor Control Blockset / Parameter Estimation / ACIM Parameter Estimation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

生成用于交流感应电机 (ACIM) 参数估计的配置元素。

ACIM Parameter Estimation Configurator 模块生成以下用于估计交流感应电机参数的配置元素：

- 用于电机和逆变器硬件的元素
- 用于估计励磁电流 *Id0* 的元素
- 用于估计电机电阻 (*Rs*) 的元素
- 用于估计以下项的元素：

  - 转子电阻，*Rr*
  - 励磁电感，*Lm*
  - 定子漏感，*Lls*
  - 转子漏感，*Llr*
- 用于估计电机惯量 (*J*) 和摩擦常数 (*B*) 的元素

该模块使用参数设置生成包含配置元素的输出总线。你可以在以下 ACIM 参数估计模块中使用这些配置元素：

- Id0 Estimator
- ACIM Rs Estimator
- RrL Estimator
- ACIM Mechanical Parameter Estimator
