# Macro script
# Constants
ARCHETYPE_DATA = {
    "power": ("Power", "♣"),
    "control": ("Control", "♦"),
    "support": ("Support", "♥"),
    "special": ("Special", "♠")
}

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

ELEMENT_ICONS = {
    "dark": ":material-moon-waning-gibbous: ",
    "electric": ":material-lightning-bolt: ",
    "fire": ":material-fire: ",
    "ice": ":material-snowflake-variant: ",
    "rude": ":material-skull: ",
    "wind": ":material-weather-windy: ",
    "star": ":material-hexagram: ",
}

# Helper functions
def _create_hover_span(content, tooltip):
    """Create a hover span with tooltip."""
    return f'<span class="hover" hover="{tooltip}">{content}</span>'

def _get_rank_text(rank):
  """Convert rank to star text, handling face cards and numeric ranks."""
  if rank in FACE_CARD_RANKS:
      return f"{FACE_CARD_RANKS[rank]}-Star"
  
  try:
      return f"{int(rank) - 1}-Star"
  except ValueError:
      return None

# Env
def define_env(env):
  @env.macro
  def center(text):
      return f'<div style="text-align: center;">{text}</div>'
  
  @env.macro
  def element(value):
    icon = ELEMENT_ICONS.get(value)
    if icon is None:
        return '<span class="badge">:material-alert-circle: Invalid</span>'
    
    return f'<span class="badge {value}">{icon}{value}</span>'
  
  @env.macro
  def rarity(rarity, rank, archetype):
    rarity_full, rarity_display = RARITY_DATA.get(rarity, ("Unknown", "ERR"))
    archetype_full, archetype_icon = ARCHETYPE_DATA.get(archetype, ("Unknown", "?"))

    text = f"{rarity_display} {rank}{archetype_icon}"
        
    rank_text = _get_rank_text(rank)
    if rank_text is None:
        return _create_hover_span(text, "The dog ate the rating.")
    
    tooltip = f"{rarity_full} {rank_text} {archetype_full}"
    return _create_hover_span(text, tooltip)
