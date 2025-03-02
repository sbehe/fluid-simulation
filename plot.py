import matplotlib.pyplot as plt
import pandas as pd

# List of thread counts and corresponding file names
thread_files = {
    1: "thread_01.csv",
    2: "thread_02.csv",
    4: "thread_04.csv",
    8: "thread_08.csv",
    16: "thread_16.csv"
}

# Read all CSV files into a dictionary
data = {threads: pd.read_csv(filename) for threads, filename in thread_files.items()}

# Plot 1: Speedup vs. Threads
serial_time = data[1]["SimStepTime"].mean()  # Baseline: time for 1 thread
speedups = [serial_time / data[t]["SimStepTime"].mean() for t in thread_files.keys()]

plt.figure(figsize=(8, 6))
plt.plot(thread_files.keys(), speedups, marker='o', linestyle='-', color='b', label="Speedup")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs. Threads")
plt.xticks(list(thread_files.keys()))
plt.grid(True)
plt.legend()
plt.savefig("speedup.png")
plt.close()

# Plot 2: Computation Time per Timestep for Each Thread Count
for threads, df in data.items():
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Timestep"], df["SimStepTime"], s=10, label=f"{threads} Threads", alpha=0.7)
    plt.xlabel("Timestep Index")
    plt.ylabel("Computation Time per Timestep (s)")
    plt.title(f"Computation Time per Timestep ({threads} Threads)")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"computation_with_thread_count-{threads}.png")  # Save each plot separately
    plt.close()