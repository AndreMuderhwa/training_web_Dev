from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . models import * 

# Create your views here.

@login_required
def home_view(request):
    return render(request,'inscription/inscription_page.html')

def save_etudiant(request):
    if request.method=="POST":
        n=request.POST.get('nom')
        pst=request.POST.get('postnom')
        prn=request.POST.get('prenom')
        sx=request.POST.get('sexe')
        img=request.FILES.get('image')
        if n and pst and prn and sx and img:
            data={
                "nom":n,
                "postnom":pst,
                "prenom":prn,
                "sexe":sx,
                "image":img
            }
            Etudiant.objects.create(**data) #ORM
            return redirect('list-etudiant')
    return redirect("home-view")
    
def list_etudiant(request):
    qs=Etudiant.objects.all()
    data={
        "listeEtudiant":qs
    }
    return render(request,"inscription/liste.html",context=data)

def update_etudiant(request,pk):
    et=get_object_or_404(Etudiant,id=pk)
    if request.method=='POST':
        n=request.POST.get('nom')
        pst=request.POST.get('postnom')
        prn=request.POST.get('prenom')
        sx=request.POST.get('sexe')
        img=request.FILES.get('image')
        #modification
        et.nom=n
        et.postnom=pst
        et.prenom=prn
        et.sexe=sx
        et.image=img if img is not None else et.image
        et.save()
        return redirect('list-etudiant')

    return render(request,"inscription/modifier_page.html",{"etudiant":et})

# def delete_etudiant(request,id):
#     etu=get_object_or_404(Etudiant,id=id)
#     if request.method=="POST":
#         etu.delete()
#         return redirect('list-etudiant')
#     return render(request,"inscription/delete_page.html",{"etudiant":etu})

def delete_etudiant(request,id):
    etu=get_object_or_404(Etudiant,id=id)
    etu.delete()
    return redirect('list-etudiant')

def save_inscription(request):
    etudiants=Etudiant.objects.all()
    facultes=Faculte.objects.all()
    promotions=Promotion.objects.all()
    data={
        "etudiants":etudiants,
        "facultes":facultes,
        "promotions":promotions
    }
    if request.method=="POST":
        etudiant_id=request.POST.get('etudiant')
        etudiant=get_object_or_404(Etudiant,id=etudiant_id)

        faculte_id=request.POST.get('faculte')
        faculte=get_object_or_404(Faculte, id=faculte_id)

        promotion_id=request.POST.get('promotion')
        promotion=get_object_or_404(Promotion, id=promotion_id)
        ds={
            "refEtudiant":etudiant,
            "refPromotion":promotion,
            "refFaculte":faculte
        }
        Inscription.objects.create(**ds)
        return redirect('list-inscrit')


    return render(request,"inscription/save_insc.html",context=data)

def list_inscrit(request):
    qs=Inscription.objects.select_related('refEtudiant').all()
    return render(request,"inscription/liste_inscrit.html",{"inscrits":qs})

def login_view(request):
    context={}
    if request.method=="POST":
        usn=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(username=usn,password=pwd)
        if user is None:
            context['error']="Mot de passe ou Nom d'utilisateur incorrect !!"
        else:
            login(request,user)
            return redirect('home-view')
    return render(request,"inscription/login_page.html",context=context)
            
def logout_view(request):
    logout(request)
    return redirect('login')