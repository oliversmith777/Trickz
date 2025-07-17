
# analysis.py  
import random  

def analyze_clip(path: str, trick: str) -> dict:  
    """Very simple placeholder.  
    Returns a fake score and canned suggestions based on trick name."""  
    score = random.randint(60, 95)  
    tips = {  
        "backflip": [  
            "Set higher before you tuck.",  
            "Open earlier to spot your landing."
        ],  
        "frontflip": [
            "Commit fully to the rotation.",
            "Keep your head neutral during the flip."
        ],
        "360": [
            "Lead with your shoulders.", 
            "Keep skis level in the air."
        ],
        "180": [
            "Wind up your shoulders more.",
            "Look where you want to land."
        ]
    }  
    return {"score": score, "suggestions": tips.get(trick, ["Nice work!"])}
