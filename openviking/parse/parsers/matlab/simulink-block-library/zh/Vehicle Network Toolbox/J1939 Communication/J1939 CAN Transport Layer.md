---
type: simulink-block
title: 'J1939 CAN Transport Layer'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'J1939 Communication'
documentation_page: 'j1939cantransportlayer'
documentation_source_path: 'ug/j1939cantransportlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# J1939 CAN Transport Layer

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Config name
  summary: J1939 网络配置名称 配置列表选项
  group: ''
- name: Device
  summary: CAN 设备 设备列表选项
  group: ''
- name: Bus speed
  summary: CAN 总线速度 250000（默认）| 500000
  group: ''
- name: Sample time
  summary: 仿真刷新率 0.01（默认）| 数值
  group: ''
```

### **Config name** — J1939 网络配置名称 配置列表选项

要与此传输层模块关联的 J1939 Network Configuration 模块的名称。

### **Device** — CAN 设备 设备列表选项

从所有已连接的 CAN 设备中选择的 CAN 设备。

### **Bus speed** — CAN 总线速度 `250000`（默认）| `500000`

CAN 总线的速度，以每秒位数表示，指定为 J1939 协议支持的两种速率之一：250000 或 500000。默认值为 250000。

### **Sample time** — 仿真刷新率 `0.01`（默认）| 数值

仿真刷新率，指定为模块在仿真期间的采样时间。此值定义了 J1939 CAN Transport Layer 模块在仿真期间运行的频率。有关仿真采样时序的信息，请参阅 Timing in Hardware Interface Models。如果该模块位于触发子系统内或继承采样时间，请指定值为 `-1`。您也可以为采样时间指定一个 MATLAB® 变量。默认值为 `0.01` 仿真秒。
## 所属库

Vehicle Network Toolbox / J1939 Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

通过 CAN 传输 J1939 报文

J1939 CAN Transport Layer 模块允许通过 CAN 总线进行 J1939 通信。此模块将用户定义的 J1939 网络配置与已连接的 CAN 设备关联。对于模型中的每个 J1939 Network Configuration 模块，使用一个此模块。

### 其他支持的功能

J1939 通信模块支持使用 Simulink® 加速模式和快速加速模式。使用此功能，您可以加速 Simulink 模型的执行。有关此功能的更多信息，请参阅 Acceleration (Simulink)。

J1939 通信模块还支持具有有限部署能力的代码生成。代码生成需要 Microsoft® C++ 编译器。
