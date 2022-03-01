
correct = "c"
misplaced = "m"
incorrect = "i"

def check_word(request_body, store):
    response = {}
    request_word = "".join(request_body["guess"])

    if request_word not in store.allowed_words:
        return {"allowed": False}

    solution_word = store.actual_words[request_body["time"]]["word"]
    solution_count = dict(store.actual_words[request_body["time"]]["count"])

    result = [incorrect] * 5
    for i, c in enumerate(request_word):
        if c == solution_word[i]:
            result[i] = correct
            solution_count[c] -= 1
            continue

        if c != solution_word[i] and c in solution_count and solution_count[c] > 0:
            result[i] = misplaced

    print(solution_count)

    return {"allowed": True, "result": result}
