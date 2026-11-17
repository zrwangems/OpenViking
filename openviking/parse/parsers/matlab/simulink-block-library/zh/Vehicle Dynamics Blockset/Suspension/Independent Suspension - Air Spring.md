---
type: simulink-block
title: 'Independent Suspension - Air Spring'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Suspension'
documentation_page: 'independentsuspensionairspring'
documentation_source_path: 'ref/independentsuspensionairspring.html'
language: zh-CN
chinese_source: worker-translation
---

# Independent Suspension - Air Spring

## 端口
```yaml
ports:
- name: WhlPz
  summary: 车轮 z 轴位移数组
  direction: input
- name: WhlRe
  summary: 车轮有效半径数组
  direction: input
- name: WhlVz
  summary: 车轮 z 轴速度数组
  direction: input
- name: WhlFx
  summary: 作用于车辆上的车轮纵向力数组
  direction: input
- name: WhlFy
  summary: 作用于车辆上的车轮侧向力数组
  direction: input
- name: WhlM
  summary: 车轮阵列上的悬架力矩
  direction: input
- name: VehP
  summary: 车辆位移阵列
  direction: input
- name: VehV
  summary: 车辆速度数组
  direction: input
- name: StrgAng
  summary: 转向角，可选数组
  direction: input
- name: Pressure
  summary: 空气弹簧中的压力数组
  direction: input
- name: Info
  summary: 总线信号总线
  direction: output
- name: VehF
  summary: 作用在车辆上的悬架力 array
  direction: output
- name: VehM
  summary: 作用在车辆上的悬架力矩 array
  direction: output
- name: WhlF
  summary: 车轮上的悬架力 array
  direction: output
- name: WhlV
  summary: 车轮速度 array
  direction: output
- name: WhlAng
  summary: 车轮外倾角、主销后倾角、前束角 array
  direction: output
```

### 输入

### **WhlPz** — 车轮 `z` 轴位移数组

车轮位移 *zw*，沿车轮固定的 *z* 轴方向，单位为 m。数组维度为 `1` 乘以车辆上车轮总数。

例如，对于每轴两个车轮的两轴车辆，`WhlPz`：

- 信号数组维度为 `[1x4]`。

  WhlPz=zw=[zw1,1zw1,2zw2,1zw2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlPz(1,1)` | `1` | `1` |
  | 前右 | `WhlPz(1,2)` | `1` | `2` |
  | 后左 | `WhlPz(1,3)` | `2` | `1` |
  | 后右 | `WhlPz(1,4)` | `2` | `2` |

### **WhlRe** — 车轮有效半径数组

有效车轮半径 *Rew*，单位为 m。数组维度为 `1` 乘以车辆上车轮总数。

例如，对于每轴两个车轮的两轴车辆，`WhlRe`：

- 信号数组维度为 `[1x4]`。

  WhlRe=Rew=[Rew1,1Rew1,2Rew2,1Rew2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlRe(1,1)` | `1` | `1` |
  | 前右 | `WhlRe(1,2)` | `1` | `2` |
  | 后左 | `WhlRe(1,3)` | `2` | `1` |
  | 后右 | `WhlRe(1,4)` | `2` | `2` |

### **WhlVz** — 车轮 `z` 轴速度数组

车轮速度 *żw*，沿车轮固定的 *z* 轴方向，单位为 m。数组维度为 `1` 乘以车辆上车轮总数。

例如，对于每轴两个车轮的两轴车辆，`WhlVz`：

- 信号数组维度为 `[1x4]`。

  WhlVz=z˙w=[z˙w1,1z˙w1,2z˙w2,1z˙w2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlVz(1,1)` | `1` | `1` |
  | 前右 | `WhlVz(1,2)` | `1` | `2` |
  | 后左 | `WhlVz(1,3)` | `2` | `1` |
  | 后右 | `WhlVz(1,4)` | `2` | `2` |

### **WhlFx** — 作用于车辆上的车轮纵向力数组

施加到车辆上的车轮纵向力 *Fwx*，沿惯性固定的 *x* 轴方向。数组维度为 `1` 乘以车辆上车轮总数。

例如，对于每轴两个车轮的两轴车辆，`WhlFx`：

- 信号数组维度为 `[1x4]`。

  WhlFx=Fwx=[Fwx1,1Fwx1,2Fwx2,1Fwx2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlFx(1,1)` | `1` | `1` |
  | 前右 | `WhlFx(1,2)` | `1` | `2` |
  | 后左 | `WhlFx(1,3)` | `2` | `1` |
  | 后右 | `WhlFx(1,4)` | `2` | `2` |

### **WhlFy** — 作用于车辆上的车轮侧向力数组

施加到车辆上的车轮侧向力 *Fwy*，沿惯性固定的 *y* 轴方向。数组维度为 `1` 乘以车辆上车轮总数。

例如，对于每轴两个车轮的两轴车辆，`WhlFy`：

- 信号数组维度为 `[1x4]`。

  WhlFy=Fwy=[Fwy1,1Fwy1,2Fwy2,1Fwy2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlFy(1,1)` | `1` | `1` |
  | 前右 | `WhlFy(1,2)` | `1` | `2` |
  | 后左 | `WhlFy(1.3)` | `2` | `1` |
  | 后右 | `WhlFy(1,4)` | `2` | `2` |

### **WhlM** — 车轮阵列上的悬架力矩

在车轴 `a`、车轮 `t` 处的纵向、横向和垂向悬架力矩，施加在车轴车轮托架参考坐标系处的车轮上，单位为 N·m。输入数组维度为 `3` × 车辆上的车轮数量。

- `WhlM(1,...)` — 施加在车轮上、绕惯性固定 *x* 轴的悬架力矩（纵向）
- `WhlM(2,...)` — 施加在车轮上、绕惯性固定 *y* 轴的悬架力矩（横向）
- `WhlM(3,...)` — 施加在车轮上、绕惯性固定 *z* 轴的悬架力矩（垂向）

例如，对于每轴两个车轮的两轴车辆，`WhlM`：

- 信号维度为 `[3x4]`。
- 信号包含施加在四个车轮上的悬架力矩，按其车轴和车轮位置排列。

  WhlM=Mw=[Mwx1,1Mwx1,2Mwx2,1Mwx2,2Mwy1,1Mwy1,2Mwy2,1Mwy2,2Mwz1,1Mwz1,2Mwz2,1Mwz2,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 | 力矩轴 |
  | --- | --- | --- | --- | --- |
  | 左前 | `WhlM(1,1)` | `1` | `1` | 惯性固定 *x* 轴（纵向） |
  | 右前 | `WhlM(1,2)` | `1` | `2` |
  | 左后 | `WhlM(1,3)` | `2` | `1` |
  | 右后 | `WhlM(1,4)` | `2` | `2` |
  | 左前 | `WhlM(2,1)` | `1` | `1` | 惯性固定 *y* 轴（横向） |
  | 右前 | `WhlM(2,2)` | `1` | `2` |
  | 左后 | `WhlM(2,3)` | `2` | `1` |
  | 右后 | `WhlM(2,4)` | `2` | `2` |
  | 左前 | `WhlM(3,1)` | `1` | `1` | 惯性固定 *z* 轴（垂向） |
  | 右前 | `WhlM(3,2)` | `1` | `2` |
  | 左后 | `WhlM(3,3)` | `2` | `1` |
  | 右后 | `WhlM(3,4)` | `2` | `2` |

### **VehP** — 车辆位移阵列

在车轴 `a`、车轮 `t` 处沿惯性固定坐标系的车辆位移，单位为 m。输入数组维度为 `3` × 车辆上的车轮数量。

- `VehP(1,...)` — 车轮处的车辆位移，*xv*，沿惯性固定 *x* 轴
- `VehP(2,...)` — 车轮处的车辆位移，*yv*，沿惯性固定 *y* 轴
- `VehP(3,...)` — 车轮处的车辆位移，*zv*，沿惯性固定 *z* 轴

例如，对于每轴两个车轮的两轴车辆，`VehP`：

- 信号维度为 `[3x4]`。
- 信号包含四个位移，按其车轴和车轮位置排列。

  VehP=[xvyvzv]=[xv1,1xv1,2xv2,1xv2,2yv1,1yv1,2yv2,1yv2,2zv1,1zv1,2zv2,1zv2,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 | 轴 |
  | --- | --- | --- | --- | --- |
  | 左前 | `VehP(1,1)` | `1` | `1` | 惯性固定 *x* 轴 |
  | 右前 | `VehP(1,2)` | `1` | `2` |
  | 左后 | `VehP(1,3)` | `2` | `1` |
  | 右后 | `VehP(1,4)` | `2` | `2` |
  | 左前 | `VehP(2,1)` | `1` | `1` | 惯性固定 *y* 轴 |
  | 右前 | `VehP(2,2)` | `1` | `2` |
  | 左后 | `VehP(2,3)` | `2` | `1` |
  | 右后 | `VehP(2,4)` | `2` | `2` |
  | 左前 | `VehP(3,1)` | `1` | `1` | 惯性固定 *z* 轴 |
  | 右前 | `VehP(3,2)` | `1` | `2` |
  | 左后 | `VehP(3,3)` | `2` | `1` |
  | 右后 | `VehP(3,4)` | `2` | `2` |

### **VehV** — 车辆速度数组

车辆在车轴 `a`、车轮 `t` 处沿惯性固定坐标系的速度，单位为 m。输入数组维度为 `3` 乘以车辆上的车轮数。

- `VehV(1,...)` — 车轮处的车辆速度，
  *xv*，沿惯性固定 *x* 轴
- `VehV(2,...)` — 车轮处的车辆速度，
  *yv*，沿惯性固定 *y* 轴
- `VehV(3,...)` — 车轮处的车辆速度，
  *zv*，沿惯性固定 *z* 轴

例如，对于每轴两个车轮的两轴车辆，`VehV`：

- 信号维度为 `[3x4]`。
- 信号包含 `4` 个速度，按其车轴和车轮位置排列。

  VehV=[x˙vy˙vz˙v]=[x˙v1,1x˙v1,2x˙v2,1x˙v2,2y˙v1,1y˙v1,2y˙v2,1y˙v2,2z˙v1,1z˙v1,2z˙v2,1z˙v2,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 | 轴 |
  | --- | --- | --- | --- | --- |
  | 左前 | `VehV(1,1)` | `1` | `1` | 惯性固定 *x* 轴 |
  | 右前 | `VehV(1,2)` | `1` | `2` |
  | 左后 | `VehV(1,3)` | `2` | `1` |
  | 右后 | `VehV(1,4)` | `2` | `2` |
  | 左前 | `VehV(2,1)` | `1` | `1` | 惯性固定 *y* 轴 |
  | 右前 | `VehV(2,2)` | `1` | `2` |
  | 左后 | `VehV(2,3)` | `2` | `1` |
  | 右后 | `VehV(2,4)` | `2` | `2` |
  | 左前 | `VehV(3,1)` | `1` | `1` | 惯性固定 *z* 轴 |
  | 右前 | `VehV(3,2)` | `1` | `2` |
  | 左后 | `VehV(3,3)` | `2` | `1` |
  | 右后 | `VehV(3,4)` | `2` | `2` |

### **StrgAng** — 转向角，可选数组

每个车轮的可选转向角，*δ*。
输入数组维度为 `1` 乘以转向车轮数。

例如，对于每轴两个车轮的两轴车辆，您可以输入第一轴两个车轮的转向角。

- 要启用 **StrgAng** 端口，请将 **Steered axle enable by
  axle, StrgEnByAxl** 设置为 `[1 0]`。输入信号数组
  维度为 `[1x2]`。
- `StrgAng` 信号包含两个转向角，按其车轴和车轮位置排列。

  StrgAng=δsteer=[δsteer1,1δsteer1,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 左前 | `StrgAng(1,1)` | `1` | `1` |
  | 右前 | `StrgAng(1,2)` | `1` | `2` |

#### 依赖关系

要启用端口 **StrgAng**，请将 **Steered axle
enable by axle, StrgEnByAxl** 向量的一个元素设置为 `1`。

### **Pressure** — 空气弹簧中的压力数组

空气弹簧中的压力，*p*，单位为 bar。输入数组
维度为 `1` 乘以车辆上的车轮总数。
### 输出

### **Info** — 总线信号总线

包含模块值的总线信号。这些信号是取决于车轮位置的数组。

例如，以下是两轴两轮车辆的索引。车轮总数为四个。

- 一维数组信号（1×4）

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 左前 | `(1,1)` | `1` | `1` |
  | 右前 | `(1,2)` | `1` | `2` |
  | 左后 | `(1,3)` | `2` | `1` |
  | 右后 | `(1,4)` | `2` | `2` |
- 三维数组信号（3×4）

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 左前 | `(1,1)` | `1` | `1` |
  | 右前 | `(1,2)` | `1` | `2` |
  | 左后 | `(1,3)` | `2` | `1` |
  | 右后 | `(1,4)` | `2` | `2` |
  | 左前 | `(2,1)` | `1` | `1` |
  | 右前 | `(2,2)` | `1` | `2` |
  | 左后 | `(2,3)` | `2` | `1` |
  | 右后 | `(2,4)` | `2` | `2` |
  | 左前 | `(3,1)` | `1` | `1` |
  | 右前 | `(3,2)` | `1` | `2` |
  | 左后 | `(3,3)` | `2` | `1` |
  | 右后 | `(3,4)` | `2` | `2` |

| 信号 | 描述 | 数组信号 | 变量 | 单位 |
| --- | --- | --- | --- | --- |
| `Camber` | 根据轴和车轮位置的车轮角度。 | 一维 | WhlAng[1,...]=ξ=[ξa,t] | rad |
| `Caster` | WhlAng[2,...]=η=[ηa,t] |
| `Toe` | WhlAng[3,...]=ζ=[ζa,t] |
| `Height` | 悬架高度 | 一维 | *H* | m |
| `Power` | 悬架功率耗散 | 一维 | *Psusp* | W |
| `Energy` | 悬架吸收能量 | 一维 | *Esusp* | J |
| `VehF` | 施加到车辆的悬架力 | 三维 | 对于两轴、每轴两轮的车辆：  VehF=Fv=[Fvx1,1Fvx1,2Fvx2,1Fvx2,2Fvy1,1Fvy1,2Fvy2,1Fvy2,2Fvz1,1Fvz1,2Fvz2,1Fvz2,2] | N |
| `VehM` | 施加到车辆的悬架力矩 | 三维 | 对于两轴、每轴两轮的车辆：  VehM=Mv=[Mvx1,1Mvx1,2Mvx2,1Mvx2,2Mvy1,1Mvy1,2Mvy2,1Mvy2,2Mvz1,1Mvz1,2Mvz2,1Mvz2,2] | N·m |
| `WhlF` | 施加到车轮的悬架力 | 三维 | 对于两轴、每轴两轮的车辆：  WhlF=Fw=[Fwx1,1Fwx1,2Fwx2,1Fwx2,2Fwy1,1Fwy1,2Fwy2,1Fwy2,2Fwz1,1Fwz1,2Fwz2,1Fwz2,2] | N |
| `WhlP` | 车轮位移 | 三维 | 对于两轴、每轴两轮的车辆：  WhlP=[xwywzw]=[xw1,1xw1,2xw2,1xw2,2yw1,1yw1,2yw2,1ywy2,2zwtr1,1zwtr1,2zwtr2,1zwtr2,2] | m |
| `WhlV` | 车轮速度 | 三维 | 对于两轴、每轴两轮的车辆：  WhlV=[x˙wy˙wz˙w]=[x˙w1,1x˙w1,2x˙w2,1x˙w2,2y˙w1,1y˙w1,2y˙w2,1y˙w2,2z˙w1,1z˙w1,2z˙w2,1z˙w2,2] | m/s |
| `WhlAng` | 车轮外倾角、主销后倾角、前束角 | 三维 | 对于两轴、每轴两轮的车辆：  WhlAng=[ξηζ]=[ξ1,1ξ1,2ξ2,1ξ2,2η1,1η1,2η2,1η2,2ζ1,1ζ1,2ζ2,1ζ2,2] | rad |

### **VehF** — 作用在车辆上的悬架力 `array`

在车轴 `a`、车轮 `t` 处，作用于车辆悬架连接点处的纵向、横向和垂向悬架力，单位为 N。数组维度为 `3` 乘以车辆上的车轮数。

- `VehF(1,...)` — 沿惯性固定 *x* 轴（纵向）施加到车辆上的悬架力
- `VehF(2,...)` — 沿惯性固定 *y* 轴（横向）施加到车辆上的悬架力
- `VehF(3,...)` — 沿惯性固定 *z* 轴（垂向）施加到车辆上的悬架力

例如，对于每轴两个车轮的两轴车辆，`VehF`：

- 信号维度为 `[3x4]`。
- 信号包含根据车轴和车轮位置施加到车辆上的悬架力。

  VehF=Fv=[Fvx1,1Fvx1,2Fvx2,1Fvx2,2Fvy1,1Fvy1,2Fvy2,1Fvy2,2Fvz1,1Fvz1,2Fvz2,1Fvz2,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 | 力轴 |
  | --- | --- | --- | --- | --- |
  | 左前 | `VehF(1,1)` | `1` | `1` | 惯性固定 *x* 轴（纵向） |
  | 右前 | `VehF(1,2)` | `1` | `2` |
  | 左后 | `VehF(1,3)` | `2` | `1` |
  | 右后 | `VehF(1,4)` | `2` | `2` |
  | 左前 | `VehF(2,1)` | `1` | `1` | 惯性固定 *y* 轴（横向） |
  | 右前 | `VehF(2,2)` | `1` | `2` |
  | 左后 | `VehF(2,3)` | `2` | `1` |
  | 右后 | `VehF(2,4)` | `2` | `2` |
  | 左前 | `VehF(3,1)` | `1` | `1` | 惯性固定 *z* 轴（垂向） |
  | 右前 | `VehF(3,2)` | `1` | `2` |
  | 左后 | `VehF(3,3)` | `2` | `1` |
  | 右后 | `VehF(3,4)` | `2` | `2` |

### **VehM** — 作用在车辆上的悬架力矩 `array`

在车轴 `a`、车轮 `t` 处，作用于车辆悬架连接点处的纵向、横向和垂向悬架力矩，单位为 N·m。数组维度为 `3` 乘以车辆上的车轮数。

- `VehM(1,...)` — 绕惯性固定 *x* 轴（纵向）施加到车辆上的悬架力矩
- `VehM(2,...)` — 绕惯性固定 *y* 轴（横向）施加到车辆上的悬架力矩
- `VehM(3,...)` — 绕惯性固定 *z* 轴（垂向）施加到车辆上的悬架力矩

例如，对于每轴两个车轮的两轴车辆，`VehM`：

- 信号维度为 `[3x4]`。
- 信号包含根据车轴和车轮位置施加到车辆上的悬架力矩。

  VehM=Mv=[Mvx1,1Mvx1,2Mvx2,1Mvx2,2Mvy1,1Mvy1,2Mvy2,1Mvy2,2Mvz1,1Mvz1,2Mvz2,1Mvz2,2]

  | 数组元素 | 车轴 | 车轮编号 | 力矩轴 |
  | --- | --- | --- | --- |
  | `VehM(1,1)` | `1` | `1` | 惯性固定 *x* 轴（纵向） |
  | `VehM(1,2)` | `1` | `2` |
  | `VehM(1,3)` | `2` | `1` |
  | `VehM(1,4)` | `2` | `2` |
  | `VehM(2,1)` | `1` | `1` | 惯性固定 *y* 轴（横向） |
  | `VehM(2,2)` | `1` | `2` |
  | `VehM(2,3)` | `2` | `1` |
  | `VehM(2,4)` | `2` | `2` |
  | `VehM(3,1)` | `1` | `1` | 惯性固定 *z* 轴（垂向） |
  | `VehM(3,2)` | `1` | `2` |
  | `VehM(3,3)` | `2` | `1` |
  | `VehM(3,4)` | `2` | `2` |

### **WhlF** — 车轮上的悬架力 `array`

在车轴 `a`、车轮 `t` 处的纵向、横向和垂向悬架力，施加在车轴车轮托架参考坐标系处的车轮上，单位为 N。数组维度为 `3` 乘以车辆上的车轮数量。

- `WhlF(1,...)` — 沿惯性固定 *x* 轴（纵向）作用在车轮上的悬架力
- `WhlF(2,...)` — 沿惯性固定 *y* 轴（横向）作用在车轮上的悬架力
- `WhlF(3,...)` — 沿惯性固定 *z* 轴（垂向）作用在车轮上的悬架力

例如，对于每轴有两个车轮的两轴车辆，`WhlF`：

- 信号维度为 `[3x4]`。
- 信号包含根据车轴和车轮位置施加到车辆上的车轮力。

  WhlF=Fw=[Fwx1,1Fwx1,2Fwx2,1Fwx2,2Fwy1,1Fwy1,2Fwy2,1Fwy2,2Fwz1,1Fwz1,2Fwz2,1Fwz2,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 | 力轴 |
  | --- | --- | --- | --- | --- |
  | 左前 | `WhlF(1,1)` | `1` | `1` | 惯性固定 *x* 轴（纵向） |
  | 右前 | `WhlF(1,2)` | `1` | `2` |
  | 左后 | `WhlF(1,3)` | `2` | `1` |
  | 右后 | `WhlF(1,4)` | `2` | `2` |
  | 左前 | `WhlF(2,1)` | `1` | `1` | 惯性固定 *y* 轴（横向） |
  | 右前 | `WhlF(2,2)` | `1` | `2` |
  | 左后 | `WhlF(2,3)` | `2` | `1` |
  | 右后 | `WhlF(2,4)` | `2` | `2` |
  | 左前 | `WhlF(3,1)` | `1` | `1` | 惯性固定 *z* 轴（垂向） |
  | 右前 | `WhlF(3,2)` | `1` | `2` |
  | 左后 | `WhlF(3,3)` | `2` | `1` |
  | 右后 | `WhlF(3,4)` | `2` | `2` |

### **WhlV** — 车轮速度 `array`

在车轴 `a`、车轮 `t` 处的纵向、横向和垂向车轮速度，单位为 m/s。数组维度为 `3` 乘以车辆上的车轮数量。

- `WhlV(1,...)` — 沿惯性固定 *x* 轴（纵向）的车轮速度
- `WhlV(2,...)` — 沿惯性固定 *y* 轴（横向）的车轮速度
- `WhlV(3,...)` — 沿惯性固定 *z* 轴（垂向）的车轮速度

例如，对于每轴有两个车轮的两轴车辆，`WhlV`：

- 信号维度为 `[3x4]`。
- 信号包含根据车轴和车轮位置施加到车辆上的车轮力。

  WhlV=[x˙wy˙wz˙w]=[x˙w1,1x˙w1,2x˙w2,1x˙w2,2y˙w1,1y˙w1,2y˙w2,1y˙w2,2z˙w1,1z˙w1,2z˙w2,1z˙w2,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 | 力轴 |
  | --- | --- | --- | --- | --- |
  | 左前 | `WhlV(1,1)` | `1` | `1` | 惯性固定 *x* 轴（纵向） |
  | 右前 | `WhlV(1,2)` | `1` | `2` |
  | 左后 | `WhlV(1,3)` | `2` | `1` |
  | 右后 | `WhlV(1,4)` | `2` | `2` |
  | 左前 | `WhlV(2,1)` | `1` | `1` | 惯性固定 *y* 轴（横向） |
  | 右前 | `WhlV(2,2)` | `1` | `2` |
  | 左后 | `WhlV(2,3)` | `2` | `1` |
  | 右后 | `WhlV(2,4)` | `2` | `2` |
  | 左前 | `WhlV(3,1)` | `1` | `1` | 惯性固定 *z* 轴（垂向） |
  | 右前 | `WhlV(3,2)` | `1` | `2` |
  | 左后 | `WhlV(3,3)` | `2` | `1` |
  | 右后 | `WhlV(3,4)` | `2` | `2` |

### **WhlAng** — 车轮外倾角、主销后倾角、前束角 `array`

车轴 `a`、车轮 `t` 处的车轮外倾角、主销后倾角和前束角，单位为 rad。数组维度为 `3` 乘以车辆上的车轮数量。

- `WhlAng(1,...)` — 外倾角
- `WhlAng(2,...)` — 主销后倾角
- `WhlAng(3,...)` — 前束角

例如，对于每轴两个车轮的两轴车辆，`WhlAng`：

- 信号维度为 `[3x4]`。
- 信号包含根据车轴和车轮位置的角度。

  WhlAng=[ξηζ]=[ξ1,1ξ1,2ξ2,1ξ2,2η1,1η1,2η2,1η2,2ζ1,1ζ1,2ζ2,1ζ2,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 | 角度 |
  | --- | --- | --- | --- | --- |
  | 左前 | `WhlAng(1,1)` | `1` | `1` | 外倾角 |
  | 右前 | `WhlAng(1,2)` | `1` | `2` |
  | 左后 | `WhlAng(1,3)` | `2` | `1` |
  | 右后 | `WhlAng(1,4)` | `2` | `2` |
  | 左前 | `WhlAng(2,1)` | `1` | `1` | 主销后倾角 |
  | 右前 | `WhlAng(2,2)` | `1` | `2` |
  | 左后 | `WhlAng(2,3)` | `2` | `1` |
  | 右后 | `WhlAng(2,4)` | `2` | `2` |
  | 左前 | `WhlAng(3,1)` | `1` | `1` | 前束角 |
  | 右前 | `WhlF(3,2)` | `1` | `2` |
  | 左后 | `WhlF(3,3)` | `2` | `1` |
  | 右后 | `WhlF(3,4)` | `2` | `2` |
## 参数
```yaml
parameters:
- name: Model type
  summary: 空气悬架模型类型 Physical（默认）| Mapped
  group: ''
  block_parameter: SuspModelType
  values: Physical（默认）| Mapped
- name: Air suspension spring preload, F0z
  summary: 空气悬架弹簧预载 9810（默认）| 标量
  group: ''
  block_parameter: F0z
  values: 9810（默认）| 标量
- name: Air suspension shock damping constant, Cz
  summary: 空气悬架减振器阻尼常数 10000（默认）| 标量
  group: ''
  block_parameter: Cz
  values: 10000（默认）| 标量
- name: Air spring effective area, EffctArea
  summary: 空气弹簧有效面积 0.21993（默认）| 标量
  group: ''
  block_parameter: EffctArea
  values: 0.21993（默认）| 标量
- name: Air spring volume in design position, VolDgnPos
  summary: 设计位置下的空气弹簧体积 0.08（默认）| 标量
  group: ''
  block_parameter: VolDgnPos
  values: 0.08（默认） | 标量
- name: 空气弹簧等熵指数，IstpExp
  summary: 空气弹簧等熵指数 1.4（默认） | 标量
  group: ''
  block_parameter: IstpExp
  values: 1.4（默认） | 标量
- name: 空气弹簧外径，OuterDiam
  summary: 空气弹簧外径 0.6199（默认） | 标量
  group: ''
  block_parameter: OuterDiam
  values: 0.6199（默认） | 标量
- name: 空气弹簧活塞直径，PistDiam
  summary: 空气弹簧活塞直径 0.236（默认） | 标量
  group: ''
  block_parameter: PistDiam
  values: 0.236（默认） | 标量
- name: 空气悬架最大高度，Hmax
  summary: 空气悬架最大高度 0.5（默认） | 标量
  group: ''
  block_parameter: Hmax
  values: 0.5（默认） | 标量
- name: 转向中心处的前束角，Toe
  summary: 前束角 0.0349（默认） | 标量
  group: ''
  block_parameter: Toe
  values: 0.0349（默认） | 标量
- name: 侧倾转向对悬架高度斜率，RollStrgSlp
  summary: 转向角悬架斜率 -0.2269（默认） | 标量 | vector
  group: ''
  block_parameter: RollStrgSlp
  values: -0.2269（默认） | 标量 | vector
- name: Toe angle vs steering angle slope, ToeStrgSlp
  summary: 前束角与转向角斜率 0.01（默认）| 标量 | 向量
  group: ''
  block_parameter: ToeStrgSlp
  values: 0.01（默认）| 标量 | 向量
- name: Caster angle at steering center, Caster
  summary: 转向中心处的后倾角 0.0698（默认）| 标量
  group: ''
  block_parameter: Caster
  values: 0.0698（默认）| 标量
- name: Caster angle vs suspension height slope, CasterHslp
  summary: 后倾角与悬架高度斜率 -0.2269（默认）| 标量 | 向量
  group: ''
  block_parameter: CasterHslp
  values: -0.2269（默认）| 标量 | 向量
- name: Caster angle vs steering angle slope, CasterStrgSlp
  summary: 后倾角与转向角斜率 0.01（默认）| 标量 | 向量
  group: ''
  block_parameter: CasterStrgSlp
  values: 0.01（默认）| 标量 | 向量
- name: Camber angle at steering center, Camber
  summary: 转向中心处的外倾角 0.0698（默认）| 标量
  group: ''
  block_parameter: Camber
  values: 0.0698（默认）| 标量
- name: Camber angle vs suspension height slope, CamberHslp
  summary: 外倾角与悬架高度斜率 -0.2269（默认）| 标量 | 向量
  group: ''
  block_parameter: CamberHslp
  values: -0.2269（默认） | 标量 | 向量
- name: 外倾角与转向角斜率，CamberStrgSlp
  summary: 外倾角与转向角斜率 0.01（默认） | 标量 | 向量
  group: ''
  block_parameter: CamberStrgSlp
  values: 0.01（默认） | 标量 | 向量
- name: 悬架高度与转向角斜率，StrgHgtSlp
  summary: 悬架高度与转向角斜率 0.1432（默认） | 标量 | 向量
  group: ''
  block_parameter: StrgHgtSlp
  values: 0.1432（默认） | 标量 | 向量
- name: 车轴断点，f_susp_axl_bp
  summary: 断点 [1 2]（默认） | 1 乘 P 数组
  group: ''
  block_parameter: f_susp_axl_bp
  values: '[1 2]（默认） | 1 乘 P 数组'
- name: 垂直轴悬架高度断点，f_susp_dz_bp
  summary: 断点 1 乘 M 数组
  group: ''
  block_parameter: f_susp_dz_bp
  values: 1 乘 M 数组
- name: 垂直轴空气悬架压力断点，f_susp_press_bp
  summary: 垂直轴空气悬架压力断点 [0.50 7]（默认） | 1 乘 M 数组
  group: ''
  block_parameter: f_susp_press_bp
  values: '[0.50 7]（默认） | 1 乘 M 数组'
- name: 垂直空气轴悬架力和力矩响应，f_susp_fmz
  summary: 输出数组 zeros(31,31,61,2,4)（默认）| M×N×O×P×4 数组
  group: ''
  block_parameter: f_susp_fmz
  values: zeros(31,31,61,2,4)（默认）| M×N×O×P×4 数组
- name: 空气悬架减振器阻尼常数，c_airSusp
  summary: 空气悬架减振器阻尼常数 6e6（默认）| 标量
  group: ''
  block_parameter: c_airSusp
  values: 6e6（默认）| 标量
- name: 悬架几何响应，f_susp_geom
  summary: 悬架几何响应 zeros(31,61,2,3)（默认）| M×O×P×3 数组
  group: ''
  block_parameter: f_susp_geom
  values: zeros(31,61,2,3)（默认）| M×O×P×3 数组
- name: 转向角断点，f_susp_strgdelta_bp
  summary: 转向角断点 1×O 数组
  group: ''
  block_parameter: f_susp_strgdelta_bp
  values: 1×O 数组
- name: 防倾杆臂半径，AntiSwayR
  summary: 防倾杆臂半径 0.2（默认）| scalar | vector
  group: ''
  block_parameter: AntiSwayR
  values: 0.2（默认）| scalar | vector
- name: Anti-sway arm neutral angle, AntiSwayNtrlAng
  summary: 防倾杆臂中位角 0.5236（默认）| scalar | vector
  group: ''
  block_parameter: AntiSwayNtrlAng
  values: 0.5236（默认）| scalar | vector
- name: Anti-sway torsion spring constant, AntiSwayTrsK
  summary: 防倾杆扭转弹簧常数 5.7296e+03（默认）| scalar | vector
  group: ''
  block_parameter: AntiSwayTrsK
  values: 5.7296e+03（默认）| scalar | vector
```

### **Model type** — 空气悬架模型类型 `Physical`（默认）| `Mapped`

空气悬架模型类型，指定为 `Physical` 或 `Mapped`。如果您有悬架的数据可用，请使用 `Mapped` 模型类型。如果您没有悬架的数据，请使用 `Physical` 模型类型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SuspModelType` |
| **值：** | `Physical`（默认）| `Mapped` |
| **数据类型：** | `character vector` |

#### Physical

### **Air suspension spring preload, F0z** — 空气悬架弹簧预载 `9810`（默认）| 标量

空气悬架弹簧载荷，*F0z*，单位为 N。

#### 依赖关系

要启用该参数，请将 **Model Type** 设置为 `Physical`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `F0z` |
| **值：** | `9810`（默认）| 标量 |
| **数据类型：** | `double` |

### **Air suspension shock damping constant, Cz** — 空气悬架减振器阻尼常数 `10000`（默认）| 标量

空气悬架减振器阻尼常数，*Cz*，单位为 Ns/m。

#### 依赖关系

要启用该参数，请将 **Model Type** 设置为 `Physical`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cz` |
| **值：** | `10000`（默认）| 标量 |
| **数据类型：** | `double` |

### **Air spring effective area, EffctArea** — 空气弹簧有效面积 `0.21993`（默认）| 标量

空气弹簧有效面积，*EffctArea*，单位为 m^2。

#### 依赖关系

要启用该参数，请将 **Model Type** 设置为 `Physical`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EffctArea` |
| **值：** | `0.21993`（默认）| 标量 |
| **数据类型：** | `double` |

### **Air spring volume in design position, VolDgnPos** — 设计位置下的空气弹簧体积 `0.08`（默认）| 标量

设计位置下的空气弹簧体积，*VolDngPos*，单位为 m^3。

#### 依赖关系

要启用该参数，请将 **Model Type** 设置为 `Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VolDgnPos` |
| **值：** | `0.08`（默认） | 标量 |
| **数据类型：** | `double` |

### **空气弹簧等熵指数，IstpExp** — 空气弹簧等熵指数 `1.4`（默认） | 标量

空气弹簧等熵指数，*IstpExp*，无量纲。

#### 依赖关系

要启用该参数，请将 **模型类型** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `IstpExp` |
| **值：** | `1.4`（默认） | 标量 |
| **数据类型：** | `double` |

### **空气弹簧外径，OuterDiam** — 空气弹簧外径 `0.6199`（默认） | 标量

空气弹簧外径，*OuterDiam*，单位为 m。

#### 依赖关系

要启用该参数，请将 **模型类型** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OuterDiam` |
| **值：** | `0.6199`（默认） | 标量 |
| **数据类型：** | `double` |

### **空气弹簧活塞直径，PistDiam** — 空气弹簧活塞直径 `0.236`（默认） | 标量

空气弹簧活塞直径，*PistDiam*，单位为 m。

#### 依赖关系

要启用该参数，请将 **模型类型** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PistDiam` |
| **值：** | `0.236`（默认） | 标量 |
| **数据类型：** | `double` |

### **空气悬架最大高度，Hmax** — 空气悬架最大高度 `0.5`（默认） | 标量

空气悬架最大高度，*Hmax*，单位为 m。

#### 依赖关系

要启用该参数，请将 **模型类型** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Hmax` |
| **值：** | `0.5`（默认） | 标量 |
| **数据类型：** | `double` |

### **转向中心处的前束角，Toe** — 前束角 `0.0349`（默认） | 标量

零转向角时的标称悬架前束角，
*ζ0a*，单位为 rad。

#### 依赖关系

要启用该参数，请将 **模型类型** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Toe` |
| **值：** | `0.0349`（默认） | 标量 |
| **数据类型：** | `double` |

### **侧倾转向对悬架高度斜率，RollStrgSlp** — 转向角悬架斜率 `-0.2269`（默认） | 标量 | `vector`

侧倾转向角对悬架高度，
*mhtoea*，
单位为 rad/m。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，模块
将对所有轴使用该值。

#### 依赖关系

要启用该参数，请将 **模型类型** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RollStrgSlp` |
| **值：** | `-0.2269`（默认） | 标量 | `vector` |
| **数据类型：** | `double` |

### **Toe angle vs steering angle slope, ToeStrgSlp** — 前束角与转向角斜率 `0.01`（默认）| 标量 | 向量

前束角与转向角斜率，
*mtoesteera*，
无量纲。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，该模块
对所有轴使用该值。

#### 依赖

要启用端口 **StrgAng**，将 **Steered axle
enable by axle, StrgEnByAxl** 向量的一个元素设置为
`1`。

要创建此参数，将 **Model Type** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ToeStrgSlp` |
| **值：** | `0.01`（默认）| 标量 | 向量 |
| **数据类型：** | `double` |

### **Caster angle at steering center, Caster** — 转向中心处的后倾角 `0.0698`（默认）| 标量

零转向角处的标称悬架后倾角，
*η0a*，单位为 rad。

#### 依赖

要启用该参数，将 **Model Type** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Caster` |
| **值：** | `0.0698`（默认）| 标量 |
| **数据类型：** | `double` |

### **Caster angle vs suspension height slope, CasterHslp** — 后倾角与悬架高度斜率 `-0.2269`（默认）| 标量 | 向量

后倾角与悬架高度，
*mhcastera*，
单位为 rad/m。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，该模块
对所有轴使用该值。

#### 依赖

要启用该参数，将 **Model Type** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CasterHslp` |
| **值：** | `-0.2269`（默认）| 标量 | 向量 |
| **数据类型：** | `double` |

### **Caster angle vs steering angle slope, CasterStrgSlp** — 后倾角与转向角斜率 `0.01`（默认）| 标量 | 向量

后倾角与转向角斜率，
*mcastersteera*，
无量纲。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，该模块
对所有轴使用该值。

#### 依赖

要启用端口 **StrgAng**，将 **Steered axle
enable by axle, StrgEnByAxl** 向量的一个元素设置为
`1`。

要创建此参数，将 **Model Type** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CasterStrgSlp` |
| **值：** | `0.01`（默认）| 标量 | 向量 |
| **数据类型：** | `double` |

### **Camber angle at steering center, Camber** — 转向中心处的外倾角 `0.0698`（默认）| 标量

零转向角处的标称悬架外倾角，
*ξ0a*，单位为 rad。

#### 依赖

要启用该参数，将 **Model Type** 设置为
`Physical`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Camber` |
| **值：** | `0.0698`（默认）| 标量 |
| **数据类型：** | `double` |

### **Camber angle vs suspension height slope, CamberHslp** — 外倾角与悬架高度斜率 `-0.2269`（默认）| 标量 | 向量

外倾角与悬架高度，
*mhcambera*，
单位为 rad/m。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，该模块
对所有轴使用该值。

#### 依赖关系

要启用该参数，请将 **Model Type** 设置为
`Physical`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CamberHslp` |
| **值：** | `-0.2269`（默认） | 标量 | 向量 |
| **数据类型：** | `double` |

### **外倾角与转向角斜率，CamberStrgSlp** — 外倾角与转向角斜率 `0.01`（默认） | 标量 | 向量

外倾角与转向角斜率，
*mcambersteera*，
无量纲。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，模块
将该值用于所有车轴。

#### 依赖关系

要启用端口 **StrgAng**，请将 **Steered axle
enable by axle, StrgEnByAxl** 向量的一个元素设置为
`1`。

要创建此参数，请将 **Model Type** 设置为
`Physical`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CamberStrgSlp` |
| **值：** | `0.01`（默认） | 标量 | 向量 |
| **数据类型：** | `double` |

### **悬架高度与转向角斜率，StrgHgtSlp** — 悬架高度与转向角斜率 `0.1432`（默认） | 标量 | 向量

施加在悬架车轮托架参考点处的转向角与垂直力斜率，
*mhsteera*，单位为
m/rad。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，模块
将该值用于所有车轴。

#### 依赖关系

要启用端口 **StrgAng**，请将 **Steered axle
enable by axle, StrgEnByAxl** 向量的一个元素设置为
`1`。

要创建此参数，请将 **Model Type** 设置为
`Physical`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgHgtSlp` |
| **值：** | `0.1432`（默认） | 标量 | 向量 |
| **数据类型：** | `double` |

#### 映射

### **车轴断点，f\_susp\_axl\_bp** — 断点 `[1 2]`（默认） | `1` 乘 `P` 数组

车轴断点，*f\_susp\_axl\_bp*，无量纲。

#### 依赖关系

要启用此参数，请将 **Model type** 设置为
`Mapped`。

#### 编程用法

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_susp_axl_bp` |
| **值：** | `[1 2]`（默认） | `1` 乘 `P` 数组 |
| **数据类型：** | `double` |

### **垂直轴悬架高度断点，f\_susp\_dz\_bp** — 断点 `1` 乘 `M` 数组

垂直轴悬架高度断点，*f\_susp\_dz\_bp*，单位为
m。

#### 依赖关系

要启用此参数，请将 **Model type** 设置为
`Mapped`。

#### 编程用法

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_susp_dz_bp` |
| **值：** | `1` 乘 `M` 数组 |
| **数据类型：** | `double` |

### **垂直轴空气悬架压力断点，f\_susp\_press\_bp** — 垂直轴空气悬架压力断点 `[0.50 7]`（默认） | `1` 乘 `M` 数组

垂直轴空气悬架压力断点，*f\_susp\_press\_bp*，
单位为 m/s。

#### 依赖关系

要启用此参数，请将 **Model type** 设置为
`Mapped`。

#### 编程用法

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_susp_press_bp` |
| **值：** | `[0.50 7]`（默认） | `1` 乘 `M` 数组 |
| **数据类型：** | `double` |

### **垂直空气轴悬架力和力矩响应，f\_susp\_fmz** — 输出数组 `zeros(31,31,61,2,4)`（默认）| `M`×`N`×`O`×`P`×`4` 数组

输出值数组，作为以下变量的函数：

- 垂直悬架高度，*M*
- 垂直悬架高度速度，*N*
- 转向角，*O*
- 车轴，*P*
- 四种输出类型：

  - 1 — 垂直力，单位为 N
  - 2 — 用户自定义输出
  - 3 — 储存能量，单位为 J
  - 4 — 吸收功率，单位为 W

数组维度必须与断点维度匹配。

#### 依赖关系

要启用此参数，请将 **模型类型** 设置为
`Mapped`。

#### 程序化使用

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_susp_fmz` |
| **值：** | `zeros(31,31,61,2,4)`（默认）| `M`×`N`×`O`×`P`×`4` 数组 |
| **数据类型：** | `double` |

### **空气悬架减振器阻尼常数，c\_airSusp** — 空气悬架减振器阻尼常数 `6e6`（默认）| 标量

空气悬架减振器阻尼常数，*c\_airSusp*，单位为 Ns/m。

#### 依赖关系

要启用此参数，请将 **模型类型** 设置为
`Mapped`。

#### 程序化使用

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `c_airSusp` |
| **值：** | `6e6`（默认）| 标量 |
| **数据类型：** | `double` |

### **悬架几何响应，f\_susp\_geom** — 悬架几何响应 `zeros(31,61,2,3)`（默认）| `M`×`O`×`P`×`3` 数组

几何悬架值数组，作为以下变量的函数：

- 垂直悬架高度，*M*
- 转向角，*O*
- 车轴，*P*
- 三种输出类型：

  - 1 — 外倾角，单位为 rad
  - 2 — 主销后倾角，单位为 rad
  - 3 — 前束角，单位为 rad

数组维度必须与断点维度匹配

#### 依赖关系

要启用此参数，请将 **模型类型** 设置为
`Mapped`。

#### 程序化使用

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_susp_geom` |
| **值：** | `zeros(31,61,2,3)`（默认）| `M`×`O`×`P`×`3` 数组 |
| **数据类型：** | `double` |

### **转向角断点，f\_susp\_strgdelta\_bp** — 转向角断点 `1`×`O` 数组

转向角断点，单位为 rad。

#### 依赖关系

要启用此参数，请将 **模型类型** 设置为
`Mapped`。

#### 程序化使用

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_susp_strgdelta_bp` |
| **值：** | `1`×`O` 数组 |
| **数据类型：** | `double` |

### **防倾杆臂半径，AntiSwayR** — 防倾杆臂半径 `0.2`（默认）| `scalar` | `vector`

防倾杆臂半径，*r*，单位为 m。

向量为 `1` 乘以车辆车轴数，
*Na*。如果提供标量值，模块
将对所有车轴使用该值。

#### 依赖关系

将 **逐轴防倾杆启用，AntiSwayEnByAxl** 向量的元素设置为 1 会创建以下防倾杆参数：

- **防倾杆臂半径，AntiSwayR**
- **防倾杆臂中性角，AntiSwayNtrlAng**
- **防倾杆扭转弹簧常数，AntiSwayTrsK**

#### 程序化使用

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AntiSwayR` |
| **值：** | `0.2`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **Anti-sway arm neutral angle, AntiSwayNtrlAng** — 防倾杆臂中位角 `0.5236`（默认）| `scalar` | `vector`

防倾杆臂中位角，*θ0a*，在名义悬架高度处，单位为 rad。

向量为 `1` × 车辆轴数，*Na*。如果提供标量值，模块会将该值用于所有车轴。

#### 依赖关系

将 **Anti-sway axle enable by axle, AntiSwayEnByAxl** 向量的某个元素设置为 1 会创建以下防倾杆参数：

- **Anti-sway arm radius, AntiSwayR**
- **Anti-sway arm neutral angle, AntiSwayNtrlAng**
- **Anti-sway torsion spring constant, AntiSwayTrsK**

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AntiSwayNtrlAng` |
| **值：** | `0.5236`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **Anti-sway torsion spring constant, AntiSwayTrsK** — 防倾杆扭转弹簧常数 `5.7296e+03`（默认）| `scalar` | `vector`

防倾杆扭转弹簧常数，*ka*，单位为 N·m/rad。

向量为 `1` × 车辆轴数，*Na*。如果提供标量值，模块会将该值用于所有车轴。

#### 依赖关系

将 **Anti-sway axle enable by axle, AntiSwayEnByAxl** 向量的某个元素设置为 1 会创建以下防倾杆参数：

- **Anti-sway arm radius, AntiSwayR**
- **Anti-sway arm neutral angle, AntiSwayNtrlAng**
- **Anti-sway torsion spring constant, AntiSwayTrsK**

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AntiSwayTrsK` |
| **值：** | `5.7296e+03`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |
## 所属库

Vehicle Dynamics Blockset / Suspension

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

空气弹簧独立悬架

Independent Suspension - Air Spring 模块实现了一个具有多轴且每轴多轮的空气弹簧独立悬架。您可以使用该模块，根据测量或仿真的悬架响应数据来建模悬架几何、柔度和阻尼效应

该模块将悬架柔度、阻尼和几何效应建模为车辆与轮架相对位置和速度的函数，并使用各轴特定的柔度和阻尼参数。利用悬架柔度和阻尼，该模块计算作用在车辆和车轮上的悬架力。该模块使用 *Z* 向下坐标系（定义于 SAE J670）。下表描述了您可以为每个悬架元件指定的设置。

| 悬架元件 | 设置 |
| --- | --- |
| 轴 | - 多个车轮 - 对具有两个车轮的轴使用防倾杆 - 悬架参数 |
| 车轮 | - 转向角 |

该模块包含储能弹簧元件和耗能阻尼器元件。它不包含储能质量元件。该模块假设连接到该模块的车辆（簧上）和车轮（簧下）模块存储与质量相关的悬架能量。

下表总结了具有以下配置的车辆的模块参数设置：

- 两个轴
- 每轴两个车轮
- 前轴两个车轮的转向角输入
- 前轴上的防倾杆

| 参数 | 设置 |
| --- | --- |
| **Number of axles, NumAxl** | `2` |
| **Number of wheels by axle, NumWhlsByAxl** | `[2 2]` |
| **Steered axle enable by axle, StrgEnByAxl** | `[1 0]` |
| **Anti-sway axle enable by axle, AntiSwayEnByAxl** | `[1 0]` |

该模块使用车轮编号 *t* 来索引输入和输出信号。下表总结了具有以下配置的车辆的车轮、轴以及对应的车轮编号：

- 两个轴
- 每轴两个车轮

| 车轮 | 轴 | 车轮编号 |
| --- | --- | --- |
| 左前 | 前 | `1` |
| 右前 | 前 | `2` |
| 左后 | 后 | `1` |
| 右后 | 后 | `2` |

### Suspension Compliance and Damping

当您将 **Model type** 参数设置为
`Mapped` 时，该模块使用一个查找表，将垂向阻尼和柔度与悬架高度、空气弹簧压力和转向角关联起来。您可以校准车轮力查找表，使得转向角从标称中心位置变化时产生的力能够增加车辆高度。

该模块实现以下方程。

Fwzlookupa=f(zva,t−zwa,t,z˙va,t−z˙wa,t,δsteera,t)Fwza,t=Fwzlookupa+Fzaswya,t

该模块假设悬架元件无质量。因此，施加到车辆上的悬架力和力矩等于施加到车轮上的悬架力和力矩。

Fvxa,t=Fwxa,tFvya,t=Fwya,tFvza,t=−Fwza,tMvxa,t=Mwxa,t+Fwya,t(Rewya,t+Ha,t)Mvya,t=Mwya,t+Fwxa,t(Rewxa,t+Ha,t)Mvza,t=Mwza,t

该模块将车轮位置和速度设置为等于车辆的横向和纵向位置和速度。

xwa,t=xva,tywa,t=yva,tx˙wa,t=x˙va,ty˙wa,t=y˙va,t

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Fwza,t*, *Mwza,t* | 施加到车轴 `a`、车轮 `t` 上的车轮的悬架力和力矩，沿车轮固定 *z* 轴 |
| *Fwxa,t*, *Mwxa,t* | 施加到车轴 `a`、车轮 `t` 上的车轮的悬架力和力矩，沿车轮固定 *x* 轴 |
| *Fwya,t*, *Mwya,t* | 施加到车轴 `a`、车轮 `t` 上的车轮的悬架力和力矩，沿车轮固定 *y* 轴 |
| *Fvza,t*, *Mvza,t* | 施加到车轴 `a`、车轮 `t` 上的车辆的悬架力和力矩，沿车轮固定 *z* 轴 |
| *Fvxa,t*, *Mvxa,t* | 施加到车轴 `a`、车轮 `t` 上的车辆的悬架力和力矩，沿车轮固定 *x* 轴 |
| *Fvya,t*, *Mvya,t* | 施加到车轴 `a`、车轮 `t` 上的车辆的悬架力和力矩，沿车轮固定 *y* 轴 |
| *Fz0a* | 施加到车轴 `a` 上车轮的垂向悬架弹簧预紧力 |
| *kza* | 施加到车轴 `a` 上车轮的垂向弹簧常数 |
| *kwaz* | 车轮与车轴接口柔度常数 |
| *mhsteera* | 施加到车轴 `a` 上车轮转向节处的转向角对垂向力的斜率 |
| *δsteera,t* | 车轴 `a`、车轮 `t` 的转向角输入 |
| *cza* | 施加到车轴 `a` 上车轮的垂向阻尼常数 |
| *cwaz* | 车轮与车轴接口阻尼常数 |
| *Rewa,t* | 车轴 `a`、车轮 `t` 的有效车轮半径 |
| *Fzhstopa,t* | 车轴 `a`、车轮 `t` 处的垂向硬限位力，沿惯性固定 *z* 轴 |
| *Fzaswya,t* | 车轴 `a`、车轮 `t` 处的垂向防倾力，沿惯性固定 *z* 轴 |
| *Fwaz0* | 车轮与车轴接口柔度常数 |
| *zva,t*, *żva,t* | 车轴 `a`、车轮 `t` 处的车辆位移和速度，沿惯性固定 *z* 轴 |
| *zwa,t*, *żwa,t* | 车轴 `a`、车轮 `t` 处的车轮位移和速度，沿惯性固定 *z* 轴 |
| *xva,t*, *ẋva,t* | 车轴 `a`、车轮 `t` 处的车辆位移和速度，沿惯性固定 *z* 轴 |
| *xwa,t*, *ẋwa,t* | 车轴 `a`、车轮 `t` 处的车轮位移和速度，沿惯性固定 *z* 轴 |
| *yva,t*, *ẏva,t* | 车轴 `a`、车轮 `t` 处的车辆位移和速度，沿惯性固定 *y* 轴 |
| *ywa,t*, *ẏwa,t* | 车轴 `a`、车轮 `t` 处的车轮位移和速度，沿惯性固定 *y* 轴 |
| *Ha,t* | 车轴 `a`、车轮 `t` 处的悬架高度 |
| *Rewa,t* | 车轴 `a`、车轮 `t` 处的有效车轮半径 |

当您将 **Model type** 参数设置为
`Physical` 时，该模块将弹簧力计算为弹簧挠度的函数。

F=p0Aw(V0V0−Vs)xwhereV=π4(0.4DA2+0.6DK2)

该模块将弹簧刚度计算为有效面积和内部体积的函数。

k=x(1+p0)Aw2V0

这些方程使用以下变量。

|  |  |
| --- | --- |
| *p0* | 静态工作压力 |
| *Aw* | 有效面积 |
| *V0* | 设计位置下的体积 |
| *V* | 空气弹簧的体积梯度 |
| *s* | 弹簧挠度 |
| *X* | 等熵指数 |

### Hardstop Forces

模块施加的硬止点反馈力 *Fzhstopa,t* 取决于悬架是在压缩还是在伸张。模块在以下情况下施加该力：

- 在压缩时，当悬架压缩量超过 **Suspension maximum height, Hmax** 参数指定的最大距离时
- 在伸张时，当悬架伸张量大于 **Suspension maximum height, Hmax** 参数指定的最大伸张量时

为计算该力，模块使用基于双曲正切和指数缩放的刚度。

### Anti-Sway Bar

可选地，使用 **Anti-sway axle enable by axle, AntiSwayEnByAxl** 参数为具有两个车轮的车轴实现防倾杆力 *Fzaswya,t*。下图展示了防倾杆如何在共享车轴上的两个独立悬架车轮之间传递扭矩。每个独立悬架通过一个从防倾杆延伸到独立悬架连接点的半径臂向防倾杆施加扭矩。

防倾杆连接到独立悬架的示意图

为计算防倾杆力，模块实现以下方程。

| 计算 | 方程 |
| --- | --- |
| 给定车轴和车轮的防倾杆角偏转，*Δϴa,t* | θ0a=tan−1(z0r)Δθa,t=tan−1(rtanθ0a−zwa,t+zva,tr) |
| 防倾杆扭转角，*ϴa* | θa=−tan−1(rtanθ0a−zwa,1+zva,1r)−tan−1(rtanθ0a−zwa,2+zva,2r) |
| 防倾杆扭矩，*τa* | τa=kaθa |
| 施加到车轴 `a`、车轮 `t` 上的车轮沿车轮固定 *z* 轴的防倾杆力 | Fzaswya,1=(τar)cos(θ0a−tan−1(rtanθ0a−zwa,1+zva,1r))Fzaswya,2=(τar)cos(θ0a−tan−1(rtanθ0a−zwa,2+zva,2r)) |

这些方程和图示使用以下变量。

|  |  |
| --- | --- |
| *τa* | 防倾杆扭矩 |
| *θ* | 防倾杆扭转角 |
| *θ0a* | 初始防倾杆扭转角 |
| *Δϴa,t* | 车轴 `a`、车轮 `t` 处的防倾杆角偏转 |
| *r* | 防倾杆臂半径 |
| *z0* | 从防倾杆连接点到防倾杆中心线的垂直距离 |
| *Fzswaya,t* | 施加到车轴 `a`、车轮 `t` 上的车轮沿车轮固定 *z* 轴的防倾杆力 |
| *zva,t* | 车轴 `a`、车轮 `t` 处车辆沿惯性固定 *z* 轴的位移 |
| *zwa,t* | 车轴 `a`、车轮 `t` 处车轮沿惯性固定 *z* 轴的位移 |

### Camber, Caster, and Toe Angles

为计算外倾角、主销后倾角和前束角，模块使用查找表 *Galookup*，该查找表是悬架高度和转向角的函数。

[ξa,tηa,tζa,t]=Galookupf(zwa,t−zva,t,δsteera,t)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ξa,t* | 车轴 `a`、车轮 `t` 上车轮的外倾角 |
| *ηa,t* | 车轴 `a`、车轮 `t` 上车轮的主销后倾角 |
| *ζa,t* | 车轴 `a`、车轮 `t` 上车轮的前束角 |
| *δsteera,t* | 车轴 `a`、车轮 `t` 的转向角输入 |
| *zva,t* | 车轴 `a`、车轮 `t` 处车辆沿惯性固定 *z* 轴的位移 |
| *zwa,t* | 车轴 `a`、车轮 `t` 处车轮沿惯性固定 *z* 轴的位移 |

### Steering Angles

可选地，您可以为车轮输入转向角。为计算车轮的转向角，模块根据悬架高度对输入转向角进行偏移。为进行计算，模块使用查找表 *Galookup*，该查找表是悬架位置和转向角的函数。

δwhlsteera,t=δsteera,t+Galookupf(zwa,t−zva,t,δsteera,t)

该方程使用以下变量。

|  |  |
| --- | --- |
| *δwhlsteera,t* | 车轴 `a`、车轮 `t` 的车轮转向角 |
| *δsteera,t* | 车轴 `a`、车轮 `t` 的转向角输入 |
| *zva,t* | 车轴 `a`、车轮 `t` 处车辆沿惯性固定 *z* 轴的位移 |
| *zwa,t* | 车轴 `a`、车轮 `t` 处车轮沿惯性固定 *z* 轴的位移 |

### 功率与能量

该模块为每个车轴 `a` 和车轮 `t` 计算以下悬架特性。

| 计算项 | 方程 |
| --- | --- |
| 耗散功率，*Psuspa,t* | Psuspa,t=Fwzlookupa(z˙va,t−z˙wa,t,z˙va,t−z˙wa,t,δsteera,t) |
| 吸收能量，*Esuspa,t* | Esuspa,t=Fwzlookupa(z˙va,t−z˙wa,t,z˙va,t−z˙wa,t,δsteera,t) |
| 悬架高度，*Ha,t* | Ha,t=−(zva,t−zwa,t−median(f\_susp\_dz\_bp)) |
| 从轮毂中心到轮胎/道路界面的距离 | zwtra,t=Rewa,t+Ha,t |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *mhsteera* | 施加在车轴 `a` 上车轮轮毂处的转向角到垂直力的斜率 |
| *δsteera,t* | 车轴 `a`、车轮 `t` 的转向角输入 |
| *Rewa,t* | 车轴 `a`、车轮 `t` 从轮毂中心到轮胎/道路界面的有效车轮半径 |
| *f\_susp\_dz\_bp* | 垂直轴悬架高度断点 |
| *zwtra,t* | 沿惯性固定 *z* 轴，从轮毂中心到轮胎/道路界面的距离 |
| *zva,t*、*żva,t* | 沿惯性固定 *z* 轴，车轴 `a`、车轮 `t` 处的车辆位移和速度 |
| *zwa,t*、*żwa,t* | 沿惯性固定 *z* 轴，车轴 `a`、车轮 `t* 处的车轮位移和速度 |
