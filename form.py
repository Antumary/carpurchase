from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # -*- coding: utf-8 -*-
       

        import os,sys
from google.colab import drive 
drive.mount('/content/drive')
os.chdir("/content/drive/My Drive/Colab Notebooks/")
sys.path.append("/content/drive/My Drive/Colab Noteboos/")
        dataset = pd.read_csv("Salary_Data.csv")

        x = dataset.iloc[:, :-1].values

        y = dataset.iloc[:, 1].values

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=0)

        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        y_pred = regressor.predict(X_test)

        p = request.form.get("input")

        Xnew = [[p]]

        result = regressor.predict(Xnew)

        value = result.tolist()


        # getting input

        final=str(value[0])




        return final

    return render_template("form.html")

if __name__=='__main__':
   app.run()