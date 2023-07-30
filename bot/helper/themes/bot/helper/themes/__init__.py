from random import choice as rchoice
from bot import config_dict, LOGGER
from bot.helper.themes import skull_theme

AVL_THEMES = {'skull': skull_theme}

def BotTheme(var_name, **format_vars):
    theme_ = config_dict['BOT_THEME']

    if theme_ in AVL_THEMES:
        text = getattr(AVL_THEMES[theme_].SKULL(), var_name)
    elif theme_ == 'random':
        rantheme = rchoice(list(AVL_THEMES.values()))
        LOGGER.info(f"Random Theme Chosen: {rantheme}")
        text = getattr(rantheme.SKULL(), var_name)
    else:
        text = getattr(skull_theme.SKULL(), var_name)

    formatted_text = text.format_map(format_vars)
    return formatted_tex
