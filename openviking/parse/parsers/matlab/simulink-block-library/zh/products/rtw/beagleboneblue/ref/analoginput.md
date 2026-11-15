---
type: simulink-block
title: 'Analog Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'analoginput'
documentation_source_path: 'beagleboneblue/ref/analoginput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input

## 端口

### 输出

### **Port\_1** — 模拟输入引脚的电压 标量

测量 BeagleBone® Blue 硬件上模拟引脚相对于模拟输入参考电压的电压。如果测得电压等于地电压，则该模块在 raw 模式下输出 `0`，在 volt 模式下输出 `0`。
如果测得电压等于模拟参考电压，则该模块在 raw 模式下输出 `4096`，在 volt 模式下输出 `1.8`。

**数据类型：** `double`

## 参数

### **Pin** — 模拟输入引脚的引脚编号 AIN0 (默认) | AIN1 | AIN2 | AIN3 | LIPO Battery | DC Jack

指定引脚编号。

要打开引脚映射表，请点击 **View pin map**。

确保为模型的不同模块分配不同的引脚编号。

### **Mode** — 读取输出电压的模式 Raw (默认) | Volt

- Raw - 该模块将电压输出为 12-bit 数字值。
- Volt - 该模块以 volts 为单位输出电压

### **Sample time** — 模块读取输入引脚值的频率 0.1 (默认)

指定此模块测量模拟输入引脚电压的频率，以 seconds 为单位。

当将此参数指定为`-1`时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

测量指定模拟输入引脚的电压

此模块测量指定模拟输入引脚的电压。该模块将测量值输出为 double 值。
