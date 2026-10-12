# Week 5 

For this assignment I made a small version of MapReduce on my laptop using Python. 

## What's in here

- data: has loans_full.csv with 40 loan records, and then I split it into 3 smaller files (partition1, partition2, partition3) to act like partitions
- map_step.py: goes through each partition and makes a (category, 1) pair for every loan
- shuffle_step.py: takes all the map outputs and groups them by category
- reduce_step.py: adds everything up and saves the final counts
- sequential.py: does the same count but just reads the full file in one go, so I could compare
- map_outputs, shuffle_outputs, results: these get made when you run the scripts
- shuffle_simulation.md, performance_notes.md, reflection.md: my write ups

## How to run it

Run these in order in the terminal:

    python3 map_step.py
    python3 shuffle_step.py
    python3 reduce_step.py
    python3 sequential.py

## Results

Both the partitioned way and the sequential way got the same counts:

laptop -> 20
camera -> 13
projector -> 7
