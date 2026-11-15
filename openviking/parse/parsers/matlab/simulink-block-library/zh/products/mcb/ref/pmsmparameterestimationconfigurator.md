---
type: simulink-block
title: 'PMSM Parameter Estimation Configurator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Parameter Estimation'
documentation_page: 'pmsmparameterestimationconfigurator'
documentation_source_path: 'ref/pmsmparameterestimationconfigurator.html'
language: zh-CN
chinese_source: official
---

# PMSM Parameter Estimation Configurator

## 端口

### 输出

### **Config** — 总线信号 总线

总线信号包括以下配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 电机和逆变器硬件元素 | 极对数 | | | - |
| 电机的额定转速 | | | RPM |
| 电机的额定电流 | | | A |
| 最大可测量逆变器电流 | | | A |
| 板电阻 | | | 欧姆 |
| 电流感测增益 | | | A/ADC 计数 |
| 电压感测增益 | | | V/ADC 计数 |
| 参数估计采样时间 | | | 秒 |
| 用于估计电机电感（*Ld* 和 *Lq*）的元素 | 最大频率 | | | Hz |
| 最小频率 | | | Hz |
| 频率扫描的步长 | | | Hz |
| 用于估计的频率步长 | | | Hz |
| 估计时所用频率数 | | | - |
| 用于估计反电动势常量 (*Ke*)、电机惯量 (*J*) 和摩擦常量 (*B*) 的元素 | 反电动势估计时间 | | | 秒 |
| 反电动势估计最大转速限值 | | | RPM |
| 指定电流控制器增益 (off/on) | | | - |
| 比例增益 | | | - |
| 积分增益 | | | - |
| *Iq* 参考电流(相对于电机额定电流的比率) | | | PU 电流 |
| 惯量估计的转速下限 | | | RPM |

配置元素类似于模块参数。有关这些元素的详细信息，请参阅。

**数据类型:** `single`

## 参数

#### 电机和逆变器

### **极对数** — 电机极对数 `4` (默认) | `scalar`

PMSM 中可用的极对数。

### **额定转速(RPM)** — 电机额定转速 `4000` (默认) | `scalar`

PMSM 的额定转速（以 RPM 为单位）。

### **额定电机电流(A)** — 电机额定电流 `7` (默认) | `scalar`

PMSM 的额定电流（以安培为单位）。

### **最大逆变器电流(A)** — 最大可测量电流 `21` (默认) | `scalar`

系统（包括逆变器和控制器）可以测量的最大电流（以安培为单位）。

### **板电阻(欧姆)** — 逆变器电桥电阻 `0.0043` (默认) | `scalar`

相电流路径中的电阻（不包括电机电阻）（以欧姆为单位）。您可以从逆变器硬件的数据表中获得此值。

### **电流感测增益(A/ADC 计数)** — 每个 ADC 计数的电流 `0.0105` (默认) | `scalar`

逆变器的电流感测电路的增益。此值确定对应于模数转换器 (ADC) 计数（可测量电流范围的分辨率）的电流（以安培为单位）。

### **电压感测增益(V/ADC 计数)** — 每个 ADC 计数的电压 `0.0098` (默认) | `scalar`

逆变器的电压感测电路的增益。此值确定对应于模数转换器 (ADC) 计数（可测量电压范围的分辨率）的电压（以伏特为单位）。

#### Ld 和 Lq 估计

### **最高频率(Hz)** — 频率扫描的最大注入频率 `1000` (默认) | `scalar`

Ld Estimator 和 Lq Estimator 模块为开始频率扫描而注入的最大频率（以赫兹为单位）。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **最低频率(Hz)** — 频率扫描的最小注入频率 `400` (默认) | `scalar`

Ld Estimator 和 Lq Estimator 模块为结束频率扫描而注入的最小频率（以赫兹为单位）。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **频率扫描步长(Hz)** — 频率扫描的步长 `100` (默认) | `scalar`

Ld Estimator 和 Lq Estimator 模块在频率扫描期间递减频率所使用的步长（以赫兹为单位）。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **估计时所用频率步长(Hz)** — *Ld* 和 *Lq* 估计的频率步长 `10` (默认) | `scalar`

Ld Estimator 和 Lq Estimator 模块在 *Ld* 和 *Lq* 估计过程中用于增加频率的步长（单位为赫兹）。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **估计时所用频率数** — 为 *Ld* 和 *Lq* 估计注入的频率数 `10` (默认) | `scalar`

Ld Estimator 和 Lq Estimator 模块在频率扫描后注入以估计 *Ld* 和 *Lq* 参数的频率数（步长由**估计时所用频率步长(Hz)** 参数定义）。有关更多详细信息，请参阅 Ld Estimator 和 Lq Estimator。

### **电流测量延迟(秒)** — 电流测量延迟 `2 * 50e-6` (默认) | `scalar`

从电流变化到微控制器中测得变化电流的时间点之间的时滞（以秒为单位）。

#### Ke、J、B 估计

### **反电动势估计时间(秒)** — 估计反电动势时的电机运行持续时间 `5` (默认) | `scalar`

PMSM Mechanical Parameter Estimator 模块为估计反电动势而使用闭环控制运行电机的持续时间 *Ke*（以秒为单位）。有关更多详细信息，请参阅 PMSM Mechanical Parameter Estimator。

### **反电动势估计最大转速限值(RPM)** — 估计反电动势时的电机转速 `3500` (默认) | `scalar`

PMSM Mechanical Parameter Estimator 模块为估计反电动势 *Ke* 而使用闭环控制运行电机的转速（以 RPM 为单位）。有关更多详细信息，请参阅 PMSM Mechanical Parameter Estimator。

### **Iq 参考电流(相对于电机额定电流的比率)** — 估计 *Ke*、*J* 和 *B* 时 FOC 的基电流 `0.2` (默认) | `scalar`

参考电流 *Iq*（采用电机额定电流的单位），用于达到**反电动势估计最大转速限值(RPM)** 参数中指定的参考转速。有关估计过程的详细信息，请参阅 PMSM Mechanical Parameter Estimator。

### **指定电流控制器增益** — 指定 PI 电流控制器增益 `off` (默认) | `on`

选择此参数可启用以下字段：

- **比例增益**
- **积分增益**

您可以使用这些字段输入实现闭环控制的 PI 电流控制器的比例和积分增益，以估计 *Ke*、*J* 和 *B*。

如果清除此参数，模块会自动计算比例增益和积分增益。

有关估计过程的详细信息，请参阅 PMSM Mechanical Parameter Estimator。

### **比例增益** — PI 控制器的比例增益 `1` (默认) | `scalar`

PI 电流控制器的比例增益 *kp*，用于实现磁场定向控制以便以闭环控制方式运行电机并估计 *Ke*、*J* 和 *B*。

#### 依赖关系

要启用此参数，请选择**指定电流控制器增益**参数。

### **积分增益** — PI 控制器的积分增益 `1000` (默认) | `scalar`

PI 电流控制器的积分增益 *ki*，用于实现磁场定向控制以便以闭环控制方式运行电机并估计 *Ke*、*J* 和 *B*。

#### 依赖关系

要启用此参数，请选择**指定电流控制器增益**参数。

### **惯量估计的转速下限(RPM)** — 减速期间的转速下限 `1000` (默认) | `scalar`

减速期间的转速下限（以 RPM 为单位），在达到此下限转速时，PMSM Mechanical Parameter Estimation 模块会记录时间戳，以用于估计电机惯量。有关估计过程的详细信息，请参阅 PMSM Mechanical Parameter Estimator。

### **参数估计采样时间(秒)** — 参数估计的采样时间 `50e-6` (默认) | `scalar`

参数估计算法的采样时间（以秒为单位）。此参数定义 PMSM 在以下参数估计模块中的采样时间：

- PMSM Rs Estimator
- Ld Estimator
- Lq Estimator
- PMSM Mechanical Parameter Estimator

## 所属库

Motor Control Blockset / Parameter Estimation / PMSM Parameter Estimation

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2023a 中推出**

## 描述

为 PMSM 参数估计生成配置元素

PMSM Parameter Estimation Configurator 模块生成以下配置元素，用于估计永磁同步电机 (PMSM) 的参数：

- 电机和逆变器硬件元素
- 用于估计电机电阻 (*Rs*) 的元素
- 用于估计电机电感（*Ld* 和 *Lq*）的元素
- 用于估计反电动势常量 (*Ke*)、电机惯量 (*J*) 和摩擦常量 (*B*) 的元素

该模块使用参数设置来生成包含配置元素的输出总线。您可以在以下 PMSM 参数估计模块中使用配置元素：

- Rs Estimator
- Ld Estimator
- Lq Estimator
- PMSM Mechanical Parameter Estimator
