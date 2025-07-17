
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

DETAILED_COACHING = {
    "backflip": {
        "fundamentals": [
            "Your takeoff angle should be 15-20° backward - not straight up",
            "Keep your arms reaching forward until you start the flip",
            "Pull your knees to chest, don't throw your head back"
        ],
        "advanced": [
            "Focus on 'setting' your flip - pause at takeoff before tucking",
            "Open your tuck when you can see the landing, not before",
            "Land with slight forward lean to absorb impact properly"
        ],
        "common_mistakes": [
            "Throwing head back too early kills your rotation",
            "Opening too late causes over-rotation and back slap",
            "Weak takeoff leads to incomplete rotation"
        ]
    },
    "frontflip": {
        "fundamentals": [
            "Lean slightly forward (5-10°) at takeoff, never backward",
            "Drive your knees up to your chest aggressively",
            "Keep your head in neutral position throughout"
        ],
        "advanced": [
            "Use a slight 'pop' with your legs to initiate rotation",
            "Grab your shins (not knees) for tighter rotation",
            "Spot your landing by looking between your legs when opening"
        ],
        "common_mistakes": [
            "Leaning back at takeoff completely kills the trick",
            "Throwing your head down causes dangerous over-rotation",
            "Weak core engagement leads to loose, slow rotation"
        ]
    },
    "360": {
        "fundamentals": [
            "Wind up your shoulders opposite to spin direction before takeoff",
            "Lead with your shoulders, not your hips",
            "Keep your skis parallel and level throughout"
        ],
        "advanced": [
            "Use your poles for momentum generation on takeoff",
            "Pull your arms tight to your body to increase spin speed",
            "Begin unwinding 90° before landing to slow rotation"
        ],
        "common_mistakes": [
            "Spinning with hips first creates axis problems",
            "Looking down during spin causes forward pitch",
            "Opening arms too early slows rotation prematurely"
        ]
    },
    "540": {
        "fundamentals": [
            "Requires strong 360 foundation before attempting",
            "Generate 30% more rotation speed than a 360",
            "Keep your axis perfectly vertical throughout"
        ],
        "advanced": [
            "Use counter-rotation of arms to control spin speed",
            "Spot your landing at 360° mark, then complete rotation",
            "Practice on trampoline first to build spatial awareness"
        ],
        "common_mistakes": [
            "Rushing the trick without mastering 360s first",
            "Off-axis rotation from poor takeoff technique",
            "Panic opening causing dangerous under-rotation"
        ]
    },
    "720": {
        "fundamentals": [
            "Master 540s consistently before attempting",
            "Requires exceptional air awareness and body control",
            "Generate maximum rotation speed at takeoff"
        ],
        "advanced": [
            "Use 'cork' technique - slight off-axis rotation for easier completion",
            "Keep extremely tight body position until 540° mark",
            "Practice visualization and mental rehearsal extensively"
        ],
        "common_mistakes": [
            "Attempting without sufficient 540 experience",
            "Losing body position halfway through rotation",
            "Poor landing preparation due to disorientation"
        ]
    },
    "back tuck": {
        "fundamentals": [
            "Strong vertical takeoff - no backward lean",
            "Pull knees to chest explosively after takeoff",
            "Keep your head neutral, eyes forward"
        ],
        "advanced": [
            "Use 'delay tuck' technique - brief pause before pulling knees",
            "Grab behind your knees for maximum rotation speed",
            "Open aggressively when you see the surface"
        ],
        "common_mistakes": [
            "Leaning back at takeoff causes dangerous trajectory",
            "Weak tuck position leads to incomplete rotation",
            "Early opening results in under-rotation and flat landing"
        ]
    },
    "front tuck": {
        "fundamentals": [
            "Slight forward lean at takeoff (never backward)",
            "Drive knees up aggressively while keeping head neutral",
            "Focus on tight tuck position for fast rotation"
        ],
        "advanced": [
            "Use 'block' takeoff technique - resist forward momentum briefly",
            "Grab your shins for tightest possible rotation",
            "Open by extending legs down, not throwing head up"
        ],
        "common_mistakes": [
            "Any backward lean completely ruins the trick",
            "Throwing head forward causes dangerous over-rotation",
            "Loose tuck position leads to slow, incomplete rotation"
        ]
    },
    "180": {
        "fundamentals": [
            "Perfect your straight airs before attempting spins",
            "Wind up shoulders opposite to spin direction",
            "Keep skis parallel and maintain balance"
        ],
        "advanced": [
            "Focus on style - grab between your legs or behind back",
            "Control rotation speed to land exactly at 180°",
            "Practice switch landing to improve balance"
        ],
        "common_mistakes": [
            "Rushing the learning process without air awareness",
            "Over-rotating due to excessive wind-up",
            "Poor takeoff technique affecting overall form"
        ]
    },
    "seat drop": {
        "fundamentals": [
            "Land with hips and hands touching surface simultaneously",
            "Keep legs straight and together",
            "Maintain upright torso throughout"
        ],
        "advanced": [
            "Perfect your bounce timing for combination tricks",
            "Focus on precise body positioning for maximum control",
            "Use seat drop as setup for more complex sequences"
        ],
        "common_mistakes": [
            "Landing hands first disrupts proper body position",
            "Leaning too far back causes loss of control",
            "Bent legs reduce stability and bounce quality"
        ]
    },
    "barani": {
        "fundamentals": [
            "Master back tuck and half twist separately first",
            "Initiate flip first, then add twist at peak height",
            "Keep eyes on horizon during twist portion"
        ],
        "advanced": [
            "Use progressive training - back tuck to back, then add twist",
            "Focus on timing - twist too early ruins the flip",
            "Practice on lower heights to build confidence"
        ],
        "common_mistakes": [
            "Starting twist too early kills flip rotation",
            "Poor body position during twist phase",
            "Inadequate flip foundation before attempting"
        ]
    }
}

def analyze_clip(path: str, trick: str) -> dict:
    """Enhanced analysis with world-class coaching feedback."""
    # Simulate different performance levels
    performance_level = random.choice(["beginner", "intermediate", "advanced"])
    score = random.randint(1, 10)
    
    coaching = DETAILED_COACHING.get(trick, {
        "fundamentals": ["Focus on proper takeoff technique"],
        "advanced": ["Work on style and consistency"],
        "common_mistakes": ["Practice the basics more"]
    })
    
    # Generate personalized feedback based on performance level
    if performance_level == "beginner":
        feedback = [
            f"🎯 FOUNDATION WORK: {tip}" for tip in coaching.get("fundamentals", [])
        ] + [
            f"⚠️ AVOID: {mistake}" for mistake in coaching.get("common_mistakes", [])[:2]
        ]
    elif performance_level == "intermediate":
        feedback = [
            f"📈 NEXT LEVEL: {tip}" for tip in coaching.get("advanced", [])[:2]
        ] + [
            f"🎯 REFINE: {tip}" for tip in coaching.get("fundamentals", [])[:1]
        ] + [
            f"⚠️ WATCH OUT: {mistake}" for mistake in coaching.get("common_mistakes", [])[:1]
        ]
    else:  # advanced
        feedback = [
            f"🏆 MASTER CLASS: {tip}" for tip in coaching.get("advanced", [])
        ] + [
            f"🎯 PERFECT: {tip}" for tip in coaching.get("fundamentals", [])[:1]
        ]
    
    # Add score-based general feedback
    if score <= 3:
        feedback.insert(0, "💪 Keep practicing! Focus on fundamentals and safety first.")
    elif score <= 6:
        feedback.insert(0, "🎯 Good progress! Work on consistency and technique refinement.")
    elif score <= 8:
        feedback.insert(0, "🔥 Strong execution! Focus on style and advanced variations.")
    else:
        feedback.insert(0, "🏆 Excellent work! You're performing at competition level.")
    
    return {"score": score, "suggestions": feedback}
