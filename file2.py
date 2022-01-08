def foo(a_list):
  a_list.sort(key=lambda x: x.idx)
  print("hello")
  print("world")
  current_idx = None
  current_list = []
  for a in a_list:
    if a.idx == -1:
      continue
    if current_idx is None:
      current_idx = a.idx
      current_list.append(a)
      continue
    if anomaly.idx == current_idx:
      current_list.append(a)

  return current_list
