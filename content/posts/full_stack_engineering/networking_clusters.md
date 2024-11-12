---
date: 2024-04-01
title: "Networking clusters"
---

### Load Balancers
- The public IP exposed are the load balancers. They are like the security guard.
- new request come, they ask the security guard where to send the request. 
- the security guard assign a server.
- (session stickness means only first time ask the security guard, other solution is always ask the security guard)
- task: prevent overload on a single server by distributing the traffic.

### Core, Aggregation, and Access layers (differnt jobs for routers)
- Core Layer: 
    - Superhighway for traffic.
- Aggregation Layer: 
    - Middle manager: combine traffic flow before hitting the core layer.s
- Access Layer: 
    - First point of contact, for example the router of a rack (which contain some servers).


