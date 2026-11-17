---
type: simulink-block
title: 'Log Event'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Profiling'
documentation_page: 'logevent'
documentation_source_path: 'io_ref/logevent.html'
language: zh-CN
chinese_source: worker-translation
---

# Log Event

## 端口
```yaml
ports:
- name: T
  summary: 日志事件触发 1..0
  direction: input
```

### 输入

### **T** — 日志事件触发 `1..0`

当 T（触发输入）从 0 变为 1（上升沿）或从 1 变为 0（下降沿）时，
该模块将参数 **Channel**、**Code** 和
**Value** 所定义的用户自定义简单事件插入到执行性能分析事件流中。

**示例：**  1
## 参数
```yaml
parameters:
- name: Channel
  summary: 事件通道 ID 0（默认）| int
  group: ''
- name: Code
  summary: 事件代码编号 0（默认）| uint32
  group: ''
- name: Value
  summary: 事件值编号 0（默认）| uint32
  group: ''
- name: Trigger type
  summary: 选择触发信号边沿 Rising（默认）| Falling | Either
  group: ''
```

### **Channel** — 事件通道 ID `0`（默认）| int

选择事件通道 ID，例如 `500`。

#### 程序化使用

```
channel
```

### **Code** — 事件代码编号 `0`（默认）| uint32

选择事件代码编号，例如 `200`。

#### 程序化使用

```
code
```

### **Value** — 事件值编号 `0`（默认）| uint32

选择事件值编号，例如 `200`。

#### 程序化使用

```
value
```

### **Trigger type** — 选择触发信号边沿 `Rising`（默认）| `Falling` | `Either`

选择触发该模块的信号变化类型。当 T（触发输入）
从 0 变为 1（Rising）或从 1 变为 9（Falling）时，该模块将参数 **Channel**、
**Code** 和 **Value** 所定义的用户自定义
简单事件插入到执行性能分析
事件流中。

#### 程序化使用

```
trigger
```
## 所属库

Simulink Real-Time / Profiling

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

记录执行性能分析事件

Log Event 模块在被触发时，将用户自定义事件插入到执行
性能分析事件流中。用户自定义事件包括通道 ID、代码
编号和值编号。通道 ID 值的范围为 0 到 1023。
