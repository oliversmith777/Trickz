
import random

TRICKS = [
    # Ski spins
    "straight air", "180", "360", "540", "720", "900", "1080",
    # Ski flips
    "backflip", "frontflip", "cork 720", "bio 540", "misty 540",
    # Trampoline basics
    "seat drop", "front drop", "back drop", "back tuck", "front tuck",
    "barani", "full twist", "double back", "double front"
]

TRICK_TIPS = {
    "backflip": [
        "Set higher before you tuck.",
        "Open earlier to spot your landing."
    ],
    "360": [
        "Lead with your shoulders.",
        "Keep skis level in the air."
    ],
    "seat drop": [
        "Land with hips and hands at the same time.",
        "Keep your core tight to avoid bouncing off-axis."
    ],
    "frontflip": [
        "Commit fully to the rotation.",
        "Keep your head neutral during the flip."
    ],
    "180": [
        "Wind up your shoulders more.",
        "Look where you want to land."
    ],
    "540": [
        "Start the spin early in your takeoff.",
        "Use your arms to generate rotation."
    ],
    "720": [
        "Keep your core tight throughout.",
        "Spot your landing on the second rotation."
    ],
    "back tuck": [
        "Drive your knees to your chest.",
        "Keep your head neutral until opening."
    ],
    "front tuck": [
        "Lean slightly forward on takeoff.",
        "Pull your knees up, don't throw your head down."
    ],
    "barani": [
        "Initiate the flip first, then the twist.",
        "Keep your eyes on the horizon during the twist."
    ],
    "full twist": [
        "Use your arms to drive the twist.",
        "Keep your body straight and tight."
    ]
}

def analyze_clip(path: str, trick: str) -> dict:
    """Very simple placeholder.  
    Returns a fake score and canned suggestions based on trick name."""
    score = random.randint(1, 10)          # new 1-10 scale
    tips = TRICK_TIPS.get(trick, ["Nice work!"])
    return {"score": score, "suggestions": tips}
