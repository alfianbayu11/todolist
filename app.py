from unicodedata import name
import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer, Float
import pandas as pd
from database import Task

# connect to database
engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()
st.title("Todo List APP")

name = st.text_input('What do you want today?')


if st.button("Save") and name:
    with st.spinner("saving..."):
        task = Task(name=name)
        sess.add(task)
        sess.commit()
        st.success("Saved to database")

op = st.checkbox("Show task from database")
if op:
    df = pd.read_sql('task', engine)
    st.table(df)
# def add_todo():
#     task = st.text_input("Task:")
#     if task != "":
#         task = Task(name=task)
#         sess.add(Task)
#         sess.commit()
#         st.success("saved to database")
#     else:
#         st.error("error")


# def view_todo():
#     todos = sess.query(Task).all()
#     return todos
