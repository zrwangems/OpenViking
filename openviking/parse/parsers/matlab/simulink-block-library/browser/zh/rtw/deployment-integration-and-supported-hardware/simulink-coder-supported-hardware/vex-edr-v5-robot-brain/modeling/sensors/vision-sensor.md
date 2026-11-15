---
type: simulink-block
title: 'Vision Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'visionsensor'
documentation_source_path: 'vexv5/ref/visionsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Vision Sensor

## 端口

### 输出

### **Object count** — V5 Vision Sensor 检测到的对象数量 [1,10]

V5 Vision Sensor 基于所选 `Color signature` 的 ID 检测到的对象（颜色斑块）数量。一个 Vision Sensor 模块可用于基于所选 ID 检测最多 10 个对象。

#### 依赖关系

此输出取决于为 **Maximum no. of objects** 参数选择的值。

**数据类型:** `double`

### **X** — 检测到的颜色斑块基于视场的 X 坐标 pixels | vector

基于视场的颜色斑块（对象）的 x 坐标，以 pixels 为单位，由 V5 Vision Sensor 检测得到。如果检测到多个对象（例如 `n` 个），则此输出为 1-by-`n` 的值数组。

**数据类型:** `double`

### **Y** — 检测到的颜色斑块基于视场的 Y 坐标 pixels | vector

基于视场的颜色斑块（对象）的 y 坐标，由 V5 Vision Sensor 检测得到。如果检测到多个对象（例如 `n` 个），则此输出为 1-by-`n` 的值数组。

**数据类型:** `double`

### **Width** — 检测到的颜色斑块的视场宽度 pixels | vector

由 V5 Vision Sensor 检测到的颜色斑块的视场宽度。如果检测到多个对象（例如 `n` 个），则此输出为 1-by-`n` 的值数组。

**数据类型:** `double`

### **Height** — 检测到的颜色斑块的视场高度 pixels | vector

由 V5 Vision Sensor 检测到的颜色斑块的视场高度。如果检测到多个对象（例如 `n` 个），则此输出为 1-by-`n` 的值数组。

**数据类型:** `double`

## 参数

### **Smart Port** — 选择 V5 Vision Sensor 连接的 Smart Port 1（默认） | `1` 到 `21`

选择 VEX EDR V5 Robot Brain 上 V5 Vision Sensor 所连接的 Smart Port。VEX EDR V5 Robot Brain 上有 21 个 Smart Port 可供连接 V5 Vision Sensor。

对于模型中的每个模块，Smart Port 必须唯一。如果使用多个具有相同端口的 Vision Sensor 模块，则只有最后执行的 Vision Sensor 模块可能处于活动状态。

### **Color Signature** — 用于检测对象的颜色签名 ID `SIG_1`（默认）

选择颜色签名的 ID（您使用 VEX Vision Utility 配置的 ID）以检测对象。该 ID 对应于颜色签名在 Vision Utility 中出现的顺序，而与您为特定签名提供的名称无关。

### **Max no. of objects** — V5 Vision Sensor 应尝试检测的最大对象数量 `1`（默认）

根据所选 `Color signature` 的 ID，选择 V5 Vision Sensor 应尝试检测的最大对象数量。

### **Enable display on VEX V5 Brain** — 在 VEX V5 Robot Brain 的 LCD 屏幕上启用检测到的对象的显示 `1`（默认）

选择此选项可启用对象（由 V5 Vision Sensor 检测到的）在 VEX V5 Robot Brain 的 LCD 屏幕上的显示。LCD 屏幕中显示的颜色斑块大小对应于对象与 V5 Vision Sensor 的距离。

### **Sample time** — 模块读取值的时间间隔 `0.2`（默认） | positive scalar | -1

输入模块从 V5 Vision Sensor 读取值的时间间隔。

将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

### 启动 V5 Vision Utility

要配置您在 Vision Sensor 模块中指定的颜色签名，您需要使用 VEX Vision Utility。在模块封装中点击 **Launch V5 Vision Utility** 以启动 Vision Utility。

有关使用 VEX Vision Utility 将颜色签名保存到 V5 Vision Sensor 的详细信息，请参阅 Train V5 Vision Sensor for Color Signature。

### 可视化检测到的对象

要在 VEX V5 robot brain 上可视化检测到的对象，请在 Vision Sensor 模块上选择 **Enable display on VEX V5 Brain**。

下面显示了由 Vision Sensor 检测到的对象的示例屏幕。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

表示已连接的 V5 Vision Sensor 并读取颜色斑块（对象）的坐标

Vision Sensor 模块表示连接到 VEX® EDR V5 Robot Brain 上指定端口的 V5 Vision Sensor，并读取由 V5 Vision Sensor 检测到的颜色斑块（对象）的坐标。要检测的颜色斑块取决于您在此模块中选择的颜色签名的 ID。

要配置颜色签名，请参阅启动 V5 Vision Utility。
