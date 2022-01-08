def foo(a_list: list):
  """
  some comments foo bar
  """
  a_list.sort(key=lambda x: x.idx)
  current_idx = None
  current_list = []
  for a in a_list:
    current_idx = a.idx
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    if current_idx is None:
      current_idx = a.idx
      continue
    if a.idx == current_idx:
      current_list.append(a)

  return current_list
