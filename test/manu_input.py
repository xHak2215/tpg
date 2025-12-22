import tpg

inp=tpg.InputMany()

tpg.clear()

inp.input_at(1,3,'1>')
inp.input_at(1,4,'2>')


print(inp.run_inputs())