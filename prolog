:- dynamic fact/1.

% ----------- RULES (Knowledge Base) -----------

% Flu
fact(disease(flu)) :-
    fact(fever),
    fact(cough),
    fact(body_ache).

% Cold
fact(disease(cold)) :-
    fact(sneezing),
    fact(runny_nose),
    fact(sore_throat).

% COVID-19
fact(disease(covid19)) :-
    fact(fever),
    fact(cough),
    fact(loss_of_smell).

% Malaria
fact(disease(malaria)) :-
    fact(fever),
    fact(chills),
    fact(sweating).

% ----------- FORWARD CHAINING ENGINE -----------

forward_chain :-
    fact(disease(D)),
    write('Diagnosis: '), write(D), nl, !.

forward_chain :-
    write('No matching disease found.'), nl.

% ----------- USER INPUT -----------

ask(Symptom) :-
    write('Do you have '), write(Symptom), write('? (yes/no): '),
    read(Response),
    Response == yes,
    assert(fact(Symptom)).

% ----------- START SYSTEM -----------

start :-
    ask(fever),
    ask(cough),
    ask(body_ache),
    ask(sneezing),
    ask(runny_nose),
    ask(sore_throat),
    ask(loss_of_smell),
    ask(chills),
    ask(sweating),
    forward_chain.


run: 

?- start.
Do you have fever? yes.
Do you have cough? yes.
Do you have body_ache? yes.

Diagnosis: flu