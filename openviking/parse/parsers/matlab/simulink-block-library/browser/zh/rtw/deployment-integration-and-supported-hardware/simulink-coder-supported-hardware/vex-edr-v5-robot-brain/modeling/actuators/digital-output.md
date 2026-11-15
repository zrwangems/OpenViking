---
type: simulink-block
title: 'Digital Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Actuators'
documentation_page: 'digitaloutput'
documentation_source_path: 'vexv5/ref/digitaloutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Output

## 端口

### 输入

### **Port\_1** — 设置引脚 `1` | `0` 的逻辑值（1 或 0）

将输入端口连接到生成逻辑值（`1` 或 `0`）的模块。

**数据类型：** `Boolean`

## 参数

### **3-Wire Expander (smart port)** — 选择 3-Wire Expander 使用的 smart port `None`（默认）| `1` 到 `21`

如果使用 3-Wire Expander，请指定 VEX EDR V5 Robot Brain 上该扩展器所连接的 smart port。

### **Port** — 选择要将数字信号发送到的 3-wire 端口 `A`（默认）| `A` 到 `H`

选择 VEX EDR V5 Robot Brain 上要将数字信号发送到的 3-wire 端口。

不要在同一模型中将同一端口分配给多个 Digital Output 模块。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

将逻辑值设置到 VEX EDR V5 Robot Brain 上的 3-wire 端口

Digital Output 模块用于将数字/逻辑值（1 或 0）设置到 VEX® EDR V5 Robot Brain 上所选的 3-wire 端口。
