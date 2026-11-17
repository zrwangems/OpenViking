---
type: simulink-block
title: 'F2807x/F2837xD/F2837xS/F28004x/F2838x/F2800xx CMPSS'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F280013x'
documentation_page: 'f2807xf2837xdf2837xsf28004xf2838xf2800xxcmpss'
documentation_source_path: 'ref/f2807xf2837xdf2837xsf28004xf2838xf2800xxcmpss.html'
language: zh-CN
chinese_source: worker-translation
---

# F2807x/F2837xD/F2837xS/F28004x/F2838x/F2800xx CMPSS

## 端口

### 输入

### **DAC** — DAC 模块 `scalar`

12 位 DAC 参考值用于比较器的第二个输入引脚。

DAC 范围为 0 到 4095。任何超出范围的值都会被饱和处理。

#### 依赖关系

DAC 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **DAC
  module**
- **Specify DAC/RAMP parameter(s) Via** 设置为
  **输入端口**

### **REF** — 斜坡参考值 `scalar`

斜坡发生器用于为比较器的第二个输入引脚创建斜坡参考电压的斜坡参考值。

REF 值应在 0 到 65535 范围内。任何超出范围的值都会被饱和处理。

#### 依赖关系

REF 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **RAMP
  module**
- **Specify DAC/RAMP parameter(s) Via** 设置为
  **输入端口**
- 此端口仅适用于 COMPH 模块。

### **DEC** — RAMP 递减值 `scalar`

斜坡发生器用于为比较器的第二个输入引脚创建斜坡参考电压的斜坡递减值。

DEC 范围为 0 到 65535。任何超出范围的值都会被饱和处理。

#### 依赖关系

DEC 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **RAMP
  module**
- **Specify DAC/RAMP parameter(s) Via** 设置为
  **输入端口**
- 此端口仅适用于 COMPH 模块。

### **DLY** — RAMP 延迟值 `scalar`

斜坡发生器用于为比较器的第二个输入引脚创建斜坡参考电压的斜坡延迟值。

DLY 范围为 0 到 8192。任何超出范围的值都会被饱和处理。

#### 依赖关系

DLY 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **RAMP
  module**
- **Specify DAC/RAMP parameter(s) Via** 设置为
  **输入端口**
- 此端口仅适用于 COMPH 模块。

### **LCLR** — 锁存清除 `scalar`

用于清除比较器锁存输出的信号。任何大于 0 的值都将清除锁存输出。

#### 依赖关系

锁存清除端口仅在选中 **Enable latch
clear** 参数时出现。
### 输出

### **STS** — 比较器状态输出 `scalar`

如果第一个输入引脚上的电压大于第二个输入引脚上的电压，比较器模块输出 1。否则，输出 0。

### **LTH** — 比较器锁存 `scalar`

比较器锁存输出是 CMPSS 比较器经过数字化和数字滤波器限定后的触发状态。

锁存值可以通过软件或 PWMSYNC 清除。

#### 依赖关系

要启用此端口，请选中 **Enable latch output**
参数。

## 参数

### **Comparator module** — 指示要使用的模块 `CMPSS1_COMPH`（默认）| `CMPSSx_COMPL` | `CMPSSx_COMPH` | `其中 x 的范围为 1 到 8`

选择应配置哪个比较器模块来输出比较结果。

**注意**

不同处理器可用的模块数量会有所不同。

### **Second input** — 第二个输入引脚的来源 `External pin`（默认）| `Internal DAC`

第二个输入引脚（负输入引脚）的电压源，指定为 External pin 或 Internal DAC。

### **DAC source select** — 内部 DAC 的来源 `DAC module`（默认）| `RAMP module`

选择内部 DAC 的来源以为负输入引脚生成电压，指定为 DAC module 或 RAMP module。

#### 依赖关系

此参数仅适用于 COMPH 模块。

### **Specify DAC/RAMP parameter(s) via** — 配置源 DAC/RAMP 值来源 `Dialog`（默认）| `Input port`

选择 DAC 或 RAMP 值是通过输入端口指定还是从对话框指定。

当您选择输入端口时，模块会为比较器模块生成输入端口。

当您将 **DAC source select** 参数设置为 **DAC
module** 时，模块生成 **DAC** 端口；当 DAC
source select 设置为 RAMP module 时，它生成 **REF**、
**DEC** 和 **DLY** 端口。

#### 参数依赖关系

此参数仅适用于 COMPH 模块。

### **DAC value (DACH)** — 指定 DAC 值 `0`（默认）

指定内部 DAC 的 DAC 值以在负输入上生成电压。

### **DAC initial value** — 指定 DAC 初始值 `0`（默认）

指定内部 DAC 的 DAC 初始值以在负输入上生成电压。

#### 依赖关系

DAC 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **DAC
  module**
- **Specify DAC/RAMP parameter(s) Via** 设置为
  **输入端口**

### **RAMP reference value** — 指定 RAMP 参考值 `0`（默认）

RAMP 参考值在 0 到 65535 范围内。任何超出范围的值都会被饱和处理。

RAMP 发生器从参考值开始递减。

#### 依赖关系

REF 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **RAMP
  module**
- **Specify DAC/RAMP parameter(s) Via** 设置为
  **Dialog**
- 此端口仅适用于 COMPH 模块。

### **RAMP decrement value** — 指定 RAMP 递减值 `0`（默认）

RAMP 递减值在 0 到 65535 范围内。任何超出范围的值都会被饱和处理。

RAMP 发生器以递减值为步长递减 RAMP 参考值。

#### 依赖关系

DEC 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **RAMP
  module**
- **Specify DAC/RAMP parameter(s) Via** 设置为
  **Dialog**
- 此端口仅适用于 COMPH 模块。

### **RAMP delay value** — 指定 RAMP 延迟值 `0`（默认）

RAMP 延迟值在 0 到 8192 范围内。任何超出范围的值都会被饱和处理。

RAMP 发生器在开始以 RAMP 递减值为步长递减 RAMP 参考值之前等待延迟值。

#### 依赖关系

DLY 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **RAMP
  module**
- **Specify DAC/RAMP parameter(s) via** 设置为
  **Dialog**
- 此端口仅适用于 COMPH 模块。

### **RAMP initial reference value** — 指定 RAMP 初始参考值 `0`（默认）

RAMP 初始参考值在 0 到 65535 范围内。任何超出范围的值都会被饱和处理。

RAMP 发生器从参考值开始递减。

#### 依赖关系

REF 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **RAMP
  module**
- **Specify DAC/RAMP parameter(s) Via** 设置为
  **输入端口**
- 此端口仅适用于 COMPH 模块。

### **RAMP initial decrement value** — 指定 RAMP 递减值 `0`（默认）

RAMP 初始递减值在 0 到 65535 范围内。任何超出范围的值都会被饱和处理。

RAMP 发生器以递减值为步长递减 RAMP 参考值。

#### 依赖关系

DEC 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **RAMP
  module**
- **Specify DAC/RAMP parameter(s) Via** 设置为
  **输入端口**
- 此端口仅适用于 COMPH 模块。

### **RAMP initial delay value** — 指定 RAMP 延迟值 `0`（默认）

RAMP 初始延迟值在 0 到 8192 范围内。任何超出范围的值都会被饱和处理。

RAMP 发生器在开始以 RAMP 递减值为步长递减 RAMP 参考值之前等待延迟值。

#### 依赖关系

DLY 端口仅在以下参数设置时出现：

- **Second input** 设置为 **Internal
  DAC**
- **DAC source select** 设置为 **RAMP
  module**
- **Specify DAC/RAMP parameter(s) via** 设置为
  **输入端口**
- 此端口仅适用于 COMPH 模块。

### **Enable latch output** — 比较器锁存输出 `off`（默认）| `on`

比较器数字滤波器输出的锁存值。

选择此参数以启用 LTH 端口。

### **Enable latch clear** — 清除比较器锁存值 `off`（默认）| on

锁存清除信号用于清除比较器锁存状态信号。任何大于 0 的值都将清除锁存信号。

选择此参数以启用 LCLR 端口。

### **Sample time** — 从比较器读取数据的频率 `0.1`（默认）

使用此参数指定采样之间的时间间隔。要从上游模块继承采样时间，请将此参数设置为 -1。

## 所属库

C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

比较比较器引脚上的两个输入电压

比较器子系统由两个模块组成，比较器高（COMPH）和比较器
低（COMPH）。当第一个输入引脚（正输入）上的电压大于第二个输入引脚（负输入）上的电压时，每个模块生成高数字输出。
当第一个输入引脚（正输入）上的电压小于第二个输入引脚（负输入）上的电压时，每个模块生成低数字输出。

第二个输入引脚可以是外部引脚或 DAC 模块。
