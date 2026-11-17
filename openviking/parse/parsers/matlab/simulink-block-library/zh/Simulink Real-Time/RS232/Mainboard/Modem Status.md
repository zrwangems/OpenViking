---
type: simulink-block
title: 'Modem Status'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232 / Mainboard'
documentation_page: 'modemstatus'
documentation_source_path: 'io_ref/modemstatus.html'
language: zh-CN
chinese_source: worker-translation
---

# Modem Status

## 端口

### 输出

### **CTS** — 清除发送线路的状态 `true` | `false`

如果为 `true`，则调制解调器已准备好接收数据。

#### 依赖关系

要使此输出可见，请选择 **CTS** 参数。

### **DSR** — 数据装置就绪线路的状态 `true` | `false`

如果为 `true`，则调制解调器已准备好发送和接收数据。

#### 依赖关系

要使此输出可见，请选择 **DSR** 参数。

### **DCD** — 数据载波检测线路的状态 `true` | `false`

如果为 `true`，则调制解调器正在从远程设备接收载波。

#### 依赖关系

要使此输出可见，请选择 **DCD** 参数。

## 参数

### **CTS** — 启用清除发送状态输出 `on`（默认）| `off`

选中此复选框可监视调制解调器的 CTS 线路。

选择此参数可使 `CTS` 端口可见。

#### 编程使用

```
cts
```

### **DSR** — 启用数据装置就绪状态输出 `on`（默认）| `off`

选中此复选框可监视调制解调器的 DSR 线路。

选择此参数可使 `DSR` 端口可见。

#### 编程使用

```
dsr
```

### **DCD** — 启用数据载波检测状态输出 `on`（默认）| `off`

选中此复选框可监视调制解调器的 DCD 线路。

选择此参数可使 `DCD` 端口可见。

#### 编程使用

```
dcd
```

### **Sample time** — 模块的采样时间 `-1`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 编程使用

```
sampletime
```

### **Serial port** — 正在访问的端口 `Legacy Serial Port 1`（默认）| .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

指定用于通信的串行端口。

如果使用 USB 转串行适配器，目标计算机会按照适配器连接到串行设备的顺序将这些适配器检测为 `serusb1`、`serusb2` 等。

如果端口连接没有变化，则端口分配顺序在目标计算机或串行设备的电源循环期间保持不变。

#### 编程使用

|  |
| --- |
| **模块参数**：`port` |

## 所属库

Simulink Real-Time / RS232 / Mainboard

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

返回调制解调器控制线路的状态

Modem Status 模块读取 Speedgoat® 目标计算机上输入调制解调器控制线路的状态。

此模块的输出类型为 `Boolean`。如果输入电压为正，则输出为 true。如果输入电压为负，则输出为 false。
