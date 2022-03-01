
def validate_request_body(request_body, store):
    if not request_body:
        return 'Invalid Request', 400

    guess_array = request_body.get("guess")
    if not guess_array:
        return "key 'guess' is missing from request body", 400
    
    timestamp = request_body.get("time")
    if not timestamp:
        return "key 'time' is missing from request body", 400
    if timestamp not in store.actual_words:
        return "word for requested 'time' is not available", 400
    
    if type(guess_array) != list or len(guess_array) != 5 or not all(len(c) == 1 for c in guess_array):
        return "bad guess array", 400

    return "ok", 200
