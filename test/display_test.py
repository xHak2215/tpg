import tpg

displu=tpg.display()

displu.box(15, 11, 1, 1, symbol='@')

displu.box(15, 11, 22, 1, filling=True)

displu.cursor(3,3 ,symbol='h')
displu.cursor(4,3 ,symbol='i')

displu.echo(end='\n')