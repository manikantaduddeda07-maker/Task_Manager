from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id_counter = 1

@app.route('/', methods=['GET', 'POST'])
def home():
    global task_id_counter

    if request.method == 'POST':
        task_name = request.form.get('task')

        if task_name:
            tasks.append({
                'id': task_id_counter,
                'name': task_name,
                'completed': False
            })
            task_id_counter += 1

        return redirect(url_for('home'))

    return render_template('index.html', tasks=tasks)


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return redirect(url_for('home'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
