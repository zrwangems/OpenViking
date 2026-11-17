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
chinese_source: worker-translation
---

# C28x DAC

## 端口

### 输入

### **Port\_1** — 输入信号 `real` | `scalar`

输入端口，模块通过该端口接收数字输入值，将其转换为模拟信号。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `double`

## 参数

### **DAC channel** — 用于生成模拟输出的 DAC 通道 `12`（默认值）

输入用于生成模拟信号的 DAC 通道。可选择的 DAC 通道为 A、B 或 C。

### **Saturate on input overflow (>4095)** — 输入溢出时饱和输入值的选项 `off` | `on`

选中此复选框可在输入值高于 4095 时将输入值饱和至 4095。

#### 兼容性注意事项

在 R2021b 之前，当 **Saturate on input overflow (>4095)** 参数未选中时，DAC 的输入值大于 `65536` 会导致输出饱和在 `65535`。从 R2021b 开始，输出会回绕，即输入 `65580` 时输出为 `44 (65580-65536)`。

## 所属库

C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

配置 DAC 以在指定的 DAC 通道 A/B/C（12 位）上生成模拟输出

为 F2837x/F2807x/F28004x 和 F2838x/C28x 处理器在指定的 DAC 通道 A、B 或 C 上生成模拟输出。该模块接受范围为 0 到 4095 的 12 位值作为输入。您可以使用 **Saturate on input outflow** 选项将高于 4095 的值饱和至 4095。

该模块的输出引脚与 ADC 模块输入复用。当您在模型中使用 DAC 模块时，ADC 的对应通道不能用作输入。如果使用，ADC 将对 DAC 输出进行采样。

ADC 和 DAC 之间共享的引脚为 DACOUTA/ADCINA0、DACOUTB/ADCINA1 和 DACOUTC/ADCINB1。DAC 模块的输入可以是 double、float、int 和 uint。该模块将输入类型转换为 uint16。
