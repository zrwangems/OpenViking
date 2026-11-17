---
type: simulink-block
title: 'C28x Hardware Interrupt'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Scheduling'
documentation_page: 'c28xhardwareinterrupt'
documentation_source_path: 'ref/c28xhardwareinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# C28x Hardware Interrupt

## 端口

### 输入

### **SimIRQ** — 仿真中断输入端口 标量

当您启用 SimIRQ 输入端口时，该中断模块在仿真中发起函数调用。但是，**SimIRQ** 在生成的代码中被忽略。

#### 依赖关系

要启用 **SimIRQ** 端口，请选择 **Enable simulation port** 参数。

**数据类型：** `Boolean`
### 输出

### **IRQ** — 生成中断请求 `Scalar`

该模块的输出是一个函数调用。函数调用线的大小等于该模块设置为处理的中断数量。

## 参数

### **CPU interrupt number** — 指定 CPU 中断向量 `[1 1]`（默认）| [1, 8] 范围内的整数

输入您想要异步处理的中断的 CPU 中断编号向量。

### **PIE interrupt number** — 指定 PIE 中断向量 `[1 2]`（默认）

输入您想要异步处理的中断的 PIE 中断编号向量。

### **Simulink task priorities** — 提供与异步中断关联的任务的相对重要性 `[30 26]`（默认）

输入您想要异步处理的中断的任务优先级向量。

任务优先级表示与异步中断关联的任务的相对重要性。此字段中的最小值表示最高优先级。基本速率任务的默认优先级值为 40，因此每个异步触发任务的优先级值必须小于 40（以将其配置为更高优先级），这些任务才能抢占基本速率任务。

### **Preemption flags: preemptable-1, non-preemptable-0** — 指定中断的抢占标志向量 `0 0`（默认）

输入您想要异步处理的中断的抢占标志向量。

抢占标志决定给定中断是否可抢占。抢占优先于优先级排序，如果某个中断在较低优先级任务运行时触发了较高优先级任务，则较低优先级任务的执行可以被挂起，并在较高优先级任务完成后恢复，前提是较低优先级任务被配置为可抢占。

### **Enable simulation input** — 启用仿真端口以阻止 `off`（默认）| `on`

选择此参数以添加兼容的仿真输入端口。

选择此参数使您能够在 Simulink® 软件模型的上下文中测试异步中断处理。

### PIE 和 CPU 中断编号

每个中断由 CPU 中断编号、PIE 中断编号、任务优先级和抢占标志来描述。

CPU 和 PIE 中断编号共同唯一地指定单个外设或外设模块的单个中断。

支持 12×8 中断的 C28x 处理器 F280013x 的 PIE 和 CPU 中断编号为：

**F280013x 处理器的 PIE 和 CPU 中断编号**

| PIE ⇒ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | ADCA1 | ADCC1 | - | XINT1 | XINT2 | SYS\_ERR | TIMER0 | WAKE |
| 2 | EPWM1\_TZ | EPWM2\_TZ | EPWM3\_TZ | EPWM4\_TZ | EPWM5\_TZ | EPWM6\_ TZ | EPWM7\_TZ |  |
| 3 | EPWM1 | EPWM2 | EPWM3 | EPWM4 | EPWM5 | EPWM6 | EPWM7 |  |
| 4 | ECAP1 | ECAP2 | - | - | - | - | - |  |
| 5 | EQEP1 | - | - | - | - | - | - |  |
| 6 | SPIA\_RX | SPIA\_TX | - | - | - | - | DCC0 |  |
| 7 | - | - | - | - | - | - | - | - |
| 8 | I2CA | I2CA\_FIFO | I2CB | I2CB\_FIFO | SCIC\_RX | SCIC\_TX | - | - |
| 9 | SCIA\_RX | SCIA\_TX | SCIB\_RX | SCIB\_TX | CANA\_0 | CANA\_1 | - | - |
| 10 | ADCA\_EVT | ADCA2 | ADCA3 | ADCA4 | ADCC\_EVT | ADCC2 | ADCC3 | ADCC4 |
| 11 | - | - | - | - | - | - | - | - |
| 12 | XINT3 | XINT4 | XINT5 | - | FLSS\_INT | - | - | - |

支持 12×8 中断的 C28x 处理器 F280015x 的 PIE 和 CPU 中断编号为：

**F280015x 处理器的 PIE 和 CPU 中断编号**

| PIE ⇒ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | ADCA1 | ADCC1 | - | XINT1 | XINT2 | SYS\_ERR | TIMER0 | WAKE |
| 2 | EPWM1\_TZ | EPWM2\_TZ | EPWM3\_TZ | EPWM4\_TZ | EPWM5\_TZ | EPWM6\_ TZ | EPWM7\_TZ |  |
| 3 | EPWM1 | EPWM2 | EPWM3 | EPWM4 | EPWM5 | EPWM6 | EPWM7 |  |
| 4 | ECAP1 | ECAP2 | ECAP3 | - | - | - | - |  |
| 5 | EQEP1 | EQEP2 | - | - | - | - | - |  |
| 6 | SPIA\_RX | SPIA\_TX | - | - | LINA\_0 | LINA\_1 | DCC0 |  |
| 7 | - | - | - | - | - | - | PMBUSA | - |
| 8 | I2CA | I2CA\_FIFO | I2CB | I2CB\_FIFO | SCIC\_RX | SCIC\_TX | - | - |
| 9 | SCIA\_RX | SCIA\_TX | SCIB\_RX | SCIB\_TX | CANA\_0 | CANA\_1 | MCANSS0 | MCANSS1 |
| 10 | ADCA\_EVT | ADCA2 | ADCA3 | ADCA4 | ADCC\_EVT | ADCC2 | ADCC3 | ADCC4 |
| 11 | - | - | - | - | - | - | - | - |
| 12 | XINT3 | XINT4 | XINT5 | - | FLSS\_INT | VCRC | MCANSS WAKE AND TS PLS | MCANSS ECC CORR PLS |

支持 12×16 中断的 TI 处理器 F28P65x 的 PIE 和 CPU 中断编号为：

**F28P65x 处理器的 PIE 和 CPU 中断编号**

| PIE ⇒ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | ADCA1 | ADCB1 | ADCC1 | XINT1 | XINT2 | - | TIMER 0 | WAKE / WDOG |
| 2 | EPWM1\_TZ | EPWM2\_TZ | EPWM3\_TZ | EPWM4\_TZ | EPWM5\_TZ | EPWM6\_ TZ | EPWM7\_TZ | EPWM8\_TZ |
| 3 | EPWM1 | EPWM2 | EPWM3 | EPWM4 | EPWM5 | EPWM6 | EPWM7 | EPWM8 |
| 4 | ECAP1 | ECAP2 | ECAP3 | ECAP4 | ECAP5 | ECAP6 | ECAP7 | Reserved |
| 5 | EQEP1 | EQEP2 | EQEP3 | EQEP4 | CLB1 | CLB2 | CLB3 | CLB4 |
| 6 | SPIA\_RX | SPIA\_TX | SPIB\_RX | SPIB\_TX | LINA\_0 | LINA\_1 | LINB\_0 | LINB\_1 |
| 7 | DMA\_CH1 | DMA\_CH2 | DMA\_CH3 | DMA\_CH4 | DMA\_CH5 | DMA\_CH6 | EQEP\_5 | EQEP\_6 |
| 8 | I2CA | I2CA\_FIFO | I2CB | I2CB\_FIFO | UARTA\_INT | UARTB\_INT | EPWM17\_TZ | EPWM18\_TZ |
| 9 | SCIA\_RX | SCIA\_TX | SCIB\_RX | SCIB\_TX | DCANA\_1 | DCANA\_2 | EPWM17 | EPWM18 |
| 10 | ADCA\_EVT | ADCA2 | ADCA3 | ADCA4 | ADCB\_EVT | ADCB2 | ADCB3 | ADCB4 |
| 11 | CPU1\_CLA1\_1 | CPU1\_CLA1\_2 | CPU1\_CLA1\_3 | CPU1\_CLA1\_4 | CPU1\_CLA1\_5 | CPU1\_CLA1\_6 | CPU1\_CLA1\_7 | CPU1\_CLA1\_8 |
| 12 | XINT3 | XINT4 | XINT5 | CPU1\_MPOST\_INT | FLSS\_INT | - | FPU\_OVERFLOW | FPU\_UNDERFLOW |

| PIE ⇒ | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | I2CA | SYS\_ERR | ECATSYNC0 | ECATINTn | CIPC0 | CIPC1 | CIPC2 | CIPC3 |
| 2 | EPWM9\_TZ | EPWM10\_ TZ | EPWM11\_TZ | EPWM12\_TZ | EPWM13\_TZ | EPWM14\_TZ | EPWM15\_TZ | EPWM16\_TZ |
| 3 | EPWM9 | EPWM10 | EPWM11 | EPWM12 | EPWM13 | EPWM14 | EPWM15 | EPWM16 |
| 4 | FSITXA\_INT1 | FSITXA\_INT2 | FSITXB\_INT1 | FSITXB\_INT2 | FSIRXA\_INT1 | FSIRXA\_INT2 | FSIRXB\_INT1 | FSIRXB\_INT2 |
| 5 | SDFM1 | SDFM2 | ECATRST | ECATSYNC1 | SDFM1DR1 | SDFM1DR2 | SDFM1DR3 | SDFM1DR4 |
| 6 | SPIC\_RX | SPIC\_TX | SPID\_RX | SPID\_TX | SDFM2DR1 | SDFM2DR2 | SDFM2DR3 | SDFM2DR4 |
| 7 | FSITXA\_INT1 | FSITXA\_INT2 | FSIRXA\_INT1 | FSIRXA\_INT2 | SDFM3DR1 | SDFM3DR2 | SDFM3DR3 | SDFM3DR4 |
| 8 | - | - | SDFM3 | SDFM4 | CLB5 | CLB6 | - | - |
| 9 | MCANSS\_A0 | MCANSS\_A1 | MCANSS\_ECC\_CORR\_PLS | MCANSS\_WAKE\_AND\_TS\_PLS | PMBUSA | AES\_INT | USBA | Reserved |
| 10 | ADCC\_EVT | ADCC2 | ADCC3 | ADCC4 | Reserved | Reserved | Reserved | ADCHECKINT |
| 11 | MCANSS\_B0 | MCANSS\_B1 | MCANSS\_BECC\_CORR\_PLS | MCANSS\_B\_WAKE\_AND\_TS\_PLS | SDFM4DR1 | SDFM4DR2 | SDFM4DR3 | SDFM4DR4 |
| 12 | \_ | ECAP6\_INT2 | ECAP7\_INT2 | - | CPU1\_CRC\_INT | CPU1\_CLA1CRC\_INT | CPU1\_CLA OVER FLOW | CPU1\_CLA UNDERFLOW |

支持 12×16 中断的 TI 处理器 F28P55x 的 PIE 和 CPU 中断编号为：

**F28P55x 处理器的 PIE 和 CPU 中断编号**

| PIE ⇒ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | ADCA1 | ADCB1 | ADCC1 | XINT1 | XINT2 | SYS\_ERR | TIMER 0 | WAKE / WDOG |
| 2 | EPWM1\_TZ | EPWM2\_TZ | EPWM3\_TZ | EPWM4\_TZ | EPWM5\_TZ | EPWM6\_ TZ | EPWM7\_TZ | EPWM8\_TZ |
| 3 | EPWM1 | EPWM2 | EPWM3 | EPWM4 | EPWM5 | EPWM6 | EPWM7 | EPWM8 |
| 4 | ECAP1 | ECAP2 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 5 | EQEP1 | EQEP2 | EQEP3 | Reserved | CLB1 | CLB2 | Reserved | Reserved |
| 6 | SPIA\_RX | SPIA\_TX | SPIB\_RX | SPIB\_TX | Reserved | Reserved | DCC0 | DCC1 |
| 7 | DMA\_CH1 | DMA\_CH2 | DMA\_CH3 | DMA\_CH4 | DMA\_CH5 | DMA\_CH6 | PMBUSA | Reserved |
| 8 | I2CA | I2CA\_FIFO | I2CB | I2CB\_FIFO | SCIC\_RX | SCIC\_TX | Reserved | Reserved |
| 9 | SCIA\_RX | SCIA\_TX | SCIB\_RX | SCIB\_TX | Reserved | Reserved | MCANASS0 | MCANASS1 |
| 10 | ADCA\_EVT | ADCA2 | ADCA3 | ADCA4 | ADCB\_EVT | ADCB2 | ADCB3 | ADCB4 |
| 11 | CLA1\_1 | CLA1\_2 | CLA1\_3 | CLA1\_4 | CLA1\_5 | CLA1\_6 | CLA1\_7 | CLA1\_8 |
| 12 | XINT3 | XINT4 | XINT5 | Reserved | FLSS\_INT | Reserved | MCANASS\_WAKE\_AND\_TS\_PLS | MCANASS\_ECC\_CORR\_PLS |

| PIE ⇒ | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | ADCD1 | ADCE1 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 2 | EPWM9\_TZ | EPWM10\_ TZ | EPWM11\_TZ | EPWM12\_TZ | Reserved | Reserved | Reserved | Reserved |
| 3 | EPWM9 | EPWM10 | EPWM11 | EPWM12 | Reserved | Reserved | Reserved | Reserved |
| 4 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 5 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 6 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 7 | Reserved | Reserved | FSITXA\_INT1 | FSITXA\_INT2 | FSIRXA\_INT1 | FSIRXA\_INT2 | Reserved | Reserved |
| 8 | LINA\_0 | LINA\_1 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 9 | MCANBSS0 | MCANBSS1 | MCANBSS\_ECC\_CORR\_PLS | MCANSS\_WAKE\_AND\_TS\_PLS | Reserved | Reserved | USB | NPU |
| 10 | ADCC\_EVT | ADCC2 | ADCC3 | ADCC4 | ADCD\_EVT | ADCD2 | ADCD3 | ADCD4 |
| 11 | ADCE\_EVT | ADCE2 | ADCE3 | ADCE4 | Reserved | Reserved | Reserved | Reserved |
| 12 | \_ | ECAP6\_INT2 | ECAP7\_INT2 | - | CPU1\_CRC\_INT | CPU1\_CLA1CRC\_INT | CPU1\_CLA OVER FLOW | CPU1\_CLA UNDERFLOW |

下表列出了支持 12×8 中断的 c28x 处理器 F280x、F2802x、F2803x、F2805x、F2806x、F2833x、F28M35x 和 F28M36x 的 PIE 和 CPU 中断编号。行标题 1–12 表示 CPU 值，列标题 1–8 表示 PIE 值。

**F280x、F2802x、F2803x、F2805x、F2806x、F2833x、F28M35x 和 F28M36x 处理器的 PIE 和 CPU 中断编号**

| PIE ⇒ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | SEQ1INT (ADC) / ADCINT1 | SEQ2INT (ADC) / ADCINT2 | Reserved | XINT1 | XINT2 | ADCINT / ADCINT9 | TINT0 (TIMER 0) | WAKEINT (LPM/WD) |
| 2 | EPWM1\_TZINT | EPWM2\_TZINT | EPWM3\_TZINT | EPWM4\_TZINT | EPWM5\_TZINT | EPWM6\_ TZINT | EPWM7\_TZINT | EPWM8\_TZINT |
| 3 | EPWM1\_INT | EPWM2\_INT | EPWM3\_INT | EPWM4\_INT | EPWM5\_INT | EPWM6\_ INT | EPWM7\_INT | EPWM8\_INT |
| 4 | ECAP1\_INT | ECAP2\_INT | ECAP3\_INT | ECAP4\_INT | ECAP5\_INT | ECAP6\_INT | EPWM10\_TZINT / HRCAP1\_INT | EPWM9\_TZINT / HRCAP2\_INT |
| 5 | EQEP1\_INT | EQEP2\_INT | EQEP3\_INT | HRCAP3\_INT | HRCAP4\_INT | Reserved | EPWM10\_INT | EPWM9\_INT |
| 6 | SPIRXINTA (SPI-A) | SPITXINTA (SPI-A) | SPIRXINTB (SPIB\_RX) / MRINTB (McBSP-B) | SPITXINTB (SPIB\_TX) / MXINTB (McBSP-B) | SPIRXINTC (SPI-C) / MRINTA (McBSP-A\_RX) | SPITXINTC (SPI-C) / MXINTA (McBSP-A\_TX) | SPIRXINTD (SPI-D) / EPWM12\_TZINT | SPITXINTD (SPI-D) / EPWM11\_TZINT |
| 7 | DINTCH1 (DMA1) | DINTCH2 (DMA2) | DINTCH3 (DMA3) | DINTCH4 (DMA4) | DINTCH5 (DMA5) | DINTCH6 (DMA6) | EPWM12\_INT | EPWM11\_INT |
| 8 | I2CINT1A | I2CINT2A | Reserved | Reserved | SCIRXINTC (SCI-C) | SCITXINTC (SCI-C) | Reserved | Reserved |
| 9 | SCIRXINTA (SCIA\_RX) | SCITXINTA (SCIA\_TX) | SCIRXINTB (SCIB\_RX) / LINA\_INT0 | SCITXINTB (SCIB\_TX) / LINA\_INT1 | ECAN0INTA (CANA\_1) | ECAN1INTA (CANA\_2) | ECAN0INTB (CANB\_1) | ECAN1INTB (CANB\_2) |
| 10 | EPWM9\_TZINT / ADCINT1 | EPWM10\_TZINT / ADCINT2 | EPWM11\_TZINT / ADCINT3 | EPWM12\_TZINT / ADCINT4 | EPWM13\_TZINT / ADCINT5 | EPWM14\_TZINT / ADCINT6 | EPWM15\_TZINT / ADCINT7 | EPWM16\_TZINT / ADCINT8 |
| 11 | CLA1\_INT1 / EPWM9\_INT7 / MTOCIPCINT1 | CLA1\_INT2 / EPWM10\_INT / MTOCIPCINT2 | CLA1\_INT3 / EPWM11\_INT / MTOCIPCINT3 | CLA1\_INT4 / EPWM12\_INT / MTOCIPCINT4 / | CLA1\_INT5 / EPWM13\_INT | CLA1\_INT6 / EPWM14\_INT | CLA1\_INT7 / EPWM15\_INT | CLA1\_INT8 / EPWM16\_INT |
| 12 | XINT3 | XINT4 / C28FLSINGERR | XINT5 | XINT6 / C28RAMSINGERR | XINT7 / C28RAMACCVIOL | Reserved | LVF | LUF |

支持 12×16 中断的 c28x 处理器 F2807x、F2837xS、F2837xD、F2838x、F28004x、F28002x 和 F28003x 的 PIE 和 CPU 中断编号为：

**F2807x、F2837xS、F2837xD、F2838x、F28004x、F28002x 和 F28003x 处理器的 PIE 和 CPU 中断编号**

| PIE ⇒ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | ADCA1 | ADCB1 | ADCC1 | XINT1 | XINT2 | ADCD1 | TIMER 0 | WAKE / WDOG |
| 2 | EPWM1\_TZ | EPWM2\_TZ | EPWM3\_TZ | EPWM4\_TZ | EPWM5\_TZ | EPWM6\_ TZ | EPWM7\_TZ | EPWM8\_TZ |
| 3 | EPWM1 | EPWM2 | EPWM3 | EPWM4 | EPWM5 | EPWM6 | EPWM7 | EPWM8 |
| 4 | ECAP1 | ECAP2 | ECAP3 | ECAP4 | ECAP5 | ECAP6 | ECAP7 | Reserved |
| 5 | EQEP1 | EQEP2 | EQEP3 | Reserved | CLB1 | CLB2 | CLB3 | CLB4 |
| 6 | SPIA\_RX | SPIA\_TX | SPIB\_RX | SPIB\_TX | MCBSPA\_RX | MCBSPA\_TX | MCBSPB\_RX | MCBSPB\_TX |
| 7 | DMA\_CH1 | DMA\_CH2 | DMA\_CH3 | DMA\_CH4 | DMA\_CH5 | DMA\_CH6 | Reserved | Reserved |
| 8 | I2CA | I2CA\_FIFO | I2CB | I2CB\_FIFO | SCIC\_RX | SCIC\_TX | SCID\_RX | SCID\_TX |
| 9 | SCIA\_RX | SCIA\_TX | SCIB\_RX | SCIB\_TX | CANA\_0 | CANA\_1 | CANB\_0 | CANB\_1 |
| 10 | ADCA\_EVT | ADCA2 | ADCA3 | ADCA4 | ADCB\_EVT | ADCB2 | ADCB3 | ADCB4 |
| 11 | CLA1\_1 | CLA1\_2 | CLA1\_3 | CLA1\_4 | CLA1\_5 | CLA1\_6 | CLA1\_7 | CLA1\_8 |
| 12 | XINT3 | XINT4 | XINT5 | MPOST | FMC.DONE | VCU | FPU\_OVERFLOW | FPU\_UNDERFLOW |

| PIE ⇒ | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | I2CA | SYS\_ERR | ECATSYNC0 (CPU1 only) | ECATINTn (CPU1 only) | IPC0/CIPC0 | IPC1/CIPC1 | IPC2/CIPC2 | IPC3/CIPC3 |
| 2 | EPWM9\_TZ | EPWM10\_ TZ | EPWM11\_TZ | EPWM12\_TZ | EPWM13\_TZ | EPWM14\_TZ | EPWM15\_TZ | EPWM16\_TZ |
| 3 | EPWM9 | EPWM10 | EPWM11 | EPWM12 | EPWM13 | EPWM14 | EPWM15 | EPWM16 |
| 4 | FSITXA\_INT1 | FSITXA\_INT2 | FSITXB\_INT1 | FSITXB\_INT2 | FSIRXA\_INT1 | FSIRXA\_INT2 | FSIRXB\_INT1 | FSIRXB\_INT2 |
| 5 | SD1 / SDFM1 | SD2/SDFM1 | ECATRSTINTn (CPU1 only) | ECATSYNC1 (CPU1 only) | SDFM1DR1 | SDFM1DR2 | SDFM1DR3 | SDFM1DR4 |
| 6 | SPIC\_RX | SPIC\_TX | SPID\_RX | SPID\_TX | SDFM2DR1 | SDFM2DR2 | SDFM2DR3 | SDFM2DR4 |
| 7 | FSIRXC\_INT1 | FSIRXC\_INT2 | FSIRXD\_INT1 | FSIRXD\_INT2 | FSIRXE\_INT1 | FSIRXE\_INT2 | FSIRXF\_INT1 | FSIRXF\_INT2 |
| 8 | LINA\_0/FSIRXG\_INT1 | LINA\_1/FSIRXG\_INT2 | FSIRXH\_INT1 | FSIRXH\_INT2 | PMBUSA/CLB5 | CLB6 | UPPA (CPU1 only)/CLB7 | CLB8 |
| 9 | MCANSS\_INT0(CPU1 only) | MCANSS\_INT1 (CPU1 only) | MCANSS\_ECC\_CORR\_PUL\_INT (CPU1 only) | MCANSS\_WAKE\_AND\_TS\_PLS\_INT (CPU1 only) | PMBUSA | CM\_STATUS (CPU1 only) | USBA (CPU1 only) | Reserved |
| 10 | ADCC\_EVT | ADCC2 | ADCC3 | ADCC4 | ADCD\_EVT | ADCD2 | ADCD3 | ADCD4 |
| 11 | CMTOCPUxIPCINTR0 | CMTOCPUxIPCINTR1 | CMTOCPUxIPCINTR2 | CMTOCPUxIPCINTR3 | CMTOCPUxIPCINTR4 | CMTOCPUxIPCINTR5 | CMTOCPUxIPCINTR6 | CMTOCPUxIPCINTR7 |
| 12 | EMIF\_ ERROR | RAM\_CORRECTABLE\_ERROR/ECAP6INT2 | FLASH\_CORRECTABLE\_ERROR/ECAP7INT2 | RAM\_ACCESS\_VIOLATION | SYS\_PLL\_ SLIP/CPUxCRC\_INT | AUX\_PLL\_SLIP//CLA1CRC\_INT | CLA OVER FLOW | CLA UNDERFLOW |

c281x 处理器的 PIE 和 CPU 中断编号为：

**C281x 处理器的 PIE 和 CPU 中断编号**

| PIE ⇒ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPU ⇓ |
| 1 | PDPINTA (EV-A) | PDPINTB (EV-B) | Reserved | XINT1 | XINT2 | ADCINT (ADC) | TINT0 (TIMER 0) | WAKEINT (LPM/WD) |
| 2 | CMP1INT (EV-A) | CMP2INT (EV-A) | CMP3INT (EV-A) | T1PINT (EV-A) | T1CINT (EV-A) | T1UFINT (EV-A) | T1OFINT (EV-A) | Reserved |
| 3 | T2PINT (EV-A) | T2CINT (EV-A) | T2UFINT (EV-A) | T2OFINT (EV-A) | CAPINT1 (EV-A) | CAPINT2 (EV-A) | CAPINT3 (EV-A) | Reserved |
| 4 | CMP4INT (EV-B) | CMP5INT (EV-B) | CMP6INT (EV-B) | T3PINT (EV-B) | T3CINT (EV-B) | T3UFINT (EV-B) | T3OFINT (EV-B) | Reserved |
| 5 | T4PINT (EV-B) | T4CINT (EV-B) | T4UFINT (EV-B) | T4OFINT (EV-B) | CAPINT4 (EV-B) | CAPINT5 (EV-B) | CAPINT6 (EV-B) | Reserved |
| 6 | SPIRXINTA (SPI) | SPITXINTA (SPI) | Reserved | Reserved | MRINT (McBSP) | MXINT (McBSP) | Reserved | Reserved |
| 7 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 8 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 9 | SCIRXINTA (SCI-A) | SCITXINTA (SCI-A) | SCIRXINTB (SCI-B) | SCITXINTB (SCI-B) | ECAN0INT (CAN) | ECAN1INT (CAN) | Reserved | Reserved |
| 10 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 11 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |
| 12 | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved | Reserved |

## 所属库

C2000 Microcontroller Blockset / Scheduling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

用于处理 C28x 处理器上硬件中断的中断服务例程

基于定时器中断的执行调度模型无法满足某些实时应用对外部事件响应的要求。C28x Hardware Interrupt 模块通过允许对其他模块在 C28x DSP Chip Support Library 中管理的事件所触发的异步中断进行处理，解决了这一问题。

当 C28x Hardware Interrupt 模块具有外部中断选择时，该选择会在所选通用 I/O 引脚上使能中断。要配置这些引脚，请参阅 **Configuration Parameters** > **Hardware Implementation** > **Hardware board settings** > **Target hardware resources** > **External Interrupt** 窗格。有关详细信息，请参阅 Model Configuration Parameters for Texas Instruments C2000 Processors。

任务优先级表示与异步中断相关联任务的相对重要性。此字段中的最低值表示最高优先级。基础速率任务的默认优先级值为 40，因此每个异步触发任务的优先级值必须小于 40（以将其配置为更高优先级），这些任务才能抢占基础速率任务。

抢占标志决定给定中断是否可抢占。抢占会覆盖优先级排序，如果某个中断在较低优先级任务正在运行时触发了较高优先级任务，则只要较低优先级任务配置为可抢占，较低优先级任务的执行就可以被挂起，并在较高优先级任务完成后恢复。

### 向量化输出

此模块的输出是函数调用。函数调用行的长度等于该模块设置为处理的中断数。每个中断由模块对话框上显示的四个参数表示。这些参数是一组四个等长向量。每个中断由每个参数中的一个元素表示（共四个元素），每个元素来自这些向量中相同位置的元素。

每个中断由以下内容描述：

- CPU 中断编号
- 外设中断扩展 (PIE) 中断编号
- 任务优先级
- 抢占标志
