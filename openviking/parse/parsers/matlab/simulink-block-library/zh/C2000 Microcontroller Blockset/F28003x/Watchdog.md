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
chinese_source: worker-translation
---

# C28x Watchdog

## 端口
```yaml
ports:
- name: Input
  summary: 复位看门狗计数器 标量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
```

### 输入

### **Input** — 复位看门狗计数器 标量

当输入信号为 `1` 时，计数器被复位。

#### 依赖

此参数仅在 **Watchdog counter reset source** 设置为 `Input port` 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
## 参数
```yaml
parameters:
- name: Watchdog counter reset source
  summary: 看门狗计数器复位源 Specify via dialog（默认）| Input port
  group: ''
- name: Sample time
  summary: 处理器复位看门狗定时器的频率 –1（默认）| 标量
  group: ''
```

### **Watchdog counter reset source** — 看门狗计数器复位源 `Specify via dialog`（默认）| `Input port`

看门狗计数器复位源。

- `Input` — 在看门狗模块上创建一个输入端口。当输入信号为 `1` 时，计数器被复位。
- `Specify via dialog` — 看门狗定时器根据 **Sample time** 值进行复位。

### **Sample time** — 处理器复位看门狗定时器的频率 `–1`（默认）| 标量

模块的采样时间，以秒为单位。要异步执行此模块，请将此参数设置为 `-1`。

#### 依赖

此参数仅在 **Watchdog counter reset source** 设置为 `Specify via dialog` 时出现。
## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

配置处理器看门狗模块的计数器复位源

此模块配置处理器上看门狗模块的计数器复位源。配置后，看门狗模块如果未被定期维护，将复位系统。
