---
type: simulink-block
title: 'Comparator'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Analog Peripherals'
documentation_page: 'comparator'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/comparator.html'
language: zh-CN
chinese_source: worker-translation
---

# Comparator

## 端口

### 输入

### **Enable** — 使能运行时标量

端口 `Enable` 允许用户在运行时使能比较器模块。

#### 依赖关系

要使能此端口，请选择 **Run time module enable** 参数。

**数据类型：** `uint8` | `uint16`
### 输出

### **result** — 比较器结果标量

该模块输出比较器的结果。

- `0` - +ve 引脚输入大于 -ve 引脚
  输入
- `1` - +ve 引脚输入小于 -ve 引脚输入

**数据类型：** `Boolean`

### **Status** — 比较器状态标量

该模块输出比较器执行状态。

- `0` - 有效结果
- `1` - 无效结果

#### 依赖关系

要使能此端口，请选择 **Run time module enable** 和 **Output status** 参数。

**数据类型：** `Boolean`

## 参数

### **Comparator module** — 选择比较器模块 `COMP1`（默认） | `COMP2` | `COMP3` | `COMP4` | `COMP5` | `COMP6` | `COMP7`

选择用于比较模拟输入的比较器模块。

### **Run time module enable** — 选择以使能比较器 `off`（默认） | `on`

选择 Run time module enable 以在运行时使能比较器。选择此参数会配置 enable 输入端口。

### **Output status** — 比较器输出 `off`（默认） | `on`

选择此参数时，模块会配置 **Status** 输出端口。Status 端口输出比较器的状态。

#### 依赖关系

要使能此参数，请选择 **Run time module enable** 参数。

### **Sample time** — 模块读取引脚值的频率 `-1`（默认） | `non-negative real value`

指定模块读取引脚值的频率（以 seconds 为单位）。输入大于零的值。当将此参数指定为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2023b 中引入**

## 描述

比较外设上的两个模拟输入并提供结果

Comparator 模块比较外设上的两个模拟输入，并提供结果的逻辑值。
