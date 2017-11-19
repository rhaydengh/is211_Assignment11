#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 11"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

todolist = []

@app.route('/')
def todoapp():
    return render_template('index.html', todolist=todolist)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    task1 = request.form['task1']
    task2 = request.form['task2']
    task3 = request.form['task3']
    email = request.form["email"]
    priority = request.form["priority"]
    todolist.append(task1)
    if '@' not in email:
        print "Invalid e-mail"
        return redirect('/')
    elif priority != "low" and priority != "medium" and priority != "high":
        print "Invalid Priority"
        return redirect('/')
    else:
        todolist.append(task1)
        return render_template('index.html', priority=priority, task1=task1, task2=task2, task3=task3, todolist=todolist)

@app.route('/clear', methods = ['POST'])
def clear():
    todolist = []
    return render_template('index.html', todolist=todolist)

if __name__ == "__main__":
    app.run()