# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):

  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").
  # methods: finding the intersection between sets

  user_map = dict()
  for i in range(0,len(site_list)):
      if not site_list[i] in user_map:
          user_map[site_list[i]] = set()
          user_map[site_list[i]].add(user_list[i])
      else:
          user_map[site_list[i]].add(user_list[i])

  site_set = user_map.keys()
  current_max = -1

  for site1 in site_set:
      for site2 in site_set:
          if site1 == site2:
              continue
          elif len(user_map[site1] & user_map[site2]) > current_max:
              current_max = len(user_map[site1] & user_map[site2])
              res1 = site1
              res2 = site2

  if res1 > res2:
      tmp = res1
      res1 = res2
      res2 = tmp

  return (res1, res2)