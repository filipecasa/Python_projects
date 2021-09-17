import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get the x,y coordinates on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
states = pd.read_csv("50_states.csv")
# states_list = [state for state in states.state]
states_list = states.state.to_list()

correct_answer = []

while len(correct_answer) < 50:

    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 States Correct",
                                    prompt="What's another state name?").title()
    x,y = states[states.state == answer_state].x.to_string(index=False),\
          states[states.state == answer_state].y.to_string(index=False)
    if answer_state == "Exit" or answer_state == "Quit":
        missing_states = []
        for state in states_list:
            if state not in correct_answer:
                missing_states.append(state)
        # print(missing_states)
        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        correct_answer.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x), int(y))
        t.write(answer_state)



