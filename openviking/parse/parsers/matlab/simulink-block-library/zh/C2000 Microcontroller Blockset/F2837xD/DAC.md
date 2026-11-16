---
type: simulink-block
title: 'C28x DAC'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F28003x'
documentation_page: 'c28xdac'
documentation_source_path: 'ref/c28xdac.html'
language: zh-CN
chinese_source: official
---

# C28x DAC

## 端口

### 输入

### **Port\_1** — 输入信号 `real` | `scalar`

输入端口，模块通过该端口接收数字输入值并将其转换为模拟信号。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `double`

## 参数

### **DAC 通道** — DAC 通道用于生成模拟输出 `12` (默认)

输入要生成模拟信号的 DAC 通道。您可以选择的 DAC 通道有 A、B 或 C。

### **Saturate on input overflow (>4095)** — 输入溢出时，可以选择限制输入值。 `off` | `on`

选中此复选框，当输入值大于 4095 时，将输入值饱和为 4095。

#### 兼容性注意事项

在 R2021b 之前的版本中，当取消选择 **Saturate on input overflow (>4095)** 参数时，DAC 的输入值大于 `65536` 会导致输出饱和在 `65535`。从 R2021b 开始，输出会循环，即，对于输入 `65580`，输出为 `44 (65580-65536)`。

## 所属库

C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2016b 中推出**

## 描述

配置 DAC 在指定的 DAC 通道 A/B/C 上生成模拟输出（12 位）

对于 F2837x/F2807x/F28004x 和 F2838x/C28x 处理器，在指定的 DAC 通道 A、B 或 C 上生成模拟输出。该模块接受一个 12 位值作为输入，范围为 0 到 4095。您可以使用 **Saturate on input outflow** 选项将高于 4095 的值饱和到 4095。

该模块的输出引脚与 ADC 模块的输入引脚复用。在模型中使用 DAC 模块时，ADC 的相应通道不能用作输入。如果使用，ADC 将对 DAC 输出进行采样。

ADC 和 DAC 共用的引脚是 DACOUTA/ADCINA0、DACOUTB/ADCINA1 和 DACOUTC/ADCINB1。DAC 模块的输入可以是 double、float、int 和 uint 类型。该模块将输入强制转换为 uint16 类型。
