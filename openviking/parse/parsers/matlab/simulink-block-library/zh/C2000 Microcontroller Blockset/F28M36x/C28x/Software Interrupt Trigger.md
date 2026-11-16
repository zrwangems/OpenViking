---
type: simulink-block
title: 'C28x Software Interrupt Trigger'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c28xsoftwareinterrupttrigger'
documentation_source_path: 'ref/c28xsoftwareinterrupttrigger.html'
language: zh-CN
chinese_source: official
---

# C28x Software Interrupt Trigger

## 端口

### 输入

### **PIEIFRx.INTy** — 触发软件中断 标量

当输入值大于 **Trigger software interrupt when input value is greater than** 参数中的值时，Software Interrupt Trigger 模块会根据 **CUP interrupt number** 和 **PIE interrupt number** 参数触发软件中断。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### **CPU 中断编号** — CPU 中断号与硬件中断相对应 `7` (默认) | 标量

输入一个整数值，设置与硬件中断对应的 CPU 中断号。有关 C2000 处理器的 CPU 编号的信息，请参阅 C28x Hardware Interrupt。

### **PIE 中断编号** — 与硬件中断对应的 PIE 中断号 `8` (默认) | 标量

输入一个整数值来设置与硬件中断对应的 PIE 编号。有关 C2000 处理器的 PIE 编号的信息，请参阅 C28x Hardware Interrupt。

### **Trigger software interrupt when input value is greater than** — 设置高于该值时，模块会发出中断。 `0` (默认) | 标量

输入指示中断是由请求例程发出的电平值。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

生成软件触发的不可屏蔽中断

当您将 Software Interrupt Trigger 模块添加到模型中时，该模块会轮询输入端口上的值。当输入值大于 **Trigger software interrupt when input value is greater than** 参数中的值时，该模块会将与所选 CPU 和外设中断扩展 (PIE) 编号对应的中断发布到模型中的 Hardware Interrupt 模块。

要使用此模块，请将 Hardware Interrupt 模块添加到您的模型中。Hardware Interrupt 模块将此模块中由软件触发的中断处理成处理器上的中断服务例程。将 Hardware Interrupt 模块中的中断号设置为您在 Software Interrupt Trigger 模块中设置的值。

CPU 和 PIE 中断号共同指定单个外围模块的单个中断。有关 CPU 和 PIE 中断号到这些外围中断的映射信息，请参阅 C28x Hardware Interrupt。

**注意**

Software Interrupt Trigger 模块不支持定点输入。
