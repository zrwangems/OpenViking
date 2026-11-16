---
type: simulink-block
title: 'C2802x/C2803x/C2806x/F28M3x COMP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c2802xc2803xc2806xf28m3xcomp'
documentation_source_path: 'ref/c2802xc2803xc2806xf28m3xcomp.html'
language: zh-CN
chinese_source: worker-translation
---

# C2802x/C2803x/C2806x/F28M3x COMP

## 端口

在 R2025b 中未记录。

## 参数

**比较器模块**
:   选择要配置的比较器模块。每个模块仅使用一个模块。

**第二输入**
:   选择 `COMPxB`，以将 **Input Pin A** 的电压与 **Input Pin B** 进行比较

    选择 `Internal DAC`，以将 **Input Pin A** 的电压与位于比较器中的 DAC 基准输出进行比较。有关更多信息，请参见 *TMS320x2802x, 2803x Piccolo Analog-to-Digital Converter (ADC) and Comparator* 的 “DAC Reference” 部分。

    如果 **Input Pin A** 的值大于 **Input Pin B** 或 10 位 DAC 基准，则比较器源输出 1。否则，它输出 0。

**反转比较器输出**
:   选择此复选框可对比较器源的输出应用逻辑 NOT。例如，当比较器源输出 1 时，电路将其反转为 0。

**同步**
:   选择 `Asynchronous` 以传递比较器输出的异步版本。选择 `Synchronous` 以传递比较器输出的同步版本。选择 `Synchronous` 会启用 **限定周期** 选项。

**限定周期**
:   在传递比较器输出的变化之前对其进行限定。`Passed through` 设置会传递比较器值的变化，而不对其进行限定。`consecutive clocks` 设置会在收到指定数量的、具有相同值的连续采样之后，传递比较器值的变化。使用此设置可防止比较器输出中出现间歇性和杂散变化。

**采样时间**
:   指定采样之间的时间间隔。要从上游模块继承采样时间，请将此参数设置为 -1。

**比较器模块**
:   选择要配置的比较器模块。每个模块仅使用一个模块。

**第二输入**
:   选择 `COMPxB`，以将 **Input Pin A** 的电压与 **Input Pin B** 进行比较

    选择 `Internal DAC`，以将 **Input Pin A** 的电压与位于比较器中的 DAC 基准输出进行比较。有关更多信息，请参见 *TMS320x2802x, 2803x Piccolo Analog-to-Digital Converter (ADC) and Comparator* 的 “DAC Reference” 部分。

    如果 **Input Pin A** 的值大于 **Input Pin B** 或 10 位 DAC 基准，则比较器源输出 1。否则，它输出 0。

**反转比较器输出**
:   选择此复选框可对比较器源的输出应用逻辑 NOT。例如，当比较器源输出 1 时，电路将其反转为 0。

**同步**
:   选择 `Asynchronous` 以传递比较器输出的异步版本。选择 `Synchronous` 以传递比较器输出的同步版本。选择 `Synchronous` 会启用 **限定周期** 选项。

**限定周期**
:   在传递比较器输出的变化之前对其进行限定。`Passed through` 设置会传递比较器值的变化，而不对其进行限定。`consecutive clocks` 设置会在收到指定数量的、具有相同值的连续采样之后，传递比较器值的变化。使用此设置可防止比较器输出中出现间歇性和杂散变化。

**采样时间**
:   指定采样之间的时间间隔。要从上游模块继承采样时间，请将此参数设置为 -1。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

在 R2025b 中未记录。

## 描述

比较比较器引脚上的两个输入电压

# C2802x/C2803x/C2806x/F28M3x COMP

比较比较器引脚上的两个输入电压

配置比较器模块，以在处理器的比较器引脚上输出比较结果。

- C2802x/C2803x/C2806x/F28M3x COMP 模块
