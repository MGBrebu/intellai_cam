import time

# CLASS: General performance timer
# Remembers runs, total time, and average time
class Timer:
    def __init__(self, label=None, verbose=True):
        if label is None:
            Timer._counter += 1
            label = f"Timer-{Timer._counter}"
        self.label = label
        self.verbose = verbose
        self.start_time = None
        self.total_time = 0.0
        self.call_count = 0
        self.success_call_count = 0
        self.times = []
        self.success_times = []
    
    # DEF: Start a timer
    def start(self):
        if self.start_time is not None:
            raise RuntimeError("Timer is already running. Call stop() before starting again.")
        self.start_time = time.perf_counter()

    # DEF: Get elapsed time since start
    def get_time(self):
        if self.start_time is None:
            raise RuntimeError("Timer is not running. Call start() before getting time.")
        return time.perf_counter() - self.start_time

    # DEF: Stop the timer and return elapsed time
    def stop(self):
        if self.start_time is None:
            return "Timer is not running. Call start() before stopping."
        duration = time.perf_counter() - self.start_time
        self.total_time += duration
        self.call_count += 1
        self.times.append(duration)
        self.start_time = None

        if self.verbose and self.label:
            print(f"[T:{self.label}] Run {self.call_count}: {duration:.4f} seconds")

        return duration
    
    # DEF: Reset the timer to initial state
    # Adds to call count and overall times list
    # Does not add to successful call count or successful times list
    def reset(self):
        duration = time.perf_counter() - self.start_time
        self.start_time = None
        self.call_count += 1
        self.times.append(duration)
        if self.verbose and self.label:
            print(f"[T:{self.label}] Run {self.call_count}: RESET")
        return 0.0
    
    # DEF: Get the average time of all runs
    def average(self):
        avg_success_time = self.total_time / self.success_call_count if self.success_call_count > 0 else 0.0
        avg_time = self.total_time / self.call_count if self.call_count > 0 else 0.0
        return avg_time
    
    # DEF: Print a summary of the timer object
    # Includes total time, call count (+successful), and average time (+successful)
    def summary(self, print_runs=True, print_avg=True):
        output = f"\n== Timer Summary: {self.label or 'Unnamed'}\n"
        output += f"Time: {self.total_time:.4f} sec\n"
        if print_runs:
            output += f"Runs: {self.call_count}\n"
            if self.success_call_count > 0:
                output += f"Successful runs: {self.success_call_count}\n"
        if print_avg:
            output += f"Average time: {self.average():.4f} sec\n"
            if self.success_call_count > 0:
                output += f"Average successful time: {self.total_time / self.success_call_count:.4f} sec\n"
        return output.strip()
    
    # DEF: Get the times list
    def get_times(self):
        return self.times