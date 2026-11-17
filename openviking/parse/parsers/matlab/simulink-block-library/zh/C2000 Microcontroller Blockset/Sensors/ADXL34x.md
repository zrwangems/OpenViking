---
type: simulink-block
title: 'ADXL34x Accelerometer'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'adxl34xaccelerometer'
documentation_source_path: 'ref/adxl34xaccelerometer.html'
language: zh-CN
chinese_source: worker-translation
---

# ADXL34x Accelerometer

## 端口
```yaml
ports:
- name: Acceleration
  summary: ADXL34x 传感器测得的线性加速度向量
  direction: output
  data_types: double
```

### 输出

### **Acceleration** — ADXL34x 传感器测得的线性加速度向量

此端口以 1×3 数组的形式输出沿 *x*、*y* 和 *z* 轴的线性加速度（单位为 m/s2）。

**数据类型：** `double`

**注意**

据观察，市场上有许多有故障的克隆 ADXL345 传感器，其 Z 轴原始输出变得无响应。请从正规分销商处购买传感器以避免此问题。
## 参数
```yaml
parameters:
- name: I2C module
  summary: 用于通信的模块 I2C_A（默认）
  group: ''
- name: I2C address
  summary: ADXL34x 传感器的 I2C 地址 0x53（默认）| 0x1D
  group: ''
- name: Data type
  summary: ADXL34x 传感器值的输出数据类型 single（默认）| double
  group: ''
- name: Sample time
  summary: 读取数据的时间间隔 -1（默认）| 正整数
  group: ''
- name: Accelerometer range
  summary: 测量线性加速度的满量程 ±4g（默认）| ±2g | ±8g | ±16g
  group: 高级设置
- name: Accelerometer output data rate
  summary: 加速度计数据的采样速率 12.5 Hz（默认）| 0.1 Hz | 0.2 Hz | 0.39 Hz | 0.78 Hz | 1.56 Hz | 3.13 Hz | 6.25 Hz | 25 Hz | 50 Hz | 100
    Hz | 200 Hz | 400 Hz | 800 Hz | 1600 Hz
  group: 高级设置
- name: Enable data ready interrupt
  summary: 数据就绪时使能中断 off（默认）| on
  group: 高级设置
- name: Interrupt generate pin
  summary: 用于生成数据就绪中断的引脚 INT1（默认）| INT2
  group: 高级设置
```

### **I2C module** — 用于通信的模块 `I2C_A`（默认）

用于与 ADXL34x 传感器通信的 I2C 模块。不同 C2000 处理器支持的 I2C 模块数量各不相同。您可以通过打开“配置参数”对话框并查看 **Target hardware resources** 下的 I2C 特定选项卡，找到与处理器（您在 Simulink 模型中为 Hardware Board 参数所选择的处理器）对应的受支持 I2C 模块。

### **I2C address** — ADXL34x 传感器的 I2C 地址 `0x53`（默认）| `0x1D`

该模块从中读取值的 ADXL34x 传感器的 I2C 地址。

根据传感器 ALT 引脚上的逻辑电平，ADXL34x 传感器可以有两个 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| ALT | 低 | 0x53 |
| 高 | 0x1D |

### **Data type** — ADXL34x 传感器值的输出数据类型 `single`（默认）| `double`

选择该模块从中读取值的传感器的数据类型。

指定从 ADXL34x 传感器读取的值的输出数据类型。C2000 板的默认数据类型为 `single`。如有需要，可使用此参数将值更改为 `double`。

### **Sample time** — 读取数据的时间间隔 `-1`（默认）| 正整数

指定此模块从 ADXL34x 传感器读取数据的频率。当您将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 高级设置

### **Accelerometer range** — 测量线性加速度的满量程 `±4g`（默认）| `±2g` | `±8g` | `±16g`

选择加速度计可测量的加速度范围。

### **Accelerometer output data rate** — 加速度计数据的采样速率 `12.5 Hz`（默认）| `0.1 Hz` | `0.2 Hz` | `0.39 Hz` | `0.78 Hz` | `1.56 Hz` | `3.13 Hz` | `6.25 Hz` | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz`

选择加速度计数据的采样输出数据速率。

### **Enable data ready interrupt** — 数据就绪时使能中断 `off`（默认）| `on`

如果选择此选项，当数据就绪时，传感器的 INT1 或 INT2 引脚上会生成中断，允许您触发其他子系统执行任何操作。

### **Interrupt generate pin** — 用于生成数据就绪中断的引脚 `INT1`（默认）| `INT2`

选择用于读取加速度计数据的中断生成引脚。

#### 依赖关系

要启用此参数，请选择 **Enable data ready interrupt** 参数。
## 所属库

C2000 Microcontroller Blockset / Sensors Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

测量 ADXL34x 系列加速度计沿各轴的线性加速度

ADXL34x Accelerometer 模块使用 C2000 板从 ADXL34x 系列加速度计（ADXL343、ADXL344、ADXL345 和 ADXL346）读取数据。

您可以使用此模块测量沿 *X*、*Y* 和 *Z* 轴的线性加速度。该模块还提供使能数据就绪中断的选项。

该模块以 1×3 数组的形式输出加速度。
