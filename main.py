from flask import Flask, render_template,request,jsonify

from index import get_Sentiment_Polarity



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")



@app.route("/get_sentiment", methods=["POST"])
def get_Sentiment():
    
    if request.method == "POST":		
    
        lyrics = request.form['lyrics']
        #attempted_ = request.form['']
        
        result = get_Sentiment_Polarity(lyrics)
    
        return jsonify(result)






@app.route("/about")
def about():
    return render_template("about.html")







if __name__ == "__main__":
    app.run(debug=True)
