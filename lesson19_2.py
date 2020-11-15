def get_strings(city):
      l, city = str(), ''.join(city.lower().split())
      for w in city:
            if w not in l:
                  l += w +':' + '*' * city.count(w) + ','
      return l[:-1]

assert get_strings("Chicago") == "c:**,h:*,i:*,a:*,g:*,o:*", 'Test failed'
assert get_strings("Bangkok") == "b:*,a:*,n:*,g:*,k:**,o:*", 'Test failed'
assert get_strings("Las Vegas") == "l:*,a:**,s:**,v:*,e:*,g:*", 'Test failed'