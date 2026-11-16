---
type: simulink-block
title: 'MCAN Interrupt Status'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'mcaninterruptstatus'
documentation_source_path: 'ref/mcaninterruptstatus.html'
language: en
---

# MCAN Interrupt Status

## Ports

### Output

### **MCAN\_IR** — Status of MCAN interrupt register uint32

Output port to display entire MCAN\_IR register status as uint32 value.

The flags are set when one of the listed conditions is detected
(edge-sensitive). The flags remain set until the host clears them. A flag is cleared
by writing a `1` to the corresponding bit position. Writing a
`0` has no effect. A hard reset will clear the register.

**MCAN\_IR Register**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bit** | `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31` |
| **Type** | `RF0N` | `RF0W` | `RF0F` | `RF0L` | `RF1N` | `RF1W` | `RF1F` | `RF1L` | `HPM` | `TC` | `TCF` | `TFE` | `TEFN` | `TEFW` | `TEFF` | `TEFL` | `TSW` | `MRAF` | `TOO` | `DRX` | `RESERVED` | `BEU` | `ELO` | `EP` | `EW` | `BO` | `WDI` | `PEA` | `PED` | `ARA` | `RESERVED` | `RESERVED` |

#### Dependencies

To enable this port, select the **MCAN interrupt register
output** parameter.

### **TEFN** — Status of TX event FIFO new entry boolean

Output port to display the transmit (TX) event first in, first out (FIFO) new
entry status. The status port outputs:

- `0` - TX event FIFO unchanged
- `1` - TX handler wrote TX event FIFO element

#### Dependencies

To enable this port, select the **TX event FIFO new
element** parameter.

### **TEFW** — Status of TX event FIFO watermark reached boolean

Output port to display the TX event FIFO watermark reached status. Once the
status is cleared and the FIFO level is still above the watermark level, then the
bit is not enabled. The bit is enabled only while going from low to high. The status
port outputs:

- `0` - TX event FIFO fill level below watermark
- `1` - TX event FIFO fill level reached watermark

#### Dependencies

To enable this port, select the **TX event FIFO
watermark** parameter.

### **TEFF** — Status of TX event FIFO full boolean

Output port to display the TX event FIFO full status. The status port outputs:

- `0` - TX event FIFO not full
- `1` - TX event FIFO full

#### Dependencies

To enable this port, select the **TX event FIFO
full** parameter.

### **TEFL** — Status of TX event FIFO element lost boolean

Output port to display the TX event FIFO element lost status. The status port outputs:

- `0` - No TX Event FIFO element lost
- `1` - TX event FIFO element lost, also set after write
  attempt to TX event FIFO of size zero

#### Dependencies

To enable this port, select the **TX event FIFO element
lost** parameter.

### **TC** — Status of transmission completed boolean

Output port to display the transmission completed status. The status port outputs:

- `0` - No transmission completed
- `1` - Transmission completed

#### Dependencies

To enable this port, select the **Transmission
complete** parameter.

### **TCF** — Status of transmission cancellation finished boolean

Output port to display the transmission cancellation finished status. The status
port outputs:

- `0` - No transmission cancellation finished
- `1` - Transmission cancellation finished

#### Dependencies

To enable this port, select the **Transmission
cancellation finished** parameter.

### **TFE** — Status of transmission FIFO empty boolean

Output port to display the transmission FIFO empty status. The status port outputs:

- `0` - TX FIFO non-empty
- `1` - TX FIFO empty

#### Dependencies

To enable this port, select the **TX FIFO empty**
parameter.

### **HPM** — Status of high priority message boolean

Output port to display the high priority message status. The status port outputs:

- `0` - No high priority message received
- `1` - High priority message received

#### Dependencies

To enable this port, select the **High priority
message** parameter.

### **RF0N** — Status of RX FIFO 0 new message boolean

Output port to display the receive (RX) FIFO 0 new message status. The status
port outputs:

- `0` - No new message written to RX FIFO 0
- `1` - New message written to RX FIFO 0

#### Dependencies

To enable this port, select the **RX FIFO 0 new
message** parameter.

### **RF0W** — Status of RX FIFO 0 watermark reached boolean

Output port to display the receive (RX) FIFO 0 watermark reached status. Once
the status is cleared and the FIFO level is still above the watermark level, then
the bit is not enabled. The bit is enabled only while going from low to high. The
status port outputs:

- `0` - RX FIFO 0 fill level below watermark
- `1` - RX FIFO 0 fill level reached watermark

#### Dependencies

To enable this port, select the **RX FIFO 0
watermark** parameter.

### **RF0FL** — Status of RX FIFO 0 full boolean

Output port to display the receive (RX) FIFO 0 full status. The status port outputs:

- `0` - RX FIFO 0 not full
- `1` - RX FIFO 0 full

#### Dependencies

To enable this port, select the **RX FIFO 0
full** parameter.

### **RF0ML** — Status of RX FIFO 0 message lost boolean

Output port to display the RX FIFO 0 message lost status. The status port outputs:

- `0` - No RX FIFO 0 message lost
- `1` - RX FIFO 0 message lost, also set after write
  attempt to RX FIFO 0 of size zero

#### Dependencies

To enable this port, select the **RX FIFO 0 message
lost** parameter.

### **DRX** — Status of dedicated RX buffer message boolean

Message stored to dedicated RX buffer. The flag is set whenever a received
message has been stored into a dedicated RX Buffer.

The status port outputs:

- `0` - No RX buffer updated
- `1` - At least one received message stored into an RX
  buffer

#### Dependencies

To enable this port, select the **Dedicated RX buffer
message** parameter.

### **RF1N** — Status of RX FIFO 1 new message boolean

Output port to display the receive (RX) FIFO 1 new message status. The status
port outputs:

- `0` - No new message written to RX FIFO 1
- `1` - New message written to RX FIFO 1

#### Dependencies

To enable this port, select the **RX FIFO 1 new
message** parameter.

### **RF1W** — Status of RX FIFO 1 watermark reached boolean

Output port to display the receive (RX) FIFO 1 watermark reached status. Once
the status is cleared and the FIFO level is still above the watermark level, then
the bit is not enabled. The bit is enabled only while going from low to high. The
status port outputs:

- `0` - RX FIFO 1 fill level below watermark
- `1` - RX FIFO 1 fill level reached watermark

#### Dependencies

To enable this port, select the **RX FIFO 1 watermark
reached** parameter.

### **RF1FL** — Status of RX FIFO 1 full boolean

Output port to display the receive (RX) FIFO 1 full status. The status port outputs:

- `0` - RX FIFO 1 not full
- `1` - RX FIFO 1 full

#### Dependencies

To enable this port, select the **RX FIFO 1
full** parameter.

### **RF1ML** — Status of RX FIFO 1 message lost boolean

Output port to display the RX FIFO 1 message lost status. The status port outputs:

- `0` - No RX FIFO 1 message lost
- `1` - RX FIFO 1 message lost, also set after write
  attempt to RX FIFO 1 of size zero

#### Dependencies

To enable this port, select the **RX FIFO 1 message
lost** parameter.

### **TSW** — Status of timestamp wraparound boolean

Output port to display the timestamp wraparound status. The status port outputs:

- `0` - No timestamp counter wrap-around
- `1` - Timestamp counter wrapped around

#### Dependencies

To enable this port, select the **Timestamp
wraparound** parameter.

### **TOO** — Status of timeout occurred boolean

Output port to display the timeout occurred status. The status port outputs:

- `0` - No timeout
- `1` - Timeout reached

#### Dependencies

To enable this port, select the **Timeout
occurred** parameter.

### **ELO** — Status of error logging overflow boolean

Output port to display the error logging overflow status. The status port outputs:

- `0` - CAN error logging counter did not overflow
- `1` - Overflow of CAN error logging counter
  occurred

#### Dependencies

To enable this port, select the **Error logging
overflow** parameter.

### **EW** — Status of error warning boolean

Output port to display the error warning status. The status port outputs:

- `0` - Error warning status unchanged
- `1` - Error warning status changed

#### Dependencies

To enable this port, select the **Warning
status** parameter.

### **WD** — Status of watchdog event boolean

Output port to display the watchdog event status. The status port outputs:

- `0` - No message RAM watchdog event occurred
- `1` - Message RAM watchdog event due to missing
  ready

#### Dependencies

To enable this port, select the **Watchdog
event** parameter.

### **PED** — Status of protocol error in data phase boolean

Protocol error in data phase (Data Bit Time is used)

Output port to display the protocol error in data phase status. The status port outputs:

- `0` - No protocol error in data phase
- `1` - Protocol error in data phase detected

#### Dependencies

To enable this port, select the **Data protocol
error** parameter.

### **MRAF** — Status of message RAM access failure boolean

The flag is set, when the RX Handler:

- Has not completed acceptance filtering or storage of an accepted message
  until the arbitration field of the following message has been received. In
  this case acceptance filtering or message storage is aborted and the RX
  Handler starts processing of the following message.
- Was not able to write a message to the Message RAM. In this case message
  storage is aborted.

In both cases the FIFO put index is not updated respectively. The new data flag
for a dedicated RX Buffer is not set, a partly stored message is overwritten when
the next message is stored to this location.

The flag is set when the Tx Handler could not read a message from the Message
RAM in time. In this case message transmission is aborted. In case of a TX Handler
access failure the MCAN is switched into Restricted Operation Mode.

Output port to display the message RAM access failure status. The status port outputs:

- `0` - No message RAM access failure occurred
- `1` - Message RAM access failure occurred

#### Dependencies

To enable this port, select the **Message RAM access
failure** parameter.

### **BEU** — Status of bit error uncorrected boolean

Bit error uncorrected. Message RAM bit error detected, uncorrected. This bit is
set when a double bit error is detected by the ECC aggregator attached to the
Message RAM. An uncorrected Message RAM bit error sets CCCR.INIT to
`1`. This is done to avoid transmission of corrupted data.

Output port to display the bit error uncorrected status. The status port outputs:

- `0` - No bit error detected when reading from Message
  RAM
- `1` - Bit error detected, uncorrected (e.g. parity
  logic)

#### Dependencies

To enable this port, select the **Bit error
uncorrected** parameter.

### **EP** — Status of error passive boolean

Output port to display the error passive status. The status port outputs:

- `0` - Error passive status unchanged
- `1` - Error passive status changed

#### Dependencies

To enable this port, select the **Error passive
status** parameter.

### **BO** — Status of bus off boolean

Output port to display the bus off status. The status port outputs:

- `0` - Bus off status unchanged
- `1` - Bus off status changed

#### Dependencies

To enable this port, select the **Bus off
status** parameter.

### **PEA** — Status of arbitration protocol error boolean

Protocol error in arbitration phase (Nominal Bit Time is used)

Output port to display the arbitration protocol error status. The status port outputs:

- `0` - No protocol error in arbitration phase
- `1` - Protocol error in arbitration phase detected

#### Dependencies

To enable this port, select the **Arbitration protocol
error** parameter.

### **ARA** — Status of access to reserved address boolean

Output port to display the reversed address access status. The status port outputs:

- `0` - No access to reserved address occurred
- `1` - Access to reserved address occurred

#### Dependencies

To enable this port, select the **Reversed address
access** parameter.

## Parameters

Not documented in R2025b.

## Libraries

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F28p65x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Output specific bits of MCAN interrupt register or entire register

The MCAN Interrupt Status block outputs specific bits of MCAN\_IR
register or the entire MCAN\_IR register. The register values are cleared after reading the
specific bits or entire MCAN\_IR register.

Select the `MCAN interrupt register output` parameter to output the
entire MCAN interrupt register.

If `MCAN interrupt register output` parameter is not selected then the
block outputs specific bits from MCAN\_IR register based on the selection from
`Transmit sources`, `Receive sources` and
`General sources`.

Configure Receive, Transmit and other interrupt sources in configuration parameters. For
more, Model Configuration Parameters for Texas Instruments C2000 Processors.
