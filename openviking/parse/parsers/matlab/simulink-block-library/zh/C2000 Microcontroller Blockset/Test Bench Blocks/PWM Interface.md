---
type: simulink-block
title: 'PWM Interface'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Test Bench Blocks'
documentation_page: 'pwminterface'
documentation_source_path: 'ref/pwminterface.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Interface

## 端口

### 输入

### **msg** — SoC 消息数据数值向量

此端口从所连接的 PWM Write 模块的 **msg** 端口接收占空比数据。

**数据类型：** `SoCData`
### 输出

### **PWM** — 脉宽调制信号标量

此端口输出由 **dCycle** 输入端口定义的脉宽调制方波。

#### 依赖关系

要启用此端口，请将 **Output mode** 参数设置为 `Switching`。

**数据类型：** `double`

### **~PWM** — 互补脉宽调制信号标量

此端口输出互补 **PWM** 信号。

#### 依赖关系

要启用此端口，请将 **Output mode** 参数设置为 `Switching`。

**数据类型：** `double`

### **dCycle** — 脉宽调制信号的模拟近似标量

此端口发出 PWM 波形的平均值，该值是占空比输入值的直通。此图显示等效于 PWM 输出的平均输出信号。

PWM 信号的近似波形。

#### 依赖关系

要启用此端口，请将 **Output mode** 参数设置为 `Average`。

**数据类型：** `double`

### **event** — 每个 PWM 周期发出的事件标量

此端口在每个 PWM 输出事件期间发送消息，该消息可连接到 ADC Interface 模块的 **start** 端口，以在闭环系统中同步 ADC 和 PWM 事件。

#### 依赖关系

要启用此端口，必须将 **Type** 参数设置为 `ADC start` 或 `ADC start and PWM interrupt`。

**数据类型：** `rteEvent`

### **event*`n`*** — 每个 PWM 周期发出的复制事件标量

此端口创建 **event** 输出端口的复制端口，以协调多个 ADC 模块与 PWM 模块。

#### 依赖关系

要启用此端口，请将 **Type** 参数设置为 `ADC start` 或 `ADC start and PWM interrupt`，并将 **Number of replicas** 参数设置为大于或等于 2 的值。

**数据类型：** `rteEvent`

### **interrupt** — 每个 PWM 周期发出的中断事件标量

此端口在每个 PWM 输出事件期间发送消息，该消息可连接到 Task Manager 模块，以响应 PWM 输出更新来触发其他任务。

#### 依赖关系

要启用此参数，请将 **Type** 参数设置为 `PWM interrupt` 或 `ADC start and PWM interrupt`。

**数据类型：** `rteEvent`

## 参数

### 主要

### **PWM waveform period (s)** — PWM 波形的周期 `50e-6`（默认值）| 正标量

指定 PWM 波形的周期，以 seconds 为单位。

**注意**

对于 `PWM waveform period (s)` 为 10ns 的情况，占空比必须大于 1%。

### **Output mode** — 输出模式 `Switching`（默认值）| `Average`

通过指定 `Switching` 将输出信号仿真为真实 PWM 波形，或通过指定 `Average` 将其仿真为占空比的平均值。

**示例：** `Switching`

### **Counter mode** — 计数器波形 `Up-Down`（默认值）| `Up` | `Down`

计数器模式指定驱动 PWM 模块内部 PWM 输出信号的底层锯齿波形的形状。在 `Up` 模式下，锯齿计数器递增到最大值，然后在每个周期复位为零。在 `Down` 模式下，锯齿计数器递减到零，然后复位为最大值。在 `Up-Down` 模式下，锯齿计数器从零振荡到最大值。

**示例：** `Up`

### **Sampling mode** — 采样模式 `End of PWM period`（默认值）| `Mid or End of PWM period` | `Immediate (at compare matches)`

指定对输入占空比进行采样的时间。

**示例：** `Mid or End of PWM period`

### **Dead time (s)** — 死区切换延迟 `1e-6`（默认值）| 正标量

在关闭逆变器一个桥臂的其中一个晶体管与开启另一个晶体管之间引入时间延迟，以确保不会发生死短路。此图显示预期的占空比以及由晶体管切换死区引入的延迟。

**示例：** `450e-9`

### PWM 输出

### **At *`position`* of period** — 周期中 *`position`* 处的信号变化 `High` | `Low` | `Change` | `NoChange`

指定 PWM 波形信号在波形中相对于总周期的 *`position`* 处的状态。当设置为 `High` 或 `Low` 时，波形输出分别变为 `1` 或 `0`。当设置为 `Change` 时，波形反转当前值。当设置为 `NoChange` 时，波形不变化。*`position`* 可以是 PWM 波形的 `start` 或 `mid` 点。下表给出这些参数的默认设置。

| 参数 | 默认值 |
| --- | --- |
| **At start of period** | `High` |
| **At mid of period** | `NoChange` |

#### 依赖关系

`At mid of period` 仅在 **Counter mode** 参数设置为 Up-Down 时可用。

### **At compare *`n`*** — 比较器 n 触发时的信号变化 `High` | `Low` | `Change` | `NoChange`

指定当内部 PWM 计数器触发比较器 *`n`* 时 PWM 波形信号的状态。当设置为 `High` 或 `Low` 时，波形输出分别变为 `1` 或 `0`。当设置为 `Change` 时，波形反转当前值。当设置为 `NoChange` 时，波形不变化。有两个比较器 `1` 和 `2` 可用于修改 PWM 信号。下表给出这些参数的默认设置。

| 参数 | 默认值 |
| --- | --- |
| **At compare 1** | `Low` |
| **At compare 2** | `NoChange` |

#### 依赖关系

**At compare 1** 和 **At compare 2** 参数仅在 **Counter mode** 参数设置为 `Up` 或 `Down` 时可用。

### **At compare *`n`* *`direction`* count** — 比较器 n 触发时的信号变化 `High` | `Low` | `Change` | `NoChange`

指定当内部 PWM 计数器按指定 *`direction`* 越过比较器 *`n`* 值时 PWM 波形信号的状态。当设置为 `High` 或 `Low` 时，波形输出分别变为 `1` 或 `0`。当设置为 `Change` 时，波形反转当前值。当设置为 `NoChange` 时，波形不变化。有两个比较器 `1` 和 `2` 可用于修改 PWM 信号。下表给出这些参数的默认设置。

| 参数 | 默认值 |
| --- | --- |
| **At compare 1 up count** | `Low` |
| **At compare 1 down count** | `High` |
| **At compare 2 up count** | `NoChange` |
| **At compare 2 down count** | `NoChange` |

#### 依赖关系

这些参数仅在 **Counter mode** 参数设置为 `Up-Down` 时可用。

### 相位

### **Phase offset in degree (0-360)** — PWM 波形偏移标量，范围从 `0` 到 `360`

指定 PWM 波形相对于波形周期的相位。相位表示为 `0` 到 `360` degrees 之间的标量。

### 事件

### **Type** — 要生成的事件类型 `ADC start`（默认值）| `PWM interrupt` | `ADC start and PWM interrupt`

指定要在其上生成事件的事件类型。当 **Type** 值设置为：

- `ADC start` — 生成事件以触发启动 ADC 转换。
- `PWM interrupt` — 生成中断事件以触发任务启动。
- `ADC start and PWM interrupt` — 为 ADC 和任务生成事件。

**示例：** `ADC start and PWM interrupt`

### **ADC start condition** — 相对于 PWM 波形的触发模式 `End of PWM period`（默认值）| `Mid of PWM period` | `Mid or End of PWM period` | `Compare 1 up count` | `Compare 1 down count` | `Compare 2 up count` | `Compare 2 down count`

指定此模块相对于 PWM 波形何时触发事件。

**示例：** `Mid or End of PWM period`

#### 依赖关系

要启用此参数，必须将 **Type** 参数设置为 `ADC start` 或 `ADC start and PWM interrupt`。

### **Generate on** — 在 PWM 更新的倍数上生成事件 `1st event`（默认值）| `nth event` | `16th event`

指定在 PWM 事件的指定倍数上生成并输出 ADC 触发事件。例如，如果 **Generate on** 设置为 `6th event`，则 PWM Interface 模块接收 6 个消息，更新输出 6 次，然后生成 ADC 事件消息。

**示例：** `4th event`

#### 依赖关系

要启用此参数，必须将 **Type** 参数设置为 `ADC start` 或 `ADC start and PWM interrupt`。

### **Number of replicas** — 生成复制事件端口 `1`（默认值）| 从 `1` 到 `16` 的整数

在模块上生成复制 ADC 事件端口和事件。使用此参数协调从单个 PWM Interface 模块触发多个 ADC 模块。

**示例：** `4`

#### 依赖关系

要启用此参数，必须将 **Type** 参数设置为 `ADC start` 或 `ADC start and PWM interrupt`。

### **PWM interrupt condition** — 相对于 PWM 波形的触发模式 `End of PWM period`（默认值）| `Mid of PWM period` | `Mid or End of PWM period` | `Compare 1 up count` | `Compare 1 down count` | `Compare 2 up count` | `Compare 2 down count`

指定此模块相对于 PWM 波形何时触发中断事件。

**示例：** `Mid or End of PWM period`

#### 依赖关系

要启用此参数，必须将 **Type** 参数设置为 `PWM interrupt` 或 `ADC start and PWM interrupt`。

### **Interrupt latency (s)** — 中断生成延迟 `0`（默认值）| 正数

指定 PWM 硬件模块从完成输出更新到在软件中生成中断所需的时间。

**示例：** `0.00001`

#### 依赖关系

要启用此参数，必须将 **Type** 参数设置为 `PWM interrupt` 或 `ADC start and PWM interrupt`。

### **Generate on** — 在 PWM 更新的倍数上生成事件 `1st event`（默认值）| `nth event` | `16th event`

指定在 PWM 事件的指定倍数上生成并输出 PWM 中断触发事件。例如，如果 **Generate on** 设置为 `6th event`，则 PWM Interface 模块接收 6 个消息，更新输出 6 次，然后生成 PWM 中断事件消息。

**示例：** `4th event`

#### 依赖关系

要启用此参数，必须将 **Type** 参数设置为 `PWM interrupt` 或 `ADC start and PWM interrupt`。

## 所属库

SoC Blockset / Peripherals C2000 Microcontroller Blockset / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码并在 SoC 设备上执行，请使用 SoC Builder (SoC Blockset) 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅 Use SoC Builder to Generate SoC Design (SoC Blockset)。

## 版本历史

**在 R2020b 中引入**

## 描述

仿真来自硬件的脉宽调制 (PWM) 输出

PWM Interface 模块仿真硬件板的 PWM 输出。此模块从所连接的 PWM Write 模块获取占空比数据消息，该 PWM Write 模块可以生成开关脉宽调制波形，也可以将占空比数值传递到输出。
