---
type: simulink-block
title: 'Incremental Shaft Encoder'
family: 'sps'
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
```yaml
ports:
- name: R
  summary: 旋转速度 机械旋转
  direction: unspecified
- name: C
  summary: 旋转速度 机械旋转
  direction: unspecified
- name: A
  summary: 电压 电气
  direction: unspecified
- name: B
  summary: 电压 电气
  direction: unspecified
- name: Z
  summary: 索引或同步 电气
  direction: unspecified
- name: Ref
  summary: 电压 电气
  direction: unspecified
```

### 守恒

### **R** — 旋转速度 机械旋转

与传感器正探头关联的机械旋转守恒端口。

### **C** — 旋转速度 机械旋转

与传感器负（参考）探头关联的机械旋转守恒端口。

### **A** — 电压 电气

编码电气输出。

### **B** — 电压 电气

编码电气输出。

### **Z** — 索引或同步 电气

索引（或同步）电气输出。

### **Ref** — 电压 电气

浮零伏参考。
## 参数
```yaml
parameters:
- name: Pulses per revolution
  summary: 脉冲计数 2（默认）
  group: ''
- name: Output voltage amplitude
  summary: 电压 5 V（默认）
  group: ''
- name: Index pulse offset relative to shaft initial angle
  summary: 位置 0 deg（默认）
  group: ''
```

### **Pulses per revolution** — 脉冲计数 `2`（默认）

轴每转在 *A* 和 *B* 各相上产生的脉冲数。

### **Output voltage amplitude** — 电压 `5` `V`（默认）

输出为高电平时轴编码器输出电压的幅值。

### **Index pulse offset relative to shaft initial angle** — 位置 `0` `deg`（默认）

索引脉冲 *Z* 相对于仿真开始时轴角度的偏移量。此参数用于设置索引脉冲的初始位置。
## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

将角位置转换为电气脉冲的行为模型

Incremental Shaft Encoder 模块表示一种将轴角位置信息转换为电气脉冲的设备。该模块在轴每转时在端口 **A** 和 **B** 上产生 *N* 个脉冲，其中 *N* 是您为 **Pulses per revolution** 参数指定的值。脉冲 *A* 和 *B* 相位相差 90 度。如果轴沿正方向旋转，则 *A* 超前 *B*。该模块每转在端口 **Z** 上产生一个索引脉冲。*Z* 脉冲的正跳变始终与 *A* 脉冲的正跳变重合，且 *Z* 脉冲长度等于 *A* 和 *B* 脉冲的长度。端口 **A**、**B** 和 **Z** 处的电压相对于 **Ref** 参考端口电压定义。

如果您需要建模轴编码器信号，以支持解码算法的开发或包含量化效应，请使用此模块。否则，请使用 Simscape™ Foundation 库中的 Ideal Rotational Motion Sensor 模块。

### 假设与限制

- Incremental Shaft Encoder 模块不可线性化。对于需要模型线性化的控制设计研究，请使用 Simscape Foundation 库中的 Ideal Rotational Motion Sensor 模块。
