---
type: simulink-block
title: 'PWM'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'pwm'
documentation_source_path: 'beagleboneblue/ref/pwm.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM

## 端口

### 输入

### **Port\_1** — 占空比值标量

有效输入范围为 `0 - 100`。该输入控制方波的占空比。输入值 `0` 将占空比设为 0% 或无功率，而输入值 `100` 将占空比设为 100% 或满功率。中间输入值（例如 `0.333`）将占空比设为 33.3%，或 1/3 功率。超出范围的输入值（例如 `-0.2` 或 `1.2`）输出最小或最大功率。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Pin** — 选择数字输出引脚 GPS\_HEADER\_PIN\_3（默认） | GPS\_HEADER\_PIN\_4

指定模块生成 PWM 信号的数字输出。

要查看板上的引脚映射，请点击 **View pin map**。

在模型中，每个模块必须具有唯一的引脚编号。

### **Frequency** — PWM 信号的频率 2000（默认）

设置 PWM 信号的频率。如果有两个 PWM 模块，请将两个模块设置为相同频率。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

数字输出引脚的脉宽调制

PWM 模块改变数字输出引脚的功率输出。输入值设置在特定周期内数字方波处于 on 状态的时间百分比。此时间百分比称为占空比。
