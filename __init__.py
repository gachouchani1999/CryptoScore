from flask import Flask, render_template,request, redirect, url_for
import tx_analyzer
import tx_scraper
import ml_algorithm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
   return render_template("home.html")


@app.route('/home')
def return_home():
   return render_template("home.html")


@app.route('/report')
def report_page():
   return render_template("report.html")


@app.route('/API')
def API_page():
   return render_template("API.html")

@app.route('/calculation', methods=['GET', 'POST'])
def calculate_score():
   return render_template('home.html')
   
@app.route('/Results', methods=['GET', 'POST'])
def calculation():
     if request.method=="POST":
      addr = request.form['wallet-address']
      data = tx_scraper.address_scraper(addr)
      all_txs = tx_scraper.tx_extractor(data)
      basic_data = tx_scraper.basic_extractor(data)
      tx_depth2 = tx_scraper.depth2_list(data,all_txs)
      tx_depth3 = tx_scraper.depth3_list(data,tx_depth2)
      g = tx_analyzer.create_Graph(tx_depth3)
      criteria = tx_analyzer.analysis_criteria(g,tx_depth3,basic_data)
      algorithm_pred = ml_algorithm.ml_model(criteria)
      return algorithm_pred
      
      #print ('wallet_address')
      #return render_template("Resluts.html")
if __name__ == '__main__':
   app.debug== True
   app.run()