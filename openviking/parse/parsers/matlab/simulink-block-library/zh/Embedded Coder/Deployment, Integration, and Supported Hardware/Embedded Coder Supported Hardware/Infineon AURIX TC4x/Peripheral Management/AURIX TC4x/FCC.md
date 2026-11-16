---
type: simulink-block
title: 'FCC'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'fcc'
documentation_source_path: 'infineonaurix/ref/fcc.html'
language: zh-CN
chinese_source: worker-translation
---

# FCC

## 端口

### 输入

### **threshold** — 用于比较的阈值标量

在此端口指定用于比较的参考阈值。

#### 依赖项

要启用此端口，请将 **Mode** 参数设置为 `Normal` 或 `Hysteresis`，并选中 **Enable threshold input** 参数。

**数据类型：** `single`

### **stepWidth** — 斜坡的步宽标量

在此端口指定斜坡的步宽。

#### 依赖项

要启用此参数，请将 **Mode** 参数设置为 `Ramp`，并选中 **Enable ramp configuration inputs** 参数。

**数据类型：** `single`

### **stepSize** — 斜坡的步长标量

在此端口指定斜坡的步长。

#### 依赖项

要启用此参数，请将 **Mode** 参数设置为 `Ramp`，并选中 **Enable ramp configuration inputs** 参数。

**数据类型：** `single`

### **rampStart** — 斜坡的起始值标量

在此端口指定斜坡的起始值。

#### 依赖项

要启用此参数，请将 **Mode** 参数设置为 `Ramp`，并选中 **Enable ramp configuration inputs** 参数。

**数据类型：** `single`

### **rampEnd** — 斜坡的结束值标量

在此端口指定斜坡的结束值。

#### 依赖项

要查看此参数，请将 **Mode** 参数选择为 `Ramp`，并确保 **Enable ramp configuration inputs** 参数已启用。

**数据类型：** `single`

### 输出

### **status** — 边界标志的状态 `0` | `1`

模块在阈值更新期间输出边界标志的状态，为以下值之一：

- `0 —` 边界标志未激活
- `1 —` 边界标志已激活

**数据类型：** `Boolean`

### **threshold** — 斜坡模式下的最终阈值标量

此端口返回 FCC 在斜坡模式结束时达到的阈值。

#### 依赖项

要启用此端口，请将 **Mode** 参数设置为 `Ramp`，并选中 **Enable threshold output** 参数。

**数据类型：** `single`

## 参数

### **Mode** — 阈值更新的操作模式 `Normal`（默认） | `Hysteresis` | `Ramp`

选择以下操作模式之一：

- `Normal—` 将阈值参考值与模拟输入信号进行比较。如果启用 **Enable threshold input** 参数，则比较器使用阈值，直到发生硬件或软件触发。如果未启用，模块将初始阈值设置为 5V。
- `Hysteresis—` 将上限和下限阈值与模拟输入信号进行比较。在此模式下，你可以使用阈值触发或软件触发事件更新新的阈值限值。
- `Ramp—` 将斜坡阈值信号与模拟输入信号进行比较。你可以配置斜坡信号的起始值、结束值、步长（表示每一步的电压增量）和步宽（表示每一步的时间增量）。使用以下情况控制斜坡模式的开始和结束：

  - 在软件触发时启动斜坡，并在达到 End of Threshold Value (ETV) 时结束
  - 在软件触发时启动斜坡，并在收到硬件触发或达到 ETV 值时结束
  - 在软件触发时启动斜坡，并在边界标志转换或达到 ETV 值时结束
  - 在硬件触发时启动斜坡，并在达到 ETV 值时结束
  - 在硬件触发时启动斜坡，并在收到另一个硬件触发或达到 ETV 值时结束

  你可以使用此操作模式在系统软启动或掉电操作期间控制输入信号行为，而无需软件干预。

`Normal`、`Hysteresis` 或 `Ramp`。

选择操作模式会启用 FCC Peripheral Configuration 中 **Threshold** 选项卡中的选项。

### **Enable threshold input** — 启用 threshold 输入的选项 `on`（默认） | `off`

选中此参数以配置 **threshold** 输入端口。

#### 依赖项

要启用此参数，请将 **Mode** 参数设置为 `Normal` 或 `Hysteresis`。

### **Enable ramp configuration inputs** — 启用斜坡配置输入端口的选项 `on`（默认） | `off`

选中此参数以启用用于配置斜坡模式的输入端口。

选中此参数后，模块会配置 **stepWidth**、**stepSize**、**rampStart** 和 **rampEnd** 输入端口。

#### 依赖项

要启用此参数，请将 **Mode** 参数设置为 `Ramp`。

### **Enable threshold output** — 启用 threshold 输出的选项 `on`（默认） | `off`

选中此参数以配置 **threshold** 输出端口。

#### 依赖项

要启用此参数，请将 **Mode** 参数设置为 `Ramp`。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

检测模拟输入信号何时越过 10 位阈值

FCC 模块对快速比较比较器 (FCC) 进行建模，该比较器检测模拟输入信号的值交叉何时越过可编程 10 位阈值。该模块将边界标志的状态输出为 Boolean 值。
