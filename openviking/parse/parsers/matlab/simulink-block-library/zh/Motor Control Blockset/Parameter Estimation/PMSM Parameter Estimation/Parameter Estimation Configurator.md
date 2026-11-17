---
type: simulink-block
title: 'PMSM Parameter Estimation Configurator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / PMSM Parameter Estimation'
documentation_page: 'pmsmparameterestimationconfigurator'
documentation_source_path: 'ref/pmsmparameterestimationconfigurator.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Parameter Estimation Configurator

## 端口
```yaml
ports:
- name: Config
  summary: 总线信号总线
  direction: output
  data_types: single
```

### 输出

### **Config** — 总线信号总线

该总线信号包含以下配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 电机和逆变器硬件元素 | 极对数 | | | - |
| 电机额定转速 | | | RPM |
| 电机额定电流 | | | A |
| 最大可测量逆变器电流 | | | A |
| 板电阻 | | | ohms |
| 电流检测增益 | | | A/ADC Count |
| 电压检测增益 | | | V/ADC Count |
| 参数估计采样时间 | | | seconds |
| 用于估计电机电感（*Ld* 和 *Lq*）的元素 | 最大频率 | | | Hz |
| 最小频率 | | | Hz |
| 频率扫描步长 | | | Hz |
| 估计的频率步长 | | | Hz |
| 用于估计的频率数量 | | | - |
| 用于估计反电动势常数（*Ke*）、电机惯量（*J*）和摩擦常数（*B*）的元素 | 反电动势估计时间 | | | seconds |
| 反电动势估计最大转速限制 | | | RPM |
| 指定电流控制器增益（off/on） | | | - |
| 比例增益 | | | - |
| 积分增益 | | | - |
| *Iq* 参考电流与电机额定电流之比 | | | PU current |
| 惯量估计的下限转速 | | | RPM |

配置元素与模块参数类似。有关这些元素的详细信息，请参阅。

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Number of pole pairs
  summary: 电机极对数 4（默认）| scalar
  group: ''
- name: Rated speed (RPM)
  summary: 电机额定转速 4000（默认）| scalar
  group: ''
- name: Rated motor current (A)
  summary: 电机额定电流 7（默认）| scalar
  group: ''
- name: Maximum inverter current (A)
  summary: 最大可测量电流 21（默认）| scalar
  group: ''
- name: Board resistance (ohm)
  summary: 逆变器桥电阻 0.0043（默认）| scalar
  group: ''
- name: Current sense gain (A/ADC Count)
  summary: 每个 ADC 计数的电流 0.0105（默认）| scalar
  group: ''
- name: Voltage sense gain (V/ADC Count)
  summary: 每个 ADC 计数的电压 0.0098（默认）| scalar
  group: ''
- name: Maximum frequency (Hz)
  summary: 频率扫描注入的最大频率 1000（默认）| scalar
  group: ''
- name: Minimum frequency (Hz)
  summary: 频率扫描注入的最小频率 400（默认）| scalar
  group: ''
- name: Step for frequency sweep (Hz)
  summary: 频率扫描的步长 100（默认）| scalar
  group: ''
- name: Frequency step size for estimation (Hz)
  summary: '*Ld* 和 *Lq* 估计的频率步长 10（默认）| scalar'
  group: ''
- name: Number of frequencies for estimation
  summary: 用于 *Ld* 和 *Lq* 估计的注入频率数量 10（默认）| scalar
  group: ''
- name: Current measurement delay (s)
  summary: 电流测量延迟 2 * 50e-6（默认）| scalar
  group: ''
- name: Back EMF estimation time (s)
  summary: 估计反电动势时的电机运行持续时间 5（默认）| scalar
  group: ''
- name: Back EMF estimation maximum speed limit (RPM)
  summary: 估计反电动势时的电机转速 3500（默认）| scalar
  group: ''
- name: Iq reference current as a ratio of rated motor current
  summary: 估计 *Ke*、*J* 和 *B* 时用于 FOC 的参考电流 0.2（默认）| scalar
  group: ''
- name: Specify current controller gains
  summary: 指定 PI 电流控制器增益 off（默认）| on
  group: ''
- name: Proportional gain
  summary: PI 控制器的比例增益 1（默认）| scalar
  group: ''
- name: Integral gain
  summary: PI 控制器的积分增益 1000（默认）| scalar
  group: ''
- name: Speed lower limit for inertia estimation (RPM)
  summary: 惯性估计期间的下限转速 1000（默认）| scalar
  group: ''
- name: 参数估计采样时间 (s)
  summary: 参数估计的采样时间 50e-6（默认）| scalar
  group: ''
```

#### 电机和逆变器

### **Number of pole pairs** — 电机极对数 `4`（默认）| `scalar`

PMSM 中可用的极对数。

### **Rated speed (RPM)** — 电机额定转速 `4000`（默认）| `scalar`

PMSM 的额定转速（以 RPM 为单位）。

### **Rated motor current (A)** — 电机额定电流 `7`（默认）| `scalar`

PMSM 的额定电流（以安培为单位）。

### **Maximum inverter current (A)** — 最大可测量电流 `21`（默认）| `scalar`

系统（包括逆变器和控制器）可以测量的最大电流（以安培为单位）。

### **Board resistance (ohm)** — 逆变器桥电阻 `0.0043`（默认）| `scalar`

相电流路径中的电阻（以欧姆为单位）（不包括电机电阻）。您可以从逆变器硬件的数据表中获取此值。

### **Current sense gain (A/ADC Count)** — 每个 ADC 计数的电流 `0.0105`（默认）| `scalar`

逆变器电流检测电路的增益。此值确定一个模数转换器（ADC）计数对应的电流（以安培为单位）（可测量电流范围的分辨率）。

### **Voltage sense gain (V/ADC Count)** — 每个 ADC 计数的电压 `0.0098`（默认）| `scalar`

逆变器电压检测电路的增益。此值确定一个模数转换器（ADC）计数对应的电压（以伏特为单位）（可测量电压范围的分辨率）。

#### Ld 和 Lq 估计

### **Maximum frequency (Hz)** — 频率扫描注入的最大频率 `1000`（默认）| `scalar`

Ld Estimator 和 Lq Estimator 模块注入以开始频率扫描的最大频率（以赫兹为单位）。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **Minimum frequency (Hz)** — 频率扫描注入的最小频率 `400`（默认）| `scalar`

Ld Estimator 和 Lq Estimator 模块注入以结束频率扫描的最小频率（以赫兹为单位）。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **Step for frequency sweep (Hz)** — 频率扫描的步长 `100`（默认）| `scalar`

Ld Estimator 和 Lq Estimator 模块在频率扫描期间递减频率所使用的步长（以赫兹为单位）。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **Frequency step size for estimation (Hz)** — *Ld* 和 *Lq* 估计的频率步长 `10`（默认）| `scalar`

Ld Estimator 和 Lq Estimator 模块在 *Ld* 和 *Lq* 估计过程中用于递增频率的步长（以赫兹为单位）。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **Number of frequencies for estimation** — 用于 *Ld* 和 *Lq* 估计的注入频率数量 `10`（默认）| `scalar`

Ld Estimator 和 Lq Estimator 模块在频率扫描之后注入的频率数量（步长由 **Frequency step size for estimation (Hz)** 参数定义），用于估计 *Ld* 和 *Lq* 参数。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **Current measurement delay (s)** — 电流测量延迟 `2 * 50e-6`（默认）| `scalar`

电流变化实例与微控制器中测量变化后电流的时间点之间的时间延迟（以秒为单位）。

#### Ke、J、B 估计

### **Back EMF estimation time (s)** — 估计反电动势时的电机运行持续时间 `5`（默认）| `scalar`

PMSM Mechanical Parameter Estimator 模块使用闭环控制运行电机以估计反电动势 *Ke* 的持续时间（以秒为单位）。有关更多详细信息，请参阅 PMSM Mechanical Parameter Estimator。

### **Back EMF estimation maximum speed limit (RPM)** — 估计反电动势时的电机转速 `3500`（默认）| `scalar`

PMSM Mechanical Parameter Estimator 模块使用闭环控制运行电机以估计反电动势 *Ke* 时的转速（以 RPM 为单位）。有关更多详细信息，请参阅 PMSM Mechanical Parameter Estimator。

### **Iq reference current as a ratio of rated motor current** — 估计 *Ke*、*J* 和 *B* 时用于 FOC 的参考电流 `0.2`（默认）| `scalar`

参考电流 *Iq*（以电机额定电流为单位），用于达到 **Back EMF estimation maximum speed limit (RPM)** 参数中指定的参考转速。有关估计过程的更多信息，请参阅 PMSM Mechanical Parameter Estimator。

### **Specify current controller gains** — 指定 PI 电流控制器增益 `off`（默认）| `on`

选择此参数以启用以下字段：

- **Proportional gain**
- **Integral gain**

您可以使用这些字段输入 PI 电流控制器的比例增益和积分增益，这些控制器实现闭环控制以估计 *Ke*、*J* 和 *B*。

如果清除此参数，模块将自动计算比例增益和积分增益。

有关估计过程的更多信息，请参阅 PMSM Mechanical Parameter Estimator。

### **Proportional gain** — PI 控制器的比例增益 `1`（默认）| `scalar`

PI 电流控制器的比例增益 *kp*，该控制器实现磁场定向控制以在闭环控制中运行电机并估计 *Ke*、*J* 和 *B*。

#### 依赖关系

要启用此参数，请选择 **Specify current controller gains** 参数。

### **Integral gain** — PI 控制器的积分增益 `1000`（默认）| `scalar`

PI 电流控制器的积分增益 *ki*，该控制器实现磁场定向控制以在闭环控制中运行电机并估计 *Ke*、*J* 和 *B*。

#### 依赖关系

要启用此参数，请选择 **Specify current controller gains** 参数。

### **Speed lower limit for inertia estimation (RPM)** — 惯性估计期间的下限转速 `1000`（默认）| `scalar`

PMSM Mechanical Parameter Estimation 模块在降速期间记录用于估计电机惯量的时间戳时的下限转速（以 RPM 为单位）。有关估计过程的更多信息，请参阅 PMSM Mechanical Parameter Estimator。

### **参数估计采样时间 (s)** — 参数估计的采样时间 `50e-6`（默认）| `scalar`

参数估计算法的采样时间（以秒为单位）。此参数定义了以下 PMSM 参数估计模块中的采样时间：

- PMSM Rs Estimator
- Ld Estimator
- Lq Estimator
- PMSM Mechanical Parameter Estimator
## 所属库

Motor Control Blockset / Parameter Estimation / PMSM Parameter Estimation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

生成用于 PMSM 参数估计的配置元素

PMSM Parameter Estimation Configurator 模块生成以下配置元素，用于估计永磁同步电机 (PMSM) 的参数：

- 电机和逆变器硬件元素
- 用于估计电机电阻 (*Rs*) 的元素
- 用于估计电机电感（*Ld* 和 *Lq*）的元素
- 用于估计反电动势常数 (*Ke*)、电机惯量 (*J*) 和摩擦常数 (*B*) 的元素

该模块使用参数设置生成包含配置元素的输出总线。您可以在以下 PMSM 参数估计模块中使用这些配置元素：

- Rs Estimator
- Ld Estimator
- Lq Estimator
- PMSM Mechanical Parameter Estimator
