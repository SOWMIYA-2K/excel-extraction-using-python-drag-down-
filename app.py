import pandas as pd
from flask import Flask

from flask import render_template,request


app = Flask(__name__)

@app.route('/')
def ind():
    return render_template('index.html')

@app.route('/d')
def d():
    gdata = request.args.get('value', '') 
    print(gdata)

    pd.set_option('display.max_rows', None)
    pd.set_option("expand_frame_repr", True)


    data = pd.read_excel (gdata,na_filter=False) 
    df = pd.DataFrame(data)

    df2 = df.iloc[2:,:]


    df2.rename(columns = {'CANNA Continental' : 'Product Reference','Unnamed: 1':'Product Name','Unnamed: 2':'Product Category','Unnamed: 3':'UOM','Unnamed: 4':'Type','Unnamed: 5':'Weight by unit','Unnamed: 6':'Weight by cs','Unnamed: 7':'Unit per cs','Unnamed: 8':'Pieces full pallet'}, inplace = True)

    df2.reset_index(inplace=True, drop=True)
    
    dff=df2.loc[:,['Product Reference','Product Name','Product Category','UOM','Type','Weight by unit','Weight by cs','Unit per cs','Pieces full pallet']]

    return render_template('d.html',dff=dff)


if __name__ == "__main__":

    app.run(debug=True)
