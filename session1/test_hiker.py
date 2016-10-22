import hiker

def test_life_the_universe_and_everything():
    '''a simple example to start you off'''
    douglas = hiker.Hiker(4,8)
    assert douglas.answer() == 54

    def test_one_cell_alive():
        douglas = hiker.Hiker(4,8)
        array_cells = [[2,4]]
        douglas.add_cells(array_cells)

        douglas.count_alives() == 1

        douglas.next_iteration()

        douglas.count_alives() == 0
