import turtle
import pandas

data=pandas.read_csv("50_states.csv")
states=data["state"].to_list()

screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states=[]
while len(guessed_states) <50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another State's name?").title()
    guessed_states.append(answer_state)
    if answer_state=="Exit":
        missed_states = []
        for state in states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data=pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break


    if answer_state in states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())



turtle.mainloop()