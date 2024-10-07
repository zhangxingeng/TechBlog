---
title: "How a Request is Passed"
date: 2024-06-07
---

## Procedure of How a Request is Passed in a Cloud Scalable Architecture

1. **Client Request**:
   - A client (e.g., a web browser or mobile app) sends a request to access a resource or service.

2. **Internet**:
   - The request travels over the internet to reach the server infrastructure hosting the application or service.

3. **Load Balancer**:
   - The request first hits a load balancer (e.g., an AWS Elastic Load Balancer, NGINX, or HAProxy).
   - The load balancer distributes incoming requests across multiple backend servers to balance the load and ensure high availability.

4. **Server Handling**:
   - The load balancer forwards the request to one of the available servers in the backend. This server could be a physical machine, a virtual machine, or a containerized environment managed by Kubernetes.

5. **Reverse Proxy (kube-proxy in Kubernetes)**:
   - Within the selected server (or node in Kubernetes), the request reaches the reverse proxy. In a Kubernetes environment, `kube-proxy` acts as the reverse proxy.
   - The reverse proxy (`kube-proxy`) routes the request to the appropriate pod based on the service and endpoints configuration.

6. **Pod and API Gateway**:
   - The request is forwarded to the appropriate pod (let's call it pod #k) by the reverse proxy.
   - Inside the pod, the API server (which might be part of a microservices architecture) receives the request.
   - If an API gateway (like Kong, NGINX, or Traefik) is deployed within the pod or at the cluster level, it can perform additional tasks such as authentication, rate limiting, and request transformation before the API server processes the request.

7. **API Server**:
   - The API server within the pod processes the request. It executes the business logic, interacts with the database if needed, and prepares the response.
   - The API server sends the response back to the reverse proxy.

8. **Response Path**:
   - The reverse proxy forwards the response back to the load balancer.
   - The load balancer sends the response over the internet to the client.

### Example Workflow:

Let's break this down into a specific example for clarity:

#### Scenario: A Client Requests User Data from a Web Application

1. **Client Request**:
   - The client sends a GET request to `https://example.com/api/users/123`.

2. **Internet**:
   - The request travels through the internet to reach the server infrastructure.

3. **Load Balancer**:
   - The request hits the load balancer (e.g., AWS ELB), which decides to forward the request to one of the backend servers, say Server A.

4. **Server Handling**:
   - Server A receives the request. It could be a node in a Kubernetes cluster.

5. **Reverse Proxy (kube-proxy)**:
   - The `kube-proxy` on Server A determines that the request should be handled by a pod running the user service.
   - It forwards the request to pod #k.

6. **Pod and API Gateway**:
   - Inside pod #k, the request might first hit an API gateway (e.g., Kong) if it's configured within the pod or cluster.
   - The API gateway performs tasks such as authentication and request validation.
   - The request is then forwarded to the API server within the pod.

7. **API Server**:
   - The API server processes the request, retrieves user data from the database, and constructs a response.

8. **Response Path**:
   - The API server sends the response back to the `kube-proxy`.
   - The `kube-proxy` routes the response back to the load balancer.
   - The load balancer forwards the response to the client over the internet.

### Diagram Representation:

```plaintext
Client ---> Internet ---> Load Balancer ---> Server A (Node)
                                  |
                              kube-proxy
                                  |
                              Pod #k
                              /   \
                      API Gateway  API Server
                                  |
                             Database (if needed)
```

### Summary:

- The client request is distributed to a backend server by the load balancer.
- The reverse proxy (`kube-proxy`) on the server routes the request to the appropriate pod.
- The API server within the pod processes the request and generates a response.
- The response travels back through the reverse proxy and load balancer to the client.

This setup ensures efficient handling of requests, load balancing, security, and scalability in a modern cloud-native architecture.