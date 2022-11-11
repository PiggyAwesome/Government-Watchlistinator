import webbrowser
import time


deafult_terms = [
    "Anarchist Cookbook", "Anarchist Cookbook pdf", "https://cdn.preterhuman.net/texts/terrorism_and_pyrotechnics/explosives/MISC/Anarchist%20Cookbook%20-%20William%20Powell.pdf",
    "How to make a pipe bomb", "https://www.vanderbilt.edu/physicsdemonstration/davesdemos/demonstrations/demo100.htm", "https://onlinelibrary.wiley.com/doi/10.1111/1556-4029.12294", 
    "how to get high", "what drugs can make you high",
    "what mushrooms can make you high?", "psilocybin mushrooms", "where can i buy psilocybin mushrooms?", "https://www.24high.com/en/MUSHROOMS", "https://www.24high.com/en/MUSHROOMS/42--Top-10-Mushrooms/",
    "where can i buy weed?", "best types of weed", "white widow weed",
    "crystal meth", "crystal meth sell prices", "how to cook meth", "easy way to cook meth",
    "cocaine", "cocaine price", "how to make cocaine", "https://sunrisehouse.com/cocaine-addiction-treatment/how-made/", "coca leaves", "where can i buy coca plant seeds?", "https://www.amazon.com/Coca-Plant-Seeds/s?k=Coca+Plant+Seeds", "https://www.etsy.com/ie/market/coca_seeds",
    "easy way to kill someone", "strongest poison", "most dangerous poison", "https://theconversation.com/handle-with-care-the-worlds-five-deadliest-poisons-56089",
    "ricin", "how to make ricin", "https://emergency.cdc.gov/agent/ricin/facts.asp#:~:text=Ricin%20can%20be%20made%20from,centigrade%20(176%20degrees%20Fahrenheit).", "how to make castor oil at home", "https://www.jotscroll.com/castor-oil-how-make-castor-oil-home", "where can i buy castor beans?", "https://www.amazon.com/Castor-Beans/s?k=Castor+Beans",
    "TATP", "How to make TATP", "https://www.dni.gov/files/NCTC/documents/jcat/firstresponderstoolbox/78--NCTC-DHS-FBI---Triacetone-Triperoxide-(TATP)-.pdf",
    "Most deadly nerve agents", "a laboratory history of chemical warfare agents", "a laboratory history of chemical warfare agents pdf"]

class Searcher:
    def __init__(self, terms=[], include_deafult=True):
        if include_deafult == True:
            self.terms = terms + deafult_terms
        else:
            self.terms = terms

    def search(self):
        for x in self.terms:
            if "http" in x:
                webbrowser.open_new_tab(x)
            else:
                webbrowser.open("https://www.google.com/search?q=" + x)


