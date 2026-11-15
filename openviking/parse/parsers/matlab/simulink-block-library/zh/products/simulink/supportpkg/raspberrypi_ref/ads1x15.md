---
type: simulink-block
title: 'ADS1x15'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'ads1x15'
documentation_source_path: 'supportpkg/raspberrypi_ref/ads1x15.html'
language: zh-CN
chinese_source: worker-translation
---

# ADS1x15

## 端口

### 输出

### **data** — ADC 数字数据标量

该模块输出模拟通道转换后的数字数据。对于 ADS1015 转换器，数字输出值的范围为 0 到 4095；而对于 ADS1115 转换器，数字输出值的范围为 0 到 65535。

**数据类型：** `int16`

## 参数

### 基本

### **ADC 芯片** — ADC 转换器 IC `ADS1015`（默认）| `ADS1115`

选择用于执行模数转换的 ADC 转换器集成电路 (IC)。ADS1015 IC 是 12 位 ADC，而 ADS1115 IC 是 16 位 ADC。

### **I2C 地址** — ADS1x15 IC 的 I2C 地址 `0x48`（默认）| `0x49` | `0x4A` | `0x4B`

选择用于与 Raspberry Pi 板通信的 ADS1x15 ADC 的 I2C 地址。ADS1x15 ADC 可以有四个 I2C 地址，具体取决于引脚 SCL 和 SDA 上的逻辑电平。

| I2C 地址 | ADC 地址引脚 |
| --- | --- |
| 0x48 | GND |
| 0x49 | VIN |
| 0x4A | SDA |
| 0x4B | SCL |

### **转换模式** — ADC 转换模式 `Single-shot`（默认）| `Continuous`

- `Single-shot` — 在此模式下，ADC 在指定的采样时间仅执行一次模数转换，并写入 ADC 结果数据寄存器。
- `Continuous` — 在此模式下，模拟输入会连续转换为其数字等效值，并写入 ADC 结果数据寄存器。

### **输入通道** — ADC 转换器的模拟输入通道 `A0 - A1 (Differential)`（默认）| `A0 - A3 (Differential)` | `A1 - A3 (Differential)` | `A2 - A3 (Differential)` | `A0 - GND (Single-ended)` | `A1 - GND (Single-ended)` | `A2 - GND (Single-ended)` | `A3 - GND (Single-ended)`

选择 ADC 转换器的模拟输入通道。

- `A0 - A1 (Differential)` — 测量传感器 A0 和 A1 输入通道之间的电压差。
- `A0 - A3 (Differential)` — 测量传感器 A0 和 A3 输入通道之间的电压差。
- `A1 - A3 (Differential)` — 测量传感器 A1 和 A3 输入通道之间的电压差。
- `A2 - A3 (Differential)` — 测量传感器 A2 和 A3 输入通道之间的电压差。
- `A0 - GND (Single-ended)` — 测量 A0 输入通道上相对于传感器 GND 引脚的模拟电压。
- `A1 - GND (Single-ended)` — 测量 A1 输入通道上相对于传感器 GND 引脚的模拟电压。
- `A2 - GND (Single-ended)` — 测量 A2 输入通道上相对于传感器 GND 引脚的模拟电压。
- `A3 - GND (Single-ended)` — 测量 A3 输入通道上相对于传感器 GND 引脚的模拟电压。

### **增益** — 放大输入模拟信号 `+/-2.048V`（默认）| `+/-6.144V` | `+/-4.096V` | `+/-1.024V` | `+/-0.512V` | `+/-0.256V`

选择 ADC 转换器的增益，以放大微弱的输入模拟信号。

### **数据速率** — 数据转换速率 `1600SPS`（默认）| `128SPS` | `250SPS` | `490SPS` | `920SPS` | `2400SPS` | `3300SPS`

选择 ADC 转换器的模数转换速率，单位为每秒采样数 (SPS)。

### **采样时间** — 模块读取数据的时间间隔 `0.01`（默认）| scalar

输入为所选输入通道转换的连续采样集之间的时间，单位为秒。这是从结果寄存器读取值的速率。

### 高级

### **启用比较器** — 启用高级 ADC 选项 `off`（默认）| `on`

选择此选项可启用对 ADC 应用有用的高级功能。

### **模式** — ADC 比较器模式 `Traditional with hysteresis`（默认）| `Window`

选择 ADC 芯片上 ALERT 引脚比较器的工作模式。

- `Traditional with hysteresis` — 在此模式下，当转换数据超过高阈值寄存器中设置的限值时，ADC 芯片上的 ALERT 引脚会置为有效。当输入信号降至低阈值寄存器值以下时，比较器随后会置为无效。
- `Window` — 在此模式下，当转换数据超过高阈值寄存器或降至低阈值寄存器以下时，ALERT 引脚会置为有效。

#### 依赖关系

- 要启用此参数，请选择 **启用比较器**。

### **极性配置** — ADC 比较器极性配置 `Active low`（默认）| `Active high`

选择 ADC 芯片上 ALERT 引脚的比较器极性。

- `Active low` — 在数字输出信号的下降沿使 ADC 芯片的 ALERT 引脚置为有效。
- `Active high` — 在数字输出信号的上升沿使 ADC 芯片的 ALERT 引脚置为有效。

#### 依赖关系

- 要启用此参数，请选择 **启用比较器**。

### **锁存配置** — ADC 比较器锁存配置 `Non-latching`（默认）| `Latching`

选择 ADC 芯片上 ALERT 引脚的锁存配置。

- `Non-latching` — 选择此选项可在输入模拟信号未超出低阈值和高阈值时清除 ADC 芯片 ALERT 引脚上的有效状态。
- `Latching` — 选择此选项可使 ADC 芯片 ALERT 引脚上的有效状态继续保持，即使输入模拟信号未超出低阈值和高阈值。

#### 依赖关系

- 要启用此参数，请选择 **启用比较器**。

### **队列配置** — 在 ADC 芯片 ALERT 引脚置为有效之前的队列配置 `Assert after 1 conversion`（默认）| `Assert after 2 conversions` | `Assert after 4 conversions`

选择此选项以控制在使 ADC 芯片的 ALERT 引脚置为有效之前，所需超过上限或下限阈值的连续转换次数。

#### 依赖关系

- 要启用此参数，请选择 **启用比较器**。

### **低阈值** — 队列配置的低阈值 `0`（默认）| scalar

输入在使 ADC 芯片的 ALERT 引脚置为有效之前，用于队列配置的较低阈值。

#### 依赖关系

- 要启用此参数，请选择 **启用比较器**。

### **高阈值** — 队列配置的高阈值 `0`（默认）| scalar

输入在使 ADC 芯片的 ALERT 引脚置为有效之前，用于队列配置的较高阈值。

#### 依赖关系

- 要启用此参数，请选择 **启用比较器**。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Basic

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

从 ADS1015 和 ADS1115 ADC 读取数字输出数据

使用 ADS1x15 模数转换器模块对连接到所选 ADC 输入引脚的信号执行模数转换。该模块输出表示模拟输入信号的数字值，并将转换后的值存储在数字信号处理器的结果寄存器中。您可以使用此模块捕获来自外部源（例如信号发生器、频率发生器或音频设备）的模拟信号并将其数字化。使用 ADS1x15 模块，您可以针对 ADS1015 和 ADS1115 转换器进行配置，它们分别提供 12 位和 16 位精度的数字输出。

### 硬件连接

当您选择 A0 - A1 作为 ADS1x15 传感器的差分输入通道时，请使用下表设置 Raspberry Pi® 板、ADS1x15 传感器和模拟源设备之间的连接。对于您选择的任何其他输入通道，请相应地建立硬件连接。

| Raspberry Pi | ADS1x15 传感器 | 设备 |
| --- | --- | --- |
| VCC | VCC |  |
| GPIO 2 | SDA |
| GPIO 3 | SCL |
| GND | GND | GND |
|  | A0 | Sig + |
| A1 | Sig - |
