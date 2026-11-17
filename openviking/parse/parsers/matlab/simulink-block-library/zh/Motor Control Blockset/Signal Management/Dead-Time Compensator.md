---
type: simulink-block
title: 'Dead-Time Compensator'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'deadtimecompensator'
documentation_source_path: 'ref/deadtimecompensator.html'
language: zh-CN
chinese_source: worker-translation
---

# Dead-Time Compensator

## 端口
```yaml
ports:
- name: Vabc
  summary: 参考电压 标量
  direction: input
  data_types: single | double | fixed point
- name: Iab
  summary: 测量的电机电流 标量
  direction: input
  data_types: single | double | fixed point
- name: fPWM
  summary: PWM 频率 标量
  direction: input
  data_types: single | double | fixed point
- name: Vdc
  summary: 逆变器直流电压 标量
  direction: input
  data_types: single | double | fixed point
- name: Enable
  summary: 使能模块输出的信号 标量
  direction: input
  data_types: single | double | fixed point
- name: Vabc ± Δ
  summary: 补偿后的三相电压 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **Vabc** — 参考电压 标量

三相参考电压（单位：伏特）。

**数据类型：** `single` | `double` | `fixed point`

### **Iab** — 测量的电机电流 标量

电机相 *a* 和相 *b* 电流的测量值（单位：安培）。

**数据类型：** `single` | `double` | `fixed point`

### **fPWM** — PWM 频率 标量

用于执行脉宽调制的载波频率（单位：赫兹）。

**数据类型：** `single` | `double` | `fixed point`

### **Vdc** — 逆变器直流电压 标量

逆变器的直流电压电源（单位：伏特）。

**数据类型：** `single` | `double` | `fixed point`

### **Enable** — 使能模块输出的信号 标量

使能模块输出的信号：

- `1` — 使能补偿（模块输出补偿后的电压）。
- `0` — 禁用补偿（模块输出输入电压）。

#### 依赖关系

要使能此端口，请选择 **Show enable port** 参数。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Vabc ± Δ** — 补偿后的三相电压 标量

经过逆变器死区效应补偿后的电机三相电压（单位：伏特）。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Dead time (s)
  summary: 逆变器开关死区时间 1e-6（默认）| 标量
  group: ''
- name: Enable hysteresis for currents near zero-crossing
  summary: 为接近零交叉点的电流使能滞环算法的选项 off（默认）| on
  group: ''
- name: Current hysteresis band (A)
  summary: 零交叉点附近的电流滞环带 0.1（默认）| 标量
  group: ''
- name: Motor current input
  summary: 电机电流输入类型 Two currents (Ia,Ib)（默认）| Three currents (Ia,Ib,Ic)
  group: ''
- name: Show enable port
  summary: 使能输入端口的选项 off（默认）| on
  group: 输入
```

### **Dead time (s)** — 逆变器开关死区时间 `1e-6`（默认）| 标量

逆变器开关的死区时间（单位：秒）。

### **Enable hysteresis for currents near zero-crossing** — 为接近零交叉点的电流使能滞环算法的选项 `off`（默认）| `on`

选择此参数以在输入电机相电流的零交叉区域附近使能滞环算法。

该模块检测电机电流极性以确定电压补偿。在电流零交叉点附近使用滞环带，有助于在电机电流存在噪声时更好地检测电流极性。

### **Current hysteresis band (A)** — 零交叉点附近的电流滞环带 `0.1`（默认）| 标量

电流控制器的滞环带 *h*。开启点为 *h*，关闭点为 *-h*。

#### 依赖关系

要使能此参数，请选择 **Enable hysteresis for currents near zero-crossing**。

### **Motor current input** — 电机电流输入类型 `Two currents (Ia,Ib)`（默认）| `Three currents (Ia,Ib,Ic)`

电机电流输入的数量。您可以选择以下选项之一：

- `Two currents (Ia,Ib)`
- `Three currents (Ia,Ib,Ic)`

### 输入

### **Show enable port** — 使能输入端口的选项 off（默认）| `on`

选择此参数以显示输入端口 **Enable**。
## 所属库

Motor Control Blockset / Signal Management Motor Control Blockset HDL Support / Signal Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

当您选择 **Enable hysteresis for currents near zero-crossing** 参数时，该模块不支持 HDL 代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

通过修改参考电压来克服死区效应

Dead-Time Compensator 模块补偿逆变器死区。使用此模块补偿三相逆变器的死区效应。

用于电机驱动应用的三相逆变器本质上是非线性的。逆变器中的死区（即为了避免逆变器桥臂短路而添加的死区）对这种非线性有显著影响。尽管死区确保了逆变器的安全运行，但它可能对逆变器的性能产生不利影响。这会导致逆变器输出电压波形偏离其原本预期的形式。

该模块接受三相参考电压、测量的电机电流、PWM 频率和逆变器直流电压作为输入。它提供补偿逆变器死区效应的三相电压输出。该补偿有助于降低电机转矩或电流中的噪声或纹波，从而改善电机驱动性能。

下图显示了该模块在电机控制算法中的位置。
