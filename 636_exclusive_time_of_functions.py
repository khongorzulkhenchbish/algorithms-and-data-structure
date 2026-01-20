class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """ The intuition is to understand that only one function can be active at any given timestamp.
        Call Stack: When a function starts, its ID is pushed onto a stack. When it ends, it is popped.

        Whenever process starts, we should append it to the stack, whether the same process id
        exists or not, because a recursive processes is starting.

        We should return an exec_time array where index will be the process id,
        and the value will be total process.

        The input will be valid, meaning there is no end of process that hasn't started yet.

        Time: O(N), Space: O(N/2)
        """
        exec_time = [0] * n
        process_stack = []

        # track only the previous timestamp
        prev_time = 0

        for log in logs:
            func_id, signal, timestamp = log.split(":")
            func_id, timestamp = int(func_id), int(timestamp)

            if signal == "start":
                # if there's something on the stack, it was running until now
                if process_stack:
                    exec_time[process_stack[-1]] += (timestamp - prev_time)
                
                process_stack.append(func_id)
                # current time will be the prev_time, so next iteration, whether it is start/end
                # current timestamp should be subtracted
                prev_time = timestamp
            else:
                # signal == "end", e.g: "0:start:2", "0:end:5"
                # +1 because the end time is inclusive [2,5] = 5-2+1 = 4
                exec_time[process_stack.pop()] += (timestamp - prev_time + 1)
                # because current process was finished, the end should be the next one.
                prev_time = timestamp + 1
        
        return exec_time