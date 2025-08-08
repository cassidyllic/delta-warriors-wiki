# Configuration data
TP_TOOLTIPS = {
    "cost": lambda tp_cost: f"Costs {tp_cost}% TP",
    "equal": lambda tp_cost: f"Requires TP exactly at {tp_cost}%",
    "max": lambda tp_cost: "Costs 100% TP (full gauge)",
    "min": lambda tp_cost: f"Requires at least {tp_cost}% TP",
    "vary": lambda tp_cost: "Varying TP costs"
}

RARITY_DATA = {
    "c": ("Common", "<span class='rarity-c'>C</span>"),
    "uc": ("Uncommon", "<span class='rarity-uc'>UC</span>"),
    "r": ("Rare", "<span class='rarity-r'>R</span>"),
    "sr": ("Super Rare", "<span class='rarity-sr'>SR</span>"),
    "ssr": ("Super Special Rare", "<span class='rarity-ssr'>SSR</span>"),
    "lr": ("Legendary Rare", "<span class='rarity-lr'>LR</span>"),
    "xlr": ("Exalted Legendary Rare", "<span class='rarity-xlr'>XLR</span>"),
    "ex": ("Exclusive", "<span class='rarity-ex'>EX</span>")
}

ARCHETYPE_DATA = {
    "club": ("Offense / Power", "♣"),
    "diamond": ("Control / Ranged", "♦"),
    "heart": ("Utility / Support", "♥"),
    "spade": ("Special / Gimmick", "♠")
}

FACE_CARD_RANKS = {"J": 10, "Q": 11, "K": 12, "A": 13}

COST_TYPES = {
    "end": ("Endurance", ":material-chess-rook:", "endurance"),
    "str": ("Strength", ":material-chess-knight:", "strength"),
    "tec": ("Technique", ":material-chess-bishop:", "technique")
}

# Helper functions
def _get_tp_display_and_tooltip(tp_cost, tp_type):
    """Generate TP cost display text and tooltip."""
    if tp_type == "max":
        display_cost = "TP MAX"
    elif tp_type == "equal":
        display_cost = f"TP ≡ {tp_cost}%"
    elif tp_type == "vary":
        display_cost = "TP Δ"
    else:
        display_cost = f"{tp_cost}% TP"
    
    tooltip = TP_TOOLTIPS.get(tp_type, TP_TOOLTIPS["cost"])(tp_cost)
    return display_cost, tooltip

def _get_rank_text(rank):
    """Convert rank to star text, handling face cards and numeric ranks."""
    if rank in FACE_CARD_RANKS:
        return f"{FACE_CARD_RANKS[rank]}-Star"
    
    try:
        return f"{int(rank) - 1}-Star"
    except ValueError:
        return None

def _create_hover_span(content, tooltip):
    """Create a hover span with tooltip."""
    return f'<span class="hover" hover="{tooltip}">{content}</span>'

def define_env(env):
    @env.macro
    def cost(amount, type):
        if type not in COST_TYPES:
            return "Bark! Bark!"

        name, icon, css_class = COST_TYPES[type]
        tooltip = f"Costs {amount} {name} EXP"
        content = f'{icon}{{ .{css_class} }}<span class="{css_class}">{amount}</span>'
        return _create_hover_span(content, tooltip)

    @env.macro
    def rarity(rarity, rank, archetype):
        rarity_full, rarity_display = RARITY_DATA.get(rarity, ("Unknown", "?"))
        archetype_full, archetype_icon = ARCHETYPE_DATA.get(archetype, ("Unknown", "?"))
        
        text = f"{rarity_display} {rank}{archetype_icon}"
        
        rank_text = _get_rank_text(rank)
        if rank_text is None:
            return _create_hover_span(text, "The dog ate the rating.")
        
        tooltip = f"{rarity_full} {rank_text} {archetype_full}"
        return _create_hover_span(text, tooltip)

    @env.macro
    def technique(name, element=None, tags=None, tp_cost=None, tp_type="cost"):
        result = f'<b style="color: var(--md-primary-fg-color)">{name}</b>'
        
        if element:
            result += f' <span class="tag-base elemental {element.lower()}">{element}</span>'
        
        if tags:
            result += ''.join(f' <span class="tag-base tag">{tag}</span>' for tag in tags)
        
        if tp_cost or tp_type in ("max", "vary"):
            display_cost, tooltip = _get_tp_display_and_tooltip(tp_cost, tp_type)
            result += f' <span class="tag-base tp hover" hover="{tooltip}">{display_cost}</span>'
        
        return result + '<br>'
    
    @env.macro
    def center(text):
        return f'<div style="text-align: center;">{text}</div>'
