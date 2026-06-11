import sys

log = " ".join(sys.argv[1:]).lower()

if "crashloopbackoff" in log:
    print("Issue: CrashLoopBackOff")
    print("\nRecommended Actions:")
    print("kubectl describe pod <pod-name> -n fitness")
    print("kubectl logs <pod-name> -n fitness")

    print("\nAutomation Script:")
    print("""
#!/bin/bash
kubectl rollout restart deployment/fitness-tracker-app -n fitness
""")

elif "imagepullbackoff" in log:
    print("Issue: Image Pull Failure")

    print("\nRecommended Actions:")
    print("kubectl describe pod <pod-name> -n fitness")
    print("docker pull <image-name>")

    print("\nAutomation Script:")
    print("""
#!/bin/bash
kubectl set image deployment/fitness-tracker-app \
fitness-tracker-app=abhishekjoshhi/fitness-tracker:prod \
-n fitness
""")

elif "oomkilled" in log:
    print("Issue: Out Of Memory")

    print("\nRecommended Actions:")
    print("Increase memory limits")

    print("\nAutomation Script:")
    print("""
#!/bin/bash
kubectl top pod -n fitness
""")

else:
    print("No known issue detected")
