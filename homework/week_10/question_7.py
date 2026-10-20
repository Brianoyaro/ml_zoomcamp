# Apply the checked-in service:

# kubectl apply -f service.yaml --context kind-mlzoomcamp-2026
# kubectl get service subscription --context kind-mlzoomcamp-2026
# The service deliberately uses ClusterIP, which works on every kind install; we will access it with port forwarding rather than relying on a cloud LoadBalancer implementation.

# Which selector value routes traffic to the deployment?



# Answer: app: subscription

