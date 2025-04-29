def get_num_words(text):
  length = len(text.split())
  return length

def get_chars_dict(text):
  chars = {}
  for char in text:
    lowered = char.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(chars_dict):
  list_of_dicts = []
  for c in chars_dict:
    list_of_dicts.append({"char": c, "num": chars_dict[c]})
  list_of_dicts.sort(reverse=True, key=sort_on)
  return list_of_dicts
