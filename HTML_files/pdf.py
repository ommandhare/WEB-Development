from flask import Flask, request, render_template, send_file
import fitz  # PyMuPDF
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/update-pdf', methods=['POST'])
def update_pdf():
    # Retrieve form data
    employee_name = request.form['employee_name']
    employee_number = request.form['employee_number']
    date_joined = request.form['date_joined']
    department = request.form['department']
    designation = request.form['designation']
    basic = request.form['basic']
    hra = request.form['hra']
    lta = request.form['lta']
    city_allowance = request.form['city_allowance']
    gratuity = request.form['gratuity']

    # Open the existing PDF
    pdf_document = fitz.open("DummyEmpSalary (003).pdf")

    # Assuming the data is in a specific location in the PDF, replace the text.
    # Here, we simply iterate over the pages and replace text; you might need more complex handling.
    for page in pdf_document:
        page.replace_text('Ramachandra Dev', employee_name)
        page.replace_text('1', employee_number)
        page.replace_text('31-10-2022', date_joined)
        page.replace_text('Data Engineering', department)
        page.replace_text('Data Engineer', designation)
        page.replace_text('17500', basic)
        page.replace_text('8750', hra)
        page.replace_text('1458', lta)
        page.replace_text('21450', city_allowance)
        page.replace_text('842', gratuity)

    # Save the updated PDF to a bytes buffer
    buffer = io.BytesIO()
    pdf_document.save(buffer)
    pdf_document.close()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="UpdatedPayslip.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
