import collections

def analyze_logs(filepath):

    # using a Counter is cleaner than standard dict
    error_map = collections.Counter()

    try:
        with open(filepath, "r") as file:
            for line in file:
                cols = line.strip().split()
                
                # if less than 9, we will get index error
                if len(cols) < 9:
                    continue

                #extract status code
                status_code_str = cols[-2]

                try:
                    status_code = int(status_code_str)
                except ValueError:
                    continue # skip if the status isn't a number

                request_path = cols[6]

                # turn "search?q=abc" into "/search"
                clean_path =  request_path.split("?")[0]
                
                # register the request map ad how many times it occurred
                error_map[clean_path] += 1

    except FileNotFoundError:
        print("File not found")

    return error_map.most_common(3)

if __name__ == "__main__":

    result = analyze_logs("access_log.txt")
    for request_path, count in result:
        print(f"{request_path}: {count}")