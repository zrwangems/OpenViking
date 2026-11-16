---
type: simulink-block
title: 'Serial Transmit'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'serialtransmit'
documentation_source_path: 'freedomboard/ref/serialtransmit.html'
language: en
---

# Serial Transmit

## Ports

Not documented in R2025b.

## Parameters

**UART**
:   Select the UART for the serial communication interface.

    Make sure not to select UART0 when you use external mode because the External
    mode uses UART0 for target to host communication.

**Send mode**
:   To transmit an array of byte data to the UART, set the Send mode parameter to
    putc.

    Select printf value for debugging purposes. You can send an array of any data
    type to the terminal.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Send an [MxN] array of data to the UART

Send an [MXN] array of data to the selected UART.

You can change the Baud Rate and also select the Tx pin for the UARTx Serial Interface
from **Configuration Parameters**  > **Hardware Implementation pane** > **UARTx**.

During simulations without the hardware, this block does nothing.
