def check_longest_substring(input_str):
    result_len = 0
    result = []
    current_substring = ""
    visitesd_ch = set()
    for ch in input_str:
        if ch in visitesd_ch:
            if current_substring != "" and len(current_substring) > result_len:
                result = [current_substring]
                result_len = len(current_substring)
            elif len(current_substring) == result_len:
                result.append(current_substring)

            visitesd_ch = {ch}
            current_substring = ch
            continue

        current_substring += ch
        visitesd_ch.add(ch)

    if current_substring != "" and len(current_substring) > result_len:
        result = [current_substring]
        result_len = len(current_substring)
    elif len(current_substring) == result_len:
        result.append(current_substring)

    print(result)


sample_str = "ababccdefabcdefka"
check_longest_substring(sample_str)
