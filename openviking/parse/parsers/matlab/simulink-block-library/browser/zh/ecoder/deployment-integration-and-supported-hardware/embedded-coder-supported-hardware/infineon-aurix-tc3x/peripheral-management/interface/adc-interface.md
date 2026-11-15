---
type: simulink-block
title: 'ADC Interface'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / Interface'
documentation_page: 'adcinterface'
documentation_source_path: 'ref/adcinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# ADC Interface

## 端口

### 输入

### **start** — 启动模数转换，启动一个模数转换事件

指定一个事件信号，以开始对 **analog** 输入端口信号进行采样和测量。

**数据类型：** `rteEvent`

### **analog** — 模拟电压信号标量

输入模拟电压信号，将其转换为数字测量值。

**数据类型：** `double` | `single`
### 输出

### **digital** — SoC 消息数据标量

此端口将 ADC Interface 输入信号数据作为消息发送到 ADC Read 模块的 **msg** 输入端口。

**数据类型：** `SoCData`

### **wd event** — 模拟看门狗任务事件信号标量

此端口在模拟电压信号超过指定的 **Lower threshold** 和 **Upper threshold** 属性值时发送消息。此输出连接到 Task Manager 模块的输入，以执行关联的事件驱动任务，从而对过压或欠压输入事件做出反应。

#### 依赖项

要启用此端口，请启用 **Enable analog watchdog** 参数。

**数据类型：** `rteEvent`

### **event** — 任务事件信号标量

此端口在每次模数信号转换事件时发送消息。此输出连接到 Task Manager 模块的输入，以在执行 ADC 事件后执行关联的事件驱动任务。

#### 依赖项

要启用此端口，请启用 **Enable interrupt** 参数。

**数据类型：** `rteEvent`

## 参数

### 单通道

### **Resolution (bits)** — 数字测量的分辨率 `12`（默认） | `16`

输入模拟信号可以用 12 位或 16 位形式的数字值表示。1 位可以表示的模拟信号最小值称为 *分辨率*。一位表示 ADC 可测量的最小电压分辨率。最小电压分辨率可以使用以下公式确定：

其中 `n` 是 **Resolution (bits)**，`Vref` 是 **Voltage reference (V)** 参数值。

**示例：** `16`

### **Voltage reference (V)** — ADC 中的参考电压 `3`（默认） | `3.3`

参考电压决定了 ADC 在不饱和情况下可以转换为数字值的总电压范围。任何高于此值的电压信号都会产生可由 **Resolution (bits)** 参数表示的最大可能值。

**示例：** `3.3`

### **Acquisition time (s)** — ADC 捕获输入电压所需的时间 `320e-9`（默认） | 正标量

指定 ADC 在采样期间捕获输入电压所需的时间。

**示例：** `200e-9`

### **Conversion time (s)** — 将物理电压采样转换为数字值的时间 `240e-9`（默认） | 正标量

指定将物理电压采样转换为数字表示并输出该值所需的时间。

**示例：** `20e-9`

### **Charge/dischard time constant (s)** — ADC 采集电路的充电或放电时间常数 `0`（默认） | 非负标量

指定 ADC 采样采集电路的充电或放电时间常数。

### 多通道

### **Number of channel** — 多通道采样中使用的通道数 `1`（默认） | 范围 1 到 16 的整数

指定 ADC 模块使用的通道数。指定 2 个或更多通道可以实现更高效或更精确的输入信号测量。

### **Conversion type** — 多通道转换类型 `Sequential`（默认） | `Simultaneous` | `Oversampling`

选择多通道转换的类型。

- `Sequential` — 对每个 ADC 通道进行顺序测量。在新的 ADC 事件发生时，通道序列中的下一个通道会对输入信号进行新的测量。所有其他先前的通道值保持不变。顺序测量通过允许每个通道的单独转换时间超过 ADC 模块的采样率来改进采样。
- `Simultaneous` — 对每个 ADC 通道进行同步测量。在新的 ADC 事件发生时，所有通道都会对输入信号进行新的测量，替换先前捕获的值。同步测量允许使用平均值或其他滤波器从测量中去除噪声。
- `Oversampling` — 在 ADC 的多个通道上执行过采样测量。在两个定时器驱动的 ADC 事件之间，每个通道会进行带有时间偏移的 ADC 测量，从而使各通道在两个 ADC 事件之间均匀地对输入信号进行采样。所得的通道输出在每个采样点提供输入信号的过采样测量值。过采样测量允许 ADC 模块超过单个通道和 ADC 硬件的理论 Nyquist 采样率。

### 事件

### **Enable interrupt** — 用于启用中断事件生成的选项 enable（默认） | disable

选择此参数后，ADC Interface 模块将在 ADC 采集后生成中断，并启用 **event** 输出端口。您可以将此 **event** 端口连接到 Task Manager 模块，以模拟异步 ADC 操作。

### **Condition** — 触发中断的条件 `Acquisition time`（默认） | `Acquisition + Conversion time`

选择生成 ADC 中断事件的时间条件。使用 `Acquisition + Conversion time` 时，中断在完整测量可用时生成。使用 `Acquisition time` 时，中断在测量值可用之前生成。这允许关联任务在转换期间启动，并减少总测量周期中的执行延迟。

### **Enable analog watchdog** — 用于启用模拟看门狗中断事件生成的选项 off（默认） | on

选择此参数后，ADC Interface 模块将在输入电压超过指定的 **Lower threshold** 和 **Upper threshold** 参数值的 ADC 采集后生成模拟看门狗中断。选择此参数还会启用 **wd event** 输出端口，您可以将其连接到 Task Manager 模块，以模拟对 ADC 输入信号上的过压或欠压事件执行任务操作。

### **Lower threshold** — 看门狗触发的下限阈值 `0.1`（默认） | 实数值标量

指定模拟输入信号的下限阈值，用于触发模拟看门狗中断事件。

**示例：** `0.2`

### **Upper threshold** — 看门狗触发的上限阈值 `2.9`（默认） | 实数值标量

指定模拟输入信号的上限阈值，用于触发模拟看门狗中断事件。

**示例：** `3.0`

### **Interrupt latency (s)** — 中断生成延迟 `0`（默认） | 正标量

指定 ADC 硬件模块从转换完成到在软件中生成中断所需的时间。

**示例：** `0.00001`

## 所属库

SoC Blockset / Peripherals C2000 Microcontroller Blockset / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要自动为您的设计生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder (SoC Blockset) 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅 Generate Code and Deploy Using SoC Builder for Infineon® AURIX™ TC3x 和 Generate Code and Deploy Using SoC Builder for Infineon AURIX TC4x microcontrollers。

## 版本历史

**在 R2020b 中引入**

## 描述

将 ADC 输入引脚上的模拟信号转换为数字信号

ADC Interface 模块模拟硬件板的模数转换（ADC）。输入模拟信号会被采样并转换为具有代表性的数字值。start 事件消息向该模块发出信号，以对输入模拟电压信号进行采样。当转换完成时，该模块会发出模拟信号的数字表示，并向 Task Manager 模块发送事件。此时，连接的任务可以使用新的 ADC 采样执行。
