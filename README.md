# sudoku_solver_project
A solo project where I aim to create a sudoku-solving file

# To-do list:
## Pressing:

- Make remove_potentials_from_area_if_only_in_row
- Make remove_potentials_from_area_if_only_in_column
- Make remove_deterministic_groups <- FUNCTION FOR 2, FUNCTION FOR 3, SEE HOW TO GENERALISE
- Develop more algorithms to eliminate potentials

## General:
- Add documentation
- Requirements file

## Stretch:
- Add Sudoku input capability
- Confine Area class to be square-shaped (only when passed square-numbered grid sizes)

## Completed:
- ~~Create a Cell class with relevant attributes and properties~~
- ~~Create a Grid class with relevant attributes and properties~~
- ~~Create a Row class with relevant attributes and properties~~
- ~~Update Grid to populate grid with Cell objects instead of '0's~~
- ~~Test for Cell.solve()~~
- ~~Create Column class~~
- ~~Test Column class~~
- ~~Create Area class~~
- ~~Test Area class~~
- ~~Create utils file and test_utils file~~
- ~~Create isSquare function in utils~~
- ~~Test isSquare function~~
- ~~Test some methods and attributes on pre-made 4x4 grid~~
- ~~Test Rows on pre-made 4x4 grid~~
- ~~Test Columns on pre-made 4x4 grid~~
- ~~Test Areas on pre-made 4x4 grid~~
- ~~Made a Cell method which reduces the potentials~~
- ~~Make function that reduces potentials by solutions~~
- ~~Make function that sets solution by singular appearance in Row~~
- ~~Make function that sets solution by singular appearance in Column~~
- ~~Area.data needs editing, it assigns datum as though we are using a 9x9 grid, despite testing with a 4x4 grid~~
- ~~Make function that sets solution by singular appearance in Area~~
- ~~Test many methods and attributes on pre-made 9x9 grid~~
- ~~Make only_one_left algorithm~~
- ~~Test only_one_left on 4x4 grid~~
- ~~Test only_one_left on 9x9 grid~~