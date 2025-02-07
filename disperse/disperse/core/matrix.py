from dataclasses import dataclass, field

@dataclass
class Matrix:
  width:int
  height:int
  name:str = field(default="Matriz dispersa")
  value_default:int = field(default=0)

  content:dict = field(default_factory=dict)

  def query(self, x:int, y:int):
    col:dict|any = self.content.get(x)
    if not col:
      return self.value_default
    
    return col.get(y, self.value_default)
  
  def set(self, x:int, y:int, value):
    col:dict|any = self.content.get(x)
    if not col:
      self.content[x] = {y: value}
      return

    self.content[x][y] = value

  def sum(self, x:int, y:int, value):
    col:dict|any = self.content.get(x)
    if not col:
      self.content[x] = {y: value}
      return

    data = self.query(x, y)
    self.content[x][y] = data + value    

  def export(self):
    return self.content