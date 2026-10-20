# Apply the checked-in deployment:

# kubectl apply -f deployment.yaml --context kind-mlzoomcamp-2026
# kubectl rollout status deployment/subscription --context kind-mlzoomcamp-2026
# kubectl get pods --context kind-mlzoomcamp-2026
# The deployment uses image zoomcamp-model:2026-hw10, listens on container port 9696, and has a readiness probe on /health.

# What value is used for the container port?


# Answer: 9696