from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password setting',
    'database': 'mysql_study',
    'port': 3306
}


@app.route('/')
def show_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    columns = [i[0] for i in cursor.description]


    cursor.close()
    conn.close()

    html_template = '''
    <h1>Users Table</h1>
    <table border="1">
        <tr>
            {% for col in columns %}
            <th>{{ col }}</th>
            {% endfor %}
        </tr>
        {% for row in rows %}
        <tr>
            {% for item in row %}
            <td>{{ item }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>
    '''
    return render_template_string(html_template, columns=columns, rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
