---
type: simulink-block
title: 'HTTP Client'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'httpclient'
documentation_source_path: 'supportpkg/raspberrypi_ref/httpclient.html'
language: en
---

# HTTP Client

## Ports

### Input

### **URL** — URL of server character vector

Specify the URL of the server at this port as a `uint8` vector input.

**Tip**

If you are using the String
library blocks to create a URL, use a String to
ASCII block to convert the string to a `uint8`
vector.

**Data Types:** `uint8`

### **Payload** — Request payload character vector

Specify at this port the data that you want the Raspberry Pi hardware to send as part of an HTTP request to the remote server.

#### Dependencies

- To enable this port, select **Request has payload
  input**.

**Data Types:** `uint8`
### Output

### **Status** — Status of HTTP request `0` | `1` | `2`

This port outputs the status of the HTTP request to the remote server.

- `0` — Indicates a failure in sending the request to the
  server.
- `1` — Indicates that the Raspberry Pi hardware successfully sent the request to the server.
- `2` — Indicates an invalid request. The block waits to make
  the next HTTP request to the server.

**Data Types:** `uint8`

### **Error** — Error message from server character vector

This port outputs the error message from the server related to all communication
failures. If the **Status** port outputs `0` or
`2`, then the **Error** port outputs the
corresponding error message.

#### Dependencies

- To enable this port, clear **Request has response
  output**.

**Data Types:** `uint8`

### **Response** — Response message from server character vector

This port outputs the response message from the server related to all successful
HTTP requests. If the **Status** port outputs `0`,
then the **Error** port outputs the error message. If the
**Status** port outputs `1`, then the
**Response** port outputs the response message.

#### Dependencies

- To enable this port, select **Request has response
  output**.

**Data Types:** `uint8`

### **Data Size** — Size of response data from server scalar

This port outputs the size of the response message data received from the
server.

#### Dependencies

- To enable this port, select **Request has response
  output**.

**Data Types:** `int32`

## Parameters

### Main

### **Request Method** — HTTP request method `GET` (default) | `POST` | `PUT`

Select the HTTP request method.

- `GET` — This method requests data from a specified
  resource.
- `POST` — This method sends data to a server to
  create a resource.
- `PUT` — This method sends data to a server to
  update a resource.

### **Update Interval (seconds)** — Interval between HTTP requests `2` (default) | positive integer

Specify the number of seconds to wait between subsequent HTTP requests.

### **Request has payload input** — Payload input in request `off` (default) | `on`

Select this option if the HTTP request contains payload data in the JSON or text
formats.

### **Content Type** — Input payload content type `application/json` (default) | `text/plain`

Select the content type of the payload input in the HTTP request. If you select
the POST or PUT request methods, the client sends the content type information to the
server directly based on the data.

#### Dependencies

- To enable this parameter, select **Request has payload
  input**.

### **Request has response output** — Payload output in response `off` (default) | `on`

Select this option if the HTTP response from the server contains payload
data.

### **Maximum length of the output Message** — Maximum length of output data `256` (default) | positive integer

Enter the maximum length of the expected payload data.

#### Dependencies

- To enable this parameter, select **Request has response
  output**.

### **Accept** — Format of output data `application/json` (default) | `text/plain`

Select the format of the output payload data.

#### Dependencies

- To enable this parameter, select **Request has response
  output**.

### **Print diagnostic messages** — Print diagnostic messages on serial port `off` (default) | `on`

Select this option to print diagnostic messages for each HTTP request on the
Raspberry Pi serial port.

### Advanced

### **Number of custom headers** — HTTP request headers `0` (default) | `1` | `2` | `3`

Select the number of custom HTTP request headers. You can customize a header that
contains one or more key-value pairs to provide more information about the request.
The value `0` indicates that the HTTP request has no custom header.
Similarly, the value `2` indicates that the HTTP request has two
custom headers.

### **Key** — HTTP request header key character vector

Specify the key of the HTTP request header. The number of **Key**
parameter boxes in the block dialog box depends on the number of headers you specify
in the **Number of custom headers** parameter. For example, if you
set **Number of custom headers** to `2`, the
block generates two **Key** parameters.

#### Dependencies

- To enable this parameter, set **Number of custom headers**
  to `1`, `2`, or
  `3`.

### **Value** — HTTP request header value character vector

Specify the value of the custom HTTP request header key. The number of
**Value** parameter boxes in the block dialog box depends on the
number of headers you specify in the **Number of custom headers**
parameter. For example, if you set **Number of custom headers** to
`3`, the block generates three **Value**
parameters.

#### Dependencies

- To enable this parameter, set **Number of custom headers**
  to `1`, `2`, or
  `3`.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Send and receive data from HTTP server over URL connection

Use the HTTP Client block to send and receive data from the remote server
using the HTTP protocol. You can send data in the text or JSON formats. The Raspberry Pi® hardware acts as a client and can send HTTP requests to the remote server over a
uniform resource locator (URL) connection. The block supports the HTTP GET, POST, and PUT
methods.
