__author__ = "730470758"
import matplotlib.pyplot as plt
from exercises.ex07.runtime_analysis_functions import evaluate_runtime,evaluate_memory_usage

START_SIZE: int = 1
END_SIZE: int = 1000

times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - Israel25")
plt.show()

times2 = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times2)
plt.title("Runtime Analysis of Insertion Sort - Israel25")
plt.show()

usage = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - Israel25")
plt.show()
 
usage2 = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage2)
plt.title("Memory Usage Analysis of Insertion Sort - Israel25")
plt.show()