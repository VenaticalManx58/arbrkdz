class Hash_table():

  def __init__(self, size):
    self.size = size
    self.array = [None]*self.size
    self.length = 0
  
  #def new(self):
    #self.array = [None]*32
  
  def size_func(self):
    return self.length

  
  def enlarge(self):
    self.array += [None]*self.size
    self.size *= 2

  def put(self, pair):
    #print(self.array)
    self.pair = pair
    self.key = str(pair[0])
    self.place = hash(self.key) % self.size
    while self.array[self.place] != None:
      if self.array[self.place][0] == self.key:
        self.array[self.place] = self.pair
        return
      self.place = self.place + 1
      if self.place > self.size - 1:
        self.enlarge()
        self.array[self.place] = self.pair
        return
    self.array[self.place] = (str(self.key), pair[1]); self.length += 1

  #Необязательная функция, но нужная мне для проверки себя
  def printt(self):
    print(self.array)

  
  
  def delete(self, key):
    self.place = hash(key) % self.size
    while True:
      if self.array[self.place] == None: print("ОШИБКА!!!111"); return
      elif self.array[self.place][0] != str(key): self.place += 1
      else: self.array[self.place] = None; self.length -= 1; return

  def get(self, key):
    self.place = hash(key) % self.size
    while True:
      if (self.array[self.place] == None) or (self.place > self.size-1):
        print("ОШИБКА!!!111"); return
      elif self.array[self.place][0] != str(key): self.place += 1
      else: return self.array[self.place][1]
  
  def contains(self, key):
    self.place = hash(key) % self.size
    while True:
      if self.array[self.place] == None: return False
      elif self.place > self.size-1: return False
      elif self.array[self.place][0] != str(key): self.place += 1
      else: return True

def new(size=32):
  return Hash_table(size)

'''
a = "вася"
b = 1
p = (a, b)
p1 = ("lol", 2)
p2 = ("lolita", 4)
print(p[0], p[1])


arrr = new()
arrr.put(p)
arrr.printt()
arrr.put(p)
arrr.printt()
arrr.put(p1)
arrr.printt()
arrr.put(p2)
arrr.printt()
print(arrr.sizefunc())
#arrr.put(p)
#arrr.put(p)
print(arrr.delete("lolita"))
arrr.printt()
print(arrr.get("lolita"))
print(arrr.contains("lolita"))
print(arrr.sizefunc())
'''
