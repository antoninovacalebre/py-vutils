import psutil as ps
import time


def exec_and_monitor(cmd, log_file: str = 'log.txt', monitor_frequency=10) -> tuple[float, float]:
    '''
    Executes command and monitors its Peak Memory Usage (in bytes) and Peak CPU Usage (%)
    '''
    dt = 1 / monitor_frequency

    with open('log.txt', 'w') as f:
        process = ps.Popen(cmd, stdin=None, stdout=f)

        peak_mem = 0
        peak_cpu = 0

        while(process.is_running()):
            # capture the memory and cpu utilization at an instance
            try:
                mem = process.memory_info().rss
                cpu = process.cpu_percent()
            except:
                break

            # track the peak utilization of the process
            if mem > peak_mem:
                peak_mem = mem
            if cpu > peak_cpu:
                peak_cpu = cpu
            if mem == 0.0:
                break

            time.sleep(dt)

    return peak_mem, peak_cpu
