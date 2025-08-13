# Macro script
# Constants
ARCHETYPE_DATA = {
    "power": ("Power", ":material-cards-club:"),
    "control": ("Control", ":material-cards-diamond:"),
    "support": ("Support", ":material-cards-heart:"),
    "special": ("Special", ":material-cards-spade:")
}
FACE_CARD_NAMES = {"J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}
FACE_CARD_RANKS = {"J": 10, "Q": 11, "K": 12, "A": 13}
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
SOUL_DATA = {
    "darkner": lambda html_class, html_style: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="{html_class}" style="{html_style}"><path d="M12.1,18.55L12,18.65L11.89,18.55C7.14,14.24 4,11.39 4,8.5C4,6.5 5.5,5 7.5,5C9.04,5 10.54,6 11.07,7.36H12.93C13.46,6 14.96,5 16.5,5C18.5,5 20,6.5 20,8.5C20,11.39 16.86,14.24 12.1,18.55M16.5,3C14.76,3 13.09,3.81 12,5.08C10.91,3.81 9.24,3 7.5,3C4.42,3 2,5.41 2,8.5C2,12.27 5.4,15.36 10.55,20.03L12,21.35L13.45,20.03C18.6,15.36 22,12.27 22,8.5C22,5.41 19.58,3 16.5,3Z" fill="currentColor" /></svg>',
    "lightner": lambda html_class, html_style: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="{html_class}" style="{html_style}"><path d="M12,21.35L10.55,20.03C5.4,15.36 2,12.27 2,8.5C2,5.41 4.42,3 7.5,3C9.24,3 10.91,3.81 12,5.08C13.09,3.81 14.76,3 16.5,3C19.58,3 22,5.41 22,8.5C22,12.27 18.6,15.36 13.45,20.03L12,21.35Z" fill="currentColor" /></svg>',
    "soulless": lambda html_class, html_style: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="{html_class}" style="{html_style}"><path d="M12 5C15.87 5 19 8.13 19 12C19 15.87 15.87 19 12 19C8.13 19 5 15.87 5 12C5 8.13 8.13 5 12 5M12 2C17.5 2 22 6.5 22 12C22 17.5 17.5 22 12 22C6.5 22 2 17.5 2 12C2 6.5 6.5 2 12 2M12 4C7.58 4 4 7.58 4 12C4 16.42 7.58 20 12 20C16.42 20 20 16.42 20 12C20 7.58 16.42 4 12 4Z" fill="currentColor" /></svg>'
}
SP_DATA = {
    "endurance": ("Endurance", ":material-chess-rook: "),
    "strength": ("Strength", ":material-chess-knight: "),
    "technique": ("Technique", ":material-chess-bishop: ")
}

# Helper functions
def _create_hover_span(content, tooltip):
    """Create a hover span with tooltip."""
    return f'<span class="title" title="{tooltip}">{content}</span>'

def _get_rank_text(rank):
    """Convert rank to star text, handling face cards and numeric ranks."""
    if rank in FACE_CARD_RANKS:
        return f"{FACE_CARD_RANKS[rank]}-Star"

    try:
        return f"{int(rank) - 1}-Star"
    except ValueError:
        return None

def _format_rank_display(rank):
    """Format rank for display (e.g., 'A' -> 'Ace', '8' -> '8')."""
    if rank in FACE_CARD_NAMES:
        return FACE_CARD_NAMES[rank]
    return rank

# Env
def define_env(env):
    @env.macro
    def rarity(rarity, rank, archetype):
        rarity_full, rarity_display = RARITY_DATA.get(rarity, ("Unknown", "ERR"))
        archetype_full, archetype_icon = ARCHETYPE_DATA.get(archetype, ("Unknown", "?"))
        rank_display = _format_rank_display(rank)
        
        text = f"{rarity_display} {rank_display} of {archetype_icon}"
            
        rank_text = _get_rank_text(rank)
        if rank_text is None:
            return _create_hover_span(text, "The dog ate the rating.")

        tooltip = f"{rarity_full} {rank_text} {archetype_full}-Type"
        return _create_hover_span(text, tooltip)

    @env.macro
    def soul(value, html_class="", html_style=""):
        funct = SOUL_DATA.get(value)
        if funct is None:
            return f'<img src="/delta-warriors-wiki/assets/img/dog.webp" alt="The dog ate the soul." style="{html_style}">'
        
        return funct(html_class, html_style)

    @env.macro
    def sp(value, sp_type):
        name, icon = SP_DATA.get(sp_type)
        text = f'<span class="{sp_type} title" title="Costs {value} {name}">{icon}{value}</span>'

        return text
