---
type: simulink-block
title: 'F2807x/F2837xD/F2837xS/F28004x/F28003x/F2838x/F28p65x SDFM'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F28003x'
documentation_page: 'f2807xf2837xdf2837xsf28004xf28003xf2838xf28p65xsdfm'
documentation_source_path: 'ref/f2807xf2837xdf2837xsf28004xf28003xf2838xf28p65xsdfm.html'
language: zh-CN
chinese_source: worker-translation
---

# F2807x/F2837xD/F2837xS/F28004x/F28003x/F2838x SDFM

## 端口

### 输出

### **DFSTS** — 数据滤波器状态 `0` | `1` | `-1`

数据滤波器返回的状态为以下之一：

- 0 - 数据滤波器未就绪
- 1 - 数据滤波器就绪
- -1 - 调制器时钟故障

### **DFLTX** — 数据滤波器 `scalar`

主滤波器数据输出。它以 32-bit 或 16-bit
格式表示。

**DFLTX** - x 表示滤波器通道。

### **CFSTS** — 比较器状态 `0` | `1` | `2` | `3` | `4` | `5` | `-1`

不同处理器的比较器状态值不同。

**比较器状态值**

| 比较器状态值 | F2837x/07 | F28004x | F2838x/003x/P65x |
| --- | --- | --- | --- |
| 0 | 未发生比较器事件 | 未发生比较器事件 | 未发生比较器事件 |
| 1 | 低阈值事件 (LLT) | 低阈值事件 (LLT)  无 HLTZ | 比较器事件 1 (CEVT1)。 无 HLTZ |
| 2 | 高阈值事件 (HLT) | 高阈值事件 (HLT)  无 HLTZ | 比较器事件 2 (CEVT2)。 无 HLTZ |
| 3 | 不适用 | HLTZ。无 HLT 且无 LLT | HLTZ。无 CEVT1 且无 CEVT2 |
| 4 | 不适用 | HLTZ 和 LLT | CEVT1 和 HLTZ |
| 5 | 不适用 | HLTZ 和 HLT | CEVT2 和 HLTZ |
| -1 | 调制器时钟故障 | 调制器时钟故障 | 调制器时钟故障 |

#### 依赖关系

要启用此端口，请选择 **Enable comparator filter
output** 参数。

### **CFLTX** — 比较器滤波器 `scalar`

次级数据滤波器输出。**CFLTX** - x 表示
滤波器通道。

此比较器滤波器仅适用于特定处理器。

#### 依赖关系

要启用此端口，请选择 **Enable comparator filter
output** 参数。

## 参数

### **SDFM module** — 指示要使用的寄存器 `1` (default) | `2`

选择应配置为输出结果的 SDFM 寄存器。

**注意**

F28004x 处理器只有一个 SDFM 模块。

### **Filter channel** — 选择滤波器模块 `Filter1` (default) | `Filter2` | `Filter3` | `Filter4`

每个滤波器通道由一个输入控制单元、一个数据滤波器单元和一个比较器滤波器单元组成。每个滤波器模块均可独立配置。SDFM 模块由四个主滤波器和四个次级滤波器组成。

### **Data representation** — 内部 DAC 的来源 `16-bit` (default) | `32-bit`

数据滤波器输出可以 32-bit 或 16-bit 格式表示。

默认情况下，数据滤波器输出以 16-bit 格式表示。当输出以 16-bit 格式表示时，所需的移位在内部处理。

### **Sample time** — 读取数据的频率 `0.1` (default)

使用此参数指定采样之间的时间间隔。要从上游模块继承采样时间，请将此参数设置为 `-1`。

### **Enable comparator filter output** — 启用比较器输出端口 `off` (default) | `on`

选择此选项以启用比较器状态 (CFSTS) 和比较器滤波器 (CFLTX) 输出端口。

## 所属库

C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

配置 SDFM 模块的滤波器通道

Sigma delta 滤波器模块 (SDFM) 是一款四通道数字滤波器，专为电机控制应用中的电流测量和旋转变压器位置解码而设计。每个输入通道可以接收独立的 delta-sigma (ΔΣ) 调制器位流。这些位流由四个可独立编程的数字抽取滤波器处理。

该滤波器组包括一个快速比较器（次级滤波器），用于过流和欠流监测的即时数字阈值比较，以及一个主数据滤波器。

每个 SDFM 模块包含：

- 四个独立可配置的主滤波器（数据滤波器）单元。
- 四个独立、可配置的次级滤波器（比较器）单元。
- 八个外部引脚（四个 sigma-delta 数据输入引脚和四个 sigma-delta 时钟输入引脚）。
- 四种不同的可配置调制器时钟模式。

有关配置滤波器通道的更多信息，请参阅 SDFM Configuration Parameters。
