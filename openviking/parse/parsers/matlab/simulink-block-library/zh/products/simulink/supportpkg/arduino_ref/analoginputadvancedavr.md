---
type: simulink-block
title: 'Analog Input AVR'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'analoginputadvancedavr'
documentation_source_path: 'supportpkg/arduino_ref/analoginputadvancedavr.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input AVR

## 端口

### 输出

### **ADC\_Ch1(A0)** — ADC 输出数据标量

该模块输出 Arduino 板模拟输入引脚接收到的、经数字化转换后的电压数据。输出端口数量取决于您在 **模拟输入引脚数** 参数中指定的模拟输入引脚数量。例如，如果您将 **模拟输入引脚数** 参数设置为 `3`，则该模块启用三个输出端口，端口名称为 **ADC\_Ch1(A0)**、**ADC\_Ch2(A1)** 和 **ADC\_Ch3(A2)**。

**数据类型：** `double`

## 参数

### **模拟输入引脚数** — 选择模拟输入的数量 `1`（默认） | `2` | `3`

选择用于模数转换的输入数量。

### **引脚编号 1** — Arduino 引脚编号 `0`（默认） | Arduino 板引脚编号

输入 Arduino 板模拟输入引脚编号。要打开 Arduino 引脚映射表，请点击 **查看引脚映射**。有关如何为 Analog Input 模块分配引脚的更多信息，请参阅 Arduino 定时器无关模块的引脚映射。

**引脚编号** 参数的数量取决于您在 **模拟输入引脚数** 参数中指定的模拟输入引脚数量。例如，如果您将 **模拟输入引脚数** 参数设置为 `3`，则该模块启用 **引脚编号 2** 和 **引脚编号 3** 参数。您可以相应地输入 Arduino 板的模拟引脚编号。

### **ADC 触发** — 选择用于启动 ADC 转换的触发器 `Free running mode`（默认） | `Timer/Counter 0 Compare Match A` | `Timer/Counter 0 Overflow` | `Timer/Counter 1 Compare Match B` | `Timer/Counter 1 Overflow` | `Timer/Counter 4 Overflow` | `Timer/Counter 4 Compare Match A` | `Timer/Counter 4 Compare Match B` | `Timer/Counter 4 Compare Match D`

选择定时器/计数器触发器，以在触发器的正边沿启动 ADC 转换。使用 PWM 模块将 Arduino 硬件板引脚连接到 PWM 输入信号，以启用定时器/计数器。

- `Free running mode` — 独立于时钟运行，并在上一次转换结束时触发一次 ADC 转换。
- `Timer/Counter 0 Compare Match A` — 一旦 Timer/Counter 0 的值与输出比较寄存器 (OCR) A 中存储的值匹配，就触发一次 ADC 转换。
- `Timer/Counter 0 Overflow` — 当 Timer/Counter 0 寄存器中设置的值达到其最大值时，触发一次 ADC 转换。
- `Timer/Counter 1 Compare Match B` — 一旦 Timer/Counter 0 的值与 OCR B 中存储的值匹配，就触发一次 ADC 转换。
- `Timer/Counter 1 Overflow` — 当 Timer/Counter 1 寄存器中设置的值达到其最大值时，触发一次 ADC 转换。
- `Timer/Counter 4 Overflow` — 当 Timer/Counter 4 寄存器中设置的值达到其最大值时，触发一次 ADC 转换。
- `Timer/Counter 4 Compare Match A` — 一旦 Timer/Counter 4 的值与 OCR A 中存储的值匹配，就触发一次 ADC 转换。
- `Timer/Counter 4 Compare Match B` — 一旦 Timer/Counter 4 的值与 OCR B 中存储的值匹配，就触发一次 ADC 转换。
- `Timer/Counter 4 Compare Match D` — 一旦 Timer/Counter 4 的值与 OCR D 中存储的值匹配，就触发一次 ADC 转换。

### **启用 ADC 转换完成中断** — 在 ADC 转换完成后启用中断 `on`（默认） | `off`

选择此选项可在 Arduino 硬件引脚处的模拟电压转换为其等效数字电压后生成中断。

## 所属库

Simulink Support Package for Arduino Hardware / Advanced / AVR

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

在 Arduino AVR 内核的模拟引脚完成 ADC 转换后读取 ADC 寄存器值

使用 Analog Input 模块在 Arduino® AVR 模拟引脚上完成模数转换后，从 ADC 寄存器读取值。您可以使用该模块同时读取最多三个模拟电压输出。

**注意**

Analog Input 模块支持 C/C++ 代码生成。此功能允许您使用 Embedded Coder® 生成 C 和 C++ 代码。
