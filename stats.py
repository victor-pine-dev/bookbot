def get_words_count(text):
    count = len(text.split())    
    return count

def get_characters_count(text):
    result = {}

    for ch in text:
        ch = ch.lower()
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1

    return result

def sort_on(items):
    return items["num"]

def get_chars_report(chars_stats):
    result = []

    for k,v in chars_stats.items():
        result.append({
            "char": k,
            "num": v
        })

    result.sort(reverse=True, key=sort_on)

    return result

