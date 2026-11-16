---
type: simulink-block
title: 'C28x Watchdog'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'watchdog'
documentation_source_path: 'ref/watchdog.html'
language: zh-CN
chinese_source: official
---

# C28x Watchdog

## 端口

### 输入

### **Input** — 重置 Watchdog 计数器 标量

当输入信号为 `1` 时，计数器复位。

#### 依赖关系

只有当 **Watchdog counter reset source** 设置为**输入端口**时，此参数才会出现。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### **Watchdog 计数器复位源** — Watchdog 计数器复位源 **通过对话框指定** (默认) | **输入端口**

Watchdog 计数器重置源。

- **输入** - 在 Watchdog 模块上创建一个输入端口。当输入信号为 `1` 时，计数器复位。
- **通过对话框指定** - 根据**采样时间**的值重置 Watchdog 定时器。

### **采样时间** — 处理器重置 Watchdog 定时器的频率 `–1` (默认) | 标量

以秒为单位记录该模块的采样时间。要异步执行此模块，请将此参数设置为 `-1`。

#### 依赖关系

只有当 **Watchdog counter reset source** 设置为**通过对话框指定**时，此参数才会出现。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

配置处理器 Watchdog 模块的计数器复位源

该模块配置处理器上 Watchdog 模块的计数器复位源。监控模块配置完成后，如果未定期维护，则会重置系统。
