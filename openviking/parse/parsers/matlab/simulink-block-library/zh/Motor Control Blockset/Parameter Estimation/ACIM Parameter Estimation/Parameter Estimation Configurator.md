---
type: simulink-block
title: 'ACIM Parameter Estimation Configurator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / ACIM Parameter Estimation'
documentation_page: 'acimparameterestimationconfigurator'
documentation_source_path: 'ref/acimparameterestimationconfigurator.html'
language: zh-CN
chinese_source: worker-translation
---

# ACIM Parameter Estimation Configurator

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

总线信号包含以下配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 电机和逆变器硬件元素 | 极对数 | | | - |
| 额定频率 | | | Hz |
| 电机标称电流 | | | A |
| 标称电压 | | | V |
| 最大可测量逆变器电流 | | | A |
| 板电阻 | | | ohm |
| 电流检测增益 | | | A/ADC Count |
| 电压检测增益 | | | V/ADC Count |
| 用于估计励磁电流 *Id0* 的元素 | 测量时间 | | | seconds |
| 开环斜坡时间 | | | seconds |
| 用于估计电机电阻（*Rs*）的元素 | 估计时间 | | | seconds |
| *Vd* 参考电压 1 | | | PU voltage |
| *Vd* 参考电压 2 | | | PU voltage |
| 用于估计转子电阻（*Rr*）、励磁电感（*Lm*）、定子漏电感（*Lls*）和转子漏电感（*Llr*）的元素 | 频率 1（作为额定频率的比例） | | | PU frequency |
| 频率 2（作为额定频率的比例） | | | PU frequency |
| 用于 *Lm* 的高频 | | | Hz |
| 电压扫描的起始电压 | | | PU voltage |
| 电压扫描的电压步长 | | | PU voltage |
| 高频注入电压 | | | PU voltage |
| 用于估计电机惯量（*J*）和摩擦常数（*B*）的元素 | 闭环速度持续时间 | | | seconds |
| 闭环速度 | | | RPM |
| 用于 FOC 的 *Iq* 参考电流 | | | PU current |
| 比例增益 | | | - |
| 积分增益 | | | - |
| 惯量估计的速度下限 | | | RPM |
| - | 参数估计采样时间 | | | seconds |

配置元素与模块参数类似。有关这些元素的详细信息，请参阅参数。

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Number of pole pairs
  summary: 电机极对数 2（默认）| scalar
  group: ''
- name: Rated frequency (Hz)
  summary: 电机额定频率 50（默认）| scalar
  group: ''
- name: Nominal motor current (A)
  summary: 电机标称电流 2（默认）| scalar
  group: ''
- name: Nominal voltage (V)
  summary: 电机标称电压 24（默认）| scalar
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
- name: Measurement time (sec)
  summary: 用于测量和平均电流的时间 5（默认）| scalar
  group: ''
- name: Open loop ramp time (sec)
  summary: 分配给频率斜坡上升的时间 3（默认）| scalar
  group: ''
- name: Estimation time (sec)
  summary: 运行 *Rs* 估计算法的时间 2（默认）| scalar
  group: ''
- name: Vd reference voltage 1 (PU)
  summary: 用于 *Rs* 估计的第一个参考电压 0.1（默认）| scalar
  group: ''
- name: Vd reference voltage 2 (PU)
  summary: 用于 *Rs* 估计的第二个参考电压 0.2（默认）| scalar
  group: ''
- name: Frequency 1 as a ratio of rated frequency (PU)
  summary: 第一个注入低频与额定频率的比值 0.1（默认）| scalar
  group: ''
- name: Frequency 2 as a ratio of rated frequency (PU)
  summary: 第二个注入低频与额定频率的比值 0.2（默认）| scalar
  group: ''
- name: High Frequency for Lm (Hz)
  summary: 第三个注入信号的频率 200（默认）| scalar
  group: ''
- name: Voltage sweep start value voltage (PU)
  summary: 电压扫描开始时的初始电压 0.1（默认）| scalar
  group: ''
- name: Voltage sweep step value voltage (PU)
  summary: 电压扫描的步长 0.0125（默认）| scalar
  group: ''
- name: High frequency injection voltage (PU)
  summary: 第三个注入信号的电压 0.1（默认）| scalar
  group: ''
- name: Current measurement delay (s)
  summary: 电流测量中的延迟 2 * 50e-6（默认）| scalar
  group: ''
- name: 闭环持续时间 (sec)
  summary: 闭环电机运行持续时间 5（默认）| scalar
  group: ''
- name: 闭环速度 (RPM)
  summary: 闭环电机速度 950（默认）| scalar
  group: ''
- name: 用于 FOC 的 Iq 参考电流 (PU)
  summary: 估算 *J* 和 *B* 时用于 FOC 的参考电流 0.2（默认）| scalar
  group: ''
- name: 指定电流控制器增益
  summary: 指定 PI 电流控制器增益 off（默认）| on
  group: ''
- name: 比例增益
  summary: PI 控制器的比例增益 1（默认）| scalar
  group: ''
- name: 积分增益
  summary: PI 控制器的积分增益 1000（默认）| scalar
  group: ''
- name: 惯性估算的速度下限 (RPM)
  summary: 惯性滑行期间的速度下限 100（默认）| scalar
  group: ''
- name: 参数估算采样时间 (sec)
  summary: 参数估算的采样时间 50e-6（默认）| scalar
  group: ''
```

#### 电机和逆变器

### **Number of pole pairs** — 电机极对数 `2`（默认）| `scalar`

感应电机中可用的极对数。

### **Rated frequency (Hz)** — 电机额定频率 `50`（默认）| `scalar`

感应电机的额定频率（以赫兹为单位）。

### **Nominal motor current (A)** — 电机标称电流 `2`（默认）| `scalar`

感应电机的额定电流（以安培为单位）。

### **Nominal voltage (V)** — 电机标称电压 `24`（默认）| `scalar`

感应电机的额定电压（以伏特为单位）。

### **Maximum inverter current (A)** — 最大可测量电流 `21`（默认）| `scalar`

系统（包括逆变器和控制器）可以测量的最大电流（以安培为单位）。

### **Board resistance (ohm)** — 逆变器桥电阻 `0.0043`（默认）| `scalar`

相电流路径中的电阻（不包括电机电阻）。您可以从逆变器硬件的数据手册中获取此值。

### **Current sense gain (A/ADC Count)** — 每个 ADC 计数的电流 `0.0105`（默认）| `scalar`

逆变器电流检测电路的增益。此值确定一个模数转换器（ADC）计数对应的电流（以安培为单位）（可测量电流范围的分辨率）。

### **Voltage sense gain (V/ADC Count)** — 每个 ADC 计数的电压 `0.0098`（默认）| `scalar`

逆变器电压检测电路的增益。此值确定一个模数转换器（ADC）计数对应的电压（以伏特为单位）（可测量电压范围的分辨率）。

#### Id0 估计

### **Measurement time (sec)** — 用于测量和平均电流的时间 `5`（默认）| `scalar`

用于测量和平均感应电机开环运行电流响应中峰值的时间。有关 *Id0* 估计的更多详细信息，请参阅 Id0 Estimator。

### **Open loop ramp time (sec)** — 分配给频率斜坡上升的时间 `3`（默认）| `scalar`

你希望分配给电机运行频率斜坡上升并达到电机额定频率 90% 的时间。有关 *Id0* 估计的更多详细信息，请参阅 Id0 Estimator。

#### Rs Estimation

### **Estimation time (sec)** — 运行 *Rs* 估计算法的时间 `2`（默认）| `scalar`

你希望分配给运行电机电阻（*Rs*）估计算法的时间。该值定义了 ACIM Rs Estimator 模块注入每个电压以测量电机电阻的时间持续时间。有关 *Rs* 估计的更多详细信息，请参阅 ACIM Rs Estimator。

### **Vd reference voltage 1 (PU)** — 用于 *Rs* 估计的第一个参考电压 `0.1`（默认）| `scalar`

ACIM Rs Estimator 模块用于测量电机电阻（*Rs*）的第一个参考电机相电压（以标幺值表示）。默认情况下，该模块将此字段设置为逆变器直流电压的 10%。有关 *Rs* 估计的更多详细信息，请参阅 ACIM Rs Estimator。有关标幺值系统的更多详细信息，请参阅 Per-Unit System。

### **Vd reference voltage 2 (PU)** — 用于 *Rs* 估计的第二个参考电压 `0.2`（默认）| `scalar`

ACIM Rs Estimator 模块用于测量电机电阻（*Rs*）的第二个参考电机相电压（以标幺值表示）。默认情况下，该模块将此字段设置为逆变器直流电压的 20%。有关 *Rs* 估计的更多详细信息，请参阅 ACIM Rs Estimator。有关标幺值系统的更多详细信息，请参阅 Per-Unit System。

#### Rr, Lm, Lls, Llr Estimation

### **Frequency 1 as a ratio of rated frequency (PU)** — 第一个注入低频与额定频率的比值 `0.1`（默认）| `scalar`

第一个注入低频与感应电机额定频率的比值（以标幺值表示）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关标幺值系统的更多详细信息，请参阅 Per-Unit System。

### **Frequency 2 as a ratio of rated frequency (PU)** — 第二个注入低频与额定频率的比值 `0.2`（默认）| `scalar`

第二个注入低频与感应电机额定频率的比值（以标幺值表示）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关标幺值系统的更多详细信息，请参阅 Per-Unit System。

### **High Frequency for Lm (Hz)** — 第三个注入信号的频率 `200`（默认）| `scalar`

该模块为机械参数估计注入的第三个（高频）信号的频率（以赫兹为单位）。有关估计过程的更多详细信息，请参阅 RrL Estimator。

### **Voltage sweep start value voltage (PU)** — 电压扫描开始时的初始电压 `0.1`（默认）| `scalar`

电压扫描开始时的初始电压（该模块注入的第一个和第二个低频信号的电压，以标幺值表示）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关标幺值系统的更多详细信息，请参阅 Per-Unit System。

### **Voltage sweep step value voltage (PU)** — 电压扫描的步长 `0.0125`（默认）| `scalar`

该模块用于对两个注入低频信号执行电压扫描的步长（以标幺值表示）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关标幺值系统的更多详细信息，请参阅 Per-Unit System。

### **High frequency injection voltage (PU)** — 第三个注入信号的电压 `0.1`（默认）| `scalar`

该模块为机械参数估计注入的第三个（高频）信号的电压（以标幺值表示）。有关估计过程的更多详细信息，请参阅 RrL Estimator。有关标幺值系统的更多详细信息，请参阅 Per-Unit System。

### **Current measurement delay (s)** — 电流测量中的延迟 `2 * 50e-6`（默认）| `scalar`

电流变化发生时刻与微控制器中测量到变化后电流的时间点之间的时间延迟。

#### J, B 估算

### **闭环持续时间 (sec)** — 闭环电机运行持续时间 `5`（默认）| `scalar`

ACIM 机械参数估算器模块在启动惯性滑行之前，使用闭环控制运行电机的持续时间（以秒为单位）。有关估算过程的更多信息，请参阅 ACIM 机械参数估算器。

### **闭环速度 (RPM)** — 闭环电机速度 `950`（默认）| `scalar`

ACIM 机械参数估算器模块使用闭环控制运行电机时的速度（以 RPM 为单位）。有关估算过程的更多信息，请参阅 ACIM 机械参数估算器。

### **用于 FOC 的 Iq 参考电流 (PU)** — 估算 *J* 和 *B* 时用于 FOC 的参考电流 `0.2`（默认）| `scalar`

参考电流 *Iq*（以电机额定电流为单位），用于达到 **闭环速度 (RPM)** 参数中指定的参考速度。有关估算过程的更多信息，请参阅 ACIM 机械参数估算器。

### **指定电流控制器增益** — 指定 PI 电流控制器增益 `off`（默认）| `on`

选择此参数以启用以下字段：

- **比例增益**
- **积分增益**

您可以使用这些字段输入 PI 电流控制器的比例增益和积分增益，这些控制器实现闭环控制以估算 *J* 和 *B*。

如果清除此参数，模块将自动计算比例增益和积分增益。

要了解有关估算过程的更多信息，请参阅 ACIM 机械参数估算器。

### **比例增益** — PI 控制器的比例增益 `1`（默认）| `scalar`

PI 电流控制器的比例增益 *kp*，该控制器实现磁场定向控制以在闭环控制中运行电机并估算 *J* 和 *B*。

#### 依赖关系

要启用此参数，请选择 **指定电流控制器增益** 参数。

### **积分增益** — PI 控制器的积分增益 `1000`（默认）| `scalar`

PI 电流控制器的积分增益 *ki*，该控制器实现磁场定向控制以在闭环控制中运行电机并估算 *J* 和 *B*。

#### 依赖关系

要启用此参数，请选择 **指定电流控制器增益** 参数。

### **惯性估算的速度下限 (RPM)** — 惯性滑行期间的速度下限 `100`（默认）| `scalar`

ACIM 机械参数估算模块在惯性滑行期间记录时间戳以估算电机惯量的速度下限。有关估算过程的更多详细信息，请参阅 ACIM 机械参数估算。

### **参数估算采样时间 (sec)** — 参数估算的采样时间 `50e-6`（默认）| `scalar`

参数估算算法的采样时间。此参数定义了以下交流感应电机参数估算模块的采样时间：

- Id0 Estimator
- ACIM Rs Estimator
- Rr L Estimator
- ACIM Mechanical Parameter Estimator
## 所属库

Motor Control Blockset / Parameter Estimation / ACIM Parameter Estimation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

为交流感应电机（ACIM）参数估计生成配置元素

ACIM Parameter Estimation Configurator 模块为估计交流感应电机的参数生成以下配置元素：

- 电机和逆变器硬件元素
- 用于估计励磁电流 *Id0* 的元素
- 用于估计电机电阻（*Rs*）的元素
- 用于估计以下项的元素：

  - 转子电阻，*Rr*
  - 励磁电感，*Lm*
  - 定子漏电感，*Lls*
  - 转子漏电感，*Llr*
- 用于估计电机惯量（*J*）和摩擦常数（*B*）的元素

该模块使用参数设置生成包含配置元素的输出总线。您可以在以下 ACIM 参数估计模块中使用这些配置元素：

- Id0 Estimator
- ACIM Rs Estimator
- RrL Estimator
- ACIM Mechanical Parameter Estimator
