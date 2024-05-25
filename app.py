from flask import Flask, render_template, request

app = Flask(__name__)

def hitung_rata_rata_gula_darah(data_gula_darah):
    if not data_gula_darah:
        return 0

    total_gula_darah = sum(data_gula_darah)
    jumlah_data = len(data_gula_darah)
    rata_rata = total_gula_darah / jumlah_data
    return rata_rata

def tentukan_kategori_diabetes(nilai):
    if nilai < 140:
        return "Normal"
    elif 140 <= nilai < 200:
        return "Pre-diabetes"
    else:
        return "Diabetes"

@app.route('/', methods=['GET', 'POST'])
def index():
    rata_rata = None
    nilai_gula_darah = []
    error = None
    kategori = None

    if request.method == 'POST':
        try:
            nilai_gula_darah = request.form.getlist('nilai_gula_darah')
            nilai_gula_darah = [float(nilai) for nilai in nilai_gula_darah if nilai]
            rata_rata = hitung_rata_rata_gula_darah(nilai_gula_darah)
            kategori = tentukan_kategori_diabetes(rata_rata)
        except ValueError:
            error = "Input tidak valid. Silakan masukkan angka yang benar."

    return render_template('index.html', rata_rata=rata_rata, nilai_gula_darah=nilai_gula_darah, error=error, kategori=kategori)

if __name__ == '__main__':
    app.run(debug=True)
