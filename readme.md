# solve the data type form to better suit the game

    objects
          piece
               move()--forward
               reset()--return to station
               disable()--can't choose because move overflow
               active--boolean
               colorId--string color
               Id--int

          cell
              constructor(type)
              type -- string (start,openField,homeRun,home)
               add()--append
               remove()--reset the pieces present at the cell
               hostilePresent()--boolean
               
          board
               
          stations
                 4-storage for each of the four color types
                 

## we can set 4 paths for each of the four pieces type
## to restructure the code to animate smoothly we will use a property that links the id of the display wise cell(html) to the codewise cell(javascript)

15x15 grid