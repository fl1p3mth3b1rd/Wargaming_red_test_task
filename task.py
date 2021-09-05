from flask import Flask, request, render_template
from processing import count_TF_IDF
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def load_txt_view():
    if request.method == 'POST':
        res = count_TF_IDF(request.files.get('file'))
        print('check1')
        if isinstance(res, list):
            print('check2')
            return render_template('result.html', res=res)
        else:
            print('check3')
            return f"""
                Ошибка: {res}
                <form method="POST" enctype='multipart/form-data'>
                <input type="file" name="file">
                <button type="submit">Загрузить</button>
                </form>
                """
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)