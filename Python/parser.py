import re

def extract_last_word(file_path, start_time, end_time):

    result = []

    timestamp_pattern = re.compile(r"\d{2}:\d{2}:\d{2}.\d{3}")

    with open(file_path, 'r') as file:
        for line in file:
            timestamp_match = timestamp_pattern.search(line)

            if timestamp_match:
                current_timestamp = timestamp_match.group()
                if start_time <= current_timestamp <= end_time:
                    words = line.split()
                    if words:
                        last_word = words[-1]
                        result.append(last_word)
                        
    return result

if __name__ == '__main__':

    file_path = './logcat_applications.txt'
    start_time = '17:56:07.996'
    end_time = '17:56:08.360'

    result_list = extract_last_word(file_path, start_time, end_time)

    print(result_list)
