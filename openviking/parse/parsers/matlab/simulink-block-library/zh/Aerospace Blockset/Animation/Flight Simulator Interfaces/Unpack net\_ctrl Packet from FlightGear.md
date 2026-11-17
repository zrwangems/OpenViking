---
type: simulink-block
title: 'Unpack net_ctrl Packet from FlightGear'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'unpacknet_ctrlpacketfromflightgear'
documentation_source_path: 'unpacknet_ctrlpacketfromflightgear.html'
language: zh-CN
chinese_source: worker-translation
---

# Unpack net_ctrl Packet from FlightGear

## 端口
```yaml
ports:
- name: net_ctrl
  summary: 要解包的 FlightGear 数据包 数组
  direction: input
  data_types: uint8
- name: wind_speed_kt
  summary: 风速 标量
  direction: output
  data_types: double
- name: wind_dir_deg
  summary: 风向 标量
  direction: output
  data_types: double
- name: turbulence_norm
  summary: 湍流范数 标量
  direction: output
  data_types: double
- name: temp_c
  summary: 环境温度 标量
  direction: output
  data_types: double
- name: press_inhg
  summary: 环境压力 标量
  direction: output
  data_types: double
- name: hground
  summary: 地面标高 标量
  direction: output
  data_types: double
- name: magvar
  summary: 当地磁差 标量
  direction: output
  data_types: double
- name: icing
  summary: 结冰状态 标量
  direction: output
  data_types: uint32
- name: aileron
  summary: 归一化副翼位置 1 | 标量
  direction: output
  data_types: double
- name: elevator
  summary: 归一化升降舵位置 1 | 标量
  direction: output
  data_types: double
- name: rudder
  summary: 归一化方向舵位置 1 | 标量
  direction: output
  data_types: double
- name: aileron_trim
  summary: 归一化副翼配平位置 标量
  direction: output
  data_types: double
- name: elevator_trim
  summary: 归一化升降舵配平位置 1 | 标量
  direction: output
  data_types: double
- name: rudder_trim
  summary: 归一化方向舵配平位置 1 | 标量
  direction: output
  data_types: double
- name: flaps
  summary: 归一化襟翼位置 1 | 标量
  direction: output
  data_types: double
- name: spoilers
  summary: 归一化扰流板位置 1 | 标量
  direction: output
  data_types: single
- name: speedbrake
  summary: 归一化减速板位置 1 | 标量
  direction: output
  data_types: single
- name: flaps_power
  summary: 襟翼电源 1 | 标量
  direction: output
  data_types: uint32
- name: flap_motor_ok
  summary: 襟翼电机供电 标量
  direction: output
  data_types: uint32
- name: num_engines
  summary: 有效发动机数量 标量
  direction: output
  data_types: uint32
- name: master_bat
  summary: 主电池开关 向量
  direction: output
  data_types: uint32
- name: master_alt
  summary: 主交流发电机开关 向量
  direction: output
  data_types: uint32
- name: magnetos
  summary: 磁电机开关 标量
  direction: output
  data_types: uint32
- name: starter_power
  summary: 启动电机电源 1 | 向量
  direction: output
  data_types: uint32
- name: throttle
  summary: 归一化油门位置 1 | 向量
  direction: output
  data_types: double
- name: mixture
  summary: 归一化混合比杆位置 1 | 向量
  direction: output
  data_types: double
- name: condition
  summary: 归一化状态 1 | 向量
  direction: output
  data_types: uint32
- name: fuel_pump_power
  summary: 归一化减速板位置 1 | 标量
  direction: output
  data_types: uint32
- name: prop_advance
  summary: 螺旋桨前进比 1 | 向量
  direction: output
  data_types: double
- name: feed_tank_to
  summary: 供油油箱切换 向量
  direction: output
  data_types: uint32
- name: reverse
  summary: 反推开关 向量
  direction: output
  data_types: uint32
- name: engine_ok
  summary: 发动机状态指示 向量
  direction: output
  data_types: uint32
- name: mag_left_ok
  summary: 左磁电机状态指示 向量
  direction: output
  data_types: uint32
- name: mag_right_ok
  summary: 右磁电机状态指示 向量
  direction: output
  data_types: uint32
- name: spark_plugs_ok
  summary: 归一化减速板位置 向量
  direction: output
  data_types: uint32
- name: oil_press_status
  summary: 油压状态指示 0 | 1 | 2 | 标量
  direction: output
  data_types: uint32
- name: fuel_pump_ok
  summary: 燃油管理状态指示 向量
  direction: output
  data_types: uint32
- name: num_tanks
  summary: 有效油箱数量 标量
  direction: output
  data_types: uint32
- name: fuel_selector
  summary: 燃油选择器 标量
  direction: output
  data_types: single
- name: xfer_pump
  summary: 指定传输 向量
  direction: output
  data_types: uint32
- name: cross_feed
  summary: 交输阀 标量
  direction: output
  data_types: single
- name: brake_left
  summary: 左刹车踏板位置 飞行员 标量
  direction: output
  data_types: double
- name: brake_right
  summary: 右刹车踏板位置 飞行员 标量
  direction: output
  data_types: double
- name: copilot_brake_left
  summary: 左刹车踏板位置 飞行员 标量
  direction: output
  data_types: double
- name: copilot_brake_right
  summary: 右刹车踏板位置 飞行员 标量
  direction: output
  data_types: double
- name: brake_parking
  summary: 刹车停留位置 标量
  direction: output
  data_types: double
- name: gear_handle
  summary: 起落架手柄位置 标量
  direction: output
  data_types: uint32
- name: master_avionics
  summary: 主航电开关 标量
  direction: output
  data_types: uint32
- name: comm_1
  summary: Comm 1 频率 标量
  direction: output
  data_types: double
- name: comm_2
  summary: Comm 2 频率 标量
  direction: output
  data_types: double
- name: nav_1
  summary: Nav 1 频率 标量
  direction: output
  data_types: double
- name: nav_2
  summary: Nav 2 频率 标量
  direction: output
  data_types: double
```

### 输入

### **net\_ctrl** — 要解包的 FlightGear 数据包 数组

要解包的 FlightGear 数据包，指定为数组。

**数据类型：** `uint8`
### 输出

#### 环境输出

### **wind\_speed\_kt** — 风速 标量

风速，指定为标量，单位为节。

#### 依赖

要启用此端口，请选中 **Show environment
outputs** 复选框。

**数据类型：** `double`

### **wind\_dir\_deg** — 风向 标量

风向，指定为标量，单位为度。

#### 依赖

要启用此端口，请选中 **Show environment
outputs** 复选框。

**数据类型：** `double`

### **turbulence\_norm** — 湍流范数 标量

湍流范数，指定为标量。

#### 依赖

要启用此端口，请选中 **Show environment
outputs** 复选框。

**数据类型：** `double`

### **temp\_c** — 环境温度 标量

环境温度，指定为标量，单位为摄氏度。

#### 依赖

要启用此端口，请选中 **Show environment
outputs** 复选框。

**数据类型：** `double`

### **press\_inhg** — 环境压力 标量

环境压力，指定为标量，单位为 inHg。

#### 依赖

要启用此端口，请选中 **Show environment
outputs** 复选框。

**数据类型：** `double`

### **hground** — 地面标高 标量

地面标高，指定为标量，单位为米。

#### 依赖

要启用此端口，请选中 **Show environment
outputs** 复选框。

**数据类型：** `double`

### **magvar** — 当地磁差 标量

当地磁差，指定为标量。

#### 依赖

要启用此端口，请选中 **Show environment
outputs** 复选框。

**数据类型：** `double`

### **icing** — 结冰状态 标量

结冰状态，指定为标量，单位为度。

#### 依赖

要启用此端口，请选中 **Show environment
outputs** 复选框。

**数据类型：** `uint32`

#### 操纵面位置输入

### **aileron** — 归一化副翼位置 `1` | 标量

归一化副翼位置 [-1,1]，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `double`

### **elevator** — 归一化升降舵位置 `1` | 标量

归一化升降舵位置 [-1,1]，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `double`

### **rudder** — 归一化方向舵位置 `1` | 标量

归一化方向舵位置 [-1,1]，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `double`

### **aileron\_trim** — 归一化副翼配平位置 标量

归一化副翼配平位置 [-1,1]，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `double`

### **elevator\_trim** — 归一化升降舵配平位置 `1` | 标量

归一化升降舵配平位置 [-1,1]，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `double`

### **rudder\_trim** — 归一化方向舵配平位置 `1` | 标量

归一化方向舵配平位置 [-1,1]，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `double`

### **flaps** — 归一化襟翼位置 `1` | 标量

归一化襟翼位置 [-0,1]，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `double`

### **spoilers** — 归一化扰流板位置 `1` | 标量

归一化扰流板位置 [0,1]，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `single`

### **speedbrake** — 归一化减速板位置 `1` | 标量

归一化减速板位置 [0,1]，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `single`

### **flaps\_power** — 襟翼电源 `1` | 标量

襟翼电源，指定为标量。值
`1` 表示电源可用。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `uint32`

### **flap\_motor\_ok** — 襟翼电机供电 标量

襟翼电机供电，指定为标量。

#### 依赖

要启用此端口，请选中 **Show control surface
position outputs** 复选框。

**数据类型：** `uint32`

#### 发动机/燃油输出

### **num\_engines** — 有效发动机数量 标量

有效发动机数量，指定为标量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **master\_bat** — 主电池开关 向量

主电池开关，指定为
向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **master\_alt** — 主交流发电机开关 向量

主交流发电机开关，指定为
向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **magnetos** — 磁电机开关 标量

磁电机开关，指定为标量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **starter\_power** — 启动电机电源 `1` | 向量

启动电机电源，指定为向量。值
`1` 表示电源可用。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **throttle** — 归一化油门位置 `1` | 向量

归一化油门位置 [0,1]，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `double`

### **mixture** — 归一化混合比杆位置 `1` | 向量

归一化混合比杆位置 [0,1]，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `double`

### **condition** — 归一化状态 `1` | 向量

归一化状态 [0,1]，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **fuel\_pump\_power** — 归一化减速板位置 `1` | 标量

燃油泵电源，指定为向量。值
`1` 表示泵已开启。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **prop\_advance** — 螺旋桨前进比 `1` | 向量

螺旋桨前进比 [0,1]，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `double`

### **feed\_tank\_to** — 供油油箱切换 向量

供油油箱切换，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **reverse** — 反推开关 向量

反推开关，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **engine\_ok** — 发动机状态指示 向量

发动机状态指示，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **mag\_left\_ok** — 左磁电机状态指示 向量

左磁电机状态指示，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **mag\_right\_ok** — 右磁电机状态指示 向量

右磁电机状态指示，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **spark\_plugs\_ok** — 归一化减速板位置 向量

火花塞状态指示，指定为向量。值
`0` 表示火花塞已失效。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **oil\_press\_status** — 油压状态指示 `0` | `1` | `2` | 标量

油压状态指示，指定为向量。

- `0` — 油压正常
- `1` — 油压过低
- `2` — 油压失效

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **fuel\_pump\_ok** — 燃油管理状态指示 向量

燃油管理状态指示，指定为向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **num\_tanks** — 有效油箱数量 标量

有效油箱数量，指定为标量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **fuel\_selector** — 燃油选择器 标量

燃油选择器，指定为向量。

- `0` — 关闭
- `1` — 开启

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `single`

### **xfer\_pump** — 指定传输 向量

指定从数组值到油箱的传输，由值指定为
向量。

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `uint32`

### **cross\_feed** — 交输阀 标量

交输阀，指定为标量。

- `0` — 假
- `1` — 开启

#### 依赖

要启用此端口，请选中 **Show engine/fuel
outputs** 复选框。

**数据类型：** `single`

#### 起落架输出

### **brake\_left** — 左刹车踏板位置 飞行员 标量

左刹车踏板位置 飞行员，指定为标量。

#### 依赖

要启用此端口，请选中 **Show landing gear
outputs** 复选框。

**数据类型：** `double`

### **brake\_right** — 右刹车踏板位置 飞行员 标量

右刹车踏板位置 飞行员，指定为标量。

#### 依赖

要启用此端口，请选中 **Show landing gear
outputs** 复选框。

**数据类型：** `double`

### **copilot\_brake\_left** — 左刹车踏板位置 飞行员 标量

左刹车踏板位置 飞行员，指定为标量。

#### 依赖

要启用此端口，请选中 **Show landing gear
outputs** 复选框。

**数据类型：** `double`

### **copilot\_brake\_right** — 右刹车踏板位置 飞行员 标量

右刹车踏板位置 飞行员，指定为标量。

#### 依赖

要启用此端口，请选中 **Show landing gear
outputs** 复选框。

**数据类型：** `double`

### **brake\_parking** — 刹车停留位置 标量

刹车停留位置，指定为标量。

#### 依赖

要启用此端口，请选中 **Show landing gear
outputs** 复选框。

**数据类型：** `double`

### **gear\_handle** — 起落架手柄位置 标量

起落架手柄位置，指定为标量。

- `0` — 起落架手柄收起
- `1` — 起落架手柄放下

#### 依赖

要启用此端口，请选中 **Show landing gear
outputs** 复选框。

**数据类型：** `uint32`

#### 航电输出

### **master\_avionics** — 主航电开关 标量

主航电开关，指定为
标量。

#### 依赖

要启用此端口，请选中 **Show avionic
outputs** 复选框。

**数据类型：** `uint32`

### **comm\_1** — Comm 1 频率 标量

Comm 1 频率，指定为标量，单位为 Hz。

#### 依赖

要启用此端口，请选中 **Show avionic
outputs** 复选框。

**数据类型：** `double`

### **comm\_2** — Comm 2 频率 标量

Comm 2 频率，指定为标量，单位为 Hz。

#### 依赖

要启用此端口，请选中 **Show avionic
outputs** 复选框。

**数据类型：** `double`

### **nav\_1** — Nav 1 频率 标量

Nav 1 频率，指定为标量，单位为 Hz。

#### 依赖

要启用此端口，请选中 **Show avionic
outputs** 复选框。

**数据类型：** `double`

### **nav\_2** — Nav 2 频率 标量

Nav 2 频率，指定为标量，单位为 Hz。

#### 依赖

要启用此端口，请选中 **Show avionic
outputs** 复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Show control surface position outputs
  summary: 操纵面位置输出 off (默认) | on
  group: ''
  block_parameter: ShowControlSurfacePositionOutputs
  type: 字符向量
  values: '''off'' | ''on'''
- name: Show engine/fuel outputs
  summary: 发动机/燃油输出 off (默认) | on
  group: ''
  block_parameter: ShowEngineFuelOutputs
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: 显示起落架输出
  summary: 起落架输出 off（默认）| on
  group: ''
  block_parameter: ShowLandingGearOutputs
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: 显示航电输出
  summary: 航电输出 off（默认）| on
  group: ''
  block_parameter: ShowAvionicOutputs
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: 显示环境输出
  summary: 环境输出 on（默认）| off
  group: ''
  block_parameter: ShowEnvironmentOutputs
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''on'''
- name: 采样时间
  summary: 采样时间 1/30（默认）| 标量
  group: ''
  block_parameter: SampleTime
  type: 字符向量
  values: 标量
  default: '''1/30'''
```

### **Show control surface position outputs** — 操纵面位置输出 `off` (默认) | `on`

选中此复选框以包含来自
FlightGear `net_ctrl` 数据包的操纵面位置输出。

#### 依赖

选中此复选框以启用这些输入端口。

**信号组 1：操纵面位置输出**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`aileron`* | 1 (无量纲) | double | 1 | 归一化副翼位置 [-1,1] |
| *`elevator`* | 1 (无量纲) | double | 1 | 归一化升降舵位置 [-1,1] |
| *`rudder`* | 1 (无量纲) | double | 1 | 归一化方向舵位置 [-1,1] |
| *`aileron_trim`* | 1 (无量纲) | double | 1 | 归一化副翼配平位置 [-1,1] |
| *`elevator_trim`* | 1 (无量纲) | double | 1 | 归一化升降舵配平位置 [-1,1] |
| *`rudder_trim`* | 1 (无量纲) | double | 1 | 归一化方向舵配平位置 [-1,1] |
| *`flaps`* | 1 (无量纲) | double | 1 | 归一化襟翼位置 [-0,1] |
| *`spoilers`* | 1 (无量纲) | double | 1 | 归一化扰流板位置 [0,1] |
| *`speedbrake`* | 1 (无量纲) | double | 1 | 归一化减速板位置 [0,1] |
| *`flaps_power`* | 1 (无量纲) | uint32 | 1 | 襟翼电源（`1` = 电源可用） |
| *`flap_motor_ok`* | — | uint32 | 1 | 襟翼电机供电 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowControlSurfacePositionOutputs` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### **Show engine/fuel outputs** — 发动机/燃油输出 `off` (默认) | `on`

选中此复选框以包含来自
FlightGear `net_ctrl` 数据包的发动机和燃油输出。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 2：发动机/燃油输出**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`num_engines`* | — | uint32 | 1 | 有效发动机数量 |
| *`master_bat`* | — | uint32 | 4 | 主电池开关 |
| *`master_alt`* | — | uint32 | 4 | 主交流发电机开关 |
| *`magnetos`* | — | uint32 | 4 | 磁电机开关 |
| *`starter_power`* | — | uint32 | 4 | 起动机电源（`1` = 起动机电源可用） |
| *`throttle`* | 1（无量纲） | double | 4 | 归一化油门位置 [0,1] |
| *`mixture`* | 1（无量纲） | double | 4 | 归一化混合比杆位置 [0,1] |
| *`condition`* | 1（无量纲） | double | 4 | 归一化状态 [0,1] |
| *`fuel_pump_power`* | — | uint32 | 4 | 燃油泵电源 `1` = 开启） |
| *`prop_advance`* | 1（无量纲） | double | 4 | 螺旋桨前进比 [0,1] |
| *`feed_tank_to`* | — | uint32 | 4 | 供油油箱切换 |
| *`reverse`* | — | uint32 | 4 | 反向开关 |
| *`engine_ok`* | — | uint32 | 4 | 发动机状态指示器 |
| *`mag_left_ok`* | — | uint32 | 4 | 左磁电机状态指示器 |
| *`mag_right_ok`* | — | uint32 | 4 | 右磁电机状态指示器 |
| *`spark_plugs_ok`* | — | uint32 | 4 | 火花塞状态指示器（`0` = 火花塞故障） |
| *`oil_press_status`* | — | uint32 | 4 | 油压状态指示器（0 = 正常，1 = 偏低，2 = 完全失效） |
| *`fuel_pump_ok`* | — | uint32 | 4 | 燃油管理状态指示器 |
| *`num_tanks`* | — | uint32 | 1 | 有效油箱数量 |
| *`fuel_selector`* | — | uint32 | 8 | 燃油选择器。（`0` = 关闭，`1` = 开启） |
| *`xfer_pump`* | — | uint32 | 5 | 指定从数组值传输到由值指定的油箱 |
| *`cross_feed`* | — | uint32 | 1 | 交叉供油阀（`0` = false，`1` = 开启） |

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowEngineFuelOutputs` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **显示起落架输出** — 起落架输出 `off`（默认）| `on`

选中此复选框以包含来自 FlightGear `net_ctrl` 数据包的起落架输出。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 3：起落架输出**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`brake_left`* | — | double | 1 | 左刹车踏板位置（飞行员） |
| *`brake_right`* | — | double | 1 | 右刹车踏板位置（飞行员） |
| *`copilot_brake_left`* | — | double | 1 | 左刹车踏板位置（副驾驶） |
| *`copilot_brake_right`* | — | double | 1 | 右刹车踏板位置（副驾驶） |
| *`brake_parking`* | — | double | 1 | 驻车刹车位置 |
| *`gear_handle`* | — | uint32 | 1 | 起落架手柄位置（`1` = 起落架手柄放下，`0` = 起落架手柄收起） |

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowLandingGearOutputs` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **显示航电输出** — 航电输出 `off`（默认）| `on`

选中此复选框以包含来自 FlightGear `net_ctrl` 数据包的航电输出。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 4：航电输出**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`master_avionics`* | — | uint32 | 1 | 主航电开关 |
| *`comm_1`* | Hz | double | 1 | Comm 1 频率 |
| *`comm_2`* | Hz | double | 1 | Comm 2 频率 |
| *`nav_1`* | Hz | double | 1 | Nav 1 频率 |
| *`nav_2`* | Hz | double | 1 | Nav 2 频率 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowAvionicOutputs` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **显示环境输出** — 环境输出 `on`（默认）| `off`

选中此复选框以包含来自 FlightGear `net_ctrl` 数据包的环境输出。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 5：环境输出**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`wind_speed_kt`* | knot | double | 1 | 风速 |
| *`wind_dir_deg`* | deg | double | 1 | 风向 |
| *`turbulence_norm`* | — | double | 1 | 湍流范数 |
| *`temp_c`* | deg C | double | 1 | 环境温度 |
| *`press_inhg`* | inHg | double | 1 | 环境压力 |
| *`hground`* | m | double | 1 | 地面高程 |
| *`magvar`* | deg | double | 1 | 当地磁差 |
| *`icing`* | – | uint32 | 1 | 结冰状态 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowEnvironmentOutputs` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### **采样时间** — 采样时间 1/30（默认）| 标量

将采样时间（-1 表示继承）指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数**： `SampleTime` |
| **类型**： 字符向量 |
| **值**： 标量 |
| **默认值**： `'1/30'` |
## 所属库

Aerospace Blockset / Animation / Flight Simulator Interfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

解包从 FlightGear 接收的 net_ctrl 变量数据包

Unpack net\_ctrl Packet from FlightGear 模块解包通过 Receive net\_ctrl Packet from FlightGear 模块从 FlightGear 接收的 `net_ctrl` 变量数据包，并使其可用于 Simulink® 环境。

Aerospace Blockset™ 产品支持从 v2.6 开始的 FlightGear 版本。如果您使用的 FlightGear 版本早于 2.6，模型将显示来自 Simulink Upgrade Advisor 的通知。请考虑使用 Upgrade Advisor 升级您的 FlightGear 版本。有关详细信息，请参阅 Supported FlightGear Versions。
