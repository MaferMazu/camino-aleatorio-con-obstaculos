from bokeh.plotting import figure, show
import statistics
import DrunkCrashing
    

if __name__ == "__main__":
    board = SquareBoard(5)
    board.fillboard([[0,1],[1,1],[2,1],[1,3],[1,4],[3,3],[4,3]])
    borrachos=[]
    # Choques cuando los borrachos dan x steps
    collisions_10steps=[]
    collisions_100steps=[]
    collisions_1000steps=[]
    collisions_10000steps=[]
    # Distancia que recorren los borrachos cuando dan x pasos
    dist_10steps=[]
    dist_100steps=[]
    dist_1000steps=[]
    dist_10000steps=[]

    # Creo 10 borrachos
    for i in range(10):
        borracho=DrunkCrashing([0,0],board)
        borrachos.append(borracho)


    # Por cada borracho veo su comportamiento cada x pasos
    for borracho in borrachos:
        # 10 steps
        for i in range(10):
            borracho.move()
        collisions_10steps.append(borracho.collide)
        dist_10steps.append(borracho.dist())
        borracho.clearposition()
        borracho.clearcollide()

        # 100 steps
        for i in range(100):
            borracho.move()
        collisions_100steps.append(borracho.collide)
        dist_100steps.append(borracho.dist())
        borracho.clearposition()
        borracho.clearcollide()

        # 1000 steps
        for i in range(1000):
            borracho.move()
        collisions_1000steps.append(borracho.collide)
        dist_1000steps.append(borracho.dist())
        borracho.clearposition()
        borracho.clearcollide()

        # 10000 steps
        for i in range(10000):
            borracho.move()
        collisions_10000steps.append(borracho.collide)
        dist_10000steps.append(borracho.dist())
        borracho.clearposition()
        borracho.clearcollide()

    x=[10,100,1000,10000]

    y1=[statistics.median(dist_10steps),statistics.median(dist_100steps),statistics.median(dist_1000steps),statistics.median(dist_10000steps)]
    y2=[statistics.median(collisions_10steps),statistics.median(collisions_100steps),statistics.median(collisions_1000steps),statistics.median(collisions_10000steps)]
    graph=figure(title='Cuánto chocan y avanzan los borrachos',x_axis_label='steps')
    graph.line(x,y1,line_color='pink',legend='avance',line_width=4)
    graph.line(x,y2,line_color='blue',legend='collide',line_width=3)

    show(graph)