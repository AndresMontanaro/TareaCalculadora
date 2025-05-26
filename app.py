from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    resultado = ''
    valor1 = ''
    operacion = ''
    if request.method == 'POST':
        resultado = request.form.get('resultado', '')
        valor1 = request.form.get('valor1', '')
        operacion = request.form.get('operacion', '')

        if 'n0' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '0'
        elif 'n1' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '1'
        elif 'n2' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '2'
        elif 'n3' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '3'
        elif 'n4' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '4'
        elif 'n5' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '5'
        elif 'n6' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '6'
        elif 'n7' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '7'
        elif 'n8' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '8'
        elif 'n9' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and '²' not in resultado:
                resultado += '9'
        elif 'nclear' in request.form:
            resultado = ''
            valor1 = ''
            operacion = ''
        elif 'nmas' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and not operacion:
                valor1 = resultado
                resultado = ''
                operacion = '+'
        elif 'nmenos' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and not operacion:
                valor1 = resultado
                resultado = ''
                operacion = '-'
        elif 'nmultiplicacion' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and not operacion:
                valor1 = resultado
                resultado = ''
                operacion = '*'
        elif 'ndivision' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and not operacion:
                valor1 = resultado
                resultado = ''
                operacion = '/'
        elif 'nraizcuadrada' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and not resultado and not operacion:
                resultado += '√'
                operacion = '√'
        elif 'npotencia2' in request.form:
            if (resultado != 'Error' and resultado != 'Indivisible entre 0') and resultado and not operacion:
                if '²' not in resultado:
                    valor1 = resultado
                    resultado += '²'
                    operacion = '**2'      
        elif 'nigual' in request.form:
            if resultado != 'Error' and resultado != 'Indivisible entre 0':
                if operacion == '+' and valor1 != '':
                    try:
                        if valor1.isdigit():
                            total = int(valor1) + int(resultado)
                        else:
                            total = float(valor1) + int(resultado)

                        if str(total)[-2:] == '.0':
                            resultado = str(int(total))
                        else:
                            resultado = str(total)

                        valor1 = ''
                        operacion = ''
                    except:
                        resultado = "Error"
                if operacion == '-' and valor1 != '':
                    try:
                        if valor1.isdigit():
                            total = int(valor1) - int(resultado)
                        else:
                            total = float(valor1) - int(resultado)

                        if str(total)[-2:] == '.0':
                            resultado = str(int(total))
                        else:
                            resultado = str(total)

                        valor1 = ''
                        operacion = ''
                    except:
                        resultado = 'Error'
                if operacion == '*' and valor1 != '':
                    try:
                        if valor1.isdigit():
                            total = int(valor1) * int(resultado)
                        else:
                            total = float(valor1) * int(resultado)

                        if str(total)[-2:] == '.0':
                            resultado = str(int(total))
                        else:
                            resultado = str(total)       

                        valor1 = ''
                        operacion = ''
                    except:
                        resultado = 'Error'
                if operacion == '/' and valor1 != '':
                    try:
                        if valor1.isdigit():
                            total = int(valor1) / int(resultado)
                        else:
                            total = float(valor1) / int(resultado)

                        if str(total)[-2:] == '.0':
                            resultado = str(int(total))
                        else:
                            resultado = str(total)

                        valor1 = ''
                        operacion = ''
                    except ZeroDivisionError:
                        resultado = 'Indivisible entre 0'
                    except:
                        resultado = 'Error'
                if operacion == '√':
                    try:
                        total = math.sqrt(float(resultado[1:]))
                        
                        if str(total)[-2:] == '.0':
                            resultado = str(int(total))
                        else:
                            resultado = str(total)

                        valor1 = ''
                        operacion = ''
                    except:
                        resultado = 'Error'
                if operacion == '**2' and valor1 != '':
                    try:
                        if valor1.isdigit():
                            total = int(valor1) ** 2
                        else:
                            total = float(valor1) ** 2

                        if str(total)[-2:] == '.0':
                            resultado = str(int(total))
                        else:
                            resultado = str(total)

                        valor1 = ''
                        operacion = ''
                    except:
                        resultado = 'Error'

    return render_template('inicio.html', resultado=resultado, valor1=valor1, operacion=operacion)

if __name__ == '__main__':
    app.run(debug=True)
