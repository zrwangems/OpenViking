---
type: simulink-block
title: 'Pack net_fdm Packet for FlightGear'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'packnet_fdmpacketforflightgear'
documentation_source_path: 'packnet_fdmpacketforflightgear.html'
language: zh-CN
chinese_source: worker-translation
---

# Pack net_fdm Packet for FlightGear

## 端口

### 输入

#### 位置/姿态输入

### **l** — 经度标量

经度，指定为标量，单位为 rad。

#### 依赖关系

要启用此端口，请选中 **Show position/attitude inputs** 复选框。

**数据类型：** `double`

### **μ** — 纬度标量

纬度，指定为标量，单位为 rad。

#### 依赖关系

要启用此端口，请选中 **Show position/attitude inputs** 复选框。

**数据类型：** `double`

### **h** — 高度标量

高度，指定为标量，单位为 m。

#### 依赖关系

要启用此端口，请选中 **Show position/attitude inputs** 复选框。

**数据类型：** `double`

### **ϕ** — 滚转角标量

滚转角，指定为标量，单位为 rad。

#### 依赖关系

要启用此端口，请选中 **Show position/attitude inputs** 复选框。

**数据类型：** `single`

### **θ** — 俯仰角标量

俯仰角，指定为标量，单位为 rad。

#### 依赖关系

要启用此端口，请选中 **Show position/attitude inputs** 复选框。

**数据类型：** `single`

### **ψ** — 偏航角标量

偏航角，指定为标量，单位为 rad。

#### 依赖关系

要启用此端口，请选中 **Show position/attitude inputs** 复选框。

**数据类型：** `single`

#### 速度/加速度输入

### **α** — 迎角标量

迎角，指定为标量，单位为 rad。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **β** — 侧滑角标量

侧滑角，指定为标量，单位为 rad。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **dφ/dt** — 滚转角速率标量

滚转角速率，指定为标量，单位为 rad/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **dθ/dt** — 俯仰角速率标量

俯仰角速率，指定为标量，单位为 rad/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **dψ/dt** — 偏航角速率标量

偏航角速率，指定为标量，单位为 rad/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **Vcas** — 校准空速标量

校准空速，指定为标量，单位为 knots。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **climb\_rate** — 爬升率标量

爬升率，指定为标量，单位为 feet/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **vnorth** — 机体坐标系中的北向速度标量

机体坐标系中的北向速度，指定为标量，单位为 ft/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **veast** — 机体坐标系中的东向速度标量

机体坐标系中的东向速度，指定为标量，单位为 feet/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **vdown** — 下降速度标量

下降速度，指定为标量，单位为 feet/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **vwind body north** — 相对于当地气团的机体坐标系北向速度标量

相对于当地气团的机体坐标系北向速度，指定为标量，单位为 ft/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **vwind body east** — 相对于当地气团的机体坐标系东向速度标量

相对于当地气团的机体坐标系东向速度，指定为标量，单位为 ft/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **vwind body down** — 相对于气团的机体坐标系下降速度标量

相对于气团的机体坐标系下降速度，指定为标量，单位为 ft/sec。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **AX pilot** — 机体坐标系 *X* 加速度标量

机体坐标系 *X* 加速度，指定为标量，单位为 ft/sec2。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **AY pilot** — 机体坐标系 *Y* 加速度标量

机体坐标系 *Y* 加速度，指定为标量，单位为 ft/sec2。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **AZ pilot** — 机体坐标系 *Z* 加速度标量

机体坐标系 *Z* 加速度，指定为标量，单位为 ft/sec2。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **stall\_warning** — 失速量标量

失速量 [0-1]，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

### **slip\_degree** — 侧滑球偏转标量

侧滑球偏转，指定为标量，单位为 degrees。

#### 依赖关系

要启用此端口，请选中 **Show velocity/acceleration inputs** 复选框。

**数据类型：** `single`

#### 控制面位置输入

### **elevator** — 归一化升降舵位置标量

归一化升降舵位置，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

### **elevator\_trim\_tab** — 归一化升降舵调整片位置标量

归一化升降舵调整片位置，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

### **left\_flap** — 归一化左襟翼位置标量

归一化左襟翼位置，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

### **right\_flap** — 归一化右襟翼位置标量

归一化右襟翼位置，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

### **left\_aileron** — 归一化左副翼位置标量

归一化左副翼位置。指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

### **right\_aileron** — 归一化右副翼位置标量

归一化右副翼位置，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

### **rudder** — 归一化方向舵位置标量

归一化方向舵位置，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

### **nose\_wheel** — 归一化前轮位置标量

归一化前轮位置，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

### **speedbrake** — 归一化减速板位置标量

归一化减速板位置，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

### **spoilers** — 归一化扰流板位置标量

归一化扰流板位置，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show control surface position inputs** 复选框。

**数据类型：** `single`

#### 发动机/燃油输入

### **num\_engines** — 发动机数量标量

发动机数量，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `uint32`

### **eng\_state** — 发动机状态向量

发动机状态（off、cranking、running），指定为向量。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `uint32`

### **rpm** — 发动机 RPM 向量

发动机 RPM，指定为向量，单位为 rev/min。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

### **fuel\_flow** — 燃油流量向量

燃油流量，指定为向量，单位为 gal/hr。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

### **fuel\_px** — 燃油压力向量

燃油压力，指定为向量，单位为 psi。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

### **egt** — 排气温度向量

排气温度，指定为向量，单位为 deg F。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

### **cht** — 气缸头温度标量

气缸头温度，指定为向量，单位为 deg F。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

### **mp\_osi** — 歧管压力向量

歧管压力，指定为向量，单位为 psi。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

### **tit** — 涡轮入口温度向量

涡轮入口温度，指定为向量，单位为 deg F。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

### **oil\_temp** — 油温向量

油温，指定为向量，单位为 deg F。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

### **oil\_px** — 油压向量

油压，指定为向量，单位为 psi。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

### **num\_tanks** — 燃油箱数量标量

燃油箱数量，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `uin32`

### **fuel\_quantity** — 每个燃油箱的燃油量向量

每个燃油箱的燃油量，指定为向量，单位为 gal。

#### 依赖关系

要启用此端口，请选中 **Show engine/fuel inputs** 复选框。

**数据类型：** `single`

#### 起落架输入

### **num\_wheels** — 车轮数量标量

车轮数量，指定为标量。

#### 依赖关系

要启用此端口，请选中 **Show landing gear inputs** 复选框。

**数据类型：** `uint32`

### **wow** — 轮载开关向量

轮载开关，指定为向量。

#### 依赖关系

要启用此端口，请选中 **Show landing gear inputs** 复选框。

**数据类型：** `uint32`

### **gear\_pos** — 起落架归一化位置向量

起落架归一化位置，指定为向量。

#### 依赖关系

要启用此端口，请选中 **Show landing gear inputs** 复选框。

**数据类型：** `single`

### **gear\_steer** — 起落架归一化转向向量

起落架归一化转向，指定为向量。

#### 依赖关系

要启用此端口，请选中 **Show landing gear inputs** 复选框。

**数据类型：** `single`

### **gear\_compression** — 起落架归一化压缩向量

起落架归一化压缩，指定为向量。

#### 依赖关系

要启用此端口，请选中 **Show landing gear inputs** 复选框。

**数据类型：** `single`

#### 环境输入

### **agl** — 离地高度标量

离地高度，指定为标量，单位为 m。

#### 依赖关系

要启用此端口，请选中 **Show environment inputs** 复选框。

**数据类型：** `single`

### **cur\_time** — 当前 UNIX® 时间标量

当前 UNIX 时间，指定为标量，单位为 sec。

#### 依赖关系

要启用此端口，请选中 **Show environment inputs** 复选框。

**数据类型：** `uint32`

### **warp** — 相对于 UNIX 时间的偏移秒数标量

相对于 UNIX 时间的偏移秒数，指定为标量，单位为 sec。

#### 依赖关系

要启用此端口，请选中 **Show environment inputs** 复选框。

**数据类型：** `int32`

### **visibility** — 能见度标量

能见度（用于视觉效果），指定为标量，单位为 m。

#### 依赖关系

要启用此端口，请选中 **Show environment inputs** 复选框。

**数据类型：** `single`

### 输出

### **net\_fdm** — 为 FlightGear 生成的包数组

为 FlightGear 生成的包，指定为数组。

**数据类型：** `single` | `double` | `uint32`

## 参数

### **Show position/altitude inputs** — 位置和高度输入 `on`（默认） | `off`

选中此复选框可在 FlightGear `net_fdm` 数据包中包括位置和高度输入。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 1：位置/高度输入**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`longitude`* | rad | double | 1 | 大地经度 |
| *`latitude`* | rad | double | 1 | 大地纬度 |
| *`altitude`* | m | double | 1 | 海平面以上的高度 |
| *`theta`* | rad | single | 1 | 俯仰角 |
| *`phi`* | rad | single | 1 | 滚转角 |
| *`psi`* | rad | single | 1 | 偏航角 |

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowPositionAttitudeInputs` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### **Show velocity/acceleration inputs** — 速度/加速度输入 `off`（默认） | `on`

选中此复选框可在 FlightGear `net_fdm` 数据包中包括速度/加速度输入。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 2：速度/加速度输入**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`alpha`* | rad | double | 1 | 迎角 |
| *`beta`* | rad | single | 1 | 侧滑角 |
| *`dphi/dt`* | rad/sec | single | 1 | 滚转角速率 |
| *`dtheta/dt`* | rad/sec | single | 1 | 俯仰角速率 |
| *`dpsi/dt`* | rad/sec | single | 1 | 偏航角速率 |
| *`Vcas`* | knot | single | 1 | 校准空速 |
| *`climb_rate`* | feet/sec | single | 1 | 爬升率 |
| *`v_north`* | feet/sec | single | 1 | 机体坐标系中的北向速度 |
| *`v_east`* | feet/sec | single | 1 | 机体坐标系中的东向速度 |
| *`v_down`* | feet/sec | single | 1 | 下降速度 |
| *`v_wind_body_north`* | feet/sec | single | 1 | 相对于当地气团的机体坐标系北向速度 |
| *`v_wind_body_east`* | feet/sec | single | 1 | 相对于当地气团的机体坐标系东向速度 |
| *`v_wind_body_down`* | feet/sec | single | 1 | 相对于气团的机体坐标系下降速度 |
| *`Axpilot`* | feet/sec2 | single | 1 | 机体坐标系 *X* 加速度 |
| *`Aypilot`* | feet/sec2 | single | 1 | 机体坐标系 *Y* 加速度 |
| *`Azpilot`* | feet/sec2 | single | 1 | 机体坐标系 *Z* 加速度 |
| *`stall_warning`* | — | single | 1 | 失速量 [0-1] |
| *`slip_deg`* | degrees | single | 1 | 侧滑球偏转 |

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowVelocityAccelerationInputs` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Show control surface position inputs** — 控制面位置输入 `off`（默认） | `on`

选中此复选框可在 FlightGear `net_fdm` 数据包中包括控制面位置输入。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 3：控制面位置输入**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`elevator`* | 1 (dimensionless) | single | 1 | 归一化升降舵位置 |
| *`elevator_trim_tab`* | 1 (dimensionless) | single | 1 | 归一化升降舵调整片位置 |
| *`left_flap`* | 1 (dimensionless) | single | 1 | 归一化左襟翼位置 |
| *`right_flap`* | 1 (dimensionless) | single | 1 | 归一化右襟翼位置 |
| *`left_aileron`* | 1 (dimensionless) | single | 1 | 归一化左副翼位置 |
| *`right_aileron`* | 1 (dimensionless) | single | 1 | 归一化右副翼位置 |
| *`rudder`* | 1 (dimensionless) | single | 1 | 归一化方向舵位置 |
| *`nose_wheel`* | 1 (dimensionless) | single | 1 | 归一化前轮位置 |
| *`speedbrake`* | 1 (dimensionless) | single | 1 | 归一化减速板位置 |
| *`spoilers`* | 1 (dimensionless) | single | 1 | 归一化扰流板位置 |

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowControlSurfacePositionInputs` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Show engine/fuel inputs** — 发动机/燃油输入 `off`（默认） | `on`

选中此复选框可在 FlightGear `net_fdm` 数据包中包括发动机/燃油输入。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 4：发动机/燃油输入**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`num_engines`* | — | uint32 | 1 | 发动机数量 |
| *`eng_state`* | — | uint32 | 4 | 发动机状态（off、cranking、running） |
| *`rpm`* | rev/min | single | 4 | 发动机 RPM |
| *`fuel_flow`* | gal/hour | single | 4 | 燃油流量 |
| *`fuel_px`* | psi | single | 4 | 燃油压力 |
| *`egt`* | deg F | single | 4 | 排气温度 |
| *`cht`* | deg F | single | 4 | 气缸头温度 |
| *`mp_osi`* | psi | single | 4 | 歧管压力 |
| *`tit`* | deg F | single | 4 | 涡轮入口温度 |
| *`oil_temp`* | deg F | single | 4 | 油温 |
| *`oil_px`* | psi | single | 4 | 油压 |
| *`num_tanks`* | — | uint32 | 1 | 燃油箱数量 |
| *`fuel_quantity`* | gal | single | 4 | 每个燃油箱的燃油量 |

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowEngineFuelInputs` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Show landing gear inputs** — 起落架输入 `off`（默认） | `on`

选中此复选框可在 FlightGear `net_fdm` 数据包中包括起落架输入。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 5：起落架输入**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`num_wheels`* | — | uint32 | 1 | 车轮数量 |
| *`wow`* | — | uint32 | 3 | 轮载开关 |
| *`gear_pos`* | — | single | 3 | 起落架归一化位置 |
| *`gear_steer`* | — | single | 3 | 起落架归一化转向 |
| *`gear_compression`* | — | single | 3 | 起落架归一化压缩 |

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowLandingGearInputs` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Show environment inputs** — 环境输入 `off`（默认） | `on`

选中此复选框可在 FlightGear `net_fdm` 数据包中包括环境输入。

#### 依赖关系

选中此复选框以启用这些输入端口。

**信号组 6：环境输入**

| 名称 | 单位 | 类型 | 宽度 | 描述 |
| --- | --- | --- | --- | --- |
| *`agl`* | m | single | 1 | 离地高度 |
| *`cur_time`* | sec | uint32 | 1 | 当前 UNIX 时间 |
| *`warp`* | sec | int32 | 1 | 相对于 UNIX 时间的偏移秒数 |
| *`visibility`* | m | single | 1 | 能见度，单位为米（用于视觉效果） |

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowEnvironmentInputs` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Sample time** — 采样时间 `1/30`（默认） | scalar

指定采样时间（-1 表示继承）。

#### 编程用法

|  |
| --- |
| **模块参数**： `SampleTime` |
| **类型**： character vector |
| **值**： scalar |
| **默认值**： `'1/30'` |

## 所属库

Aerospace Blockset / Animation / Flight Simulator Interfaces

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

为 FlightGear 生成 net_fdm 数据包

Pack net\_fdm Packet for FlightGear 模块根据单独输入创建与特定版本 FlightGear 飞行模拟器兼容的 FlightGear `net_fdm` 数据包。此模块接受 FlightGear `net_fdm` 数据包支持的所有信号。这些信号分为六组：

- 位置/姿态输入
- 速度/加速度输入
- 控制面位置输入
- 发动机/燃油输入
- 起落架输入
- 环境输入

要启用或禁用这些组的输入，请选择关联的模块参数。模块输入端口会根据请求的信号组而变化。对于属于非活动信号组的包值，模块会插入零。

Aerospace Blockset™ 产品支持从 v2.6 开始的 FlightGear 版本。如果您使用的 FlightGear 版本早于 2.6，模型会显示来自 Simulink® Upgrade Advisor 的通知。请考虑使用 Upgrade Advisor 升级您的 FlightGear 版本。有关详细信息，请参阅支持的 FlightGear 版本。
