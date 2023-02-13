import streamlit as st
import funcs

todos = funcs.func_read()

def add_todo():

    new_todo = st.session_state["new"]

    todos.append(new_todo + "\n")

    funcs.func_write(todos)

    st.session_state["new"] = ""

st.title("My ToDo Web App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:

        todos.pop(index)
        funcs.func_write(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a new todo...",
              on_change=add_todo, key="new")
