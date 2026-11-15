---
type: simulink-block
title: 'Analog Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'analogoutput'
documentation_source_path: 'freescalefrdmk64fboard/ref/analogoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Output

## 端口

### 输入

### **Port\_1** — 输入信号标量

此模块接受 0 和 +1 之间的值。

当提供 0–1 之间的值时，此模块会向 DAC0\_OUT 引脚输出模拟信号，使得：

    Vout = Vref *[(1+(input*4095))/4096]

Vref 是 DAC 的参考电压，可从 **配置参数** > **硬件实现窗格** > **DAC** > **DAC0 参考电压** 中选择。

**数据类型：** `single` | `double`

## 参数

### **采样时间** — 从输入端口读取值的频率 `0.1` (默认)

指定此模块从输入端口读取值的频率，单位为 seconds。

当将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

将模拟输出信号发送到 DAC0_OUT 引脚

Analog Output 模块将模拟信号发送到板上的 DAC0\_OUT 引脚。

当提供 0–1 之间的值时，此模块会向 DAC0\_OUT 引脚输出模拟信号，使得：

    Vout = Vref *[(1+(input*4095))/4096]

Vref 是 DAC 的参考电压，可从 **配置参数** > **硬件实现窗格** > **DAC** > **DAC0 参考电压** 中选择。

确保在同一模型中仅使用一个 Analog Output 模块。
