from chatapp.models import QueryDB, IntentDB
from chatapp.forms import QueryForm, IntentForm

import pdb

def insert_query(context):
    result = {}
    error = []    
    # insert intent into intentDB 
    intent_data = {
        "intent" : context["intent"]
    }
    intent_form = IntentForm(intent_data)
    if intent_form.is_valid():
        intent_obj = intent_form.save(commit=True)
        result["is_intent_inserted"] = True
        
    if intent_form.errors:
        intent_obj = IntentDB.objects.filter(intent = context["intent"]).first()
        result["is_intent_inserted"] = False    
        error.append(intent_form.errors)
    # query + intent into intentDB
    query_data = {
        "query" : context["query"],
        "intent" : intent_obj
    }
    query_form = QueryForm(query_data)
    if query_form.is_valid():
        query_form.save(commit=True)
        result["is_query_inserted"] = True
    if query_form.errors:
        result["is_query_inserted"] = False    
        error.append(query_form.errors)
    return result, error

def retrieve_all_intent(context):
    result = {}
    error = []    
    # retrieve all data from intent db
    intents = []
    intent_obj = IntentDB.objects.all()
    for intent in intent_obj:
        intents.append(intent.intent)
    result["intent"] = intents
    return result, error