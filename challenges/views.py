from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string



monthly_challenges = {
    "january": "This month is January!",
    "february": "This month is February!",
    "march": "This month is March!",
    "april": "This month is April!",
    "may": "This month is May!",
    "june": "This month is June!",
    "july": "This month is July!",
    "august": "This month is August!",
    "September": "This month is Septmember!",
    "October": "This month is October!",
    "November": "This month is November!",
    "December": None

}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
    

def monthly_challenges_by_numbers(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenges_text,
            "month_name": month
        })
    except:
        # respnose_data = render_to_string("404.html")
        # return HttpResponseNotFound(respnose_data)
        raise Http404()
    



























    
