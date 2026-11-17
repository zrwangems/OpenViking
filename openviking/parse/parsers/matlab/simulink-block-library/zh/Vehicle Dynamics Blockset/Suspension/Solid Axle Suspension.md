---
type: simulink-block
title: 'Solid Axle Suspension'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Suspension'
documentation_page: 'solidaxlesuspension'
documentation_source_path: 'ref/solidaxlesuspension.html'
language: zh-CN
chinese_source: worker-translation
---

# Solid Axle Suspension

## 端口

### 输入

### **WhlPz** — 车轮 `z` 轴位移数组

车轮位移，*zw*，沿车轮固定的
*z* 轴，单位为 m。数组维度为 `1` 乘以
车辆上车轮总数。

例如，对于每轴两个车轮的两轴车辆，
`WhlPz`：

- 信号数组维度为 `[1x4]`。

  WhlPz=zw=[zw1,1zw1,2zw2,1zw2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlPz(1,1)` | `1` | `1` |
  | 前右 | `WhlPz(1,2)` | `1` | `2` |
  | 后左 | `WhlPz(1,3)` | `2` | `1` |
  | 后右 | `WhlPz(1,4)` | `2` | `2` |

### **WhlRe** — 车轮有效半径数组

有效车轮半径，*Rew*，单位为 m。数组
维度为 `1` 乘以车辆上车轮总数。

例如，对于每轴两个车轮的两轴车辆，
`WhlRe`：

- 信号数组维度为 `[1x4]`。

  WhlRe=Rew=[Rew1,1Rew1,2Rew2,1Rew2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlRe(1,1)` | `1` | `1` |
  | 前右 | `WhlRe(1,2)` | `1` | `2` |
  | 后左 | `WhlRe(1,3)` | `2` | `1` |
  | 后右 | `WhlRe(1,4)` | `2` | `2` |

### **WhlVz** — 车轮 `z` 轴速度数组

车轮速度，*żw*，沿车轮固定的
*z* 轴，单位为 m。数组维度为 `1` 乘以
车辆上车轮总数。

例如，对于每轴两个车轮的两轴车辆，
`WhlVz`：

- 信号数组维度为 `[1x4]`。

  WhlVz=z˙w=[z˙w1,1z˙w1,2z˙w2,1z˙w2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlVz(1,1)` | `1` | `1` |
  | 前右 | `WhlVz(1,2)` | `1` | `2` |
  | 后左 | `WhlVz(1,3)` | `2` | `1` |
  | 后右 | `WhlVz(1,4)` | `2` | `2` |

### **WhlFx** — 车辆上的纵向车轮力数组

施加到车辆上的纵向车轮力，
*Fwx*，沿惯性固定的
*x* 轴。数组维度为 `1` 乘以车辆上
车轮总数。

例如，对于每轴两个车轮的两轴车辆，
`WhlFx`：

- 信号数组维度为 `[1x4]`。

  WhlFx=Fwx=[Fwx1,1Fwx1,2Fwx2,1Fwx2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlFx(1,1)` | `1` | `1` |
  | 前右 | `WhlFx(1,2)` | `1` | `2` |
  | 后左 | `WhlFx(1,3)` | `2` | `1` |
  | 后右 | `WhlFx(1,4)` | `2` | `2` |

### **WhlFy** — 车辆上的横向车轮力数组

施加到车辆上的横向车轮力，
*Fwy*，沿惯性固定的
*y* 轴。数组维度为 `1` 乘以车辆上
车轮总数。

例如，对于每轴两个车轮的两轴车辆，
`WhlFy`：

- 信号数组维度为 `[1x4]`。

  WhlFy=Fwy=[Fwy1,1Fwy1,2Fwy2,1Fwy2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 前左 | `WhlFy(1,1)` | `1` | `1` |
  | 前右 | `WhlFy(1,2)` | `1` | `2` |
  | 后左 | `WhlFy(1.3)` | `2` | `1` |
  | 后右 | `WhlFy(1,4)` | `2` | `2` |

### **WhlM** — 车轮阵列上的悬架力矩

在车轴 `a`、车轮 `t` 处的纵向、横向和垂向悬架力矩，施加于车轴车轮托架参考坐标系处的车轮，单位为 N·m。输入阵列维度为 `3` 乘以车辆上的车轮数量。

- `WhlM(1,...)` — 施加于车轮的、绕惯性固定 *x* 轴的悬架力矩（纵向）
- `WhlM(2,...)` — 施加于车轮的、绕惯性固定 *y* 轴的悬架力矩（横向）
- `WhlM(3,...)` — 施加于车轮的、绕惯性固定 *z* 轴的悬架力矩（垂向）

例如，对于每轴两个车轮的两轴车辆，`WhlM`：

- 信号维度为 `[3x4]`。
- 信号包含施加于四个车轮的悬架力矩，依据其车轴和车轮位置。

  WhlM=Mw=[Mwx1,1Mwx1,2Mwx2,1Mwx2,2Mwy1,1Mwy1,2Mwy2,1Mwy2,2Mwz1,1Mwz1,2Mwz2,1Mwz2,2]

  | 车轮 | 阵列元素 | 车轴 | 车轮编号 | 力矩轴 |
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

在车轴 `a`、车轮 `t` 处沿惯性固定坐标系的车辆位移，单位为 m。输入阵列维度为 `3` 乘以车辆上的车轮数量。

- `VehP(1,...)` — 车轮处的车辆位移，*xv*，沿惯性固定 *x* 轴
- `VehP(2,...)` — 车轮处的车辆位移，*yv*，沿惯性固定 *y* 轴
- `VehP(3,...)` — 车轮处的车辆位移，*zv*，沿惯性固定 *z* 轴

例如，对于每轴两个车轮的两轴车辆，`VehP`：

- 信号维度为 `[3x4]`。
- 信号包含四个位移，依据其车轴和车轮位置。

  VehP=[xvyvzv]=[xv1,1xv1,2xv2,1xv2,2yv1,1yv1,2yv2,1yv2,2zv1,1zv1,2zv2,1zv2,2]

  | 车轮 | 阵列元素 | 车轴 | 车轮编号 | 轴 |
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
### 输出

### **Info** — 总线信号总线

包含模块值的总线信号。这些信号是取决于车轮位置的数组。

例如，以下是两轴两轮车辆的索引。车轮总数为四个。

- 一维数组信号（1×4）

  | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- |
  | `(1,1)` | `1` | `1` |
  | `(1,2)` | `1` | `2` |
  | `(1,3)` | `2` | `1` |
  | `(1,4)` | `2` | `2` |
- 三维数组信号（3×4）

  | 数组元素 | 轴 | 车轮编号 |
  | --- | --- | --- |
  | `(1,1)` | `1` | `1` |
  | `(1,2)` | `1` | `2` |
  | `(1,3)` | `2` | `1` |
  | `(1,4)` | `2` | `2` |
  | `(2,1)` | `1` | `1` |
  | `(2,2)` | `1` | `2` |
  | `(2,3)` | `2` | `1` |
  | `(2,4)` | `2` | `2` |
  | `(3,1)` | `1` | `1` |
  | `(3,2)` | `1` | `2` |
  | `(3,3)` | `2` | `1` |
  | `(3,4)` | `2` | `2` |

| 信号 | 描述 | 数组信号 | 变量 | 单位 |
| --- | --- | --- | --- | --- |
| `Camber` | 根据轴确定的车轮角度。 | 1D | WhlAng[1,...]=ξ=[ξa,t] | rad |
| `Caster` | WhlAng[2,...]=η=[ηa,t] |
| `Toe` | WhlAng[3,...]=ζ=[ζa,t] |
| `Height` | 悬架高度 | 1D | *H* | m |
| `Power` | 悬架功率耗散 | 1D | *Psusp* | W |
| `Energy` | 悬架吸收能量 | 1D | *Esusp* | J |
| `VehF` | 施加到车辆的悬架力 | 3D | 对于两轴、每轴两轮的车辆：  VehF=Fv=[Fvx1,1Fvx1,2Fvx2,1Fvx2,2Fvy1,1Fvy1,2Fvy2,1Fvy2,2Fvz1,1Fvz1,2Fvz2,1Fvz2,2] | N |
| `VehM` | 施加到车辆的悬架力矩 | 3D | 对于两轴、每轴两轮的车辆：  VehM=Mv=[Mvx1,1Mvx1,2Mvx2,1Mvx2,2Mvy1,1Mvy1,2Mvy2,1Mvy2,2Mvz1,1Mvz1,2Mvz2,1Mvz2,2] | N·m |
| `WhlF` | 施加到车轮的悬架力 | 3D | 对于两轴、每轴两轮的车辆：  WhlF=Fw=[Fwx1,1Fwx1,2Fwx2,1Fwx2,2Fwy1,1Fwy1,2Fwy2,1Fwy2,2Fwz1,1Fwz1,2Fwz2,1Fwz2,2] | N |
| `WhlP` | 车轮位移 | 3D | 对于两轴、每轴两轮的车辆：  WhlP=[xwywzw]=[xw1,1xw1,2xw2,1xw2,2yw1,1yw1,2yw2,1ywy2,2zwtr1,1zwtr1,2zwtr2,1zwtr2,2] | m |
| `WhlV` | 车轮速度 | 3D | 对于两轴、每轴两轮的车辆：  WhlV=[x˙wy˙wz˙w]=[x˙w1,1x˙w1,2x˙w2,1x˙w2,2y˙w1,1y˙w1,2y˙w2,1y˙w2,2z˙w1,1z˙w1,2z˙w2,1z˙w2,2] | m/s |
| `WhlAng` | 车轮外倾角、主销后倾角、前束角 | 3D | 对于两轴、每轴两轮的车辆：  WhlAng=[ξηζ]=[ξ1,1ξ1,2ξ2,1ξ2,2η1,1η1,2η2,1η2,2ζ1,1ζ1,2ζ2,1ζ2,2] | rad |

### **VehF** — 施加到车辆的悬架力 `array`

在轴 `a`、车轮 `t` 处，施加到车辆悬架连接点处的纵向、横向和垂向悬架力，单位为 N。数组维度为 `3` 乘以车辆上的车轮数量。

- `VehF(1,...)` — 沿惯性固定 *x* 轴（纵向）施加到车辆的悬架力
- `VehF(2,...)` — 沿惯性固定 *y* 轴（横向）施加到车辆的悬架力
- `VehF(3,...)` — 沿惯性固定 *z* 轴（垂向）施加到车辆的悬架力

例如，对于两轴、每轴两轮的车辆，`VehF`：

- 信号维度为 `[3x4]`。
- 信号包含根据轴和车轮位置施加到车辆的悬架力。

  VehF=Fv=[Fvx1,1Fvx1,2Fvx2,1Fvx2,2Fvy1,1Fvy1,2Fvy2,1Fvy2,2Fvz1,1Fvz1,2Fvz2,1Fvz2,2]

  | 车轮 | 数组元素 | 轴 | 车轮编号 | 力轴 |
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

在车轴 `a`、车轮 `t` 处的纵向、横向和垂向悬架力矩，作用于悬架连接点处的车辆，单位为 N·m。数组维度为 `3` 乘以车辆上的车轮数量。

- `VehM(1,...)` — 作用于车辆上、绕惯性固定 *x* 轴的悬架力矩（纵向）
- `VehM(2,...)` — 作用于车辆上、绕惯性固定 *y* 轴的悬架力矩（横向）
- `VehM(3,...)` — 作用于车辆上、绕惯性固定 *z* 轴的悬架力矩（垂向）

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

### **WhlF** — 作用在车轮上的悬架力 `array`

在车轴 `a`、车轮 `t` 处的纵向、横向和垂向悬架力，作用于车轴车轮托架参考坐标系处的车轮，单位为 N。数组维度为 `3` 乘以车辆上的车轮数量。

- `WhlF(1,...)` — 沿惯性固定 *x* 轴作用在车轮上的悬架力（纵向）
- `WhlF(2,...)` — 沿惯性固定 *y* 轴作用在车轮上的悬架力（横向）
- `WhlF(3,...)` — 沿惯性固定 *z* 轴作用在车轮上的悬架力（垂向）

例如，对于每轴两个车轮的两轴车辆，`WhlF`：

- 信号维度为 `[3x4]`。
- 信号包含根据车轴和车轮位置施加到车辆上的车轮力。

  WhlF=Fw=[Fwx1,1Fwx1,2Fwx2,1Fwx2,2Fwy1,1Fwy1,2Fwy2,1Fwy2,2Fwz1,1Fwz1,2Fwz2,1Fwz2,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 | 力轴 |
  | --- | --- | --- | --- | --- |
  | 前左 | `WhlF(1,1)` | `1` | `1` | 惯性固定 *x* 轴（纵向） |
  | 前右 | `WhlF(1,2)` | `1` | `2` |
  | 后左 | `WhlF(1,3)` | `2` | `1` |
  | 后右 | `WhlF(1,4)` | `2` | `2` |
  | 前左 | `WhlF(2,1)` | `1` | `1` | 惯性固定 *y* 轴（横向） |
  | 前右 | `WhlF(2,2)` | `1` | `2` |
  | 后左 | `WhlF(2,3)` | `2` | `1` |
  | 后右 | `WhlF(2,4)` | `2` | `2` |
  | 前左 | `WhlF(3,1)` | `1` | `1` | 惯性固定 *z* 轴（垂向） |
  | 前右 | `WhlF(3,2)` | `1` | `2` |
  | 后左 | `WhlF(3,3)` | `2` | `1` |
  | 后右 | `WhlF(3,4)` | `2` | `2` |

### **WhlV** — 车轮速度 `array`

在车轴 `a`、车轮 `t` 处的纵向、侧向和垂向车轮速度，单位为 m/s。数组维度为 `3` 乘以车辆上的车轮数量。

- `WhlV(1,...)` — 沿惯性固定 *x* 轴的车轮速度（纵向）
- `WhlV(2,...)` — 沿惯性固定 *y* 轴的车轮速度（侧向）
- `WhlV(3,...)` — 沿惯性固定 *z* 轴的车轮速度（垂向）

例如，对于每轴两个车轮的两轴车辆，`WhlV`：

- 信号维度为 `[3x4]`。
- 信号包含根据车轴和车轮位置施加到车辆上的车轮力。

  WhlV=[x˙wy˙wz˙w]=[x˙w1,1x˙w1,2x˙w2,1x˙w2,2y˙w1,1y˙w1,2y˙w2,1y˙w2,2z˙w1,1z˙w1,2z˙w2,1z˙w2,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 | 力轴 |
  | --- | --- | --- | --- | --- |
  | 左前 | `WhlV(1,1)` | `1` | `1` | 惯性固定 *x* 轴（纵向） |
  | 右前 | `WhlV(1,2)` | `1` | `2` |
  | 左后 | `WhlV(1,3)` | `2` | `1` |
  | 右后 | `WhlV(1,4)` | `2` | `2` |
  | 左前 | `WhlV(2,1)` | `1` | `1` | 惯性固定 *y* 轴（侧向） |
  | 右前 | `WhlV(2,2)` | `1` | `2` |
  | 左后 | `WhlV(2,3)` | `2` | `1` |
  | 右后 | `WhlV(2,4)` | `2` | `2` |
  | 左前 | `WhlV(3,1)` | `1` | `1` | 惯性固定 *z* 轴（垂向） |
  | 右前 | `WhlV(3,2)` | `1` | `2` |
  | 左后 | `WhlV(3,3)` | `2` | `1` |
  | 右后 | `WhlV(3,4)` | `2` | `2` |

### **WhlAng** — 车轮外倾角、主销后倾角、前束角 `array`

在车轴 `a`、车轮 `t` 处的外倾角、主销后倾角和前束角，单位为 rad。数组维度为 `3` 乘以车辆上的车轮数量。

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

### 车轴

### **Number of axles, NumAxl** — 车轴数量 `2`（默认）| `scalar`

车轴数量，*Na*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumAxl` |
| **值：** | `2`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Number of wheels by axle, NumWhlsByAxl** — 每轴车轮数量 `[2 2]`（默认）| `vector`

每轴车轮数量，*Nta*，无量纲。向量为 `1` 乘以车辆车轴数量，*Na*。例如，`[1,2]` 表示第一轴有一个车轮，第二轴有两个车轮。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumWhlsByAxl` |
| **值：** | `[2 2]`（默认）| `vector` |
| **数据类型：** | `double` |

### **Steered axle enable by axle, StrgEnByAxl** — 用于启用车轴转向的布尔向量 `[1 0]`（默认）| `vector`

用于启用车轴转向的布尔向量，
*Ensteer*，无量纲。向量大小为
`1` × 车辆车轴数，
*Na*。例如：

- `[1 0]`—对于两轴车辆，启用一轴
  转向并禁用二轴转向
- `[1 1]`—对于两轴车辆，启用一轴和
  二轴转向

#### 依赖关系

将 **Steered axle enable by axle,
StrgEnByAxl** 向量的某个元素设置为 1：

- 创建输入端口 `StrgAng`。
- 创建以下参数

  - **Toe angle vs steering angle slope,
    ToeStrgSlp**
  - **Caster angle vs steering angle slope,
    CasterStrgSlp**
  - **Camber angle vs steering angle slope,
    CamberStrgSlp**
  - **Suspension height vs steering angle slope,
    StrgHgtSlp**

例如，对于每轴有两个车轮的两轴车辆，您可以为第一轴上的两个车轮输入转向角。

- 要启用 **StrgAng** 端口，请将 **Steered axle enable by
  axle, StrgEnByAxl** 设置为 `[1 0]`。输入信号数组
  维度为 `[1x2]`。
- `StrgAng` 信号包含两个转向角，分别对应
  其车轴和车轮位置。

  StrgAng=δsteer=[δsteer1,1δsteer1,2]

  | 车轮 | 数组元素 | 车轴 | 车轮编号 |
  | --- | --- | --- | --- |
  | 左前 | `StrgAng(1,1)` | `1` | `1` |
  | 右前 | `StrgAng(1,2)` | `1` | `2` |

#### 程序化使用

要以程序化方式设置模块参数
值，请使用 `set_param` 函数。

要以程序化方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgEnByAxl` |
| **值：** | `[1 0]`（默认）| `vector` |
| **数据类型：** | `double` |

### **Axle and wheels lumped principal moments of inertia about longitudinal axis, AxlIxx** — 转动惯量 `200`（默认）| `vector`

车轴和车轮绕纵轴的总主转动惯量，
*AxlIxx*，单位为 kg\*m^2。

向量大小为 `1` × 车辆车轴数，
*Na*。如果提供标量值，模块
将对所有车轴使用该值。

#### 程序化使用

要以程序化方式设置模块参数
值，请使用 `set_param` 函数。

要以程序化方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AxlIxx` |
| **值：** | `200`（默认）| `vector` |
| **数据类型：** | `double` |

### **Axle and wheels lumped mass, AxlM** — 质量 `300`（默认）| `vector`

车轴和车轮的总质量，*AxlM*，单位为 kg。

向量大小为 `1` × 车辆车轴数，
*Na*。如果提供标量值，模块
将对所有车轴使用该值。

#### 程序化使用

要以程序化方式设置模块参数
值，请使用 `set_param` 函数。

要以程序化方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AxlM` |
| **值：** | `300`（默认）| `vector` |
| **数据类型：** | `double` |

### **Track hardpoint coordinates relative to axle center, TrackCoords** — 点 `[0 0 0 0;-1 1 -1 1;0 0 0 0]`（默认）| `array`

Track hardpoint coordinates，*Tct*，沿
solid axle 的 *x*、*y* 和
*z* 轴，单位为 m。

例如，对于每轴两个车轮的两轴车辆，
`TrackCoords` 数组：

- 维度为 `[3x4]`。
- 根据其轴和车轮位置包含四个 track hardpoint coordinates。

  Tct=[xw1,1xw1,2xw2,1xw2,2yw1,1yw1,2yw2,1yw2,2zw1,1zw1,2zw2,1zw2,2]

  | 数组元素 | 轴 | 车轮编号 | 坐标轴 |
  | --- | --- | --- | --- |
  | `TrackCoords(1,1)` | `1` | `1` | Solid axle *x*-axis |
  | `TrackCoords(1,2)` | `1` | `2` |
  | `TrackCoords(1,3)` | `2` | `1` |
  | `TrackCoords(1,4)` | `2` | `2` |
  | `TrackCoords(2,1)` | `1` | `1` | Solid axle *y*-axis |
  | `TrackCoords(2,2)` | `1` | `2` |
  | `TrackCoords(2,3)` | `2` | `1` |
  | `TrackCoords(2,4)` | `2` | `2` |
  | `TrackCoords(3,1)` | `1` | `1` | Solid axle *z*-axis |
  | `TrackCoords(3,2)` | `1` | `2` |
  | `TrackCoords(3,3)` | `2` | `1` |
  | `TrackCoords(3,4)` | `2` | `2` |

#### 编程使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TrackCoords` |
| **值**：| `[0 0 0 0;-1 1 -1 1;0 0 0 0]`（默认）| `array` |
| **Data Types:** | `double` |

### **Suspension hardpoint coordinates relative to axle center, SuspCoords** — 点 `[0 0 0 0;-1 1 -1 1;0 0 0 0]`（默认）| `array`

Suspension hardpoint coordinates，*Sct*，
沿 solid axle 的 *x*-、*y*- 和
*z*-轴，单位为 m。

例如，对于每轴两个车轮的两轴车辆，
`SuspCoords` 数组：

- 维度为 `[3x4]`。
- 根据其轴和 track 位置包含四个 track hardpoint coordinates。

  Sct=[xs1,1xs1,2xs2,1xs2,2ys1,1ys1,2ys2,1ys2,2zs1,1zs1,2zs2,1zs2,2]

  | 数组元素 | 轴 | Track | 坐标轴 |
  | --- | --- | --- | --- |
  | `SuspCoords(1,1)` | `1` | `1` | Solid axle *x*-axis |
  | `SuspCoords(1,2)` | `1` | `2` |
  | `SuspCoords(1,3)` | `2` | `1` |
  | `SuspCoords(1,4)` | `2` | `2` |
  | `SuspCoords(2,1)` | `1` | `1` | Solid axle *y*-axis |
  | `SuspCoords(2,2)` | `1` | `2` |
  | `SuspCoords(2,3)` | `2` | `1` |
  | `SuspCoords(2,4)` | `2` | `2` |
  | `SuspCoords(3,1)` | `1` | `1` | Solid axle *z*-axis |
  | `SuspCoords(3,2)` | `1` | `2` |
  | `SuspCoords(3,3)` | `2` | `1` |
  | `SuspCoords(3,4)` | `2` | `2` |

#### 编程使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SuspCoords` |
| **值**：| `[0 0 0 0;-1 1 -1 1;0 0 0 0]`（默认）| `array` |
| **Data Types:** | `double` |

### **Wheel and axle interface compliance constant, KzWhlAxl** — 弹簧刚度 `6437000`（默认）| `scalar`

Wheel and axle interface compliance constant，
*kwaz*，单位为 N/m。

#### 编程使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `KzWhlAxl` |
| **值**：| `6437000`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Wheel and axle interface compliance preload, F0zWhlAxl** — 弹簧刚度 `9810`（默认）| `scalar`

Wheel and axle interface compliance preload，
*Fwaz0*，单位为 N。

#### 编程使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `F0zWhlAxl` |
| **值**：| `9810`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Wheel and axle interface damping constant, CzWhlAxl** — 阻尼 `10000`（默认）| `scalar`

Wheel and axle interface damping constant，
*cwaz*，单位为 m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CzWhlAxl` |
| **值：** | `10000`（默认）| `scalar` |
| **数据类型：** | `double` |

### Suspension

#### 柔度和阻尼 - 被动

### **悬架弹簧刚度，Kz** — 悬架弹簧刚度 `64370`（默认）| `scalar` | `vector`

车轴 a 上独立悬架车轮的线性垂直弹簧刚度，
*kza*，单位为
N/m。

向量为 `1` 乘车辆车轴数，
*Na*。如果提供标量值，模块
将该值用于所有车轴。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kz` |
| **值：** | `64370`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **悬架弹簧预载，F0z** — 悬架弹簧预载 `9810`（默认）| `scalar` | `vector`

在轮架参考坐标处施加到车轴上车轮的垂直预载弹簧力，
*Fz0a*，单位为 N。
正预载力：

- 使车辆抬升。
- 沿惯性固定
  *z* 轴负方向。

向量为 `1` 乘车辆车轴数，
*Na*。如果提供标量值，模块
将该值用于所有车轴。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `F0z` |
| **值：** | `9810`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **悬架减振器阻尼常数，Cz** — 悬架减振器阻尼常数 `10000`（默认）| `scalar` | `vector`

车轴 a 上独立悬架车轮的线性垂直阻尼常数，
*cza*，单位为
Ns/m。

向量为 `1` 乘车辆车轴数，
*Na*。如果提供标量值，模块
将该值用于所有车轴。

#### 依赖关系

要创建此参数，请清除 **Enable active
damping**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cz` |
| **值：** | `10000`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **悬架最大高度，Hmax** — 高度 `0.5`（默认）| `scalar` | `vector`

车轴 `a` 在悬架达到硬限位之前的最大悬架伸张或最小悬架压缩高度，
*Hmax*，单位为 m。

向量为 `1` 乘车辆车轴数，
*Na*。如果提供标量值，模块
将该值用于所有车轴。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Hmax` |
| **值：** | `0.5`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

#### 几何

### **转向中心处的前束角，Toe** — 前束角 `0.0349`（默认）| `scalar`

零转向角处的标称悬架前束角，
*ζ0a*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Toe` |
| **值：** | `0.0349`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Roll steer vs suspension height slope, RollStrgSlp** — 转向角悬架斜率 `-0.2269`（默认）| `scalar` | `vector`

侧倾转向角与悬架高度的关系，
*mhtoea*，
单位为 rad/m。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，该模块
将该值用于所有车轴。

#### 程序化使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RollStrgSlp` |
| **值：** | `-0.2269`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **Toe angle vs steering angle slope, ToeStrgSlp** — 前束角转向斜率 `0.01`（默认）| `scalar` | `vector`

前束角与转向角的斜率，
*mtoesteera*，
无量纲。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，该模块
将该值用于所有车轴。

#### 依赖关系

要启用端口 **StrgAng**，请将 **Steered axle
enable by axle, StrgEnByAxl** 向量的一个元素设置为 `1`。

#### 程序化使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ToeStrgSlp` |
| **值：** | `0.01`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **Caster angle at steering center, Caster** — 转向中心处的主销后倾角 `0.0698`（默认）| `scalar`

零转向角时的标称悬架主销后倾角，
*η0a*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Caster` |
| **值：** | `0.0698`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Caster angle vs suspension height slope, CasterHslp** — 主销后倾角与悬架高度斜率 `-0.2269`（默认）| `scalar` | `vector`

主销后倾角与悬架高度的关系，
*mhcastera*，
单位为 rad/m。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，该模块
将该值用于所有车轴。

#### 程序化使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CasterHslp` |
| **值：** | `-0.2269`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **Caster angle vs steering angle slope, CasterStrgSlp** — 主销后倾角与转向角斜率 `0.01`（默认）| `scalar` | `vector`

主销后倾角与转向角的斜率，
*mcastersteera*，
无量纲。

向量为 `1` 乘车辆轴数，
*Na*。如果提供标量值，该模块
将该值用于所有车轴。

#### 依赖关系

要启用端口 **StrgAng**，请将 **Steered axle
enable by axle, StrgEnByAxl** 向量的一个元素设置为 `1`。

#### 程序化使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CasterStrgSlp` |
| **值：** | `0.01`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **Camber angle at steering center, Camber** — 转向中心处的车轮外倾角 `0.0698`（默认）| `scalar`

零转向角时的标称悬架车轮外倾角，
*ξ0a*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Camber` |
| **值：** | `0.0698`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Camber angle vs suspension height slope, CamberHslp** — 车轮外倾角与悬架高度斜率 `-0.2269`（默认）| `scalar` | `vector`

车轮外倾角与悬架高度之比，
*mhcambera*，
单位为 rad/m。

向量大小为 `1` × 车辆轴数，
*Na*。如果提供标量值，该模块
对所有轴使用该值。

#### 程序化使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CamberHslp` |
| **值：** | `-0.2269`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **Camber angle vs steering angle slope, CamberStrgSlp** — 车轮外倾角与转向角斜率 `0.01`（默认）| `scalar` | `vector`

车轮外倾角与转向角斜率，
*mcambersteera*，
无量纲。

向量大小为 `1` × 车辆轴数，
*Na*。如果提供标量值，该模块
对所有轴使用该值。

#### 依赖关系

要启用端口 **StrgAng**，请将 **Steered axle
enable by axle, StrgEnByAxl** 向量的某个元素设置为 `1`。

#### 程序化使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CamberStrgSlp` |
| **值：** | `0.01`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

### **Suspension height vs steering angle slope, StrgHgtSlp** — 悬架高度与转向角斜率 `0.1432`（默认）| `scalar` | `vector`

转向角与施加在悬架车轮托架
参考点处的垂直力之比，
*mhsteera*，单位为
m/rad。

向量大小为 `1` × 车辆轴数，
*Na*。如果提供标量值，该模块
对所有轴使用该值。

#### 依赖关系

要启用端口 **StrgAng**，请将 **Steered axle
enable by axle, StrgEnByAxl** 向量的某个元素设置为 `1`。

#### 程序化使用

要以编程方式设置模块参数
值，请使用 `set_param` 函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgHgtSlp` |
| **值：** | `0.1432`（默认）| `scalar` | `vector` |
| **数据类型：** | `double` |

## 所属库

Vehicle Dynamics Blockset / Suspension

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2022b：参数名称从 `NumTracksByAxl` 更改为 `NumWhlsByAxl`

**Number of tracks by axle, NumTracksByAxl** 参数已重命名
为 **Number of wheels by axle, NumWhlsByAxl**。

该模块使用每轴车轮数来索引
输入和输出模块信号。

## 描述

多轴整体桥悬架

整体桥悬架模块为多轴、每轴多轮的情况实现整体桥悬架。

该模块将悬架的柔度、阻尼和几何效应建模为车轮位置和速度的函数，并具有各轴特定的柔度和阻尼参数。利用车轮位置和速度，该模块计算垂直车轮位置以及作用在车辆和车轮上的悬架力。该模块使用 *Z* 向下坐标系（定义于 SAE J670）和整体桥坐标系。整体桥坐标系与 *Z* 向下车辆坐标系对齐，其 *x* 轴指向车辆前进方向。

整体桥示意图

下表描述了可为每个悬架元件指定的设置。

| 悬架元件 | 设置 |
| --- | --- |
| 车轴 | - 多个车轮 - 悬架参数 |
| 车轮 | - 转向角 |

该模块包含储能弹簧元件和耗能阻尼器元件。该模块还通过车轴侧倾角加速度以及车轴质心垂直和横向加速度存储能量。

下表总结了具有以下配置的车辆的模块参数设置：

- 两个车轴
- 每轴两个车轮
- 前轴两个车轮的转向角输入

| 参数 | 设置 |
| --- | --- |
| **Number of axles, NumAxl** | `2` |
| **Number of wheels by axle, NumWhlsByAxl** | `[2 2]` |
| **Steered axle enable by axle, StrgEnByAxl** | `[1 0]` |

该模块使用车轮编号 *t* 来索引输入和输出信号。下表总结了具有以下配置的车辆的车轮、车轴及对应车轮编号：

- 两个车轴
- 每轴两个车轮

| 车轮 | 车轴 | 车轮编号 |
| --- | --- | --- |
| 左前 | 前 | `1` |
| 右前 | 前 | `2` |
| 左后 | 后 | `1` |
| 右后 | 后 | `2` |

### Suspension Compliance and Damping

该模块使用线性弹簧和阻尼器来建模悬架系统对车辆和车轮的垂向动力学效应。具体而言，该模块：

| 使用 | 计算 |
| --- | --- |
| - 车辆的纵向和横向位移与速度。 - 车轮的纵向和横向位移与速度。 - 施加到车辆上的垂向车轮力。 | - 施加到车轴中心的悬架力。 - 车辆和车轮的垂向位移与速度。 - 施加到车辆上的纵向、横向和垂向悬架力与力矩。 - 施加到车轮上的纵向、横向和垂向悬架力与力矩。 |

为计算车轴的动力学，该模块实现以下方程。该模块忽略以下效应的影响：

- 横向和纵向平动速度。
- 绕垂向轴和横向轴的角速度。

[x¨ay¨az¨a]=1Ma[FxaFyaFza]+[x˙ay˙az˙a]×[pqr]=1Ma[00Fza]+[00z˙a]×[p00]+[00g]=[0pz˙aFzaMa+g][p˙q˙r˙]=[[MxMyMz]−[pqr]×[Ixx000Iyy000Izz][pqr]][Ixx000Iyy000Izz]−1=[[Mx00]−[pq0]×[Ixx000Iyy000Izz][p00]][Ixx000Iyy000Izz]−1=[MxIxx00]

车轴质心上的净垂向力是作用在车轴上的车轮力和悬架力之和。

Fza=∑t=1Nta(Fwza,t+Fz0a+kza(zva,t−zsa,t+mhsteera|δsteera,t|)+cza(z˙va,t−z˙sa,t))

整体式车轴悬架绕侧倾轴的净力矩考虑了悬架和车轮的硬点坐标。

Mx=∑t=1Nta(Fwza,tywt+(Fz0a+kza(zva,t−zsa,t+mhsteera|δsteera,t|)+cza(z˙va,t−z˙sa,t))yst+Mwxa,tIxxIxx+Maywt)

模块参数提供轮距和悬架硬点坐标。

Tct=[xw1xw2…yw1yw2…zw1zw2…]Sct=[xs1xs2…ys1ys2…zs1zs2…]

该模块使用欧拉角将轮距和悬架位移、速度及加速度变换到车辆坐标系。

为计算施加到车辆上的悬架力，该模块实现以下方程。

Fvza,t=−(Fz0a+kza(zva,t−zsa,t+mhsteera|δsteera,t|)+cza(z˙va,t−z˙sa,t)+Fzhstopa,t)

施加到车辆上的悬架力和力矩等于施加到车轮上的悬架力和力矩。

Fvxa,t=Fwxa,tFvya,t=Fwya,tFvza,t=−Fwza,tMvxa,t=Mwxa,t+Fwya,t(Rewya,t+Ha,t)Mvya,t=Mwya,t+Fwxa,t(Rewxa,t+Ha,t)Mvza,t=Mwza,t

为计算施加到车轮位置处悬架的垂向力，该模块实现一个刚性弹簧-阻尼器，如下所示。

整体式车轴上的弹簧阻尼器示意图。

该模块使用以下方程。

Fwza,t=−Fwaz0−kwaz(zwa,t−zsa,t)−cwaz(z˙wa,t−z˙sa,t)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Fwza,t*, *Mwza,t* | 沿车轮固定 *z* 轴施加在轴 `a`、车轮 `t` 上的悬架力和力矩 |
| *Fwxa,t*, *Mwxa,t* | 沿车轮固定 *x* 轴施加在轴 `a`、车轮 `t` 上的悬架力和力矩 |
| *Fwya,t*, *Mwya,t* | 沿车轮固定 *y* 轴施加在轴 `a`、车轮 `t` 上的悬架力和力矩 |
| *Fvza,t*, *Mvza,t* | 沿车轮固定 *z* 轴施加在车辆上、轴 `a`、车轮 `t` 处的悬架力和力矩 |
| *Fvxa,t*, *Mvxa,t* | 沿车轮固定 *x* 轴施加在车辆上、轴 `a`、车轮 `t` 处的悬架力和力矩 |
| *Fvya,t*, *Mvya,t* | 沿车轮固定 *y* 轴施加在车辆上、轴 `a`、车轮 `t` 处的悬架力和力矩 |
| *Fz0a* | 施加在轴 `a` 上车轮的垂直悬架弹簧预紧力 |
| *kza* | 施加在轴 `a` 上车轮的垂直弹簧常数 |
| *kwaz* | 车轮与轴接口柔度常数 |
| *mhsteera* | 施加在轴 `a` 上车轮转向节处的转向角对垂直力斜率 |
| *δsteera,t* | 轴 `a`、车轮 `t` 的转向角输入 |
| *cza* | 施加在轴 `a` 上车轮的垂直阻尼常数 |
| *cwaz* | 车轮与轴接口阻尼常数 |
| *Rewa,t* | 轴 `a`、车轮 `t` 的有效车轮半径 |
| *Fzhstopa,t* | 轴 `a`、车轮 `t` 处沿惯性固定 *z* 轴的垂直硬限位力 |
| *Fzaswya,t* | 轴 `a`、车轮 `t` 处沿惯性固定 *z* 轴的垂直防侧倾力 |
| *Fwaz0* | 车轮与轴接口柔度常数 |
| *zva,t*, *żva,t* | 轴 `a`、车轮 `t` 处沿惯性固定 *z* 轴的车辆位移和速度 |
| *zwa,t*, *żwa,t* | 轴 `a`、车轮 `t` 处沿惯性固定 *z* 轴的车轮位移和速度 |
| *xva,t*, *ẋva,t* | 轴 `a`、车轮 `t` 处沿惯性固定 *z* 轴的车辆位移和速度 |
| *xwa,t*, *ẋwa,t* | 轴 `a`、车轮 `t` 处沿惯性固定 *z* 轴的车轮位移和速度 |
| *yva,t*, *ẏva,t* | 轴 `a`、车轮 `t` 处沿惯性固定 *y* 轴的车辆位移和速度 |
| *ywa,t*, *ẏwa,t* | 轴 `a`、车轮 `t` 处沿惯性固定 *y* 轴的车轮位移和速度 |
| *Ha,t* | 轴 `a`、车轮 `t` 处的悬架高度 |
| *Rewa,t* | 轴 `a`、车轮 `t` 处的有效车轮半径 |

### 硬限位力

模块施加的硬限位反馈力 *Fzhstopa,t* 取决于悬架是在压缩还是在伸张。模块在以下情况下施加该力：

- 在压缩时，当悬架压缩量超过 **Suspension maximum height, Hmax** 参数指定的最大距离
- 在伸张时，当悬架伸张量大于 **Suspension maximum height, Hmax** 参数指定的最大伸张量

为计算该力，模块使用基于双曲正切和指数缩放的刚度。

### Camber, Caster, and Toe Angles

为计算外倾角、主销后倾角和前束角，模块使用悬架高度和转向角的线性函数。

ξa,t=ξ0a+mhcambera(zwa,t−zva,t−mhsteera|δsteera,t|)+mcambersteera|δsteera,t|ηa,t=η0a+mhcastera(zwa,t−zva,t−mhsteera|δsteera,t|)+mcastersteera|δsteera,t|ζa,t=ζ0a+mhtoea(zwa,t−zva,t−mhsteera|δsteera,t|)+mtoesteera|δsteera,t|

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ξa,t* | 轴 `a`、车轮 `t` 上车轮的外倾角 |
| *ηa,t* | 轴 `a`、车轮 `t` 上车轮的主销后倾角 |
| *ζa,t* | 轴 `a`、车轮 `t` 上车轮的前束角 |
| *ξ0a*、*η0a*、*ζ0a* | 轴 a 在零转向角下的标称悬架外倾角、主销后倾角和前束角 |
| *mhcambera*、*mhcastera*、*mhtoea* | 轴 `a` 的外倾角、主销后倾角和前束角分别相对于悬架高度的斜率 |
| *mcambersteera*、*mcastersteera*、*mtoesteera* | 轴 `a` 的外倾角、主销后倾角和前束角分别相对于转向角的斜率 |
| *mhsteera* | 轴 `a` 的转向角相对于垂向力的斜率 |
| *δsteera,t* | 轴 `a`、车轮 `t` 的转向角输入 |
| *zva,t* | 轴 `a`、车轮 `t` 沿惯性固定 *z* 轴的车辆位移 |
| *zwa,t* | 轴 `a`、车轮 `t` 沿惯性固定 *z* 轴的车轮位移 |

### Steering Angles

可选地，使用 **Steered axle enable by axle, StrgEnByAxl** 参数输入车轮的转向角。为计算车轮的转向角，模块使用悬架高度的线性函数对输入转向角进行偏移。

δwhlsteera,t=δsteera,t+mhtoea(zwa,t−zva,t−mhsteera|δsteera,t|)+mtoesteera|δsteera,t|

该方程使用以下变量。

|  |  |
| --- | --- |
| *mtoesteera* | 轴 `a` 前束角相对于转向角的斜率 |
| *mhsteera* | 轴 `a` 转向角相对于垂向力的斜率 |
| *mhtoea* | 轴 `a` 前束角相对于悬架高度的斜率 |
| *δwhlsteera,t* | 轴 `a`、车轮 `t` 的车轮转向角 |
| *δsteera,t* | 轴 `a`、车轮 `t` 的转向角输入 |
| *zva,t* | 轴 `a`、车轮 `t` 沿惯性固定 *z* 轴的车辆位移 |
| *zwa,t* | 轴 `a`、车轮 `t` 沿惯性固定 *z* 轴的车轮位移 |

### Power and Energy

模块为每个轴 `a`、车轮 `t` 计算以下悬架特性。

| 计算 | 方程 |
| --- | --- |
| 耗散功率，*Psuspa,t* | Psuspa,t=Fwzlookupa(z˙va,t−z˙wa,t,z˙va,t−z˙wa,t,δsteera,t) |
| 吸收能量，*Esuspa,t* | Esuspa,t=Fwzlookupa(z˙va,t−z˙wa,t,z˙va,t−z˙wa,t,δsteera,t) |
| 悬架高度，*Ha,t* | Ha,t=−(zva,t−zwa,t+Fz0akza+mhsteera|δsteera,t|) |
| 从车轮托架中心到轮胎/道路界面的距离 | zwtra,t=Rewa,t+Ha,t |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *mhsteera* | 轴 `a` 上车轮施加在车轮托架处的转向角相对于垂向力的斜率 |
| *δsteera,t* | 轴 `a`、车轮 `t` 的转向角输入 |
| *Rewa,t* | 轴 `a`、车轮 `t` 从车轮托架中心到轮胎/道路界面的有效车轮半径 |
| *Fz0a* | 施加到轴 `a` 上车轮的垂向悬架弹簧预紧力 |
| *zwtra,t* | 沿惯性固定 *z* 轴从车轮托架中心到轮胎/道路界面的距离 |
| *zva,t*、*żva,t* | 轴 `a`、车轮 `t` 沿惯性固定 *z* 轴的车辆位移和速度 |
| *zwa,t*、*żwa,t* | 轴 `a`、车轮 `t` 沿惯性固定 *z* 轴的车轮位移和速度 |
