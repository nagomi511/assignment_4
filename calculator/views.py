from django.shortcuts import render
from .forms import InputForm
import math, socket

def calculator_view(request):
    result = None
    error = None
    server = socket.gethostname()

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            # 条件分岐
            if c < 0:
                error = "c is negative."
            else:
                c3 = c ** 3
                root = math.sqrt(c3)

                if c3 > 1000:
                    temp = root * 10
                else:
                    if a == 0:
                        error = "Division by zero (a=0)."
                    else:
                        temp = root / a

                if error is None:
                    result = temp + b
        else:
            error = "Please enter numeric values."
    else:
        form = InputForm()

    return render(request, "calculator/result.html", {
        "form": form,
        "result": result,
        "error": error,
        "server": server,
    })
