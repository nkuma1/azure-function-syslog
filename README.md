**Use Case:** Customer SIEM/Syslog Server is running inside on-premise data center. 

**Function Architecture:** Setup Azure Function in App Service Plan to integrate Azure Function with Virtual Network.  

Prisma Cloud – > Webhook (Azure Function) – > Vnet Integration – > Route traffic to on-premise data center syslog server.

#### Step 1: Azure Function Setup

Create a Function App

*   Publish: Code
*   Runtime stack: Python
*   Version: 3.11

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/6d5be81749397327b17a97c7c4458855bec0be2d225b39a0.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/b44ee10d3da87fc0b6e40a02e6b2f823e89af040432639b2.png)

**Step 2: Azure Function integration with Azure VNET**

Open Function Networking setting:

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/5adcd15d06be9328a1900c95af1881fff8f8fe02efc43e6a.png)

Click, Outbound Traffic configuration - Virtual Network Integration

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/b91313d3733481a03c2776f464c6fb0b8c3017ea29757f7b.png)

Click, Add virtual network integration

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/9e43aad094e296bb7ea0a20a205ab18c3babe4991d712eba.png)

Select VNET and Subnet and click Connect. \[This integration will be used to route traffic from Azure Function to SIEM/Syslog Server\]

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/074457d57d0bca06382a1750dfc624821ba64832d02c2e38.png)

You might need to update route table to route traffic depending on your environment.
