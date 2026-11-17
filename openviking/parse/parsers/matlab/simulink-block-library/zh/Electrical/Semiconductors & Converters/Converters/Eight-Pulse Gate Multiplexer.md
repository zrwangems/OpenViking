---
type: simulink-block
title: 'Eight-Pulse Gate Multiplexer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'eightpulsegatemultiplexer'
documentation_source_path: 'ref/eightpulsegatemultiplexer.html'
language: zh-CN
chinese_source: worker-translation
---

# Eight-Pulse Gate Multiplexer

## 端口
```yaml
ports:
- name: G1
  summary: 栅极控制电压信号 1，V 物理信号
  direction: input
  data_types: double
- name: G2
  summary: 栅极控制电压信号 2，V 物理信号
  direction: input
  data_types: double
- name: G3
  summary: 栅极控制电压信号 3，V 物理信号
  direction: input
  data_types: double
- name: G4
  summary: 栅极控制电压信号 4，V 物理信号
  direction: input
  data_types: double
- name: G5
  summary: 栅极控制电压信号 5，V 物理信号
  direction: input
  data_types: double
- name: G6
  summary: 栅极控制电压信号 6，V 物理信号
  direction: input
  data_types: double
- name: G7
  summary: 栅极控制电压信号 7，V 物理信号
  direction: input
  data_types: double
- name: G8
  summary: 栅极控制电压信号 8，V 物理信号
  direction: input
  data_types: double
- name: G1
  summary: 栅极控制电压信号 1 电气
  direction: input
- name: a
  summary: '*A* 相参考点 电气'
  direction: input
- name: G3
  summary: 栅极控制电压信号 3 电气
  direction: input
- name: b
  summary: '*B* 相参考点 电气'
  direction: input
- name: G5
  summary: 栅极控制电压信号 5 电气
  direction: input
- name: c
  summary: '*C* 相参考点 电气'
  direction: input
- name: G7
  summary: 栅极控制电压信号 7 电气
  direction: input
- name: d
  summary: '*D* 相参考点 电气'
  direction: input
- name: G2
  summary: 栅极控制电压信号 2 电气
  direction: input
- name: G4
  summary: 栅极控制电压信号 4 电气
  direction: input
- name: G6
  summary: 栅极控制电压信号 6 电气
  direction: input
- name: G8
  summary: 栅极控制电压信号 8 电气
  direction: input
- name: L
  summary: 直流参考点 电气
  direction: input
```

### 输入

### **G1** — 栅极控制电压信号 1，V 物理信号

与 Bidirectional DC-DC Converter 模块中第一个开关器件栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`PS`。

**数据类型：** `double`

### **G2** — 栅极控制电压信号 2，V 物理信号

与 Bidirectional DC-DC Converter 模块中第二个开关器件栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`PS`。

**数据类型：** `double`

### **G3** — 栅极控制电压信号 3，V 物理信号

与 Bidirectional DC-DC Converter 模块中第三个开关器件栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`PS`。

**数据类型：** `double`

### **G4** — 栅极控制电压信号 4，V 物理信号

与 Bidirectional DC-DC Converter 模块中第四个开关器件栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`PS`。

**数据类型：** `double`

### **G5** — 栅极控制电压信号 5，V 物理信号

与 Bidirectional DC-DC Converter 模块中第五个开关器件栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`PS`。

**数据类型：** `double`

### **G6** — 栅极控制电压信号 6，V 物理信号

与 Bidirectional DC-DC Converter 模块中第六个开关器件栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`PS`。

**数据类型：** `double`

### **G7** — 栅极控制电压信号 7，V 物理信号

与 Bidirectional DC-DC Converter 模块中第七个开关器件栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`PS`。

**数据类型：** `double`

### **G8** — 栅极控制电压信号 8，V 物理信号

与 Bidirectional DC-DC Converter 模块中第八个开关器件栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`PS`。

**数据类型：** `double`
### 守恒

### **G1** — 栅极控制电压信号 1 电气

与 Bidirectional DC-DC Converter 模块中第一个开关器件栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **a** — *A* 相参考点 电气

与高侧开关器件的 *A* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **G3** — 栅极控制电压信号 3 电气

与 Bidirectional DC-DC Converter 模块中第三个开关器件栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **b** — *B* 相参考点 电气

与高侧开关器件的 *B* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **G5** — 栅极控制电压信号 5 电气

与 Bidirectional DC-DC Converter 模块中第五个开关器件栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **c** — *C* 相参考点 电气

与高侧开关器件的 *C* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **G7** — 栅极控制电压信号 7 电气

与 Bidirectional DC-DC Converter 模块中第七个开关器件栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **d** — *D* 相参考点 电气

与高侧开关器件的 *D* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **G2** — 栅极控制电压信号 2 电气

与 Bidirectional DC-DC Converter 模块中第二个开关器件栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **G4** — 栅极控制电压信号 4 电气

与 Bidirectional DC-DC Converter 模块中第四个开关器件栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **G6** — 栅极控制电压信号 6 电气

与 Bidirectional DC-DC Converter 模块中第六个开关器件栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **G8** — 栅极控制电压信号 8 电气

与 Bidirectional DC-DC Converter 模块中第八个开关器件栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。

### **L** — 直流参考点 电气

与低侧开关器件的直流负连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为
`Electrical`。
## 参数
```yaml
parameters:
- name: Gate-control port
  summary: 栅极控制端口 PS（默认）| Electrical
  group: ''
```

### **Gate-control port** — 栅极控制端口 `PS`（默认）| `Electrical`

是暴露物理信号控制端口还是电气控制端口。
## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

将栅极电压信号多路复用至 Bidirectional DC-DC Converter 模块

Eight-Pulse Gate Multiplexer 模块将栅极电压信号路由至 Bidirectional DC-DC Converter 模块中的八个开关器件。该模块将八个独立的栅极信号多路复用为单个向量。

当您将 **Gate-control port** 参数设置为
`Electrical` 时，该模块会暴露表示电气参考点的守恒端口。这些端口与连接到 Bidirectional DC-DC Converter 模块中高侧开关器件的各相电压以及每个低侧开关器件共用的直流负电压相关联。
