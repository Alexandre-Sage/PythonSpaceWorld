#!/usr/bin/python3.8
#-*-coding:utf-8-*

from flask import Flask, render_template, redirect, url_for, request

from random import randint

from livereload import server, shell
#######################################################

app=Flask (__name__)

#######################################################

good_answer={"rep1":"Navi", "rep2":"4al", "rep3":"Bleu"}
user_answer={}
selectioned=False
selectioned_for_random={0: {'Nom': 'Nom', 'Prenom': 'Prenom', 'Mail': 'Mail'},1:{"Nom":"Lopez","Prenom":"Armando","Mail":"@"},2:{"Nom" : "Sage", "Prenom":"Alexandre", "Mail":"@"},3:{"Nom":"Hippolyte","Prenom":"Sage", "Mail":"@"}, 4:{"Nom":"Romany","Prenom":"Michelle", "Mail":"@"},5:{"Nom":"Capucine","Prenom":"Sage", "Mail":"@"},6:{"Nom":"Patrick", "Prenom":"Sage", "Mail":"@"}, 7:{"Nom":"Dominique","Prenom":"Sage","Mail":"@"}} #selectioned_for_random test
key=8 # key test
#selectioned_for_random={}
#key=0

#######################################################

@app.route ("/")
def page_acceuil():
    return render_template("index.html")

#######################################################

@app.route("/start", methods=["GET","POST"])
def page_debut():
    global user_answer
    if request.method=="POST":
        formulaire=request.form.to_dict()
        if "navi" in formulaire:
            user_answer["rep1"]="Navi"
            print(user_answer)
        elif "dothraki" in formulaire:
            user_answer["rep1"]="Dothraki"
            print(user_answer)
        else:
            user_answer["rep1"]="Pandoriant"
            print(user_answer)
        return redirect(url_for("page_quest2"))
    return render_template("layout.html", param1=page_debut, user=user_answer)

#######################################################

@app.route("/two", methods=["GET","POST"])
def page_quest2():
    global user_answer
    if request.method=="POST":
        formulaire=request.form.to_dict()
        if "4al" in formulaire:
            user_answer["rep2"]="4al"
            print(user_answer)
        elif "15al" in formulaire:
            user_answer["rep2"]="15al"
            print(user_answer)
        else:
            user_answer["rep2"]="9al"
            print(user_answer)
        return redirect(url_for("page_quest3"))
    return render_template("question2.html", param2=page_quest2, user=user_answer)

#######################################################

@app.route("/three", methods=["GET","POST"])
def page_quest3():
    global user_answer
    global good_answer
    global selectioned
    if request.method=="POST":
        formulaire=request.form.to_dict()
        if "bleu" in formulaire:
            user_answer["rep3"]="Bleu"
            print(user_answer)
        elif "rouge" in formulaire:
            user_answer["rep3"]="Rouge"
            print(user_answer)
        else:
            user_answer["rep3"]="Marron"
            print(user_answer)
        if user_answer["rep1"]==good_answer["rep1"] and user_answer["rep2"]==good_answer["rep2"] and user_answer["rep3"]==good_answer["rep3"]:
            selectioned=True
            print("win")
            return redirect(url_for("page_reg"))
        else:
            return redirect(url_for("page_retry"))
    return render_template("question3.html", param3=page_quest3, user=selectioned)

#######################################################
@app.route("/register", methods=["GET","POST"])
def page_reg():
    global selectioned
    global selectioned_for_random
    global key
    if selectioned==True:
        if request.method=="POST":
            formulaire2=request.form.to_dict()
            if "button_send" in formulaire2:
                coordonees={"Nom":formulaire2["nom"], "Prenom":formulaire2["prenom"], "Mail":formulaire2["mail"]}
                selectioned_for_random[key]=coordonees
                key+=1
                print(selectioned_for_random)
                print(key)
            return redirect(url_for("page_end"))
    return render_template("register.html", param4=page_reg, id=key,  select=selectioned_for_random)

#######################################################

@app.route("/retry", methods=["GET","POST"])
def page_retry():
    return render_template("retry.html", param5=page_retry)

#######################################################

@app.route("/end", methods=["GET","POST"])
def page_end():
    return render_template("end.html", param6=page_end)

#######################################################

@app.route("/admin", methods=["GET","POST"])
def page_admin():
    global selectioned_for_random
    win=False
    wining_number=randint(0,len(selectioned_for_random))
    winner=selectioned_for_random[wining_number]
    print(wining_number)
    print(winner)
    return render_template("admin.html" , param7="page_admin", select=selectioned_for_random, gagnant=winner)





if __name__ == '__main__':
    server = Server(app.wsgi_app)
