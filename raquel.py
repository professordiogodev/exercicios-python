from game import attack

def raquel_attack(origin, target):
    attack(origin, target)
    origin["hp"] += 1
    if origin["hp"] > origin["max_hp"]:
        origin["hp"] = origin["max_hp"]
    print(f"{origin['name']} curou-se 1 HP")

     # Habilidade da Raquel - Curar-se 1 ponto de vida a cada ataque

def raquel_heal(origin):
    origin["hp"] += 5
    if origin["hp"] > origin["max_hp"]:
        origin["hp"] = origin["max_hp"]
    print(f"{origin['name']} curou-se 5 HP")

def raquel_spell(origin, target):
    print("Raquel lançou um Spell!")
    target["hp"] -= 8
    if target["hp"] < 0:
        target["hp"] = 0

raquel = {
    "name": "Raquel",
    "hp": 50,
    "max_hp": 50,
    "attack": 4,
    "max_attack": 4,
    "gold": 0,
    "nivel": 1,
    "xp": 0,
    "attack_logic": raquel_attack,
    "heal": raquel_heal,
    "spell": raquel_spell
}