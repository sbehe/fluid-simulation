# OpenMP-Accelerated 2D Lattice Boltzmann Fluid Simulation

This project implements a parallelized 2D Lattice Boltzmann Method (LBM) fluid simulation using OpenMP. The simulation efficiently models fluid dynamics and leverages multicore CPUs for performance gains via shared-memory parallelism.

## Overview

The simulation performs 2D fluid flow modeling using the Lattice Boltzmann Method, a numerical approach widely used in computational fluid dynamics. This version integrates OpenMP to parallelize key operations across multiple threads, dramatically reducing total runtime for large-scale simulations.

Simulation components:
- **Computation**: Core physics calculations including collision, streaming, and boundary processing.
- **Conversion**: Translates simulation data to pixel buffers for image rendering.
- **I/O**: Outputs rendered images for each timestep.

The simulation runs for 10,000 steps and supports benchmarking with 1, 2, 4, 8, and 16 threads.

## Features

- Multithreaded loop parallelism with OpenMP
- Dynamic scheduling and reduction techniques
- Fine-grained timing breakdown of compute, conversion, and I/O phases
- Output of per-timestep metrics to `fluid.csv`
- Speedup and compute performance plots

## Build Instructions

### Requirements
- GCC or Clang with OpenMP support
- `make`

### Build Commands
```
make all
```
### Targets
	•	lbmSimulation: OpenMP-parallelized simulation
	•	lbmSimulation-serial: Baseline serial version
	•	clean: Removes binaries and temporary files

### Running the Simulation

Set thread count with OMP_NUM_THREADS:
```
export OMP_NUM_THREADS=4
./lbmSimulation
```
Example (16 threads):
```
export OMP_NUM_THREADS=16
./lbmSimulation
```

### Generated output:
	•	fluid.csv: Time breakdowns for each timestep
	•	out/frame_*.ppm: Image output (optional visualization)
	•	speedup.png: Thread count vs. speedup chart
	•	computation.png: Compute time per timestep chart

## Performance Results
Benchmarked on 1 to 16 threads. The baseline runtime for the serial version was 3756.85s. Performance was evaluated using both total runtime and per-phase metrics (compute, convert, I/O).

Results from executing with different thread counts is stored in csv file named `thread_<thread_count>.csv`

Speedup graph is generated in speedup.png
Computaion graph is generated in computation_with_thread_count-n.png
plot.py is used to generate the graphs

## Technical Highlights
	•	Loop Parallelism: Key loops over the fluid domain were parallelized using #pragma omp parallel for.
	•	Reduction: Correct handling of global accumulations using OpenMP’s reduction clause.
	•	Scheduling: Comparison of static vs. dynamic scheduling strategies to improve load balancing.
	•	Race Condition Avoidance: Shared variable access carefully managed to avoid data races.
	•	Scalability: Achieved substantial speedup on up to 16 threads with good scaling behavior.

## Future Improvements
	•	Explore hybrid MPI + OpenMP parallelism for cluster-scale execution.
	•	Tune OpenMP scheduling policies based on grid characteristics.
	•	Profile memory access patterns to reduce cache thrashing.
	•	Investigate SIMD optimizations for inner loops.
