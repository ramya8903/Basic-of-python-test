# Chat context Window Optimizer

def context_optimizer(total_messages):
    if total_messages <= 100:
      status = "Normal"
      active = total_messages
      compressed = 0
    else:
      status = "optimizer"
      active = 100
      compressed = total_messages - 100
print(f"status: {status}, Active: {active}, Compressed: {compressed}")

# Taking input from user
total_messages = int(input("Enter total number of messages:"))

# Calling function
context_optimizer(total_messages)

output:
Enter total number of messages: 150
status: optimized, Active: 100, Compressed: 50
