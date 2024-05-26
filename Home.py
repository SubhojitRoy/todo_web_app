import streamlit as st
from modules import functions

todos = functions.read_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.set_page_config(layout="wide")
st.title("My To-Do App")
st.subheader("My To-Do App")
# st.write("This is a simple comment")
# st.write("This is a simple <b>comment</b>",
#          unsafe_allow_html=True)
st.write("<h1>This is a simple <b>comment</b></h1>",
         unsafe_allow_html=True)                          #same as st.title module

st.text_input(label="", placeholder="Add your todo...",
              on_change=add_todo, key="new_todo")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# st.text_input(label="", placeholder="write your todo...",
#               on_change=add_todo, key="new_todo")
