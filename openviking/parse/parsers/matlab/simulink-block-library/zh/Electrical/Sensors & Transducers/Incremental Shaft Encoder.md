---
type: simulink-block
title: 'Incremental Shaft Encoder'
family: 'sensors-transducers'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'incrementalshaftencoder'
documentation_source_path: 'ref/incrementalshaftencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Incremental Shaft Encoder

## 端口

### 守恒

### **R** — 旋转速度 机械旋转

与传感器正探针关联的机械旋转守恒端口。

### **C** — 旋转速度 机械旋转

与传感器负（参考）探针关联的机械旋转守恒端口。

### **A** — 电压 电气

编码电输出。

### **B** — 电压 电气

编码电输出。

### **Z** — 索引或同步 电气

索引或同步电输出。

### **Ref** — 电压 电气

浮地零伏参考。

## 参数

### **每转脉冲数** — 脉冲计数 `2`（默认）

轴每转一圈在 *A* 和 *B* 每个相位上产生的脉冲数。

### **输出电压幅值** — 电压 `5` `V`（默认）

当输出为高电平时，轴编码器输出电压的幅值。

### **索引脉冲相对于轴初始角度的偏移** — 位置 `0` `deg`（默认）

索引脉冲 *Z* 相对于仿真开始时轴角度的偏移。此参数允许您设置索引脉冲的初始位置。

## 所属库

Simscape / 电气 / 传感器与换能器

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

将角位置转换为电脉冲的行为模型

Incremental Shaft Encoder 模块表示一种将轴的角位置信息转换为电脉冲的设备。该模块在轴每转一圈时在端口 **A** 和 **B** 上产生 *N* 个脉冲，其中 *N* 是您为 **每转脉冲数** 参数指定的值。脉冲 *A* 和 *B* 相位相差 90 度。如果轴沿正方向旋转，则 *A* 超前 *B*。该模块每转一圈在端口 **Z** 上产生一个索引脉冲。*Z* 脉冲的正跳变始终与 *A* 脉冲的正跳变重合，并且 *Z* 脉冲的长度等于 *A* 和 *B* 脉冲的长度。端口 **A**、**B** 和 **Z** 处的电压是相对于 **Ref** 参考端口电压定义的。

如果您需要对轴编码器信号进行建模，以支持解码算法的开发或包含量化效应，请使用此模块。否则，请使用 Simscape™ Foundation 库中的 Ideal Rotational Motion Sensor 模块。

### 假设和限制

- Incremental Shaft Encoder 模块不可线性化。对于需要模型线性化的控制设计研究，请使用 Simscape Foundation 库中的 Ideal Rotational Motion Sensor 模块。
