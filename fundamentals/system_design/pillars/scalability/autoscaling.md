# How Autoscaling Works

Autoscaling is a cloud computing feature that automatically adjusts the number of computing resources, such as virtual machines (VMs), to match application demand. It ensures high availability and optimizes costs by adding resources during peak load and removing them when demand is low.

### Key Steps of Autoscaling

1. **Define Policies:**  
   Establish rules that specify the conditions under which resources should scale.  
   
2. **Monitor Metrics:**  
   Continuously track key performance indicators (KPIs) such as CPU usage, memory, network traffic, or queue length.  
   
3. **Scale Out:**  
   When a metric exceeds a defined threshold (e.g., CPU utilization goes above 70%), the autoscaler automatically adds new instances to handle the increased load.  
   
4. **Scale In:**  
   When a metric falls below a threshold (e.g., CPU usage drops to 40%), the autoscaler removes unnecessary instances, reducing costs.

---

### Key Benefits of Autoscaling

- **Cost Efficiency:**  
  Prevents over-provisioning of resources, resulting in lower cloud spending.

- **High Availability:**  
  Ensures applications remain responsive and accessible during traffic surges.

- **Improved Performance:**  
  Dynamically allocates the right amount of resources to maintain consistent performance.

- **Simplified Management:**  
  Automates resource management, reducing the need for manual intervention.

---

### Types of Scaling

- **Horizontal Scaling (Scale Out/In):**  
  Adding or removing servers or VMs. This is the primary method of autoscaling.

- **Vertical Scaling (Scale Up/Down):**  
  Changing the capacity of an existing resource, like upgrading a VM’s CPU or memory. Less commonly automated due to potential downtime.

---

### Examples and Use Cases

- **E-commerce:**  
  During holiday seasons or flash sales, autoscaling adds servers to handle surges in customer traffic and scales back when traffic decreases.

- **Media Streaming:**  
  Manages sudden spikes when new popular content is released.

- **Startups:**  
  Supports growth without significant upfront investment by paying only for the resources needed at any time.

---

### Useful Videos

- **How Autoscaling Works with AWS EC2:**  
  https://m.youtube.com/watch?v=rcWgcFMlwFw

- **Types of Autoscaling Explained:**  
  https://www.youtube.com/watch?v=nHnSKgyftAw

---

### References

1. https://www.esds.co.in/kb/autoscaling-advantages-and-disadvantages/
2. https://www.ibm.com/think/topics/autoscaling
3. https://cloud.google.com/compute/docs/load-balancing-and-autoscaling
4. https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-overview
5. https://nathanpeck.com/amazon-ecs-autoscaling/
6. https://www.vmware.com/topics/auto-scaling
7. https://learn.microsoft.com/en-us/azure/architecture/best-practices/auto-scaling
8. https://umbrellacost.com/blog/autoscaling-in-cloud-computing/
9. https://www.datadoghq.com/knowledge-center/auto-scaling/
